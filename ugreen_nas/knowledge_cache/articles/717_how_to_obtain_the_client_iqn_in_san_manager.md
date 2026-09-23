# How to Obtain the Client IQN in SAN Manager

> **Article ID**: `717`  
> **Category**: `Application Guide > SAN Manager > FAQ > How to Obtain the Client IQN in SAN Manager`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/717  

---

When configuring a **Group (Client Group)**, you need to enter the **Client IQN**, which is the unique identifier used by the client device's iSCSI initiator to establish a connection with the Target (on the NAS). The **Client IQN** **is different from the Target IQN**, and must be entered correctly to ensure that the permission settings take effect properly.

## How to obtain the Client IQN (using Windows as an example):

1. Press Win+R to open the Run dialog, type iscsicpl, and click "OK" to open the iSCSI initiator.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/799056feb09c4ef39c7048c240913f72.webp)

2. In the **iSCSI initiator**, click the "**Configure**" button, copy the initiator name (client IQN), and use it later in **SAN Manager**.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/6d27764d1bda44de8f4a80d750f9c2ed.webp)

3. If the IQN name contains Chinese characters, click "**Change**" to modify them to English characters, ensuring the IQN meets the standard format.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/bdff2bdef4f74f2aacaf9a84b911c9f6.webp)

4. Return to the **SAN Manager** **Group creation page**, paste the client IQN, and click "**OK**" to complete the Group client group creation.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/0fc4aa14aee54dbcb457a2a1954b7120.webp)

## How to obtain the Client IQN (using macOS as an example）

● macOS **does not have a built-in iSCSI initiator**, so third-party software is required to connect iSCSI devices.

● Using **DAEMON Tools** as an Example:After configuring the iSCSI connection in the software, you can obtain the client IQN.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/000b819545a645df998b381f99410bc3.webp)

## Configure LUN Permissions

1. After creating the Group, navigate to the **LUN** page, locate the target LUN, and click the "**Edit**" button.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/94f7c9f1ca4f4319a3809db4034ae708.webp)

2. In the pop-up "**Edit LUN**" window, switch to the "**Permissions**" tab.

3. Set the permission mode to "**Custom**".

4. Click the "**Add**" button and select the previously created **Group client group**.

5. In the **Permission** column, set the Group’s permission to "**Read-Only**".

6. Click "**OK**" to save all settings and complete the permission configuration.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/695056dbe98b4e67a47d551bdcaaf9d9.webp)

## Common Issue

### Why does the permission not take effect when the client IQN doesn't match the iSCSI IQN of the client device?

**Issue Description:**If the client IQN does not match the actual iSCSI IQN of the client device, the system will be unable to correctly associate the client with the Group permissions. As a result, the configured permissions will not take effect.

**Solution:**Ensure that the **client IQN** exactly matches the **iSCSI IQN of the client device**. Only when the IQNs match correctly will the permission settings be properly applied.
