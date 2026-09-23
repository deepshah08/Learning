# Why UGREEN NAS Drives Stay Awake and What Causes Them to Spin Up?

> **Article ID**: `876`  
> **Category**: `Troubleshooting > Why UGREEN NAS Drives Stay Awake and What Causes Them to Spin Up?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/876  

---

## Overview

For a hard drive to enter sleep mode, the storage space it belongs to must remain inactive for the specified period, with no read or write operations.

Any disk activity initiated by the system, apps, users, or background services will keep the drive running. As a result, the drive may not enter sleep mode even when the feature is enabled, or it may wake up again after going to sleep.

## Troubleshooting Steps

If the drives do not enter sleep mode, check the following items in order.

### File Access and Transfers

The following activities read from or write to the drives, preventing them from entering sleep mode or waking them after they have gone to sleep:

● Opening "**Files**".

● Browsing files in the storage space where the drives are located.

● Uploading files to that storage space.

● Downloading files from that storage space.

● Moving, copying, deleting, or renaming files.

● Other users accessing that storage space through the web interface, desktop client, mobile app, or TV client.

If any file transfer is running in the storage space, whether an upload or download, the drives will remain active.

### Apps, Docker, and Virtual Machines

If apps, Docker containers, or virtual machines are installed in the storage space and are running or accessing data, the drives cannot enter sleep mode.

Common scenarios include:

● A Docker container is running.

● A virtual machine image is stored in the storage space and the virtual machine is running.

● An app is accessing files in the storage space.

● Tasks such as media library scans in "**Theater**", video playback, photo browsing, or UGREEN AI recognition are reading files.

● Sync or backup services are running in the background. They may access the drives even when no sync task is currently in progress.

● Apps such as Tencent Mobile Game Accelerator are running in the background and accessing data.

### Downloading and Seeding Tasks

Download apps continuously access the drives. If a download or seeding task is active, the drives will usually be unable to enter sleep mode.

Common scenarios include:

● An active download task in "**Download Center**".

● An active download task in Xunlei.

● Xunlei is seeding files.

● A Docker container is running a download or seeding task.

● Another download app is reading or writing files.

### Cache, Mounts, and Background Writes

The following configurations may cause the system to access mechanical drives periodically:

● Using an M.2 drive as a read/write cache.

● The system periodically writing cached data back to the storage space.

● Mounting files through WebDAV.

● Using the storage space as cache for a WebDAV mount.

When read/write cache is enabled, periodic cache write-back may prevent mechanical drives from remaining in sleep mode for extended periods.

### RAID Arrays and Storage Consistency Tasks

If the storage space uses RAID 1, RAID 5, RAID 6, or RAID 10, the system may perform light background I/O while idle.

These operations help maintain RAID data integrity and consistency, so the drives may not remain in sleep mode for long periods.

### Device Sign-In and System App Access

The following system activities may also wake the drives:

● Signing in to the device.

● Accessing a drive that contains an enabled personal folder after signing in.

● Accessing the drive where installed packages are stored after signing in.

● Opening **Storage Manager**.

● Checking drive status with smartctl.

● Accessing storage resources through **SAN Manager**.

Opening **Storage Manager** wakes the drives because the system checks their health status.

## Drives and Storage Spaces That May Not Support Sleep Mode

The following drive and storage types do not support, or may not support, sleep mode:

● M.2 drives

● SSDs

● External storage spaces

● External USB drives or drive enclosures without sleep support

If the drive itself or the connected external device does not support sleep mode, enabling the setting may have no effect.
