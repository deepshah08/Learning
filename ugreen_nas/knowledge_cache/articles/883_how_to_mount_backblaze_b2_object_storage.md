# How to Mount Backblaze B2 Object Storage?

> **Article ID**: `883`  
> **Category**: `Application Guide > Cloud Drives > How to Mount Backblaze B2 Object Storage?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/883  

---

## Applicability

**Applicable client:** UGREEN NAS PC client (Windows/macOS).

**Applicable version:** NAS firmware 1.17.0.0031 or later.

This document is for reference only. The actual interface and operation paths may vary slightly depending on system or app version updates. Please refer to the actual interface.

## Overview

UGREEN NAS supports mounting **Backblaze B2 object storage** through "**Cloud Drives**". Once mounted, files stored in Backblaze B2 can be accessed and managed directly from the NAS, without repeatedly downloading or transferring them between the cloud and local storage.

**Note**: Access to this feature depends on the network environment. Before getting started, make sure the current network can connect to Backblaze B2 services normally.

## Before You Begin

Before mounting Backblaze B2, sign in to the Backblaze account and have the following information ready:

● **Bucket Name:** The name of the storage bucket.

● **Key ID:** The application key ID.

● **application Key:** The application key.

The Backblaze interface may vary by region and language, so the path for obtaining the **Key ID** and **applicationKey** may differ. If these details cannot be found, contact Backblaze Support for instructions.

## Add a Backblaze B2 Connection

Once connected, Backblaze B2 appears as a separate directory in the connection list on the left side.

1. On the UGREEN NAS desktop, open "**Cloud Drives**", then click "**New connection**" in the sidebar.

![](https://file-us.ugreennas.com/admin/article/2026-06-29/ff1be63075fd4772ac94d05b8e42536c.webp)

2. In the cloud storage list, select "**Backblaze B2**", then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-06-29/18b3aaff07e846c19a0a2024bfdd4cd7.webp)

3. In the configuration window, enter the "**Key ID**" and **"Application key**", then select the bucket to mount.

4. After confirming that the information is correct, click "**Connect**".

![](https://file-us.ugreennas.com/admin/article/2026-06-29/0714cad7c9b5466bbc2342ae483e8b30.webp)

Once connected, Backblaze B2 appears as a separate directory in the connection list on the left side of "**Cloud Drives**".

## Create a Bucket

If no bucket is available in the Backblaze account, create one directly from the connection window.

1. Open the "**Bucket**" drop-down menu, then select "**New bucket**".

![](https://file-us.ugreennas.com/admin/article/2026-06-29/b9fd1d0c6113456d896bc2426d984e49.webp)

2. Configure the bucket as prompted, then click "**Confirm**" to create it.

![](https://file-us.ugreennas.com/admin/article/2026-06-29/3e5dd47306a64f638c823dbc9dfa3bb8.webp)

3. Once the bucket has been created, return to the connection window and select it.

**Note**:

● Configure the bucket according to the requirements shown by Backblaze.

● For help with any of the settings, refer to the Backblaze documentation or contact Backblaze Support.

## Remove an Existing Cloud Drive Connection

If the connection is no longer needed, it can be removed from the UGREEN NAS. Removing the connection only disconnects the cloud drive and does not delete any files stored in Backblaze B2.

**Steps**:

1. Open "**Cloud Drives**", then find the Backblaze B2 connection to remove in the connection list on the left.

2. Hover over the connection name, click "**…**" on the right, then select "**Delete**".

![](https://file-us.ugreennas.com/admin/article/2026-06-29/0397dd80bf2c4b8a9f4afe6e84f7f064.webp)

3. In the confirmation window, click **"Delete"**.

After deletion, the connection will be removed from the sidebar in "**Cloud Drives**".

## Manage Files in Backblaze B2

Once the Backblaze B2 connection has been added, files can be transferred between the UGREEN NAS and Backblaze B2 through "**Cloud Drives**".

The following actions are supported:

● Upload files from the NAS to Backblaze B2.

● Download files from Backblaze B2 to the local NAS.

● Create sync tasks to keep cloud and NAS directories in sync.

● View upload, download, and operation logs.

File transfer speeds may vary depending on the network environment, file size, and the availability of Backblaze B2 services.

### Upload NAS Files to Backblaze B2

1. Open "**Cloud Drives**", then select the connected Backblaze B2 drive from the connection list on the left.

2. In the main panel, find "**Upload to Cloud Drive**" and click "**Select file**".

3. Set the save path on Backblaze B2, then click "**Select file**"**.**

![](https://file-us.ugreennas.com/admin/article/2026-06-29/8e1eebc4253348eba286978e8eca8df2.webp)

4. In the file picker, select the NAS files to upload.

5. Click "**Confirm**" to start the upload.

After the upload starts, click "**Upload**" in the top bar to view the upload progress in real time.

### Download Backblaze B2 Files to the NAS

1. Open "**Cloud Drives**", then select the connected Backblaze B2 drive from the connection list on the left.

2. In the main panel, find "**Download to NAS**" and click "**Select file**".

3. In the download window, select the files to download from Backblaze B2, then click "**Next**".

4. In the location selection window, choose a destination folder on the NAS, then click "**Confirm**" to start the download.

After the download starts, click "**Download**" in the top bar to view the download progress in real time.

### Sync Backblaze B2 with UGREEN NAS

To keep a specified Backblaze B2 directory and NAS directory in sync over time, create a sync task.

1. Open "**Cloud Drives**", then select the connected Backblaze B2 drive from the connection list on the left.

2. In the main panel, find "**Sync Cloud Drive with NAS**" and click "**Create sync task**".

3. In the "**Create sync task**" window, configure the sync rules and any required advanced settings, then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-06-29/78efec6006b5485faafd38929a492528.webp)

4. Select a sync strategy, then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-06-29/de0bcac6d3d7440da5f44661ec53f456.webp)

5. Enter a task name, review the settings, then click "**Confirm**" to create the task.

![](https://file-us.ugreennas.com/admin/article/2026-06-29/e1b8138f26a5467c95412e3eacc5f729.webp)

## Advanced Settings

When creating a sync task, configure the advanced settings as needed. The following options are available:

● **File filtering rules:** Exclude files in specified formats or categories.

● **File conflict handling:** Choose how files are handled when a conflict occurs.

Keep the default settings if no additional configuration is required.

## Sync Strategies

The following sync strategies are available:

● **Manual synchronization:** The task does not run automatically on a schedule. To run it, click "**Sync now**"manually.

● **Scheduled synchronization:** The task runs automatically according to the configured schedule. Select this option, then set the sync frequency and the first start time.

## Manage Existing Sync Tasks

1. Open "**Cloud Drives**", then select the connected Backblaze B2 drive from the connection list on the left.

2. Click "**Sync task**" in the top bar, then locate the task to manage.

The following actions are available in the sync task list:

● Click "**Sync now**" to run the task manually.

● Click "**More**" on the right, then select "**Edit**" to modify the sync settings.

● Click "**More**" on the right, then select "**Delete**" to remove the sync task.

Deleting a sync task only removes its sync rules. Files already stored in Backblaze B2 or on the NAS will not be deleted.

![](https://file-us.ugreennas.com/admin/article/2026-06-29/064d705542c54b4aaf7d3a9207cce201.webp)

## View Cloud Drive Logs

The system automatically records cloud drive activity, making it easier to troubleshoot transfer errors and review past operations.

1. Open "**Cloud Drives**", then select the connected Backblaze B2 drive from the connection list on the left.

2. Click "**Log records**" in the top bar.

3. On the log page, switch between "**File transfer records**" and "**Action log records**" as needed.

![](https://file-us.ugreennas.com/admin/article/2026-06-29/65b75d7ffddd40b286f34aef79256c68.webp)

The log page also supports the following actions:

● Search for specific records.

● Export log records as a local file.

● Delete logs that are no longer needed.

## FAQs

#### What should I do if the connection fails with a permission error?

Go to Backblaze B2 and check that the **Key ID** and **applicationKey** are correct. Also make sure the key has permission to access the selected bucket.

If the error persists after the configuration has been verified, contact Backblaze Support to check the account, bucket, and key permissions.

#### Why is access to files in Backblaze B2 slow?

Backblaze B2 performance depends on the current network environment. Upload, download, and file browsing speeds may be affected by network quality, the region where the bucket is hosted, and file size.

For better performance, choose a bucket region that is geographically closer to the NAS.

#### How do I update the Key ID or application Key on the NAS?

The current version does not support editing credentials for an existing connection. To use a different **Key ID** or **application Key**, delete the current Backblaze B2 connection, then add it again using the new credentials.

Deleting the connection only disconnects the NAS from Backblaze B2. Files stored in Backblaze B2 will not be deleted.

#### What determines my permissions for file operations after mounting Backblaze B2?

Permissions for browsing, copying, moving, deleting, renaming, and downloading Backblaze B2 files in "**Cloud Drives**" are determined by the permissions configured in Backblaze B2.

If a file cannot be deleted, written to, or moved, first check the bucket permissions and key permissions in Backblaze B2.

## Notes

● Keep the network connection stable when uploading or downloading large files. A network interruption may cause a transfer to fail or a sync task to encounter an error.

● Before creating a sync task, check the sync direction and file conflict handling settings to avoid files being overwritten or synced more than once because of incorrect rules.

● If a sync task fails, check "**Log records**" first. Use the error details to troubleshoot the network connection, file paths, permissions, or account status.
