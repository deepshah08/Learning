# [FAQ] What to Do if the RAID Sync Speed is Slow in the Storage?

> **Article ID**: `471`  
> **Category**: `Application Guide > Storage > FAQ > [FAQ] What to Do if the RAID Sync Speed is Slow in the Storage?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/471  

---

## Problem Description

When performing storage pool repairs, data reorganization, hard disk replacement, or RAID type changes in the UGOS Pro system, you may notice that the RAID synchronization task progresses slowly, resulting in extended data synchronization times.

This occurs because the RAID synchronization speed is influenced by the system's default synchronization strategy and resource usage. Typically, synchronizing 1TB of data takes approximately 4 hours. However, the synchronization speed may vary depending on the priority settings of the system's performance configuration.

## Solution

You can improve the RAID sync speed by changing the sync strategy. Follow these steps:

1. Log in to the UGOS Pro system via the computer or web interface.

2. Go to the **[Storage] > [Storage] > [Advanced Settings]** page.

3. In the **Performance options**, select **"Priortize RAID sync"** to enhance sync speed.

**Notes:**

● To reduce system resource usage and prevent prolonged synchronization times, it is recommended not to perform file write operations during the RAID synchronization process.

● Once the RAID synchronization task is completed, it is recommended to switch back to the "Prioritize user read/write" synchronization strategy to enhance the system's file read and write performance.

![](https://file-us.ugreennas.com/admin/article/2025-08-29/efb9d81ea23e426fb1477c95b1a89053.webp)
