# How to Create a File Sync Task Between UGREEN NAS and a Local Computer?

> **Article ID**: `399`  
> **Category**: `Application Guide > Sync & Backup > How to Create a File Sync Task Between UGREEN NAS and a Local Computer?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/399  

---

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS)

**Applicable Version**: NAS Firmware 1.18.0.0093 or later

The screenshots in this document are for reference only. The actual interface may vary slightly depending on the system or app version, please refer to the actual interface displayed.

## Introduction

With the "**Sync this computer**" feature, you can keep specified folders on your computer synchronized with your UGREEN NAS, ensuring consistent data across multiple devices.

**Note**: Sync tasks require the UGREEN NAS PC client to be running. Sync operations will stop automatically after the client is closed.

## Install the UGREEN NAS PC Client

1. Visit the [Download Center](https://ai.ugreen.com/pages/downloads) on the UGREEN NAS official website, download and install the UGREEN NAS PC client compatible with your device model.

2. Open the UGREEN NAS App and log in to the UGOS Pro system.

## Set Sync Target

1. Go to "**Sync&Backup**" > "**Sync**".

2. Click "**Add**", select "**Sync this computer**", and click "**Next**" to start creating a sync task.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/ccf972e46d3f4895af3ddab7de881488.webp)

## Set Sync Rules

In the sync rules settings page, specify the sync paths and sync direction:

![](https://file-us.ugreennas.com/admin/article/2026-08-12/03e6908fec0b466ca8e39a3bfc7ce0a3.webp)

**Select Sync Paths**

● **Computer Path**: Select the folder on your computer that you want to sync.

● **UGREEN NAS Path**: Select the corresponding target folder on your UGREEN NAS.

**Select Sync Direction**

|  |  |
| --- | --- |
| **Sync Method** | **Description** |
| Two-way sync | Synchronizes files between the computer and UGREEN NAS in both directions, keeping data on both sides consistent. |
| One-way sync | Only syncs data changes from UGREEN NAS to the computer. When files are deleted on the NAS, the corresponding files on the computer will not be deleted. |
| One-way sync | Only syncs data changes from the computer to UGREEN NAS. When files are deleted on the computer, the corresponding files on the NAS will not be deleted. |

**Example**:

If you want to keep the "**Project Documents**" folder on your computer synchronized with the "**Shared Folder A**" folder on your NAS, select "**Two-way sync**". After setup, any file changes made on either device will be automatically synchronized to the other side.

If you want to sync the same data across multiple computers, create a separate sync task on each computer and set the UGREEN NAS Path to the same "**Shared Folder A**" folder.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/cbe4a414958e455685da127e81fe1f14.webp)

### Configure Advanced Settings

In Advanced Settings, you can further configure the details of the sync task.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/0de074142185409fb4c6939bcc8ed843.webp)

#### File Filter

You can exclude specific files or folders from syncing to avoid unnecessary use of sync resources.

● **Hidden File Filter**: By default, hidden files and folders prefixed with **.** are not synced. To sync these files, manually enable this option.

● **Custom Filter Rules**: Select "**Filter the following file (folder) names or file extensions**" to add or remove filter rules as needed:

**Add Rules**: Click "**Add**" and enter a file name or extension. Multiple rules can be separated with an English semicolon "**;**".

**Delete Rules**: Hover over the rule and click the floating "**×**" icon to delete it.

**Filter Rule Examples**:

|  |  |  |
| --- | --- | --- |
| **Filter Type** | **Example** | **Description** |
| Specific file name | `abc.doc` | Does not sync files named abc.doc |
| Wildcard match | `test*.doc` | Does not sync files starting with test and ending with .doc |
| Extension filter | `*.jpg` | Does not sync all JPG image files |

#### File Conflict Handling

When the same file is modified on both the computer and NAS at the same time, the system will handle the conflict according to the selected rule:

● **Keep the new file and rename the old file** (default): The system automatically adds a suffix to files with the same name to prevent data from being overwritten.

● You can also select other conflict handling methods based on your needs.

## Set Sync Policy

After completing the sync rules settings, click "**Next Step**" to enter the sync policy settings page:

![](https://file-us.ugreennas.com/admin/article/2026-08-12/7631d3b526c7425dbd926502a0805eec.webp)

● **Real-time Sync**: The system automatically performs sync when file changes are detected (recommended).

● **Manual Sync**: Sync is performed only when you manually click "**Sync Now**".

After making your selection, click "**Next Step**" to preview the sync task.

## Preview and Manage Tasks

In the preview interface, you can:

![](https://file-us.ugreennas.com/admin/article/2026-08-12/fbf4afeafa2040498c32aad938434d2d.webp)

● Customize the name of the sync task.

● Review all configured settings.

● If changes are needed, click "**Previous**" to return and modify the settings.

● After confirming that all settings are correct, click "**Confirm**" to create the sync task.

### Manage Tasks

After creating a sync task, you can manage sync devices and tasks in the "**Sync**" interface:

![](https://file-us.ugreennas.com/admin/article/2026-08-12/ba850c9d204845a0a0abf2049547c8c8.webp)

● **Suspend/Resume Sync**: Click "**Suspend sync**" to pause the current sync task. Click again to resume syncing.

● **Edit**: Click "**More**" > "**Edit**" to modify sync settings.

● **Computer Recycle Bin**: Click "**More**" > "**Computer Recycle Bin**" to view files deleted from the UGREEN NAS sync path.

● **NAS Recycle Bin**: Click "**More**" > "**NAS Recycle Bin**" to view files deleted from the computer sync path.

● **Delete**: Click "**More**" > "**Delete**" to remove the sync task.

● **Quickly Create a New Task**: Click the "**···**" button on the right side of a sync device to quickly create a new sync task for that device.

### Desktop Tray Program Display

Click the UGREEN NAS icon in the local computer taskbar to quickly view the transfer status of files in Sync&Backup tasks and pause ongoing transfer tasks.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/dd1ab323891e4f269a01cf809376283f.webp)
