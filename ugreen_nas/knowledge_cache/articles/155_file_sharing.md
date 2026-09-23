# File Sharing

> **Article ID**: `155`  
> **Category**: `Application Guide > Files > File Sharing`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/155  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: NAS Firmware 1.18.0.0093 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

The Files app supports creating share links for files and folders. After a share link is created, you can send the link or QR code to others, who can access the shared content through the link.

When creating a share link, you can configure the recipient, validity period, access method, password, and visit limit, and choose whether to allow downloads.

## Create a Share Link

1. Open the Files app and go to the directory where the target file or folder is located.

2. Right-click the file or folder you want to share and select "**Share**".

3. Configure the sharing settings on the Share page.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/6597a625ee7540e1bbb4642378bae308.webp)

4. After confirming the settings, click "**Confirm**".

5. The system will automatically generate a share link and QR code. Send the share link or QR code to users who need access.

## Share Settings

### Access Method

The following access methods are supported:

● **LAN**

● **UGREENlink**

● **DDNS**

### UGREENlink Sharing

To share using **UGREENlink**, enable the UGREENlink service first.

Follow the steps below:

1. Open **Control Panel** and go to "**Device connection**" > "**Remote access**".

2. Enable the UGREENlink Remote Access service.

After enabling the service, you can select UGREENlink as the access method when creating a share link.

### DDNS Sharing

The **DDNS** option is hidden by default. To share using DDNS, the following requirements must be met:

● DDNS support has been enabled and domain name service configured in Control Panel under "**Device connection**" > "**Remote access**".

● The current NAS system is accessed using the configured DDNS domain.

After meeting the above requirements, the DDNS access method will be available when creating a share link.

## View Share Links

**Users on This Device**

Users on this device can access shared content after opening the share link and completing account login. They can download shared files or folders. In addition, users on this device can view shared content in "**Files**" > "**Shares**".

**External Users**

External users do not need to register an account. They can access shared content by opening the share link and download shared files or folders.

**Note**:

● Image, audio, video, and other file types support online preview, allowing users to view files without downloading them.

● Online preview requires browser support. If certain files cannot be opened, it may be because the file format is not supported for direct preview by the current browser. You can download the file and open it using a local application.

## Manage Share Links

On the "**Sharing management**" page, you can centrally view and manage all created file share links. Whether sharing files with other accounts on this device or generating links for external users, you can manage all share links in one place.

Open the "**Files**" app, click "**Management**" > "**Sharing management**" on the top toolbar to enter the management page.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/90e5f94c74724cd4ad49d1a099d0475e.webp)

### Share List Information

The page displays key information and statuses of all share records in a list:

● **Title**: Displays the name of the shared file or folder.

● **Recipient**: Indicates the target recipient of the share, including "**External user**" (access through a link) or "**User on this device**" (sharing between accounts).

● **Validity**: Displays the link expiration date. The status includes a specific expiration date (for example, 2026-01-01) or "**Permanent**".

● **Status**: Sharing (the link is currently available); Invalid (the link has expired and can no longer be accessed externally).

### Management Operations

**Individual Management**:

Three shortcut action icons are available in the "**Actions**" column on the right side of each list item:

● **Copy link**: Copy the share link to the clipboard with one click for easy sharing.

● **Edit settings**: Modify the recipient, validity, password, visit limit, access method, and whether downloads are allowed.

● **Delete share**: Stop sharing immediately. The link will become invalid and can no longer be accessed.

**Batch Maintenance**:

The top toolbar provides efficient maintenance tools:

● **Clear invalid links**: Click "**Clear invalid links**" at the top to automatically remove all historical records with the "**Invalid**" status and quickly free up list space.

● **Delete**: Select one or more records in the list, then click the red "**Delete**" button to manually remove the selected share records.

● **Search**: Enter file title keywords in the search box at the top right to quickly locate specific share records.

## Related Information

[How to Generate File Sharing and Request Links via DDNS?](https://support.ugnas.com/knowledgecenter/detail/article/zh-CN/863)
