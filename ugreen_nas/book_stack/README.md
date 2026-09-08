# 📚 Automated E-Book & Digital Bookshelf Stack (Calibre-Web-Automated + Shelfmark)

> **Node**: UGREEN DXP2800 NAS (`192.168.1.80`)  
> **Status**: 🟢 **Production**  
> **Ports**: `8083` (Calibre-Web-Automated), `8084` (Shelfmark)  
> **Network**: `media_net` (Docker Bridge)  
> **Storage Tier**: Hot NVMe SSD (`/volume2/docker/book_stack`) + Cold SATA CMR HDD (`/volume1/data/books`)

---

## 🏛️ System Architecture

```mermaid
flowchart TD
    subgraph Client["User Clients"]
        Browser["Web Browser (Mac/Phone)"]
        KOReader["KOReader (E-ink / Tablet)"]
        Kindle["Amazon Kindle"]
    end

    subgraph NAS_Docker["UGREEN DXP2800 Docker Network (media_net)"]
        SM["Shelfmark (:8084)\nSearch & Multi-Source Downloader"]
        CWA["Calibre-Web-Automated (:8083)\nCatalog & In-Browser Reader"]
        PR["Prowlarr (:9696)\nTorrent Indexers"]
        QB["qBittorrent (:8080)\nBitTorrent Client"]
        HP["Homepage Dashboard (:3000)"]
    end

    subgraph Storage["Asymmetric Storage Tiering"]
        NVMe["NVMe SSD (/volume2/docker/book_stack)\n• CWA metadata.db & app configs\n• Shelfmark SQLite & cache"]
        HDD_Ingest["SATA CMR HDD (/volume1/data/books/ingest)\n• Auto-ingest staging folder"]
        HDD_Lib["SATA CMR HDD (/volume1/data/books/library)\n• Permanent Organized EPUB/PDF library"]
    end

    subgraph Sources["Book Sources"]
        AA["Anna's Archive / LibGen (DDL)"]
        IRC["IRC Highway (#ebooks)"]
        Torrents["BitTorrent Swarm (TPB, 1337x, MAM)"]
    end

    Browser -->|Search Book| SM
    SM -->|1. Direct Download| AA
    SM -->|2. IRC Highway| IRC
    SM -->|3. Torrent Search| PR
    PR -->|Push Magnet| QB
    QB -->|Download| Torrents

    AA & IRC & QB -->|Save EPUB/PDF| HDD_Ingest
    HDD_Ingest -->|Auto-Ingest Watcher| CWA
    CWA -->|Fetch Metadata & Covers| CWA
    CWA -->|Catalog & Deduplicate| HDD_Lib
    CWA -.->|Write Cache| NVMe

    Browser -->|Read Online| CWA
    KOReader -->|OPDS Sync (:8083/opds)| CWA
    CWA -->|Send-to-Kindle (SMTP)| Kindle
    HP -->|Live Service Widgets| SM & CWA
```

---

## ⚙️ Configuration Parameter Matrix

| Parameter | Calibre-Web-Automated | Shelfmark | Notes |
| :--- | :--- | :--- | :--- |
| **Image** | `crocodilestick/calibre-web-automated:latest` | `ghcr.io/calibrain/shelfmark:latest` | `linux/amd64` |
| **Container Port** | `8083` | `8084` | Verified free on NAS |
| **Host Endpoint** | [http://192.168.1.80:8083](http://192.168.1.80:8083) | [http://192.168.1.80:8084](http://192.168.1.80:8084) | Reachable on local LAN |
| **Hot Storage (NVMe)** | `/volume2/docker/book_stack/calibre-web-automated/config` | `/volume2/docker/book_stack/shelfmark/config` | SQLite databases, browser cache |
| **Cold Storage (HDD)** | `/volume1/data/books/library` | `/volume1/data/books/ingest` | 10TB IronWolf CMR |
| **PUID / PGID** | `1000` / `10` (`Deep Shah:admin`) | `1000` / `10` (`Deep Shah:admin`) | Matches host UGOS user |
| **Prowlarr Integration** | N/A | `http://prowlarr:9696` | Internal API key attached |
| **qBittorrent Integration** | N/A | `http://qbittorrent:8080` | Subnet whitelisted on `media_net` |
| **Metadata Providers** | Hardcover / OpenLibrary / Google Books | Open Library (`OPENLIBRARY_ENABLED=true`) | Zero API keys required |

---

## 🚀 Live Health Check & Verification Commands

Run these commands over OpenSSH ControlMaster session to verify status:

```bash
# 1. Container status and port bindings
docker ps --filter "name=calibre-web-automated" --filter "name=shelfmark" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# 2. HTTP readiness checks
curl -I http://192.168.1.80:8083   # Returns 302 Found (redirect to login)
curl -I http://192.168.1.80:8084   # Returns 200 OK

# 3. OPDS wireless catalog check (for KOReader / Moon+ Reader)
curl -s -u admin:admin123 http://192.168.1.80:8083/opds | grep "<title>"

# 4. Ingest directory watch check
ls -lh /volume1/data/books/ingest/

# 5. Library directory contents and SQLite DB
ls -lh /volume1/data/books/library/
sqlite3 /volume1/data/books/library/metadata.db "SELECT id, title, path FROM books;"
```

---

## 📱 Client Connection Guides

### 1. In-Browser Reader (Desktop, iPhone, iPad, Galaxy Tab)
- Open: [http://192.168.1.80:8083](http://192.168.1.80:8083)
- Default credentials: `admin` / `admin123`
- Click any book cover and select **Read in Browser** to read EPUBs or PDFs with customized fonts, dark mode, and bookmarking.

### 2. KOReader (Kindle Jailbreak, Kobo, Onyx Boox, Android)
1. In KOReader, open the top menu and select **OPDS Catalog**.
2. Add New Catalog:
   - **Catalog Name**: `Home NAS Bookshelf`
   - **Catalog URL**: `http://192.168.1.80:8083/opds`
   - **Username**: `admin`
   - **Password**: `admin123`
3. Browse authors, series, and recently added books directly on the e-ink screen with 1-click download.

### 3. Send-to-Kindle (Email Push)
1. In Calibre-Web, navigate to **Admin** $\rightarrow$ **Edit Basic Configuration** $\rightarrow$ **E-Mail Server Settings**.
2. Enter your SMTP details (e.g., Gmail App Password or local SMTP).
3. In user profile, enter your Amazon `@kindle.com` delivery email.
4. Clicking **Send to Kindle** automatically converts/sanitizes the EPUB and emails it to your e-reader.

---

## 🔄 Rollback & Disaster Recovery

If you need to restart or recreate the stack:

```bash
# Restart stack
cd /volume2/docker/book_stack
docker compose restart

# Complete rollback / container destruction (preserves all library books and SQLite DB)
docker compose down
# Recreate from scratch:
docker compose up -d
```
