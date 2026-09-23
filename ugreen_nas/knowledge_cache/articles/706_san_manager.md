# SAN Manager

> **Article ID**: `706`  
> **Category**: `Application Guide > SAN Manager > SAN Manager`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/706  

---

**Applicable Version**: UGOS Pro 1.11.0.0002 and above.

The interface screenshots and optionsshown in this documentare for reference only. Actual display may vary depending on system version, application version, or device model. Please refer to the actual interface.

# Application Overview

The " **SAN Manager" application** delivers powerful iSCSI service capabilities, enabling the virtualization of NAS storage space into " **virtual disks**. **"** These disks can be recognized by computers over IP networks as local hard drives, facilitating efficient and flexible remote storage access.

## What is iSCSI?

Think of iSCSI as a **"virtual hard drive mapping** " technology. Once connected via iSCSI, the space on your NAS appears on your computer like a newly inserted physical hard drive, supporting formatting, partitioning, software installation, and data storage.

### Core Concepts

When using SAN Manager, you need to understand these three core terms:

● **LUN (Logical Unit)**: Equivalent to **the** "virtual hard drive" **itself**. You can configure its size, storage location, and type.

● **Target: The** " **entry point** " or " **access channel"** for clients to connect to LUNs. Each Target has a unique **IQN** (Identifier) and supports CHAP authentication configuration.

● **Group:** A collection for batch managing permissions. Multiple clients can be grouped together to grant unified access to specific LUNs.

## Quick Start: Creating and Connecting

## Preparation Before Use

Before beginning, ensure:

● The NAS has created available storage spaces.

● Your computer and NAS are on the same LAN or have network connectivity.

● You have obtained the NAS's IP address ( **viewable** in the PC client's " **Control Panel"** > " **Network Settings"** > "Network Connections **"** ).

## Step 1: Create a Virtual Disk (LUN)

1. Open **the "SAN Manager" application**, navigate to **the "LUN" page**, and click " **Add"**.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/c9b1e391-e44a-4b0f-9e03-71c43e457c65.png)

2. Configure parameters:

● **Name**: Customize (e.g., Game Drive).

● **Type**: Recommended to select Thick LUN (more stable performance).

● **Location**: Select SSD-based storage for optimal performance.

● **Capacity**: Set as needed (e.g., 200GB).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/95e7c41e-c4e2-4940-9bc2-44f80f45507d.png)

3. Click " **OK** " to complete creation.

## Step 2: Create a Target

1. Navigate to **the "Target" page** and click " **Add"**.

2. Select the LUN created earlier and click " **Next**."

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/a3163f44-58a7-4dc3-aa5f-4d835089d6de.png)

3. For IQN, it is recommended to use the system-generated default prefix and add an identifier (e.g. , target-Game) to the suffix for easy identification. Click " **OK"** to complete creation.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/0a81ff19-556d-4ec1-89b8-d1602fb3cbee.png)

**Note**: The default IQN prefix provided complies with iSCSI standards for better compatibility.

## Step 3: Client Mounting (Windows/macOS)

### Windows Client (using Windows 11 as an example)

1. Press Win + R, type ` iscsicpl `, and press Enter.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/72413b28-cc21-4be9-af61-d93f72095a26.png)

2. On first run, click " **Yes** " to start the service.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/82af82c0-c36a-4d02-a97f-9157df8d11ad.png)

3. Switch to **the** " **Discovery** " tab and click " **Discover Portal"**.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/64cdb837-d3c9-4005-8816-cdac7ad2958c.png)

4. Enter the NAS IP address, keep the default port 3260, and click " **OK"**.

> The port number used for the iSCSI connection must match the port configured in the SAN Manager application under "Settings" > "iSCSI" > "Server Ports" (default port is 3260).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/3fe92dba-5435-4c07-b916-9961f9db0f23.png)

5. Switch to **the "Targets" tab**, locate the target, select it, and click " **Connect"**.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/046d0ea0-8b3d-4d25-9f22-8a6467326d1c.png)

6. Click " **OK"** in the pop-up window.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/cc209b5a-4d3a-40a2-a5f6-2594519754b2.png)

7. The status changes to " **Connected**," indicating success.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/6736adbe-78f2-45db-a1e9-4d7eb1cab919.png)

**Initializing disks**:

1. Press Win + R, type diskmgmt.msc to open Disk Management.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/b88dffd8-cd29-4817-8da3-c7a530cb4078.png)

2. The system will prompt you to initialize the new disk (choose GPT or MBR). Right-click the " **Unallocated** " space and select " **New Simple Volume**." Format it to use.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/8d054add-cb62-43ff-aa04-78c9071fd449.png)

### macOS Client

macOS does not include an iSCSI initiator by default; third-party software (such as DAEMON Tools) is required.

1. Install and launch **DAEMON Tools for Mac**. Right-click " **Add"** on the main interface.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/3565a680-13f7-4a0c-9b04-429170dd8d1e.png)

2. Enter the IP address and port (3260) of the U-NEXT NAS, then click " **Add"**.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/38ce82ba-f4d6-407a-a1bd-76301a0a5fea.png)

