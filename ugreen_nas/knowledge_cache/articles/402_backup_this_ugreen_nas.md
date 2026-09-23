# Backup This UGREEN NAS

> **Article ID**: `402`  
> **Category**: `Application Guide > Sync & Backup > Backup This UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/402  

---

## Applicability

**Applicable Clients**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: UGOS Pro firmware 1.18.0.0093 or later

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

Backing up data from your local UGREEN NAS to a remote rsync or WebDAV file server (such as another UGREEN NAS) helps protect your data and prevent data loss if the local device fails. You can easily complete this task from the "**Back up & Restore**" page.

## Prerequisites

● The "**Sync & Backup**" app is installed on the local NAS.

● The remote server has rsync or WebDAV enabled, and you have the required connection information (server address, port, username, password, etc.).

● The local NAS and remote server can communicate over the network (if the two devices are not on the same LAN, you can connect using a DDNS domain name or public IP address).

**Note**: To back up data from your local UGREEN NAS to a third-party NAS or remote server, make sure the destination device supports and has enabled the rsync or WebDAV file service protocol. Contact the device manufacturer for compatibility details.

## Create Backup Task

1. Go to "**Sync & Backup**" > "**Back up & Restore**".

2. Click "**Create backup task**", select "**Backup this UGREEN NAS**", then click "**Next**" to start creating a backup task.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/679e42f6f03747a2901b13edff7083b0.webp)

## Connect Backup Destination Server

On the "**Connect backup destination server**" page, select an rsync or WebDAV file server and enter the required information as described below.

### Method 1: rsync Server

![](https://file-us.ugreennas.com/admin/article/2026-09-09/054f6487bf5945c8a9d16bd085cfeda8.webp)

Enter the following connection information:

● **Server address**: Enter the IP address or domain name of the remote rsync server.

● **Transmission Encryption**: Enable it as needed to help protect data during transmission.

● **Port**: Enter the communication port used by the device (default: 873).

● **Username**: Enter the username used to connect to the rsync file server.

● **Password**: Enter the corresponding login password.

After confirming that the information is correct, click "**Confirm**" to continue. If you have connected to this server before, select it directly from the "**Existing connection**" drop-down menu.

### Method 2: WebDAV Server

![](https://file-us.ugreennas.com/admin/article/2026-09-09/c2e0a3ff8924458897b4c194f26b4857.webp)

Enter the following connection information:

● **Server address**: Enter the IP address or domain name of the remote WebDAV server.

● **Protocol**: Select HTTPS (encrypted transmission) or HTTP as needed.

● **Port**: Enter the communication port (default HTTP port: 5005; default HTTPS port: 5006).

● **Root folder**: Enter the shared folder path on the WebDAV file server.

● **Username**: Enter the username used to connect to the WebDAV file server.

● **Password**: Enter the corresponding login password.

After confirming that the information is correct, click "**Confirm**" to continue. If you have connected to this server before, select it directly from the "**Existing connection**" drop-down menu.

**Additional Information**

**Root Folder Path Example** (UGREEN NAS):

|  |  |
| --- | --- |
| **Shared Folder Name** | **Path to Enter** |
| `downloads` | `/downloads` |
| `documents` | `/documents` |

**Path Entry Considerations**:

● **Case Sensitivity**: Make sure the path name exactly matches the Shared Folder name (for example,`/Downloads`and `/downloads` are not the same).

## Select the Backup Source and Destination

On the "**Backup Selection**" page, complete the following settings:

1. **Select Source**: Select the local folders you want to back up (multiple selections are supported).

2. **Select Backup destination**: Select the destination storage path on the remote server.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/e931c2510757478cb3486ce3cb940d6c.webp)

**Set Filter Rule (Optional)**

Use filtering rules to exclude files that do not need to be backed up:

● **Limit file size**: Check "**Limit file size**" and set the maximum file size. Files larger than this limit will not be backed up.

● **Filter file names or files extensions**: Check "**Filter the following file names(folders) or file extensions**" to add or remove filtering rules:

●   **Add rule**: Click "**Add**" and enter a file name or extension (separate multiple entries with an English semicolon ";").

●   **Delete rule**: Hover over the rule field and click the floating "**×**" to delete it.

Default excluded formats: The system excludes temporary files such as *.lnk*, .swp, .*temp*, and .tmp by default. You can adjust these settings as needed.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/6bdefedc587949a6a47b705f8672f8f8.webp)

3. After confirming that the settings are correct, click "**Next**".

## Set Backup Plan and Backup Version Policy

On the "**Backup Settings**" page, configure the following:

**Plan**

Click "**On**" to configure a backup schedule. Choose daily, weekdays, weekends, or custom dates, and set the backup start time.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/5011eec08cfc418687891f93d3af9b52.webp)

**Backup Version Policy**

This feature supports multi-version differential backups and retains multiple backup versions. Once enabled, the system keeps the latest backup versions based on the retention count you set. After checking "**On**", the system retains only the latest version by default. You can also customize the number of versions to retain.

When finished, click "**Next**".

## Preview and Create the Task 1

On the "**Preview**" page, you can:

![](https://file-us.ugreennas.com/admin/article/2026-09-09/70a59f92a22747dd806a68b7a0df52b8.webp)

● Customize the task name.

● Review all settings and make sure they are correct.

● Check "**Back up immediately after creation**" to run the first backup as soon as the task is created.

● Click "**Confirm**" to create the task.

## Task Management

After the task is created, you can view and manage connected devices and backup tasks on the "**Back up & Restore**" page:

![](https://file-us.ugreennas.com/admin/article/2026-09-09/073a9730ae844a29bbbd74ea4a0c480b.webp)

● Click the "**···**" button on the right side of a device to quickly create a backup task or manage the connection.

In the backup task list:

● Click "**Back Up**" to start a backup manually.

● Click "**More**" to view the backup version list, edit the task, or delete the task.

## Notes

● **Version List**: This applies only to "**Backing Up UGREEN NAS to a Remote Server**" tasks. After "**Backup version policy**" is enabled, you can view the historical version list. Each backup creates a new version folder, so keep in mind that retaining more versions uses more storage space.

● **Backup File Encryption**: When UGREEN NAS data is backed up to a remote server, backup files are encrypted by default. Their actual contents can only be viewed after the files are restored from the remote server back to UGREEN NAS.

● **Network & Permissions**: If two devices on different LANs need to set up a file backup task, you can connect to the NAS using a DDNS domain name or public IP address and then create the backup. Make sure the other device supports and has enabled rsync/WebDAV services and that the required ports are mapped correctly. For details, see "[Rsync](https://support.ugnas.com/knowledgecenter/detail/article/en-US/81) " and "[WebDAV](https://support.ugnas.com/knowledgecenter/detail/article/en-US/82) ".
