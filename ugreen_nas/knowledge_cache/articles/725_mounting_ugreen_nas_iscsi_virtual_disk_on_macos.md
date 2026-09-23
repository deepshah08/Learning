# Mounting UGREEN NAS iSCSI Virtual Disk on macOS

> **Article ID**: `725`  
> **Category**: `Application Guide > SAN Manager > FAQ > Mounting UGREEN NAS iSCSI Virtual Disk on macOS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/725  

---

> **Applicable Note:** This article applies to UGOS Pro firmware version 1.6.1.2846 and SAN Manager app version 1.0.0.0046. The screenshots provided are for reference only; the actual interface may vary slightly depending on the system or app version. Some options and features may differ between versions. Please refer to the actual interface or consult the latest help documentation.

Unlike Windows, macOS **does not come with a built-in iSCSI initiator**. Therefore, third-party software is required to connect to iSCSI devices. The following example uses DAEMON Tools to demonstrate the process of mounting an iSCSI LUN provided by UGREEN NAS on macOS.

# **NAS-Side Configuration (UGOS Pro System)**

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

![](https://file-us.ugreennas.com/admin/article/2025-07-03/db4b8e550447473f971361211ef0a186.webp)

4. Click [Target] > [Add], and in the wizard, select the LUN you just created.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/525fd538abd04d9cbb8348702a59e281.webp)

5. Set an easily recognizable IQN (e.g., “**Game**”), then click "OK".

![](https://file-us.ugreennas.com/admin/article/2025-07-03/d600b2042ecd45c3be2314bcded3b35e.webp)

## **Enable CHAP Authentication (Optional)**

**CHAP** is an authentication mechanism designed to enhance the security of iSCSI connections. It verifies the identity between the client and NAS using a username and password, preventing unauthorized devices from connecting to the iSCSI Target.  
For added security, you can also enable **Mutual CHAP Authentication**, allowing the client and NAS to authenticate each other.

**Steps:**

1. Open SAN Manager, click "Settings", and locate the **Default iSCSI CHAP** settings on the right side.

2. Enable **CHAP Authentication**, then set the Username and Password.

3. (Optional) Enable **Mutual CHAP Authentication** by setting a second pair of username and password (note: the second password must be different from the first one).

4. Click "Save" to save the configuration.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/355a5f48ce6347e380cccf979936fead.webp)

5. Go back to the [Target] page, select your desired Target, and click "Edit".

![](https://file-us.ugreennas.com/admin/article/2025-07-03/c9b6ffaa4bf6448bb38562b977169bd1.webp)

6. Check "Enable CHAP Authentication". By default, the CHAP information you just configured will be used. If different credentials are required, you can select “Custom” to set them separately.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/e7cf3fe2acb7406faa4d5c27aef25fa2.webp)

7. Click "OK" to complete the setup.

> Once CHAP is enabled, the client will be prompted with a login window when connecting to the iSCSI Target. The correct username and password must be entered to establish the connection.

# **iSCSI Mount Configuration on macOS**

1. Download and install **DAEMON Tools for Mac** (prefer the latest version).

2. Launch DAEMON Tools and go to the main interface.

3. **Right-click** on the blank area in the main window and choose "Add".

![](https://file-us.ugreennas.com/admin/article/2025-07-03/71a4d9c7cf224ac69d0f3b60ce13bb73.webp)

4. In the pop-up window, enter the **IP address** of the UGREEN NAS and click [Add].

![](https://file-us.ugreennas.com/admin/article/2025-07-03/0450df8a61fa4ea383d7da1567da3fba.webp)

5. Once added, the available Targets list will display.

6. Select the desired Target (IQN name), right-click on it, and choose "Connect".

![](https://file-us.ugreennas.com/admin/article/2025-07-03/fb57c879c40140008348d4d61cf5b2e9.webp)

7. If the Target status shows Connected, the iSCSI virtual disk is successfully connected.

8. The system will automatically mount the iSCSI LUN after a few seconds.

9. The mounted disk will appear on the desktop and Finder sidebar, acting as a local disk.

10. You can perform normal operations like reading, writing, formatting, and partitioning.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/46c6d23d80ec4c81916387437cd92fa6.webp)

**Notes:** When connecting a new disk for the first time, you may need to initialize it using Disk Utility—for example, by formatting it to APFS or exFAT file system.

## Configure CHAP or Mutual CHAP Authentication (If Enabled)

1. If **CHAP** and **Mutual CHAP** authentication are enabled, a **"Target Authentication"** window will pop up when connecting to the Target.

2. Enter the **Username** and **Password** (the CHAP name and secret set on the NAS).

3. If **Mutual CHAP** is also enabled, check the corresponding option and enter the **Target's Username and Password**.

4. Click "OK" to complete the connection.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/60ca8df45add49ab8630b4c43b435e46.webp)
