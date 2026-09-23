# [Tutorial] How to Access Files on UGREEN NAS via FTP Protocol

> **Article ID**: `489`  
> **Category**: `Application Guide > Control Panel > File Service > [Tutorial] How to Access Files on UGREEN NAS via FTP Protocol`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/489  

---

FTP (File Transfer Protocol) is a standard protocol used for transferring files over a network. You can use FTP to access and manage files stored on your NAS. With its simplicity, speed, and efficiency, FTP is widely used for file sharing and transfer. This article introduces how to enable the FTP service in UGOS Pro and allow users to access shared folders on UGREEN NAS via FTP.

## How to Enable the FTP Service in UGOS Pro?

1. Log in to the UGOS Pro system and go to **[Control Panel] > [File Service] > [FTP]**. Choose one of the following options and configure the related settings accordingly:

● **Enable FTP Service (Unencrypted):** FTP offers faster transfer speeds and requires fewer system resources.

● **Enable FTPS Service:** Due to encryption, FTPS provides slower transfer speeds and consumes more CPU resources.

![](https://file-us.ugreennas.com/admin/article/2025-08-28/d932aa799ee94bc296449e6e6e90393d.webp)

2. Configure additional **advanced settings** as needed. You can change the default FTP port (default is 21), enable FTP logging and encoding settings, and set limits on the maximum number of online users and upload/download speeds based on network conditions.

3. After completing the settings, click **"Apply"** to save and activate them.

## How to Access UGREEN NAS Files via FTP/FTPS on a Windows PC

1. Make sure that your Windows computer and the UGREEN NAS are on the same local network. You can refer to [“How to confirm if Your Computer and NAS Are on the Same Local Area Network.”](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMTIxLCJhcnRpY2xlSW5mb0lkIjozODgsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

2. Press`Win + E` to open File Explorer on your Windows computer.

3. In the address bar, enter `ftp://<NAS_IP Address>`，and press Enter. For example: `ftp://192.168.22.153`.

![](https://file-us.ugreennas.com/admin/article/2025-08-28/148f2d6a8fa9496dad94ef5b5b66cee1.webp)

4. You will be prompted to enter a username and password. Enter the account credentials for your UGREEN NAS device, then click "Log On."

![](https://file-us.ugreennas.com/admin/article/2025-08-28/9a2afd871e9c4623b55e8150be446679.webp)

5. After successfully logging in, you can access the files on your UGREEN NAS in File Explorer, just like browsing and managing local folders.

![](https://file-us.ugreennas.com/admin/article/2025-08-28/4e0aa34936c34d9e92e7858cce611068.webp)

## How to Access UGREEN NAS Files via FTP Client?

1. Open your FTP client (the following example uses FileZilla).

2. Enter the IP address or DDNS hostname of your UGREEN NAS in the Host field (e.g., `192.168.24.123`).

3. Enter the username and password for your UGREEN NAS. Note: The account you use must have the appropriate access permissions for the folder.

4. Enter the port number for FTP service on your UGREEN NAS. If no port number is specified, the default FTP port is`21`. If FTPS is enabled, the FileZilla client will automatically use port `21` for an encrypted connection. Then, click **"Quickconnect."**

5. Click **"Quickconnect"** to log in to your UGREEN NAS. Once logged in, you will be able to view the shared folder structure on the NAS and perform file uploads, downloads, or management operations.

![](https://file-us.ugreennas.com/admin/article/2025-08-28/e26812e61906429e9190766e60bf5791.webp)

**Please Note:**

● The default port number for FTP service is `21`.

● It is recommended to use `UTF-8` encoding for FTP service to ensure that the encoding settings of the FTP client match those of the UGREEN NAS, allowing for correct display of file contents.
