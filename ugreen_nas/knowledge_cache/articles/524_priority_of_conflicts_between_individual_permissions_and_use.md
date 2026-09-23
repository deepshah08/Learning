# Priority of Conflicts Between Individual Permissions and User Group Permissions

> **Article ID**: `524`  
> **Category**: `Application Guide > Control Panel > User Management > Priority of Conflicts Between Individual Permissions and User Group Permissions`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/524  

---

In the UGOS Pro system, when conflicts occur between individual user permissions and the permissions of the user group they belong to, the system follows a permission priority rule: "**Deny access>Read-only>Read/Write>Empty**." For example, if a user is assigned both "**Read/Write**" and "**Read-only**" permissions for the same shared folder, the system will prioritize the "**Read-only**" restriction. Through this rule, the system strengthens data security and enables stricter access control, helping prevent unauthorized access and accidental file modifications.

![](https://file-us.ugreennas.com/admin/article/2026-05-09/36efa7f6ada14b19a125b0d39030dbbe.webp)

## Permission Definitions and Conflict

#### 1 Permission Definitions

● **Individual Permissions**: Permissions assigned directly to a user for a shared folder, representing the user's direct access control.

● **User Group Permissions**: Unified permission settings applied to a group of users, affecting all members within the group.

#### 2 Typical Permission Conflict Scenarios

Assume the following permission settings exist for a shared folder:

● The individual permission of user `User1` is set to "**Deny access**."

● The permission of user group `group1` is set to "**Read & Write,**" and `User1` is a member of this group.

In this case, the system will apply the permission priority rules, and the individual permission "**Deny access**" will take precedence.

## Permission Priority Rules

1. **Deny access Takes Priority**

● When the individual permission is set to "**Deny access,**" the user will be unable to access the shared folder regardless of the user group permission settings.

● When the individual permission is set to "**Read only**" or "**Read & Write,**"but the user group permission is set to "**Deny access,**" the user will still be unable to access the shared folder.

2. **Read only Takes Priority Over Read & Write**

● When the individual permission is set to "**Read & Write**," but the user group permission is set to **"Read only,"** the system will prioritize the "**Read only**" restriction to enhance data security and prevent accidental file modifications.

● When the individual permission is set to "**Read only,**" but the user group permission is set to "**Read & Write,**" the user will only be allowed to access shared files in "**Read only"** mode and will not be able to upload, edit, or delete files.

## Practical Application Examples

Assume the following shared folder permission configuration:

1. **Individual Permission Configuration**

If only `User1` is assigned the individual permission "**Read & Write,**" then `User1` will be able to perform read and write operations on the shared folder, regardless of whether the user belongs to any user group.

![](https://file-us.ugreennas.com/admin/article/2026-05-09/efe59afe706846b3b0d4b64b0275f059.webp)

2. **User Group Permissions Only**

If only the user group `group1` is assigned the permission "**Read only,**" then all members of `group1` will only be able to access the shared folder with "**Read only**" permissions and will not be allowed to modify files.

![](https://file-us.ugreennas.com/admin/article/2026-05-09/10537d36fac24456b88f995b440df92e.webp)

3. **Conflict Between Individual Permissions and User Group Permissions**

If `User1` belongs to `group1` and their permissions conflict:

● `User1` **permission: Read & Write**

● `group1` **permission: Read only**

**Effective permission**: According to the priority rules, `User1` will ultimately have "**Read only**" permission and will not be able to modify the shared folder.

![](https://file-us.ugreennas.com/admin/article/2026-05-09/7bedd97b30784a3eae20aa18c1736124.webp)
