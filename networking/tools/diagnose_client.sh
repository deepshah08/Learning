#!/usr/bin/env bash
# ==============================================================================
# LAN Client Diagnostic & RF Health Profiler
# ==============================================================================
# Scope: Automated diagnostics for Wi-Fi/Ethernet clients across Pi 5 (Primary)
#        and UGREEN NAS (Secondary Standby).
#
# Usage:
#   ./diagnose_client.sh [IP_OR_HOSTNAME]
#   Example: ./diagnose_client.sh 192.168.1.98
# ==============================================================================

set -euo pipefail

TARGET_IP="${1:-192.168.1.98}"
PI_HOST="pi5"
NAS_HOST="nas"

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

echo -e "${BOLD}${CYAN}======================================================================${NC}"
echo -e "${BOLD}${CYAN}   🛡️  HOMELAB LAN CLIENT & RF HEALTH DIAGNOSTIC SUITE${NC}"
echo -e "${BOLD}${CYAN}======================================================================${NC}"
echo -e "Target IP: ${BOLD}${YELLOW}${TARGET_IP}${NC}"
echo -e "Primary Node: ${BOLD}Raspberry Pi 5 (192.168.1.92)${NC} | Secondary: ${BOLD}UGREEN NAS (192.168.1.80)${NC}"
echo ""

# ------------------------------------------------------------------------------
# 1. LAYER 2 ARP & HARDWARE MAC AUDIT
# ------------------------------------------------------------------------------
echo -e "${BOLD}${BLUE}[1/5] Probing Layer 2 ARP Neighbor State on Pi 5...${NC}"
ARP_ENTRY=$(ssh -o ConnectTimeout=5 "${PI_HOST}" "ip neigh show | grep -E '${TARGET_IP}' || true")

if [ -z "${ARP_ENTRY}" ]; then
    echo -e "  ${YELLOW}⚠️  No ARP entry found for ${TARGET_IP}. Performing arping discovery...${NC}"
    ssh "${PI_HOST}" "sudo arping -c 2 -I eth0 ${TARGET_IP} >/dev/null 2>&1 || true"
    ARP_ENTRY=$(ssh "${PI_HOST}" "ip neigh show | grep -E '${TARGET_IP}' || true")
fi

if [ -n "${ARP_ENTRY}" ]; then
    echo -e "  ${GREEN}✓ ARP Neighbor Detected:${NC} ${ARP_ENTRY}"
    CLIENT_MAC=$(echo "${ARP_ENTRY}" | awk '{print $5}')
else
    echo -e "  ${RED}✗ Device unresolvable on Layer 2 broadcast domain.${NC}"
    CLIENT_MAC=""
fi
echo ""

# ------------------------------------------------------------------------------
# 2. DHCP LEASE & ACTIVE RESERVATION CHECK
# ------------------------------------------------------------------------------
echo -e "${BOLD}${BLUE}[2/5] Inspecting DHCP Leases & Static Reservations...${NC}"
PI_LEASE=$(ssh "${PI_HOST}" "sudo cat /etc/pihole/dhcp.leases 2>/dev/null | grep -E '${TARGET_IP}' || true")
PI_STATIC=$(ssh "${PI_HOST}" "cat /etc/dnsmasq.d/99-static-reservations.conf 2>/dev/null | grep -E '${TARGET_IP}' || true")
NAS_STATIC=$(ssh "${NAS_HOST}" "cat /volume2/docker/dhcp_server/dnsmasq.conf 2>/dev/null | grep -E '${TARGET_IP}' || true")

if [ -n "${PI_LEASE}" ]; then
    echo -e "  ${GREEN}✓ Active Lease on Primary Pi 5:${NC} ${PI_LEASE}"
else
    echo -e "  ${YELLOW}⚠️  No active dynamic lease found in Pi 5 lease table (normal if static or pending renewal).${NC}"
fi

if [ -n "${PI_STATIC}" ]; then
    echo -e "  ${GREEN}✓ Primary Static Reservation:${NC} ${PI_STATIC}"
fi

if [ -n "${NAS_STATIC}" ]; then
    echo -e "  ${RED}🚨 WARNING: Static reservation also present on NAS Standby Server!${NC}"
    echo -e "     Entry: ${NAS_STATIC}"
    echo -e "     ${YELLOW}Risk: Causes cross-server DHCPOFFER races and 'wrong server-ID' DHCPNAKs.${NC}"
else
    echo -e "  ${GREEN}✓ NAS Standby Clean:${NC} No duplicate static reservation on secondary server."
fi
echo ""

# ------------------------------------------------------------------------------
# 3. CROSS-SERVER DHCP TRANSACTION & NAK AUDIT
# ------------------------------------------------------------------------------
echo -e "${BOLD}${BLUE}[3/5] Auditing Recent DHCP Transactions for Conflicts...${NC}"
SEARCH_KEY="${TARGET_IP}"
if [ -n "${CLIENT_MAC}" ]; then
    SEARCH_KEY="${TARGET_IP}|${CLIENT_MAC}"
