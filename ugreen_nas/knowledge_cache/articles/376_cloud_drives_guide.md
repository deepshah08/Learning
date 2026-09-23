# Cloud Drives Guide

> **Article ID**: `376`  
> **Category**: `Application Guide > Cloud Drives > Cloud Drives Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/376  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS)

**Applicable Version**: NAS Firmware 1.18.2.0100 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

"**Cloud Drives**" is a cross-platform file management app provided by UGREEN NAS. It supports uploading, downloading, and syncing files between NAS storage and various third-party cloud drives. With this app, you can easily manage file transfers between your NAS and popular cloud storage services for file sharing, syncing, and backup across multiple platforms.

## Installation and Access

1. Open "**App Center**", find "**Cloud Drives**" in the app list

2. Click "**Install**" to start the installation wizard, and follow the on-screen instructions to complete the setup.

3. Once installed, you can access the app by clicking the "**Cloud Drive**" icon on the UGREEN NAS desktop or in "**My apps**".

## Supported Third-Party Cloud Drives

The Cloud Drives app supports connections to multiple third-party cloud drive services, including **Baidu Netdisk**, **Aliyun Drive**, **Quark Drive**, **115 Life**, **189 Cloud**, **Microsoft OneDrive**, **Google Drive**, **Dropbox**, **Amazon S3**, and **Backblaze B2**.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/4fb1afa26c9c49d89732c9e495800fc7.webp)

## Overview Page

On the "**Overview**" page, you can view the status of drives, your personal device connection information, and other users' device connection information (visible to administrators only).

**Note**: Information about other users' devices includes connection name, user, status, and the option to delete connection.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/6ee068371bf044da9c8d57910167be69.webp)

## Adding Cloud Drive

Cloud Drives supports multiple cloud services, including Baidu Netdisk, Aliyun Drive, Quark Drive, 115 Drive, Microsoft OneDrive, Google Drive and more.

**Steps:**

1. Click "**New connection**" or"**Create**", select the desired cloud drive in the pop-up window, and click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-08-17/4dcd51818c3141c5a21bda53bdbae9bb.webp)

2. The system will open the login page for the selected drive. Complete login as instructed.

3. After a successful login, the cloud drive will be automatically added to the "**Cloud Drives**", allowing users to view and manage it directly.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/47fd5207979f41c584ecf484fc55162b.webp)

● **View cloud drive status**: Open the "**Cloud Drives**", and under "**Cloud Drive Connection**" in the left panel, select your personal cloud drive to view its connection status and storage usage.

● **Manage connected cloud drives**: Click the "**…**" button on the right side of the cloud drive, select "**Management**", and customize the "**Polling period**" for the connected cloud drive.

● **Remove a connected cloud drive**: Click the "**…**" button on the right side of the cloud drive and select "**Delete**" to remove the connection.

**Note**:

● Each cloud drive account can only be connected to one user on the NAS.

● If multiple users attempt to add the same account, subsequent connections will fail.

● The "**Polling Period**" determines how often the NAS checks the cloud drive for file changes. When polling is enabled and a period is set, the NAS sends a request to the cloud drive server at the specified interval. If file changes are detected, the NAS starts synchronization (download or update). If no changes are detected, the NAS remains idle until the next polling cycle.

## Uploading NAS Files to a Cloud Drive

1. In Cloud Drives, select the target drive and go to the "**Connect**" page.

2. Click "**Upload to Cloud Drive**">"**Select file**" to open the upload settings window.

3. Choose the save path in the cloud drive and click "**Select file**".

![](https://file-us.ugreennas.com/admin/article/2026-08-17/a565b50fb4c24856b7321832842fd67f.webp)

4. Select the files or folders on UGREEN NAS, then click "**Confirm**" to start uploading. Users can monitor task progress under the "**Upload**" tab and view historical upload tasks in "**Log records**".

![](https://file-us.ugreennas.com/admin/article/2026-08-17/f097c781509d47e389e99c533ad3f704.webp)

**Note:** If uploading files to the cloud drive fails, the possible reasons include:

● **Network issues**: Please check whether your network connection is functioning properly.

● **Permission issues**: Please ensure that you have sufficient permissions for the selected files and folders to perform the upload operation.

## Downloading Cloud Drive Files to NAS

1. On the "**Connect**" page of the target drive, click "**Download to NAS**"**>**"**Select file**".

2. Select the desired files or folders from the cloud drive and click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-08-17/6f424735f739472bb9a7e6ca7204f7b8.webp)

3. Set the save path on your UGREEN NAS and click "**Confirm**" to start the download.

4. You can view task progress on the "**Download**" page and view historical tasks on the "**Log records**" page.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/41f8865b57164c4d9299babc0a58e857.webp)

## Create a Sync Task Between a Cloud Drive and the NAS

● **Supported cloud drives for synchronization**:

Aliyun Drive, 115 Drive, Microsoft OneDrive, Baidu Netdisk, and Google Drive.

● **Supported synchronization directions**:

**Two-way sync**: Files are synchronized bidirectionally between the cloud drive and UGREEN NAS. Any changes on either side (such as adding, modifying, or deleting files) will be reflected on the other side.

**Sync cloud drive files to UGREEN NAS only**: Files are synchronized from the cloud drive to UGREEN NAS only. If a file is deleted from the cloud drive, the corresponding file in UGREEN NAS will also be deleted.

**Sync UGREEN NAS files to cloud drive only**: Files are synchronized from UGREEN NAS to the cloud drive only. If a file is deleted from UGREEN NAS, the corresponding file in the cloud drive will also be deleted.

● **Supported synchronization modes**:

**Real-time sync**: Enables automatic real-time file synchronization, but consumes relatively more system resources.

**Manual sync**: File synchronization occurs only when "**Sync now**" is manually clicked. Enabling manual sync helps reduce computing resource usage and server load.

**Scheduled sync**: Files are synchronized automatically at regular intervals based on a predefined schedule. When this option is selected, you can click "**New plan**" to configure the sync frequency (Every day / Every week / Every month / Once / Customize) and the start time.

### Creating Two-Way Sync Task

To keep files in the cloud and on your NAS fully synchronized (including additions, modifications, deletions, and moves), please follow these steps to create a sync task:

1. On the "**Conect**" page, click "**Sync Cloud Drives with NAS**"**>**"**Create sync task**" to open the setup wizard.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/b57d43d14e974de6a571907169156ec5.webp)

2. Configure the sync rules by selecting the cloud drive path and the NAS path, and set the sync direction to **"Two-way sync"**.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/ac0a5602f7f5444ea1ee5d00710c724f.webp)

3. In **"Advanced settings"**(optional), you can precisely select subfolders for synchronization, configure file filtering rules, and define how filename conflicts are handled. After completing the settings, click **"Next"**.

**Description:**

● **Sync folder**: Select the remote folders to be synchronized. (Files and folders with names starting with "**.**" usually indicate hidden files and hidden folders.)

● **File filter**: You can prevent specific files from being synchronized by setting a maximum file size or by specifying file names or file extensions. This helps save storage space and ensures efficient use of cloud storage. In addition, you can click "**Add**" to create additional filtering rules.

● **File conflict**: Select how file conflicts should be handled when they occur (rename conflicting files or overwrite existing files).

![](https://file-us.ugreennas.com/admin/article/2026-08-17/8c50f48e28784653ad1e8c1a515046a9.webp)

4. After configuring the synchronization policy, click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-08-17/7c87edd1c3e34646b572ad614cdafb52.webp)

5. Review the task settings. If everything is correct, click "**Confirm**" to create the task. Created tasks can be viewed and managed on the "**Sync task**" page.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/f73f17f4c5de40e7943776469033edb0.webp)

### Creating One-Way Sync Task

If you want to enable one-way synchronization between the cloud drive and the NAS (including file additions, modifications, deletions, and moves), please create a sync task by following the steps below:

1. On the **"Connect"** page, click "**Sync Cloud Drives with NAS**">"**Create sync task**" to open the setup wizard.

2. Set sync rules by selecting the cloud path, NAS path, and choosing "**Sync only data changes from the cloud storage and the NAS**" or "**Sync only data changes from the NAS to the cloud drive**". Click "**Next**" after setting.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/cec79fd7423b4ccda479ff9d1f8e22f6.webp)

3. Set a sync strategy and Click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-08-17/78f83a7482ba4276a86ccfc2a9952d7e.webp)

4. Review the task settings. If everything is correct, click "**Confirm**" to create the task. The created task can be viewed and managed on the "**Sync task**" page.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/5e1eb22b7e87448692724b6ad1a8cd4a.webp)

**Note:** When the synchronization mode of a sync task is set to "**Real-time Synchronization**", to prevent missed synchronizations caused by network fluctuations, you can enable the "**Polling period**" feature (on the "**Connection**" page, click the "**…**" button next to the cloud drive and select "**Management**"). This allows the system to periodically perform a full comparison of file lists. Please note that enabling the polling interval may affect hard drive hibernation.

### View Sync Task Progress

After creating a sync task, you can view detailed progress and synchronization status on the "**Sync task**" page.

● **Add a new sync task**: Click "**Add**" to create a new sync task.

● **Start a sync task immediately**: If a sync task has not started, click "**Sync now**" to start the synchronization.

● **View sync task details**: Click "**More**" to edit or delete the sync task.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/9dafbd48d1f445559468d5d0edba41ca.webp)

**Notes**:

● If you have read-only permission for a remote shared folder, it cannot be set as a synchronization destination.

● When selecting a folder to synchronize, it must not be located in the same directory as another folder that is already being synchronized under the same connection.

● After deleting a sync task, if you want to reconnect, a full resynchronization is required.

## View Logs

On the "**Log records**" page, you can search and view detailed operation logs (including file transfer records and action log records). You can also export logs in TXT, CSV, or HTML format to your local computer.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/31e8fe96fd69421c8acf990e85d6e959.webp)

## Set Administrator Mode

If your account role is "**Administrator**", you can enable "**Administrator mode**" in "**Settings**" of the "**Cloud Drives**" app. Once enabled, you can view and manage other users' Cloud Drive connections on the "**Overview**" page.

**Note**:

● Administrator mode is disabled by default and must be enabled manually.

● In Administrator mode, if you have not connected any Cloud Drive, you cannot view other users' Cloud Drive connections. To view and manage other users' connections, add at least one Cloud Drive connection first.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/3607637b7d4b4470aa7026ac32bd31c6.webp)

## FAQ

**Q1: Unable to connect to Google Drive?**

Please check whether your NAS network environment can normally access Google services. If network access is restricted, try switching to a different network or reconnecting in an environment where Google services are available.

![](https://file-us.ugreennas.com/admin/article/2026-08-17/91b8ef831fb7442783454010e541fe88.webp)
