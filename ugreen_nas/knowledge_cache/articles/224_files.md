# Files

> **Article ID**: `224`  
> **Category**: `Application Guide > Files > Files`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/224  

---

**Applicable Version**: UGOS Pro 1.18.0.0002 or later.

The screenshots and options in this document are for reference only. The actual display may vary by system version, app version, or device model, Please refer to the actual interface.

# Introduction

The Files app helps you easily organize, browse, and categorize all your files. It provides a variety of practical features, including file sharing, file collection, folder permission management, connecting to network folders, duplicate file detection, and creating desktop shortcuts for files and folders. These features make file management more efficient, secure, and convenient.

## Files Interface

The Files app consists of three main sections: the left navigation pane, the top toolbar, and the file list.

### Left Navigation Pane

The left pane displays storage resources and quick access entries available to the current account. You can expand, collapse, or switch between different directories from the left navigation pane.

![](https://file-us.ugreennas.com/admin/article/2026-07-24/02254718523244f5ba0bea5f5cbe3a54.webp)

● **Favorites**: Displays favorited folders. To add a folder to Favorites, select the folder, right-click, and choose "**Create shortcut**" > "**Favorites**". After being added, the folder will appear in Favorites for quick access.

● **Personal Folder**: The Personal Folder is a private space for the current account and is accessible only by the current user by default.

● **Shared Folder**: Shared Folder stores files shared by teams or family members. Users with appropriate permissions can access, manage, and collaborate on files through this entry.

● **User Folder** (Administrators only): User Folder is visible only to administrators. Administrators can use this entry to view all personal folders created by users on the device. This entry is not displayed for regular users. If an administrator enables Full rights for a user, the user can choose whether to hide their Personal Folder from other users.

● **Network folder**: Network Folder displays remote folders mounted through file service protocols, such as SMB and WebDAV. After mounting, you can access files on other devices through this entry.

● **External Device**: When an external device, such as a USB hard drive, USB flash drive, or card reader, is connected to the NAS, it will be displayed here. Users can directly browse, copy, or move files on the external device.

● **Sharings**: Displays folders shared with the current user on the device. If other users share folders with you, you can access them through this entry.

● **Mount Image**: Displays the contents of mounted ISO images. You can right-click an ISO image file in Files and select "**Mount Image**". After mounting, the image contents will appear under "**Mount Image**". When finished, right-click the image and select "**Unmount**".

● **Tag**: Displays all color tag categories. You can add tags to files or folders. After adding tags, the system uses corresponding colors to identify them, making it easier to filter and find files later.

● **Settings**: Opens the Files settings page. Available settings may vary depending on the actual interface.

● **Recycle Bin**: Displays deleted files and folders. If a deleted file is still in Recycle Bin, you can open "**Recycle Bin**" and select "**Restore**" to recover it. After emptying Recycle Bin, files can no longer be recovered through Recycle Bin.

### Top Toolbar

After opening **Files**, you can quickly perform file operations from the top toolbar. The available toolbar functions may vary depending on the current directory, file type, and selection status. Some buttons are unavailable when no file is selected.

![](https://file-us.ugreennas.com/admin/article/2026-07-24/ca962279eef248af9c64d1c9d928adbf.webp)

**Create**: Click "**Create**" to add a folder in the current directory. You can also create a shared folder or connect a network folder.

**Upload**: Click "**Upload**" to select files from a local device and upload them to the current directory on the NAS.

**Copy, Paste, Cut, Rename**: Common editing operations. Select a file or folder to use these functions.

**Manage:** Click "**Manage**" to expand more advanced management features, including:

● User Folder management

● Shared folder management

● Sharing management

● File request management

● File deduplication

**Filter and Sort**: You can use Filter or Sort to adjust how files are displayed in the file list. For example, you can view files by file type, name, size, modification time, and other conditions. Available filter and sort options may vary depending on the actual interface.

**View**:Click "**View**" to switch between different file display modes. The following view modes are supported:

● **List**

● **Large**

● **Standard**

● **Thumbnail**

You can select a suitable view based on the number of files and your browsing preferences.

**Details**: Click "**Details**" to open or close the details pane. After selecting a file or folder, you can view related information in the details pane, such as the name, type, size, and modification time. The details pane also displays information such as the number of items in a folder. Available details may vary depending on the actual interface.

### File List Area

The file list area displays files and folders in the current directory. You can view information such as file name, size, type, and modification date, and perform operations such as sorting, filtering, uploading, and right-click actions.

**File Sorting**: You can click the column headers to sort files. By default, sorting is supported by the following fields:

● Name

● Size

● Type

● Recently Modified

To view more sorting options, click "**···**" on the right side of the list. You can sort files by creation date, recently accessed, tag, and other conditions. Available sorting options may vary depending on the actual interface.

![](https://file-us.ugreennas.com/admin/article/2026-07-24/f91e14d1ee3e452f84b67da3f65a6f38.webp)

**Selecting Multiple Files**: The file list supports multi-select operations for batch file management. You can select multiple files using the following methods:

● Hold the **Shift** key and select multiple consecutive files.

● Drag the mouse to select multiple files.

● Select multiple files using checkboxes, then perform batch operations.

After selecting multiple files, you can perform operations such as copying, moving, and deleting. Available operations may vary depending on the actual interface.

**Drag to Upload**: You can drag files from your local computer to the file list area. After releasing the mouse button, the files will be uploaded to the current directory. Before uploading, make sure you have write permission for the current directory. If you do not have permission, the upload may fail.

**Right-Click Menu**: Right-click a file or folder to quickly perform common operations. The available options in the right-click menu may vary depending on the file type, directory permissions, and selection status. Please refer to the actual interface.

## Files Features

In Files, you can right-click any file or folder to open the function menu and perform various operations.

![](https://file-us.ugreennas.com/admin/article/2026-07-24/0e0be0bbf993492b9b0f9f33fb826582.webp)

### Basic File Operations

The following section provides an overview of basic file operations. For detailed instructions, please refer to [Basic File Operations](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmMTQ2In0=) .

● **Open and Preview**: Click "**Open**" to preview file contents or enter a folder directly.

● **Upload**: Click "**Upload**" to upload files and folders from your local computer to UGREEN NAS.

● **Download**: Click "**Download**" to save files from the NAS to your current local device (computer or mobile device).

● **Copy and Cut**: Select "**Copy**" or "**Cut**", then paste the files to the target location.

● **Rename**: Click "**Rename**" to modify the name of a file or folder.

● **Delete**: Click "**Delete**" to move unwanted files to Recycle Bin.

● **Copy/Move to**: Use "**Copy**" or "**Move to** to" transfer files directly to a specified folder in the directory selection window.

● **Compress Files**: Select one or more files and click "**Add to compressed file**" to package them into a compressed file.

● **Decompress**: For compressed files, you can select "**Decompress**" to extract files to the current directory, or select "**Decompress to**" to extract files to a specified path.

● **Properties**: Select a file or folder, right-click, and choose "**Properties**" to view detailed information such as file size, path, and modification time.

● **Tag Files/Folders**: Add color tags to files or folders for easier classification and archiving.

● **Create Shortcut**: Click "**Create shortcut**" to add frequently used folder entries to "**Favorites**" or the desktop.

● **Move to Vault**: Enable Vault first, then click "**Move to Vault**" to move sensitive files to an encrypted space for protection. For details, see [Vault](https://support.ugnas.com/knowledgecenter/detail/article/en-US/673).

### Advanced File Management Features

● **User Folder management**: The system supports flexible configuration of users' personal folders.

● **Shared folder management**: The system supports creating and managing shared folders for team collaboration, with strict permission policies to ensure data security.

● **Sharing management**: This feature is designed for temporary file transfers or external sharing. You can centrally manage all generated sharing links here.

● **File request management**: This feature is designed for scenarios where files need to be collected from multiple users, such as collecting event photos, assignments, or documents.

● **File deduplication**: The system automatically detects and removes duplicate files in folders to help free up storage space.
