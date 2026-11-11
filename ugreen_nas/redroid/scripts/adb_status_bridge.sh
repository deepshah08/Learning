#!/usr/bin/env bash
set -u

DEVICE="192.168.1.80:5555"
NAS_HOST="Deep Shah@192.168.1.80"
STATUS_TARGET="/volume2/docker/redroid/status.txt"
LOG_FILE="/tmp/adb_status_bridge.log"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

log "Starting High-Precision ADB Status Bridge for ReDroid Photos..."

PREV_BYTES=0

while true; do
    CURR_BYTES=$(adb -s "$DEVICE" shell "cat /proc/net/dev 2>/dev/null" | grep eth0 | awk '{print $10}' || echo 0)
    
    if [ "$PREV_BYTES" -gt 0 ] && [ "$CURR_BYTES" -gt 0 ]; then
        DIFF=$((CURR_BYTES - PREV_BYTES))
        RATE_KB=$((DIFF / 1024 / 10))
    else
        RATE_KB=0
    fi
    PREV_BYTES="$CURR_BYTES"
    
    STATUS="IDLE"
    if [ "$RATE_KB" -gt 500 ]; then
        STATUS="Backing up (${RATE_KB} KB/s)"
    else
        DUMP=$(adb -s "$DEVICE" shell "rm -f /sdcard/live_ui.xml && uiautomator dump /sdcard/live_ui.xml >/dev/null 2>&1 && cat /sdcard/live_ui.xml 2>/dev/null" || true)
        if echo "$DUMP" | grep -q "Backup complete"; then
            STATUS="Backup complete"
        elif echo "$DUMP" | grep -q "Backing up"; then
            ITEMS_LEFT=$(echo "$DUMP" | sed 's/>/>\n/g' | grep -o 'content-desc="[^"]*"' | grep -o '[0-9]* items left' | head -n 1 || true)
            if [ -n "$ITEMS_LEFT" ]; then
                STATUS="Backing up ($ITEMS_LEFT)"
            else
                STATUS="Backing up"
            fi
        else
            if [ "$RATE_KB" -gt 50 ]; then
                STATUS="Backing up (${RATE_KB} KB/s)"
            else
                STATUS="IDLE"
            fi
        fi
    fi
    
    ssh -o ControlMaster=auto -o ControlPersist=1h -o BatchMode=yes "$NAS_HOST" "echo '$STATUS' > $STATUS_TARGET" 2>/dev/null || true
    log "Updated status on NAS: $STATUS (TX rate: ${RATE_KB} KB/s, Total TX: $((CURR_BYTES / 1024 / 1024)) MB)"
    
    sleep 10
done
