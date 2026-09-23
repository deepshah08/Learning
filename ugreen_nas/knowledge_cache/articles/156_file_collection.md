# File Collection

> **Article ID**: `156`  
> **Category**: `Application Guide > Files > File Collection`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/156  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: NAS Firmware 1.18.0.0093 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

The Files app provides the Request files feature, which allows users to collect files from others in one place. After creating a file request link, others can upload files to the specified folder through the link without logging in to the NAS, making it easy to collect, organize, and back up data.

## Recommended Use Cases

The Request files feature can be used in the following scenarios:

● Collecting documents or images from customers

● Collecting student assignments from teachers

● Allowing team members to upload collaborative documents

● Collecting registration attachments for events

## Create a File Request

If you need to collect files uploaded by others, you can create a file request and generate a link for others to upload files.

Follow the steps below:

1. Open the Files app and go to the target folder where you want to store the collected files.

2. Right-click the folder and select "**Request files**" from the menu.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/6dabe2433e1047e4a720720a5c0e6b5a.webp)

3. On the file request settings page, configure the request parameters.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/9964b8f312914980a8b3a93f6b0ef214.webp)

4. Confirm that the settings are correct, then click "**Confirm**".

5. The system will automatically generate a file request link and QR code. Send the link or QR code to users who need to upload files.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/6cb25f3c8b0441c98deedb1e560d6eb9.webp)

## File Request Settings

### Access Method

The following access methods are supported:

● **LAN**

● **UGREENlink**

● **DDNS**

### UGREENlink Sharing

To share using **UGREENlink**, make sure the UGREENlink service is enabled first.

Follow the steps below:

1. Open **Control Panel** and go to "**Device connection**" **>** "**Remote cccess**".

2. Enable the UGREENlinkremote access service.

After enabling the service, you can select UGREENlink as the access method when creating a file request link.

### DDNS Sharing

The **DDNS** option is hidden by default. To share using DDNS, the following requirements must be met:

● DDNS support has been enabled and the domain service has been configured in Control Panel **>** "**Device connection**" **>** "**Remote access**".

● The current NAS system is accessed through the configured DDNS domain.

After meeting the above requirements, the DDNS access method will be available when creating a file request link.

## Manage File Requests

1. Open the Files app and go to the file management page.

2. Click "**Management**" in the top navigation bar and select "**File request management**".

![](https://file-us.ugreennas.com/admin/article/2026-08-07/62ddd2adbf7b453bad25e0056a8f5fbb.webp)

On the "**File request management**" page, you can view created file request information and manage file requests in one place. The available operations are as follows:

![](https://file-us.ugreennas.com/admin/article/2026-08-07/79b63c7bbe6a43568880ded727a6309d.webp)

① **Edit file request links**: Select a file request and modify its related settings.

② **Delete file request links**: Delete file requests that are no longer needed.

③ **Share file request links**: Copy the file request link or QR code and send it to other users, allowing them to upload files.

④ **Set validity period**: Click the "**Validity**" icon to set the number of valid days for the file request link and view the expiration date.

⑤ **Set access password**: Click the "**Password**" icon to set a password for the file request link. After enabling a password, users must enter the correct password to access the link.

⑥ **Set visit limit**: Click the "**Visits**" icon to set the maximum number of visits allowed for the file request link and configure the access limit.

⑦**Clear invalid links**: Remove file request links that have expired.
