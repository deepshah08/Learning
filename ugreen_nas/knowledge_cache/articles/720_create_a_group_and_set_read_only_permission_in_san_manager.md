# Create a Group and Set Read-Only Permission in SAN Manager

> **Article ID**: `720`  
> **Category**: `Application Guide > SAN Manager > FAQ > Create a Group and Set Read-Only Permission in SAN Manager`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/720  

---

Create a Group and Set Read-Only Permission in SAN Manager

If you wish to ensure that the disk connected to the LUN can **only be read and not written to or modified**, you can achieve this by setting the LUN permissions to "read-only".

> After creating a Group client group in the SAN Manager, add the group to the LUN permission settings and set its access to "read-only." Once configured, clients in the Group will only have read access and will not be able to write, delete, or modify data.

## Applicable Scenario

This operation is also applicable when the **iSCSI cluster function** is enabled.

When multiple clients connect to the same LUN and simultaneously have read/write permissions, **data write conflicts are highly likely**, which could lead to data corruption, file system crashes, and risks to NAS data consistency.

To avoid such issues, it is recommended to set "read-only permissions" for all clients sharing the LUN, **ensuring data integrity and stability**.

## Steps

**Step 1: Create Group Client Group**

1. Open "SAN Manager" and navigate to the "Group" page.

2. Click the "Add" button to enter the Group creation page.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/2258afd52ecc40609431dab4ddd4003f.webp)

3. **Fill in the client IQN**, which needs to be obtained from the client device’s iSCSI initiator. For example, on a **Windows** system, press Win+R to open the Run dialog, type iscsicpl, and click "OK" to open the iSCSI initiator.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/b9a250ba9c80458d8bd4c76d4e686dd9.webp)

4. In the **iSCSI initiator**, click the "**Configure**" button, copy the initiator name (client IQN), and use it later in **SAN Manager**.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/7caeb8ad06bb4ad8b32ad890daeb1560.webp)

5. If the IQN name contains Chinese characters, click "**Change**" to modify them to English characters, ensuring the IQN meets the standard format.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/b6d5b1a46cbb4784b2031784ee1d5b41.webp)

6. Return to the **SAN Manager** **Group creation page**, paste the client IQN, and click "**OK**" to complete the Group client group creation.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/eff2f0044fa14720942e2effa0036214.webp)

**Step 2: Configure LUN Permissions**

1. After creating the Group, navigate to the **LUN** page, locate the target LUN, and click the "**Edit**" button.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/c9d9f954cf994ddda5363e18a9c7e3fc.webp)

2. In the pop-up "**Edit LUN**" window, switch to the "**Permissions**" tab.

3. Set the permission mode to "**Custom**".

4. Click the "**Add**" button and select the previously created **Group client group**.

5. In the **Permission** column, set the Group’s permission to "**Read-Only**".

6. Click "**OK**" to save all settings and complete the permission configuration.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/91a9e5621bd7421194f97e59a2e67dab.webp)

## Setting Access Denial Permissions

If the permission mode is set to "Custom" but no Groups are added, the system will default to **denying access** to the LUN for all clients.

## Notes

● The Group must be created in advance on the [Group] page and include the correct client IQNs.

● Read-only permission is suitable for scenarios where multiple clients need to access the same LUN but should not modify data.

● Read-only permission is suitable for scenarios where multiple clients need to access the same LUN but should not modify data.

## Common Issue

**Q：Read-only permission is suitable for scenarios where multiple clients need to access the same LUN but should not modify data.**

A：After changing permissions, connected clients retain their existing session settings. To apply the new read-only permission, you must disconnect and reconnect the client so it can establish a new session and load the updated permission settings.
