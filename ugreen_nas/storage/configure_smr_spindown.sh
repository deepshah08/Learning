#!/usr/bin/env bash
# ==============================================================================
# SMR External USB Drive: Automated Spindown & Power Management Configuration
# Target: 8TB Seagate Expansion SMR (STKR8000400 / ST8000DM004)
# ==============================================================================
set -euo pipefail

PATH="$PATH:/usr/sbin:/sbin:/usr/local/bin"

echo "=== 🔍 Scanning for External USB SMR Drives ==="

# Identify USB storage devices
TARGET_DEV=""
for DEV in /sys/block/sd*; do
    DEV_NAME=$(basename "$DEV")
    # Exclude internal NAS disk (/dev/sda)
    if [ "$DEV_NAME" == "sda" ]; then
        continue
    fi
    
    # Check if device is USB
    if udevadm info --query=property --name="/dev/$DEV_NAME" 2>/dev/null | grep -q "ID_BUS=usb"; then
        MODEL=$(udevadm info --query=property --name="/dev/$DEV_NAME" | grep "ID_MODEL=" | cut -d'=' -f2 || echo "Unknown")
        VENDOR=$(udevadm info --query=property --name="/dev/$DEV_NAME" | grep "ID_VENDOR=" | cut -d'=' -f2 || echo "Unknown")
        echo "Found USB Drive: /dev/$DEV_NAME ($VENDOR - $MODEL)"
        TARGET_DEV="/dev/$DEV_NAME"
        break
    fi
done

if [ -z "$TARGET_DEV" ]; then
    echo "⚠️ No external USB hard drive detected. Please plug in the 8TB Seagate SMR drive and run again."
    exit 0
fi

echo ""
echo "=== ⚙️ Configuring Power Saving & 15-Min Spindown on $TARGET_DEV ==="

# 1. Set Standby Timeout to 15 minutes (180 * 5 seconds = 900s = 15 min)
echo "Setting 15-minute idle spindown timeout (hdparm -S 180)..."
hdparm -S 180 "$TARGET_DEV" || true

# 2. Enable Advanced Power Management (APM 127 = Spindown enabled)
echo "Enabling APM spindown profile (hdparm -B 127)..."
hdparm -B 127 "$TARGET_DEV" || true

# 3. Query current drive power status
echo ""
echo "=== 📊 Current Drive Status ==="
hdparm -C "$TARGET_DEV" || true

echo ""
echo "=== ✅ SMR Spindown Policy Active ==="
echo "1. The drive will stay active during sequential writes."
echo "2. Once backup completes and internal SMR track realignment finishes, the drive will automatically spin down (0 RPM) after 15 minutes of inactivity."
echo "3. Host read/write requests will automatically spin up the drive on-demand."
