# UGOS Pro July 2026 System Update Notes

> **Article ID**: `915`  
> **Category**: `Release notes > UGOS Pro July 2026 System Update Notes`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/915  

---

# Introduction

This update covers UGOS Pro firmware, app suite, and clients. It introduces new features including Dedicated graphics card management, Folder encryption, Mount OneDrive, Baby Album Milestones, Surveillance AI detection, and CarPlay. It also optimizes the user experience for storage, media playback, hard drive hibernation, and more.

Related tutorials in the Knowledge Center have been updated accordingly. You can learn more about feature descriptions and operation methods through the "**Related documents**" in this article.

# Read Before Updating

## Supported Products

This update applies to products running the **UGOS Pro** system. Before upgrading, confirm the corresponding processor architecture based on your product model.

**x86 architecture**:

● DXP Series: DXP2800 Series, DXP4800 Series, DXP6800 Series, DXP8800 Series, DXP480T Series

● DX Series: DX4600 Series, DX4700 Series

● DH Series: DH2600

**ARM architecture**:

● DH Series: DH2300 Series, DH4300 Series

## Upgrade Notes

1. To use the features described in this article, upgrade the system firmware, app suite, or client to the corresponding version or higher.

2. Some new features in the app suite require a specific system firmware version. If the system firmware version is lower than the minimum compatible version, you may not receive update notifications for the app or may not be able to use the related features properly.

3. Supported features may vary depending on the product model, processor architecture, and client platform. Please refer to the actual update content displayed on your device.

# UGOS Pro Firmware

## Version Information

**System firmware version**: V1.18.0.0083

## Control Panel

**Hardware & Power**: Added a Dedicated graphics card management panel, allowing users to view and manage Dedicated graphics cards connected to the device.

**Supported Models**:

● **DXP480T Plus**

● **DXP6800 Series**

● **DXP8800 Series**

● **iDX Series**

**Related documents**:

● [Control Panel Dedicated Graphics Card Feature](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmOTA3IiwiY2xpZW50VHlwZSI6IlBDIn0=)

● [UGREEN NAS Hardware Passthrough Feature](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmOTExIiwiY2xpZW50VHlwZSI6IlBDIn0=)

## Storage

1. Supports mounting RAID disks created by third-party systems as External Storage, with the option to select Read-only or Read/Write mode.

