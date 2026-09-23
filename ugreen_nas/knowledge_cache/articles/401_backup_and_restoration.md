# Backup and Restoration

> **Article ID**: `401`  
> **Category**: `Application Guide > Sync & Backup > Backup and Restoration`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/401  

---

In **[Sync & Backup]**, backup is the process of copying data to another location to prevent data loss. Unlike synchronization, backup does not overwrite the original data. The primary goal of backup is to ensure that original data can be restored in the event of data corruption, accidental deletion, or hardware failure.

## **Access the Backup & Restore Interface**

To use the [**Backup and Restore]** feature, follow these steps to access the interface:

1. Open the UGOS Pro and go to the App Library.
2. Navigate to the **Sync & Backup** app and click to open it.
3. In the **Sync & Backup** app, select the **Backup and Restore** option to enter the backup and restore settings.

If you haven't installed the **Sync & Backup** app yet, visit the **App Center** and follow these steps to install it:

1. Open the **App Center**.
2. Enter "**Sync & Backup**" in the search bar and search.
3. Locate the **Sync & Backup** app and click the "**Install**" button to install it.

Once the installation is complete, follow the steps above to access the **[Backup and Restore]** interface and begin setting up your backup and restore tasks.

In the **[Back up & Restore]** interface, you can:

* View and manage connected backup devices.
* Manage backup tasks on these devices.
* Click "**Add"** to create new backup tasks, such as backing up UGREEN NAS to a remote server, backing up a remote server to UGREEN NAS, or backing up computer data to UGREEN NAS.
* Click the "**Restore**" button to restore backup files from a remote server back to UGREEN NAS. You can choose to restore by backup task or select specific backup files to restore.

![](https://ugreen-pro.oss-cn-shenzhen.aliyuncs.com/ugreen-pro/admin/article/20241211/e63a3e69-5e53-434c-8daf-bf1a4b5cafa2.png)

## **Backup Modes Supported by UGOS Pro**

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250303/a189e547-6605-4e05-a474-aa53a562bd63.png)

1. **Back Up UGREEN NAS to a Remote Server**

This backup mode is designed to back up data from the local UGREEN NAS to a remote server. It is ideal for scenarios where offsite backups are needed to enhance data security and disaster recovery capabilities. The system supports multi-version backups, allowing users to choose how many backup versions to retain for recovery to a specific point in time when needed.

2. **Back Up a Remote Server to UGREEN NAS**

This backup mode is used to back up data from a remote server (such as an rsync server) to the local UGREEN NAS, ensuring that remote server data is securely stored and managed locally. It supports setting up automatic backup tasks that, according to the user-configured schedule, automatically back up computer files to the NAS.

3. **Back Up a Computer to UGREEN NAS**

This mode is designed for backing up files from personal computers to UGREEN NAS, allowing users to centrally manage and protect their personal data. It supports incremental backups, which only back up changed file content, as well as image backups that create a complete copy of the computer's data on the NAS.

## Differences Between Sync and Backup

1. **Purpose**

   * **Sync**: The main goal of sync is to keep files consistent across multiple devices. It ensures that the content on each device is identical, so changes made on one device are reflected on the others.
   * **Backup**: Backup is all about protecting your data. Its primary purpose is to safeguard against data loss or corruption, allowing you to restore your original files if something goes wrong.
2. **Data Flow Direction**

   * **Sync**: Sync allows for **two-way data flow**, meaning files can be updated on both devices and changes are automatically synchronized.
   * **Backup**: Backup typically follows a **one-way flow**, where data is copied from one device to a storage device, leaving the original data intact and unchanged.
3. **Data Overwrite**

   * **Sync**: In syncing, older versions of files may be **overwritten** by newer versions to ensure that all devices have the same, up-to-date content.。
   * **Backup**: With backups, **older versions are preserved**. Each backup creates a new version, so you can always go back and restore a previous version of your files if needed.

**Practical Tips**

* **Use Sync for Work Files:** Sync is ideal for files that are frequently accessed and updated. It ensures that changes are reflected across all devices, making it perfect for collaborative or active work files.
* **Use Backup for Important Data:** For critical data, it's best to perform regular backups and store them in a physically separate location, such as an external hard drive or cloud storage. This helps ensure that your important files are protected in case of accidental loss or damage.
