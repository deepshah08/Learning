# Why Does UGREEN NAS Still Show "Insufficient volume capacity" When Uploading file to Drive After Expanding Cloud Storage?

> **Article ID**: `798`  
> **Category**: `Application Guide > Cloud Drives > Why Does UGREEN NAS Still Show "Insufficient volume capacity" When Uploading file to Drive After Expanding Cloud Storage?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/798  

---

## Applicability

**Applicable Clients**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: NAS firmware 1.18.0.0032 or later

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## Problem Description

When uploading files from the NAS to a cloud drive, the upload fails and the system displays "**Insufficient volume capacity**". After expanding the cloud drive storage, the same error still appears when you try uploading from the NAS again.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/6f0b9acf71024990b036d04f8e02cee2.webp)

## Cause Analysis

This issue is caused by "**cached capacity information**". When the NAS mounts a network folder, it retrieves the current capacity information. After you expand storage on the cloud drive, the NAS may not immediately sync the updated capacity information. As a result, the system may still determine that the storage is full based on the previous capacity limit.

## Solution

To sync the latest capacity information, "**Disconnect and Reconnect**" the network folder to force the mount status to refresh.

**Steps**:

1. Open the "**Files**" app and click "**Network folder**" in the left navigation pane.

2. Locate the target cloud drive icon, right-click it, and select "**Disconnect**".

![](https://file-us.ugreennas.com/admin/article/2026-09-07/cbb3ed1e4a4e438187be5f4085c47a0e.webp)

3. After the status refreshes, right-click the cloud drive icon again and select "**Reconnect**".

![](https://file-us.ugreennas.com/admin/article/2026-09-07/f007e87e557e46069732109adb48e652.webp)

Once reconnected, the system will retrieve the latest capacity information. You can then try uploading the files again.
