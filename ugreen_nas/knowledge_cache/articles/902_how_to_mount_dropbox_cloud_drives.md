# How to Mount Dropbox Cloud Drives?

> **Article ID**: `902`  
> **Category**: `Application Guide > Cloud Drives > How to Mount Dropbox Cloud Drives?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/902  

---

## Applicability

**Applicable client**: UGREEN NAS PC Client (Windows/macOS).

**Applicable version**: NAS firmware 1.17.0.0031 and later.

The descriptions in this document are for reference only. The actual interface and operation paths may vary due to system or App updates, please refer to the actual interface.

## Introduction

UGREEN NAS supports mounting Dropbox through the Cloud Drives App. After mounting, you can access and manage files in Dropbox directly from UGREEN NAS without repeatedly downloading or transferring files between the cloud and local storage.

**Note**: Access to and use of this feature may be affected by the network environment. Before use, make sure your current network connection can access Dropbox services properly.

## Preparation

Before mounting, prepare a valid Dropbox account. Dropbox pages may vary depending on the region and language settings. If you are unable to register or log in to your Dropbox account, contact Dropbox Support for assistance.

## Adding a Dropbox Connection

1. On the UGREEN NAS system desktop, open the Cloud Drives App and click "**New connection**" in the sidebar.

![](https://file-us.ugreennas.com/admin/article/2026-08-20/5a61f2259e7744d39fb65d215e8cbd85.webp)

2. In the pop-up Cloud Drive list, select "**Dropbox**" and click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-08-20/e56d237621cc4632ad97bfe3ae7536a3.webp)

3. In the login window, enter your Dropbox account information, then follow the on-screen instructions to complete login and authorization.

![](https://file-us.ugreennas.com/admin/article/2026-08-20/d521f652be0d4a7d8acc77acbb5f8417.webp)

After the connection is successful, Dropbox will appear as a separate directory in the connection list on the Cloud Drives sidebar.

## Deleting an Added Cloud Drive Connection

If you no longer need a connection, you can remove it from UGREEN NAS. This operation only disconnects the cloud drive connection and does not delete any files stored in Dropbox.

**Steps**:

1. Open the **Cloud Drives** App and find the Dropbox connection you want to delete in the connection list on the sidebar.

2. Hover over the Cloud Drive name, click "**···**" on the right > "**Delete**".

![](https://file-us.ugreennas.com/admin/article/2026-08-20/a640cbf433f941cfa26d9f59e0ff90f4.webp)

3. In the confirmation window that appears, click "**Delete**".

After deletion, the connection will be removed from the Cloud Drives sidebar.

## Managing Files in Dropbox

After successfully adding a Dropbox connection, you can transfer files between UGREEN NAS and Dropbox through the Cloud Drives.

The system supports the following features:

● Upload files from NAS to Dropbox.

● Download files from Dropbox to the local NAS.

● Create sync task to keep data between the cloud drive and UGREEN NAS directories consistent.

● View upload, download, and operation logs.

File transfer speeds may vary depending on the network environment, file size, and Dropbox service status.

### Uploading Files from NAS to Dropbox

1. Open the Cloud Drives App and click the added Dropbox cloud drive in the connection list on the left.

2. In the main panel on the right, find the "**Upload to Cloud Drive**" section and click "**Select file**".

3. Configure the cloud drive storage path, which is the directory where files will be stored in Dropbox, then click "**Select file**".

4. In the pop-up file selector, select the NAS files you want to upload.

5. Click "**Confirm**" to start uploading.

After the upload starts, you can click "**Upload**" in the top bar to view the real-time upload progress.

### Downloading Files from Dropbox to Local NAS

1. Open the Cloud Drives App and click the added Dropbox cloud drive in the connection list on the left.

2. In the main panel on the right, find the "**Download to NAS**" section and click "**Select file**".

3. In the download window, select the Dropbox files you want to download, then click "**Next**".

4. In the location selection window, specify the folder where the files will be saved on the local NAS, then click "**Confirm**" to start downloading.

After the download starts, you can click "**Download**" in the top bar to view the real-time download progress.

### Syncing Dropbox with UGREEN NAS

If you need to keep data between Dropbox and a specified NAS directory synchronized over time, you can create a sync task.

1. Open the Cloud Drives App and click the added Dropbox cloud drive in the connection list on the left.

2. In the main panel on the right, find the "**Sync Cloud Drive with NAS**" section and click "**Create sync task**".

3. In the Create sync task window, configure the sync Rules and advanced settings as needed. After completing the settings, click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-08-20/6d833b0e10f94c2482c3c780cad2768a.webp)

4. Configure the Sync Strategy, then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-08-20/7e8338ad6ece4a0a9fdc6a0752a4bb4d.webp)

5. Set the Task name, then click "**Confirm**" to complete the creation.

![](https://file-us.ugreennas.com/admin/article/2026-08-20/ed81163d05fd43da85521f6d049e7763.webp)

## Advanced Settings

When creating a sync task, you can configure advanced settings as needed. The following options are available:

● File Filter Rules: Exclude files with specific formats or file types.

● File Conflict Handling Strategy: Set how to handle file conflicts when they occur.

If no special requirements apply, you can keep the default settings.

## Sync Strategy

The following sync strategies are available:

● Manual Sync: The task will not run automatically after creation. You need to click "**Sync now**" manually to start the sync task.

● Scheduled Sync: The task will run automatically according to the configured schedule. After selecting this option, you need to set the sync frequency and first start time.

## Managing Created Sync Task

1. Open the Cloud Drives App and click the added Dropbox cloud drive in the connection list on the left.

2. In the top bar of the main panel on the right, click "**Sync task**" and find the sync task you want to manage.

In the sync task list, you can perform the following operations:

● Click "**Sync now**" to manually run the task.

● Click "**More**" on the right and select "**Edit**" to modify the sync rules.

● Click "**More**" on the right and select "**Delete**" to delete the sync task.

Deleting a sync task only removes the sync rules. It will not delete existing files in Dropbox or on NAS.

![](https://file-us.ugreennas.com/admin/article/2026-08-20/e6c6dd9edfaa44ebac347cba2da6aeb3.webp)

## Viewing Cloud Drive Log Records

The system automatically records cloud drive-related operations, making it easier to troubleshoot transfer errors or perform operation audits.

1. Open the Cloud Drives App and click the Colud Drive Connection on the left.

2. In the top bar of the main panel on the right, click "**Log records**".

3. On the log page, switch between "**File transfer records**" and "**Action log records**" to view records.

![](https://file-us.ugreennas.com/admin/article/2026-08-20/a058f09c3b294f80adabd3a3779c4eee.webp)

The Log records page supports the following features:

● Search for records using the search box.

● Export Log records as local files.

● Clear redundant Log records.

## FAQs

### Q1: Why is accessing files in Dropbox slow?

The access speed of Dropbox is affected by the current network environment. Upload, download, and file browsing speeds may be affected by factors such as network quality and file size.

### Q2: What affects file operation permissions after mounting?

When browsing, copying, moving, deleting, renaming, or downloading Dropbox files in the Cloud Drives App, the actual permissions depend on the permission settings of Dropbox.

If you are unable to delete, write, or move files, check the Dropbox permissions first.

## Notes

● When uploading or downloading large files, keep the network connection stable. Network interruptions may cause transfer failures or sync task errors.

● Before creating a sync task, confirm the sync direction and file conflict handling strategy to avoid file overwriting or duplicate syncing caused by incorrect rule settings.

● If a sync task fails, check the **Log records** first. Troubleshoot network, path, permission, or account issues based on the error information.
