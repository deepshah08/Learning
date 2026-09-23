# How to Generate File Sharing and Request Links via DDNS?

> **Article ID**: `863`  
> **Category**: `Application Guide > Files > FAQ > How to Generate File Sharing and Request Links via DDNS?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/863  

---

## Applicability

**Applicable clients:** UGREEN NAS desktop app (Windows/macOS) and UGREEN NAS mobile app (iOS/Android).

**Applicable version:** NAS firmware 1.16.0.0042 or later.

**Applicable users:** Users with a public IP address and a DDNS domain name.

This article is for reference only. The actual interface and operation path may vary slightly depending on your system or app version. Please refer to the actual interface.

## Why Use DDNS

In earlier versions, system-generated links for file sharing and Request files only supported access via a **LAN IP address** or the official **UGREENlink service**.

UGREEN NAS now supports sharing via **DDNS**, or Dynamic DNS. Compared with UGREENlink, the official relay service, DDNS can offer significant speed advantages:

● **Native direct connection:** With DDNS, access from external networks no longer goes through official relay servers. Instead, external users can establish a point-to-point connection with your NAS.

● **Higher speed potential:** Transfer speeds are no longer limited by the bandwidth of official servers. Instead, the speed depends on **the bandwidth limit of the network where your NAS is located**, such as the upload bandwidth provided by your ISP. This usually allows for a faster download and upload experience.

**Note**: Actual speeds may still be limited by the network environment of the user accessing the link, as well as any cross-network or cross-region routing limitations from the ISP.

## Requirements

To use the system’s native DDNS sharing method, make sure your setup meets the following requirements:

● **Desktop configuration only**

You need to log in to the **UGREEN NAS desktop app (Windows/macOS) or the web browser client**, then configure the DDNS service in **Control Panel**>**Device Connection**. Please note that the current version of the UGREEN NAS mobile app (iOS/Android) does not support this configuration feature.

● **Native service required**

This sharing mechanism **does not support** **third-party DDNS services**. If you use a third-party DDNS service through a home soft router, the Jiedianxiaobao app, or a Docker container, the system will not be able to detect it. As a result, when you create a file sharing or Request files link, the **DDNS** option will not appear in the access method drop-down menu.

## Configure Native DDNS

1. On the system desktop, open "**Control Panel**", then click "**Device Connection**".

2. Switch to the "**Remote Access**" tab at the top.

3. Find and select "**Enable DDNS Support**" on the page, then click "**+ Add**" below.

![](https://file-us.ugreennas.com/admin/article/2026-05-29/e667952f4c6b4a249956551c80c6ca27.webp)

4. Select the service provider where you purchased your domain name, then enter the required key and domain information according to the provider’s parameter requirements.

5. After filling in the information, click "**Connection test"**. After the system shows that the connection status is "**Normal"**, click "**Apply"** to save the settings. The NAS will automatically update the changing public IP address to the domain name in the background.

![](https://file-us.ugreennas.com/admin/article/2026-05-29/aed9e13a87d94e16866d1897028cabb6.webp)

## Log In to the System Using the DDNS Domain Name

1. After DDNS takes effect, the connected DDNS domain name will show the status "**Normal**".

![](https://file-us.ugreennas.com/admin/article/2026-05-29/c21377aae6634ec1a222916cbce761bf.webp)

2. Log out of the current session, then log back in to the UGREEN NAS system using the DDNS domain name you just configured.

**Note:** This step is required in order to use the DDNS sharing option.

## Create a File Sharing or Request Files Link

Before performing the following steps, make sure you are currently logged in to the UGREEN NAS system using the DDNS domain name configured in "**Control Panel**". Do not use UGREENlink or a DDNS domain name configured through a third-party tool. Only in this login state can the system use the DDNS sharing mechanism.

### Steps on Desktop

1. After logging in to the UGREEN NAS system with your DDNS domain name, open "**Files**".

2. In the file list, right-click the target folder you want to share or use for requesting files.

3. From the pop-up menu, select "**Share**" or "**Request files**".

![](https://file-us.ugreennas.com/admin/article/2026-05-29/22881cd1a2cd4b59b367665800b0e0db.webp)

4. In the creation window, find "**Access method**". **DDNS** should be selected by default.

5. Set the "**Validity**" period and "**Password**" as needed.

6. When finished, click "**Confirm**". In the window that appears, click "**Copy**" and share the link with the intended user. When the user opens the link, data will be transferred over your NAS network connection.

![](https://file-us.ugreennas.com/admin/article/2026-05-29/59806d113bc349ea907bdcdd7d0bd33b.webp)

### Steps on Mobile

1. After logging in to the UGREEN NAS app with your DDNS domain name, open "**Files"**.

2. Find the file or folder you want to use, then tap "**···"** to the right of its name.

3. From the pop-up menu, select "**Share"** or "**Request files"**.

4. In the creation window, find "**Access method"**. **DDNS** should be selected by default.

5. Set the "**Validity"** period and "**Password"** as needed.

6. When finished, tap "**Copy"**, or share the link through another app. When the user opens the link, data will be transferred over your NAS network connection.

![](https://file-us.ugreennas.com/admin/article/2026-05-29/c3716ace7c7640d8ace0b558abea976c.webp)

## Related Articles

### How to Configure a DDNS Domain Name to Log In to UGREEN NAS

<https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmODYyIiwiY2xpZW50VHlwZSI6IlBDIn0=>
