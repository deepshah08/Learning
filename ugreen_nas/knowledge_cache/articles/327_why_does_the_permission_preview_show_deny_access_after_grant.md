# Why Does the Permission Preview Show "Deny access" After Granting "Read & Write" Permission to a Shared Folder

> **Article ID**: `327`  
> **Category**: `Application Guide > Files > FAQ > Why Does the Permission Preview Show "Deny access" After Granting "Read & Write" Permission to a Shared Folder`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/327  

---

> **Applicable Version**: UGOS Pro 1.15.0.0114 and above
>
> Screenshots and interfaces in this document are for reference only. Actual displays may vary depending on system or application version. Some features may change across versions, please refer to your actual interface.

## Issue Description

In the **Files** application, when configuring shared folder access permissions for a user or user group, the permission preview may still display "**Deny access**" even after selecting "**Read & Write**" or "**Read only**"permissions.

![](https://file-us.ugreennas.com/admin/article/2026-05-13/139fe81ff0b14daaaa2985a913c2d4c1.webp)

## Cause Analysis

When a user's individual permission conflicts with the permissions of the user groups they belong to, the system applies the following priority rule: **Deny access>Read only>Read & Write**. For example, If the user group permission is set to "**Deny access**", While the user's individual permission is set to "**Read only**", in this case, a conflict occurs, and "**Deny access**" takes precedence. As a result, the user's effective permission becomes "**Deny access**".

![](https://file-us.ugreennas.com/admin/article/2026-05-13/a59e2e3112f5475ca51c330daf9b9abd.webp)

## Solution

If this issue occurs, follow these steps to check whether a "**Deny access**" permission has been configured:

1. Go to "**Control Panel**" and navigate to "**User Management>User Group>Edit user group>Permissions & Settings**".

2. In the "**Permissions & Settings**" list, select the target shared folder and check whether "**Deny access**" is enabled.

![](https://file-us.ugreennas.com/admin/article/2026-05-13/0fbad7bd7f1e437598111882343f0e46.webp)

3. If you want the user to have "**Read & Write**" or "**Read only**" permission, reselect the corresponding permission and click "**Save**" to apply the changes.

**Note**: When a user belongs to multiple user groups, group permission priority follows the order: **Deny access>Read only>Read & Write>Empty**. For example, there is a user belongs to both Group A and Group B. In Group A, the permission for the folder "Video" is set to **Read only**. In Group B, the permission for the folder "Video"is set to **Deny access**. In this case, the user's effective permission for th folder "Video"will be **Deny access**.
