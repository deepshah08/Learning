# How to Back Up NAS Files Between Storage Pools?

> **Article ID**: `681`  
> **Category**: `Application Guide > Sync & Backup > How to Back Up NAS Files Between Storage Pools?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/681  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client(Windows/macOS), Web Browser

**Applicable Version**: NAS Firmware 1.18.0.0093 or later

The screenshots in this document are for reference only. The actual interface may vary slightly depending on the system or app version, please refer to the actual interface displayed.

## Introduction

In "**Sync & Backup**", you can use "**Backup between storage pools**" to regularly back up data from one storage pool to another. For example, you can back up important files in Storage Pool 1 (such as Folder A) to Storage Pool 2 (such as Folder B). This provides cross-storage-pool data protection and reduces the risk of data loss caused by a failure of a single storage pool.

## Prerequisites

Before using this feature, make sure the following requirements are met:

● The system firmware and "**Sync & Backup**" app are both updated to the latest version.

● The NAS has at least two storage pools with sufficient available capacity.

● If the NAS currently has only one storage pool, install an additional drive and create another storage pool before configuring the backup task.

## Create a backup task

1. Open "**Sync & Backup**", go to "**Back up & Restore**", click "**Add**", select "**Backup between storage pools**" as the backup type, and then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-08-12/36b010069e984faf97b0ef012aa2cc02.webp)

2. Select the backup source and backup destination, and configure filter rules as needed:

![](https://file-us.ugreennas.com/admin/article/2026-08-12/85d485a0aa7a4010b97f890739b99cc7.webp)

● **Source**: You can select multiple folders as backup sources.

● **Backup destination**: You can select only one destination folder, and it must be located in a different storage pool from the backup source.

● **Filter Rule (optional)**: Configure file filtering rules as needed. You can exclude files from backup based on file size, file name, or file extension.

3. After completing all settings, click "**Next**" to continue.

4. Select the **Backup mode** and configure the **Backup Plan**:

![](https://file-us.ugreennas.com/admin/article/2026-08-12/c83a274067454bc9b510f018dedc353c.webp)

|  |  |  |
| --- | --- | --- |
| **Backup mode** | **Description** | **Recommended use** |
| Incremental Backup | Maintains a single version and backs up only files that have been added or modified since the previous backup. Files deleted from the source are retained at the backup destination. | Long-term data retention and protection against accidental deletion |
| Mirror backup | Maintains a single version and keeps the backup destination identical to the source. Files at the destination that no longer exist in the source will be deleted. | Exact replication and environment cloning |

Set the time for backups to run automatically. Supported schedule types include Every Day, weekdays only, weekends only, and custom schedules (for example, every day at 2:00 AM), helping reduce the impact of backup tasks on device use during the day.

5. After completing the configuration, click "**Next**". On the Preview page, review all settings. You can:

![](https://file-us.ugreennas.com/admin/article/2026-08-12/ac6eadd90bae4b589594aee8c8067960.webp)

● Modify the backup task name.

● Select "**Back up immediately after creation**" to automatically start the first backup after the task is created.

6. Click "**Confirm**" to create the backup task.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/7380a7c58bd94054ab26e049517a9c0a.webp)

## View and manage backup tasks

Created tasks can be managed from the "**Back up & Restore**" page:

● View the backup task status, run a backup immediately, or pause a task.

● Click "**More**" > "**Edit Task**" to modify the task name, backup source, filter rules, or backup plan.

● Click "**More**" > "**Delete Task**" to remove completed tasks or tasks that are no longer needed.

● Click the "**···**" button on the right side of a task to quickly create a new backup task.

## Notes

● If the device has only one storage pool, "**Backup between storage pools**" is unavailable.

● Backups use some system resources. It is recommended to schedule backup tasks during periods when the device is idle, such as at night.

● Do not insert or remove drives during a backup. Make sure the corresponding storage pools are healthy and the network connection is stable to prevent the task from being interrupted or failing.

● If an error occurs during backup, go to "**Log**" to view the details, or contact technical support for assistance.
