# Cloud Drive File Encryption

> **Article ID**: `932`  
> **Category**: `Application Guide > Cloud Drives > Cloud Drive File Encryption`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/932  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client, Web Browser

**Applicable Version**: UGOS Pro Firmware 1.19.1.0093 or later

The screenshots in this document are for reference only. The actual interface may vary slightly depending on the system or app version, please refer to the actual interface displayed.

## Introduction

Cloud Drives supports file encryption for connected cloud drives. After enabling this feature, files can be encrypted when uploading files to a cloud drive or creating a cloud drive sync task.

After encryption, the cloud drive cannot recognize or access the file contents. When encrypted files are downloaded or synced back to NAS, the system can use the configured password to decrypt them.

**Note**: Keep your encryption password safe. If you forget or change the password, encrypted files cannot be decrypted or downloaded.

## Feature Access

1. Open "**Cloud Drives**" and find the target cloud drive in the connection list on the sidebar.

2. Hover over the cloud drive name, click "**···**" on the right ＞ "**Cloud drive file encryption**".

![](https://file-us.ugreennas.com/admin/article/2026-08-26/58186705739649b58cc19d110469592e.webp)

3. "**Enable**" the feature, set a password, and click "**Confirm**"

![](https://file-us.ugreennas.com/admin/article/2026-08-26/9744f931d3784ebfa062188431743428.webp)

After enabling, this cloud drive connection can use the file encryption feature.

## Encrypt Files During Upload

After enabling Cloud drive file encryption, you can enable encryption when uploading files to a cloud drive. Follow these steps:

1. Open "**Cloud Drives**", click the target cloud drive, and select the files to upload.

2. On the upload page, enable "**Encrypted upload**", and click "**Upload**".

![](https://file-us.ugreennas.com/admin/article/2026-08-26/062e393c3a5d49a99bac8db3ee6bcd3b.webp)

During the upload process, the system will automatically encrypt the files using the configured password.

## Whether to Decrypt Encrypted Files When Downloading

When downloading encrypted files from a cloud drive, you can select whether to decrypt the files in the bottom-left corner of the page.

![](https://file-us.ugreennas.com/admin/article/2026-08-26/017830ddb9f7477a89e240156c360a03.webp)

### Download Without Decryption

If you select "**Do not decrypt**", the downloaded files will have garbled file names. When opened, the file contents will also appear as garbled text.

## Download with Decryption

If you select "**Decrypt**", the system will automatically decrypt the downloaded files using the currently configured password.

● When the password is correct, the downloaded file names will be displayed normally and the file contents can be opened as usual.

● When the password is incorrect, the file names cannot be decrypted correctly and the download task will fail.

![](https://file-us.ugreennas.com/admin/article/2026-08-26/24f04ead9ca449e299945e015ce9a99c.webp)

**Note**: If the password used to encrypt the file is different from the password currently set for Cloud drive file encryption, enabling file decryption will not decrypt the file correctly.

## What to Do If Download Fails Due to an Incorrect Password?

If a download fails due to an incorrect password, the task in the download list cannot be recovered by retrying. Even if you later change the Cloud drive file encryption password back to the correct one and retry the task, the download will still fail.

If this issue occurs, follow these steps:

1. Change the Cloud drive file encryption password to the correct password.

2. Return to the cloud drive file list, select the file again, and start a new download task.

## Enable File Encryption in Sync Tasks

When creating or editing a cloud drive sync task, you can enable encrypted sync in "**Advanced settings**".

![](https://file-us.ugreennas.com/admin/article/2026-08-26/947b61ad26604153874cb3d5ddda309c.webp)

After enabling:

● Files will be automatically encrypted when synced to the cloud drive.

● The cloud drive cannot recognize or access the encrypted files normally.

● When encrypted files are synced back to NAS, the system will automatically decrypt them.

![](https://file-us.ugreennas.com/admin/article/2026-08-26/9185ec6648c04b52ab77ebce7c01f0f9.webp)

## Notes

● Forgetting the password will prevent files from being decrypted or downloaded.

● Do not modify the names of encrypted files. Otherwise, the files may not be decrypted correctly.

● Encrypted files displayed on the cloud drive cannot be opened normally. This is expected behavior after encryption.

● Feature names and page layouts may vary slightly between different system versions. Please refer to the actual interface display.
