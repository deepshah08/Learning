# 🎯 Master Architectural Prompt for oGPT-6-Astra

> **Copy and paste everything below this line into your prompt window with `oGPT-6-astra`:**

---

```markdown
# 🏛️ System Architecture Prompt: Designing Node IT13-MAX for Exponential Productivity

## 📌 Context & Ground Truth Infrastructure
You are acting as my **Principal Systems Architect, Infrastructure DevOps Lead, and Autonomous AI Engineer**. 

I am commissioning a new powerhouse bare-metal compute node in my established homelab ecosystem: **Node 3 — GEEKOM IT13 Max Mini PC** running **Ubuntu Server 24.04 LTS**.

### My Existing 3-Tier Homelab Fleet:
1. **Node 1: UGREEN DXP2800 NAS (`192.168.1.80`)**:
   - Intel N100 (4C/4T) | 8 GB DDR5 RAM | 2.5GbE Wired LAN.
   - **Storage Tiering**: Hot 4TB WD_BLACK SN850X NVMe SSD (`/volume2`, 2,400 TBW, hosts Docker/Databases) + Cold 10TB Seagate IronWolf CMR HDD (`/volume1`, 0 RPM deep hibernation, hosts Plex/bulk media).
   - **Services**: Plex (Intel QuickSync 4K transcode), *Arr Stack (Radarr, Sonarr, Prowlarr, qBittorrent, Bazarr), Vaultwarden, Homepage, Secondary Pi-hole.
2. **Node 2: Raspberry Pi 5 (`192.168.1.92`)**:
   - Broadcom BCM2712 (4C @ 2.4GHz) | 16 GB LPDDR4X RAM | Wi-Fi 5 + 1GbE.
   - **Services**: Primary Pi-hole v6 FTL (ad-blocking + authoritative DHCP Option 6) + Unbound (port 5335 DNSSEC root recursive), Tailscale subnet router (`192.168.1.0/24`), n8n automation, headless Jules agent worker, and 100 containerized homelab microservices. Attached to an 8TB Seagate SMR cold archive (`/mnt/media-storage`, 15-min spindown).
3. **Pixel 1 Background Syncer & Virtual Digital Twin**:
   - Physical Pixel 1 running Syncthing for lifetime unlimited original-quality Google Photos uploads.
   - Virtual Redroid Pixel 1 twin on NAS NVMe (`port 5555`) for cloud sync validation.
4. **Node 3 (The Focus): GEEKOM IT13 Max Mini PC (`192.168.1.155`)**:
   - **CPU**: Intel Core Ultra 9 185H (16 Cores / 22 Threads: 6 P-Cores up to 5.1 GHz, 8 E-Cores up to 3.8 GHz, 2 Low-Power SoC E-Cores up to 2.5 GHz).
   - **iGPU**: Intel Arc Graphics (8 Xe-Cores, 1024 ALUs, OpenVINO / oneAPI / Level-Zero / SYCL runtime support).
   - **NPU**: Intel AI Boost NPU (dedicated 2-engine neural tile, 11 TOPS INT8 compute, `/dev/accel/accel0` in Linux 6.8).
   - **RAM**: 16 GB DDR5 5600MHz (expandable to 64 GB).
   - **Storage**: 1TB PCIe 4.0 x4 NVMe SSD (~5,000 MB/s).
   - **Networking**: Dual 2.5GbE Intel I226-V LAN + Intel Wi-Fi 7 BE200 (MAC: `f8:cf:52:eb:88:e0`).

---

## 🎯 Master Objective & Deliverable Request

I want you to synthesize this entire ecosystem and design the **Top 5 highest-leverage, concrete architectural systems** for Node IT13-MAX.

### Core Mandates:
1. **Exponential Life Productivity**: Do NOT give me generic toy homelab ideas (e.g. "run an ad-blocker" or "run Plex", which are already in production). Every idea must act as a **force multiplier on my daily productivity, personal knowledge, coding velocity, or life workflow**.
2. **Silicon-Aware Engineering**: Fully exploit the unique Meteor Lake heterogeneous architecture:
   - Route burst compiles, heavy reasoning, or code generation to **P-cores (5.1 GHz)**.
   - Route multi-tenant agent daemons and pipelines to **E-cores**.
   - Route continuous, 24/7 background listening/sensing to **LP E-cores + Intel AI Boost NPU** (near-zero watt draw, zero fan noise).
   - Route INT8/FP16 matrix math and vision/embeddings to the **8 Xe-core Intel Arc iGPU (OpenVINO)**.
3. **Homelab Integration & Zero-Copy Safety**:
   - Respect storage tiering: High-speed caches, SQLite/Postgres/Qdrant vector stores, and model weights go on IT13-MAX's 1TB NVMe.
   - Connect to UGREEN NAS (`192.168.1.80`) over 2.5GbE NFS/SMB for bulk data via zero-copy read-only bind mounts.
   - Connect to Pi 5 (`192.168.1.92`) via n8n webhooks and local DNS.
4. **16 GB RAM Budget Discipline**: Ensure proposed stacks run leanly within the 16 GB DDR5 envelope (or explicitly identify memory limits and trade-offs).

---

## 📋 Required Structure for Each of the Top 5 Proposals:
For each of your 5 design proposals, provide:
1. **Title & Productivity Value Proposition**: What concrete life/work problem does this eliminate?
2. **Architecture & Data Flow Diagram**: (Clean Mermaid flowchart or ASCII showing how IT13-MAX interacts with Mac, NAS, Pi 5, and mobile).
3. **Silicon Execution Mapping**:
   - P-Cores vs E-Cores vs LP Island
   - Arc iGPU (Xe-Cores) offload role
   - Intel AI Boost NPU assignment
   - RAM & NVMe storage budget
4. **Software & Container Stack**: Exact open-source packages, models (e.g. `qwen2.5-coder`, `faster-whisper`, `bge-m3`, `n8n`), runtimes (OpenVINO, vLLM, Ollama), and network ports.
5. **Concrete Daily Workflow Example**: Step-by-step walkthrough of how I interact with this system on a normal Tuesday.

Conclude with your **Recommended Implementation Roadmap (Phase 1 through Phase 5)** indicating which system we should deploy first once bare-metal Ubuntu finishes provisioning.
```
