# Backup to External Hard Drive/USB Drive

> **Article ID**: `679`  
> **Category**: `Application Guide > Sync & Backup > Backup to External Hard Drive/USB Drive`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/679  

---

In the UGOS Pro system, the [Sync & Backup] app not only supports internal file synchronization and remote backup for NAS, but also provides the option to back up data to locally connected storage devices (such as external hard drives or USB drives). This feature is suitable for scenarios where users want to create local offline backups of important data, offering an extra layer of protection for data security.

## **User Guide**

1. Open the [Sync & Backup] app and select [Backup & Restore] from the left sidebar.
2. Click the "Add" button in the upper-right corner of the page. In the pop-up window for selecting a backup type, choose "Backup Between Storage Pools" and click "Next" to continue.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250603/3a1c06ed-660a-4ca6-8f97-b425d553759c.png)

3. Next, select the folders you want to back up. Click the [Backup Source] field to choose one or more internal folders on the NAS as the backup source (multiple backup sources are supported).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250603/634e672a-8eb0-42b3-9c49-f64e764d22fc.png)

4. In the [Backup Destination] section, select the target folder on the mounted external hard drive or USB drive. If the external device is not displayed, please ensure it has been properly inserted and mounted (you can check this in [Files]).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250603/ee0147e4-d2e0-417b-927b-714ef4a8cc81.png)

5. **Set Filter Rule (Optional)**

To improve backup efficiency or streamline backup content, users can set filter rule in the backup task:

* **Exclude file size:** skip files exceeding the specified size.
* **Exclude specific file types:** such as `.tmp`, `.log`, and other temporary or log files

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250603/5135cd28-7e9b-4b00-a877-536f07d77cd2.png)

6. After completing the settings, click "Next" to proceed to the next step.
7. UGOS Pro offers two backup modes: choose Incremental Backup if you want to retain previous backup files, or choose Mirror Backup if you need the destination to be exactly the same as the source. Select the mode according to your needs, then click "Next" to continue.

|  |  |  |
| --- | --- | --- |
| **Backup Type** | **Features** | **Handling When Source Files Are Deleted** |
| **Incremental Backup (Recommended)** | Performs a full backup the first time, then only backs up newly added or modified files. | Backup files are retained even if the source files are deleted. |
| **Mirror Backup** | The destination device is kept exactly consistent with the source directory, including deletion operations (synchronized deletion or addition of files). | Backup files are deleted when the corresponding source files are deleted. |

8. Set the backup plan. To avoid affecting daily usage, it is recommended to schedule the task during off-peak hours, such as at night.
9. Once configuration is complete, click “Next” to proceed.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250603/85e64621-8b40-4bbb-965e-b694cb18b89e.png)

10. On the [Preview] page, you can edit the task name, review the source and destination paths, as well as the backup mode and schedule configuration. After confirming all settings, click “Confirm” to immediately create and execute the backup task.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250603/996a63ca-3d77-499c-b261-3f88573a5a93.png)

## **Notes**

* All tasks are centrally managed on the [Backup & Restore] page, where you can view progress, execution history, or manually run tasks at any time.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250603/b4324249-77da-442f-9cd7-17314e13fe5c.png)

* The [Backup Between Storage Pools] feature not only supports backups between multiple storage pools, but is also applicable for backing up data to external storage devices mounted to the system.
