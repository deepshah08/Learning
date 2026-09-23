# How to Sync Data Between UGREEN NAS and Google Drive?

> **Article ID**: `613`  
> **Category**: `Application Guide > Cloud Drives > How to Sync Data Between UGREEN NAS and Google Drive?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/613  

---

With the cloud drive tool, you can easily connect to Google Drive for quick file uploads and downloads. This is particularly helpful for data migration, backups, and when replacing your UGREEN NAS device. This guide will provide detailed instructions on how to connect Google Drive and facilitate data transfer between the UGOS Pro system and Google Drive.

## **How to Connect Google Drive to UGREEN NAS**

1. Open the Cloud Drives page, click "New Connection".
2. In the list of connected cloud drives, select Google Drive, then click "Next".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/c590577a-65c1-400a-98f9-a3d9328fb770.png)

3. Log in to Google Drive by entering your email/phone and password. If you don’t have an account, register first.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/43ead570-3d2f-4003-9b0f-50cf40e08e20.png)

4. Once logged in, return to the overview page to check the connection status of Google Drive.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/3c6839b3-7b56-42c7-aae0-ca89f5a16c6b.png)

## **How to Upload Files from UGREEN NAS to Google Drive**

1. Go to the [Cloud Drive] page and click on the connected Google Drive to check the current storage capacity.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/ceed639d-5668-4a0f-be11-01ad8304c3b1.png)

2. On the [Connection] page, select "Upload to Cloud", then click "Select File".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/50ba0508-6894-466d-8eed-e8ef85d8c832.png)

3. Choose the file save path and click "Choose File" again.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/a65762c3-efe9-4cdc-ad1c-6601a8a4342d.png)

4. In the [File Selection] window, select the files or folders from UGREEN NAS and click "Confirm"

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/a9055e24-fe1d-4af5-9bd1-2c42e2686538.png)

5. During the upload, you can monitor the progress in the Upload List.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/e89ca14e-614e-4231-bbc5-710a2fcde828.png)

6. Once uploaded, visit the Google Drive website and check the corresponding folder for the uploaded files.

## **How to Download Files from Google Drive to UGREEN NAS**

1. Go to the [Cloud Drives] page and click "Download" under Select File.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/8764764b-2dde-4c0b-a0c0-048de04cef10.png)

2. Select the files or folders to download from Google Drive and click "Next".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/af067489-9e01-4d8c-aecf-c5ba41b095ec.png)

3. Set the save path on UGREEN NAS and click "Confirm" to start the download.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/203ddbb2-e158-4ee8-9e62-2b50f34fd08c.png)

4. During the download, monitor the progress in the Download List.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/d7c42e6c-a1e8-4068-8d95-4a788eb9c647.png)

5. Once the download is complete, go to "**Files**" on UGREEN NAS and locate the corresponding folder to view the downloaded files.

## **How to Set Up a Data Sync Task Between Google Drive and UGREEN NAS**

1. On the [Cloud Drives] page, click "Create Sync Task" under Sync Cloud Drive with NAS.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/d3bf0fe3-e414-405c-bdcf-7352f12b398d.png)

2. Set sync rules:

* **Cloud Path**: Specify the folder on Google Drive to sync (e.g., "GoogleDrive/test").

* **NAS Path**: Specify the folder on UGREEN NAS to sync (e.g., "/Personal Folder/mialu/test").

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/eab55138-7590-46d1-9e7f-a81e58c04fd9.png)

Choose the sync direction:

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/dfccddc9-09d9-4d40-a89b-76bd73dde129.png)

**Two-way Sync**: Any additions, modifications, or deletions made on either Google Drive or UGREEN NAS will be synchronized to the other.

**Sync Google Drive to NAS Only**: Changes on Google Drive will sync to UGREEN NAS, but any changes made on NAS will not sync to Google Drive. By default, deleting a file on Google Drive will not delete it on NAS.

**Sync NAS to Google Drive Only**: Changes on UGREEN NAS will sync to Google Drive, but any changes made on Google Drive will not sync to NAS. By default, deleting a file on NAS will not delete it on Google Drive.

3. **Set Sync Strategy**: Choose a sync strategy based on your needs, such as selecting "Manual Synchronization," then click" Next".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/d0062e60-058c-46b7-bd8e-563e6b0fcca0.png)

4. **Confirm Task Information**: Review the settings, and once confirmed, click "Confirm" to complete the task creation.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/726ad618-301d-4946-b9ba-2a49ee8ed4d7.png)

5. Check the progress and status of the task in the [Sync Task] list.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250304/6d26c891-57cf-4451-9ebb-636345797902.png)

**Notes**

* **Network Connection**: Ensure a stable network connection during file transfer to avoid interruptions or data loss.
* **Storage Space**: Make sure there is enough storage space on both UGREEN NAS and Google Drive to prevent transfer failures due to insufficient space.
