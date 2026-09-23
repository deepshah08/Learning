# Create New Folder

> **Article ID**: `139`  
> **Category**: `Application Guide > Files > Create New Folder`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/139  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: UGOS Pro Firmware 1.18.0.0093 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

Before using the "**Files**" app, make sure a Volume has been created. If no Volume exists on the device, the following message will appear when you open Files: `No volumes available on this device. Please go to "Storage" app to create before using`.

Go to "**Storage**" first to create a Storage Pool and Volume, then use the Files features.

## Create a Personal Folder

You can create a folder in the Personal Folder directory using the following methods:

### Via the Top Toolbar

1. In "**Personal Folder**", open the target directory where you want to create a folder.

2. Click the "**+**" button on the top toolbar and select "**Create folder**".

3. Enter a folder name in the pop-up window and click "**Confirm**".

![](https://file-us.ugreennas.com/admin/article/2026-08-18/985b4afdfaf147aeb37523401f65dca6.webp)

### Via the Right-Click Menu

1. In the target directory under "**Personal Folder**", right-click the blank area in the file list to open the menu.

2. Select "**Create**" > "**Folder**" from the menu.

3. Enter a folder name and click "**Confirm**" to create the folder.

![](https://file-us.ugreennas.com/admin/article/2026-08-18/bfbb1c95d9ab47b4b30595b4e3393ac9.webp)

## Create a Shared Folder

Only administrators can create shared folders. Follow these steps:

1. Under "**Shared Folder**", click "**+**" on the top toolbar＞"**Create shared folder**".

2. Enter a name for the shared folder, select the Volume where the folder will be stored, and configure the Volume usage limit and other options as needed.

3. Click "**Create**".

After the shared folder is created, the system will open the permission settings page.

![](https://file-us.ugreennas.com/admin/article/2026-08-18/a7697b0d764e48e5b45f05b24baa3535.webp)

## Set Shared Folder Permissions

After creating a shared folder, you need to set access permissions for different users or user groups. The default permissions are as follows:

● Administrators: Read/Write.

● Standard users: Deny access.

You can change the access permissions for users or user groups as needed. Available permissions include:

● Read/Write: Can view, upload, modify, and delete files.

● Read-only: Can view and download files, but cannot modify or delete them.

● Deny access: Cannot access the folder.

![](https://file-us.ugreennas.com/admin/article/2026-08-18/f89d415c8af64bb0b9bec0a0790d5543.webp)

## Page Options

**Hide in** "**Network**": When enabled, the shared folder will not appear when browsing the network. Enable this option if you do not want the shared folder to be discoverable by other devices.

**Hide subfolders and files for users without permissions**: When enabled, users without access permission cannot see the subfolders and files in the shared folder.

**Enable recycle bin**: When enabled, files deleted from the shared folder are moved to the recycle bin first. If a file is deleted by mistake, you can try to restore it from the recycle bin.

**Admin only**: This option restricts access to the recycle bin. When enabled, only administrators can access the contents of the shared folder's recycle bin.

**Encrypt folder**: When enabled, you can set encryption protection for the shared folder. When the folder is unmounted, users cannot access the data stored in it.

## Related Reading

● [Folder Encryption](https://support.ugnas.com/knowledgecenter/detail/article/en-US/912)
