# How to Configure a Recycle Bin Cleanup Plan?

> **Article ID**: `858`  
> **Category**: `Application Guide > Files > Recycle bin > How to Configure a Recycle Bin Cleanup Plan?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/858  

---

## Applicability

**Applicable client:** UGREEN NAS desktop client (iOS / Android)

**Applicable version:** NAS firmware 1.16.0.0042 and later

This document is for reference only. The actual interface and operation paths may vary slightly due to system or app version updates. Please refer to the actual interface.

## Overview

To prevent files in Recycle Bin from gradually taking up NAS drive space when it is not cleaned for a long time, the system provides a "**Cleanup Plan**" feature. By setting predefined automation rules, the system can automatically empty files at the specified frequency and time without manual operation, helping storage space be freed up and reused more efficiently.

![](https://file-us.ugreennas.com/admin/article/2026-05-25/d93090d49676495d927067357ce1d41a.webp)

## Create a Cleanup Plan

1. On the Recycle Bin page, click the "**Settings**" icon in the lower-left corner. In the pop-up menu, select "**Cleanup Plan**".

2. On the Cleanup Plan page, click "**+ New plan**" to open the configuration window.

3. Based on your actual needs, choose to clean up "**All**" folders, or select specific folders.

4. Select the cleanup mode you need. After configuring the execution time and cleanup frequency, click "**Confirm**" at the bottom to save and enable the automated task.

## Manage or Delete Cleanup Plans

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
