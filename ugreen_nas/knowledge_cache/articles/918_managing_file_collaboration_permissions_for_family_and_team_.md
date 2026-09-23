# Managing File Collaboration Permissions for Family and Team Members

> **Article ID**: `918`  
> **Category**: `Application Guide > Files > FAQ > Managing File Collaboration Permissions for Family and Team Members`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/918  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client, Web Browser

**Applicable Version**: UGOS Pro Firmware 1.18.0.0093 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Scenario Description

In family and team collaboration scenarios, you often need to share files stored on your NAS with family members or colleagues. However, different members may require different access permissions. This document uses real-world collaboration scenarios to help you quickly understand how to assign appropriate permissions to different members in a shared folder.

## Permission Type Description

Shared folder permissions are divided into three types. You can assign permissions based on each member's role:

|  |  |  |
| --- | --- | --- |
| **Permission** | **Available operations** | **Applicable scenarios** |
| **Read/Write** | View, upload, download, edit, delete, and rename files | Team members or family members who need to collaboratively edit files |
| **Read-only** | View and download files, but cannot modify or delete them | Users who only need to browse or download files |
| **Deny access** | Cannot view or access the folder | Used to restrict certain members from accessing private content |

**Note**: After creating a Shared Folder, if no permission is assigned to a standard user, the default permission is "**Deny access**". If no permission is assigned to an administrator, the default permission is "**Read/Write**".

## Permission Conflicts and Priority Rules

In actual use, permission conflicts are a common issue. For example, a member may belong to multiple user groups, or the permissions set for a parent folder and a subfolder may be inconsistent.

**Core Rules**:

1. **Deny access has the highest priority**:Regardless of other permission settings, if "**Deny access**" is applied, the final permission will always be "**Deny access**".

The priority order is: **Deny access > Read-only > Read/Write > Not specified (blank)**.

**When a user’s individual permission conflicts with the permission of a user group, the final permission is determined by the following rules**:

|  |  |  |
| --- | --- | --- |
| **User Permission** | **User Group Permission** | **Final Permission** |
| Deny access | Any | Deny access |
| Read-only | Read-only | Read-only |
| Read-only | Read/Write | Read-only |
| Read/Write | Read/Write | Read/Write |
| Read/Write | Read-only | Read-only |
| Not specified | Read/Write | Read/Write |
| Not specified | Read-only | Read-only |
| Not specified | Not specified | Deny access |

2. **Explicit permissions take priority over inherited permissions**: If permissions are set separately for a subfolder, the permissions configured for the subfolder will take priority.

**If the permissions set for a parent folder and its subfolder are inconsistent, the final permission is determined by the following rules**:

|  |  |  |
| --- | --- | --- |
| **Parent Folder Permission** | **Subfolder Permission** | **Final Permission** |
| Read/Write | Read-only | Read-only (No conflict, the subfolder takes priority.) |
| Read-only | Read/Write | Read/Write (No conflict, the subfolder takes priority.) |
| Read/Write (or Read-only) | Deny access | Deny access |
| Deny access | Read/Write (or Read-only) | Deny access |

## Steps

### Create a Shared Folder

1. Open the Files app and select "**Shared Folder**" from the sidebar.

2. Click "**Create shared folder**", enter a folder name (for example, "Family Photos"), and configure the required settings.

3. Click "**Create**" to open the Shared Folder permission configuration page.

4. If member accounts have not been created yet, click "**Confirm**" to complete the folder creation first.

### Create Users and User Groups

To create accounts for family members or team members, go to "**Control Panel**" > "**User Management**" to create users and user groups. After creation, you can assign different permissions to members in the Shared Folder permission settings. You can also right-click an existing Shared Folder and select "**Properties**" > "**Permissions**" to configure permissions.

### Set Shared Folder Permissions for Family Members or Team Members

1. Select the user or user group to configure from the user list, and assign the required permission (**Read/Write**, **Read-only**, or **Deny access**) for each member.

2. Click "**Confirm**" to save the settings.

### Set Individual Permissions for Subfolders

