# 📸 Asymmetric Tiered Storage Architecture: NVMe vs CMR HDD

> **Design Pattern**: Application-Level Smart Tiering & Zero-Copy Direct Mounting  
> **Status**: 📝 **Documented & Staged for Implementation**  
> **Last Updated**: 2026-08-26  

---

## 🎯 The Core Dilemma & Ground Truth

### 1. The "Generic Read Cache" Trap
* **The Trap**: Block-level read caches (e.g. bcache, LVM cache, SSD Read Cache) read a file from the HDD and **write** it to the SSD to speed up future reads.
* **The Flaw**: Reading large 40MB RAW photos or 4K videos once turns every read into an SSD write, needlessly burning NVMe write endurance (TBW) on media that may never be accessed again.

### 2. The Solution: Application-Level Asymmetric Tiering
Separate the **High-Frequency Metadata & Previews** from the **Cold Bulk Original Files**:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        ASYMMETRIC PHOTO STORAGE PIPELINE                               │
├───────────────────────────────────────────┬────────────────────────────────────────────┤
│ ⚡ FAST APPLICATION TIER (4TB NVMe SSD)    │ 🗄️ COLD BULK ARCHIVE (10TB CMR IronWolf HDD)│
│    Volume 2 (/volume2)                    │    Volume 1 (/volume1)                     │
├───────────────────────────────────────────┼────────────────────────────────────────────┤
│ • SQLite Databases (Index, Face Tags, EXIF│ • Master Uncompressed RAW / JPEG Files     │
│ • Generated WebP/JPEG Thumbnails (50-100KB│ • High-Bitrate 4K Video Files              │
│ • Redroid Virtual Pixel 1 Runtime & App   │ • Cold Photo Backups                       │
├───────────────────────────────────────────┼────────────────────────────────────────────┤
│ 🚀 99% of Client Reads hit this tier:     │ 💤 10TB HDD STAYS ASLEEP at 0 RPM during:  │
│    • Timeline scrolling (Pure SSD READS)  │    • Scrolling photos                      │
│    • Searching faces, dates, locations    │    • Album browsing                        │
│    • Google Photos sync cataloging        │    • Mobile app timeline rendering         │
│    • ZERO wear on flash memory!           │    👉 Wakes ONLY on 1% Full RAW Downloads! │
└───────────────────────────────────────────┴────────────────────────────────────────────┘
```

---

## 🔄 Lifecycle Data Paths

### A. Client Write (Photo Upload from Phone)
1. **Option 1: Direct-to-HDD (Zero NVMe Writes)**
   * Mobile app writes photo directly to `/volume1/personal_folder/Photos/`.
   * NVMe writes: **0 bytes**.
   * HDD receives sequential write batch, finishes, and returns to sleep.
2. **Option 2: NVMe Ingest Buffer with Scheduled Draining**
   * Mobile app writes to `/volume2/staging/`.
   * Nightly cron batch-moves files to `/volume1/personal_folder/Photos/` sequentially.
   * HDD sleeps 23.9 hours/day.

### B. Client Read (Browsing & Viewing)
* **Gallery Browsing / Timeline Scroll**: App queries SQLite DB and loads 50KB WebP thumbnails from `/volume2`.
  * **Reads**: 100% NVMe solid-state reads (**0 flash wear, 0 dB noise, <1ms latency**).
  * **HDD State**: **100% Asleep (0 RPM)**.
* **Full-Resolution RAW Open / Export**: App fetches original file from `/volume1`.
  * HDD spins up on-demand, streams the file, and idles.

---

## 📌 Future Implementation Backlog
* [ ] Bind-mount `/volume1/personal_folder/Photos` directly into Redroid as `:ro` (`/data/media/0/DCIM/NAS_Photos:ro`).
* [ ] Configure inotify watcher to monitor `/volume1` and trigger `scan_volume` without file copying.
