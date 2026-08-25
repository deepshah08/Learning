# 📂 Native macOS SMB File Sharing & Photo Ingestion — Single Source of Truth

> **Context**: High-speed SMB3 network file sharing on UGREEN DXP2800 with Apple macOS extensions (`vfs_fruit`) for Finder drag-and-drop file management, UGREEN Photos AI indexing, and direct Google Photos uploading.  
> **Host**: UGREEN DXP2800 (`192.168.1.80` / `deepdxp2800.lan`)  
> **Status**: 🟢 **Operational & Production Verified**  
> **Protocol**: SMB3 with 2.5GbE transfer speed + macOS metadata optimization  

---

## 1. Active SMB Network Shares

| Share Name | Target Path on NAS | Purpose | Permissions |
| :--- | :--- | :--- | :--- |
| **`personal_folder`** | `/volume1/@home/Deep Shah` | Personal home directory, Photos, documents | Read / Write (`Deep Shah`) |
| **`data`** | `/volume1/data` | Media library (`movies`, `tv`, `torrents`) | Read / Write (`Deep Shah`, `pranalishah`) |
| **`yellowstone`** | `/volume1/yellowstone` | Shared household photo and file vault | Read / Write (`Deep Shah`, `tillo`) |
| **`DP`** | `/volume1/DP` | Shared joint folder | Read / Write (`Deep Shah`, `pranalishah`) |
| **`docker`** | `/volume1/docker` | Application config directories | Read / Write (`Deep Shah`) |

---

## 2. Connecting from macOS Finder (Step-by-Step)

### Option A: Quick Connect via Finder
1. Open **Finder** on your Mac.
2. Press **`Cmd + K`** (or go to menu bar: **Go ➔ Connect to Server...**).
3. In the Server Address field, enter:
   ```text
   smb://192.168.1.80
   ```
   *(Or `smb://deepdxp2800.lan` when on home Wi-Fi, or `smb://100.68.196.14` over Tailscale)*.
4. Click **Connect**.
5. Select **Registered User**:
   * **Name**: `Deep Shah` (or `pranalishah`)
   * **Password**: `S#@#j0k3R`
   * Check **"Remember this password in my keychain"**.
6. Select the share(s) you want to mount (e.g. `personal_folder`, `data`, `yellowstone`).

### Option B: Make it Permanent in Finder Sidebar
* Once mounted, drag the network drive icon from your Desktop or Finder into the **Favorites / Locations** section of your Finder Sidebar.

---

## 3. Photo Management & Ingestion Workflows

### Workflow 1: Drag-and-Drop to UGREEN Photos (AI Indexing)
* Open the mounted `personal_folder` ➔ Open the `Photos` folder.
* Drag any photos or videos from your Mac directly into `Photos`.
* **UGREEN Photos AI** will automatically trigger facial recognition, scene detection, and location tagging on the Intel N100 processor in the background.

### Workflow 2: Direct Drag-and-Drop to Google Photos
* Open **Google Photos** in your web browser ([https://photos.google.com](https://photos.google.com)).
* Open your mounted NAS folder in Finder (`personal_folder/Photos` or `yellowstone`).
* Drag and drop photos straight from Finder into the Google Photos browser tab.
* **Benefit**: Uploads directly from NAS storage without taking up local storage on your Mac's internal SSD.

---

## 4. Performance & macOS Tuning

The Samba daemon (`/etc/samba/smbglb.conf` & `/etc/samba/smbcustom.conf`) is configured with:
* `vfs objects = catia fruit streams_xattr`: Eliminates `.DS_Store` and `._*` AppleDouble file clutter while enabling fast native macOS metadata searches and Finder icon previews.
* `server max protocol = SMB3`: Maximizes read/write throughput across 2.5GbE LAN.
