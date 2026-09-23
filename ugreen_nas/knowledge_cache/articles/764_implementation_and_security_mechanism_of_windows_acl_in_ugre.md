# Implementation and Security Mechanism of Windows ACL in UGREEN NAS

> **Article ID**: `764`  
> **Category**: `Application Guide > Files > FAQ > Implementation and Security Mechanism of Windows ACL in UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/764  

---

## Overview

The Access Control List (ACL) is a fine-grained permission management mechanism used to control access to objects in a system, such as files, folders, or applications. Each ACL consists of multiple access control entries (ACE), with each entry defining the type of permissions (e.g., read, write, delete, or manage) granted to a specific user or user group.

UGREEN NAS fully supports the Windows ACL permission model. Administrators can use the user management feature in UGREEN NAS to configure independent storage quotas, access speed limits, and access permissions for different users or user groups. This ensures flexible multi-user collaboration while maintaining a high level of security.

In addition, each user has an independent "Home" folder. The system automatically applies ACL rules to isolate data access between users, ensuring privacy and security.

## Terminology

|  |  |
| --- | --- |
| **English Full Term** | **Definition** |
| Access Control List(ACL) | A list that defines the security attributes of an object, such as files, directories, or processes. An ACL consists of multiple ACE entries. |
| Access Control Entry(ACE) | The basic unit within an ACL. It defines the access permission and inheritance properties of a security principal (a User or User Group). |

## Customizing Windows ACL Permissions

UGREEN NAS provides a graphical permission management interface, allowing administrators to configure access control for users, user Groups, or shared folders in the following ways.

**Edit User Permissions:**

1. Open the [Control Panel] app, and go to [User Management] > [User].

2. Right-click the target User and select **"Edit"**.

3. Click the **"Permission & Settings"** tab to set the User's access level for the Shared Folder:

● Access denied: The user cannot access the folder or its subfolders.

● Read only: The user can view but cannot modify or delete content.

● Read/Write: The user can read, modify, delete, or create files.

4. Click **"Save"** to complete the configuration.

**Edit User Group Permissions:**

1. Open the [Control Panel] app, and go to [User Management] > [User Group].

2. Right-click the target user group and select **"Edit"**.

3. Click the **"Permission & Settings"** tab to configure the user group's access level for shared folders (access denied / read only / read/write).

4. Click **"Save"** to complete the configuration.

**Edit Shared Folder Permissions:**

1. Open the [Files] app and click **"Shared Folder"** in the sidebar.

2. Right-click the target folder and select **"Properties"**.

3. Click the **"Permission"** tab to configure access permissions for administrators, standard users, and user groups.

4. Check or uncheck the corresponding permission boxes for each user or user group, then click **"OK"** to save the settings.

## Viewing Windows ACL Permissions

In the NAS terminal, you can use the **ugacltool** command to view the ACL permission configuration of the current directory or file. For example:

```
ugacltool get test.txt
```

Example Output:

![](https://file-us.ugreennas.com/admin/article/2025-10-14/d6640a779cf04ecc8ec2cf427621c55c.webp)

The above example contains four access control entries (ACE):

● **admin(group)**: Read/Write

● **u1**: Read/Write

● **user2**: Read/Write

● **user3**: Read only

## Description of ACL Permission Bits

UGREEN NAS supports configuring ACL permissions for the following six roles and recognizes 13 permission bits (rwxpdDaARWcCo) and four inheritance attributes (fdin).  
`[user | group | owner | everyone | authenticated_user | system]`

### Permission Bits (13 Types)

|  |  |  |
| --- | --- | --- |
| **Symbol** | **Meaning** | **Description** |
| r | read data | Read file content |
| w | write data | Write or create files |
| x | execute | Execute files |
| p | append data | Create directories |
| d | delete | Delete the current file |
| D | delete child | Delete files within a directory |
| a | read attribute | Read extended attributes |
| A | write attribute | Write extended attributes |
| R | read xattr | Reserved |
| W | write xattr | Reserved |
| c | read acl | Read ACL |
| C | write acl | Modify ACL |
| o | ownership | Change ownership (can only be set to oneself) |

### Inheritance Attributes (4 Types)

|  |  |  |
| --- | --- | --- |
| **Symbol** | **Meaning** | **Description** |
| f | file inherited | File inheritance |
| d | directory inherited | Directory inheritance |
| i | inherit only | Used only for inheritance, not for authentication |
| n | no propagate | Do not propagate multiple levels of inheritance, only inherit the next level |

## Permission Inheritance Mechanism

1. **Automatic Inheritance**

Subobjects automatically inherit the ACL permissions of their parent directory by default. For example, if folder `Directory A`grants user `Mike` "Read" permission, all files within that folder will automatically allow `Mike` to access them.

2. **Dynamic Updates**

When the permissions of a parent directory are modified, the system automatically synchronizes and updates the permissions of its subfolders and files.

If a user manually modifies file permissions using the `chmod` command, ACL inheritance will still take effect again after the system restarts or when synchronization occurs.

## Security Mechanism of Windows ACL and Linux Permissions

When viewing shared folders in the NAS terminal using the ls or stat command, you may notice that file permissions appear as 777 (i.e., rwxrwxrwx).

This does not indicate a security risk—it is a deliberate design for compatibility and security.

![](https://file-us.ugreennas.com/admin/article/2025-10-14/1daf607013a9425e96f32b7307ee8d0c.webp)

1. **Compatibility Differences**

The Windows ACL model differs structurally from the traditional Linux permission model (owner/group/others), and the two cannot be mapped one-to-one.

UGREEN NAS displays permissions as 777 to ensure that all access control logic is managed exclusively by the ACL layer.

2. **Windows ACL and SSH Permission Verification Mechanism**

When a directory or file is managed by Windows ACL, the system determines access rights based on ACL permissions, rather than relying on traditional Linux permissions. In this case, running ls -l will display 777 (rwxrwxrwx), which is an intentional design for compatibility and security.

If you store your SSH public key file in a shared folder and attempt to log in to the NAS, the directory is managed by Windows ACL. Although the Linux layer shows the permissions as 777, the sshd service will detect that the key's permissions are overly permissive during its pre-login security check and will refuse authentication.

This is not a kernel-level access denial—it is an intentional security measure by the SSH service to prevent unsafe logins.

Therefore, files within shared folders displaying 777 permissions do not represent a security vulnerability. On the contrary, this mechanism prevents misplacement and misuse of sensitive key files in shared directories, offering a safer and more reliable design choice.

3. **Security Recommendations**

SSH Login Keys: Store your SSH keys in the personal ~/.ssh directory under your User's Home folder.

Docker Keys: You may store Docker-related keys in the /root directory or a custom secure directory.

Please avoid storing any sensitive credentials or key files in shared folders.

## Administrator SSH Login and ACL Verification Mechanism

For accounts that belong to the **admin user group** (administrators):

● When logging in via SSH key authentication, the system verifies only the ACL entries related to the user and the admin user group.

● If additional ACL rules are detected (e.g., other users or user groups are added to the same directory), the SSH login will be denied.

● This design ensures the security and uniqueness of SSH public key authentication.
