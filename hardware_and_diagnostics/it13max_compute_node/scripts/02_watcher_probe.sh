#!/usr/bin/env bash
# ==============================================================================
# IT13 Max Network Watcher & Telemetry Probe
# Continuously monitors ICMP ping, SSH (port 22), and RDP (port 3389)
# ==============================================================================

set -euo pipefail

TARGET_IP="192.168.1.155"
TARGET_HOST="it13_max.lan"
INTERVAL=3

echo "========================================================"
echo " Starting Telemetry Watcher for ${TARGET_HOST} (${TARGET_IP})"
echo " Monitoring ICMP, Port 22 (SSH), and Port 3389 (RDP)"
echo " Press Ctrl+C to stop"
echo "========================================================"

LAST_PING_STATE="UNKNOWN"
LAST_SSH_STATE="UNKNOWN"
LAST_RDP_STATE="UNKNOWN"

while true; do
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    
    # 1. ICMP Ping Check
    if ping -c 1 -W 1000 "${TARGET_IP}" >/dev/null 2>&1; then
        PING_STATE="UP"
    else
        PING_STATE="DOWN"
    fi

    # 2. Port 22 (SSH) Check
    if nc -zv -G 1 "${TARGET_IP}" 22 >/dev/null 2>&1; then
        SSH_STATE="OPEN"
    else
        SSH_STATE="CLOSED"
    fi

    # 3. Port 3389 (RDP) Check
    if nc -zv -G 1 "${TARGET_IP}" 3389 >/dev/null 2>&1; then
        RDP_STATE="OPEN"
    else
        RDP_STATE="CLOSED"
    fi

    # Log only on state transitions or heartbeat every 30s
    if [[ "${PING_STATE}" != "${LAST_PING_STATE}" || "${SSH_STATE}" != "${LAST_SSH_STATE}" || "${RDP_STATE}" != "${LAST_RDP_STATE}" ]]; then
        echo "[${TIMESTAMP}] 🔄 STATE CHANGE: Ping=${PING_STATE} | SSH(22)=${SSH_STATE} | RDP(3389)=${RDP_STATE}"
        LAST_PING_STATE="${PING_STATE}"
        LAST_SSH_STATE="${SSH_STATE}"
        LAST_RDP_STATE="${RDP_STATE}"
    fi

    sleep "${INTERVAL}"
done
