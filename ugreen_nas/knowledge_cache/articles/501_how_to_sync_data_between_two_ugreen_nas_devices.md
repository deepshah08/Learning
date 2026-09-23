# How to Sync Data Between Two UGREEN NAS Devices?

> **Article ID**: `501`  
> **Category**: `Application Guide > Sync & Backup > How to Sync Data Between Two UGREEN NAS Devices?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/501  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS)

**Applicable Version**: UGOS Pro Firmware 1.18.0.0093 or later

The screenshots in this document are for reference only. The actual interface may vary slightly depending on the system or app version, please refer to the actual interface displayed.

## Introduction

In home or office environments, you may need to keep data synchronized between two UGREEN NAS devices. With the "**Sync & Backup**" app in UGOS Pro, you can easily sync data between UGREEN NAS devices and keep important files consistent across multiple devices.

## Prerequisites

Before using this feature, make sure the following requirements are met:

● Prepare two UGREEN NAS devices running **UGOS Pro** **System** and make sure both devices are connected to the network.

● It is recommended that both NAS devices be on the same LAN. If they are on different networks, use UGREENlink, a public IP address, or DDNS (Dynamic DNS) to establish a connection.

● Make sure the "**Sync & Backup**" app is installed on both NAS devices.

● Check that the date, time, and time zone settings are consistent on both devices to prevent synchronization issues caused by time differences.

## Create a Sync Task

1. Log in to UGOS Pro, open "**Sync & Backup**", go to "**Sync**"> "**New sync task**".

2. Under Sync Target, select "**Sync another UGREEN NAS**", then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-08-13/30bdc50970424f62b7afe62d5f341f42.webp)

3. Enter the connection information for the remote NAS, then click "**Confirm**" to connect:

![](https://file-us.ugreennas.com/admin/article/2026-08-13/4f9028e6ae31401aae1ea3280a4a83c9.webp)

● **IP address or UGREENlink ID**: Enter the LAN IP address of the target NAS (such as 192.168.22.141) or the UGREENlink ID (such as ugreen).

● **Transmission Encryption**: It is recommended to enable this option to secure data transmission.

● **Port**: The default port for a standard connection is 9999 and normally does not need to be changed. If Transmission Encryption is enabled, change the port to 9443, the system's default encrypted connection port.

● **Username and Password**: Enter the **Administrator account** and **Password** of the remote NAS.

**Note**: If the two NAS devices are not on the same LAN, use UGREENlink, a public IP address, or DDNS to establish the connection.

4. After the connection is established, configure the following sync rules:

![](https://file-us.ugreennas.com/admin/article/2026-08-13/6f138aa186f147deb58617384d2fdb8c.webp)

● **Remote path**: Select the folder on the remote NAS to be synchronized.

● **Local path**: Select the folder on the local NAS to be synchronized.

● **Sync direction**: The following three directions are supported:

|  |  |
| --- | --- |
| **Sync direction** | **Description** |
| Two-way sync | Synchronizes files between the local NAS and remote NAS in both directions to keep data consistent on both devices. |
| One-way sync | Only changes to the local data will be synchronized to the remote path. Deleting local files won't affect the remote files. |
| One-way sync | Only changes to the remote data will be synchronized to the local path. Deleting the remote files won't affect the local files. |

(Optional) Click "**Advanced Settings**" to configure **folder and file name filtering rules** and **file conflict handling rules**.

5. Configure the Sync policy as needed. The following options are supported:

![](https://file-us.ugreennas.com/admin/article/2026-08-13/d4289bc510454e1db0b38c0f99b19b64.webp)

● **Real-time Sync**: Synchronizes immediately when the system detects file changes.

● **Manual Sync**: Runs only when you manually click "**Sync now**".

● **Sync As Planned**: Runs automatically based on the configured frequency (such as weekly) and start time (such as 2:00 AM on January 1, 2026).

● **NAS Recycle Bin**: Configure an automatic cleanup schedule for the NAS Recycle Bin as needed.

6. After completing the settings, click "**Next**".

**Note**: The sync task depends on both devices operating normally. If either device is interrupted, synchronization will stop.

7. Preview and verify all settings for the sync task. You can customize the Task Name for easier identification. After confirming that all settings are correct, click "**Confirm**" to create the task.

![](https://file-us.ugreennas.com/admin/article/2026-08-13/78621710854243f48c4bcf9ad31eb410.webp)

## Manage Sync Tasks

After a task is created, you can view its status and progress on the "**Sync**" page. The following operations are supported:

![](https://file-us.ugreennas.com/admin/article/2026-08-13/d2a1cff935974d4386cae4bf40e20e71.webp)

● **Create sync task**: Click the "**···**" icon to create a new sync task.

● **Connection management**: Delete the connection and all sync and backup tasks under it.

● **Pause/Resume task**: Pause or resume a sync task.

● **Edit Task**: Modify the sync rules, sync policy, or advanced settings.

● **NAS Recycle Bin**: NAS files deleted during synchronization are moved to the "#SyncVersion folder", where they can be permanently deleted.

● **Delete Task**: Remove a sync task that is no longer needed.

## Notes

1. If the remote NAS cannot be connected via its IP address, troubleshoot in the following order:

● Make sure the router has the correct port forwarding rules configured. For a standard connection, port 9999 must be forwarded. If Transmission Encryption is enabled, ports 9443 and 22000 must be forwarded (22000 is used specifically for encrypted data transmission).

● Check the firewall rules on the NAS and gateway devices such as the router, and make sure the ports used by "**Sync & Backup**" are allowed to access the network.

● If you are connecting via a public IP address and the IP changes frequently, it is recommended to configure DDNS to obtain a stable domain name.

2. When transferring large files or large amounts of data, it is recommended to connect the devices to a Gigabit or 2.5G network to improve transfer efficiency.

3. Avoid running too many sync tasks at the same time, as this may result in insufficient network bandwidth or reduced device performance.

4. The sync feature is primarily intended to keep data consistent between devices. For better data protection, it is recommended to regularly back up important files to a separate storage device.
