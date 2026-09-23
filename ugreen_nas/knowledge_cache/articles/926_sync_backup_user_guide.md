# Sync & Backup User Guide

> **Article ID**: `926`  
> **Category**: `Application Guide > Sync & Backup > Sync & Backup User Guide`  
> **Client Compatibility**: `MOBILE`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/926  

---

## Applicability

**Applicable Client**: UGREEN NAS App (iOS / Android)

**Applicable Version**: UGOS Pro 1.18.1.0098 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

"**Sync & Backup**" is a data protection tool in the UGREEN NAS app. It helps you automatically back up photos, videos, folders, and WeChat files from your phone to your NAS, freeing up phone storage space and preventing data loss.

Currently, three backup types are supported:

● **Photos backup**: Back up photos and videos from your phone (iOS / Android)

● **Folder backup**: Back up selected folders on your phone (Android only)

● **WeChat file backup**: Back up downloaded files from WeChat (Android only)

## Enable Photos Backup

The Photos backup feature automatically backs up photos and videos from your phone to your NAS, helping free up phone storage space. When using this feature for the first time, follow the on-screen instructions to grant access to photos on your phone.

1. Open "**Sync & Backup**", then tap "**Photos backup**" > "**Enable now**".

![](https://file-us.ugreennas.com/admin/article/2026-08-12/b17304d15e6047e38a8174916460199f.webp)

2. On the Photos backup settings page, enable the "**Photos backup**" switch and complete the following settings:

![](https://file-us.ugreennas.com/admin/article/2026-08-12/be7a2cc388ef4a2cae07307e1665a2d1.webp)

● **Backup rules**: Select Back up all albums or Continue last backup.

● **Backup source**: Select the albums on your phone to back up. You can select all albums or choose specific albums.

● **Back up to**: Select the destination path on your NAS. You can choose an existing folder in your personal library or shared folder, or manually create a new folder.

Under "**Other settings**", complete the following configurations:

● **Backup time range**: Select "Back up all" or customize a time range to back up files from a specific period only.

● **Photos sorting**: Select how backed-up files are organized:

Organize files into different folders by capture month

Store all backed-up photos in the same folder

Keep the folder structure on the phone

3. After completing the settings, the system will automatically start backing up. You can view the backup progress on the app home page or the Photos backup settings page.

**Note**：

● The system automatically creates a folder named after your phone model in the backup destination path and stores files according to the selected organization method.

● Changing the organization method only applies to newly backed-up files and does not change the storage structure of existing backups.

● To reorganize existing backup files, delete them first and then back them up again.

## Enable Folder Backup

The Folder backup feature automatically backs up selected folders from your phone to your NAS. When using this feature for the first time, follow the on-screen instructions to grant access to files on your phone.

1. Open "**Sync & Backup**", then tap "**Folder backup**" > "**Enable now**".

![](https://file-us.ugreennas.com/admin/article/2026-08-12/2cda8b89ac8e4e52a2597295389bceb3.webp)

2. On the Folder backup settings page, enable the "**Folder backup**" switch and complete the following settings:

![](https://file-us.ugreennas.com/admin/article/2026-08-12/fdc272d927414a51b49ea3b7b3ecb7f9.webp)

● **Backup rules**: Select Back up all or Continue last backup.

● **Backup source**: Select the folders on your phone to back up.

● **Back up to**: Select the destination path on your NAS. You can choose an existing folder in your personal library or shared folder, or manually create a new folder.

● **Photos sorting**: Select whether to keep the folder structure on the phone or store all files in the same folder.

3. After completing the settings, the system will automatically start backing up. You can view the backup progress on the app home page or the Folder backup settings page.

**Note**: By default, backups are performed only over Wi-Fi. If you need to use mobile data for backup, tap "**Continue backup**" and select "**Use data for this time only**" or "**Enable traffic backup**".

## WeChat File Backup

The WeChat File Backup feature automatically backs up files saved or downloaded from WeChat to your NAS.

1. Open "**Sync & Backup**", then tap "**WeChat file backup**" > "**Enable now**".

![](https://file-us.ugreennas.com/admin/article/2026-08-12/c86f4b6a3a184b3bb869ec66dc87320c.webp)

2. On the WeChat file backup settings page, enable the "**WeChat file backup**" switch and complete the following settings:

![](https://file-us.ugreennas.com/admin/article/2026-08-12/353b80ac8ec74cf4825b0243996a83ff.webp)

● **Backup rules**: Select Back up all or Continue last backup.

● **Backup source**: By default, all files downloaded from WeChat are backed up. Tap "**>**" to deselect specific file types (WeChat documents, images, videos, or other files).

● **Back up to**: Select the destination path on your NAS. You can choose an existing folder in your personal folder or shared folder, or manually create a new folder.

3. After completing the settings, the system will automatically start backing up. You can view the backup progress on the app home page or the WeChat file backup settings page.

**Note**:

● WeChat files are backed up to the "**Personal Folder / MobileBackup / [phone model]**" path by default.

● On the WeChat file backup settings page, tap "**Backed up files**" to view the list of backed-up files.

● By default, automatic backup is performed only over Wi-Fi. Backup will be paused when using a non-Wi-Fi network.

## Enable Night Backup

After enabling Night backup, the system automatically performs backup tasks during the specified time period, reducing interruptions to daily use.

**Steps**:

1. Open "**Sync & Backup**", tap the "**Settings**" icon at the top, and enter the General settings page.

2. Enable the "**Night backup**" switch.

3. Customize the backup time range. After setup is complete, when the phone battery level is above 20%, the system will automatically perform backup tasks during the specified time period.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/51bb18f3c06d4cbc94ebcc3e67d24236.webp)

## Enable Auto Backup in Background

Some phone manufacturers restrict apps from running in the background, which may interrupt backup tasks. You can enable background auto backup permissions as needed:

● **Android users**: In the Photos backup settings, tap "**Auto backup in background**" and follow the on-screen instructions to go to the phone system settings and enable the required permissions. The settings path may vary depending on the phone brand. Refer to the instructions provided by the corresponding manufacturer.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/ab2ece96401d41008e544442d0c20257.webp)

● **iOS users**: In the Photos backup settings, enable the "**Auto backup in background**" switch to allow background backup on iOS.

## View Backup Progress

You can view the status of backup tasks in the following way:

**Method 2: View on the Home Page**

1. Open the UGREEN NAS app and enter the "**Sync & Backup**" app.

2. In the home page list, you can view currently running backup tasks. If an issue occurs (such as network interruption or insufficient storage space), an error message will be displayed here.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/dbe866c5f7ed41459112e2e08b682175.webp)

3. Tap a backup task to enter the details page, where you can view **the backup progress bar** and **the number of remaining files**.

**Method 2: View in Task Center**

1. Open the UGREEN NAS app and tap the "**Task Center**" icon in the upper-right corner.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/f27d39624fd34b7d95da716b34c8186a.webp)

2. On the Task Center page, you can view the complete status of all backup tasks.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/2410c9bc1d734dfcb68b49f9e07ee6cb.webp)

## FAQs

### Q1: Why are my backed-up photos and videos not in the original quality?

UGREEN NAS does not compress or reduce the quality of files during the backup process. All photos and videos are backed up in their original quality. If the image quality appears blurry or the files are not original versions, it is usually because the files stored locally on the phone are not the original files. This is often related to cloud services or storage optimization features provided by phone manufacturers. For details, refer to "[Why Are Uploaded Photos and Videos Not in Original Quality?](https://support.ugnas.com/knowledgecenter/detail/article/en-US/795?clientType=COMMON) "

### Q2: If I select "Organize by capture month", how does the system handle files without EXIF information?

For files without EXIF information, the system categorizes them based on the time information provided by the phone's file system:

● **iOS devices**: Use the file **creation time**.

● **Android devices**: Use the file **modified time**.

### Q3: Can I set different organization rules for different backup tasks?

Yes. Each backup task (Photos backup, Folder backup, and WeChat file backup) can have its own independent destination organization settings. The settings do not affect each other.

## Notes

● If no task or progress is displayed on the "**Sync & Backup**" page, check whether auto backup is enabled or whether the backup task has already been completed.

● If a task is stuck or the progress remains unchanged for a long time, try pausing and restarting the backup.

● The system supports running multiple backup tasks simultaneously, which can be managed centrally in Task Center.

● When "**Auto backup in background**" or "**Night backup**" is enabled on iOS devices, the UGREEN NAS app will continue running backup tasks in the background, which may increase battery consumption. It is recommended to use these features when the device has sufficient battery power or is connected to a charger to prevent interruptions caused by low battery levels.