fi

RECENT_NAKS=$(ssh "${PI_HOST}" "sudo grep -E '(${SEARCH_KEY})' /var/log/pihole/pihole.log 2>/dev/null | grep -i 'DHCPNAK' | tail -n 5 || true")

if [ -n "${RECENT_NAKS}" ]; then
    echo -e "  ${RED}🚨 Detected Recent DHCPNAK Rejections on Primary Node:${NC}"
    echo "${RECENT_NAKS}" | sed 's/^/     /'
    echo -e "  ${YELLOW}➔ Diagnosis: Client requested IP with wrong server-ID or experienced offer race.${NC}"
else
    echo -e "  ${GREEN}✓ Zero DHCPNAKs detected${NC} in recent logs for target."
fi
echo ""

# ------------------------------------------------------------------------------
# 4. ICMP LATENCY, JITTER & DTIM POWER-SAVE PROFILING
# ------------------------------------------------------------------------------
echo -e "${BOLD}${BLUE}[4/5] Running 15-Packet Latency, Jitter & DTIM Power-Save Profiler...${NC}"
PING_OUTPUT=$(ssh "${PI_HOST}" "ping -c 15 -W 1 ${TARGET_IP} 2>&1 || true")

if echo "${PING_OUTPUT}" | grep -q "100% packet loss"; then
    echo -e "  ${RED}✗ 100% Packet Loss! Device is offline or blocking ICMP.${NC}"
else
    STATS_LINE=$(echo "${PING_OUTPUT}" | grep -E "rtt min/avg/max/mdev" || true)
    PKT_STATS=$(echo "${PING_OUTPUT}" | grep -E "packets transmitted" || true)
    
    echo -e "  ${CYAN}Packet Statistics:${NC} ${PKT_STATS}"
    if [ -n "${STATS_LINE}" ]; then
        echo -e "  ${CYAN}Timing Metrics:${NC}    ${STATS_LINE}"
        
        AVG_RTT=$(echo "${STATS_LINE}" | awk -F'/' '{print $5}' | cut -d'.' -f1)
        MAX_RTT=$(echo "${STATS_LINE}" | awk -F'/' '{print $6}' | cut -d'.' -f1)
        MDEV=$(echo "${STATS_LINE}" | awk -F'/' '{print $7}' | awk '{print $1}' | cut -d'.' -f1)
        
        # Analyze Profile
        if [ "${AVG_RTT}" -lt 15 ] && [ "${MAX_RTT}" -lt 50 ]; then
            echo -e "  ${GREEN}✓ EXCELLENT LINK HEALTH:${NC} Sub-15ms wire-speed Wi-Fi / Ethernet performance."
        elif [ "${AVG_RTT}" -lt 50 ] && [ "${MAX_RTT}" -ge 500 ]; then
            echo -e "  ${YELLOW}ℹ️  POWER-SAVE PROFILE DETECTED:${NC} Steady low baseline (~3-10ms) with occasional"
            echo -e "     DTIM sleep spikes (>500ms). Normal 802.11 power saving when device screen is off."
        else
            echo -e "  ${RED}⚠️  HIGH JITTER / RF ATTENUATION:${NC} Average latency elevated (${AVG_RTT}ms)."
            echo -e "     Possible causes: Metal phone case, MagSafe puck desense, or 2.4GHz interference."
        fi
    fi
fi
echo ""

# ------------------------------------------------------------------------------
# 5. DNS ACTIVITY & CAPTIVE PORTAL AUDIT
# ------------------------------------------------------------------------------
echo -e "${BOLD}${BLUE}[5/5] Auditing DNS Query Stream for Captive Portal Probes...${NC}"
RECENT_DNS=$(ssh "${PI_HOST}" "sudo grep 'from ${TARGET_IP}' /var/log/pihole/pihole.log 2>/dev/null | tail -n 8 || true")

if [ -n "${RECENT_DNS}" ]; then
    echo -e "  ${CYAN}Latest DNS Resolutions:${NC}"
    echo "${RECENT_DNS}" | sed 's/^/     /'
    
    CAPTIVE_COUNT=$(echo "${RECENT_DNS}" | grep -c "connectivitycheck.gstatic.com" || true)
    if [ "${CAPTIVE_COUNT}" -gt 2 ]; then
        echo -e "  ${YELLOW}⚠️  Repeated captive portal probes detected (${CAPTIVE_COUNT} in last sample).${NC}"
        echo -e "     Android triggers this when link quality degrades or after Wi-Fi reconnects."
    fi
else
    echo -e "  ${YELLOW}ℹ️  No recent DNS queries logged from ${TARGET_IP}.${NC}"
fi
echo ""

echo -e "${BOLD}${CYAN}======================================================================${NC}"
echo -e "${BOLD}${GREEN}   ✅ Diagnostic Run Complete${NC}"
echo -e "${BOLD}${CYAN}======================================================================${NC}"