3. Locate the corresponding Target in the list, right-click and select " **Connect"**.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/d11f1f57-8b96-487b-bd28-f2b237cbae85.png)

4. After successful connection, the disk will appear on your desktop or in Finder. Initial use requires formatting via macOS **Disk Utility** (format as APFS or exFAT).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/909e6a1b-3fa2-4ea4-8908-429ec2ba5eaf.png)

# Feature Details and Management

## LUN Management

On the " **LUN** " page, you can view status, capacity, and perform editing.

**LUN Type Comparison**:

● **Thick LUN**: Offers higher performance with pre-allocated space (physical capacity occupied immediately upon creation).

● **Thin LUNs** allocate space on demand (physical capacity occupied only when data is written ) , offering higher space utilization but requiring storage pool capacity monitoring, with slightly lower performance.

**Advanced Editing**:

Click " **Edit** " on an existing LUN to configure its permissions.

On the edit page, enable " **Advanced SCSI Command Support"** (FUA and Sync Cache) to ensure real-time data persistence and consistency, though this may impact performance.

On **the "Permissions"** tab, you can flexibly manage access rights for this LUN. **The following permission modes are supported:**

● **Allow all clients to read/write** (default): All clients connected to this Target can perform read/write operations on the LUN;

● **Custom**: Enables control over which client groups (Group) can access this LUN and their specific permissions.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/cb360f5a-5701-46e1-abf5-85d0533a386c.png)

## Target Management

The Target serves as the bridge connecting clients to LUNs. You can use the editing function to configure detailed settings for the iSCSI target's authentication methods, data integrity, and connection policies.

**Accessing the Edit Page**:

Select the target to configure from the Target list, then click the " **Edit** " button to enter the Target editing page.

**CHAP Authentication:**

CHAP enhances connection security. When enabled, clients attempting to connect to the NAS will be prompted to provide credentials for verification.

1. **Select Authentication Mode**:

● **Use Default iSCSI CHAP**: The system will use the CHAP authentication name and password you preset on **the** " **Settings** " page for verification.

● **Use Custom CHAP**: You can set a specific name (username) and password (password) for this Target.

2. **Mutual CHAP**:

● Enabling this activates a two-way authentication mechanism. Not only does the NAS verify the client, but the client also verifies the NAS identity, providing enhanced security.

**Note:**

● For enterprise or complex networks, enabling CHAP or Mutual CHAP is recommended to prevent unauthorized access.

● If your network environment is secure, you may choose not to enable it to simplify the connection process.

**CRC Checksum****:**

You can enable CRC verification to prevent data tampering or corruption during transmission. Note that enabling this feature increases CPU and network bandwidth usage.

● **Enable Header Digest**: The system will perform CRC checks on the header information of the iSCSI protocol.

● **Enable Data Digest**: The system will perform CRC checks on the data payload transmitted via iSCSI.

**iSCSI Connection Policies:**

● **iSCSI Cluster**: This feature allows multiple clients to connect to the same Target simultaneously.

**Note**: After enabling this feature, ensure the corresponding LUN permissions are set to " **Read-Only**." Simultaneous write operations to the same LUN from multiple devices can easily cause data corruption or file system crashes.

## Group (Client Group) Management

Groups are used for batch permission management, particularly when restricting certain clients to " **read-only** " access.

### How to create a Group and obtain client IQNs?

1. Using Windows as an example: Press**Win+R** to open the Run dialog , type `` `iscsicpl ``` and press Enter to launch the iSCSI Initiator.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/868f6548-55f2-47a0-a693-84634802c8a0.png)

2. Click " **Configure**," then copy **the** " **Initiator Name** " (this is the client IQN). Since the name cannot contain Chinese characters, click " **Change** " to modify it to English.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/eccd9c06-5b36-4951-89f4-a48ae1584f61.png)

3. In the " **SAN Manager** " application, click " **Group** " > " **New**," paste the IQN, and save.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/4edc830c-fb02-4028-b242-94cfabb4d956.png)

### Set "Read-Only" Permissions (to prevent data conflicts)

When multiple clients connect to the same LUN (iSCSI cluster), read-only permissions must be set.

1. Navigate to **the "LUN" page**, edit the target LUN, and switch to **the "Permissions" tab**.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/6798761b-c15d-40d4-9ccf-f958a1bc94ea.png)

2. Select " **Custom**," add the created Group, and set permissions to **Read-Only**.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/686dcace-20a2-41da-ae72-e6f6e5212d00.png)

**Note**: After modifying permissions, clients must disconnect and reconnect for changes to take effect.

## Configuration

Configure system parameters on the " **Settings** " page:

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251217/5be34573-cd46-4037-99c5-ff411ab727bc.png)

● **iSCSI Service Port**: Default 3260. Clients must reconnect after modification.

● **Base Name**: Default IQN prefix when creating a new Target.

● **Default CHAP**: A predefined authentication set serving as the default iSCSI CHAP for quick deployment.
