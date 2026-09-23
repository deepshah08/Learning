# How to Mount Baidu Netdisk Using Cloud Drives?

> **Article ID**: `470`  
> **Category**: `Application Guide > Cloud Drives > How to Mount Baidu Netdisk Using Cloud Drives?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/470  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: UGOS Pro Firmware 1.18.2.0100 or later

The screenshots in this document are for reference only. The actual interface may vary slightly depending on the system or app version, please refer to the actual interface displayed.

## Introduction

UGREEN NAS supports mounting Baidu Netdisk through the "**Cloud Drives**" app. After successful mounting, you can directly access and manage files stored in Baidu Netdisk on your UGREEN NAS, enabling quick file uploads and downloads without repeatedly switching between cloud storage and local storage.

Recommended use cases:

● Back up files from UGREEN NAS to Baidu Netdisk.

● Migrate historical data from Baidu Netdisk to UGREEN NAS.

● Migrate data when replacing a NAS device.

## Prerequisites

● Prepare a Baidu Netdisk account that can be used normally. If you do not have an account, register one first.

● Ensure that your current network environment can access Baidu Netdisk services normally.

● If you need to upload or download a large number of files, check in advance that sufficient storage space is available in Baidu Netdisk.

## Add a Baidu Netdisk Connection

1. Log in to the UGOS Pro system, open the "**Cloud Drives**" app, and click "**New connection**" in the sidebar.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/e3a5a76c9310407abef64464c7bb869c.webp)

2. In the cloud drive type list that appears, select "**Baidu Netdisk**" and click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-08-17/10af5e75c52441e19c1664cb014cc587.webp)

3. After being redirected to the Baidu Netdisk login page, enter your account and password to complete login and authorization. If you do not have a Baidu Netdisk account, register one first.

4. After successful login, you can view the connection status of Baidu Netdisk on the Cloud Drives overview page.

After the connection is established, Baidu Netdisk will appear as a separate directory in the connection list on the Cloud Drives sidebar.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/1bb8d80bdc01438b94f0c6cf241e7d46.webp)

## Manage Files in Baidu Netdisk

After successfully adding a Baidu Netdisk connection, you can use the Cloud Drives app to transfer files between your UGREEN NAS and Baidu Netdisk.

### Upload NAS Files to Baidu Netdisk

1. Open the Cloud Drives app and click the added "**Baidu Netdisk**" connection in the connection list on the left.

**Note**: You can view the current storage usage of Baidu Netdisk in the main panel on the right. If you need to upload a large amount of data, you can upgrade to a Baidu Netdisk NAS membership for additional storage capacity.

2. In the "**Upload to Cloud Drive**" section, click "**Select file**".

![](https://file-us.ugreennas.com/admin/article/2026-08-17/f3061f635e9a4fcaa14dd29a2f3d0b8f.webp)

3. In the "**Upload to Cloud Drive**"window, click "**Select file**", select the files or folders you want to upload from the UGREEN NAS Files, and click "**Confirm**".

![](https://file-us.ugreennas.com/admin/article/2026-08-17/7b865a50691d4b018a7e662f5aed8fac.webp)

4. By default, uploaded files are saved to the "**绿联网盘**" folder in Baidu Netdisk.

**Note**: According to Baidu Netdisk policies, there is a size limit for individual file uploads. Only Baidu Netdisk NAS members can customize the storage path.

5. During the upload process, you can view the current upload progress in "**Upload list**" on the top bar.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/d52d05f6c06545979a03b9880e408ae6.webp)

After all files are uploaded, open the "**绿联网盘**" folder in Baidu Netdisk through a browser to view the uploaded files.

### Download Baidu Netdisk Files to NAS

1. Open the Cloud Drives app and click the added "**Baidu Netdisk**" connection in the connection list on the left.

2. In the main panel on the right, find the"**Download to NAS**" section and click "**Select file**".

![](https://file-us.ugreennas.com/admin/article/2026-08-17/2428c6c891314dceb2cdd083da8af001.webp)

3. In the file selection window that appears, select the Baidu Netdisk files or folders you want to download, and click "**Next**".

4. In the location selection window, specify the storage path for the files on your UGREEN NAS, and click "**Confirm**" to start the download.

5. During the download process, you can view the download progress in "**Download list**"on the top bar.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/1b831c0a31354caba6de20492db46b02.webp)

After the download is complete, go to the corresponding folder path in "**Files**"to view the downloaded files.

### Sync Baidu Netdisk with UGREEN NAS

If you need to keep data in a specified Baidu Netdisk folder and NAS directory synchronized over time, you can create a sync task. The sync task scans and verifies the task folders on both Baidu Netdisk and NAS. When the system detects newly added, modified, or missing files on either side, it synchronizes the files according to the configured sync rules. During subsequent task runs, the system continues to scan the sync folders. If any differences are detected between the two locations, the corresponding files are automatically updated or synchronized.

1. Open the Cloud Drives app and click the added Baidu Netdisk connection in the connection list on the left.

2. In the main panel on the right, find the "**Sync Cloud Drive with NAS**" section and click "**Create sync task**".

![](https://file-us.ugreennas.com/admin/article/2026-08-17/9f54ab86540c4a549046761bed6f7204.webp)

3. In the Create sync task window, configure the sync rules and advanced settings as needed. After completing the settings, click "**Next**".

**Note**: Creating a Baidu Netdisk sync task requires a Baidu Netdisk NAS membership. If you do not have a membership, you can use the upload and download functions instead.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/e634cd1145d5490591676eaa95799e44.webp)

4. Configure the sync strategy and click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-08-17/e6f7eca021c7429e8ff411f0f6f53c55.webp)

5. Set the task name and click OK to complete the "**Confirm**".

![](https://file-us.ugreennas.com/admin/article/2026-08-17/28dc7d36cf284651840494afe8d69677.webp)

#### Advanced Settings Description

When creating a sync task, you can configure advanced settings as needed. The following options are supported:

● **Folder filtering**: Select the remote folders you want to sync. (Files and folders with names beginning with "." are generally hidden files and hidden folders.)

● **File filtering rules**: Exclude files with specified formats or types.

● **File conflict handling strategy**: Set how files are overwritten when file conflicts occur.

If there are no special requirements, you can keep the default settings.

#### Sync Strategy Description

The following sync strategies are supported:

● **Manual synchronization**: After the task is created, it will not run automatically on a regular basis. You need to manually click "**Sync now**" to execute the sync task.

● **Scheduled synchronization**: The task runs automatically according to the configured schedule. After selecting this option, you need to set the sync frequency and first start time.

#### Manage Created Sync Tasks

1. Open the Cloud Drives app and click the added Baidu Netdisk connection in the connection list on the left.

2. Click "**Sync task**" in the top bar of the main panel on the right, and find the sync task you want to manage.

In the sync task list, you can perform the following operations:

● Click "**Sync now**" to manually run the task.

● Click the "**More**" button on the right and select "**Edit task**" to modify sync rules.

● Click the "**More**" button on the right and select "**Delete task**" to remove the sync task.

Deleting a sync task only removes the sync rules and does not delete existing files in Baidu Netdisk or on the NAS.

## Delete an Added Cloud Drive Connection

If you no longer need to use a connection, you can delete it from your UGREEN NAS. This operation only disconnects the cloud drive connection and does not delete files stored in Baidu Netdisk.

1. Open the "**Cloud Drives**" app and find the Baidu Netdisk connection you want to delete in the connection list on the sidebar.

2. Hover over the cloud drive name, click the "**···**" button on the right > "**Delete**".

![](https://file-us.ugreennas.com/admin/article/2026-08-17/a82b6013ee204745bfe396ea21e7a4c4.webp)

3. In the confirmation window that appears, click "**Delete**".

After deletion, the connection will be removed from the Cloud Drives sidebar.

## View Cloud Drive Log Records

The system automatically records cloud drive-related operations, making it easier to troubleshoot transfer errors or review operation history.

1. Open the Cloud Drives app and click the added Baidu Netdisk connection in the connection list on the left.

2. Click "**Log records**" in the top bar of the main panel on the right.

3. After entering the log page, you can switch between "**File transfer records**" and "**Action log records**" to view the corresponding logs.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/da1bffdd6e9c4415920ded774df545e4.webp)

## Notes

● When uploading or downloading large files, ensure a stable network connection. Network interruptions may cause transfer failures or file corruption.

● Ensure that sufficient storage space is available on both the UGREEN NAS and Baidu Netdisk to avoid transfer failures caused by insufficient storage.

● Some advanced Baidu Netdisk features (such as customizing the upload path) are only available to NAS members. Choose a suitable membership plan based on your needs.

● When browsing, copying, moving, deleting, or performing other operations on Baidu Netdisk files in Cloud Drives, the actual permissions depend on the permission settings of your Baidu Netdisk account. If an operation cannot be performed, check the Baidu Netdisk permission settings first.
