# UGREEN NAS Thunderbolt Direct-Attach Usage Guide

> **Article ID**: `609`  
> **Category**: `Application Guide > Control Panel > FAQ > UGREEN NAS Thunderbolt Direct-Attach Usage Guide`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/609  

---

The Thunderbolt interface, co-developed by Intel and Apple, is a high-speed data transfer standard compatible with USB4 and USB3 devices. It not only delivers exceptional transfer speeds but also supports daisy-chaining multiple peripherals. Through Thunderbolt, users can achieve direct high-speed connections between computers and NAS devices for rapid data transfers.

Thunderbolt is renowned for its blazing-fast performance. The latest Thunderbolt 4 interface offers theoretical transfer speeds up to **40 Gbps** (Thunderbolt 4 standard), far surpassing traditional interfaces. Whether transferring large files or processing real-time workloads, Thunderbolt significantly enhances productivity.

## UGREEN NAS Thunderbolt Configuration Requirements

**1. Supported NAS Models**

The following UGREEN DXP series devices are equipped with Thunderbolt 4 ports and support Thunderbolt direct-attach functionality: DXP480T Plus, DXP6800 Pro, DXP8800 Series

**2. Cable Requirements**

**Mandatory**: Use Thunderbolt-certified cables (Thunderbolt 3/4/5) marked with the Thunderbolt symbol ⚡️.

**Avoid**: Generic USB-C cables (limited to USB protocols with ≤20 Gbps bandwidth).

**3. Host Interface Requirements**

Computer: Must have Thunderbolt 3 or newer ports (physical Type-C connector with Thunderbolt protocol support).

**Notes:**

● Although Type-C and Thunderbolt ports look identical, Thunderbolt uses a specialized communication protocol. Standard Type-C cables only support USB protocols and cannot deliver Thunderbolt’s high-speed data transfer capabilities. For optimal performance, use certified Thunderbolt cables.

● For Thunderbolt direct-attach connections, macOS is recommended due to higher transfer efficiency. Windows users must manually install drivers and address compatibility issues. Additionally, upload speeds may be slower on Windows systems.

## Thunderbolt Direct-Attach Configuration Steps

**1. Physical Connection:**

Plug one end of the Thunderbolt cable into the Thunderbolt port on the UGREEN NAS, and the other end into the Thunderbolt port on your computer (Thunderbolt ports are typically marked with the ⚡️ symbol).

![](https://file-us.ugreennas.com/admin/article/2025-08-26/e6405a03026f4be39e0c58800dc9e866.webp)

**2. Device Recognition:**

You can check the Thunderbolt connection status in either of the following ways:

**Method 1: Automatic Recognition**

After successful connection, the system will automatically assign a dedicated IP address to the Thunderbolt interface (e.g., 169.254.XX.XX).

![](https://file-us.ugreennas.com/admin/article/2025-08-26/90af78b080d441f6bee23f95f4aed3fb.webp)

● **Path to Check:** Go to [Control Panel > Network > Network Connection] and check the status of the "Thunderbolt" interface.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/c2bce5551ae54909a865504d4c75a90e.webp)

● **Edit Network Settings (IPv4/IPv6):** Click the "Edit" button. You can choose to obtain an IP address automatically (default) or manually configure an IP address and customize the MTU value.

**Method 2: Client Auto-Search (Within LAN)**

1. On the Thunderbolt-connected computer, open the UGREEN Cloud Client. On the local account login page, click "More Connections".

![](https://file-us.ugreennas.com/admin/article/2025-08-26/37618ec9c7bb421b9bd8ddc2e5db896a.webp)

2. After login, use File Management to upload/download files and test the transfer speed of the Thunderbolt direct-attach connection.

## Data Transfer Verification

You can validate the transfer speed of the Thunderbolt direct-attach connection using the following methods. This tutorial provides examples for both Windows and Mac systems.

**Method 1: File Transfer via SMB**

##### On a Windows computer:

1. Log in to your UGREEN NAS with an administrator account. Navigate to [Control Panel > File Service > SMB] and check the "Enable SMB Service" option. If this service is already enabled, skip this step.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/dfd7120c34e14cc093d5466d7ca96ef6.webp)

2. In Windows, open "This PC" and click the "Map Network Drive" button.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/a6280bba06494e1f83a46b50abb4d06c.webp)

3. In the "Folder" field, enter the \\Thunderbolt IP address of the NAS (e.g., \\169.254.12.125), then click "Browse**"** and double-click the NAS Thunderbolt IP address that appears.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/54b75c5fca5640f68db66c9bbe14dc9c.webp)

4. Enter the NAS username and password to complete authentication, then establish the connection.

5. Select the NAS shared folder and mount it to the local computer. You can test the file transfer speed of the Thunderbolt direct-attach method by uploading/downloading files.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/88742588d9fb47ad801daef21a780a1b.webp)

##### On a Mac book:

1. Log in to your UGREEN NAS with an administrator account. Navigate to [Control Panel > File Service > SMB] and check the "Enable SMB Service" option. If this service is already enabled, skip this step.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/bfd12eb8127049fdad7c01761f113a03.webp)

2. On a Mac computer, click [Finder > Go > Connect to Server].

![](https://file-us.ugreennas.com/admin/article/2025-08-26/d4477e544577438fa054f8450b9c8508.webp)

3. Enter the NAS's Thunderbolt IP address (e.g., smb://169.254.4.109).

![](https://file-us.ugreennas.com/admin/article/2025-08-26/cb1f83a742364f8595fa7a965a953276.webp)

4. Enter the NAS username and password to connect.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/75dc17c0edaa41ebbdf0a639270c835e.webp)

5. Select the folder you want to access. After successful connection, you can test the transfer speed of the Thunderbolt direct-attach method by uploading/downloading files.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/55d007bd2a3d4a018de805bca26ab158.webp)

![](https://file-us.ugreennas.com/admin/article/2025-08-26/d860c5efbf27469eb00aa9fdb3a83b82.webp)

**Note:** Transfer speeds may differ between Windows and Mac systems. Typically, macOS achieves higher transfer speeds with Thunderbolt direct-attach compared to Windows.

**Method 2: Transfer via Web Interface**

1. On your local network, enter http://NAS\_Thunderbolt\_IP:9999 in a browser (e.g., http://169.254.4.109:9999) to log into the UGREEN NAS.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/7961c1fdae03454788a9a1b3b99e1e17.webp)

![](https://file-us.ugreennas.com/admin/article/2025-08-26/8a0430b397ef4a3eb69275e80af7d90c.webp)

2. In the "Files", perform file upload/download operations to test the transfer speed of the Thunderbolt direct-attach method.
