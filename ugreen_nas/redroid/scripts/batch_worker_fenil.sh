#!/usr/bin/env bash
# ==============================================================================
# Fenil Wedding Ingestion: Resilient Checkpointed Batch Pipeline (Hardened v2)
# - Leverages Pi 5 16GB RAM (/dev/shm) for zero-wear extraction on SMR drive
# - Atomic Two-Phase Ingestion: inbox_staging -> atomic rename to inbox
# - Deterministic SQLite WAL verification (replaces unmaintained status.txt)
# - Robust globbing & shell escaping (handles spaces, parentheses, '&')
# - Exit and signal traps for guaranteed cleanup
# ==============================================================================
set -euo pipefail

DF_DIR="/mnt/media-storage/DF"
TAR_FILE="$DF_DIR/wedding_archive_DF.tar"
TEMP_STAGE="/dev/shm/staging_unpacked"
TEMP_FLAT="/dev/shm/staging_flat"
NAS_HOST="Deep Shah@192.168.1.80"
NAS_STAGING="/volume2/docker/redroid/inbox_staging"
NAS_INBOX="/volume2/docker/redroid/inbox"
STATE_FILE="$DF_DIR/fenil_processed_batches.txt"
LOG_FILE="$DF_DIR/fenil_ingest.log"
LIMITER_PATH="/volume2/docker/redroid/scripts/rate_limiter.py"
VERIFIER_PATH="/volume2/docker/redroid/scripts/verify_backup.py"

log() {
    echo "[$(date "+%Y-%m-%d %H:%M:%S")] $1" | tee -a "$LOG_FILE"
}

cleanup() {
    rm -rf "$TEMP_STAGE" "$TEMP_FLAT"
}
trap cleanup EXIT INT TERM

mkdir -p "$TEMP_STAGE" "$TEMP_FLAT"
touch "$STATE_FILE" "$LOG_FILE"

PHOTO_BATCHES=(
    "DF/Photos/drive-download-20260914T001740Z-1-001.zip"
    "DF/Photos/drive-download-20260914T001740Z-1-002.zip"
    "DF/Photos/drive-download-20260914T001740Z-1-003.zip"
    "DF/Photos/drive-download-20260914T001740Z-1-004.zip"
    "DF/Photos/drive-download-20260914T001740Z-1-005.zip"
    "DF/Photos/drive-download-20260914T001740Z-1-006.zip"
)

wait_for_google_photos() {
    local SAMPLE_FILE="$1"
    log "Waiting for Google Photos in ReDroid to finish uploading batch (verifying $SAMPLE_FILE)..."
    ssh -o BatchMode=yes "$NAS_HOST" "python3 '$VERIFIER_PATH' wait '$SAMPLE_FILE' --timeout 600"
}

