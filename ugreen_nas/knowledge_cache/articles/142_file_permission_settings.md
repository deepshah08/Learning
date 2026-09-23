# File Permission Settings

> **Article ID**: `142`  
> **Category**: `Application Guide > Files > File Permission Settings`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/142  

---

**Applicable Version:** UGOS Pro 1.10.0.0092 and above

Screenshots and interfaces in this document are for reference only. Actual displays may vary depending on system or application version. Some features may change across versions, please refer to your actual interface.

## Change Permissions for Shared Files or Folders

### Assign File or Folder Permissions

You can specify which users or user groups are allowed to access, view, or modify shared folders and their contents. Each user or user group can have customized access permissions for shared folders, as well as for individual files and subfolders.

If you need to configure more advanced permission settings for an individual user, you must enable shared folder permissions in "**Control Panel**">"**User Management**">"**User**">"**Edit**">"**Permissions & Settings**".

![](https://file-us.ugreennas.com/admin/article/2025-12-30/2d664f38e2034ac283c59f98749d7a66.webp)

To Assign Permissions for shared files or folders:

1. Open "**Files**".

2. Select the target shared file or folder.

3. Right-click and select "**Properties**". Select "**Permissions**" **i**n the pop-up window.

4. Enable or disable the following permissions for the owner, group, or other users listed:

● **Access denied**: The user or user group cannot access files or subfolders within the shared folder.

● **Read/Write**: The user or user group can access and modify files and subfolders within the shared folder.

● **Read only**: The user or user group can access files and subfolders within the shared folder, but cannot modify them.

● **Optional**: Hide subfolders and files from users who do not have permissions (applies when accessing folders via Files or SMB).

5. Click "**Confirm**" to complete the operation.

**Note:**

● When a user's assigned permissions conflict with the permissions of the user group they belong to, the effective permission is determined by the following priority order: Access denied > Read/Write > Read Only > Empty. For example, if a user group is set to "**Read only**" but a specific user within that group is set to "**Access denied**", the user's effective permission will be "**Access denied**".

● When creating a new shared folder, if users in the **admin** user group are assigned "**Access denied**", they will only be able to see the shared folder in "**Files**"**>"Shared Folder**", but will not have permission to access or modify its contents.

## Manage Shared File/Folder Permissions

To Edit User or User Group Access Permissions:

1. Select the shared file or folder you want to configure, right-click it, and choose "**Properties**".

2. Go to the "**Permissions**" tab and use the drop-down options to set permissions for users or user groups.

3. On the permission editing page, you can manage the following:

● Select the user or user group whose permissions you want to edit.

● View the current permissions assigned to users or user groups.

● Hide subfolders and files from users who do not have permission (Applies when accessing folders via Files or SMB).

4. Click "**Confirm**" to save the changes and exit the Properties window.

**Note:**

If a shared folder is displayed as having no access permission, it may be due to one of the following reasons:

● The user or user group has been deleted.

● The user or user group has been explicitly denied access to the folder by an administrator.

If you need to modify permissions for such a shared folder, go to "**Control Panel**"**>"User Management**", select the user or user group to edit, then double-click, right-click and select "**Edit**", or click the "**Edit**" option from the action menu. In the "**Edit User/User Group**" page, click "**Permissions & Settings**", and change the shared folder permission to "**Read/Write**" or "**Read Only**" as required.

## Set NFS Permissions for a Shared Folder

NFS (Network File System) permissions refer to the settings that determine which client computers and users are allowed to access shared folders on the NAS via the NFS protocol. NFS is a protocol that enables different computer systems to share files and folders over a network, and it is widely used in Linux environments.

### Set NFS Permissions for a Specific Shared Folder

1. Select the folder you want to share, right-click, and choose "**Properties**".

![](https://file-us.ugreennas.com/admin/article/2025-12-30/68794bb0d7cc453cb70c38f5102e313c.webp)

2. Switch to the "**NFS Permissions**" tab and click "**Add**" to configure an NFS rule.

![](https://file-us.ugreennas.com/admin/article/2025-12-30/f511b9365ef0493cb7d63958f157acaa.webp)

3. In the "**Add NFS rules**" settings, enter the IP address of the device that will mount the NFS in the "**Server address"** field to ensure that only authorized devices can access it. The "**Permissions**" can be set to either "**Read-only**" or "**Read/Write**".

![](https://file-us.ugreennas.com/admin/article/2025-12-30/1d21c88f541143d6a196da3bf9109776.webp)

4. After confirming that all information is correct, click "**Confirm**" to save and apply the settings. You can modify the NFS permission rules for the shared folder at any time.

![](https://file-us.ugreennas.com/admin/article/2025-12-30/cf9ed4b3d1f243f7a29ef729a749c900.webp)

### Difference Between Sync and Async

These modes control how data is written:

● Synchronous (sync) mode ensures that data is written directly to disk immediately, improving data integrity and safety.

● Asynchronous (async) mode allows data to be temporarily stored in cache and written to disk in batches, which improves performance but may increase the risk of data loss.

**Notes:**

● When the server name is in the format **.domain**, the NFS client's IP address must have a corresponding DNS PTR record. The NAS must be able to resolve the IP address back to the same **.domain** name.

● When accessing a shared folder via NFS using a specific user account: if the "**AUTH\_SYS**" security type is selected, the NFS client and the UGREEN NAS must have identical **UID** (User Identifier) and **GID** (Group Identifier) values. Otherwise, the client's access permissions to the shared folder will be treated as **others**. To avoid permission conflicts, you can select "**Map all users to admin**" under "**Squash**".

● If the external device that creates the shared folder uses the **NTFS** or **FAT** file system, the **"Map all users to admin"** option will be enforced automatically.
