# Shared Folder Permissions Guide

> **Article ID**: `363`  
> **Category**: `Application Guide > Files > FAQ > Shared Folder Permissions Guide`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/363  

---

## Applicability

**Applicable Version**: NAS Firmware 1.18.1.0098 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Differences Between Deny access, Read/Write, and Read-only Permissions

Shared folder permissions include **Deny access**, **Read/Write**, and **Read-only**. If no permission is specified, it defaults to **Empty**.

|  |  |
| --- | --- |
| **Permission** | **Description** |
| Deny access | Prevents the user or user group from reading or modifying files in the shared folder. |
| Read/Write | Allows the user or user group to read and modify files in the shared folder, including uploading, creating, editing, deleting, and renaming files. |
| Read-only | Allows the user or user group to read files in the shared folder but prevents any modifications. |
| Not set (Empty) | If the administrator does not specify a permission, the default permission is Read/Write. If a standard user does not specify a permission, the default permission is Deny access. |

## Permission Logic

When configuring shared folder permissions, the default permission settings generally apply to the current folder, its subfolders, and files. If no permission is specified for the current folder, the folder **inherits** the permission from its parent folder. If the permission for the current folder is modified, the final permission is determined based on the combined settings of the parent folder permission and the current folder permission.

**Parent Folder Permission**: Refers to the permission set for the current user or user group by the parent folder (the folder at the previous level).

**Current Folder Permission**: Refers to the permission directly set for the current user or user group on the current folder itself.

### 1 Permission Types

● **Explicit Permission**: Permission directly configured for a first-level shared folder or individually assigned to a specific folder.

● **Inherited Permission**: Permission inherited from the parent folder.

### 2 Permission Conflict and Non-Conflict Cases

● **Conflict Case**: A permission conflict occurs when either the parent folder permission or the current folder permission is set to "Deny access". Example: The parent folder permission is Read-only or Read/Write, while the current folder permission is Deny access.

● **Non-Conflict Case**: When neither permission is set to Deny access (both are Read-only or Read/Write), the permissions do not conflict and can be combined.

### 3 Priority Rules

**Case 1**: Conflict Between Explicit Permissions or Between User and User Group Permissions

● The priority order is: **Deny access > Read-only > Read/Write > Not set** (Empty).

**Case 2**: Both Explicit Permission and Inherited Permission Exist

● **Explicit permission takes priority over inherited permission.**

**Case 3**: Combined Calculation of Explicit Permission and Inherited Permission

● If a conflict occurs, "**Deny access**" takes priority:

Parent folder permission: Deny access; Current folder permission: Read/Write → Effective permission: **Deny access**

● If there is no conflict, permissions are combined, and the final permission is determined by the **current folder permission**:

Parent folder permission: Read/Write; Current folder permission: Read-only → Effective permission: **Read-only**

Parent folder permission: Read-only; Current folder permission: Read/Write → Effective permission: **Read/Write**

Parent folder permission: Read-only; Current folder permission: Read-only → Effective permission: **Read-only**

## User and User Group Permission Conflicts

When a regular user is assigned individual permissions and the user group they belong to also has permissions configured, the permission priority follows: **Deny access > Read-only > Read/Write > Empty**.

The following table lists all possible scenarios. You can refer to it based on your permission settings:

|  |  |  |
| --- | --- | --- |
| **User Permission** | **User Group Permission** | **Effective Permission** |
| Deny access | Deny access | Deny access |
| Deny access | Read-only | Deny access |
| Deny access | Read/Write | Deny access |
| Deny access | Not set | Deny access |
| Read-only | Deny access | Deny access |
| Read-only | Read-only | Read-only |
| Read-only | Read/Write | Read-only |
| Read-only | Not set | Read-only |
| Read/Write | Deny access | Deny access |
| Read/Write | Read-only | Read-only |
| Read/Write | Read/Write | Read/Write |
| Read/Write | Not set | Read/Write |
| Not set | Deny access | Deny access |
| Not set | Read-only | Read-only |
| Not set | Read/Write | Read/Write |
| Not set | Not set | Deny access |

**Notes**:

● When individual user permissions conflict with user group permissions, the priority order is **Deny access > Read-only > Read/Write > Empty**.

● When a user belongs to multiple user groups, and conflicts occur between user group permissions, the user group permission priority also follows **Deny access > Read-only > Read/Write > Empty**.

● When accessing shared folders through the SMB protocol, shared folder permissions are displayed based on the logged-in user's permissions. SMB permissions are consistent with those in Files.

● When accessing shared folders through the NFS protocol, shared folder permissions are determined by the permissions configured in NFS settings.

### Examples

Assume there are two users: userA (administrator) and userB (regular user). userB belongs to three user groups: group1, group2, and group3. Shared folder a and subfolder b have been created.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/0ff6d8d4e9504d269c35b942ad333a7d.webp)

**Scenario 1: Conflict Between Explicit Permission and Inherited Permission**

