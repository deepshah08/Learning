# UGOS Pro June 2026 System Update Notes

> **Article ID**: `917`  
> **Category**: `Release notes > UGOS Pro June 2026 System Update Notes`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/917  

---

# Introduction

This update covers UGOS Pro system firmware, app packages, and clients. It introduces new features including scheduled **sleep for specified Storage pools**, **Hard disk** **wake-up strategies**, **custom fan speed curves**, **Volume migration for app storage**, **app access permission settings**, **local AI monitoring**, **Dedicated graphics card** support for Docker, and **Backblaze B2** integration. It also includes optimizations for video playback, photo management, music playback, and system stability.

Related tutorials in Knowledge Center have been updated accordingly. For more information about feature descriptions and operation methods, refer to the "**Related Documents**" section in this article.

# Read Before Updating

## Applicable Products

This update applies to products running the **UGOS Pro** system. Before upgrading, check the processor architecture corresponding to your product model.

**x86 Architecture**:

● DXP Series: DXP2800 Series, DXP4800 Series, DXP6800 Series, DXP8800 Series, DXP480T Series

● DX Series: DX4600 Series, DX4700 Series

● DH Series: DH2600

**ARM Architecture**:

● DH2300 Series, DH4300 Series

## Upgrade Notes

1. To use the features described in this article, upgrade the system firmware, app packages, or clients to the corresponding version or higher.

2. Some new features in app packages require specific system firmware versions. If the system firmware version is lower than the minimum supported version, you may not receive app update notifications or may be unable to use related features properly.

3. Supported features may vary depending on the product model, processor architecture, and client platform. Please refer to the actual update content displayed on your device.

# UGOS Pro System Firmware

## Version Information

System firmware version: 1.17.0.0095

This update includes interface changes. To ensure proper functionality, it is recommended to update the firmware, clients, and related apps to the latest versions.

## Control Panel

### Hardware & Power

1. Power: Added "**Specified Storage pool Sleep**" and "**Wake-up Strategy**" settings for hard disk hibernation.

2. General: Added a "Custom" mode for the cooling fan, allowing users to manually configure fan speed curves.

### About

1. App Storage Space Migration: Theater, Photos, and Music now support storage space migration. After selecting a new app installation location, the migration can be completed. Support for other apps will be added gradually in future versions.

2. App Access Permissions: Theater, Photos, and Music now support configuring user roles that can access the apps. Support for other apps will be added gradually in future versions.

3. App Reset: Third-party apps and container apps now support the "**App Reset**" feature. After resetting, app data will be cleared and the app will be restored to its initial state. This can be used to resolve operation issues caused by abnormal data, incorrect configurations, or cache errors. Support for other apps will be added gradually in future versions.

### Files

1. The "**Details**" panel now supports width adjustment by dragging. It also displays the number of files and subfolders within a folder.

2. When standard users delete subfolders in shared folders, the "**Delete permanently**" option is no longer available.

3. Optimized issues that may occur when file names are too long.

### Storage

The minimum supported hard disk capacity for SSD cache has been adjusted to 16 GB.

### App Center

1. When uninstalling the snapshot app, users can now choose to delete the corresponding snapshot files at the same time.

2. Fixed an issue where added descriptions were not displayed for storage spaces when selecting an app installation location.

### Other System Updates

1. "UGREEN AI" has been renamed to "Model Management" and now supports uninstallation.

2. After uninstalling "Model Management", some AI features in apps such as Photos and Surveillance Center will become unavailable. Please proceed with caution.

3. The Image Viewer now supports bottom thumbnail preview. This feature is available for the following apps and features:

● Universal Search

● Snapshot

● Files

● Vault

● File Version Explorer

4. Optimized the startup speed of some videos in MP4 format.

5. Fixed some known issues to improve system stability and user experience.

# App Packages

## Theater

1. Added media metadata protection for video resources. Users can retain manually edited movie and TV series information, including posters and descriptions, preventing manually edited content from being overwritten during media library scans. The mobile client must also be updated to the corresponding version.

2. Added support for **Dolby TrueHD** and **DTS-HD Master Audio** audio passthrough in the video player on PC and Android TV clients. Audio can be decoded and played through an external AV receiver or soundbar. The corresponding clients must also be updated.

3. Fixed an issue where "**Rescan**" or "**Scan manually**" could not be performed when the resource path contained the “%” character.

4. Fixed some known issues to improve the user experience.

## Photos

The Photos app on mobile must be updated to version 1.17.0 or higher to use the following features.

### Baby Album

1. Added the ability to locate the timeline based on the baby’s age.

2. In the baby age timeline view, users can like and comment on photos by date.

3. When sharing a Baby Album, users can set the relationship between the shared user and the baby.

