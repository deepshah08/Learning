# How to Quickly Grant Shared Folder Management Permissions to a NAS Account

> **Article ID**: `730`  
> **Category**: `Application Guide > Files > FAQ > How to Quickly Grant Shared Folder Management Permissions to a NAS Account`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/730  

---

> **Applicable Version**: UGOS Pro 1.15.0.0114 and above
>
> Screenshots and interfaces in this document are for reference only. Actual displays may vary depending on system or application version. Some features may change across versions, please refer to your actual interface.

In the UGOS Pro system, administrators can grant users full access permissions to specific shared folders by configuring shared folder permissions. After assigning "**Read & Write**" permission, users can create, modify, move, or delete files within that folder. The following methods can be used to configure permissions:

## Configure Shared Folder Permissions via Control Panel

1. Open "**Control Panel**" and go to "**User Management**">"**User**".

![](https://file-us.ugreennas.com/admin/article/2026-05-13/649609d5de254161ae413692365c7dba.webp)

2. In the user list, locate the target user and **double-click the user** to enter the edit page.

3. Switch to the "**Permissions & Settings**" tab.

4. In the shared folder list, locate the target folder.

5. Set the permission to "**Read & Write**", then click "**Save**" to apply the settings.

![](https://file-us.ugreennas.com/admin/article/2026-05-13/b67313bbd65c45fb80fc381b0d40e568.webp)

## Configure Shared Folder Permissions via Files

1. Open "**Files**" and click "**Shared Folder**" in the left sidebar.

2. Select the target shared folder, right-click it, and choose "**Properties**".

![](https://file-us.ugreennas.com/admin/article/2026-05-13/5cfc745cc67241638b43873454539cd0.webp)

3. Switch to the "**Permissions**" tab and locate the target user.

4. Set the user's permission to "**Read & Write**", then click "**Confirm**" to save the configuration.

![](https://file-us.ugreennas.com/admin/article/2026-05-13/4512bfc731134e2481df59b0adcb06d6.webp)

**Note**:

When a user belongs to multiple user groups, and those groups have different permissions for the same shared folder, the system applies permissions according to the following priority order: **Deny access>Read only>Read & Write**

● **Example 1**:User A belongs to two user groups. Group X has "**Read only**" permission for Shared Folder A, while Group Y has "**Read & Write**" permission. After permission evaluation, User A's effective permission for the folder will be "**Read only**", meaning the user cannot modify the folder contents.

● **Example 2**: User A has "**Read & Write**" permission individually, but one of the user's groups is assigned "**Deny access**" for the same shared folder. In this case, the final effective permission will be "**Deny access**", and the user will not be able to access the folder.
