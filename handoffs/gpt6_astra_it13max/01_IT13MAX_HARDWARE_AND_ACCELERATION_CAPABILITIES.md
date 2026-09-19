# ⚡ Node 3: GEEKOM IT13 Max Hardware & Acceleration Capabilities

> **Target Node**: `it13max` (`192.168.1.155`)  
> **Role in Homelab**: Unthrottled AI Inference, Continuous Build Automation, & Heavy Distributed Compute

---

## 🔬 1. Processor & Execution Engine: Intel Core Ultra 9 185H (Meteor Lake)

The Intel Core Ultra 9 185H provides an asymmetric 3D high-performance hybrid architecture:
- **Total Cores / Threads**: **16 Cores / 22 Threads**
  - **6 Performance Cores (P-Cores)**: Base 2.3 GHz, Boost up to **5.1 GHz** (AVX2, FMA3, heavy single-threaded & compiling tasks).
  - **8 Efficient Cores (E-Cores)**: Base 1.8 GHz, Boost up to **3.8 GHz** (Multi-tenant microservice execution).
  - **2 Low-Power Island E-Cores (LP E-Cores)**: Located directly on the SoC tile (Base 1.0 GHz, Boost up to **2.5 GHz**) for ultra-low-power background idle listening.
- **Cache**: 24 MB Intel Smart Cache (L3).
- **Base Power (TDP)**: 45W | **Maximum Turbo Power**: 115W.

---

## 🎨 2. Graphics & Neural Acceleration Cores

### A. Intel Arc Graphics (8 Xe-Cores)
- **Architecture**: Intel Xe-LPG with 128 Vector Engines (1024 ALUs), 8 Ray Tracing Units, and 8 Samplers.
- **Clock**: Up to **2.35 GHz**.
- **Software Runtimes**: Native Linux **OpenVINO**, **Intel oneAPI**, Level Zero (`ze`), and Vulkan / SYCL.
- **AI Math Throughput**: Full support for native INT8, FP16, and BF16 matrix operations.
- **Inference Benchmark Target**:
  - `qwen2.5-coder:7b` / `llama-3.2:3b` at 30–50 tokens/sec using OpenVINO GPU offload.
  - CLIP image embeddings at <15ms per image.
  - Real-time video processing (WhisperX / Faster-Whisper) at >10x real-time speed.

### B. Intel AI Boost NPU (Neural Processing Unit)
- **Hardware**: Dedicated 2-engine NPU tile directly on the Meteor Lake silicon.
- **Performance**: Up to **11 TOPS** dedicated INT8 NPU compute (total platform AI compute up to 34 TOPS).
- **Linux Driver Support**: Intel VPU / NPU driver (`/dev/accel/accel0` in Linux Kernel 6.8+).
- **Strategic Purpose**: Zero-wattage continuous background tasks (continuous audio transcription, presence detection, anomaly detection, continuous document embeddings) that run 24/7 without heating the chassis or spinning the fan.

---

## 🧠 3. Memory & High-Speed Storage Tiers

- **System Memory**: **16 GB DDR5 5600 MHz SODIMM** (Single stick populated, expandable to 64 GB dual-channel via secondary SODIMM slot).
- **Internal Storage**: **1TB PCIe 4.0 x4 NVMe SSD** (`WPBSN4M8-1TGP`).
  - Sequential Reads: ~5,000 MB/s.
  - Sequential Writes: ~4,500 MB/s.
  - High-endurance NVMe tier dedicated to container images, local scratch spaces, build caches, and model weight weights.

---

## 🌐 4. Networking & Interconnect Topology

- **Dual 2.5GbE Wired Ethernet**:
  - Controller: Dual Intel Ethernet Controller **I226-V** (`38:F7:CD:D7:8E:D8` and `38:F7:CD:D7:8E:D5`).
  - Capable of 2.5 Gbps line-rate throughput or redundant failover bonding (`balance-rr` or `active-backup`).
- **Wi-Fi 7 Interface**:
  - Chipset: **Intel Wi-Fi 7 BE200 320MHz** (MAC: `f8:cf:52:eb:88:e0`).
  - Speeds up to 1.4 Gbps over 6 GHz / 5 GHz bands connected to whole-home AP `Rimjhim`.
- **Bluetooth**: Bluetooth 5.4 LE.

---

## 🔒 5. Decoupled Role in Homelab

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│                    NODE 3: GEEKOM IT13-MAX COMPUTE ENGINE                    │
├──────────────────────────────────────────────────────────────────────────────┤
│  ⚡ 16-Core / 22-Thread Ultra 9 185H  •  8 Xe-Core Arc GPU  •  AI Boost NPU  │
├──────────────────────────────────────────────────────────────────────────────┤
│  • Offload all CPU-bound workloads from Raspberry Pi 5 (which protects DNS)  │
│  • Offload heavy AI, vision, and ML from UGREEN NAS (which protects Plex)     │
│  • High-throughput private inference node (Ollama, vLLM, OpenVINO)           │
│  • High-concurrency autonomous developer agent execution environment        │
│  • High-speed data processing pipeline interfacing with NAS storage over LAN  │
└──────────────────────────────────────────────────────────────────────────────┘
```