4. Added support for creating Baby Albums from folders and setting up one-way sync.

### Other Updates

1. Added Slideshow playback.

2. The "Uploaded by others" filter in Baby Albums and regular albums now supports filtering by specified users.

3. Optimized the browsing experience on the "**Categorization > People**" page:

● Supports remembering the scroll position of the list.

● After switching AI Categorization tabs, changing filter conditions, or performing search or refresh operations, the list automatically returns to the top.

4. Fixed an issue where the shooting date of videos exported from Photoshop was reset after playback if the date had been modified in Photos.

5. Fixed an issue where animated WebP images could not be played when viewing original images.

6. Fixed an issue where the page automatically returned to the top after clicking the zoom button.

7. Fixed some known issues to improve the user experience.

## Music

1. Optimized the issue where the duration of DTS audio files was read incorrectly.

2. Fixed some known issues to improve the user experience.

## Docker

The following graphics card-related features are supported on:

● DXP480T Plus

● DXP6800 Series

● DXP8800 Series

● iDX Series

Updates:

1. Added Dedicated graphics card support. After connecting a Dedicated graphics card through a UGREEN GPU dock or PCIe slot, users can select the corresponding graphics card in container settings. The mobile client must also be updated to the corresponding version.

2. Added support for resetting third-party apps and container apps through "**Control Panel**" **>** "**About**" **>** "**Apps**".

After resetting, app data will be cleared and the app will be restored to its initial state. This can be used to resolve operation issues caused by abnormal data, incorrect configurations, or cache errors. The system firmware must be updated to the corresponding version. Support for other apps will be added gradually in future versions.

3. Fixed some known issues to improve the user experience.

## Cloud Drives

1. Added support for Backblaze B2. The mobile client must also be updated to the corresponding version.

2. Fixed some known issues to improve the user experience.

## Downloads

1. Optimized the issue where Downloads could not automatically recognize UGREEN NAS share links containing Chinese characters after being copied on the PC client.

2. Fixed some known issues to improve the user experience.

## Snapshot

1. When uninstalling the Snapshot app, users can now choose to delete the corresponding snapshot files at the same time.

2. Fixed some known issues to improve the user experience.

## Text Editor

1. Fixed an issue where changes were still applied after canceling the save operation when switching interface styles in Settings.

2. Fixed some known issues to improve the user experience.

## Vault and File Version Management

1. The Image Viewer now supports bottom thumbnail preview.

2. Fixed some known issues to improve the user experience.

## NVIDIA Driver 570.181

Applicable to some x86 architecture products.

Added support for using NVIDIA Dedicated graphics cards with Docker apps.

## NVIDIA Docker Toolkit

Applicable to some x86 architecture products.

The "**NVIDIA Docker Toolkit**" app is now officially available, providing the runtime environment required for Docker containers to use NVIDIA Dedicated graphics cards.

## Uliya

Applicable to iDX Series devices.

1. Added support for app uninstallation.

2. Fixed some known issues to improve the user experience.

## Model Management

1. "**UGREEN AI**" has been renamed to "**Model Management**" and now supports uninstallation. After uninstalling, some AI features in apps such as Photos and Surveillance Center will become unavailable. Please proceed with caution.

2. Fixed some known issues to improve the user experience.

## Surveillance Center

### Applicability

This Surveillance Center update does not apply to the DX4600 Series, DX4700 Series, or DH2600. These devices will not receive this app update and do not support the new features described below.

The Local AI detection feature requires the face recognition and general detection models in the "**Model Management**" app.

### Update Details

1. Added support for connecting cameras through ONVIF and RTSP protocols, with compatibility for multi-channel devices.

2. Added support for custom event recording and notification settings, along with live view preview and recording file management.

3. Added Local AIdetection, supporting the recognition of the following event types:

● People

● Faces

● Pets

● Vehicles

When enabled, recorded videos and real-time video streams through the ONVIF protocol will be analyzed using UGREEN NAS local AI models. When relevant events are detected, the system can generate event records and send notifications.

4. Fixed some known issues to improve the user experience.

## Other App Updates

The following apps have fixed some known issues to further improve stability and user experience:

● SAN Manager: Applicable to some x86 and ARM architecture products

● Voice Memos: Applicable to **iDX Series** devices

● DLNA

● Online Documents

● Security Manager

● Thunder

● Sync & Backup

● Virtual Machine: Applicable to x86 architecture products

● Comics

# Clients

## Windows Client

1. Fixed an issue where related processes did not release CPU resources in time after closing the video player.

2. Fixed some known issues to improve the user experience.

## Other Clients

The following clients have fixed some known issues to further improve stability and user experience:

● macOS Client

● Android Mobile Client

● iOS Mobile Client

● Android TV

● Apple TV
