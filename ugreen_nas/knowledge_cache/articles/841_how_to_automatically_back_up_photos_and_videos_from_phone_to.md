# How to Automatically Back Up Photos and Videos from Phone to NAS Photos

> **Article ID**: `841`  
> **Category**: `Application Guide > Photos > How to Automatically Back Up Photos and Videos from Phone to NAS Photos`  
> **Client Compatibility**: `MOBILE`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/841  

---

## Applicability

**Applicable Client**: UGREEN NAS Mobile App (iOS / Android)

**Applicable Version**: UGOS Pro Firmware 1.18.1.0098 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

With the Photos Backup feature in the UGREEN NAS app, you can automatically back up photos and videos from your phone to Photos on your NAS. This helps prevent data loss while freeing up storage space on your phone.

## Prerequisites

Before you begin, make sure the following requirements are met:

● "**Sync & Backup**" and "**Photos**" are installed from App Center on your NAS.

● Your phone is connected to a Wi-Fi network. For the initial backup, Wi-Fi is recommended to avoid using mobile data.

● Make sure your NAS has sufficient available storage space.

## Enable Photos backup

1. Open the "**Photos**" app, tap "**Settings**" in the bottom navigation bar, find "**Photos backup**", and tap "**Enable**".

![](https://file-us.ugreennas.com/admin/article/2026-08-12/30a28367cb314418bc02289290d33633.webp)

Alternatively, open "**Sync & Backup**", tap "**Photos backup**" > "**Enable**".

2. On the Photos backup settings page, configure the following:

![](https://file-us.ugreennas.com/admin/article/2026-08-12/5fbc8de07ee643c2bf009df247e3f628.webp)

● **Backup rule**: Choose to back up all files or Continue last backup.

● **Backup source**: Select the albums on your phone that you want to back up. You can select all albums or only specific albums.

● **Back up to**: Select a destination folder linked to Photos on your NAS. You can choose an existing folder under a personal or shared folder, or create a new folder.

● **Backup time range**: Choose All, or set a custom time range to back up only files from the specified period.

● **Photos sorting**: Choose how backed-up files are organized:

Sort by recording date (month/year): Organizes backed-up photos and videos into separate folders by the month and year they were taken.

Flatten all content: Stores all backed-up photos and videos in a single folder.

Keep original directory structure (Android only): Stores backed-up photos and videos on the NAS using the original directory structure on your phone.

3. Once the setup is complete, the backup starts automatically.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/b88685b011ff4eee9929cc60fd959c75.webp)

**Notes**：

● When Keep original directory structure is selected, the system automatically creates a folder named after your phone model under the backup destination.

● If you change the sorting method for a backup task, the new setting applies only to newly backed-up files. The folder structure of files already backed up will not be changed.

● To reorganize files that have already been backed up, delete them first and then back them up again.

## View backup progress

You can check the status of a backup task in the following three ways:

**Method 1: Check from the Sync & Backup home page**

1. Open the UGREEN NAS app and go to "**Sync & Backup**".

2. On the Mobile Phone Backup home page, you can view the currently running backup task and its progress.

3. Tap the backup task to open the details page, where you can view the **backup progress bar** and the **number of remaining items**.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/521321409b5547818185df66e4c451ed.webp)

**Method 2: Check from Task center**

1. Open the UGREEN NAS app and tap the "**Task center**" icon in the upper-right corner.

2. On the Task center page, you can view the full status of all backup tasks.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/c4b416b865ac474db22b43772e7b3b72.webp)

**Method 3: Check from Photos**

1. Open the UGREEN NAS app and go to "**Photos**".

2. On the Library page, you can view the backup task status and the number of remaining items.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/fd5ba837d04040fb8ec752e8660b04d0.webp)

## Set up a scheduled backup task (optional)

If you want backups to run automatically during a specified time period with less impact on daily use, you can enable Night backup in "**Sync & Backup**".

1. Tap the "**Settings**" icon at the top of the Photos backup page to open the General settings page.

2. Turn on "**Night backup**" and set the backup time range.

3. The system will automatically run backups during the specified time period.

You can also enable **Auto backup in background**, **Mobile data backup**, and **Energy-saving backup** as needed.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/b92f539a915147669b69107802e0887d.webp)

## FAQs

**Q1: Why aren't my backed-up photos and videos in their original quality?**

UGREEN NAS does not compress photos or videos or reduce their quality during backup. All photos and videos are backed up in their original quality. If backed-up files appear blurry or are not the originals, this is usually because the files stored locally on your phone are not the original files. This is commonly related to cloud services or storage optimization features provided by the phone manufacturer. For details, see "[Why Are Uploaded Photos and Videos Not in Original Quality?](https://support.ugnas.com/knowledgecenter/detail/article/en-US/795?clientType=COMMON) "

**Q2: If I select “Sort by recording date (month/year),” how are photos without EXIF data organized?**

For photos without EXIF data, the system organizes them based on the timestamps provided by the phone’s file system:

● **iOS devices**: The file **creation time** is used.

● **Android devices**: The file **modification time** is used.

## Notes

● When setting up a backup, we recommend keeping "**Mobile data backup**" disabled to avoid using mobile data.

● For subsequent backups, only newly added files are backed up. The existing folder structure remains unchanged.

● To change the folder structure of files that have already been backed up, delete the existing backup files and run the backup again.

● Files that have already been backed up can be safely deleted from your phone without affecting the copies stored on the NAS, helping free up storage space on your phone.

● When Auto backup in background is enabled, the UGREEN NAS app continues running backup tasks in the background, which may increase battery usage. We recommend using this feature when your phone has sufficient battery power or is connected to a charger.
