# How Does the Comics App Identify Comic Files and Chapters?

> **Article ID**: `937`  
> **Category**: `Application Guide > Comics > How Does the Comics App Identify Comic Files and Chapters?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/937  

---

## Applicability

**Applicable Version:** UGOS Pro firmware 1.19.1.0126 or later

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

The Comics app identifies comic titles, chapter information, and cover images based on file format, file name, and folder structure.

If a comic cannot be identified correctly, first check whether the file format, archive contents, and folder structure meet the identification requirements.

## Supported File Formats

The Comics app supports the following file formats:

`cbz`、`cbr`、`cb7`、`zip`、`rar`、`tar`、`pdf`、`epub`、`mobi`、`png`、`jpg`、`jpeg`、`webp`

## Archive Content Requirements

To ensure that comics in archive formats such as`zip`、`rar`can be identified correctly, make sure that:

● The archive contains only image files and folders.

● The archive does not contain other archive files.

● The archive does not contain non-image files, such as`PDF`documents.

## Chapter Comics Identification Rules

Chapter comics are suitable for comics organized by volumes or chapters.

### Archive-Based Chapter Comics

When a comic folder contains multiple archive files, the system identifies them as follows:

● **Comic title:** Uses the folder name.

● **Chapter content:** Each archive file in the folder is identified as a separate chapter.

Example:

● File structure: The **Cinderella** folder contains **Chapter 1.zip** and**Chapter 2.zip**.

● Identification result: The Comics app creates the **Cinderella**comic with **Chapter 1** and **Chapter 2**.

**Note:** The system does not identify empty folders. Make sure the folder contains supported archive files.

### Image-Based Chapter Comics

When comics are stored in folders containing image files, the system identifies them as follows:

● **Comic title:** Uses the name of the parent folder.

● **Chapter name:** Uses the name of the folder containing the images.

Example:

● File structure: The **Cinderella** folder contains **Chapter 1** and **Chapter 1** subfolders, with comic images stored in each subfolder.

● Identification result: The Comics app creates the **Cinderella** comic with **Chapter 1** and **Chapter 1.**

## One-shots Identification Rules

Single comics are suitable for managing an entire comic as a single item.

### Archive-Based One-shots

If an entire comic is packaged as a single archive file, the system identifies the archive as one comic.

Example:

● File structure: The comic library folder contains **Cinderella.zip**and **Peter.Pan.zip**.

● Identification result: The Comics app creates two comics: **Cinderella**and **Peter.Pan**.

#### Image-Based One-shots

If image files are stored directly in folders, the system identifies each folder containing images as a separate comic.

Example:

● File structure: The comic library folder contains **Cinderella** and **Peter.Pan** folders, with comic images stored inside each folder.

● Identification result: The Comics app creates two comics: **Cinderella** and **Peter.Pan.**

## FAQs

### Q1: Why Doesn't the Comics App Identify Empty Folders?

The system does not identify empty folders. Make sure the folder contains supported comic files.

### Q2: Why Can't an Archived Comic Be Identified?

Check the following:

● Make sure the archive format is supported.

● Make sure the archive does not contain other archive files.

● Make sure the archive does not contain non-image files.

### Q3: Why Don't Newly Added Comic Files Appear?

Rescan the comic library. Once the scan is complete, the displayed library contents will be updated automatically.

## Notes

● Comic identification results depend on file naming and folder structure. We recommend organizing your files before creating or scanning a comic library.

● Comics may not be identified correctly if an archive contains other archive files or non-image files.
