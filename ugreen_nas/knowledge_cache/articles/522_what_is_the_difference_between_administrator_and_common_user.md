# What is the difference between administrator and common user permissions?

> **Article ID**: `522`  
> **Category**: `Application Guide > Control Panel > FAQ > What is the difference between administrator and common user permissions?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/522  

---

In the UGOS Pro system, user roles are divided into two types: administrator and common user, each with different permission scopes. Understanding these differences helps in assigning roles appropriately when adding new users.

* Administrator: Has full system management permissions, including but not limited to user management, system configuration, and security settings. Administrators can perform all operations to ensure the proper functioning and administration of the system.
* common user: Limited to accessing authorized apps, shared folders, and personal folders. They do not have permission to make system-level changes or manage other users. This role is suitable for everyday use and focuses on individual needs.

Clearly distinguishing between these two roles and their respective permissions ensures system security and efficient operation. When creating a new account, please choose the appropriate role type based on actual needs.

## **Administrator vs Common user**

|  |  |  |
| --- | --- | --- |
| **Scope of Application** | **Administrator** | **Common user** |
| Storage Space | * Can access all storage spaces; newly created storage spaces are automatically available. * No quota is set by default, but custom quotas can be assigned to individual accounts as needed. | Limited to using storage space in personal folders and authorized shared folders; quotas are set by the administrator. |
| File Management | Has full management privileges, including access to all folders, even those of other users (both administrators and common users), and can assign permissions to other users. | Can only manage personal folders and authorized shared folders. |
| File Sharing Protocols | In [Control Panel]> [File Services], protocols such as SMB, FTP, NFS, rsync, and WebDAV can be enabled. These settings apply system-wide. Once enabled, file visibility can be customized for each account. | After the service is enabled, the visible file scope for the current account’s file sharing protocol connections can be configured. |
| App Center | * Can install or uninstall applications via the App Center. * Has full access to all applications and their settings. * For apps with role settings, can add, remove, or modify permissions for others. * Can manage data across all applications. | * Can use some applications, but usage is restricted by administrator settings. * Cannot add or delete other users, nor modify permission settings. * Can only view and manage data for which they have permission within applications. |
| External Storage Devices | * Can view data on connected USB drives or external hard disks via [Storage] > [External Storage] and can safely eject devices. * You can configure whether to allow common users to access files on external storage devices by default (including USB storage devices and external storage arrays) via [Storage] > [External Storage] >[Advanced Settings]. | Common users can access external storage files only if allowed in [Storage] > [External Storage] > [Advanced Settings]. |
| Remote Mounting of Other Devices and Cloud Drives | * You can mount folders or cloud drives from remote devices via [File Management] > [Network Folder]. Each user can only see the folders they have mounted and cannot view folders mounted by other users. * You can view all users’ device connection information via [Cloud Tools] > [Overview]. | * When mounting folders or cloud drives from remote devices via [File Management] > [Network Folder], users can only see the folders they have mounted and cannot see folders mounted by others. * Can only view their own device connection information via [Cloud Tools] > [Overview]. |
| SSH | You can enable the service via [Control Panel] > [Terminal > [SSH]. Once enabled, administrators will have access by default. | * Common users do not have access to this entry (SSH). |

**Related Reading**

[[FAQ] How to change a common user to an administrator user?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjoxNTE5LCJhcnRpY2xlSW5mb0lkIjo1MjEsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiMS4wIiwicGF0aENvZGUiOiIifQ==)
