# How to Create a File Backup Task Between a UGREEN NAS and a Computer？

> **Article ID**: `514`  
> **Category**: `Application Guide > Sync & Backup > How to Create a File Backup Task Between a UGREEN NAS and a Computer？`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/514  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS)

**Applicable Version**: NAS Firmware 1.18.0.0093 or later

The screenshots in this document are for reference only. The actual interface may vary slightly depending on the system or app version, please refer to the actual interface displayed.

## Introduction

With "**Backup this computer**", you can back up selected folders from your computer to your UGREEN NAS, providing an extra layer of protection for important data.

**Note**: Backup tasks require the UGREEN NAS PC client to remain running. If you exit the client, backup tasks will stop automatically.

## Install the UGREEN NAS PC Client

1. Go to the[Download Center](https://www.ugnas.com/download/) on the UGREEN NAS official website, then download and install the UGREEN NAS PC client for your device model.

2. Open the UGREEN NAS client and sign in with your UGOS Pro account.

## Set the Backup Destination

1. Go to "**Sync & Backup**" > "**Back up & Restore**".

2. Click "**Add**", select "**Backup this computer**", and start creating a backup task.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/82e369c822c24c458d91f669e08b2a2c.webp)

3. On the "**New backup task**" page, under Computer Path, select the folders on your computer that you want to back up to your UGREEN NAS. You can select multiple folders.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/ca96b99e615d47cb90bbacf60edb7612.webp)

4. Under Backup Destination, select a folder on your UGREEN NAS to store the backup files. You can select an existing folder in a personal or shared folder, or create a new folder manually.

5. To exclude files that you do not want to back up, click "**File Filter**" and configure the filtering rules. For details, see "**File Filter**" below.

6. After confirming your selections, click "**Next Step**" to continue.

## Set the Backup Policy

Under Backup settings, select a backup policy:

![](https://file-us.ugreennas.com/admin/article/2026-08-12/b318eeaf029b42babf97a147008e9dcc.webp)

|  |  |
| --- | --- |
| **Backup Method** | **Description** |
| Backup after file change | Automatically backs up files when changes are detected (recommended). |
| Manual Backup | Backs up files only when you manually click "**Back up**". |

**Note**: The system uses **incremental backup** by default, meaning that each backup only includes files that have been added or modified since the previous backup. Files deleted from the source after a backup are retained at the backup destination to help prevent data loss caused by accidental deletion.

### Configure File Filter

You can exclude specific files or folders from backup to prevent unnecessary files from taking up storage space.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/501fb97904324707a9c4178515661db1.webp)  
Select "**Filter the following file (folder) names or file extensions**". You can then add or delete filter rules as needed:

● **Add a rule**: Click "**Add**", then enter a file name or file extension. Separate multiple rules with semicolons ";".

● **Delete a rule**: Hover over a rule and click the "**×**" icon that appears to delete it.

**Filter rule examples**:

|  |  |  |
| --- | --- | --- |
| **Filter Type** | **Example** | **Description** |
| Specific file name | `abc.doc` | Does not back up files named abc.doc |
| Wildcard matching | `test*.doc` | Does not back up files whose names start with test and end with .doc |
| File extension | `*.jpg` | Does not back up any JPG image files |

## Preview and Manage the Task

On the Preview page, you can:

![](https://file-us.ugreennas.com/admin/article/2026-08-12/5c1359cd66ad4ba1a3d4222801660553.webp)

● Customize the backup task name.

● Review all configured settings.

● Click "**Previous**" to go back and make changes if needed.

● After confirming the settings, click "**Confirm**" to create the backup task.

### Manage Backup Tasks

After creating a backup task, you can manage it on the "**Back up & Restore**" page:

![](https://file-us.ugreennas.com/admin/article/2026-08-12/41ba82b60ebb4b6693c01c310d819fb3.webp)

● **Back up**: Click "**Back up**" to manually start the backup task. Click Stop backup to stop it.

● **Edit Task**: Click "**More**" > "**Edit Task**" to modify the backup settings or schedule.

● **Delete Task**: Click "**More**" > "**Delete Task**" to remove the backup task.

### System Tray Display

Click the UGREEN NAS icon in the taskbar on your computer to quickly view the transfer status of individual files in backup tasks. You can also pause tasks that are currently transferring files.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/20a3a586175b4d178b978a52900b86df.webp)
