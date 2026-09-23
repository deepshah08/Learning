# Why Are Uploaded Photos and Videos Not in Original Quality?

> **Article ID**: `795`  
> **Category**: `Application Guide > Photos > FAQ > Why Are Uploaded Photos and Videos Not in Original Quality?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/795  

---

## Applicability

**Applicable Version**: UGOS Pro Firmware 1.19.1.0093 or later

The screenshots in this document are for reference only. The actual interface may vary slightly depending on the system or app version, please refer to the actual interface displayed.

## Introduction

When uploading or backing up photos and videos using the mobile app, if the photos or videos stored on the NAS appear blurry or have a lower resolution, refer to the following information for troubleshooting and solutions.

## Cause Analysis

UGREEN NAS does not actively compress or reduce image or video quality during the upload process. By default, all files are transferred in "**original quality**". If you experience issues such as "**blurry images**" or "**non-original quality**", the most common reason is that the files stored locally on your phone are not the original versions.

This is usually related to the cloud storage optimization features of mobile operating systems (iOS/Android). When options such as "**Optimize Storage**" are enabled, the cloud stores the high-resolution originals, while the phone keeps only lower-resolution thumbnails to save local storage space.

In this situation, the NAS uploads the locally stored thumbnails, not the original files stored in the cloud.

## Solution

To ensure that photos and videos are uploaded in full original quality, you need to adjust your phone's system settings so that the original files are downloaded back to the device.

### For iOS Users (iPhone/iPad)

1. Open "**Settings**">"**Apps**", scroll down, and tap "**Photos**".

2. Under "**iCloud Photos**", change "**Optimize iPhone Storage**" to "**Download and Keep Originals**".

![](https://file-us.ugreennas.com/admin/article/2026-08-20/b9aa6ab4239440ca9e16cc4e0df02897.webp)

3. Wait for the system to automatically download the original files from iCloud to your device.

4. Once the originals are fully restored locally, re-run the photo upload task in the UGREEN NAS app.

### Android users (e.g., Xiaomi/Huawei)

1. Open "**Settings**" on your phone, scroll down and tap "**HeyTap Cloud**", then find the photo sync settings.

2. Under "**Local storage optimization**", switch from "**HD thumbnails**" to "**Original photos**".

![](https://file-us.ugreennas.com/admin/article/2026-08-20/d16bb9df3f0740899187849980fd8c5f.webp)

3. After confirming that the original photos have been restored to your device, run the UGREEN NAS photo upload task again.

## Recommendations

If you do not want to change the system storage settings, you can also try manually preloading the original files:

Before starting the NAS upload task, open the photos or videos you want to upload in your phone’s system Photos app and view them one by one. As you browse them, the phone will usually download and cache the original files from the cloud to local storage. You can then upload them to the NAS in their original quality.
