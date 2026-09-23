# Folder Management

> **Article ID**: `770`  
> **Category**: `Application Guide > Files > Folder Management`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/770  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: NAS Firmware 1.18.0.0032 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

The Files app supports managing Personal Folders and Shared Folders. With folder management features, you can adjust folder locations, capacity limits, access permissions, and encryption settings.

Administrators can centrally manage different users or shared directories based on actual usage scenarios.

## Accessing Folder Management

1. Open the Files app and click "**Management**" in the top bar.

2. Select "**User Folder management**" or "**Shared folder management**" as needed.

## User Folder Management

Administrators can manage User Folder in the **Files** app. User Folder is a personal space belonging to the corresponding user. This folder does not support setting sharing permissions.

On the User Folder Management page, the following operations are supported:

● Change the storage location of User Folder.

● Enable or disable Personal Folder for users.

● Set full rights.

● Set capacity quota.

● Edit User Folder information.

● Enable User Folder encryption.

### Access Path

Open the Files app, click "**Management**" in the top toolbar＞"**User Folder management**".

![](https://file-us.ugreennas.com/admin/article/2026-08-07/6b57a8023cc44be2a76db368b14307f4.webp)

### Page Description

After entering the **User Folder management** page, you can view the list of User Folder on the current device. The page includes the following information:

● **Name**: Displays the user name.

● **Personal Folder**: Used to enable or disable Personal Folder for the user.

● **Full rights**: Allows users to set whether their Personal Folder is hidden from other users.

● **Quota**: Sets the maximum capacity available for the user's Personal Folder.

● **Actions**: Enter the edit page to view or modify User Folder settings.

At the top of the page, you can select the unified "**Storage location**" for User Folder.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/52728ae94c85481781d706883a804338.webp)

### Enable or Disable Personal Folder

In the user list, you can control whether a user has Personal Folder enabled through the "**Personal Folder**" option.

When enabled, the user can use their own Personal Folder.

When disabled, the user can no longer use their Personal Folder.

### Set Full Rights

After enabling "**Full rights**", regular users can set whether their Personal Folder is hidden from other users.

If a user enables the hide setting, other users will not be able to view the user's Personal Folder.

Note: If a user has enabled the option to hide their Personal Folder from other users, the administrator cannot perform some management operations on the user's folder, such as enabling encryption. Please refer to the actual page prompts.

### Set Quota

You can set the maximum capacity of a user's Personal Folder in "**Quota**". Enter the capacity value and select a unit, such as **GB**. If no capacity limit is required, leave the field blank.

Before setting a quota, ensure that the target Volume has sufficient available capacity. The quota cannot exceed the available capacity of the Volume.

### Edit User Folder

To view or edit a User Folder, click "**···**" on the right side of the user ＞ "**Edit**". After entering the edit page, you can view the following information:

● Name

● Location

● File size

● Recently modified

● Creation time

