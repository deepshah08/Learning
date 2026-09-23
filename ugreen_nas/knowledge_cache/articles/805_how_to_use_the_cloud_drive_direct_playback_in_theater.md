# How to Use the Cloud Drive Direct Playback in Theater?

> **Article ID**: `805`  
> **Category**: `Application Guide > Theater > How to Use the Cloud Drive Direct Playback in Theater?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/805  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS)

**Applicable Version**: NAS Firmware 1.19.1.0063 or later

The descriptions in this document are for reference only. The interface may vary depending on system or app updates, please refer to the actual interface.

## Introduction

After connecting a cloud drive using the "**Network folder**" feature in the "**Files**" app, the cloud drive appears as a folder in Files. You can then create a media library in "**Theater**" and link it to the cloud drive folder.

Once linked, the system scans the folder for video files and identifies film information based on file names. When a match is found, the following information is automatically retrieved:

● Film poster

● Film synopsis

● Cast and crew information

After matching is complete, Theater supports **Cloud drive direct playback**, allowing you to stream videos directly from the cloud drive.

## Playback Mode

With cloud drive direct playback, the system reads data directly from the cloud drive server as a file stream, without using local NAS storage space.

If the current device or network environment does not support direct playback, the system switches to another playback method as needed, such as **Transcode via NAS**.

## Supported Cloud Storage Services

Cloud drive direct playback currently supports the following cloud storage services:

● 115 Drive

● Quark Drive

● Aliyun Drive

● OneDrive

Support for more popular cloud storage services will be added gradually. Please refer to the actual page for the latest supported services.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/971d4bf5e38f4f0eb6854bafc0c2dadc.webp)

## Supported Clients

Cloud drive direct playback is supported on the following clients:

● UGREEN NAS PC client

● UGREEN NAS mobile app (iOS / Android)

● UGREEN NAS TV client

**Note**: Cloud drive direct playback is not supported in the UGREEN NAS Web client. When playing cloud drive videos in a web browser, the system uses "**Transcode via NAS**" instead.

## Differences Between Cloud Drive Direct Playback and Transcode via NAS

When playing cloud drive videos in Theater, two playback methods are supported: "**Cloud drive direct playback**" and "**Transcode via NAS**".

### Cloud Drive Direct Playback

**How it works**: Cloud drive direct playback is the recommended method. The playback device connects directly to the cloud drive server and streams the video.

**Advantages**:

● Faster playback.

● Does not use NAS upload bandwidth.

● Does not use local NAS storage space.

### Transcode via NAS

**How it works**: The NAS first retrieves the video data from the cloud drive, then streams the video to the playback device over the NAS network.

**Limitations**:

● Playback performance depends on the upload bandwidth of the NAS network.

● If the NAS upload bandwidth is insufficient, playback may stutter.

● When playing over the internet, the bandwidth load is concentrated on the NAS network.

If "**Cloud drive direct playback**" is not enabled, the system uses "**Transcode via NAS**" by default.

## Before You Begin

Before setup, connect your cloud drive using the "**Network folder**" feature in the "**Files**" app. Once the connection is established, open Theater and create a media library.

## Create a Cloud Drive Media Library

1. Open "**Theater**" and click "**Settings**" at the top.

2. Click "**Library**" > "**New library**".

![](https://file-us.ugreennas.com/admin/article/2026-08-27/b45689305b124771966b6ca8e448bbde.webp)

3. Set the library name. Under the media folder section, add the connected cloud drive folder.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/2c0db22608bc42459c8a6f1779b0d513.webp)

4. When finished, click "**Apply**".

After the library is created, Theater scans the video files in the cloud drive folder and identifies film information based on the file names.

**Note**: For a media library that uses cloud drive folders, it is recommended to add folders from only one cloud drive.

Avoid adding local NAS folders or folders from other cloud drives to the same media library, as this may cause cloud drive path recognition issues.

## Enable Cloud Drive Direct Playback

After creating a cloud drive media library, you can enable cloud drive direct playback.

1. Open "**Theater**" and click "**Settings**" at the top.

2. Click "**Cloud drive playback mode**", then enable "**Cloud drive direct playback**".

![](https://file-us.ugreennas.com/admin/article/2026-08-27/b887ad67317949ee8920f335ceca377d.webp)

Once enabled, supported clients will prioritize cloud drive direct playback.

## Set Users Authorized for Direct Playback

To reduce the risk of issues with your cloud drive account, it is recommended to limit which users can use direct playback.

1. Open "**Theater**" and click "**Settings**" at the top.

2. Click "**Cloud drive playback mode**" > "**Users authorized for direct playback**", then select the users who are allowed to use this feature.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/1745c11d66c54ff5bfaf0a28d483106f.webp)

**Note**: Avoid frequent simultaneous access to the same cloud drive account from multiple IP addresses or by multiple users. This may trigger the cloud storage service provider's risk control mechanisms and result in restricted account access.

## How to Select a Playback Method

After creating the cloud drive media library and configuring cloud drive direct playback, wait for the media library scan and film information matching to complete.

1. Open "**Theater**" and enter the cloud drive media library you created.

2. Click the video you want to play.

When playing a cloud drive video, a cloud drive icon appears in the bottom bar of the player. Click the icon to select a playback method.

If "**Cloud drive direct playback**" is enabled, you can select direct playback. If it is not enabled, the system uses "**Transcode via NAS**" by default.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/8d58c2ffbf314b2cbcf23d17ae504575.webp)

## Related Reading

● [Mount 115 Drive via Network Folder](https://support.ugnas.com/knowledgecenter/detail/article/en-US/802)

● [Mount OneDrive Using the Network folder Feature](https://support.ugnas.com/knowledgecenter/detail/article/en-US/906)

● [FAQs for Cloud Drive Direct Playback](https://support.ugnas.com/knowledgecenter/detail/article/en-US/811)
