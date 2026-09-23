# How to Create an SSD Cache on Volume?

> **Article ID**: `415`  
> **Category**: `Application Guide > Storage > FAQ > How to Create an SSD Cache on Volume?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/415  

---

## Applicability

**Applicable platform:** UGREEN NAS running UGOS Pro

**Applicable version:** UGOS Pro firmware 1.16.0.0042 and later

This document is for reference only. The actual interface and operation paths may vary slightly due to system or app version updates. Please refer to the actual interface.

## Feature Overview

The SSD Cache feature uses high-speed SSDs to provide cache acceleration for storage pools created with HDDs. Once enabled, it can significantly improve random read/write performance and overall system responsiveness.

## Before You Start

Before configuring SSD cache, make sure you have confirmed your hardware configuration and storage pool type:

● SSD cache acceleration is only available for storage pools created with HDDs. If your storage pool is created entirely with SSDs, the "**SSD Cache**" entry will not be displayed.

● If you are not sure about the drive type used by a storage pool, go to "**Storage**">"**Hard Drive**" to check the physical drive type of the corresponding storage pool.

## Create an SSD Cache for a Volume

Enter the password of the currently signed-in account and submit it for verification. After verification is successful, the system will start building the SSD cache in the background.

1. Open the "**Storage**" app. In the left sidebar, click "**Storage**". Find the HDD storage pool for which you want to create a cache, click "**···**" on the right, and select "**SSD Cache management**" to go to the details page.

![](https://file-us.ugreennas.com/admin/article/2026-05-19/70c491fb0f1545a7a18d1a906cd6b23b.webp)

2. Click "**Create**".

![](https://file-us.ugreennas.com/admin/article/2026-05-19/dc5df67bbace494189498359348e36ec.webp)

3. Select the volume in this storage pool to which you want to mount the cache. Select"**Read-only cache**" or "**Read-Write cache**" based on your service requirements, then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-05-19/3552bd8170fd4b5b963378b414d5a78f.webp)

4. If you select "**Read-only cache**", the system will proceed directly to the next step after you click "**Next**", without displaying a pop-up prompt.If you select "**Read-Write cache**", the system will display a security warning because this mode involves the risk of delayed data writes. Read the warning carefully, click "**I understand the risk of data loss**", and then click "**Confirm**" to proceed.

![](https://file-us.ugreennas.com/admin/article/2026-05-19/bbb0d8f92d7c44e38cb15dd3f7c6bee9.webp)

5. Select the RAID type for the cache. Based on the minimum number of drives required by the selected RAID type, select the corresponding number of M.2 SSDs from the list, then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-05-19/282863fe71ad4e32b6bd7a3c028f0b60.webp)

6. Set the capacity of the selected SSDs to be used for caching, then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-05-19/7dbbda4cc4f948f3a90d6511661a712f.webp)

7. Confirm the SSD cache configuration. After confirming that all settings are correct, click "**Apply**".

![](https://file-us.ugreennas.com/admin/article/2026-05-19/ce7d12308b3c41af9524ed839b1b7bdd.webp)

8. A formatting prompt will appear. Click "**Format**".

![](https://file-us.ugreennas.com/admin/article/2026-05-19/8f572a3b8300414f93b2100c3fdf44eb.webp)

9. Enter the password of the currently signed-in account and submit it for verification. After verification is successful, the system will start building the SSD cache in the background.

![](https://file-us.ugreennas.com/admin/article/2026-05-19/67532a3658ee4d3b864d885f8aca6e94.webp)

## Manage Cache

After the SSD cache is created, you can return to the "**SSD cache management**" entry of the corresponding storage pool at any time to view the cache space that has been created. Click the cache space to view the cache hit rate and usage value.

If you need to adjust the configuration later, go to the "**SSD cache management**" page and click "**Remove**" to safely unmount the cache.

![](https://file-us.ugreennas.com/admin/article/2026-05-19/1ded4a9d549f410ea13627cc3c815e69.webp)

## Notes

● While SSD cache is being added or built, the system will temporarily disable all associated apps under the volume.

● If you need to perform hardware maintenance on the NAS, replace hardware, or remove an SSD, you must manually perform "**Remove SSD Cache**" in the system before physically removing the drive. Do not remove the drive directly. Otherwise, data in the volume may become corrupted or lost.

## Related Articles

● [What types of SSD caching does UGOS Pro support?](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmNDMwIiwiY2xpZW50VHlwZSI6IiJ9)
