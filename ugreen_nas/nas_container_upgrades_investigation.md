# NAS Container Upgrades & Host Service Starvation Investigation

> Companion: durable architecture at [./nas_container_upgrades_knowledge.md](./nas_container_upgrades_knowledge.md)
> Date: 2026-10-27 | Status: Resolved | Target: UGREEN DXP2800 NAS (192.168.1.80)

---

## 1. Trigger

Following a multi-host upgrade session across the homelab, 14 Docker container images
were updated and recreated on the UGREEN DXP2800 NAS. Shortly after, the user reported
excessive fan noise, intense mechanical hard drive thrashing, loss of OpenSSH (port 22)
connectivity, failure of the UGOS Pro Web UI (port 9999), and disappearance of the
Antigravity daemon instance.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        INCIDENT TRIGGER TIMELINE                       │
├────────────────────┬───────────────────────────────────────────────────┤
│ Mass Docker Pull   │ 14 containers pulled (Plex, Radarr, Sonarr, etc.) │
│ Container Recreate │ docker compose up -d executed in parallel batches │
│ Library Rescan     │ 5+ media apps initiate concurrent crawls on /vol1 │
│ Hardware Thrash    │ 10TB IronWolf CMR seeks peg I/O; N100 RAM sat     │
│ Host Service Crash │ sshd and UGOS Web UI hang; Docker containers live │
└────────────────────┴───────────────────────────────────────────────────┘
```

---

## 2. Investigation Path

| # | Hypothesis / Approach | What We Found | Outcome |
|---|----------------------|---------------|---------|
| 1 | NAS host is dead or kernel panicked | ICMP ping failed, but Layer 2 ARP was REACHABLE on `192.168.1.80`. | Refuted |
| 2 | Host network interface or cable dropped | Multi-port TCP probe from iT13max revealed 11 Docker ports active. | Refuted |
| 3 | UGOS Security Center IP ban blocked Mac | Probes from Pi 5 and iT13max also timed out on port 22 and 9999. | Refuted |
| 4 | Host sshd & web daemons starved by I/O & OOM | Docker survived; host services on root overlay died under swap thrash. | Confirmed |

---

## 3. Root Causes and Fixes

| # | Component | Root Cause | Fix |
|---|-----------|------------|-----|
| 1 | Media Stack (`arr_stack`, `plex`) | Recreating Plex, Radarr, Sonarr, Bazarr, and Calibre concurrently triggered simultaneous disk scans across the 10TB CMR HDD. | Enforce sequential, isolated stack upgrade waves. |
| 2 | Host Memory & Swap | Intel N100 (8GB RAM) exceeded physical headroom during parallel scans; heavy swap thrashing starved host daemons. | Cap concurrent container upgrades; reboot host via ACPI short press to clear thrashing. |
| 3 | Host Management (`sshd`, UGOS UI) | Host daemons on `/overlay` crashed or dropped listening sockets under memory exhaustion while container runtimes remained isolated. | ACPI power-cycle restores host daemons cleanly. |

---

## 4. Key Telemetry & Evidence

Multi-threaded port scan from `192.168.1.155` (`it13max`) against `192.168.1.80`:

```text
ALL OPEN PORTS (1-10000):
[53, 3000, 5055, 5555, 6767, 6881, 7878, 8080, 8083, 8084, 8085, 8089, 8181, 8989, 9696]
```

### Container Health vs. Host Health Matrix:

| Port | Service | Container State | HTTP Response |
|------|---------|-----------------|---------------|
| 22 | Host OpenSSH | Dead / Starved | Connection timed out |
| 9999 | UGOS Web UI | Dead / Starved | Connection timed out |
| 3000 | Homepage | Healthy | `HTTP/1.1 200 OK` |
| 8080 | qBittorrent | Healthy | `HTTP/1.1 200 OK` |
| 8089 | Pi-hole Web | Healthy | `HTTP/1.1 302 Found` |
| 8085 | Vaultwarden | Healthy | `HTTP/1.1 200 OK` |
| 5055 | Overseerr | Healthy | `HTTP/1.1 307 Redirect` |
| 7878 | Radarr | Healthy | `HTTP/1.1 401 Unauthorized` |
| 8989 | Sonarr | Healthy | `HTTP/1.1 401 Unauthorized` |
| 8181 | Tautulli | Healthy | `HTTP/1.1 303 Redirect` |

---

## 5. Key Learnings

1. **Containers isolate runtimes, not physical hardware resources.** Even though Docker isolated application namespaces, 5 concurrent applications accessing the single mechanical spindle on `/volume1` saturated total disk bandwidth and brought down the host.
2. **Never mass-recreate media stacks on low-power NAS nodes.** The Intel N100 with 8GB RAM must never upgrade Plex and *Arr stacks simultaneously; upgrades must be staged in discrete waves.
3. **Containerized services can outlive host management services.** When memory exhaustion hits UGOS Pro, isolated container daemons survive while the host's interactive management daemons (`sshd`, web server) are dropped by the kernel.
