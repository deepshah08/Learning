# Quickly Clean Up Duplicate Files with File Deduplication

> **Article ID**: `158`  
> **Category**: `Application Guide > Files > Quickly Clean Up Duplicate Files with File Deduplication`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/158  

---

## Applicability

**Applicable client:** UGREEN NAS PC client (Windows/macOS).

**Applicable version:** NAS firmware 1.17.0.0034 or later.

This document is for reference only. The actual interface and operation paths may vary slightly depending on system or app version updates. Please refer to the actual interface.

## Overview

File Deduplication scans the NAS for duplicate files with identical content. It supports multiple file types, including images, documents, audio, videos, and archives. By removing redundant files scattered across different folders, it helps free up storage space and makes file management more efficient.

**How Deduplication Works**：

By default, File Deduplication uses **fast matching**. It first compares file sizes to quickly identify files that may be duplicates.

For higher accuracy, enable "**Exact match**". The system will calculate the hash value of each file and compare file fingerprints. A file is identified as a duplicate only when its content is exactly the same.

## Configure a Scan Task

1. Open "**Files**", then click "**Management**">"**File deduplication**" in the top bar.

2. On the "**File deduplication**" page, select the file types to check.

3. In the lower-left corner of the page, choose whether to enable "**Exact match**" as needed.

● If "**Exact match**" is not selected, the system quickly compares files by **file size**, which takes less time.

● If "**Exact match**" is selected, the system performs low-level hash calculation to extract and compare file fingerprints. This provides the highest accuracy but takes longer.

4. Click "**Scan specified folder**" in the lower-right corner to select a custom target path, or click "**Scan all folders**" to scan all folders.

![](https://file-us.ugreennas.com/admin/article/2026-06-16/705f7ec8dea7485b8f708e2f395e4c6f.webp)

After the task starts, if there is a large amount of data, click "**Background**" to let the task continue in the background. This does not affect normal use of other system features.

![](https://file-us.ugreennas.com/admin/article/2026-06-16/53d9eaa150b54703af832d5eee2952aa.webp)

## Smart Selection and Cleanup

After the scan is complete, the system automatically opens the deduplication results panel. All duplicate files are grouped for easier review.

1. Click any file group in the list on the left. The panel on the right will show a visual preview of the file, such as an image thumbnail, along with detailed information including resolution and storage path.

![](https://file-us.ugreennas.com/admin/article/2026-06-16/d830c34b7be34257b23c0bccbade768c.webp)

2. Select the files to clean up, then click "**Clean now**" in the lower-right corner. The system will delete the selected duplicate files.

**Smart select**: The system can automatically select duplicate files based on preset rules. Click "**Smart select**" in the upper-left corner to open the drop-down menu, then choose a rule, such as keeping the most recently modified file. The system will batch-select duplicate files for deletion.

## Scan Record Management

If there are too many scan results to review and clean up at once, save the current progress through scan records.

1. In the lower-right corner of the deduplication results panel, click "**Save scan record**" to save the current comparison results.

2. Return to the"**File deduplication**" home page and click "**Scan records**" in the upper-right corner. In the history list, find the corresponding saved record and click "**View**" to restore the previous deduplication results panel and continue cleanup.
