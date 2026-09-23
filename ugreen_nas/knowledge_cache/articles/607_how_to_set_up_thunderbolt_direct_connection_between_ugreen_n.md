# How to Set Up Thunderbolt Direct Connection Between UGREEN NAS and Computer for High-Speed File Transfer

> **Article ID**: `607`  
> **Category**: `Troubleshooting > Network Failure > How to Set Up Thunderbolt Direct Connection Between UGREEN NAS and Computer for High-Speed File Transfer`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/607  

---

## Applicable Models and Versions

● **Applicable Models:** UGREEN DXP480T Plus, DXP6800 Pro, DXP8800 series

● **Supported Firmware Versions:** NAS firmware version 1.2.0.2121 and above

## Preconditions

Before starting the setup, ensure the following conditions are met:

● Both the device and computer support Thunderbolt interfaces (Thunderbolt 3 or higher).

● Use a dedicated Thunderbolt cable for the connection.

● Firmware version is updated to 1.2.0.2121 or above.。

## Setup Steps

### Establish Thunderbolt Connection Between UGREEN NAS and Computer

1. Plug one end of the Thunderbolt cable into the Thunderbolt port on the UGREEN NAS and the other end into the Thunderbolt port on the computer (Thunderbolt port is usually marked with ⚡️).

2. Log in to the UGOS Pro system with an administrator account and go to [Control Panel] > [Network] > [Network Connection].

3. Once the connection is successful, NAS will automatically assign a dedicated Thunderbolt IP address. You can find and record the Thunderbolt IP address (e.g., 172.17.70.242) in the network connection page.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/20289e970085446d8b80c47012ee248a.webp)

### Transfer Files Using Thunderbolt Direct Connection

Once the connection is established, you can transfer files using the following four methods:

**Method 1: Transfer via Client (Within LAN)**

1. On the computer connected via Thunderbolt, open the UGREEN Cloud client and, on the local account login page, click "More Connections". Find the device with the Thunderbolt icon in the device search list, click "Connect", and enter the username and password to log in.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/550cda3088694c87bbf9e57f5ce5afb3.webp)

2. Once logged in, you can upload or download files through the file manager. This allows high-speed file transfer using Thunderbolt direct connection.

**Method 2: Transfer via Web Browser**

1. In the LAN, directly enter http://<NAS Thunderbolt IP>:9999 in the browser (e.g., http://169.254.4.109:9999) to log in to the UGREEN NAS.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/a3eaff2719a5416ebfccd8c321f28d39.webp)

![](https://file-us.ugreennas.com/admin/article/2025-08-26/36f4c4c9253445fbb1b0d37576aa99bc.webp)

2. In the "**Files**", upload or download files to test the transfer speed using Thunderbolt direct connection.

**Method 3: Use Samba to Access UGREEN NAS for File Access**

##### On a Windows computer:

1. Open [Control Panel] and go to [Files Service] > [SMB]. Check the "Enable SMB Service" option. If this service is already enabled, skip this step.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/667627d2dc9a4b8893093a3e372cf0a2.webp)

2. On a Windows computer in the LAN, open "This PC", click the "..." in the top right, and select "Map Network Drive".

![](https://file-us.ugreennas.com/admin/article/2025-08-26/acf3382618c44d30aa43e42b0d52c306.webp)

3. In the Folder box, enter \\<NAS Thunderbolt IP> (e.g., \\169.254.12.125) and click "Browse".

![](https://file-us.ugreennas.com/admin/article/2025-08-26/78d86200caaa40cf992460b52c12b6a3.webp)

4. Double-click the NAS Thunderbolt IP that appears and enter the NAS username and password for authentication.

5. Once connected, select the NAS shared folder and mount it to the local computer. You can now transfer and access files at high speed through the Thunderbolt direct connection.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/374698e2c9c04db49dc420cf8709c952.webp)

##### On a Mac computer:

1. Open [Control Panel] and go to [File Service] > [SMB]. Check the "Enable SMB service" option. If this service is already enabled, skip this step.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/4af4d67d173f46d5b1f8731f085d3723.webp)

2. On the Mac, click [Finder] >[Go] > [Connect to Server].

![](https://file-us.ugreennas.com/admin/article/2025-08-26/c7851be33e3540689b08d91118cd8929.webp)

3. Enter the NAS Thunderbolt IP address (e.g., smb://169.254.4.109).

![](https://file-us.ugreennas.com/admin/article/2025-08-26/aafd8157a801414aa017166b97ce5c71.webp)

4. Enter the NAS username and password to connect.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/bf2e1b0efbaf42b29646dcad7fe051eb.webp)

5. Select the folder you want to access. Once connected, you can upload and download files at high speed via the Thunderbolt direct connection.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/6f9a4b2a81c1487f8f16400fa291180a.webp)

![](https://file-us.ugreennas.com/admin/article/2025-08-26/14396ba926a34a529d223bda9e2d9916.webp)

**Method 4: Connect to UGREEN NAS for File Access via Mac's Bonjour Service**

1. Open [Control Panel], go to [Files Service] > [Advanced settings], and check the "Enable Bonjour Service" option. If this service is already enabled, skip this step.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/0f6d050ac0204eed83e18e279e585c36.webp)

2. On the Mac desktop, click [Finder] > [Go]> [Network].

3. Select the Thunderbolt IP address of the connected NAS, and click the folder you want to access.

4. You can now perform high-speed file transfers and access via the Thunderbolt direct connection.

**Note:** Transfer speeds may vary between Windows and Mac systems. Typically, Mac systems achieve faster transfer speeds when using Thunderbolt direct connection compared to Windows systems.

## Related Links

[UGREEN NAS Thunderbolt Direct-Attach Usage Guide](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTkyOCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiZW4tVVMiLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo2MDksImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)

[How to set up Thunderbolt direct connection between UGREEN NAS and computer for high-speed file transfer?](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTkyNiwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiZW4tVVMiLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo2MDcsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)
