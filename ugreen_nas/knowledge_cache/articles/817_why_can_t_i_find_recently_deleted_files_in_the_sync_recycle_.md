# Why Can't I Find Recently Deleted Files in the Sync Recycle Bin?

> **Article ID**: `817`  
> **Category**: `Application Guide > Sync & Backup > FAQ > Why Can't I Find Recently Deleted Files in the Sync Recycle Bin?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/817  

---

## Issue Description

When a file is deleted on one side of a sync task (for example, the computer path), you may not find it in the "**Computer Recycle Bin**" of the sync task. Instead, it only appears in the computer's system recycle bin.

## Cause Analysis

This is expected behavior. UGREEN NAS uses a cross-backup mechanism to protect your files.

The sync task recycle bin is a hidden folder named `#SyncVersion`, which is only created after the NAS receives a deletion command from the other device. Therefore, deleted files are actually stored in the recycle bin on the opposite device.

## Where Deleted Files Go

Taking file deletion on the computer as an example, the system performs the following two actions:

1. **Local system recycle**: When a file is deleted from the computer's sync folder, it is moved to the computer's built-in recycle bin (such as the Windows Recycle Bin or Mac Trash). To restore it locally, you need to check the system recycle bin on your computer.

2. **Cross-device sync backup**: At the same time, the computer sends a deletion command to the UGREEN NAS. After receiving it, the NAS does not permanently delete the file. Instead, it creates a `#SyncVersion` folder in its sync directory and stores the file there. You can click "**NAS Recycle Bin**" in the sync interface to view the file that was deleted from the computer.

In summary, when a file is deleted on one device, it will be moved to that device's system recycle bin. Meanwhile, the NAS deletes it from the sync path but preserves a copy in the sync recycle bin (`#SyncVersion`) on the other device.
