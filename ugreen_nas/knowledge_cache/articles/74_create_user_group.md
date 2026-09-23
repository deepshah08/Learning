# Create User Group

> **Article ID**: `74`  
> **Category**: `Application Guide > Control Panel > User Management > Create User Group`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/74  

---

A "**User Group**" is a tool used to manage permissions for files and folders. It allows administrators to organize users with the same access permissions into a single group. By creating user groups, administrators can efficiently manage permissions for multiple users, ensuring the security and consistency of files and folders. Below is a guide to creating a user group.

## Steps to Create a User Group

1. Open the "**Control Panel**" application, then navigate to "**User Management**">"**User Group**">"**Add**".

2. In the pop-up window, enter the user group name and description, then click "**Next**".

3. Select the members to be added to the user group, then click "**Next**".

4. Choose the user group's permissions for shared folders: Access denied, Read/Write, or Read only. For more details, please refer to [Shared Folder Permission Usage Instructions](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMDcwLCJhcnRpY2xlSW5mb0lkIjozNjMsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==) .

5. Click "**Done**" to complete the creation of the user group.

![](https://file-us.ugreennas.com/admin/article/2025-12-29/a35b1541f34a4437bdfb881f64d908d8.webp)

## Usage Tips

When a user's individual permissions conflict with the permissions of the user group they belong to, the system follows the permission priority rules below:

● **Access denied > Read/Write > Read only**

● For example, if the user group permission is set to "**Access denied**" while the user's individual permission is "**Read/Write**", the user's effective permission will be "**Access denied**".

● For more information, please refer to [Priority Between Individual and User Group Permissions](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTUyMiwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo1MjQsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==) .
