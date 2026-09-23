# How to Mount an Amazon S3 Bucket?

> **Article ID**: `861`  
> **Category**: `Application Guide > Cloud Drives > How to Mount an Amazon S3 Bucket?`  
> **Client Compatibility**: `MOBILE`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/861  

---

## Applicability

**Applicable client:** UGREEN NAS mobile app (iOS / Android)

**Applicable version:** NAS firmware 1.16.0.0042 and later

This document is for reference only. The actual interface and operation paths may vary slightly due to system or app version updates. Please refer to the actual interface.

## Overview

UGREEN NAS lets you mount an Amazon S3 bucket using the "Cloud Drives" app. Once mounted, files in the S3 bucket can be accessed and managed just like local NAS files, without the need to download them from the cloud or transfer them back and forth.

## Preparation

Before you start mounting the bucket, log in to the AWS (Amazon S3) Management Console and prepare the following information:

● **Bucket Name**: The name of the bucket.

● **AWS Region**: The AWS Region where the bucket is located.

![](https://file-us.ugreennas.com/admin/article/2026-05-28/9f355f4ce5f141f79f4a0416097c38b3.webp)

● **Access Key**: The access key of the IAM user.

● **Secret Access Key**: The secret access key of the IAM user. This key can only be viewed and copied when it is created, so keep it safe.

![](https://file-us.ugreennas.com/admin/article/2026-05-28/fec1a005f1d946f0be5c773999018229.webp)

## Add an S3 Connection in Cloud Drives

1. Open "**Cloud Drives**" on your UGREEN NAS and click "**Create**".

![](https://file-us.ugreennas.com/admin/article/2026-05-28/e5630411323c487eba5a209cf803d990.webp)

2. In the cloud drive type list that appears, select "**Amazon S3**" and click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-05-28/09e37550b253401c89cf68a547d12ddc.webp)

3. In the configuration window, fill in the following parameters:

● **Server**: "**Amazon S3**" is selected by default. If your bucket is deployed in a Chinese mainland Region, select "**Amazon S3 China**" from the drop-down menu.

● **Access Key**: Enter the access key you obtained.

● **Secret Key**: Enter the corresponding secret access key.

● **Bucket**: Select the target bucket you have created from the drop-down list, or click "**New bucket**".

![](https://file-us.ugreennas.com/admin/article/2026-05-28/dfe913643fc14b0e95094001eba53b5d.webp)

4. Click "**Connect**".

5. Once connected, the Amazon S3 bucket will appear as a separate directory in the cloud drive connection list.

![](https://file-us.ugreennas.com/admin/article/2026-05-28/2b5bfb8985ad47d6b6c598b4161406da.webp)

## Unmount or Delete a Cloud Drive Connection

If you no longer need to connect to the S3 bucket, you can delete it from the system at any time. This only disconnects the bucket and does not delete any files stored in Amazon S3.

1. In the connection list of the Cloud Drives app, click the Amazon S3 cloud drive you want to disconnect.

2. Tap "**Me**" in the bottom bar.

3. Tap "**Delete connection**".

4. When prompted, tap "**Delete**".

![](https://file-us.ugreennas.com/admin/article/2026-05-28/48d78ad22d2341e4a85eac3afb917463.webp)

## Manage Files in Amazon S3

After Amazon S3 is mounted successfully, you can use "**Cloud Drives**" to transfer data between your NAS and Amazon S3. In addition to basic manual uploads and downloads, the system also supports automatic sync and log tracking.

### Upload NAS Files to Amazon S3

1. In the connection list of **"Cloud Drives"**, click the mounted Amazon S3 cloud drive.

2. Go to the cloud drive file list and tap the "**+**" button.

3. In the upload window, select the files you want to upload from your NAS to the cloud drive.

4. Select an S3 "**Storage class**" at the bottom.

**Note:** Tap the "ⓘ" icon next to a storage class to view its overview.

5. After selecting the files and storage class, tap "**Please select folder**" at the bottom.

6. In the window that appears, choose where to store the files in S3, then tap "**Select folder**".

7. Tap "**Upload**" at the bottom of the page. The files will be transferred in the background.

![](https://file-us.ugreennas.com/admin/article/2026-05-28/ec4468ccb3dc4d82926f3216488a3f06.webp)

You can track the upload progress in the **task list** in the top bar.

![](https://file-us.ugreennas.com/admin/article/2026-05-28/a3e6757d6e1a46a093f6e2981bb2be4c.webp)

### Download Files from Amazon S3 to NAS

1. In the connection list of "**Cloud Drives**", click the mounted Amazon S3 cloud drive.

2. In the file list, select the files or folders you want to download to your NAS.

3. Click "**Please select folder**" at the bottom of the page.

4. In the window that appears, choose where to save the files or folders on your NAS, then click "**Select folder**".

5. Click "**Download**" at the bottom of the page.

You can track the download progress in the **task list** in the top bar.

![](https://file-us.ugreennas.com/admin/article/2026-05-28/8d9879dceb7746c8b211a318e775499e.webp)

### Sync Cloud Drive with NAS

To keep a NAS folder and the S3 cloud data in sync over time, you can create a sync task:

1. In the connection list of "**Cloud Drives**", click the mounted Amazon S3 cloud drive.

2. Click "**Sync**" in the bottom bar, then click "**Create**".

3. In the window that appears, set up the sync rule, then click "**Next**".

4. Enter a "Task name".

5. Select the "Cloud Drive path" and "NAS path".

6. Select the "Sync direction".

7. Select the "Sync strategy". If you choose scheduled sync, set the sync frequency and first start time.

8. Select a "Storage class". Click the "ⓘ" icon next to an option to view its overview.

To run the task immediately, select **"Sync immediately after creation"**.

![](https://file-us.ugreennas.com/admin/article/2026-05-28/a8842592674e41f8aaf35fff8e938a7e.webp)

### Manage Existing Sync Tasks

1. In the connection list of "**Cloud Drives**", click the mounted Amazon S3 cloud drive.

2. Click "**Sync**" in the bottom bar and find the target task on the Sync page.

3. Click the task to open its edit page. To run it manually, click "**Sync now**".

4. To remove the task, click "**Delete**".

![](https://file-us.ugreennas.com/admin/article/2026-05-28/d928dfecd30c4a74bd0cde4c7c110e35.webp)

## FAQs

1. **How to resolve a "Permission error" when mounting fails?**

Go to the AWS console and check whether the entered "Access Key" is correct. If the settings are correct but the error persists, contact Amazon Support for help checking the account permissions.

2. **Why is access to files in the S3 bucket slow?**

Read and write speeds in "Cloud Drives" are highly dependent on the current network environment. For the best experience, choose an S3 bucket Region that is geographically closest to the NAS location.

3. **How to update AWS credentials on NAS after they are changed in AWS?**

The current version does not support updating credentials for an active connection. To use new credentials, delete the existing connection by following the steps in "Unmount or Delete a Cloud Drive Connection", then click "+ New connection" and add it again with the new "Access Key" and "Secret Key".

4. **What determines file operation permissions after mounting?**

Permissions for browsing, copying, moving, deleting, renaming, and downloading files in S3 through "Cloud Drives" depend on the S3 bucket policy in AWS and the permissions assigned to the IAM account. If deleting or writing files fails, check the permission settings in the AWS console first.
