#!/usr/bin/env bash
# ==============================================================================
# Automated Daily Media Ingestion Worker for ReDroid Pixel 1
# Governed by Centralized 1GB/day Rate Limiter (with Manual Burst Override)
# Atomic two-phase staging: inbox_staging -> atomic mv to inbox (eliminates races)
# Strictly adheres to Mechanical HDD Safety: Reads from NVMe catalog/queue
# ==============================================================================
set -euo pipefail

SCRIPT_DIR="/volume2/docker/redroid/scripts"
CONFIG_DIR="/volume2/docker/redroid/config"
INBOX_DIR="/volume2/docker/redroid/inbox"
INBOX_STAGING="/volume2/docker/redroid/inbox_staging"
MANIFEST="$SCRIPT_DIR/uploaded_manifest.txt"
LOG_FILE="$SCRIPT_DIR/batch-uploader.log"
LIMITER="$SCRIPT_DIR/rate_limiter.py"
CATALOG_FILE="$CONFIG_DIR/source_catalog.txt"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

touch "$MANIFEST" "$LOG_FILE"
mkdir -p "$INBOX_DIR" "$INBOX_STAGING" "$CONFIG_DIR"

log "=================================================="
log "Starting daily batch uploader run..."

# Check current rate limit status
STATUS_JSON=$(python3 "$LIMITER" status 2>/dev/null || echo "{}")
log "Current Rate Limiter Status: $STATUS_JSON"

# Handle optional CLI override flag
if [ "${1:-}" = "--burst" ] || [ "${1:-}" = "--override" ]; then
    BURST_GB="${2:-10}"
    log "Manual burst flag detected. Enabling override up to ${BURST_GB} GB..."
    python3 "$LIMITER" override enable --ceiling-gb "$BURST_GB" --reason "Manual user burst invocation"
fi

TOTAL_STAGED_BYTES=0
TOTAL_STAGED_COUNT=0

# Hardware Safety Directive: Read target items from static catalog or queue on NVMe
# to prevent open-ended find crawls that wake the 10TB Seagate IronWolf mechanical HDD.
if [ -f "$CATALOG_FILE" ] && [ -s "$CATALOG_FILE" ]; then
    log "Processing items from NVMe catalog: $CATALOG_FILE"
    
    TEMP_CATALOG=$(mktemp)
    cp "$CATALOG_FILE" "$TEMP_CATALOG"
    
    while IFS= read -r FILE || [ -n "$FILE" ]; do
        [ -n "$FILE" ] || continue
        # Strip comments
        [[ "$FILE" =~ ^#.* ]] && continue
        
        [ -f "$FILE" ] || continue
        
        # Check if already processed
        if grep -Fxq "$FILE" "$MANIFEST" 2>/dev/null; then
            continue
        fi
        
        FILESIZE=$(stat -c%s "$FILE" 2>/dev/null || echo 0)
        [ "$FILESIZE" -gt 0 ] || continue
        
        # Check against centralized rate limiter
        if ! python3 "$LIMITER" check "$FILESIZE" >/dev/null 2>&1; then
            log "Rate limiter budget reached for today. Stopping staging."
            break
        fi
        
        FILENAME=$(basename "$FILE")
        STAGE_DEST="$INBOX_STAGING/$FILENAME"
        FINAL_DEST="$INBOX_DIR/$FILENAME"
        
        if [ -f "$FINAL_DEST" ]; then
            FILENAME="$(date +%s)_$FILENAME"
            STAGE_DEST="$INBOX_STAGING/$FILENAME"
            FINAL_DEST="$INBOX_DIR/$FILENAME"
        fi
        
        # Atomic two-phase staging: copy to staging first, then atomic rename
        cp "$FILE" "$STAGE_DEST"
        mv -n "$STAGE_DEST" "$FINAL_DEST"
        
        echo "$FILE" >> "$MANIFEST"
        python3 "$LIMITER" record "$FILESIZE" >/dev/null 2>&1 || true
        
        TOTAL_STAGED_BYTES=$((TOTAL_STAGED_BYTES + FILESIZE))
        TOTAL_STAGED_COUNT=$((TOTAL_STAGED_COUNT + 1))
    done < "$TEMP_CATALOG"
    
    rm -f "$TEMP_CATALOG"
else
    log "Notice: No catalog found at $CATALOG_FILE (or file is empty)."
    log "To queue files without waking the mechanical HDD, append paths to $CATALOG_FILE."
fi

log "Batch staging complete: $TOTAL_STAGED_COUNT files ($((TOTAL_STAGED_BYTES / 1024 / 1024)) MB) moved to inbox."
log "The inotify scanner daemon will now ingest and index these files into ReDroid."
