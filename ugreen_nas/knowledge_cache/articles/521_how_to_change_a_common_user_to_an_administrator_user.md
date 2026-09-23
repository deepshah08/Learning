# How to change a common user to an administrator user?

> **Article ID**: `521`  
> **Category**: `Application Guide > Control Panel > FAQ > How to change a common user to an administrator user?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/521  

---

In the UGOS Pro system, user roles are divided into administrators and common users. The role determines the scope of permissions and management capabilities. Administrators have higher privileges, allowing them to fully manage the system and folders, while common users have limited permissions. For more details, please refer to [Differences Between Common Users and Administrators.](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTUyMCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo1MjIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

Below are the specific steps to upgrade a regular user to an administrator:

## **Steps**

1. Log in to the UGOS Pro management interface, navigate to [Control Panel]>[User Management]>[User], and locate the user whose role needs to be changed in the user list.
2. In the action column to the right of the target user, click the “...” button and select “Edit.”

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250606/be6376ad-b4a1-4c52-9ed0-df667e4d8831.png)

3. Go to [Edit User]>[Basic Info] page, and in the “Role” dropdown, change “common user” to “administrator.”
4. Click the “Save” button at the bottom of the page, and the system will automatically apply the changes.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250606/9ada8547-114f-4b45-83ab-137c2915ec17.png)

## **Notes**

**Administrator Privileges:**

* File Management Permissions: Administrator users can access and manage all folders, including files belonging to other users (both administrators and common users).
* Permission Assignment: Administrators can set or modify permissions for other users, including upgrading common users to administrators.

**Security Considerations:**

* Administrators have the highest level of permissions. Assign the administrator role only to trusted users to avoid potential misoperations or security risks.
* It is recommended to regularly review the list of administrator users to ensure that only necessary personnel have administrator privileges.

**Permission Revocation:**

* If you need to downgrade an administrator to a common user, use the same process to change the role from “administrator” to “common user.”
