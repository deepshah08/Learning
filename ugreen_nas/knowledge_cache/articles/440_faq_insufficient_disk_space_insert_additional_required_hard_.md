# [FAQ] Insufficient Disk Space: Insert Additional Required Hard Drives into NAS Device

> **Article ID**: `440`  
> **Category**: `Application Guide > Storage > FAQ > [FAQ] Insufficient Disk Space: Insert Additional Required Hard Drives into NAS Device`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/440  

---

## Problem

When inserting a hard drive with existing data into UGREEN NAS for use as external storage, the system may prompt: "Insufficient disk space. Please insert additional required hard drives into the NAS device". This issue prevents the hard drive from being properly used as external storage. The problem typically occurs when the inserted hard drive contains data or was previously used in another device, such as another UGREEN NAS or a different NAS system.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/b9e067f5f7484d05b14a8ca8f1f418be.webp)

**Possible Cause:** If the hard drive was previously configured as part of a RAID array, UGREEN NAS may fail to recognize the drive unless all the hard drives that constitute the RAID array are inserted into the NAS device simultaneously.

## Solution

**Solution for Hard Drives Previously Part of a RAID Array**

If the hard drive was part of a RAID array, all the associated drives in the RAID configuration must be inserted into the NAS device together. This ensures the system can correctly read the RAID information and restore the storage structure.

For example, if you previously used three hard drives configured as a RAID 5 array in the UGOS system, and then switched to the UGOS Pro system, you are required to insert all three drives into the NAS simultaneously to ensure the proper recognition and functionality of the RAID 5 array.
