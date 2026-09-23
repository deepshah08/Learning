# iSCSI Cluster and Read-Only Permission Settings Explanation

> **Article ID**: `722`  
> **Category**: `Application Guide > SAN Manager > FAQ > iSCSI Cluster and Read-Only Permission Settings Explanation`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/722  

---

iSCSI Cluster and Read-Only Permission Settings explains When users enable the **iSCSI Cluster** feature in the **Target** section of SAN Manager, it is **essential to perform the following permission configurations** to ensure system stability and data consistency.

## Steps

**Step 1: Create Group Client Group**

1. Open "SAN Manager" and navigate to the "Group" page.

2. Click the "Add" button to enter the Group creation page.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/b9d99fb73ae5444ba7a04c380db33a39.webp)

3. **Fill in the client IQN**, which needs to be obtained from the client device’s iSCSI initiator. For example, on a **Windows** system, press Win+R to open the Run dialog, type iscsicpl, and click "OK" to open the iSCSI initiator.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/8caf881a5cac41279dcbe97cae38ad8c.webp)

4. In the **iSCSI initiator**, click the "**Configure**" button, copy the initiator name (client IQN), and use it later in **SAN Manager**.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/77baa70e03344d2898a4c69554dc5f85.webp)

5. If the IQN name contains Chinese characters, click "**Change**" to modify them to English characters, ensuring the IQN meets the standard format.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/4423d0845cd242e1bb20b7f0fa8bcce0.webp)

6. Return to the **SAN Manager** **Group creation page**, paste the client IQN, and click "**OK**" to complete the Group client group creation.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/043f194ad658497ebaf952a506ae4a16.webp)

**Step 2: Configure LUN Permissions**

1. After creating the Group, navigate to the **LUN** page, locate the target LUN, and click the "**Edit**" button.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/11756a081e4644ebbad5565954a3629f.webp)

2. In the pop-up "**Edit LUN**" window, switch to the "**Permissions**" tab.

3. Set the permission mode to "**Custom**".

4. Click the "**Add**" button and select the previously created **Group client group**.

5. In the **Permission** column, set the Group’s permission to "**Read-Only**".

6. Click "**OK**" to save all settings and complete the permission configuration.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/ea0718b8dd3a41fc98dfdda15875bd6b.webp)

## Why Must LUNs Be Set to Read-Only?

iSCSI is a **block-level storage protocol**, where each LUN functions as a virtual hard drive. iSCSI is generally designed for **exclusive read/write access by a single client**. If multiple clients connect to and write to the same LUN simultaneously without coordination, it may result in the following issues:

|  |  |
| --- | --- |
| Risk Type | Description |
| Data Corruption | Concurrent writes from multiple clients can disrupt the file system structure. |
| File System Crash | Undetected write conflicts may damage partitions or metadata. |
| Data Inconsistency | Write order and synchronization cannot be guaranteed, leading to read errors. |

By enabling iSCSI Cluster Mode and setting the LUN to **Read-Only**, you can **safely allow multiple clients to access the LUN concurrently without these risks**. This configuration is suitable for scenarios like mounting ISO images or accessing archived data in a read-only fashion.

## Recommended Setup for Home Users / Multi-Device Access

For non-enterprise users who want multiple devices to access shared data, we recommend using protocols designed for concurrent access:

|  |  |
| --- | --- |
| Protocol | Advantages |
| **SMB (Recommended)** | Supports multi-user concurrent read/write access, file-level sharing, and flexible permission control. |
| WebDAV | Cross-platform compatibility; ideal for remote work and lightweight access. |
| Rsync / FTP | Better suited for scheduled backups or file transfers. |