process_batch() {
    local ITEM_PATH="$1"
    local ITEM_NAME
    ITEM_NAME=$(basename "$ITEM_PATH")

    if grep -Fxq "$ITEM_NAME" "$STATE_FILE"; then
        log "Skipping already processed batch: $ITEM_NAME"
        return 0
    fi

    log "========================================================"
    log "Processing Batch: $ITEM_NAME"
    log "========================================================"

    # Guaranteed clean slate on RAM disk
    rm -rf "$TEMP_STAGE" "$TEMP_FLAT"
    mkdir -p "$TEMP_STAGE" "$TEMP_FLAT"

    local SAMPLE_VERIFY_FILE=""

    if [[ "$ITEM_NAME" =~ \.zip$ ]]; then
        local EXTRACTED_ZIP="$DF_DIR/$ITEM_PATH"
        if [ ! -f "$EXTRACTED_ZIP" ]; then
            log "Extracting $ITEM_NAME from master TAR on SMR drive..."
            tar -xf "$TAR_FILE" -C "$DF_DIR" "$ITEM_PATH"
        else
            log "Zip already extracted on SMR: $EXTRACTED_ZIP"
        fi

        log "Unzipping $ITEM_NAME into RAM staging (/dev/shm)..."
        unzip -q "$EXTRACTED_ZIP" -d "$TEMP_STAGE"

        log "Flattening media files and filtering AppleDouble files..."
        find "$TEMP_STAGE" -type f ! -name "._*" \( \
            -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o \
            -iname "*.heic" -o -iname "*.dng" -o -iname "*.mp4" -o -iname "*.mov" \
        \) | while read -r PFILE; do
            local BNAME
            BNAME=$(basename "$PFILE")
            local PARENT
            PARENT=$(basename "$(dirname "$PFILE")")
            mv "$PFILE" "$TEMP_FLAT/${PARENT}_${BNAME}"
        done
        rm -rf "$TEMP_STAGE"/*

        local FILE_COUNT
        FILE_COUNT=$(find "$TEMP_FLAT" -maxdepth 1 -type f 2>/dev/null | wc -l)
        local STAGE_SIZE
        STAGE_SIZE=$(du -sh "$TEMP_FLAT" | cut -f1)
        
        # Pick the last file alphabetically as the verification canary
        SAMPLE_VERIFY_FILE=$(find "$TEMP_FLAT" -maxdepth 1 -type f -printf "%f\n" 2>/dev/null | sort | tail -n 1)

        log "Streaming $FILE_COUNT file(s) ($STAGE_SIZE) for $ITEM_NAME into NAS staging..."
        tar -cf - -C "$TEMP_FLAT" . | ssh -o BatchMode=yes "$NAS_HOST" "mkdir -p '$NAS_STAGING' && tar -xf - -C '$NAS_STAGING'"
        rm -rf "$TEMP_FLAT"/*

    elif [[ "$ITEM_NAME" =~ \.mp4$ ]]; then
        local EXTRACTED_MP4="$DF_DIR/$ITEM_PATH"
        if [ ! -f "$EXTRACTED_MP4" ]; then
            log "Extracting video $ITEM_NAME from master TAR on SMR drive..."
            tar -xf "$TAR_FILE" -C "$DF_DIR" "$ITEM_PATH"
        fi
        local MP4_DIR
        MP4_DIR=$(dirname "$EXTRACTED_MP4")
        local MP4_SIZE
        MP4_SIZE=$(ls -lh "$EXTRACTED_MP4" | awk '{print $5}')
        SAMPLE_VERIFY_FILE="$ITEM_NAME"

        log "Streaming video $ITEM_NAME ($MP4_SIZE) directly into NAS staging..."
        tar -cf - -C "$MP4_DIR" "$ITEM_NAME" | ssh -o BatchMode=yes "$NAS_HOST" "mkdir -p '$NAS_STAGING' && tar -xf - -C '$NAS_STAGING'"
    fi

    log "Atomically moving completed files from NAS staging to inbox (safe against '&' and special chars)..."
    ssh -o BatchMode=yes "$NAS_HOST" "find '$NAS_STAGING' -mindepth 1 -maxdepth 1 -exec mv -t '$NAS_INBOX' {} +"

    log "Waiting for NAS inotify daemon to ingest files into ReDroid DCIM..."
    local poll=0
    while true; do
        local INBOX_REMAINING
        INBOX_REMAINING=$(ssh -o BatchMode=yes "$NAS_HOST" "find '$NAS_INBOX' -mindepth 1 -maxdepth 1 -type f 2>/dev/null | wc -l" || echo 0)
        if [ "$INBOX_REMAINING" -eq 0 ]; then
            log "NAS inbox drained to 0. All items ingested into ReDroid!"
            break
        fi
        sleep 5
        ((poll++)) || true
        if [ "$poll" -gt 60 ]; then
            log "Warning: Inbox drain wait reached 5 minutes. Continuing to cloud verification..."
            break
        fi
    done

    if [ -n "$SAMPLE_VERIFY_FILE" ]; then
        wait_for_google_photos "$SAMPLE_VERIFY_FILE"
    fi

    echo "$ITEM_NAME" >> "$STATE_FILE"
    log "Checkpoint committed for $ITEM_NAME."
    log "Cooldown 30s before next batch..."
    sleep 30
}

log "Starting Fenil Wedding checkpointed batch pipeline..."

# Phase 1: Photos
for P_BATCH in "${PHOTO_BATCHES[@]}"; do
    process_batch "$P_BATCH"
done

log "=========================================================="
log "PHOTO BATCHES SUCCESSFULLY PROCESSED AND UPLOADED!"
log "=========================================================="
