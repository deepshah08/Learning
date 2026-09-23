# Basic File Operations

> **Article ID**: `146`  
> **Category**: `Application Guide > Files > Basic File Operations`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/146  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: NAS Firmware 1.18.0.0093 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

The "**Files**" app provides comprehensive and efficient file management capabilities. You can easily transfer, organize, archive, and share files.

## Uploading and Downloading

### Uploading Files or Folders

The system offers three convenient upload methods:

● **Method 1**: **Right-Click Upload**

Select the target folder in the left directory pane, then right-click in the blank area of the right pane and choose "**Upload to ‘XXX’**". Specify the file or folder you wish to upload.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/ba9f3d477a9b4bff92a4d3c09b9ca877.webp)

● **Method 2**: **Toolbar Button**

Navigate to the target folder and click the "**Upload**" button in the upper-left corner of the interface.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/bd1ebc3f0e0a4bef8e014d0992ebf5d3.webp)

● **Method 3**: **Drag-and-Drop Upload**

Drag files directly from your local computer into the desired area within Files. The system allows you to configure the default handling of duplicate filenames during drag-and-drop uploads under "**Settings**">"**General**".

![](https://file-us.ugreennas.com/admin/article/2026-08-07/a71ef8fb91744db6a18b099df14b940a.webp)

### Duplicate Filename Handling Strategies

● **Overwrite**: Replace the existing file with the same name.

● **Skip**: Keep the original file and cancel the current upload.

● **Keep**: Retain the original file; the new file will be automatically renamed as "**Filename (1)**".

### Downloading Files

● **Operation**: Select one or more files (hold Shift or Ctrl for multi-selection), right-click, and choose "**Download**".  
The files will be saved to your browser’s default download location.

### Task Monitoring and Logs

Click the "**Task Center**" icon in the top-right corner of the system desktop to view the real-time transfer progress and speed.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/f614904bb45544ec91870893ebfe2119.webp)

It is recommended to "**Enable file logs**" in "**General**" under Files Settings. This allows the system to record file operations, such as copying, deleting, and uploading files.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/c5eff9994f75428da08b1d03600644e0.webp)

## File Management

### Renaming

**Single Rename**: Right-click a file and select "**Rename**" icon, or select the file and click the "**Rename**" button on the toolbar.

### Batch Rename

Files supports batch renaming, allowing you to modify the names of multiple files at once using methods such as Find/Replace, Number format, Add content, and Edit manually.

Before batch renaming, the system displays the original and new file names for review. After confirming that everything is correct, click "**Rename**" to apply the changes.

**Operation Entry**:

1. Open "**Files**" and go to the directory where the files are located.

2. Select the files you want to rename in batches, right-click the files, and select "**Rename**".

The Batch rename window supports the following methods:

● **Find/Replace**

● **Number format**

● **Add content**

● **Edit manually**

**Find/Replace**:

This method is suitable for replacing specified text in file names with new text in batches. Follow the steps below:

1. Enter the keyword to be replaced in **Search**.

2. Enter the new keyword in **Replace with**.

3. Preview the **After** **modification** file names below.

4. After confirming the changes, click "**Rename**".

To replace file extensions, select "**Allowing to replace file extensions**".

**Note**: Changing file extensions may prevent files from opening properly. Unless required, replacing file extensions is not recommended.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/de149b181c19459289715888ba1a8415.webp)

**Number format**:

This method is suitable for renaming multiple files with sequential numbers. You can configure the following options:

● **Number type**: Select the numbering format, such as Arabic numerals.

● **Start number**: Set the number to start the sequence.

● **Prefix**: Add fixed text before the number.

● **Suffix**: Add fixed text after the number.

After configuration, the system displays a preview of the modified file names below. After confirming the changes, click "**Rename**".

**Example**: Files can be renamed sequentially as **1.zip**, **2.xlsx**, **3.xlsx**, and so on.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/4686aa29e62f4791918459dc23d725af.webp)

**Add content**:

This method is suitable for adding text to specified positions in file names in batches. You can configure the following options:

● **Type**: Select the type of content to add.

● **Location**: Select where to add the content, such as before the file name or at other positions.

● **Add content**: Enter the text to be added.

After completing the settings, preview the **After** **modification**.After confirming the changes, click "**Rename**".

