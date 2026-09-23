# How to Mount 123Pan via Cloud Drives?

> **Article ID**: `931`  
> **Category**: `Application Guide > Cloud Drives > How to Mount 123Pan via Cloud Drives?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/931  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: NAS Firmware 1.19.1.0063 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

UGREEN NAS supports mounting 123Pan through the Cloud Drives. Once mounted, you can access and manage files stored in 123Pan directly from your UGREEN NAS, without repeatedly downloading or transferring files between the cloud and local storage.

**Note**: Access to and use of this feature depend on your network environment. Before using it, make sure your current network can access 123 Pan services normally.

## Preparation

Before mounting 123Pan, make sure you have a valid 123Pan account. The 123Pan website may vary by region and language. If you are unable to register or sign in to your 123Pan account, contact 123Pan technical support for assistance.

## Add a 123Pan Connection

1. On the UGREEN NAS desktop, open the Cloud Drives app and click "**New connection**" in the sidebar.

![](https://file-us.ugreennas.com/admin/article/2026-08-25/3e9af9bfc52e46d884273413adf07c71.webp)

2. In the pop-up list of cloud drive types, select "**123Pan**", then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-08-25/a976571b82b34ec38858bf473019974b.webp)

3. In the login window, enter your 123Pan account information to sign in and complete authorization.

![](https://file-us.ugreennas.com/admin/article/2026-08-25/07223abec2174a108875e970716e75aa.webp)

Once connected, 123Pan appears as a separate directory in the connection list in the Cloud Drives sidebar.

## Delete an Added Cloud Drive Connection

If you no longer need a connection, you can delete it from UGREEN NAS. This only disconnects the cloud drive and does not delete any files stored in the cloud.

**Steps**:

1. Open the **Cloud Drives** app. In the connection list in the sidebar, find the 123Pan connection you want to delete.

2. Hover over the cloud drive name, then click "**···**" > "**Delete**" on the right.

![](https://file-us.ugreennas.com/admin/article/2026-08-25/bb4bbdec0cfb415fb105b20ebffa2a98.webp)

3. In the confirmation window that appears, click "**Deletion**".

After deletion, the connection will be removed from the Cloud Drives sidebar.

## Manage Files in 123Pan

After successfully adding a 123Pan connection, you can use Cloud Drives to transfer files between UGREEN NAS and 123Pan.

The following features are supported:

● Upload files from the NAS to 123Pan.

● Download files from 123Pan to the local NAS.

● Create sync tasks to keep data consistent between the cloud drive and UGREEN NAS directories.

● View upload, download, and operation logs.

File transfer speed may vary depending on the network environment, file size, and 123Pan service status.

### Upload NAS Files to 123Pan

1. Open the Cloud Drives app. In the connection list on the left, click the added 123Pan connection.

2. In the main panel on the right, locate "**Upload to Cloud Drive**" and click "**Select file**".

3. Configure the cloud drive save path, which specifies the directory where the files will be stored in 123Pan, then click "**Select file**".

4. In the file picker that appears, select the NAS files you want to upload, then click "**Upload**".

After the upload starts, click "**Upload**" in the top navigation bar to view the upload progress in real time.

### Download 123Pan Files to the Local NAS

1. Open the Cloud Drives app. In the connection list on the left, click the added 123Pan connection.

2. In the main panel on the right, locate "**Download to NAS**" and click "**Select file**".

3. In the download window, select the cloud files you want to download from 123Pan, then click "**Next**".

4. In the location selection window, specify the folder on the local NAS where you want to save the files, then click "**Confirm**" to start the download.

After the download starts, click "**Download**" in the top navigation bar to view the download progress in real time.

## View Cloud Drive Logs

The system automatically records cloud drive operations to help troubleshoot transfer errors or audit operations.

1. Open the Cloud Drives app. In the connection list on the left, click the added 123Pan connection.

2. In the top navigation bar of the main panel on the right, click "**Log records**".

3. On the log page, switch between "**File transfer records**" and "**Action log records**" to view the corresponding logs.

![](https://file-us.ugreennas.com/admin/article/2026-08-25/718da9210bef4524880bc943e8419ac6.webp)

## FAQs

### Q1: Why is accessing files in 123Pan slow?

The speed of accessing 123Pan depends on your current network environment. Upload, download, and file browsing speeds may be affected by factors such as network quality and file size.

### Q2: What affects file operation permissions after mounting?

When browsing, copying, moving, deleting, renaming, or downloading 123Pan files in Cloud Drives, the actual permissions depend on the permission settings in 123Pan.

If you cannot delete, write, or move files, check the permissions in 123Pan first.

## Notes

● When uploading or downloading large files, make sure the network connection remains stable. Network interruptions may cause transfer failures or sync task errors.

● Before creating a sync task, confirm the sync direction and file conflict handling policy to avoid files being overwritten or repeatedly synced due to incorrect settings.

● If a sync task fails, check Log records first. Use the error information to troubleshoot issues related to the network, path, permissions, or account status.
