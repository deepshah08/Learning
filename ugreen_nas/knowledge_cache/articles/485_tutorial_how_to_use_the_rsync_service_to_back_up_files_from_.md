# [Tutorial] How to Use the Rsync Service to Back Up Files from a Remote Server to a Local UGREEN NAS?

> **Article ID**: `485`  
> **Category**: `Application Guide > Sync & Backup > [Tutorial] How to Use the Rsync Service to Back Up Files from a Remote Server to a Local UGREEN NAS?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/485  

---

## What is rsync?

In a NAS device, an **rsync server** (or **remote server**) refers to a server that supports the rsync protocol, enabling efficient data synchronization, backup, or transfer between different devices. Remote Sync (rsync) is a fast and versatile file copying tool widely used for quickly and securely synchronizing files and folders, especially in NAS environments. For example, you can set up an rsync server on one NAS device, while another device (e.g., a computer or a second NAS) acts as a client to initiate data transfer requests for synchronization or backup.

### Advantages of Rsync Service

rsync operates very efficiently and supports incremental backups. It transfers only the differences between the source files and the destination files instead of the entire files, significantly reducing network bandwidth usage, which is ideal for frequent large data transfers.

### Applicable Scenarios for Rsync Service

● Data Backup: UGOS Pro supports backing up important data from servers to the UGREEN NAS using rsync, ensuring data security.

● Multi-Device File Synchronization: Synchronize files or folders across multiple devices to maintain version consistency.

● Data Migration: During data migration, rsync can be used to transfer NAS data to a remote server for seamless transitions.

## How to Enable Sync Service in UGOS Pro?

1. Go to **[Control Panel** > **File Service]**.

2. Find the "**rsync**" option and enable the rsync service.

3. Select the account to use with the rsync service and set the corresponding password.

4. Click "**Apply**" to save and activate.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/99ec4927fa4943f195cdfb1fd48e5418.webp)

5. By default, the rsync service uses a specific port `873` for data transmission and communication. To prevent malicious attackers from discovering the rsync service by scanning default ports or to address port conflicts, you can click [Advanced] to modify the default port number.

## How to Use the Rsync Service to Back Up Remote Server Files to the Local UGREEN NAS?

![](https://file-us.ugreennas.com/admin/article/2025-09-10/21c171b0bece4d1b8c37a7854fdc98a5.webp)

1. Ensure that the remote server (e.g., a computer or another NAS) has the rsync service installed or enabled.

2. On the local UGREEN NAS, open the [Sync & Backup] application and navigate to "Backup & Restore".

3. Choose the backup type "**Backup rsync server**" to back up remote server data to the local UGREEN NAS. Click "**Next**".

4. In the [Remote rsync server] popup window, enter the following information and click "Confirm".

● **Server Name/IP Address**: Enter the IP address of your remote server (e.g., the computer or another NAS).

Note: IP addresses support both IPv4 and IPv6. If the devices are not in the same LAN, enter the public IP or DDNS domain name.

● **Port:** Default is 873.

● **Transfer Encryption**: Choose whether to enable transfer encryption as needed to ensure secure data transmission.

● **User name and Password**: Enter the user name and corresponding login password used to connect to the rsync file server (set when enabling rsync service).

![](https://file-us.ugreennas.com/admin/article/2025-09-10/a4acc1754eeb4985bd6384ab157e0068.webp)

5. If the connection to the remote server is successful, proceed to select the backup source and destination. After setup, click "Next".

● **Backup Source**: Select the folders on the remote server that need to be backed up to the local UGREEN NAS. You can also set "Filter Rule" to limit file size. Files exceeding the set size will not be backed up. Additionally, you can set "Filter File Names or Extensions".

● **Backup Destination**: Choose the local storage path on the UGREEN NAS to store the backup files.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/69a72d9b29c64791ac2355c9e6568420.webp)

6. Set the **Backup Mode** and **Plan** as needed, then click "Next".

![](https://file-us.ugreennas.com/admin/article/2025-09-10/423331811aa54869bc6a89489e215b58.webp)

7. Name the backup task. To start the backup immediately after task creation, check "Back up immediately after creation".

![](https://file-us.ugreennas.com/admin/article/2025-09-10/85c58083563a404a8ef3758f33ccca93.webp)

8. After verifying the configuration is correct, click "Confirm" to create the backup task.

## Notes

1. Ensure that both the rsync service and client have the correct read/write permissions to avoid synchronization failures.

2. Keep the directory structure of the backup source and destination consistent during synchronization to avoid errors caused by structural changes.

3. If the remote server cannot be connected, check that the user account and password configured for rsync and the server name/IP address and port to be connected are correct, and ensure that the target device has the "rsync service" enabled.

4. When using a LAN IP connection, ensure that theUGREEN NAS and the other device or computer are in the same LAN.
