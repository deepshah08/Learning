# How to Mount OneDrive Using Cloud Drives?

> **Article ID**: `479`  
> **Category**: `Application Guide > Cloud Drives > How to Mount OneDrive Using Cloud Drives?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/479  

---

## Applicability

**Applicable Clients**: UGREEN NAS PC Client (Windows/macOS)

**Applicable Version**: NAS firmware 1.19.1.0126 or later

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

UGREEN NAS supports mounting OneDrive through the Cloud Drives app. Once mounted, you can access and manage files in OneDrive directly from UGREEN NAS without repeatedly downloading or transferring files between the cloud and local storage.

**Note**: Access to and use of this feature depend on your network environment. Before you begin, make sure your current network can access OneDrive services normally.

## Prerequisites

Before mounting OneDrive, make sure you have a working OneDrive account. OneDrive pages may vary by region and language. If you cannot register or sign in to your OneDrive account, contact OneDrive Support for assistance.

## Add OneDrive Connection

1. On the UGREEN NAS desktop, open the Cloud Drives app and click "**New Connection**" in the sidebar.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/75873556bea444dd87d62b2ee73e1e87.webp)

2. In the cloud drive type list that appears, select "**OneDrive**", then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-09-07/e214f19ce43248ee98dcc83879843647.webp)

3. In the sign-in window, enter your OneDrive account information to sign in and authorize access.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/087d2a814ba049c28ac0406982b057ef.webp)

Once connected, OneDrive appears as a separate directory in the connection list in the Cloud Drives sidebar.

## Delete Added Cloud Drive Connection

If you no longer need the connection, you can remove it from UGREEN NAS. This only disconnects the cloud drive and does not delete any files stored in OneDrive.

**Steps**:

1. Open the **Cloud Drives** app and find the OneDrive connection you want to delete in the sidebar connection list.

2. Hover over the cloud drive name, then click "**···**" > "**Delete**" on the right.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/84f8d02b85064036bbc4e9aff3d9d273.webp)

3. In the confirmation dialog, click "**Delete**".

After deletion, the connection is removed from the Cloud Drives sidebar.

## Manage Files in OneDrive

After adding a OneDrive connection, you can use Cloud Drives to transfer files between UGREEN NAS and OneDrive.

The following features are supported:

● Upload NAS files to OneDrive.

● Download OneDrive files to the local NAS.

● Create sync tasks to keep data in the cloud drive and UGREEN NAS directories in sync.

● View upload, download, and operation logs.

File transfer speeds depend on your network environment, file size, and OneDrive service status.

### Upload NAS Files to OneDrive

1. Open the Cloud Drives app and click the added OneDrive connection in the connection list on the left.

2. In the main pane on the right, find the "**Upload to Cloud Drive**" section and click "**Select Files**".

3. Select the NAS files you want to upload, then click "**Confirm**".

4. Set the cloud drive save path, which is the destination folder in OneDrive, then click "**Upload**".

Once the upload starts, click "**Upload**" in the top bar to view the upload progress in real time.

### Download OneDrive Files to the Local NAS

1. Open the Cloud Drives app and click the added OneDrive connection in the connection list on the left.

2. In the main pane on the right, find the "**Download to UGREEN NAS**" section and click "**Select Files**".

3. Select the files you want to download, then click "**Next**".

4. Choose a save location on the local NAS, then click "**Confirm**" to start the download.

Once the download starts, click "**Download**" in the top bar to view the download progress in real time.

## Sync OneDrive with UGREEN NAS

If you want to keep data in specific OneDrive and NAS directories in sync over time, create a sync task.

A sync task scans and checks the task directories in OneDrive and on the NAS. When new, modified, or missing files are detected on either side, the system syncs them according to the configured sync rules.

On subsequent runs, the system continues scanning the sync directories. If differences are detected between the two sides, the corresponding files are automatically added or updated.

1. Open the Cloud Drives app and click the added OneDrive connection in the connection list on the left.

2. In the main pane on the right, find the "**Sync Cloud Drive with NAS**" section and click "**Create sync task**".

3. In the Create Sync Task window, set the sync rules and configure advanced settings as needed. When finished, click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-09-07/9bc8e5896da142128355d5f0c6e8f774.webp)

4. Set the sync strategy, then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-09-07/bb2e811996d94def95bc6345bb1e69c5.webp)

5. Enter a task name, then click "**Confirm**" to create the task.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/ac88683e28594fad82664d16859fe000.webp)

## Advanced Settings

When creating a sync task, you can configure the following advanced settings as needed:

● Use the sync folder feature to select the remote folders you want to sync and define the sync scope.

● Use file filtering to include or exclude specific file types from the sync task.

● Use file conflict settings to define how files with the same name are handled during sync.

### Set Sync Folder

Use this feature to sync only specific folders and avoid syncing files you do not need.

1. Expand the remote folder directory and select the folders you want to sync.

2. Click "**Save**".

![](https://file-us.ugreennas.com/admin/article/2026-09-07/db206270264843a9bdaa0e477404e6d7.webp)

Example:

● Sync the `UGREEN NAS/0902`folder.

● Do not sync the`UGREEN NAS/0902/0901`subfolder.

● Sync the `UGREEN NAS/0903`folder.

**Sync Files and Folders Prefixed with "."**

By default, the system hides files and folders whose names begin with a `.` . After you enable "**Sync Files and Folders Prefixed with "."**", the sync task will include the following types of hidden files and folders:

Examples:

```
.config
.git
.env
```

Once enabled, these files are included in the sync task.

**Note**:

● Some files beginning with a `.` may contain system settings, app settings, or sensitive information.

● Unless you specifically need this feature, we recommend leaving it disabled.

### File Filter

Use "**File filter**" to filter files by size and file type for the sync task.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/d3af126c7e094979bbcc5f0dfac6f635.webp)

### File Conflict

Use "**File conflict**" to define how files with the same name are handled during sync.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/7eac8bebbf204454823003289b6264f1.webp)

### Sync Strategy

Sync tasks support the following sync methods:

● **Manual Synchronization**: The task does not run automatically after it is created. Click "**Sync now**" to start the task manually.

● **Real-time Synchronization**: After the task is created, the system continuously monitors the sync directory for file changes and automatically syncs them as changes occur.

● **Scheduled Synchronization**: The task runs automatically according to the configured schedule. When you select this option, set the sync frequency and the first start time.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/4215d919b07d4b8a9a0c0b5d83dd0419.webp)

## View Cloud Drive Logs

The system automatically records cloud drive operations to help troubleshoot transfer errors and audit activity.

1. Open the Cloud Drives app and click the added OneDrive connection in the connection list on the left.

2. In the top bar of the main pane on the right, click "**Logs records**".

3. On the Logs page, switch between "**File transfer records**" and "**Action Logs records**" to view different records.

The Logs page supports the following features:

● Search for specific records using the search box.

● Export logs as a local file.

● Clear unnecessary log records.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/04b38ecfcd7a4d348433755017e0619b.webp)
