# When a user tries to access a shared folder and sees the message "Insufficient permissions to perform this operation," how should it be handled?

> **Article ID**: `526`  
> **Category**: `Application Guide > Files > FAQ > When a user tries to access a shared folder and sees the message "Insufficient permissions to perform this operation," how should it be handled?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/526  

---

## **Issue Description**

In the UGOS Pro system, regular users may encounter the error message “Insufficient permissions to perform this operation” when attempting to access a shared folder. This issue typically occurs because the user has not been granted access to the shared folder—the current permission is set to “Access denied.” To allow the user to access the shared folder, their permission must be changed to either “Read/Write” or “Read Only.”

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250616/f05c9c51-8960-404a-a9dd-d0c4fb8f6f5b.png)

## **Solution**

You can modify shared folder permissions in either of the following two ways:

#### **Method 1: Modify Permissions via Control Panel**

1. Go to [Control Panel] > [User Management] > [User].
2. In the user list, locate the target user and click the username or the “...” button on the right.
3. In the [Edit User] > [Permissions & Settings] tab, find the shared folder you want to modify.
4. Set the permission for that shared folder to either “Read/Write” or “Read Only”, depending on your needs.
5. Click “Save” to apply the changes.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250616/3a0320c8-dfcc-4ed8-99ab-5ea8e17f7e7f.png)

#### **Method 2: Modify Permissions via Files**

1. Go to [Files] > [Shared Folder].
2. Locate the target shared folder, right-click on it, and select “Properties.”
3. In the [Properties] > [Permissions] tab, find the username whose permissions you want to modify.
4. Set the user’s permission to either “Read/Write” or “Read Only”, as needed.
5. Click “OK” to apply the changes.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250616/9d8533f1-2b4c-4d41-bf29-410d87bbc586.png)

### **Shared Folder Permission Descriptions**

* **Access denied**: The user cannot view or access any content within the shared folder.
* **Read Only**: The user can view and read files in the shared folder but cannot modify, upload, or delete any files.
* **Read/Write**: The user has full access to the shared folder, including permissions to view, read, modify, upload, and delete files.

Administrators can assign permissions based on the user's actual needs to ensure both system security and operational efficiency.
