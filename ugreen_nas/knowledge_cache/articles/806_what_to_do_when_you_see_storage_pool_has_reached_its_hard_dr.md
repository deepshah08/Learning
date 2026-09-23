# What to Do When You See "Storage Pool Has Reached Its Hard Drive Fault Tolerance Limit" While Disabling a Drive

> **Article ID**: `806`  
> **Category**: `Application Guide > Storage > FAQ > What to Do When You See "Storage Pool Has Reached Its Hard Drive Fault Tolerance Limit" While Disabling a Drive`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/806  

---

## Issue Description

When attempting to disable a drive in "**Hard Drive**"module, the system displays a warning message: "**The storage pool has reached its hard drive fault tolerance limit and therefore cannot be disabled.**"

![](https://file-us.ugreennas.com/admin/article/2026-02-28/99387e3ce7bb452f87be930c4c626707.webp)

## Cause Analysis

This message appears because the number of available drives in the current storage pool has already reached the "**minimum**" required to maintain normal operation. To prevent data loss and storage pool failure, the system activates a protection mechanism and blocks the disable action.

This is typically caused by one of the following situations:

● **Situation 1: The storage pool uses a non-fault-tolerant mode (such as Basic mode)**

A Basic storage pool consists of only one drive. Since there is no redundancy, disabling this single drive would effectively destroy the entire storage pool. Therefore, the system does not allow it to be removed through the "**Disable**" operation.

● **Situation 2: A fault-tolerant storage pool is already in a "Degraded" state (such as RAID 1 mode)**

Using RAID 1 as an example, it typically consists of two drives and allows one drive to fail. If one drive has already failed or been physically removed, the storage pool enters a "**Degraded**" state. At this point, the remaining drive holds all the data and there is no remaining fault tolerance. Disabling it would result in complete data loss, so the system blocks this operation.

## Recommended Actions

Please follow the steps below based on your specific situation:

● **For single-disk modes such as Basic:**

If you no longer need the data on the drive, or if you have already backed up important data elsewhere, go to the "**Storage pool & Volume**" page and "**delete**" the corresponding storage pool. Once the storage pool is deleted, the drive will return to an "**Unused**" state. At this point, you can safely remove it after powering off the NAS or reassign it for other purposes.

![](https://file-us.ugreennas.com/admin/article/2026-02-28/8dee66160bff441d8d3c66b880c59bb4.webp)

● **For degraded RAID modes:**

Since the storage pool is currently in a risky, non-fault-tolerant state, first prepare an "**Unused**"drive with sufficient capacity and normal health. Then, go to the "**Storage pool & Volume**" page and perform the "**Storage pool repair**" operation on the degraded pool. After the system completes data synchronization and repair, the storage pool will regain normal fault tolerance, and you can safely disable the drive.

![](https://file-us.ugreennas.com/admin/article/2026-02-28/18fd78beea4b4a519c1a5ac1bf9b204a.webp)
