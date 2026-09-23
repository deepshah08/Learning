# How to Fix Write Failures Despite Available Storage Space (Reclaim Storage Spac

> **Article ID**: `859`  
> **Category**: `Application Guide > Storage > How to Fix Write Failures Despite Available Storage Space (Reclaim Storage Spac`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/859  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client, Web Browser.

**Applicable Versions**: UGOS Pro firmware version 1.16.0.0042 or later.

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

**Requirements**: This feature is only supported on storage spaces using the Btrfs file system (EXT4 is not supported).

## Introduction

During daily use, you may encounter situations where the storage space shows sufficient free capacity, but data operations still fail frequently.

If you experience one or more of the following issues, they are usually caused by the underlying "**Fragmentation**" mechanism of the Btrfs file system, which may lock some storage space and prevent it from being effectively used:

● App issues: Apps cannot be installed or enabled, and the system displays errors such as data errors or corrupted app database files.

● File operation issues: File operations such as renaming, moving, or copying fail, with messages such as "**File or directory does not exist**" or "**Insufficient space**".

● Underlying system errors: System-level commands such as df show that free space is available, but write operations still fail.

To resolve usage issues caused by these underlying limitations, UGREEN NAS provides a dedicated "**Reclaim storage space**" feature (which is also required when data rebalancing cannot be performed). This feature deeply reorganizes unused but inaccessible hidden storage space to restore available capacity.

## Use the Reclaim Storage Space Feature

1. Open the Storage app and click "**Storage**" in the left sidebar.

2. At the top of the main panel on the right, switch to the "**Storage pool & Volume**" tab.

3. Locate the target storage space experiencing write failures and confirm that its file system is labeled as **Btrfs**.

4. Click the "**···**" icon on the right side of the storage space block and select"**Reclaim storage space**".

![](https://file-us.ugreennas.com/admin/article/2026-08-06/9b7dc6bc209e414a83282b00347e292c.webp)

5. In the confirmation dialog box, click "**Reclaim**". The system will then begin the fragmentation cleanup process.

![](https://file-us.ugreennas.com/admin/article/2026-08-06/10881073c81341699cbc820972941f6f.webp)

## Notes

The Reclaim Storage Space feature is a high-load I/O task that operates at the file system level. Before starting the operation, please be aware of the following:

● **Irreversible and cannot be interrupted**: Once the space reclaim task starts, it cannot be manually stopped midway. During execution, the volume status will continuously display "**Reclaiming**" until the task is fully completed, after which the status will return to "**Normal**".

![](https://file-us.ugreennas.com/admin/article/2026-08-06/c492def8ed1149e8884b7b2009a280b0.webp)

● **System performance degradation**: During the task, you can still access the NAS and read/write files normally. However, because the drives are operating under heavy load, overall system responsiveness and file transfer speeds may noticeably decrease. It is recommended to perform this task during off-peak hours, such as at night.

● **Normal fluctuation of available capacity (decreases first and then increases)**: During the reclaim process, the system temporarily uses additional storage space as a "**staging area**" to reorganize fragmented data. As a result, available capacity may temporarily decrease before increasing again after the reclaim process is completed.
