# Mount UGREEN NAS Drives on a Computer via SMB

> **Article ID**: `359`  
> **Category**: `Application Guide > Control Panel > File Service > Mount UGREEN NAS Drives on a Computer via SMB`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/359  

---

## Applicability

**Applicable client**: UGREEN NAS PC client (Windows/macOS).

**Applicable version**: NAS firmware 1.16.0.0042 or later.

This document is for reference only. The actual interface and operation paths may vary slightly depending on system or app version updates. Please refer to the actual interface.

## Overview

SMB is one of the most widely used and efficient file sharing protocols for local networks. After the service is enabled, files on the NAS can be accessed directly from Windows File Explorer or Mac Finder using the NAS account credentials, without opening the UGREEN NAS client.

## Enable SMB Service

1. Sign in to the system desktop, open "**Control Panel**", then click "**File Service**".

2. Switch to the "**SMB**" tab in the top bar and select "**Enable SMB service**".

3. Click "**Apply**" to enable the service.

Note: The default workgroup is `WORKGROUP`. If there are no special requirements for enterprise network isolation, keep the default setting. Click "**Advanced**" below to fine-tune the underlying protocol settings.

![](https://file-us.ugreennas.com/admin/article/2026-06-15/6cf444fe439343e4b931447365ceb421.webp)

## How to Connect and Mount on a Computer

After the service is enabled, make sure the NAS and the local computer are on the same LAN. Use the access path that matches the computer operating system.

**Note**: `DXP4800-8888` and `172.17.70.64` in the examples below are **for reference only**. Replace them with the actual device name or LAN IP address of the NAS.

### Access from Windows

Open **Windows File Explorer** from "**This PC**" or "**My Computer**", enter the LAN network path in the address bar at the top, then press **Enter**:

● **By device name:** Enter \\actual-device-name, for example \\DXP4800-8888.

● **By IP address:** Enter \\actual-LAN-IP, for example \\172.17.70.64.

![](https://file-us.ugreennas.com/admin/article/2026-06-15/e50c5e15caaa4a53b62e4e289717e18d.webp)

### Access from macOS

Open **Finder** on the Mac and press `Command + K` to open the "**Connect to Server**" window. Enter the server address:

● **By device name:** Enter smb://actual-device-name, for example smb://DXP4800-8888.

● **By IP address:** Enter smb://actual-LAN-IP, for example `smb://172.17.70.64`.

## Authentication and Special Scenarios

When connecting for the first time, the system will prompt for credentials. Follow these login rules:

● **Local standard user:** Enter the username and password created on the UGREEN NAS to complete the mount authorization.

● **Domain user:** If the NAS has joined a domain, use the following format when signing in: domain\domain-user-account+ password, for example ABC\xiaoming + Aa123456.

● **Use with Apple Time Machine:** To use Mac "**Time Machine**" backup over SMB, enable SMB first, then select "**Enable Bonjour Service**" in "**Advanced Settings**" under "**File Service**". This enables the device discovery broadcast service required for Time Machine.

![](https://file-us.ugreennas.com/admin/article/2026-06-15/ce784107885e4be891747f939c41ed4b.webp)