|  |  |
| --- | --- |
| **Specific Settings and Results** | **Permission Logic Description** |
| Assume the permissions configured for "Shared Folder a" are: group1 is set to Deny access, group2 is set to Read/Write, and group3 is set to Read-only.    userB belongs to group1, group2, and group3 at the same time. According to the priority order Deny access > Read-only > Read/Write, the highest group permission is "**Deny access**".    Therefore, the effective permission of userB for Shared Folder a is: **Deny access**.  As shown in the figure: | The permissions directly configured for a shared folder are all explicit permissions. When multiple group permissions conflict, the priority order "**Deny access > Read-only > Read/Write > Empty**" applies. |
| If a "Subfolder b" is created under "Shared Folder a", and no individual permissions are configured for the three groups (all are Empty).  Subfolder b has no explicit permission and inherits the permission from the parent folder. The effective permission of userB for Subfolder b remains: **Deny access**. | When no permission is configured for a subfolder, it automatically inherits the permission from the parent folder. |
| If the permission of "Subfolder b" is modified separately and the individual permission of userB is set to **Read-only**.  At this point, userB has an explicit permission (Read-only) on Subfolder b, while the inherited permission from the parent folder is Deny access. According to the rule that Deny access takes priority, the effective permission of userB for Subfolder b is: **Deny access**. | When either the parent folder permission or the current folder permission is "**Deny access**", it is considered a permission conflict, and "**Deny access**" takes priority. |

**Scenario 2: When Explicit Permission and Inherited Permission Do Not Conflict**

|  |  |
| --- | --- |
| Assume the permissions configured for "Shared Folder a" are: group1 is Empty, group2 is Read-only, and group3 is Empty.  Among the three groups that userB belongs to, the highest permission is Read-only. Therefore, the effective permission of userB for "Shared Folder a" is: **Read-only**.  As shown in the figure: | The user group permission is Read-only, and the user's effective permission is inherited from the group permission as Read-only. |
| If a "Subfolder b" is created under "Shared Folder a", and no permissions are configured separately.  Subfolder b inherits the permission from the parent folder, and the effective permission of userB for Subfolder b remains: **Read-only**.  As shown in the figure: | When no permission is specified for a subfolder, it inherits the permission from the parent folder. |
| If the permission of "Subfolder b" is modified separately and the individual permission of userB is set to Read/Write.  At this point, the inherited permission is Read-only, and the explicit permission is Read/Write. The two permissions do not conflict. According to the permission combination rule, the final permission is determined by the current folder permission. Therefore, the effective permission is: **Read/Write**.  As shown in the figure: | When permissions do not conflict, they are combined. When Read-only and Read/Write are combined, the final permission is determined by the current folder permission (Read/Write). |

## Additional Notes

### Required Permissions for Common File Operations in Shared Folders

Different file operations in shared folders require different permission levels. The following table lists common file operations and their required permissions:

|  |  |  |
| --- | --- | --- |
| **File Operation** | **Required Permission for Source** | **Required Permission for Destination** |
| Upload | Read/Write | Read/Write |
| Download | Read-only or Read/Write | Read/Write |
| Open | Read-only or Read/Write | - |
| Delete | Read/Write | - |
| Copy | Read-only or Read/Write | Read/Write |
| Move | Read/Write | Read/Write |
| Cut | Read/Write | Read/Write |
| Rename | Read/Write | - |
| Extract Files | Read-only or Read/Write | Read/Write |
| Compress Files | Read-only or Read/Write | Read/Write |

### Shared Folder Permission Settings

When the parent folder permission and the current folder permission are different, the available operations are as shown in the table below. You can refer to it based on your permission settings.

|  |  |
| --- | --- |
| **Permission Combination** | **Supported File Operations** |
| Parent Folder (Read/Write) + Current Folder (Read/Write) | Copy Files, Paste Files, Cut Files, Rename Files, Delete Files, Open Files, Upload Files, Download Files, Copy To, Move To, Paste and Overwrite, Add Compressed Files, Compress To, Extract Files, Extract To |
| Parent Folder (Read/Write) + Current Folder (Read-only) | Copy Files, Open Files, Download Files, Copy To |
| Parent Folder (Read/Write) + Current Folder (Deny access) | No file operation permissions |
| Parent Folder (Read-only) + Current Folder (Read/Write) | Copy Files, Paste Files, Cut Files, Rename Files, Delete Files, Open Files, Upload Files, Download Files, Copy To, Move To, Paste and Overwrite, Add Compressed Files, Compress To, Extract Files, Extract To |
| Parent Folder (Read-only) + Current Folder (Read-only) | Copy Files, Open Files, Download Files, Copy To |
| Parent Folder (Read-only) + Current Folder (Deny access) | No file operation permissions |
| Parent Folder (Deny access) + Current Folder (Read/Write) | No file operation permissions |
| Parent Folder (Deny access) + Current Folder (Read-only) | No file operation permissions |
| Parent Folder (Deny access) + Current Folder (Deny access) | No file operation permissions |

**Note**: Pasting requires the corresponding copy or move operation to be performed first. For paste and extract operations, the permission of the destination folder must be checked.
