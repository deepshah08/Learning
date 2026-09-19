# 🔄 IT13 Max Rollback, Recovery & Retrospective Guide

> **Scope**: Authoritative disaster recovery, factory reset, and Windows 11 Pro rollback procedure for the GEEKOM IT13 Max Mini PC (Intel Core Ultra 9 185H, 16GB DDR5, 1TB NVMe).

---

## 🛡️ 1. Windows 11 Pro OEM License Security

The Windows 11 Pro license included with the GEEKOM IT13 Max is **firmware-embedded (OEM_DM)**:
* **Storage Location**: Motherboard UEFI ACPI `MSDM` (Microsoft Data Management) table.
* **Extracted OEM Product Key**: `72YVN-TGVHX-6TQFD-GJMF8-F3KIT`
* **Durability**: Completely independent of the NVMe drive. Formatting, partitioning, or zeroing the NVMe SSD does **NOT** alter, delete, or invalidate this digital license.
* **Activation Protocol**: When Windows 11 Pro is reinstalled, the Microsoft installer automatically queries ACPI `MSDM`, retrieves the digital product key, and contacts Microsoft Activation Servers. No manual key entry or receipt lookup is required.

### How to Retrieve the Key Manually Anytime:

#### From Windows (PowerShell):
```powershell
(Get-CimInstance -Query 'select * from SoftwareLicensingService').OA3xOriginalProductKey
```

#### From Linux (Bash via `sysfs`):
```bash
sudo cat /sys/firmware/acpi/tables/MSDM | strings | tail -n 1
```

---

## 🔁 2. Complete Windows 11 Pro Factory Rollback Procedure

If you ever wish to revert the IT13 Max to a factory Windows 11 Pro environment:

### Step 1: Download Official Windows 11 Media
1. On any Mac, Linux, or Windows machine, download the official **Windows 11 Disk Image (ISO)** from Microsoft:
   - [Microsoft Official Windows 11 Download](https://www.microsoft.com/software-download/windows11)
2. Flash the ISO to a USB flash drive (8GB+) using:
   - **On Mac / Linux**: [BalenaEtcher](https://etcher.balena.io/) or [Raspberry Pi Imager](https://www.raspberrypi.com/software/) (`Use Custom` -> select Windows 11 ISO).
   - **Alternative**: [Ventoy](https://www.ventoy.net/) multi-boot USB.

### Step 2: Boot & Reinstall on IT13 Max
1. Plug the USB flash drive into any USB-A port on the IT13 Max.
2. Power on the IT13 Max and repeatedly press **`F7`** (or **`F12`**) to invoke the GEEKOM UEFI Boot Menu.
3. Select the USB drive (UEFI mode).
4. In the Windows setup wizard:
   - Select **Windows 11 Pro** (it will auto-detect the MSDM key if present).
   - When asked where to install, select all partitions on Drive 0 (the 1TB NVMe), click **Delete** until only "Drive 0 Unallocated Space" remains, and click **Next**.
   - Windows will partition, format, and install cleanly.

### Step 3: Drivers & Hardware Support
GEEKOM provides an official hardware driver package for the IT13 Max (Intel Core Ultra 9 185H):
* **Intel Arc Graphics & Media Driver**: [Intel Official Driver Support](https://www.intel.com/content/www/us/en/download/785597/intel-arc-iris-xe-graphics-windows.html)
* **Intel Wireless-AC / AX / BE Wi-Fi Driver**: [Intel Wi-Fi Drivers](https://www.intel.com/content/www/us/en/download/19351/windows-10-and-windows-11-wi-fi-drivers-for-intel-wireless-adapters.html)
* **GEEKOM Official Support Portal**: [GEEKOM Drivers & Software](https://www.geekompc.com/support/)

---

## 📦 3. Pre-Wipe Drive Image Backup (Optional Snapshot)

If you want a bit-for-bit raw image backup of the factory Windows install before wiping:
1. Boot any Linux Live USB (e.g. Ubuntu Server live).
2. Mount your UGREEN NAS SMB share (`//192.168.1.80/personal_folder` or `/volume2/backups`).
3. Stream a compressed disk image directly over the network:
   ```bash
   sudo dd if=/dev/nvme0n1 bs=64K status=progress | gzip -c | ssh nas "cat > /volume2/docker/backups/it13max_factory_win11_image.img.gz"
   ```
4. This preserves the exact factory state byte-for-byte without consuming local drive space.

---

## 📝 4. Retrospective & Lessons Learned

| Topic | Observation | Resolution / Best Practice |
| :--- | :--- | :--- |
| **USB-C Direct Host-to-Host** | Connecting Mac to IT13 Max via standard USB-C cable negotiated 15W USB-PD charging, but no data channel. | Both are USB Hosts. High-speed IP networking requires a certified Thunderbolt 3/4 cable (`bridge0`) or local Wi-Fi / 2.5GbE LAN. |
| **Windows OOBE Setup Lockout** | Initial Windows setup (language screen) does not load user Bluetooth stack without paired input devices. | Keep a wired USB keyboard, game controller, or USB dongle handy for the initial 3-minute wizard. |
| **Windows Sleep / Wi-Fi Drop** | Windows 11 Modern Standby drops Wi-Fi connectivity after 15–30 min idle. | For headless servers, always execute `powercfg -change -standby-timeout-ac 0` and `powercfg -hibernate off`. |
| **IP Reservation** | DHCP lease on Pi-hole v6 FTL (`192.168.1.92`) was bound to `192.168.1.155`. | Committed permanently to `/etc/dnsmasq.d/99-static-reservations.conf` with FTL reload. |
