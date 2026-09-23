# Backup Mac Files to UGREEN NAS Using Time Machine

> **Article ID**: `350`  
> **Category**: `Application Guide > Control Panel > FAQ > Backup Mac Files to UGREEN NAS Using Time Machine`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/350  

---

**Applicable Versions:**

● UGOS Pro Firmware **1.9.0.0035** or later

● macOS **Monterey 12** or later

**Note:**

Screenshots and interfaces in this document are for reference only. Actual displays may vary slightly depending on the system or app version. Some features may be adjusted across different versions; please refer to your actual interface.

Apple Official Documentation: [Back up your Mac using Time Machine](https://support.apple.com/en-us/104984) .

## Overview

Time Machine is a built-in file backup tool in macOS that supports incremental backups of the entire system, applications, files, and settings.

When used with a UGREEN NAS, you can centrally store your Mac's historical snapshots on the NAS, minimizing the risk of data loss or device failure and enabling quick restoration of the entire system.

## Steps

### Enable Time Machine on the NAS

1. In the "**Control Panel"** app, go to "**File Service" > "SMB"** and enable SMB service.

![](https://file-us.ugreennas.com/admin/article/2025-10-20/83f461ddd8e545de83e517205cfcb648.webp)

2. Switch to the "**Advanced Settings"** page and check "**Enable Bonjour Service"**.

![](https://file-us.ugreennas.com/admin/article/2025-10-20/635549c97a98415790d39da483e50c20.webp)

3. Click "**Set time machine folder"**, then select or create a dedicated shared folder as the backup target (creating a new folder is recommended), and click "**Save"** to apply.

### Connect to the NAS on a Mac

1. Open **Finder** and click the top menu "**Go" > "Connect to Server"**.

2. Enter the NAS address in the following format:

```
smb://NAS_IP
```

For example: `smb://192.168.1.100`.

3. Enter your NAS username and password to log in.

4. Locate and mount the Time Machine backup shared folder you set up on the NAS.

### Configure Time Machine

1. On your Mac, open Time Machine by going to "**System Preferences"** > "**Time Machine"** from the Apple menu.

2. Click "**Select Backup Disk"**, choose the shared folder you created in the pop-up window, and then click "**Use Disk"**.

![](https://file-us.ugreennas.com/admin/article/2025-10-20/503e0d826dd74edfb217ff030e1981b9.webp)

3. Enter your NAS user credentials to authenticate.

4. Check "**Automatic Backup"**, the system will perform the first full backup automatically, followed by incremental backups.

![](https://file-us.ugreennas.com/admin/article/2025-10-20/d8889ea54cff4707bc67442bcd14e0c8.webp)

## Set Shared Folder Capacity Quota

To prevent Time Machine from using unlimited NAS storage, it is recommended to set a capacity quota for the shared folder:

1. Open the "**Files"** app and go to "**Management" > "Shared folder management"**.

![](https://file-us.ugreennas.com/admin/article/2025-10-20/df5ea029e10f4b35ae46b0bd7e9b19cc.webp)

2. Locate the shared folder set as the **Time Machine folder** and click "**Edit"**.

![](https://file-us.ugreennas.com/admin/article/2025-10-20/3a00ffa340f84dcfa04bd3287559c7e5.webp)

3. In the edit popup, switch to the **General** tab and scroll down to **Capacity quota**.

![](https://file-us.ugreennas.com/admin/article/2025-10-20/204bfd68362a4a199b4429416a53a99e.webp)

4. Check "**Enable"**, set the maximum quota, and click "**OK"** to save.

## Why does Time Machine backup to UGREEN NAS fail?

When the Time Machine backup space is insufficient, the system will prompt a backup failure. You can resolve the issue in the following ways:

![](https://file-us.ugreennas.com/admin/article/2025-10-20/ed94bc1bf4a74835847005c18274aab9.webp)

1. **Clear the NAS Recycle Bin**  
When you delete files on the NAS, they usually go into the Recycle Bin first, occupying storage space.

● Log in to the NAS system and open the **"Files"** app;

● Locate the shared folder used for Time Machine backups, click "**Recycle Bin"** and empty it to free up space.

![](https://file-us.ugreennas.com/admin/article/2025-10-20/543700e361474a5dbd9ccf55f177a776.webp)

2. **Manually delete old backups in Time Machine (Recommended)**

This is Apple's officially recommended method to ensure backup integrity.

● Click the **Time Machine icon** in the menu bar and select **"Browse Time Machine Backups"**;

● Enter the "starfield" interface, and use the timeline on the right to find old backups you no longer need;

● Click the **gear icon** at the top of the window and select "**Delete Backup"**;

● Enter the administrator password when prompted to confirm.  
You can repeat this process to delete multiple old backups until sufficient space is freed.

3. **Clean up local snapshots on your Mac**  
When the Mac cannot connect to the backup disk, the system will create local snapshots, which occupy storage space.

● Open **Terminal** (in "Applications > Utilities");

● Enter the command to view local snapshots:

```
tmutil listlocalsnapshots /
```

● Delete a specific snapshot (replace the date with the actual snapshot name):

```
sudo tmutil deletelocalsnapshots 2025-09-01-12345
```

4. **Expand the quota of the shared folder used by Time Machine**  
If a quota has been set for the shared folder used by Time Machine, it may cause insufficient space.

● Log in to the NAS with an administrator account;

● Open "**Files" > "Management" > "Shared folder management"**;

● Find the shared folder used by Time Machine and click "**Edit"**;

● Adjust the **Capacity quota** to a larger value and save.

![](https://file-us.ugreennas.com/admin/article/2025-10-20/0f98cf776a4d40eab6b1e2720ad8ed39.webp)

5. **Expand NAS storage capacity**  
If the overall hard drive space is insufficient, you can increase capacity by adding hard drives, expanding the storage pool, or reallocating storage space.

6. **Reinitialize the backup**  
Use this method only if old backups do not need to be preserved:

● Delete the Time Machine backup directory on the NAS;

● On the Mac, reselect the NAS as the backup disk;

● The system will automatically create a brand-new backup set.
