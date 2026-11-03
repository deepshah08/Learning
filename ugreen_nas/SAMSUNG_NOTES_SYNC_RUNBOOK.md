# 📱 Samsung Notes Automated Sync & Ingestion Runbook

> **Service**: `samsung-notes-sync`  
> **Deployment Target**: UGREEN NAS (`192.168.1.80`) / GEEKOM IT13 Max (`192.168.1.155`)  
> **Storage Tier**: NVMe SSD (`/volume2/docker/samsung_notes/`)  
> **Status**: 🟢 Production Active  

---

## 1. System Architecture

```mermaid
flowchart TD
    subgraph MobileDevice ["📱 Samsung Galaxy Tab S10+ (SM-X820)"]
        SNotes["Samsung Notes Library<br/>(One UI 8 / Android 16)"]
        ExportADB["ADB UI Automation / Manual Export<br/>• Standard PDF v1.7"]
        ExportDir["/sdcard/Documents/SamsungNotesExport/"]
        FolderSync["FolderSync Lite<br/>• SMB3 Protocol<br/>• Hourly / Event Sync"]
        
        SNotes -->|"Export as Standard PDF"| ExportADB
        ExportADB --> ExportDir
        ExportDir --> FolderSync
    end

    subgraph UgreenNAS ["NAS: UGREEN DXP2800 (192.168.1.80)"]
        Samba["Samba SMB Port 445<br/>Share: 'docker'"]
        Incoming["/volume2/docker/samsung_notes/incoming/"]
        
        subgraph DockerContainer ["Container: samsung_notes_sync"]
            Daemon["Python 3.12 Sync Daemon<br/>(UID 1000:1000)"]
            Stability["is_file_stable()<br/>• Size change detector<br/>• %%EOF validator"]
            Parser["SamsungPdfParser<br/>• Extracts S-Pen RGBA overlays<br/>• Extracts JPEG paper textures<br/>• Extracts typed text streams"]
            Ledger["SyncLedger<br/>• Atomic JSON persistence<br/>• SHA-256 deduplication"]
        end
        
        NotesVault["/volume2/docker/samsung_notes/notes/<br/>• Markdown (.md)<br/>• attachments/ (*.png, *.jpg)"]
        ArchiveVault["/volume2/docker/samsung_notes/archive/<br/>• Original Vector PDFs"]
        LedgerVault["/volume2/docker/samsung_notes/ledger/<br/>• processed_ledger.json"]
        
        FolderSync -->|"SMB3 Upload"| Samba
        Samba --> Incoming
        Incoming --> Daemon
        Daemon --> Stability
        Stability --> Parser
        Parser --> NotesVault
        Parser --> ArchiveVault
        Parser --> Ledger
        Ledger --> LedgerVault
    end

    subgraph LLMAndWorker ["💻 GEEKOM IT13 Max (192.168.1.155)"]
        Qwen["Qwen 3.6-35B-A3B MoE<br/>(Coding Specialist / llamacpp)"]
        Qwen -.->|"Synthesized Core Modules"| Daemon
    end
```

---

## 2. Configuration Parameter Matrix

| Variable | Default Value | Description |
|---|---|---|
| `SAMSUNG_NOTES_INPUT_DIR` | `/data/incoming` | Directory monitored for new PDF exports. |
| `SAMSUNG_NOTES_MARKDOWN_DIR` | `/data/notes` | Target directory for generated Markdown notes. |
| `SAMSUNG_NOTES_ATTACHMENTS_DIR` | `/data/notes/attachments` | Directory for high-res extracted S-Pen PNGs & JPEG page textures. |
| `SAMSUNG_NOTES_ARCHIVE_DIR` | `/data/archive` | Safekeeping vault for original full-fidelity source PDFs. |
| `SAMSUNG_NOTES_LEDGER_FILE` | `/data/ledger/processed_ledger.json` | Atomic JSON ledger storing SHA-256 hash deduplication records. |
| `SAMSUNG_NOTES_POLL_INTERVAL_SEC` | `5.0` | Ingestion scan frequency in seconds. |
| `SAMSUNG_NOTES_STABILITY_DELAY_SEC`| `2.0` | Sleep delay checking for active file size growth. |
| `SAMSUNG_NOTES_RCLONE_ENABLED` | `false` | Optional cloud replication trigger. |
| `SAMSUNG_NOTES_RCLONE_REMOTE` | `gdrive:SamsungNotes` | Remote rclone destination path. |

---

## 3. Storage Tiering & Hardware Isolation Compliance

* **NVMe SSD Exclusivity (`/volume2`)**: All ingest drops, intermediate image extraction, SQLite/JSON ledgers, and generated markdown reside strictly on `/volume2` (4TB WD_BLACK SN850X).
* **Mechanical Pool Immunity (`/volume1`)**: Zero daemon I/O touches the mechanical HDD array, allowing the 10TB Seagate IronWolf drive to remain in 0 RPM deep hibernation.
* **Non-Root Container Isolation**: Runs as unprivileged UID `1000:1000` (`appuser:appgroup`), matching the NAS local account permissions.

---

## 4. Live CLI Health-Check & Verification

### Check Container Status & Logs (UGREEN NAS)
```bash
ssh nas "docker ps | grep samsung_notes; docker logs samsung_notes_sync --tail 20"
```

### Check Ingestion Vault State
```bash
ssh nas "ls -la /volume2/docker/samsung_notes/notes /volume2/docker/samsung_notes/archive"
```

### Inspect Ingested Deduplication Ledger
```bash
ssh nas "cat /volume2/docker/samsung_notes/ledger/processed_ledger.json | jq ."
```

### Run Batch Export from Mac
```bash
python3 "/Users/deep/Desktop/DATA ORG/tools/export_samsung_notes.py" --format pdf --all
```

---

## 5. Disaster Recovery & Rollback

### Restart Service
```bash
ssh nas "cd /volume2/docker/samsung_notes/service && docker compose restart"
```

### Force Re-Ingestion of Notes
If you need to re-parse all archived notes (e.g. after updating parser logic):
```bash
ssh nas "rm -f /volume2/docker/samsung_notes/ledger/processed_ledger.json && cp /volume2/docker/samsung_notes/archive/*.pdf /volume2/docker/samsung_notes/incoming/"
```

### Stop & Remove Service
```bash
ssh nas "cd /volume2/docker/samsung_notes/service && docker compose down"
```
