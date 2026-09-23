# Why does the #SyncVersion folder appear when using the sync feature, and does it take up space?

> **Article ID**: `632`  
> **Category**: `Application Guide > Sync & Backup > FAQ > Why does the #SyncVersion folder appear when using the sync feature, and does it take up space?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/632  

---

## **Issue Description**

When using the "Sync & Backup" feature to sync files from your local computer to the UGREEN NAS, a folder named #SyncVersion may appear on your computer if a file that is being synchronized is deleted from the NAS.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/91c9d45e-4948-4170-ac7d-7855ee5f9ed9.png)

## **Solution**

**Purpose of the #SyncVersion Folder:**

* **Prevent Data Loss**: This folder is automatically generated to prevent accidental data loss. When a file synced to the NAS is deleted on the NAS side, the system moves that file to the #SyncVersion folder on your computer so you can restore it if needed.
* **Not Synced to NAS**: The #SyncVersion folder is not included in the sync, so it does not take up NAS storage, but it does use local disk space on your computer.

**Example:**

Suppose you’ve set folder A on your computer to sync with folder B on the NAS.

If you delete a file in folder B on the NAS that was originally synced from A, that deleted file will be moved to the #SyncVersion folder on your computer.

As a result, the file is deleted from the NAS, but a copy is still retained on your computer, and you need to manually delete it if no longer needed.

**How to Permanently Delete Files:**

1. Locate the #SyncVersion folder on your computer.
2. Open it and manually delete the files inside.

**How to Restore Deleted Files:**

1. Find the desired file inside the #SyncVersion folder.
2. Move the file back to its original location.

**Can’t Find the #SyncVersion Folder?**

1. Click the [...] menu at the top of the window and select [Options] > [View].
2. Check the box for "Show hidden files, folders, and drives."

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/8d714c65-b07d-4ad9-9fc3-e027ece240a7.png)

This will allow you to see the #SyncVersion folder.
