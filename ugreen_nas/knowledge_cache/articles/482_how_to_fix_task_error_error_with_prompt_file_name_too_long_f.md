# How to Fix "Task error / Error" with Prompt "File name too long / File path may be too long" During File Transfer?

> **Article ID**: `482`  
> **Category**: `Troubleshooting > Network Failure > How to Fix "Task error / Error" with Prompt "File name too long / File path may be too long" During File Transfer?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/482  

---

## Issue Description

When transferring files using "**Files"**, "**Sync & Backup"**, or "**Cloud Drives"**, some files may trigger a "Task error" or "Error". Upon checking the error details, the prompt indicates "File name too long" or "File path may be too long".

![](https://file-us.ugreennas.com/admin/article/2025-08-29/53038ae5401e49849564deb20c23f462.webp)

## Cause Analysis

UGREEN UGOS Pro system imposes character length limits on **file names and paths**:

● **Maximum length**: 255 characters (including file extension).

● **Spaces / Special characters**: Characters such as `#`,`&`, etc. are also included in the total length.

When the **directory path (folder + file name) exceeds the character limit**, file transfer will fail. Even if the path looks valid, the system may not be able to process the sync or backup properly.

## Solution

1. Locate the file or folder flagged with "Task error", and rename it to **ensure the total length ≤ 255 characters**.

2. After adjustments, re-run the sync or backup task.