![](https://file-us.ugreennas.com/admin/article/2026-08-07/bff2a90b535c4ca089e867bb25c568dd.webp)

### Encrypt User Folder

On the Edit user folder page, switch to the "**Encryption**" tab to enable encryption for the User Folder. Follow the steps below:

1. Find the target user in the User Folder list.

2. Click "**···**" on the right side ＞ "**Edit**".

3. Switch to the "**Encryption**" tab and click "**Enable encryption**".

![](https://file-us.ugreennas.com/admin/article/2026-08-07/ff0a2c0906924ef396aeb7694e1c9709.webp)

4. Set the key and click "**Save**".

![](https://file-us.ugreennas.com/admin/article/2026-08-07/f427a7694fd14d1ba5d01082f0950e58.webp)

The system will automatically generate a key file and download it to the local device. If the key is forgotten and the key file is lost, the User Folder cannot be decrypted or mounted, and the data cannot be recovered.

## Shared Folder Management

Administrators can manage Shared Folder in the Files app. Shared Folder is designed for multiple users to share and collaborate. On the Shared Folder Management page, administrators can create, edit, delete, and mount Shared Folder, as well as configure permissions, NFS permissions, capacity limits, and folder encryption.

### Access Path

Open the Files app, click "**Management**" in the top toolbar＞"**Shared folder management**".

![](https://file-us.ugreennas.com/admin/article/2026-08-07/3dbdc673dbba4d97b2a249bd9eb29c22.webp)

### Page Description

After entering the **Shared folder management** page, you can view the list of Shared Folder on the current device. The page includes the following information:

● **Name**: Displays the name of the Shared Folder.

● **Size**: Displays the used capacity of the Shared Folder.

● **Storage location**: Displays the Volume where the Shared Folder is located.

● **Capacity limit**: Displays the capacity limit set for the Shared Folder.

● **Network visibility**: Displays whether the Shared Folder is visible in the network browsing entry on the local network.

● **Actions**: Provides access to operations such as editing, deleting, and mounting the Shared Folder.

The top of the page supports creating, searching, and sorting. You can quickly find a Shared Folder using the search box, or sort Shared Folder by name.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/90c2580849fe4ddda8cb3499bebd96c4.webp)

## Create Shared Folder

1. Go to the "**Shared folder management**" page and click "**New folder**".

2. Follow the on-screen instructions to enter the Shared Folder name, select the storage location, set the capacity limit and related options, and configure access permissions.

3. Click "**Create**".

After creation, the Shared Folder will be displayed in the Shared Folder list.

### Manage a Single Shared Folder

In the Shared Folder list, find the target Shared Folder and click "**···**" on the right side to expand the operation menu. The following operations are available:

● **Edit**: Enter the Shared Folder configuration page.

● **Delete**: Delete the Shared Folder.

● **Mount**: Mount an unmounted encrypted Shared Folder.

If a Shared Folder is encrypted and currently unmounted, a lock icon will be displayed in the list. The Shared Folder must be mounted before it can be accessed in the Files app.

### Edit Shared Folder

Click "**···** " on the right side of the Shared Folder ＞ "**Edit**" to enter the Shared Folder editing page. The editing page includes the following tabs:

● **General**

● **Permission**

● **NFS Permission**

● **Encryption**

### General Settings

In the **General** tab, you can view or modify the basic information of the Shared Folder. The page includes the following settings:

● **Name**: Displays the name of the Shared Folder. To modify the name, edit it on this page.

● **Storage location**: Displays or changes the Volume where the Shared Folder is located. To migrate the Shared Folder to another Volume, adjust the storage location here. Before migration, ensure that the target Volume has sufficient available capacity.

● **Location**: Displays the system path of the Shared Folder. For example `/volume1/Babyalbum`, where `volume1` indicates that the folder is located in Volume 1.

● **File size**: Displays the current capacity usage of the Shared Folder, as well as the number of files, subfolders, and hidden items it contains.

● **Recently modified**

● **Creation time**

● **Capacity limit**: When enabled, limits the maximum capacity that can be used by the Shared Folder. The set capacity limit cannot be lower than the current used capacity and cannot exceed the available capacity of the target Volume.

● **Hide in** "**Network**"**:** When enabled, the Shared Folder will not be displayed in the "**Network**" browsing entry on computers in the local network.

● **Hide subfolders and files from users who do not have permissions**: When enabled, users without access permissions cannot view subfolders and files within the Shared Folder. It is recommended to enable this option when multiple users share the NAS to reduce exposure of unauthorized content.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/38a3d361290743908a019d0f9424606a.webp)

### Set Shared Folder Permissions

In the "**Permissions**" tab, you can set access permissions for users on the device. The following permissions are supported:

● **Deny access**

● **Read/Write**

● **Read-only**

The page displays the administrator and regular user lists. You can set permissions for different users based on actual requirements.

### Permission Application Method

After modifying permissions, you can select the permission application method at the bottom of the page.

**Merge**: Sync changes to subfolders while retaining the existing permissions set for subfolders. This option is suitable when you only want to add or synchronize specific permissions while keeping the original permissions of subfolders.

**Overwrite**: Overwrite all permission settings for subfolders. This option is suitable when you need to apply unified permissions to the entire Shared Folder and its subfolders.

**None**: Modify permissions for the current folder only. Permissions of subfolders and files will not be changed by this operation.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/6924d18b569b42079834e84ea6bf960c.webp)

### Set NFS Permissions

In the **NFS Permissions** tab, you can configure NFS access rules for the Shared Folder. The following operations are supported:

● **Add**

● **Edit**

● **Delete**

The NFS permissions list includes the following fields:

● **Client**

● **Permission**

● **Squash**

● **Async**

● **Non-privileged port**

The mount path of the Shared Folder is displayed at the bottom of the page. For example,`/volume1/Babyalbum`. You can add NFS permission rules based on the client device and access requirements.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/0efbf027794a45b09a406a132257c3c2.webp)

**Note**: Encrypted Shared Folder with the Btrfs file system cannot be accessed through NFS sharing.

### Encrypt Shared Folder

In the "**Encryption**" tab, you can enable encryption for the Shared Folder. Follow the steps below:

1. Open the Shared Folder editing page, switch to the "**Encryption**" tab, and click "**Enable encryption**".

2. Set the key and save it according to the on-screen instructions.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/74ef6115531a4901aeed4f848af27bc5.webp)

After encryption is enabled, the system will generate a key file and automatically download it to the local device.

If the key is forgotten and the key file is lost, the Shared Folder cannot be decrypted or mounted, and the data cannot be recovered.

## Related Reading

### Folder Encryption

<https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmOTEyIiwiY2xpZW50VHlwZSI6IlBDIn0=>
