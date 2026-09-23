# How to manage user access permissions for the Theater library?

> **Article ID**: `692`  
> **Category**: `Application Guide > Theater > FAQ > How to manage user access permissions for the Theater library?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/692  

---

## **[Issue Description]**

In the UGOS Pro system, how can user access permissions to Theater libraries be configured and managed?

## **[Solution]**

User access permissions to Theater libraries are determined by user roles within the UGOS Pro system:

* **Administrator Permissions:** By default, users with the administrator role have access to all libraries.
* **Common User Permissions:** By default, regular users do not have access to any libraries and must be manually granted access by an administrator.

|  |  |
| --- | --- |
| **Permission Type** | **Description** |
| **Administrator Permissions** | Full control over the Theater, including adding libraries, deleting content, and editing metadata. |
| **Common User Permissions** | Can only view and play content in authorized libraries; cannot modify or delete any content. |

Permission settings are linked to the user's initial role configuration but do not automatically update when the role changes. Specifically:

* A newly created administrator user is granted access to all libraries by default. Even if their role is later changed to a common user, the access permissions will remain unchanged and must be manually adjusted.
* A newly created common user has no access to any libraries by default. Even if their role is later changed to an administrator, the access permissions will still be denied and must be manually adjusted.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250529/83b61a3f-951e-488a-845f-c6f742d751a8.png)

**How to Set or Modify a User’s Library Access Permissions**

1. Log in to the UGOS Pro system with an administrator account and go to the Theater [Settings] page.
2. Click "User Management" in the left menu, find the account you want to modify in the user list, and click "Set Permissions".
3. In the user permission configuration, change the library access permission from "Block Access" to "Allow Access".

4. Click "Apply" to save the settings. Once the changes are saved, the user will be able to access the library and view content.
5. Ask the user to log back into the Theater and check whether they can access the specified library.

If the permission changes do not take effect, please verify that the administrator's changes were saved successfully and recheck the configuration.

## **[Notes]**

* The initial value of a user's library access permission is based on their user role ("Administrator" or "Common User"). Changes to the user role later on will **not** automatically update library access permissions; manual adjustments are required.
* Even if a common user is granted access to a library, they still cannot perform administrator-level functions (such as library configuration or deletion).
* If a new library is added to the Theater, common users will have "Block Access" as the default permission. Administrators must manually grant access rights.
