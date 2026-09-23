# How to Back Up Data from a Local UGREEN NAS to Another NAS?

> **Article ID**: `928`  
> **Category**: `Application Guide > Sync & Backup > How to Back Up Data from a Local UGREEN NAS to Another NAS?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/928  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: UGOS Pro Firmware 1.18.0.0093 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

If you have multiple UGREEN NAS devices and want to back up data from a local UGREEN NAS to another UGREEN NAS, you can use the "**Back up this UGREEN NAS**" feature in the "**Sync & Backup**" app on UGOS Pro. This helps protect your data and prevent data loss caused by local device failure.

## Prerequisites

● The latest version of the "**Sync & Backup**" app is installed on both UGREEN NAS devices.

● rsync or WebDAV is enabled on both UGREEN NAS devices, and the required connection information is available, including the server (NAS) address, port, username, and password.

● Both NAS devices are on the same LAN (If they are on different networks, you can connect using a DDNS domain name or public IP address).

**Note**: To back up data from a local UGREEN NAS to a NAS from another brand or to a remote server, make sure the destination device supports and has enabled the rsync or WebDAV file service protocol. For compatibility details, contact the device manufacturer.

## Enable rsync or WebDAV on the NAS

1. Sign in to UGOS Pro and open "**Control Panel**".

2. Go to "**File Service**", then select rsync or WebDAV.

3. Using rsync as an example, select "**Enable rsync backup service**", then set the rsync account and Password. Click Advanced to view or configure the port number (The default rsync port is 873).

4. Click "**Apply**" to save the settings.

![](https://file-us.ugreennas.com/admin/article/2026-08-14/2541a52c9dc245518ad3a17435245a7f.webp)

## Create a Backup Task and Select the Backup Destination

1. Sign in to UGOS Pro on the local UGREEN NAS and open the "**Sync & Backup**" app.

2. Go to "**Back up & Restore**, click "**Add**", and select "**Backup this UGREEN NAS**".

![](https://file-us.ugreennas.com/admin/article/2026-08-14/b7065c39f99f4ce3ae4560b1581c706c.webp)

## Connect backup destination server

On the "**Connect backup destination server**" page, you can connect to another NAS using either the rsync or WebDAV protocol.

### Method 1: Connect to an rsync server

![](https://file-us.ugreennas.com/admin/article/2026-08-14/98276ee6fc204adda0ad27a4997a90b9.webp)

Enter the following connection information:

● **Server address**: Enter the IP address or domain name of the remote rsync server (the other UGREEN NAS).

● **Transmission Encryption**: Turn this on as needed to secure data transmission.

● **Port**: Enter the communication port (The default port is 873).

● **Username**: Enter the username for connecting to the rsync server (the other UGREEN NAS).

● **Password**: Enter the corresponding password.

After confirming that the information is correct, click "**Confirm**" to continue. If you have connected to this server before, select "**Existing connection**" and choose it directly from the drop-down list.

### Method 2: Connect to a WebDAV server

![](https://file-us.ugreennas.com/admin/article/2026-08-14/8be0358ddcd24543bb92afea9a0df2a9.webp)

Enter the following connection information:

● **Server address**: Enter the IP address or domain name of the remote WebDAV server (the other UGREEN NAS).

● **Protocol**: Select HTTPS (encrypted transmission) or HTTP as needed.

● **Port**: Enter the communication port (The default port is 5005 for HTTP and 5006 for HTTPS).

● **Root folder**: Enter the path to the shared folder on the WebDAV server (the other UGREEN NAS). **Root folder path example** (using a UGREEN NAS as an example): If the shared folder is named downloads, enter /downloads.

**Note**: The path must exactly match the shared folder name and is case-sensitive (For example, /Downloads is not the same as /downloads).

● **Username**: Enter the username for connecting to the WebDAV server (the other UGREEN NAS).

● **Password**: Enter the corresponding password.

After confirming that the information is correct, click "**Confirm**" to continue. If you have connected to this server before, select "**Existing connection**" and choose it directly from the drop-down list.

## Select the Backup Source and Destination

On the "**Selection**" page, configure the following:

![](https://file-us.ugreennas.com/admin/article/2026-08-14/4f5a35c57b504f139dbb063dab5645b1.webp)

● **Source**: Select the local folders you want to back up (You can select multiple folders).

● **Backup destination**: Select the destination path on the remote server (the other UGREEN NAS).

● **Filter Rule** (optional): Set filter rules based on **Limit** **file size** and **File names (folders) or file extensions**. After confirming the settings, click "**Next**".

## Set the Backup Plan and Version Retention Policy

On the "**Backup settings**" page, configure the following:

![](https://file-us.ugreennas.com/admin/article/2026-08-14/e1b5dad7fd744fe783ca60f0a6013ea7.webp)

● **Backup plan**: Select Every Day, Weekdays, Weekends, or Custom, and set the backup start time.

● **Backup version policy**: Select "**Enable**" to customize the number of backup versions to retain.

After completing the settings, click "**Next**".

## Preview and Manage Backup Tasks

On the "**Preview**" page, you can:

![](https://file-us.ugreennas.com/admin/article/2026-08-14/31e9b22dcbdc4702b0a4802bf24ab9d1.webp)

● Customize the Task Name.

● Review all backup settings.

● Select "**Back up immediately after creation**" to start the first backup immediately after the task is created.

Click "**Confirm**" to complete the task creation.

### Task Management

After the task is created, you can manage it from "**Back up & Restore**":

![](https://file-us.ugreennas.com/admin/article/2026-08-14/6c49380ee86e4d27b1480b5e823213af.webp)

● Click "**···**" on the right side of the device to quickly create a new task, add or edit a device note, or delete the device connection.

● Manually start or stop a backup task.

● Click "**More**" to view the backup version list, edit the task, or delete the task.
