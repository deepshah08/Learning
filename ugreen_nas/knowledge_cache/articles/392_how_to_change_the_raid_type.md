# How to Change the RAID Type?

> **Article ID**: `392`  
> **Category**: `Application Guide > Storage > How to Change the RAID Type?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/392  

---

### Applicability

**Applicable Version**: UGOS Pro firmware 1.19.1.0126 or later

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

UGREEN NAS supports changing the RAID type of a storage pool **without losing existing data**. For example, once you have added enough drives, you can upgrade a RAID 1 storage pool to RAID 5 for better performance and more efficient storage utilization.

The currently supported upgrade paths are:

● **Basic** can be upgraded directly to **RAID 1** or **RAID 5**

● **RAID 1** can be upgraded to **RAID 5**

**RAID Conversion Limitations**

Not all RAID types can be converted. The currently supported upgrade paths are:

|  |  |  |
| --- | --- | --- |
| **Current RAID Type** | **Upgradable To** | **Additional Drives Required** |
| Basic | RAID 1 | 1 |
| Basic | RAID 5 | 2 |
| RAID 1 | RAID 5 | 1 |

**Note**:

● JBOD and RAID 0 **do not support online conversion**. To change these RAID types, you must first back up your data and recreate the storage pool.

● RAID types can only be upgraded to higher levels; downgrading is not supported.

## Prerequisites

Before changing the RAID type, make sure all of the following requirements are met:

● The storage pool status is "**Normal**".

● At least one **unused and healthy** drive is available.

● The capacity of the new drive is **not smaller than** the smallest drive in the storage pool.

● For the best compatibility and performance, we recommend using drives of the same brand, model, and capacity.

● Back up important data before proceeding to protect against data corruption in unexpected situations.

## PC Instructions

1. Open the "**Storage**" app and go to "**Storage**" > "**Storage Pool & Volume**".

2. Locate the target storage pool, click the "**···**" icon on the right, and select "**Change RAID type**".

![](https://file-us.ugreennas.com/admin/article/2026-09-09/c04e3eaadfef4c07aac0fbf86669d7c2.webp)

3. In the pop-up window, confirm the target RAID type, then click "**Change**".

**Note**: If the current RAID type cannot be changed, this button will be grayed out and unavailable.

4. Select the available drive you want to add, then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-09-09/7a4a66feea3940be80f425de8bb509b3.webp)

**Note**: The added drive will be formatted. Make sure to back up any data on it beforehand.

5. Review the configuration details, then click "**Apply**" to start changing the RAID type.

6. During the process, the storage pool status will display "**Changing RAID type**". Once complete, the status will automatically return to "**Normal**".

## Mobile Instructions

1. Open the "**Storage**" app and go to the "**Storage**" page.

2. Locate the target storage pool, click the "**>**" icon on the right, and select "**Change RAID type**".

![](https://file-us.ugreennas.com/admin/article/2026-09-09/eb3d8b39efa94daaaae65617dcd50949.webp)

3. In the pop-up window, confirm the target RAID type, then click "**Change**".

![](https://file-us.ugreennas.com/admin/article/2026-09-09/d280348ed9d94b439e2870b006e6ce57.webp)

**Note**: If the current RAID type cannot be changed, this button will be grayed out and unavailable.

4. Select the available drive you want to add, then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-09-09/1643c851c8d642238b16c5d7cdd3f996.webp)

**Note**: The added drive will be formatted. Make sure to back up any data on it beforehand.

5. Review the configuration details, then click "**Apply**" to start changing the RAID type.

6. During the process, the storage pool status will display "**Changing RAID type**". Once complete, the status will automatically return to "**Normal**".

## Notes

● Changing the RAID type can take a long time and use significant system resources. We recommend performing this operation when the NAS is idle.

● Keep the NAS powered on throughout the RAID type change. Do not shut down or restart the device, as this may cause data corruption or loss.

● During RAID conversion, some apps that depend on the storage pool may be temporarily unavailable.

● If a drive fails during the process, the RAID type change will still complete, but the volume may enter a "**Degraded**" state.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/9a5fc4b8fcf94ecd9102313fd5b4c66f.webp)

● If the RAID type change fails, do not force-restart the NAS. Check the detailed error information in "**Storage**" or contact technical support for assistance.