![](https://file-us.ugreennas.com/admin/article/2026-08-07/c2754adabe8d442195cdaa1e3115d7ae.webp)

**Edit manually**:

This method is suitable for scenarios where multiple files need to be renamed individually. Follow the steps below:

1. Switch to "**Edit manually**".

2. Edit the file names one by one in the **After modification** list.

3. After confirming the changes, click "**Rename**".

Edit manually does not automatically apply any renaming rules. It is suitable for cases where file names vary significantly and each file needs to be reviewed individually.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/abf1a39c06eb4f01bd8eaf3941291818.webp)

### Copy and Move

**Methods**:

● **Menu operations**: Select files, then select "**Copy/Cut**" from the toolbar or right-click menu. Go to the destination location and select "**Paste**".

● **Shortcut keys**: Supports standard shortcuts on Windows (Ctrl+C/X/V) and macOS (Command+C/X/V).

● **Specified destination**: Right-click and select "**Copy to**" or "**Move to**", then select the destination location directly from the directory tree in the pop-up window.

**Notes**：

● **Within the same Volume**: The operation is completed very quickly because it only involves changing the logical path.

● **Across different Volumes**: The operation is slower because it requires physical data transfer. For large files, it is recommended to process them in batches.

### Delete Files

1. Open the Files App and locate the file or folder you want to delete.

2. Right-click the file or folder, select "**Delete**", and confirm the operation as prompted.

After deletion, the file will be moved to the Recycle Bin.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/df827df489be40f284d39628d28c324b.webp)

### Restore Files from Recycle Bin

1. Open the Files App and find "**Recycle Bin**" at the bottom of the left directory panel.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/1574e468025f40a7a8c5d53e1c4f6d51.webp)

2. Open Recycle Bin, select the file or folder you want to restore, and click "**Restore all**".

After restoration, the file will be restored to its original location.

**Note**: If you empty Recycle Bin, files cannot be restored through Recycle Bin.

### View File Properties

Select a file, right-click it, and select "**Properties**" to view detailed information, including File size, Size on data carrier, MD5, Recently modified, and Owner.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/783cb80cf1084f67b83c58edfcf61475.webp)

## Tagging Files or Folders (Color Labels)

You can assign color labels to files or folders via the right-click menu to visually categorize content. Clicking a specific color in the left navigation pane allows you to quickly filter and locate all labeled items.

### Adding Labels

You can tag files or folders by following these steps:

1. Select one or more files or folders in the file list.

2. Right-click and choose a color label from the context menu.

3. Once applied, the corresponding color indicator will appear next to the file or folder immediately.

**Notes**:

● Multiple labels can be applied simultaneously and can be cleared at any time.

● Labels only affect visual identification and do not alter the file itself or its storage path.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/db95e96056bf448cb2d179d8a4c4de1d.webp)

### Filtering Files by Label Color

When managing a large number of files, labels provide a fast way to locate content:

1. In the "**Files**" interface, click "**Tag**" in the left navigation pane.

2. Under the "**Tag**" category, click a specific color icon. The system will display all files tagged with that color in a consolidated view.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/636a74b1cb044da7bad6db7330f1ed72.webp)

## Compression and Extraction

### Compressing Files

**Operation**: Select files or folders, right-click, and choose "**Compress as...**".  
Select "**Add to compressed file**" to access advanced options. The system supports .zip and .7z formats and allows you to set a compression password and filename encoding to prevent garbled text.

### Decompression

The system supports common formats including .zip, .7z, .rar, .tar, and .iso.

**Decompression Methods**:

● **Decompress**: Unpacks files directly to the current directory, with options for "**Decompress part**" or "**Decompress all**".

![](https://file-us.ugreennas.com/admin/article/2026-08-07/0cdd9d56f8f542f195b1d88a20409c82.webp)

● **Decompress to**: Specify a custom destination path for the extracted files.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/5d120d368916441999e6fecf454981c6.webp)

● **Batch Decompression**: Select multiple archives to extract them simultaneously.

**Filename Encoding Issues**: If filenames appear garbled after decompression, adjust the "**Code Page**" option in the decompression dialog (for example, select Unicode or GBK).

## Online Preview

The NAS provides online preview capabilities for multiple file formats. You can double-click a file to view its contents directly without downloading:

● **Documents**: Supports PDF, TXT, and source code files.

● **Media**: Supports image previews such as JPG and PNG, as well as streaming playback for videos like MP4 and MKV.

● **Archives**: Allows you to open compressed files and browse their internal directory structure.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/478c3efd101f4af0a041cca7dc02e154.webp)
