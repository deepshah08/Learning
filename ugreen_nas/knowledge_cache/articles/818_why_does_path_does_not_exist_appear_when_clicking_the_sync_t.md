# Why Does "Path does not exist" Appear When Clicking the Sync Task Recycle

> **Article ID**: `818`  
> **Category**: `Application Guide > Sync & Backup > FAQ > Why Does "Path does not exist" Appear When Clicking the Sync Task Recycle`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/818  

---

## Issue Description

After creating a sync task in the "**Sync & Backup**" app, you may click "**Computer Recycle Bin**" or "**NAS Recycle Bin**" within the task. In some cases, the system will display the message **“Path does not exist”**.

![](https://file-us.ugreennas.com/admin/article/2026-03-31/98a677426841401ba843171303734584.webp)

## Cause Analysis

This is a normal system behavior. The recycle bin for sync tasks is a hidden folder named `#SyncVersion`.

The system only creates this folder automatically after a file has been deleted. If no files have been deleted in the sync path yet, the `#SyncVersion` folder will not exist. Therefore, when you click the recycle bin, the system will prompt that the path does not exist.

## How the Recycle Bin Works

The system uses a cross-backup mechanism to protect your files. Deleted files are stored on the opposite device.

● **Scenario 1: File deleted on the computer**

If a file is deleted from the computer's sync folder, the system will automatically create a `#SyncVersion` folder in the sync directory on the UGREEN NAS. You can then click "**NAS Recycle Bin**" in the sync task interface to view the deleted file in that NAS folder.

● **Scenario 2: File deleted on the NAS**

If a file is deleted from the sync directory on the UGREEN NAS, the system will automatically create a `#SyncVersion`folder in the computer's sync folder.  
You can then click "**Computer Recycle Bin**" in the sync task interface to view the deleted NAS file in that computer folder.
