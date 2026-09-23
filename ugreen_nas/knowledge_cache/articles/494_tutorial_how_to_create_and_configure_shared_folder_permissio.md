# [Tutorial] How to Create and Configure Shared Folder Permissions?

> **Article ID**: `494`  
> **Category**: `Application Guide > Files > FAQ > [Tutorial] How to Create and Configure Shared Folder Permissions?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/494  

---

This tutorial provides a detailed guide on how to create shared folders on UGOS Pro, set their access permissions, and configure NFS (Network File System) permissions.

## Create a New Shared Folder

![](https://file-us.ugreennas.com/admin/article/2025-09-10/133958913ad34c809bc3243edf30a393.webp)

1. Open [Files], click the "`+`" icon in the toolbar, and select "Create a New Shared Folder".

2. In theNew Shared Folder window, configure the folder settings:

● **Folder Name**:

Specify a name with 1 to 64 characters that meets the following conditions:

● Does not start or end with a space.

● Does not contain consecutive spaces.

● Does not include the following characters:`` " + = / : | * ? < > ; [ ] % ` '. ``

● **Storage Location**: Select the storage space for the shared folder. Set a storage limit if needed and decide whether to hide the folder in "Network".

● **Enable Recycle Bin**: The recycle bin is enabled by default, with access restricted to administrators only.

3. Click "Create**"** to open the [**Shared folder permission configuration**] window. Specify the access permissions for users on this UGREEN NAS device and configure whether to hide subfolders and files from unauthorized users.

4. Click "OK" to complete the operation.

## To Configure Shared Folder Permissions

You can specify which users or user groups can access, view, or modify the shared folder and its contents. Permissions can be customized for the shared folder, individual files, and subfolders. To configure advanced permission settings for individual users, you need to enable shared folder permissions in **[****Control Panel > User Management > User > Edit > Permissions and Settings]**.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/57fa628df5504d34b31bc7be6d89215c.webp)

### To Specify Permissions for Shared Files and Folders

1. Open Files and select the target shared folder or file.

2. Right-click and choose [**Properties]**. when the Properties window pop up, click **"permissions"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/b13e4b428fd14dceac106de71289c1a1.webp)

3. Configure permissions for administrator users, general users, or user groups by selecting the following options:

● Access Denied: Users or user groups cannot access files or subfolders within the shared folder.

● Read/Write: Users or user groups can access and modify files and subfolders within the shared folder.

● Read only: Users or user groups can access files and subfolders but cannot modify them.

**Optional:** Hide subfolders and files from unauthorized users when accessing the folder via Files or SMB.

4. Click "OK" to finalize the configuration.

**Notes:**

1. When there is a conflict between the permissions assigned to a user and the permissions of their user group, the permissions will be determined based on the following priority order: Access Denied > Read/Write > Read Only. For example, if a user group's permission is set to **Read Only**, but a user within the same group is assigned **Access Denied**, the user's access will be set to **Access Denied**.

2. When creating a new shared folder, if the permission for users belonging to the administrator group is set to **Access Denied**, these users will only be able to see the shared folder directory in [Files > Shared Folder], without any permission to access or modify the folder.

## To Configure NFS Permissions for a Shared Folder

**NFS (Network File System) permissions** allow you to define which client computers and users can access shared folders on your NAS via the NFS protocol. This is commonly used in Linux environments, including distributions such as CentOS and FreeBSD.

### Steps to Set NFS Permissions

![](https://file-us.ugreennas.com/admin/article/2025-09-10/293271af3e2540c8a8ff12ab2c63933b.webp)

1. Select the target shared folder in the shared folder directory that you want to configure.

2. Right-click "Properties" to open the [Properties] window and select "NFS Permissions".

3. Click "Add" to open the [Add NFS Rules] window. Define the following options:

4. Server Address: Enter the IP address of the NFS client that will access the shared folder. You can fill in this field in any of the following ways:

● Domain name or IP address: Fully qualified domain name or IP address.

● Wildcard: \*, \*.ugreen.com

● Network segment: 172.14.10.2/255.255.252.0, /24

5. Permission: Select the NFS client’s Read/Write access permission.

6. Squash: This field allows you to control NFS client user access. Choose one of the following actions:

No Mapping: Allows all NFS client users (including the root user) to retain their original access privileges.

Map all users to admin: Assigns access privileges to all NFS client users equivalent to the admin user in your system.

7. Security: Specify the type of security to implement.

**AUTH\_SYS**: Uses the NFS client’s UID (User Identifier) and GID (Group Identifier) to verify access privileges.

8. Enable Asynchronous: Check this option to allow your UGREEN NAS to respond to NFS client requests before completing file changes, improving performance.

[Additional Note]– Sync vs. Async: This controls how data is written. Sync mode ensures data is immediately written to disk, improving data safety. Async mode temporarily stores data in cache and writes it in batches, improving performance but increasing the risk of data loss.

9. Allow connections from non-privileged ports (greater than 1024): Check this option to allow NFS clients to connect to the UGREEN NAS using non-privileged ports (i.e., ports greater than 1024).

10. Click "OK" to complete the configuration.

11. Click "OK" to apply the NFS permissions.

You can go to [Properties > NFS Permissions] to edit or delete the NFS permission settings.

**Notes:**

1. When the server name format is \*.domain, the NFS client’s IP address must have a corresponding DNS PTR record so that the UGREEN NAS can resolve the same \*.domain name by reverse lookup.

2. When using a specific user account to access the shared folder via NFS: If the **AUTH\_SYS** security type is selected, the client must have identical UID (User Identifier) and GID (Group Identifier) values on both the NFS client and the UGREEN NAS. Otherwise, access permissions will be assigned as **others**. To avoid any permission conflicts, you can choose [Map all users to admin] in Squash.

3. If the file system of the external device where the shared folder was created is NTFS or FAT, the [Map all users to admin] option will be forcibly applied.
