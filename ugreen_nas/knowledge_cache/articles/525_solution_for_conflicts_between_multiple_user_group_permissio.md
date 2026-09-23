# Solution for Conflicts Between Multiple User Group Permissions

> **Article ID**: `525`  
> **Category**: `Application Guide > Control Panel > User Management > Solution for Conflicts Between Multiple User Group Permissions`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/525  

---

In the UGOS Pro system, a user can belong to multiple user groups at the same time. When permission settings among these user groups conflict, the system follows the priority rule: "**Deny access>Read-only>Read/Write>Empty.**"This enforcement ensures that user access permissions remain clear and consistent, helping prevent permission conflicts while strengthening data security.

![](https://file-us.ugreennas.com/admin/article/2026-05-09/655ad1b91d6d44a2892aa5a93654971f.webp)

## Rules for Conflicts Between Multiple User Group Permissions

1. **Deny access Takes Priority**

If any user group that the user belongs to is assigned the "**Deny access**" permission, the user will be unable to access the shared folder regardless of the permissions assigned by other user groups.

2. **Read only Takes Priority Over Read & Write**

If conflicting user group permissions are set to "**Read & Write**" and "**Read only,**" the system will assign the user "**Read only**" permission, preventing modification operations on the shared folder.

## Examples of Permission Conflict

#### 1 Permission Conflicts Between Multiple User Groups

Assume that user `User1` belongs to the following two user groups:

● group 3: Permission is set to "**Deny access.**"

● group 2: Permission is set to "**Read & Write.**"

According to the priority rule "**Deny access>Read only>Read & Write,**" "**Deny access**" takes precedence over all other permissions. Therefore, `User1` will be unable to access the shared folder.

![](https://file-us.ugreennas.com/admin/article/2026-05-09/c24745e3eb864d4a98df10ce55568fef.webp)

#### 2 Different Permission Levels Assigned by Multiple User Groups

Assume that user `User1` belongs to the following two user groups:

● group 2: Permission is set to "**Read only.**"

● group 3: Permission is set to "**Read & Write.**"

According to the priority rule "**Read only>Read & Write,**" the effective permission will be "**Read only.**" As a result, the user will not be able to modify the shared folder.

![](https://file-us.ugreennas.com/admin/article/2026-05-09/98e2b96e1fe748de8fc7c01102f3efe9.webp)
