# Network Folder Connection Guide

> **Article ID**: `153`  
> **Category**: `Application Guide > Files > Network Folder > Network Folder Connection Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/153  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: UGOS Pro Firmware 1.18.0.0093 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

The "**Connect to network folder**" feature lets you connect remote storage resources directly to your NAS. You can mount **other devices**, **servers**, or **third-party cloud drives** in the Files app, allowing you to access and manage external data just like local files without repeatedly downloading or transferring files.

## Supported Connection Types

Currently, the following two types of connections are supported:

![](https://file-us.ugreennas.com/admin/article/2026-08-14/9719085486fe4470acf279e04392a859.webp)

### General Protocols

Suitable for LAN devices or remote servers.

● **SMB**: Commonly used for NAS devices or Windows shared folders within a local network.

● **FTP**: A standard file transfer protocol.

● **WebDAV**: Supports cross-network access and is commonly used to connect NAS devices or cloud storage services that support this protocol.

● **SFTP**: A secure file transfer protocol based on SSH, offering enhanced security.

### Cloud Drive Service Types

Currently supported services include **115 Cloud Drive**, **Quark Cloud Drive**, **Aliyun Drive**, and **OneDrive**.

## Connect via a Network Protocol (SMB Example)

1. Open the "**Files**" app, then click "**+**" in the top toolbar > "**Connect to network folder**".

![](https://file-us.ugreennas.com/admin/article/2026-08-14/e5595a4e303c45d2be121093c4567ef2.webp)

2. Select "**SMB**", then click "**OK**".

![](https://file-us.ugreennas.com/admin/article/2026-08-14/44a1caa1b6834fbc9f2c5a33af77389f.webp)

3. **Enter the following information**:

● Enter the Server address (such as the NAS IP address or domain name).

● Enter the Account and Password (such as your NAS account credentials).

● After verification, select or directly enter the Server folder you want to mount.

**Note**: Example of a server folder path (using a UGREEN NAS as an example): If the shared folder is named downloads, enter /downloads. The path is case-sensitive and must exactly match the shared folder name (for example, /downloads is not the same as /downloads).

![](https://file-us.ugreennas.com/admin/article/2026-08-14/0542225b5adb40da9f463e488689fa8e.webp)

(Optional) Click "**Advanced settings**" to enter a device description or enable **Automount at startup**.

4. After completing the settings, click "**Done**". The mounted Network folder will appear in the sidebar on the "**Files**" home page.

![](https://file-us.ugreennas.com/admin/article/2026-08-14/4856ea196d774fcc88ea5746a17592f8.webp)

## Connect to a Cloud Drive (115 Cloud Drive Example)

1. On the "**Connect to network folder**" page, select the cloud drive you want to connect to, then click "**OK**".

![](https://file-us.ugreennas.com/admin/article/2026-08-14/b69004bb4fd24effb3de39ea41c58392.webp)

2. A QR code will appear. Use the corresponding cloud drive mobile app to scan the QR code and confirm authorization.

![](https://file-us.ugreennas.com/admin/article/2026-08-14/46643c3b05fd4882bc9d6959a125b70c.webp)

3. Once authorization is successful, the cloud drive contents will automatically load in the Network folder list.

![](https://file-us.ugreennas.com/admin/article/2026-08-14/9215a7c3df904e99a531e77d8a853e7b.webp)

## Manage Network Folders

You can perform the following management operations on mounted network folders:

![](https://file-us.ugreennas.com/admin/article/2026-08-14/eac5960779a44563ac33adce972a516a.webp)

● **Disconnect**: Temporarily disconnects communication with the remote server. Select the folder, right-click it, and choose "**Disconnect**". To restore the connection, select the folder again and choose "**Reconnect**".

● **Unmount**: Completely removes the mount configuration. Select the folder, right-click it, and choose "**Unmount**".

**Note**: Disconnecting or unmounting a network folder **does not delete** the original files on the remote server.

## Notes

● You can browse, copy, move, delete, rename, and download files in a network folder. The available operations depend on the permissions configured on the remote server or cloud drive account.

● Access speed depends on the current network environment. If the remote device is powered off or the cloud drive service is unavailable, the folder will be temporarily inaccessible.

● If you change connection information such as the server address, account, or password, you need to unmount the current connection and add it again.
