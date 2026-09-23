# Comics User Guide

> **Article ID**: `768`  
> **Category**: `Application Guide > Comics > Comics User Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/768  

---

## Applicability

**Applicable Clients:** UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version:** UGOS Pro firmware 1.19.1.0126 or later

**Feature Differences:**

● PC / Web Browser: Mainly used to create and manage comic libraries and configure user permissions

● Mobile: Supports the full comic reading experience

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

The Comics app lets you centrally manage and read comic files stored on your NAS. After you create a comic library, the system scans the folder linked to the library and identifies comic titles, chapter information, and cover images based on file names and folder structure.

## Quick Start

If you're using the Comics app for the first time, follow these steps:

1. In "**Files**", create a folder to store your comic files.

2. Upload or move your comic files to this folder.

3. Install the "**Comics**" app from "**App Center**".

4. Open the "**Comics**" app and create a comic library.

5. Wait for the system to scan and identify your comics.

6. Use the UGREEN NAS app on mobile to read comics.

7. Reorder comic libraries, rescan a library, or configure user permissions as needed.

## Prerequisites

Before using the "**Comics**" app, make sure that:

● You have created a folder for storing comic files in the "**Files**" app

● You have uploaded or moved your comic files to this folder

● The folder has full read permissions so the Comics app can scan and identify files properly

## Supported File Formats

The Comics app supports the following file formats:

`cbz`, `cbr`, `cb7`, `zip`, `rar`, `tar`, `pdf`, `epub`, `mobi`, `png`, `jpg`, `jpeg`, `webp`

**Note:** For comics in archive formats, the archive can contain only image files and folders. Nested archives are not supported, and the archive must not contain non-image files such as PDF documents.

## Install and Access

1. Open "**App Center**" and find the "**Comics**" app.

2. Click "**Install**" and follow the setup wizard.

3. After installation, click the "**Comics**" icon to open the app.

## Create a Comics Library

Before using Comics, create a comic library and link it to the folder where your comic files are stored.

1. Open the "**Comics**" app and click "**Create library**".

2. Set the library name and select the folder containing your comics.

3. Select "**Chapter comics**" as the library type, then click "**Confirm**".

![](https://file-us.ugreennas.com/admin/article/2026-09-09/55063acc24fc4e888ab54ffa3a15b080.webp)

Once the comic library is created, the system starts scanning the linked folder. After the scan is complete, you can view the identified comics in the Comics app.

**Note:** Comic identification results depend on file naming and folder structure. Different file organization methods produce different identification results. For details, see "**Related Reading**" at the end of this guide.

## Read Comics

Use the **UGREEN NAS App** on mobile to read comics.

The mobile app supports the following reading features:

● Single-page reading

● Double-page reading

● Split double-page reading

● Brightness adjustment

● Reading direction settings

● Zoom adjustment

● Page-turn animations

● Reading progress saving

The PC client and Web Browser currently do not support comic reading.

## Update Comic Library Content

If comic files are added, deleted, or moved in the linked folder, you can manually rescan the comic library.

1. Open the "**Comics**" app and find the target library under comic library management.

2. Hover over the comic library card, then click "**···**" in the upper-right corner > "**Scan library**".

After the scan is complete, the library contents are updated automatically.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/0b2c5c770da44adfbd3ef3041c95a348.webp)

## Manage Comic Libraries

### Reorder Comic Libraries

You can drag and drop comic libraries to reorder them. Follow these steps:

1. Open the "**Comics**" app and find the library card you want to reorder under comic library management.

2. Hover over the comic library card and click the drag icon that appears in the upper-right corner.

3. Drag the card to the desired position.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/f8fe367e70c64bfca4ac017bee67abe5.webp)

### Manage a Comic Library

Hover over a comic library card and click "**···**" in the upper-right corner to open the action menu. The following options are available:

● **Scan library:** Rescan the folder linked to the library. The system identifies and syncs newly added or modified comic files. If comics have been deleted or moved from the folder, the displayed results are updated accordingly after the scan

● **Edit:** Change the library name, linked folder, or library type

● **Delete:** Delete the selected comic library. Deleting the library does not delete the comic files in the linked folder

![](https://file-us.ugreennas.com/admin/article/2026-09-09/c11be2470aca49d39cdcea800ff9cfc7.webp)

## User Permission Management

Administrators can manage standard users' access to different comic libraries on the NAS. Administrators can access and manage all comic libraries by default, and these permissions cannot be changed.

1. Open the "**Comics**" app and click "**User**" in the left sidebar.

2. Find the target user in the user list and click "**Manage**" to open the library access permissions page.

3. Select the comic libraries the user can access, then click "**Confirm**" to save the settings.

Once configured, standard users can access only the comic libraries they are authorized to view.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/a5d0776c2bb64b9284a94df3a278edb9.webp)

## FAQs

### Q1: What Should I Do If the Comics App Cannot Scan Files?

Check the following:

● Make sure the comic files have been uploaded to the folder linked to the comic library

● Make sure the file format is supported

● Make sure the folder has full read permissions

● Make sure the comic library has been rescanned

### Q2: What Should I Do If a Standard User Cannot See a Comic Library?

Ask an administrator to open "**User**" and check whether the user has access to the corresponding comic library.

### Q3: Will Deleting a Comic Library Delete the Comic Files?

Deleting a comic library removes only the library configuration. The original comic files in the linked folder are not deleted.

## Notes

● UGREEN NAS does not provide comic files. Use only legally obtained comic files.

● If you have a large number of comic files, the initial scan may take some time. Please wait for the scan to complete.

## Related Reading

[How Does the Comics App Identify Comic Files and Chapters?](https://support.ugnas.com/knowledgecenter/detail/article/en-US/937)
