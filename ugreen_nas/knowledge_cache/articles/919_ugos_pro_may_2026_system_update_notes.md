# UGOS Pro May 2026 System Update Notes

> **Article ID**: `919`  
> **Category**: `Release notes > UGOS Pro May 2026 System Update Notes`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/919  

---

# Introduction

This update covers the UGOS Pro system firmware, application packages, and client applications. It introduces new features including Btrfs space reclamation, automatic sharing address matching, custom album models, Surveillance Center, WebDAV backup, Amazon S3 service support, and client lock screen. It also includes optimizations for file operations, media playback, photo browsing, and system stability.

Related tutorials in the Knowledge Center have been updated accordingly. You can refer to the "**Related Documents**" section in this article for more information about feature details and operation methods.

# Read Before Updating

## Supported Products

This update applies to products running the **UGOS Pro** system. Before upgrading, confirm the corresponding processor architecture based on your product model.

**x86 Architecture**:

● DXP Series: DXP2800 Series, DXP4800 Series, DXP6800 Series, DXP8800 Series, DXP480T Series

● DX Series: DX4600 Series, DX4700 Series

● DH Series: DH2600

**ARM Architecture**:

● DH Series: DH2300 Series, DH4300 Series

## Upgrade Notes

1. To use the features described in this article, upgrade the system firmware, application packages, or client applications to the corresponding version or higher.

2. Some new features in application packages require a specific system firmware version. If the system firmware version is lower than the minimum supported version, you may not receive update notifications for the application, or related features may not work properly.

3. Available features may vary depending on the product model, processor architecture, and client platform. Please refer to the actual update content displayed on your device.

# UGOS Pro System Firmware

## Version Information

System firmware version: 1.16.0.0085

## Storage

1. Added the Btrfs space reclamation feature.

2. Updated the IHM version to fix abnormal detection results for some Seagate IronWolf hard drives.

## Files

1. When creating a sharing link or file request link, the system can automatically generate the corresponding access address based on the current login method. The following connection methods are supported:

● LAN

● UGREENlink

● DDNS

2. Added file information preview to the web and desktop clients, allowing users to quickly edit file names and tags.

3. When uploading, copying, moving, or downloading files in Files and Vault, the system automatically saves the last selected path for convenient reuse.

4. Moved the "**Settings**" entry to the bottom-left corner of the page.

5. Optimized the configuration process for adding network folders through file protocols.

6. Integrated the "**Messages**" feature, allowing users to choose whether to display pop-up notifications after file operations are completed.

7. Fixed an issue where password verification was still required after increasing the available access count for an external file sharing link whose original access count had been exhausted.

## Log Center

Integrated the "**Messages**" feature, allowing users to choose whether to display pop-up notifications when log policies are triggered.

## Player

Added the memory buffering feature to improve playback smoothness in weak network environments.

This feature applies to original quality playback and transcoded playback in Theater and Files. It is currently not supported on the web client.

## Other System Updates

1. Added container application-related information to the Services list in Task Manager.

2. Fixed an issue where some external hard drive enclosures kept HDDs active after the device was shut down.

3. Fixed an issue where the AX900 wireless adapter was not automatically recognized after system updates.

4. Fixed some known issues to improve system stability and user experience.

# Application Packages

## Photos

1. Added support for custom models in Smart Classification. Users can upload 10 photos to train a model or directly import a previously trained model. Supported products:

● iDX Series

● DXP Series

● DX Series

● DH2600

2. Added Timeline view for browsing photos, with photos grouped by date.

3. Added a slider button on the right side of the folder view in the mobile client for faster photo navigation.

4. The overseas version disables photo location information by default. Users can manually enable this feature as needed.

5. Added current model version information and model upgrade notifications to the Smart Models page.

6. Optimized playback lag issues that may occur when playing Full HD videos on mobile devices.

7. Fixed an issue where photo positioning was inaccurate when returning to the list after swiping through photos on mobile devices.

8. Fixed some known issues to improve user experience.

## Theater

1. Added disk pre-buffering to the Theater player on desktop, mobile, and TV clients. Users can separately set the maximum pre-buffering space for each client and manually clear pre-buffering data. To use this feature, update the corresponding client to the latest version.

2. Added support for playing original quality direct-link content from Quark Cloud Drive on desktop and mobile clients. To use this feature, upgrade the system firmware to the corresponding version.

3. Optimized the "**My Downloads**" entry on mobile clients to keep it in a fixed position.

4. Optimized the issue where deleting downloaded media content on Android mobile clients took a long time.

5. Fixed an issue where subtitles were not displayed when playing some videos on the Windows desktop client.

6. Fixed some known issues to improve user experience.

## Sync & Backup

1. Added WebDAV protocol support for backup servers.

2. Fixed some known issues to improve user experience.

## Security

1. Added the option to scan only selected file types in Settings.

2. Moved the "**Whitelist**" feature from Scan History to "**Settings**" > "**Default scan target**".

3. Fixed some known issues to improve user experience.

## Downloads

1. Added support for downloading sharing links created through the UGREEN NAS Files app. The following access methods are currently supported:

● LAN links using the HTTPS protocol

● UGREENlink links

2. Fixed some known issues to improve user experience.

## Surveillance Center

### Applicability

This version of Surveillance Center is not supported on the following products. These devices will not receive the application update:

● DH2300 4G

● iDX6011

● iDX6011 Pro

### Update Content

1. Officially launched Surveillance Center.

2. Added support for adding cameras through ONVIF and RTSP protocols.

3. Added support for connecting multi-channel surveillance devices.

4. Added support for custom event recording and notification settings.

5. Added support for real-time camera viewing.

6. Added support for centralized viewing and management of recording files.

## Cloud Drives

1. Added Amazon S3 service support. The mobile client must also be updated to the corresponding version.。

2. Fixed some known issues to improve user experience.

## Music

1. Optimized an issue where Single Repeat mode did not work properly.

2. Optimized an issue where Single Repeat mode did not work properly.

## Other Application Updates

The following applications have fixed some known issues to further improve stability and user experience:

● DLNA

● Docker

● Online Office

● XUNLEI

● TextEdit

● Virtual Machine: Available for x86 architecture products

● Vault

● File Version Explorer

● Snapshots

# Client

## Windows Desktop Client

1. Added the client lock screen feature. When background tasks continue running, users can lock the client interface with a separate password to prevent unauthorized access by others.

Path: **Me > Client Settings**.

2. Fixed some known issues to improve user experience.

## macOS Desktop Client

1. Added the client lock screen feature. When background tasks continue running, users can lock the client interface with a separate password to prevent unauthorized access by others.

Path: **Me > Client Settings**.

2. Fixed some known issues to improve user experience.

## Other Clients

The following clients have fixed some known issues to further improve stability and user experience:

● Android mobile client

● iOS mobile client

● Android TV

● Apple TV
