# How to Sync Data Between UGREEN NAS and Aliyun Drive

> **Article ID**: `631`  
> **Category**: `Application Guide > Cloud Drives > How to Sync Data Between UGREEN NAS and Aliyun Drive`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/631  

---

With "Cloud Drives", you can easily connect to Aliyun Drive for fast file uploads and downloads. This is especially useful for data migration, backup, and when replacing your UGREEN NAS device. This guide explains how to connect Aliyun Drive and transfer data between UGOS Pro and Aliyun Drive.

## Connecting Aliyun Drive to UGREEN NAS

1. Open the "Cloud Drives" app, tap "New connection".

2. From the list of supported drives, choose "Aliyun Drive", then click "Next".

![](https://file-us.ugreennas.com/admin/article/2025-08-25/96f8c9f504b64ab281501340fc5a938e.webp)

3. You will be redirected to the Aliyun Drive login and authorization page. Enter your account credentials to log in. If you don’t have an Aliyun Drive account, please register first.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250825/940ff997-a535-4828-9062-59f2313d7c78.png)

4. Once logged in, return to the [Overview] page to view the connection status of Aliyun Drive.

![](https://file-us.ugreennas.com/admin/article/2025-08-25/e0f867c0cea24d9eb7a938bf445eef59.webp)

## Uploading Files from UGREEN NAS to Aliyun Drive

1. Tap the connected Aliyun Drive to view current cloud capacity.

![](https://file-us.ugreennas.com/admin/article/2025-08-25/6d2d32640af04832863d578597593a8f.webp)

2. On the [Connect] page, select [Upload to Cloud Drive] and click "Select file".

![](https://file-us.ugreennas.com/admin/article/2025-08-25/684d441778594051ac53959c61a25613.webp)

3. Choose the save path, then click "Select file" again.

![](https://file-us.ugreennas.com/admin/article/2025-08-25/82eb9d39407a437cb040ce6e344cd1e8.webp)

4. In the "Select file" window, select the files or folders from "Files" on your UGREEN NAS and click "Confirm".

![](https://file-us.ugreennas.com/admin/article/2025-08-25/b2905d99d2f942e292aae8351d398be0.webp)

5. During the upload process, you can monitor progress in the [Upload].

![](https://file-us.ugreennas.com/admin/article/2025-08-25/8bb6efe695c942fc82f90e4c2f474319.webp)

6. Once completed, log in to Aliyun Drive to verify the uploaded files in the designated folder.

## Downloading Files from Aliyun Drive to UGREEN NAS

1. On the [Connect] page, click "Select file" under [Download to NAS].

![](https://file-us.ugreennas.com/admin/article/2025-08-25/a49ee37b3f4e412eaa742d9301b18da5.webp)

2. Choose the files or folders from Aliyun Drive and click "Next".

![](https://file-us.ugreennas.com/admin/article/2025-08-25/ed8487a53f524a3fbaa518d47f07cbe8.webp)

3. Set the destination path on UGREEN NAS, then click "Confirm" to start the download.

![](https://file-us.ugreennas.com/admin/article/2025-08-25/7ad98f412b0e430a9fec33ad105cf1be.webp)

4. Monitor progress in the [Download].

![](https://file-us.ugreennas.com/admin/article/2025-08-25/e84a15da04e04900bf16e02c7e0e0077.webp)

5. When the download finishes, navigate to "Files" on UGREEN NAS to access the files.

## Setting Up Data Sync Between Aliyun Drive and UGREEN NAS

1. On the [Connect] page, click "Create sync task" under [Sync Cloud Drive with NAS].

![](https://file-us.ugreennas.com/admin/article/2025-08-25/220799a91d9d49f59070db6106e39bdc.webp)

2. Configure sync rules:

**Cloud Path:** Specify the folder in Aliyun Drive (e.g., ./Backup).

**NAS Path:** Specify the folder on UGREEN NAS (e.g., /Personal Folder/Tiffany/tt).

![](https://file-us.ugreennas.com/admin/article/2025-08-25/aafd7e8629ec4a5c9edc33488693f9fc.webp)

Select the sync direction:

![](https://file-us.ugreennas.com/admin/article/2025-08-25/524122ee63474446853579b505eb11e6.webp)

**Two-Way Sync:** Any changes (additions, modifications, deletions) on either side are synced to the other.

**Sync only data changes from the cloud storage to the NAS:** Only changes in Aliyun Drive are synced to UGREEN NAS. By default, deleted files in Aliyun Drive are not removed from the NAS.

**Sync only the data changes from the NAS to the cloud drive:** Only changes in UGREEN NAS are synced to Aliyun Drive. By default, deleted files on the NAS are not removed from Aliyun Drive.

3. Advanced Settings: Optionally configure file type filters or exclusions, then click "Save".

![](https://file-us.ugreennas.com/admin/article/2025-08-25/8fc7b9cc62244f268ce87425b996e3a9.webp)

4. Sync Strategy: Choose a sync strategy (e.g., Manual Synchronization) and click "Next".

![](https://file-us.ugreennas.com/admin/article/2025-08-25/f5d68dc904164abfbd1b702907f85ebe.webp)

5. Review the task details and click "Confirm" to create the sync task.

![](https://file-us.ugreennas.com/admin/article/2025-08-25/7098b6cbbe5944dd99b5d2139904e1ff.webp)

6. Check progress and status under [Sync task].

![](https://file-us.ugreennas.com/admin/article/2025-08-25/77104fba5f2c4484886b7575fad7e50a.webp)

**Notes**

● **Network Connection:** Ensure a stable network to prevent transfer interruptions or data loss.

● **Storage Space:** Verify sufficient space on both UGREEN NAS and Aliyun Drive to avoid failed transfers.
