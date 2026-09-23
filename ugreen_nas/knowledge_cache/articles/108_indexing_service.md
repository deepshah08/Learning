# Indexing Service

> **Article ID**: `108`  
> **Category**: `Application Guide > Control Panel > Indexing Service`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/108  

---

## Applicability

**Applicable client:** UGREEN NAS PC client (Windows/macOS).

**Applicable version:** NAS firmware 1.16.0.0042 or later.

This document is for reference only. The actual interface and operation paths may vary slightly depending on system or app version updates. Please refer to the actual interface.

## Overview

"**Indexing Service**" in "**Control Panel**" manages system-wide indexing and thumbnails. Proper configuration can significantly improve the efficiency of finding files and make albums and poster walls load more smoothly.

## Universal Search Configuration

Universal Search helps quickly locate large amounts of content on the NAS, and deeply integrates search results into apps such as "**Photos**", "**Music**", and "**Theater**".

1. **Access Path**

Sign in to the system desktop, open "**Control Panel**", then click "**Indexing Service**" in the left sidebar.

![](https://file-us.ugreennas.com/admin/article/2026-06-15/31968233795d4a4c90458d33285cec7c.webp)

2. **Manage Search Settings**

On the "**Indexing Service**" page, click "**Search Settings**" on the right side of "**Universal Search**" to customize the search scope and manage the system indexing service for more accurate search results. For details, see [**Universal Search User Guide**](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmNzM5IiwiY2xpZW50VHlwZSI6IlBDIn0=) .

## Thumbnail Generation

The thumbnail rendering engine applies across the NAS system. By default, thumbnails are generated in real time when an image or video file is viewed for the first time.

To improve browsing performance in apps, pre-generation rules can be configured manually.

### Advanced Settings

Click "**Advanced Settings**" for "**Thumbnail generation**". In the "**Advanced Settings**" window, the following settings can be configured:

● **Adjust thumbnail quality**

The thumbnail quality for "**Photos**" and "**Videos**" can be set separately. Choose either "**Standard**" or "**High definition**".

● **Manage the pre-generation range**

To ensure a smooth experience, the system creates thumbnail pre-generation tasks by default for specific media directories, such as folders linked to the media library in "**Theater**" and folder ranges linked to "**Photos**". The number of included directories is also displayed.

To pre-generate thumbnails for additional folders, click "**New**" in the upper-right corner and manually add them to the pre-generation range. After confirming the configuration, click "**OK**" to save.

![](https://file-us.ugreennas.com/admin/article/2026-06-15/507189cc177a44cfb7fd90fc6f171a28.webp)

### Manual Regeneration

If media covers in the file list or apps appear broken, blank, or significantly delayed during daily use, manually trigger regeneration to rebuild the thumbnails and fix the issue completely:

1. Return to the **"Indexing Service"** page, then click **"Regenerate"** for **"Thumbnail generation"**.

2. In the pop-up window, **"Generate missing thumbnails only"** is selected by default. To clear abnormal cache data and regenerate all thumbnails, clear this option before proceeding.

## FAQs

1. **Why can’t I find a newly added folder in search, or why are thumbnails missing?**

Building the index or generating a large number of thumbnails for the first time takes some time and uses system resources. Wait for the background process to complete automatically.