**Related document**:[External Storage](https://support.ugnas.com/knowledgecenter/detail/article/zh-CN/254)

2. Fixed an issue where creating or deleting SSD cache failed when the NFS kernel process occupied the Volume.

3. Fixed an issue where SSD cache could not be added to HDDs when the logical block sizes of HDDs and SSDs were inconsistent.

## Files

1. Added encryption support for top-level shared folders and User Folders.

**Related document**:[Folder Encryption](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmOTEyIiwiY2xpZW50VHlwZSI6IlBDIn0=)

2. Added support for OneDrive in Cloud drive mounting.

**Related document**:[Mount OneDrive Using the Network folder Feature](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmOTA2IiwiY2xpZW50VHlwZSI6IlBDIn0=)

3. Fixed an issue where assigning shared folder permissions to newly added users could affect container mapped path permissions.

4. Fixed an issue where creating or deleting SSD cache failed after mounting an image file with a name containing full-width spaces.

## Other System Updates

1. Universal Search: Supports searching file names using any segment of continuous English characters or numbers. The index needs to be rebuilt after the update for this feature to take effect.

2. Optimized the issue where the "**Model Management**" and "**Sync & Backup**" apps could wake up hard drives while idle. The corresponding app versions must also be updated.

3. Optimized the issue where some videos displayed an unsupported format message when casting via HDMI. This **applies to ARM architecture devices**.

4. Fixed some known issues to improve system stability and user experience.

# App Suite

## Theater

1. Optimized the display of TV show scraping results. When a TV show contains only one season, the "**Season 1**" label is no longer displayed.

2. After the update, run "**Scan and replace all**" for the Library or select "**Rescan**" for the corresponding TV show for the changes to take effect.

3. Optimized issues where some videos displayed a black screen, failed to play, or caused the app to crash when resuming playback on PC, mobile, and TV clients. The corresponding clients must also be updated.

4. Optimized an issue where the download progress was displayed incorrectly when downloading some AV1 videos offline.

5. Fixed some known issues to improve the user experience.

## App Packages

1. Baby Album supports setting the baby's lunar birthday.

2. Added the "**Milestones**" feature to Baby Album.

Related document:[How to Create Baby Album Milestones](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmOTEzIiwiY2xpZW50VHlwZSI6IlBDIn0=)

3. Added support for disabling Live Photos auto playback. The corresponding clients must also be updated.

4. Added a "**Change cover**" option to the right-click menu of photo lists on the Web and PC clients.

5. Added support for sharing external sharing links and "**Invite friends to upload**" as cards on the Web and PC clients.

6. Fixed some known issues to improve the user experience.

## Music

1. Added support for sorting within a single album by disc number and track number.

2. Fixed some known issues to improve the user experience.

## Docker

1. Added support for AMD Dedicated graphics cards. Supported Models:

● **DXP480T Plus**

● **DXP6800 Series**

● **DXP8800 Series**

● **iDX Series**

2. Fixed an issue where assigning shared folder permissions to newly added users could affect container mapped path permissions.

3. Fixed some known issues to improve the user experience.

## Virtual Machine

1. Added external graphics card passthrough support. When creating or editing a virtual machine, you can select a Dedicated graphics card under Hardware passthrough. Supported Models:

● DXP480T Plus

● DXP6800 Series

● DXP8800 Series

● iDX Series

**Related document**:[UGREEN NAS Hardware Passthrough](https://support.ugnas.com/knowledgecenter/detail/article/zh-CN/911)

2. Redesigned the Virtual Machine interface to optimize the page layout and operation workflow.

3. Fixed some known issues to improve the user experience.

## Surveillance Center

1. Cameras connected through the RTSP protocol now support local real-time AI detection.

2. Added support for adding "Known People" by taking a photo or uploading local photos.

**Related document**: [Surveillance Center User Guide](https://support.ugnas.com/knowledgecenter/detail/article/zh-CN/866)

3. Added support for filtering Event View and recording playback by event type, as well as keyword search.

4. Optimized the monitoring playback timeline. Different colors are used to distinguish event detection types, and filtering is supported.

5. Added picture-in-picture playback for live camera views on the mobile client. The mobile client must also be updated.

6. Optimized the playback interaction of camera cards on the mobile client home page. The mobile client must also be updated.

7. Fixed some known issues to improve the user experience.

## Snapshot

1. Added support for taking snapshots of encrypted folders.

2. Fixed some known issues to improve the user experience.

## Cloud Drives

1. Optimized an issue where tasks could fail due to duplicate file names when syncing or uploading files from the NAS using "**115 Cloud Drive**".

2. Fixed some known issues to improve the user experience.

## Sync & Backup

1. Optimized an issue where the app could wake up hard drives while in the idle state.

2. Fixed some known issues to improve the user experience.

## Model Management

1. Optimized an issue where the app could wake up hard drives while in the idle state.

2. Fixed some known issues to improve the user experience.

## Other App Optimizations

The following apps have fixed some known issues to further improve stability and user experience:

● Comics

● Notes

● Vault

● File Version Explorer

● Online Office

● Antivirus Manager

● Downloads

# Client

### iOS Mobile Client

1. Added the CarPlay feature, allowing users to directly access and play UGREEN NAS Music through the car system. Supports iOS 18 and iOS 26.

Related document:[How to Play UGREEN NAS Music Through CarPlay](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmOTE0In0=)

2. Fixed an issue where photos in Baby Album could not be displayed completely when the number of photos was large.

3. Fixed an issue where photo folder names containing spaces prevented users from continuing to edit or adjust settings.

4. Fixed an issue where a white screen appeared when opening GIF images in Photos.

5. Fixed some known issues to improve the user experience.

## Other Clients

The following clients have fixed some known issues to further improve stability and user experience:

● Windows PC Client

● macOS PC Client

● Android Mobile Client

● Android TV

● Apple TV
