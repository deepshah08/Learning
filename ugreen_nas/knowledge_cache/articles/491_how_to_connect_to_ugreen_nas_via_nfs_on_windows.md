# How to Connect to UGREEN NAS via NFS on Windows

> **Article ID**: `491`  
> **Category**: `Application Guide > Control Panel > File Service > How to Connect to UGREEN NAS via NFS on Windows`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/491  

---

NFS (Network File System) is an efficient network file-sharing protocol widely used for file sharing, data backup and recovery, as well as multimedia storage and access. UGOS Pro offers convenient, secure, and high-performance NFS services, with flexible configuration options to meet diverse user needs. This guide provides detailed instructions on how to enable the NFS service, configure shared folder permissions, and connect to and access files on UGREEN NAS via NFS on Windows systems.

## How to Enable NFS Service on UGOS Pro?

1. Log in to the UGOS Pro system and go to [Control Panel] > [File Service] > [NFS].。

2. Check the box to enable the NFS service, then click Apply to activate the settings.

3. In the Advanced Settings, you can select the maximum NFS protocol version and configure specific ports to optimize performance and compatibility. For more details, please refer to the [NFS Application Guide](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjo4NiwiYXJ0aWNsZUluZm9JZCI6ODAsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiMS4wIiwicGF0aENvZGUiOiJwcm8wMDEsdXJjYWJpLG5hZmh2MCw2NXc2ZmEifQ%3D%3D) .

![](https://file-us.ugreennas.com/admin/article/2025-08-28/d90d12bc3be04e77b1beabcac14ce0d6.webp)

## How to Configure NFS Permissions for Shared Folders?

1. Log in to the UGOS Pro system and go to [Files] > [Shared Folder].

2. Select the folder you wish to share, right-click and choose "Properties" > "NFS Permissions", then click Add to configure the NFS rules.

![](https://file-us.ugreennas.com/admin/article/2025-08-28/592e8b2c97494d00abe1b0a52fa821da.webp)

3. Fill in the following information in the [Add NFS Rules] window:

● **Server Address:** Enter the IP address of the client (Windows computer) that will mount the NFS protocol.

● **Permissions:** Select "Read&Write".

● **Squash:** Choose "All users mapped as admin"to ensure consistent permissions.

● **Security:** Choose "AUTH\_SYS".

● **Start Async:** Keep the default setting (recommended to enable for improved performance).

● **Allow connections from unprivileged ports(ports greater than 1024)**: Keep the default setting.

4. Click "OK" to apply the NFS rule after completing the configuration . For more details, please refer to: [How to Specify NFS Permissions for Shared Folders](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxNzcsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDEsbmo0cHQ3LDZmMDFtZiJ9) ?

![](https://file-us.ugreennas.com/admin/article/2025-08-28/6edb01f486d84610b17cb3465fb54469.webp)

## How to Connect to UGREEN NAS via NFS on Windows?

**Prerequisites**

● Ensure that your Windows version supports the NFS client feature (Windows 10 Professional or above).

● Ensure that NFS service is enabled on UGOS Pro, and the permissions for the shared folders are correctly configured.

**Enabling NFS Client**

1. Press`Win + R` to open the Run dialog, type `control`, and press Enter to open the "Control Panel".

2. Select [Programs] > [Programs and Features] in the "Control Panel".

3. Click on "Turn Windows features on or off" on the left-hand side.

4. Find and check the boxes for Service for NFS, Client for NFS, and Administrative Tools in the pop-up window, then click "OK" to complete the feature activation .

![](https://file-us.ugreennas.com/admin/article/2025-08-28/adf1986317bc46fd9c45ae22e79f3fed.webp)

### Connecting to NFS Shared Folder

##### Method 1: Connecting via Graphical Interface

1. Open "File Explorer" (`Win + E`), right-click on "This PC", and select "Map Network Drive".

2. In the pop-up window:

● Choose an unused drive letter (e.g., Y:).

● Enter the shared folder path (e.g.,`\\192.168.22.141\volume1\video`).

● Check "Reconnect at sign-in" to automatically reconnect on system startup.

3. Click "Finish". Once connected successfully, the shared folder will appear under "This PC".

![](https://file-us.ugreennas.com/admin/article/2025-08-28/c053154bc323483a902e67517acb11b9.webp)

##### Method 2: Connecting via Command Line

1. Press `Win + R`, type `cmd`to open the Command Prompt, and press "Enter".

2. In the Command Prompt, enter the following command to create a mount point (e.g., `Y:`):

```
mount -o anon \<NAS_IP address><Shared Cataloge> <Drive Letter>:
EX：
mount -o anon \192.168.22.141volume1video Y:
```

3. After successfully mounting, you can access the shared folder through the mount point (e.g., `Y:`) in File Explorer.

![](https://file-us.ugreennas.com/admin/article/2025-08-28/1d62940e390e495f922030e84ef105ff.webp)

## Common Issues

**1. Mounting Failure or Permission Error:**

● Ensure that the NFS service and shared directory permissions are configured correctly.

● Ensure that the IP address of the computer attempting to mount the NFS share is included in the NFS rule permissions for the shared directory.

● Verify that the Squash setting is set to "All users mapped as admin".

2. **Network Connection Error:**

● Check whether the network connection is functioning properly and confirm that the Windows computer and the NAS device are on the same network. Please refer to "[How to Confirm if Your Computer and NAS Are on the Same Local Area Network.](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMTIxLCJhcnRpY2xlSW5mb0lkIjozODgsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D) "

3. **Firewall Configuration:**

● Ensure that the firewall is not blocking the NFS port (default is`2049`).

4. **Mangled Display of Mounted NFS Shared Folder Names:**

● Go to the Windows computer's [Control Panel] > [Clock and Region] > [Region settings], and enable "Use Unicode UTF-8 for worldwide language support."

![](https://file-us.ugreennas.com/admin/article/2025-08-28/047799ddc14c4bb996c1f75578ed25ea.webp)
