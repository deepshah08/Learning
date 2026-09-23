# Snapshot User Guide

> **Article ID**: `654`  
> **Category**: `Application Guide > Snapshot > Snapshot User Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/654  

---

## Applicability

**Applicable Clients:** UGREEN NAS PC Client (Windows/macOS), Web browser

**Applicable Version:** UGOS Pro firmware 1.6.1.2846 or later

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

The **Snapshot** records the complete state of a folder on your NAS at a specific point in time, much like taking an "instant photo" of your data. If you accidentally delete an important file, overwrite a work document, or encounter a virus attack, you can restore the folder to the state captured by the snapshot.

Snapshots use **incremental snapshot** and **copy-on-write** technologies. Each snapshot records only the data that has changed since the previous snapshot, minimizing storage usage. For example, the first snapshot records the complete data state, while subsequent snapshots save only newly added or modified data instead of duplicating all data.

## Install and Access

1. Open "**App Center**" and locate the "**Snapshot**" app.

2. Click "**Install**" and follow the on-screen instructions to complete the installation.

3. Once installed, click the app icon on the desktop or under All Apps to start using it.

## Use Cases

Snapshots are ideal for protecting data that is rarely modified but needs to be retained for a long time, such as:

● **Family photo and video libraries:** Protect precious memories from accidental deletion.

● **Important work documents:** Prevent accidental overwriting or modification.

**Tips:**

● **Shared family photo albums:** Create a snapshot every week and retain a special version at the end of each month.

● **Storage management:** Set snapshots to be deleted automatically after 60 days while retaining snapshots from the most recent two quarters.

**Note:** Frequently modified files, such as installation packages being downloaded, may consume additional snapshot storage space.

## Feature Limitations and Supported Items

**Scope Limitations**

Snapshots are available only for Volumes created with the **Btrfs file format**. You can check the file system of storage space in the "**Storage managment**" app.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/91e478881866492e92b1fe2a9513d1a7.webp)

**Supported Snapshot Items**

Snapshots can be created for the following types of folders, including the Recycle Bin:

● **Shared folders** on a Btrfs Volume

● **Personal user folders** on a Btrfs Volume

● **Domain user folders** on a Btrfs Volume

**Snapshot Number Limits**

|  |  |  |
| --- | --- | --- |
| **Condition** | **Maximum snapshots per device** | **Maximum snapshots per shared folder** |
| Device memory≥2GB | 65536 | 1024 |
| Device memory<2GB | 4096 | 256 |

**Snapshot Storage Location**

Snapshot files are stored in  /volumeX/@snapshot/ using the following structure: folder type/folder name/snapshot file. Here, volumeX refers to the Volume containing the folder.

**Notes**

● Make sure your NAS has sufficient storage space for snapshot files.

● Regularly check whether snapshot plans are running as expected to ensure continuous data protection.

● Before restoring or cloning data, make sure you understand how the operation will affect the current data.

● This feature involves core system management operations and is available only to **administrators**. Standard users cannot use it.

## Using Snapshots

### Manually Create a Snapshot

Manually creating a snapshot is useful before making important data changes, such as updating the system or modifying files in bulk.

**Steps:**

1. Open "**Snapshot**", select the folder you want to snapshot, and click "**Take snapshot**".

![](https://file-us.ugreennas.com/admin/article/2026-09-07/d0ad758934674fc19ee70cfeaa6eabe9.webp)

2. Enter a snapshot description. We recommend using a meaningful description so the snapshot is easy to identify later. Enable or disable snapshot locking as needed, then click "**Confirm**". The system will begin creating the snapshot.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/0d171e146ae44c309eb9022386f7eb5a.webp)

3. Once complete, all snapshot records can be viewed in the Snapshot list on the Snapshot home page.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/e671549dcb024507bbc95a00adced137.webp)

## Configure a Snapshot Plan and Retention Policy

A snapshot plan automatically creates snapshots at fixed intervals, such as daily, weekly, or monthly, providing ongoing data protection without manual intervention.

**Steps:**

1. On the "Snapshot" home page, select the folder for which you want to configure a snapshot plan, then click "**Settings**".

![](https://file-us.ugreennas.com/admin/article/2026-09-07/99c3af44784641b1a653046427fd345e.webp)

2. In the "Settings" window, enable "**Snapshot plan**".

3. Configure the running mode, running date, and first running time. The system will automatically create snapshots according to the configured schedule.

4. Enable "**Retention policy**" to manage the number of stored snapshots and the storage space they use.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/a00130965dda47a39640d891dbef9a82.webp)

5. After confirming the settings, click "**Confirm**" to apply the changes.

**Recommended Configuration**

|  |  |  |
| --- | --- | --- |
| **Setting** | **Description** | **Recommendation** |
| Running mode | Supports daily, weekly, or monthly schedules | Create snapshots monthly to reduce storage usage |
| First running time | Time when the scheduled task starts | Choose an off-peak period, such as 2:00–4:00 a.m. |
| Retention policy | Custom retention period or snapshot count | Retain snapshots from the most recent 7 days or the latest 5 snapshots |

**Snapshot Plan Notes**

● Make sure the NAS is **powered on and running** at the scheduled snapshot time. Otherwise, the snapshot plan cannot be executed.

● Adjust the snapshot frequency based on available storage capacity and data volume to avoid excessive storage usage.

## Snapshot Retention Policy

A retention policy allows the system to automatically maintain snapshots based on either the number of snapshots to retain or a specified retention period. This helps prevent unnecessary storage usage caused by keeping too many snapshots or retaining them for too long.

### Configure Retention

You can configure either of the following retention policy types:

● **By snapshot amount:** Specifies the maximum number of snapshots the system will retain. When the number of snapshots exceeds the configured limit, the oldest snapshot is automatically deleted.

● **By retention days:** Specifies how many days snapshots are retained. When a snapshot exceeds the configured retention period, it is automatically deleted.

**For example**, you can configure the system to retain up to 10 snapshots or retain snapshots for 30 days to make efficient use of storage space.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/999a535dca4e4924a27841b81325a33f.webp)

**Note:** Retention policies apply only to **unlocked** snapshots. Manually locked snapshots are not affected by the retention policy.

### Automatic Cleanup

To ensure efficient automatic snapshot maintenance, the system checks for and removes snapshots that exceed the retention policy at the following times:

● **When the snapshot service starts:** When the device restarts or the snapshot service is enabled, the system automatically checks for and deletes snapshots that exceed the retention policy.

● **When a snapshot is created:** After a snapshot is created manually or by a scheduled task, the system also performs a snapshot cleanup.

**Note:** After a snapshot is deleted, it may take some time for the storage space it occupied to be reclaimed.

## Restore and Clone

**Feature Overview**

**Restore:** Restores a folder to a previous state, including its data and permission settings. This is useful for recovering data after accidental deletion or modification.

**Clone:** Creates an exact copy of a folder, including all data and permission settings. This is useful when you need a separate copy of the folder structure and contents.

**Supported Items for Restore and Clone**

|  |  |  |
| --- | --- | --- |
| **Feature / Folder type** | **Restore** | **Clone** |
| Shared folder | Fully restores data, permissions, shared folder quota, and user permissions | Supported. The cloned copy contains the same data and permissions as the original folder |
| Personal folder | Restores data, permissions, user permissions, and quota | Not supported |

**Differences Between Restore and Clone**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Feature** | **Supported folder types** | **Purpose** | **Overwrites original data** | **Recommended use** |
| Restore | User folders and shared folders | Restores data to its state at a specified point in time | Yes | Recovering from accidental changes or data loss |
| Clone | Shared folders only | Creates an independent copy while preserving the snapshot data | No | Backing up or comparing data |

## Restore Snapshot Data

Snapshot restore returns the contents of a shared folder or user folder to the state captured at a specific point in time. It can be used to recover from accidental deletion, unintended changes, and other data issues.

**Steps:**

1. Open "**Snapshot**", select the target folder from the folder list, and click "**Snapshot list**".

2. In the snapshot list, locate the historical snapshot you want to restore, click the "**···**" button on the right, then select "**Restore**".

![](https://file-us.ugreennas.com/admin/article/2026-09-07/1a295cd0b87c4e26b897fc2a6c93181c.webp)

3. The system will display a prompt. Confirm to start the restore.

**Notes:**

● If a network folder is mounted in the shared folder, the shared folder cannot be restored. Unmount the network folder before restoring.

● Before restoring, make sure **no operations are in progress** in the folder, such as uploads, moves, copies, or file extraction, to avoid data conflicts or loss.

● A snapshot restore **cannot be undone**. Proceed with caution.

● Before restoring, the system automatically creates a snapshot of the folder's current state so that you have a recovery point if needed.

## Clone Snapshot Data

Snapshot cloning creates an independent copy based on a selected historical snapshot. It is useful for backup, comparison, and similar scenarios. **Cloning is supported only for shared folders.**

**Steps:**

1. Open **"Snapshot"**, select the target folder from the **"Shared Folder"** list, then click **"Snapshot list"**.

2. In the snapshot list, locate the snapshot to clone, click the **"···"** button on the right, then select **"Clone"**.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/f9b2555354114be7b2370e0477e4dd91.webp)

3. The system creates a new shared folder on the same Volume. Its name is similar to "**Original folder name-Clone**", and its contents match the selected snapshot.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/b95482feccbf407c8e32392224795fc5.webp)

## Delete Snapshots

In the snapshot list, select the snapshot you want to delete, click the "**···**" icon, then select "**Delete**".

![](https://file-us.ugreennas.com/admin/article/2026-09-07/10f453fd0fb141e69b9e6e0bff4f568a.webp)

To delete multiple snapshots, hold Shift or Ctrl while selecting snapshots, then follow the same steps.

**Note:** A locked snapshot can only be removed when you manually perform the "**Delete**" operation.

## Uninstall Snapshot

To uninstall **"Snapshot"**, use **"App Center"**.

**Steps:**

1. Open **"App Center"**, locate **"Snapshot"**, and open its details page.

2. On the app details page, click the **"···"** button in the upper-right corner>**"Uninstall"**.

3. In the uninstall confirmation dialog, if you also want to delete the snapshot data, select "**Snapshot files for all shared folders and personal folders**".

![](https://file-us.ugreennas.com/admin/article/2026-09-07/fe23873ef45f430184e50d5083ac58eb.webp)

4. Click "**Uninstall**" and wait for the process to complete.

**Note:** Once deleted, the associated snapshot data cannot be restored through the Snapshot app.
