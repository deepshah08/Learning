# How to Set "Read & Write", "Read only", and "Deny access" Permissions for Shared Folders in Files When Multiple Users Use NAS

> **Article ID**: `518`  
> **Category**: `Application Guide > Files > FAQ > How to Set "Read & Write", "Read only", and "Deny access" Permissions for Shared Folders in Files When Multiple Users Use NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/518  

---

> **Applicable Version**: UGOS Pro 1.15.0.0114 and above
>
> Screenshots and interfaces in this document are for reference only. Actual displays may vary depending on system or application version. Some features may change across versions, please refer to your actual interface.

When sharing a UGREEN NAS with family, friends, or colleagues, you can assign different access permissions to users for shared folders, including **Deny access**, **Read & Write**, and **Read only**. If no permission is specified, it defaults to none (empty). These permission settings determine the range of operations a user or user group can perform within the shared folder. This guide explains how to configure these permissions in detail.

## Differences Between Deny Access, Read & Write, and Read Only Permissions

|  |  |  |
| --- | --- | --- |
| **Permission** | **Description** | **Recommended Use Case** |
| Deny access | Prevents a user or user group from viewing or accessing the shared folder and its files. | Suitable for restricting sensitive or private files (e.g., personal documents, financial data). |
| Read & Write | Allows a user or user group to view, read, modify, and delete files in the shared folder, with full operational privileges. | Suitable for collaborative scenarios where multiple users need to manage and edit shared files (e.g., office project teams). |
| Read only | Allows a user or user group to view and read files in the shared folder, but prohibits editing, uploading, or deleting files. | Suitable for situations where users need access to view files without modifying content (e.g., family members accessing photos). |

**Notes:**

● If an **administrator** does not specify permissions, the default is **Read & Write**; for **standard users**, the default is **Deny access**.

● If a standard user belongs to multiple user groups, the permission priority rule generally follows: **Deny access>Read only>Read & Write>Empty**.

## Setting Shared Folder Permissions for Different Users

1. In the Shared Folder list, right-click the target folder and select "**Properties**">"**Permissions**".

2. In the permissions settings interface, assign access rights to the specified users. The following example demonstrates permission settings for the shared folder "Video":

![](https://file-us.ugreennas.com/admin/article/2026-05-12/ab2e2e20f28840d792d033c71fdc9ce9.webp)

● `User1`: Set to **Deny access**, preventing User1 from viewing or accessing any content in the shared folder "Video".

● `User2`: Set to **Read & Write**, allowing User2 to access and manage files in the shared folder "Video", including uploading, downloading, editing, deleting, and renaming.

● `User3`: Set to **Read only**, allowing User3 to view files in the shared folder "Video", but preventing any modifications or uploads.

3. After configuring the permissions, click "**Confirm**" to apply the changes.
