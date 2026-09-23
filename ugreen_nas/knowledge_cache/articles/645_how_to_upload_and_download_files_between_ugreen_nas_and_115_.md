# How to Upload and Download Files Between UGREEN NAS and 115 Drive

> **Article ID**: `645`  
> **Category**: `Application Guide > Cloud Drives > How to Upload and Download Files Between UGREEN NAS and 115 Drive`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/645  

---

## Introduction

With "**Cloud Drives**", you can easily connect to 115 Drive for fast file uploads and downloads. This guide explains in detail how to connect 115 Cloud and transfer data between UGOS Pro and 115 Cloud.

## How to Connect 115 Cloud to UGREEN NAS?

1. Open the "**Cloud Drives**" app, tap "**New connection**".

2. Choose "**115 Drive**" from the pop-up list of supported drives, and click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-09-16/03935084eeee429faec3a89d20f9eacc.webp)

3. You will be redirected to the 115 Drive login page. Use the 115 Life App to scan the QR code and authorize the connection.

![](https://file-us.ugreennas.com/admin/article/2026-09-16/edca4bda5b934889913ea9ac966c56e6.webp)

![](https://file-us.ugreennas.com/admin/article/2026-09-16/c8ff6856f83840f1b40a512597163e4d.webp)

4. Once logged in, return to the "**Overview**" page to view the connection status of 115 Drive.

![](https://file-us.ugreennas.com/admin/article/2026-09-16/0cbe0536e81245819c7b34f3acbd2c6a.webp)

## How to Upload Files from UGREEN NAS to 115 Drive？

1. Tap the connected 115 Drive to view its current storage capacity.

![](https://file-us.ugreennas.com/admin/article/2026-09-16/6bcecfd2b74a43e58e82ab1bcc1a340f.webp)

2. On the "**Connect**" page, under "**Upload to Cloud Drive**", click "**Select file**".

![](https://file-us.ugreennas.com/admin/article/2026-09-16/09847d5d300947b8b084cbdd5a7b5718.webp)

3. After selecting the folder where you want to save the uploaded files, click "**Select file**" to choose the files or folders you want to upload from "**Files**" on UGREEN NAS, then click "**Confirm**" to add them.

![](https://file-us.ugreennas.com/admin/article/2026-09-16/bbfc2d16c8d04e5aa4e3a5a67d966719.webp)

4. During the upload, you can view the progress on the upload page of the connected Drive.

![](https://file-us.ugreennas.com/admin/article/2026-09-16/c534ed165335401f9216395f448397a8.webp)

5. After the upload is complete, open the 115 Drive website and view the uploaded files in the corresponding folder.

## How to Download Files from 115 Drive to UGREEN NAS?

1. On the "**Connect**" page, under "**Download to NAS**", click "**Select file**".

![](https://file-us.ugreennas.com/admin/article/2026-09-16/a48adfdfe3ab410ebebd0608902473df.webp)

2. Select the files or folders from 115 Drive, then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-09-16/ba2b9a44cf0a40e68f68dabf06adabb7.webp)

3. Set the destination path on UGREEN NAS, then click "**Confirm**" to start the download.

![](https://file-us.ugreennas.com/admin/article/2026-09-16/242552cc9adf4f8a9d8a3583b2eebd81.webp)

4. During the download, you can monitor progress in the list of Download.

![](https://file-us.ugreennas.com/admin/article/2026-09-16/19f256778ec3476e9712edb61e9ba262.webp)

5. Once completed, go to "**Files**" on UGREEN NAS to access the downloaded content.

## How to Set Up Data Sync Task Between 115 Drive and UGREEN NAS?

1. On the "**Connect**" page, click "**Create sync task**" under "**Sync Cloud Drive with NAS**".

![](https://file-us.ugreennas.com/admin/article/2026-09-16/0673b4c2964e456683fbfcacfbe5112b.webp)

2. Configure sync rules:

**Cloud Path:** Specify the folder in 115 Drive (e.g., /picture).

**NAS Path:** Specify the folder on UGREEN NAS (e.g., /Personal Folder/Tiffany/tt).

![](https://file-us.ugreennas.com/admin/article/2026-09-16/b22a8f5d19134aee84ada89dddb8b10b.webp)

Select the Sync direction:

![](https://file-us.ugreennas.com/admin/article/2026-09-16/1507af4574e546bd92438deb0e582c14.webp)

**Sync only data changes from the cloud storage to the NAS:** Only changes in 115 Drive are synced to UGREEN NAS. Changes on the NAS are not synced to 115 Drive. By default, deleting a file from 115 Drive does not delete the corresponding file on the NAS.

**Sync only the date changes form the NAS to the cloud drive:** Only changes on the NAS are synced to 115 Drive. Changes in 115 Drive are not synced to the NAS. By default, deleting a file from the NAS does not delete the corresponding file in 115 Drive.

3. Advanced Settings: You can configure additional advanced options as needed, such as filtering out files or file types you do not want to sync. Then click "**Save**".

![](https://file-us.ugreennas.com/admin/article/2026-09-16/8aed9abf0d794063bf7d72f8f14760a1.webp)

4. Sync Strategy: Choose a sync strategy (e.g., **Manual Synchronization**), then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-09-16/7c7aaa2530d740c7abaeccf970d5f1a9.webp)

5. Confirm the task information. After verifying that all settings are correct, click "**Confirm**" to complete task creation.

![](https://file-us.ugreennas.com/admin/article/2026-09-16/18fe7f537b9a43e69752ecb402e891a1.webp)

6. View task progress and status in the "**Sync task**".

![](https://file-us.ugreennas.com/admin/article/2026-09-16/f3d155fa9a0c48aea85df5f3e55b8a82.webp)

## Notes

1. **Network Connection**: During file transfers, make sure the network connection remains stable to avoid transfer interruptions or data loss caused by network fluctuations.

2. **Storage Space**: Make sure there is sufficient available storage space on both UGREEN NAS and 115 Drive before starting, to avoid task failures caused by insufficient space.

3. **Concurrent Task Limit**

● Users with a 115 Drive membership can run up to 3 concurrent tasks at the same time.

● Non-members can run only 1 concurrent task at a time.

4. **Upload and Download Speeds**

● **Upload Speed**: Upload speeds are generally the same for both members and non-members, at approximately **500 KB/s**.

● **Download Speed**: The download speed is approximately **12 MB/s** for members and **100 KB/s** for non-members.

> Actual speeds may vary depending on your network environment, server load, and other factors..

5. **File Size Limits**

The maximum size allowed for a single file on 115 Drive depends on the user's membership tier. For specific rules, please refer to the official information provided in the 115 Membership Center.

6. **Frequency Control and Task Failures**

In some cases, 115 Drive may trigger its frequency control mechanism, causing a task to fail. If this occurs, we recommend trying again later.

> The above information is for reference only. Please refer to the official 115 Drive documentation for the latest details.

7. **Why Are Some Files Missing in My 115 Life?**

After connecting 115 Drive through the NAS Cloud Drives feature, you may find that fewer files are displayed on the NAS than on the 115 Web or app version, or that some folders cannot be found.

This is usually because “**Hidden Mode**” (encrypted folders) is enabled for your 115 account. For details, see "[Why Are Some Files Missing from 115 Drive?](https://support.ugnas.com/knowledgecenter/detail/article/en-US/796) "
