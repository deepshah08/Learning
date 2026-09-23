# Mounting UGREEN NAS iSCSI Virtual Disk on Windows

> **Article ID**: `726`  
> **Category**: `Application Guide > SAN Manager > FAQ > Mounting UGREEN NAS iSCSI Virtual Disk on Windows`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/726  

---

> Content and Image Example Based on UGOS Pro Firmware Version 1.6.1.2846, SAN Manager Application Version 1.0.0.0046.Due to potential differences in the interface or functionality between firmware versions, please refer to the actual display on your device.

This article uses Windows 11 as an example to demonstrate how to map a LUN on a UGREEN NAS as a local disk using the iSCSI protocol.If you are using a different version of Windows, it is recommended to refer to the "[official Microsoft documentation](https://learn.microsoft.com/en-us/) " for detailed instructions.

# NAS-Side Configuration (UGOS Pro System)

1. Log in to the NAS, go to the "App Center", search for and install the "SAN Manager"application.

2. Open "SAN Manager", click [LUN] > [Add] to launch the LUN creation wizard and create a **virtual disk (LUN)**.

|  |  |
| --- | --- |
| **Parameter Name** | **Value** |
| LUN Name | You can use the default |
| Description | For example: “Game Disk” |
| Type | Recommended: Thick LUN |
| Location | Preferably use an SSD-based storage pool |
| Capacity | For example: 200GB |

3. Click "OK"and wait for the LUN to be created.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/22d2cec778874fc9b81f5a20d58d7ab0.webp)

4. Click [Target] > [Add], and in the wizard, select the LUN you just created.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/e2386fa1f47a40bf80702d32d96f3c32.webp)

5. Set an easily recognizable IQN (e.g., “**Game**”), then click "OK".

![](https://file-us.ugreennas.com/admin/article/2025-07-03/a96c1ed76c454364ae63dcaaf182b0ac.webp)

## Enable CHAP Authentication (Optional)

**CHAP** is an authentication mechanism designed to enhance the security of iSCSI connections. It verifies the identity between the client and NAS using a username and password, preventing unauthorized devices from connecting to the iSCSI Target.  
For added security, you can also enable **Mutual CHAP Authentication**, allowing the client and NAS to authenticate each other.

**Steps:**

1. Open SAN Manager, click "Settings", and locate the **Default iSCSI CHAP** settings on the right side.

2. Enable **CHAP Authentication**, then set the Username and Password.

3. (Optional) Enable **Mutual CHAP Authentication** by setting a second pair of username and password (note: the second password must be different from the first one).

4. Click "Save" to save the configuration.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/095df1d73719416c92d7b5bb325a281c.webp)

5. Go back to the [Target] page, select your desired Target, and click "Edit".

![](https://file-us.ugreennas.com/admin/article/2025-07-03/3ab45df6c79e4abab8d76d276a481916.webp)

6. Check "Enable CHAP Authentication". The system will use the default CHAP credentials you just set.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/04a51b60787944be89ddde50f069fc65.webp)

7. Click "OK" to complete the setup.

> Once CHAP is enabled, the client will be prompted with a login window when connecting to the iSCSI Target. The correct username and password must be entered to establish the connection.

For detailed instructions on configuring authentication during iSCSI mounting, please refer to the following sections:

* **"Steps to Enable CHAP (NAS validates client only)"**: This section explains how to configure one-way CHAP authentication where NAS validates the client identity.
* **"Steps to Enable Mutual CHAP (mutual authentication between NAS and client)"**: This section explains how to configure mutual CHAP authentication, where both NAS and the client validate each other’s identities.

Please choose the corresponding section based on your specific requirements for configuration.

# Windows-Side iSCSI Mounting Configuration (Example: Windows 11)

1. Press **WIN + R**, enter **iscsicpl**, and click "OK**"**.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/ed947914491a463e8267b7b25f27ba28.webp)

2. If this is the first time running the iSCSI Initiator, a permission confirmation window will appear. Click "Yes".

![](https://file-us.ugreennas.com/admin/article/2025-07-03/93a33212cb754fe69e5fe6e6f01ba4b5.webp)

3. Go to the "Discovery" tab and click "Discover Portal".

![](https://file-us.ugreennas.com/admin/article/2025-07-03/d06ab7fac1b94c3187fcfb39e4527c56.webp)

4. Enter the NAS IP address and click "OK".

> Make sure the iSCSI service port on NAS (default: **3260**) matches the one configured in [**SAN Manager] > [Settings] > [iSCSI Service Port]**.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/a5666d4d35d64f1d9a11fdaea6b78c5a.webp)

5. Switch to the "Targets" tab, find the discovered Target, and click "Connect".

![](https://file-us.ugreennas.com/admin/article/2025-07-03/3a233d0ea0304ccc94f8adf6d15751a5.webp)

6. A pop-up window will appear, click "OK"

![](https://file-us.ugreennas.com/admin/article/2025-07-03/f1014ed6e7134631882d0da67574cc77.webp)

7. If the Target status shows Connected, the iSCSI virtual disk has been successfully connected.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/518098342083450489aa8c7b3fd680c0.webp)

8. Press **WIN + R**, type **diskmgmt.msc**, and click "OK" to **open the Disk Management tool**.

9. The system will prompt you to initialize the new disk. Click "OK".

![](https://file-us.ugreennas.com/admin/article/2025-07-03/9a674ffbe1ea4d0a835a90fb50caba92.webp)

10. Right-click on the unallocated space of the new disk and choose "New Simple Volume".

![](https://file-us.ugreennas.com/admin/article/2025-07-03/af6d6f091c3746f580f745d47cc00e4a.webp)

11. Follow the wizard until completion. Wait for formatting to finish.

12. After formatting, Windows will automatically assign a drive letter, and you can now use this NAS virtual disk like a local hard drive.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/858b7f619bc247a980fcf86c7b4d0408.webp)

## Configure CHAP or Mutual CHAP Authentication (If Enabled)

### **Enable CHAP Only (NAS authenticates the client):**

1. Go to the [Targets] tab, select the target IQN, then click [Connect] > [Advanced].

![](https://file-us.ugreennas.com/admin/article/2025-07-03/6936708b82504ab2a306c90b3b63a861.webp)

2. Check “Enable CHAP log on”, then enter the Name and Target Secret (the username and password set in CHAP on the NAS).

![](https://file-us.ugreennas.com/admin/article/2025-07-03/4be7f8dd9e394ebf8f23d9d778a8a37b.webp)

3. Click "OK" to complete the connection.

### **Enable Mutual CHAP (NAS and client authenticate each other):**

1. Switch to the [Configuration] tab and click the "CHAP" button.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/dfc80f6b2c67452499e91401fcbc24da.webp)

2. In the pop-up window, enter the **Mutual CHAP Secret** as configured on the NAS, then click "OK".

![](https://file-us.ugreennas.com/admin/article/2025-07-03/101e5ebe157e45bebb7c4da006ff9a58.webp)

3. Reconnect to the target IQN and click [Advanced], then complete the following settings:

○ Check "Enable CHAP log on";

○ Enter the CHAP Name and CHAP Secret (used for client authentication);

○ Check "Perform mutual authentication".

![](https://file-us.ugreennas.com/admin/article/2025-07-03/93b1e0bbd825480da8c508757f99ef31.webp)

4. Click "OK" to complete authentication and establish the connection.

## Usage Tips

If the Target is not discovered or the connection fails, make sure the following conditions are met:

● The NAS and Windows devices are in the same local network.

● iSCSI service is running normally on the NAS.

● Windows firewall is not blocking the iSCSI service.
