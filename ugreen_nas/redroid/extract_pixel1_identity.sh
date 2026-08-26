#!/usr/bin/env bash
# ==============================================================================
# Pixel 1 Identity Extraction Script
# Dumps hardware serial, Android ID, build.prop, MAC, and GSF from physical phone
# ==============================================================================
set -euo pipefail

OUTPUT_DIR="$(dirname "$0")"

echo "=== 📱 Waiting for connected Pixel 1 via ADB... ==="
adb wait-for-device

echo "Device connected! Extracting identity..."

cat << 'HEADER' > "$OUTPUT_DIR/pixel1_identity.txt"
# ==============================================================================
# PHYSICAL PIXEL 1 (SAILFISH) EXTRACTED HARDWARE IDENTIFIERS
# ==============================================================================
HEADER

{
    echo "TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')"
    echo "SERIALNO=$(adb get-serialno)"
    echo "MODEL=$(adb shell getprop ro.product.model)"
    echo "DEVICE=$(adb shell getprop ro.product.device)"
    echo "BRAND=$(adb shell getprop ro.product.brand)"
    echo "NAME=$(adb shell getprop ro.product.name)"
    echo "MANUFACTURER=$(adb shell getprop ro.product.manufacturer)"
    echo "BOARD=$(adb shell getprop ro.product.board)"
    echo "PLATFORM=$(adb shell getprop ro.board.platform)"
    echo "BUILD_ID=$(adb shell getprop ro.build.id)"
    echo "BUILD_DISPLAY_ID=$(adb shell getprop ro.build.display.id)"
    echo "BUILD_FINGERPRINT=$(adb shell getprop ro.build.fingerprint)"
    echo "BUILD_VERSION_RELEASE=$(adb shell getprop ro.build.version.release)"
    echo "BUILD_VERSION_SDK=$(adb shell getprop ro.build.version.sdk)"
    echo "BUILD_SECURITY_PATCH=$(adb shell getprop ro.build.version.security_patch)"
    echo "ANDROID_ID=$(adb shell settings get secure android_id)"
    echo "WLAN_MAC=$(adb shell cat /sys/class/net/wlan0/address 2>/dev/null || echo 'N/A')"
} >> "$OUTPUT_DIR/pixel1_identity.txt"

echo "Dumping complete system property tree..."
adb shell getprop > "$OUTPUT_DIR/pixel1_all_props.dump"

echo "=== ✅ Extraction Complete ==="
cat "$OUTPUT_DIR/pixel1_identity.txt"
