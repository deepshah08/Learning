# How Parent Folder Permissions Affect Subfolders and Files

> **Article ID**: `832`  
> **Category**: `Application Guide > Files > FAQ > How Parent Folder Permissions Affect Subfolders and Files`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/832  

---

**Applicable Note**: This document applies to UGOS Pro 1.15.0.0114 and later. Screenshots and interfaces in this document are for reference only. Actual displays may vary depending on system or application version.

When configuring permissions for multi-level folders in "**Files**", changes to the permissions of a parent (upper-level) folder can have different impacts on its subfolders and files. The following explains how permission changes in a parent folder affect the permissions of subfolders and files within a multi-level folder structure.

## Default Inheritance for Newly Created Items

When a user creates a new file or subfolder within a folder, the new item will automatically inherit the permissions of its parent folder.

**Example:**

Assume there is a parent folder named "**Project Documents**" with the following permissions. When a new subfolder "**2026 Plan**" is created inside it, the new folder will inherit the same permissions:

|  |  |  |
| --- | --- | --- |
| **User** | **Parent Folder Permission (Project Documents)** | **New Subfolder Permission (2026 Plan)** |
| User A | Read & Write | Read & Write (inherited) |
| User B | Read Only | Read Only (inherited) |
| User C | No Access | No Access (inherited) |

## How Changes to Parent Permissions Affect Existing Subfolders

To enable more granular permission management and prevent unintended overwrite of subfolder settings when modifying parent folder permissions, the UGOS Pro system allows users to choose "**how changes to a parent folder's permissions are applied to existing subfolders and files, based on their specific needs**".

![](https://file-us.ugreennas.com/admin/article/2026-04-27/419ee184d6b94460971f1ea076bdac40.webp)

When modifying permissions for a parent folder (e.g., a top-level shared folder), the system provides three options:

### Option 1: Merge (Default)

Synchronize changes made to the parent folder's permissions to its subfolders, while preserving any existing independent permissions of the subfolders. The rules are as follows:

● Additions in the parent → Added to subfolders

● Removals in the parent → Removed from subfolders

● Permissions unique to subfolders and not affected by the parent → Retained

● Modifications in the parent → The same changes are applied to subfolders

**Use case**: Suitable when you want to adjust parent folder permissions while still retaining the subfolders' original granular settings.

**Example**: The parent folder initially grants access to Users A and B. A subfolder was previously granted access to User C independently.

After modifying the parent folder (removing User B and adding User D) and selecting "**Merge**", **the resulting permissions are**: The subfolder inherits the removal of B and the addition of D, while User C's independent access remains unchanged.

### Option 2: Overwrite

Replace all permission settings in subfolders, making their permissions identical to those of the parent folder.

**Use Case**: Suitable when you need to enforce a unified permission structure across the entire directory and remove all independent permissions from subfolders.

**Example**: Subfolders under the parent folder currently have different permission settings. You now want to standardize them so that only User A has read/write access and User B has read-only access.  
After selecting "**Overwrite**", the result is: All subfolders will have permissions identical to the parent folder, and any existing independent settings will be removed.

### Option 3: Do Not Apply (None)

Only modify the permissions of the current parent folder without affecting any existing subfolders or files.

**Use Case**: Suitable when you only need to adjust the access permissions of the current folder and do not want to change the existing permissions of its subfolders.

**Example**: You only need to adjust the parent folder's access permissions (e.g., adding a new administrator), while all existing subfolder permissions must remain unchanged.

After selecting "**None**", the result is: The parent folder's permissions are updated, and subfolder permissions remain unchanged.

**Notes**:

● The above three options only affect existing subfolders and files. Any newly created subfolders will still inherit permissions from their parent folder according to the default logic.

● If "**Merge**" or "**Overwrite**" is selected, applying the changes may take some time. The duration depends on the depth of the folder hierarchy and the number of files.