If you need to set different permissions for a specific subfolder within a Shared Folder (for example, only parents can edit the “**ID Documents**” subfolder under “**Family Photos**”, while others can only view it):

1. Open the Shared Folder, right-click the target subfolder, and select "**Properties**" > "**Permissions**".

2. Select the users from the user list and assign the required permissions. (Explicit permissions override permissions inherited from the parent folder.)

3. Click "**Confirm**" to apply the settings.

## Common Scenarios

### Scenario 1: Family Photo Sharing

**Requirement**: For example, you may want all family members to view and download family photos, while only you have permission to upload and organize photos.

**Setup Steps**:

1. Create a Shared Folder named "**Family Photos**".

2. Right-click the created Shared Folder and select "**Properties**" > "**Permissions**".

3. Select the corresponding family members and set their permission to "**Read-only**".

![](https://file-us.ugreennas.com/admin/article/2026-07-31/e6c80e69bf2746b2bfdedc74a2f5faaf.webp)

**Permission Settings**:

|  |  |  |
| --- | --- | --- |
| **Menber** | **Role** | **Recommended Permission** |
| You | Administrator | Read/Write (Default) |
| Other family members | Viewer and downloader | Read-only |

### Scenario 2: Team Project Collaboration

**Requirement**: Project members (such as Zhang and Wang) need to collaboratively edit documents. External Consultants only need to view and download materials. The Design Drafts folder requires the designer (Wang) to have Read/Write permission, while other members should not have access.

**Setup Steps**:

1. Create a Shared Folder named "**Project Files**", right-click it, and select "**Properties**" > "**Permissions**".

● Set project members (such as Zhang and Wang) to "**Read/Write**".

● Set External Consultants to "**Read-only**".

● Leave Intern permissions as Not specified.

![](https://file-us.ugreennas.com/admin/article/2026-07-31/854c2ecacd8c44d283cfd19921eaf692.webp)

2. Create a subfolder named "**Design Drafts**" under "**Project Files**".

● Set the designer (Wang) to "**Read/Write**" separately. Other members inherit permissions from the parent folder (Zhang: Read/Write, External Consultant: Read-only, Intern: Deny access).

● This ensures that the designer can edit files in the Design Drafts folder while other members can still access content based on their permissions inherited from the parent folder.

![](https://file-us.ugreennas.com/admin/article/2026-07-31/324597fc614c43b99c59d9249b1e9699.webp)

**Permission Settings**:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Member** | **Role** | **Parent Folder Permission (**"**Project Files**"**)** | **Subfolder Permission (**"**Design Drafts**"**)** | **Final Permission for Subfolder (**"**Design Drafts**"**)** |
| Wang | Designer | Read/Write | Read/Write | Read/Write |
| Zhang | Project Member | Read/Write | Inherited (Read/Write) | Read/Write |
| External Consultant | External Viewer | Read-only | Inherited (Read-only) | Read-only |
| Intern | Temporary Member | Not specified (Deny access by default) | Inherited (Deny access) | Deny access |

## Additional Notes

● **User group conflicts**: If a member belongs to multiple user groups and permissions conflict between groups, the same priority rule applies: **Deny access > Read-only > Read/Write > Not specified**.

● **Protocol access restrictions**: When accessing files through the SMB protocol, permissions are consistent with those in the Files app. When accessing files through the NFS protocol, permissions configured in NFS settings take priority.

● **Multi-level folder permission inheritance**: In a multi-level folder structure, changes to parent folder permissions may affect subfolders. The system uses "**Merge**" mode by default. Permissions added or removed from the parent folder will be synchronized to subfolders while retaining the subfolders’ existing individual permissions. For details about the three application modes (Merge / Overwrite / Do not apply), refer to “[How Parent Folder Permissions Affect Subfolders and Files](https://support.ugnas.com/knowledgecenter/detail/article/zh-CN/832?clientType=COMMON) ”。

## Related Articles

[How to Create User Accounts and Assign Permissions](https://support.ugnas.com/knowledgecenter/detail/article/zh-CN/852)

[Shared Folder Permissions Guide](https://support.ugnas.com/knowledgecenter/detail/article/zh-CN/363?clientType=PC)
