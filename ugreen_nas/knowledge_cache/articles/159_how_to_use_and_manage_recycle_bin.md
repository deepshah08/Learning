# How to Use and Manage Recycle Bin?

> **Article ID**: `159`  
> **Category**: `Application Guide > Files > Recycle bin > How to Use and Manage Recycle Bin?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/159  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: NAS Firmware 1.16.0.0042 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

"**Recycle Bin**" is an important feature for preventing accidental data deletion. With Recycle Bin, you can easily restore accidentally deleted files from different directories, permanently clear files to free up storage space, and set up automatic cleanup schedules.

## How to Access Recycle Bin

On the PC client, there are two quick ways to access the "**Recycle Bin**":

1. **Desktop shortcut:** Click the "**Recycle Bin**" icon on the NAS system desktop.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/dc85b58da9f64ee6a37c7a4056256e28.webp)

2. **In-app entry:** Open the "**Files**" app. At the bottom of the sidebar, click the "**Recycle Bin**" icon.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/9658bfcdc6ac4afbb23a99018806f066.webp)

## Data Categories in Recycle Bin

In "**Recycle Bin**", deleted items are categorized by source in the sidebar, making them easier to manage across different storage locations:

● **Personal**: Stores items deleted from your "**Personal folder**".

● **Shared**: Stores items deleted from "**Shared folder**".

Note: The content visible here depends on your shared folder permissions.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/657215bedad74a969345d07b15adfda5.webp)

● **Users**: Only visible to administrators. Stores items deleted from the "**Personal Folder**" of all other users on the NAS.

### Top Bar

![](https://file-us.ugreennas.com/admin/article/2026-08-07/c76249e67fa649089331c131d14e6973.webp)

**Top search bar**: Enter a file or folder name directly in the search box at the top of the page to quickly search within the current category.

**View switch**: Click the view icon in the upper-right corner, such as list view or grid view, to change how files are displayed.

**Sort**: Click the sort icon in the upper-right corner to sort files in ascending or descending order.

### List Header

When "**Recycle Bin**" is displayed in list view, you can use the header above the list to adjust how file information is shown:

● **Sort in ascending or descending order**: Click a field name in the header, such as "**Modification time**", "**Size**", or "**Deletion time**", to sort all files in the current list in ascending or descending order. This helps you locate files more quickly.

● **Show or hide fields**: If the list shows too much information or is missing the information you need, click the "**⋮**" icon on the far right of the header. In the drop-down menu, select or clear additional fields such as "**Deletion time**" and "**Modification time**".

![](https://file-us.ugreennas.com/admin/article/2026-08-07/7ef5602e12ee49e5868ec0dc45a626a1.webp)

### Restore and Delete

![](https://file-us.ugreennas.com/admin/article/2026-08-07/81699499f765448a8e87a938ed62244f.webp)

● Click "**Empty all**" in the upper-right corner of the page to permanently delete all deleted files in the current category with one click. This action cannot be undone.

● Click "**Restore all**" to restore all files in the current category to their original locations.

### File Actions and Batch Operations

In the file list of "**Recycle Bin**", you can manage files just like you would on your local computer, using the right-click menu and keyboard shortcuts for faster operations.

**Right-click menu**

Select the target file, then right-click it to open the action menu. You can perform the following actions:

● **Open**: Preview or view the file in Recycle Bin. Some file formats are supported.

● **Restore**: Restore the file to its original location before deletion.

● **Delete**: Permanently delete the file. This action cannot be undone.

● **Download**: Save the file to the local drive of your current computer without restoring it.

● **Properties**: View detailed information about the file, such as its original location, size, and deletion time.

**Select multiple files with keyboard shortcuts**

When you need to process multiple files at the same time, such as restoring or permanently deleting them in batches, you can use native Windows/macOS shortcut behavior:

● **Ctrl key (Command key on Mac)**: Hold down the key and click files to select multiple **non-adjacent** files.

● **Shift key**: Click the first file, hold down the Shift key, then click the last file to select all files in between as a **continuous** range.

● After selecting multiple files, right-click any selected file to apply the same action to all selected files.

## Recycle Bin Management

Click the "**Settings**" icon in the lower-left corner of the page, then select "**Recycle Bin management**" from the pop-up menu to go to the Recycle Bin Management page.

This page is mainly used to manage Recycle Bin switches, permission settings, and storage cleanup for shared folders and user folders.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/323560a1e10f4c3fbc778da9d8aebe0f.webp)

### Manage Recycle Bin for Shared Folders

On the "Shared Folders" tab of the "Recycle Bin Management" page, you will see a list of all shared folders on the NAS.

1. **Batch Operations**

Click "Empty All" above the list. The system will clear all deleted files in the current category with one click.

2. **Settings for a Single Shared Folder**

To configure a single shared folder, click the icon on the right side of the folder name. You can perform the following actions:

![](https://file-us.ugreennas.com/admin/article/2026-08-07/768c9a03e50143c7826583add134b6a9.webp)

● **Empty Recycle Bin (trash icon)**: Deletes only the files in this folder's Recycle Bin.

● **Disable Recycle Bin (prohibited icon)**: Turns off Recycle Bin for this folder. After it is disabled, files deleted from this folder will be permanently deleted and cannot be restored.

● **Settings (gear icon)**: Sets whether only administrators are allowed to access and operate this shared Recycle Bin.

● **View Cleanup Plan**: If a cleanup plan includes this folder, the folder will display the cleanup time. Click this option to go to the cleanup plan list.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/872280c3eb4a432089b85f3330e88135.webp)

### Manage User Recycle Bin

Switch to the "**User Folder**" tab. Here, you can view the "**Recycle Bin**" of all users on the current NAS device.

1. **Batch Operations**

In the upper-right corner of the user list, the system provides two global actions. Use them with caution:

![](https://file-us.ugreennas.com/admin/article/2026-08-07/9435742f58d043509377696288d208e5.webp)

**Empty all:** Empty the files in all users' Recycle Bins with one click.

**Disable all:** After you click this button, the system will display a secondary confirmation warning. Once you confirm "**Disable**", the system will forcibly disable Recycle Bin for all users on the NAS and permanently delete all existing files in all users' Recycle Bins. After this action is performed, files deleted by any user cannot be restored.

**2. Manage a Single User**

If you want to view the storage usage of a specific user, click "**View size**" in the list for that user.

Click "**Empty Recycle Bin**" **(trash icon)** on the right side of the user to empty the deleted files in that user's Recycle Bin.

## Configure a Recycle Bin Cleanup Plan

To prevent files in Recycle Bin from gradually taking up NAS drive space when it is not cleaned for a long time, the system provides a "**Cleanup Plan**" feature. By setting predefined automation rules, the system can automatically empty files at the specified frequency and time without manual operation, helping storage space be freed up and reused more efficiently.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/0599fcba45e74ae89f380c8c5dd17af9.webp)

### Create a Cleanup Plan

1. On the Recycle Bin page, click the "**Settings**" icon in the lower-left corner. In the pop-up menu, select "**Cleanup Plan**".

2. On the Cleanup Plan page, click "**+ New plan**" to open the configuration window.

3. Based on your actual needs, choose to clean up "**All**" folders, or select specific folders.

4. Select the cleanup mode you need. After configuring the execution time and cleanup frequency, click "**Confirm**" at the bottom to save and enable the automated task.

### Manage or Delete Cleanup Plans

As your storage strategy changes, you may need to discard or adjust existing automated plans.

1. Go to the Recycle Bin Cleanup Plan page again. The list will show all currently enabled tasks.

2. Find the plan task you want to delete, then click "**Delete**" on the right side of the item. To modify the rule, click "**Edit**".

3. A secondary confirmation pop-up will appear. Click "**Confirm**" in the pop-up to delete the plan.

## Comparison of the Two Cleanup Modes

When creating a cleanup schedule, the system provides two automatic cleanup triggers. You can choose the one that best fits how often files are generated.

### Auto Cleanup

● **How it works**: Runs on a fixed daily cycle.

● **Configurable options**: Cleanup frequency, such as deleting only files that have been kept in Recycle Bin for **more than X days**, and the specific time of day to run the cleanup, such as 12:00 every day.

● **Recommended for**: Folders that frequently generate temporary files or downloads. This helps keep storage usage under control every day.

### Scheduled Cleanup

● **How it works:** Supports longer-term planning and can run **by day** or **by month**.

● **Configurable options:** Cleanup frequency, by day or by month, and the first execution time, which can be set to a specific future date and time.

● **Recommended for:** Daily office documents and shared folders that require monthly cleanup or archiving, giving team members **enough time to restore files** deleted by mistake.

## Show or Hide Folder Recycle Bin

To make it easier to restore recently deleted files while browsing a specific folder, the system provides a "**Folder Recycle Bin**" display switch. You can choose whether to show a dedicated recycle bin entry inside each folder based on your personal preference for a cleaner interface.

### Steps

1. On the Recycle Bin page, click the"**Settings**" icon in the lower-left corner. In the pop-up menu, find the "**Show Recycle Bin of this directory**" option.

2. You can turn this option on or off as needed.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/7b3e0bb20ac44b8d8b70b9cc131daabf.webp)

### Folder Recycle Bin Display and Behavior

This feature is enabled by default.

1. **When Enabled**

When this feature is enabled, the system automatically creates and displays a quick Recycle Bin entry in the root directory of each folder.

**Display location:** It appears in the root directory of "**Personal Folder**" and in the root directory of each "**Shared Folder**".

![](https://file-us.ugreennas.com/admin/article/2026-08-07/0f9f8a13011e4063af37cb67670392b7.webp)

2. **When Disabled**

If you prefer a cleaner file browsing view and do not want to see additional system icons, you can disable this feature.

After it is disabled, the quick Recycle Bin entry in the root directory of all folders will be hidden.

Disabling this switch does not affect the underlying Recycle Bin mechanism. You can still go to "**Recycle Bin**" in the "**Files**" app to view and manage all deleted files in one place.

## Recycle Bin Permissions and Visibility Rules

To protect data privacy and system security in a multi-user environment, the content visible in Recycle Bin and the actions available are strictly separated based on the role of the currently signed-in account, either administrator or regular user, as well as folder permissions.

### Administrator-only Features

For secure system-level storage management, only administrators have access to global configuration options. Regular users will not see "**Cleanup plan**", "**Recycle Bin Management**" or "**Settings**" on the "**Recycle Bin**" page. This helps prevent regular users from accidentally deleting global system configurations or affecting other users' data.

### Permission Inheritance for Shared Folders

On the **"Shared"** tab, Recycle Bin visibility strictly follows the underlying permission settings of each shared folder:

● **Regular users:** You can only see deleted files from a shared folder in Recycle Bin if you have "**Read-Write**" or "**Read-only**" permission for that folder. If your permission is set to "**No Access**", deleted files from that folder will not be visible to you.

● **Administrators:** Administrators have "**Read-Write**" permission by default and can view and manage Recycle Bin files generated from all shared folders.

## FAQ

**Q: Can I copy the path of a Recycle Bin file and paste it into the address bar to open it?**

No. Recycle Bin is a special system directory and does not support access by "**copy path + paste into the address bar**". Please perform the operation directly in the "**Recycle Bin**" interface.
