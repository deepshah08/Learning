# [Tutorial] How to Add a Spare Hard Drive (Hot Spare) to a Storage Pool?

> **Article ID**: `420`  
> **Category**: `Application Guide > Storage > FAQ > [Tutorial] How to Add a Spare Hard Drive (Hot Spare) to a Storage Pool?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/420  

---

In the UGOS Pro system of UGREEN NAS, you can configure Hot Spare drives for your storage pool. When a drive in the storage pool fails or enters a critical state, the Hot Spare will automatically replace the faulty drive, restoring the degraded storage pool and enhancing data security.

**Please note:** You must ensure that the storage pool meets the following conditions in order to assign a Hot Spare drive for protection in the UGREEN NAS storage pool.

1. The **RAID type** of the storage pool must support hard drive redundancy (suitable for storage pools of **RAID 1, RAID 5, RAID 6, RAID 10** types).

2. **The capacity of the Hot Spare drive** must be equal to or greater than the capacity of the smallest hard drive in the storage pool.

## To Add a Hot Spare Drive

1. Go to [Storage] > [Storage pool & volume], select a redundancy-supported storage pool, and click "**Hot spare management**".

![](https://file-us.ugreennas.com/admin/article/2025-09-03/8c7831629c8b42c4b728a2661b5e0ddd.webp)

2. In the pop-up dialog box, you will see the Hot Spare status of the current storage pool and available hard drives. If there are no available hard drives that can be designated as Hot Spare, the "Add Now" button will be disabled.

![](https://file-us.ugreennas.com/admin/article/2025-09-03/1543eb7a51ca48709cc3d9ecc3750a35.webp)

3. If there is an available hard drive, click the **"Add Now"** button to add the selected hard drive as a Hot Spare.

![](https://file-us.ugreennas.com/admin/article/2025-09-03/5cb0d86df03f41c39ebc6dbdbd46c0e3.webp)

4. After configuration, click **"Apply"** to save the settings and confirm the Hot Spare has been successfully added.

**Please note:**

● All data on the selected drive will be erased when assigned as a Hot Spare. Ensure the drive contains no critical data and is in good health.

● SSD drives cannot be used as Hot Spares.

● For optimal compatibility, use drives listed in the "[HDD/SSD Compatibility List](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDA0IiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjoxNDMsImFydGljbGVJbmZvSWQiOjEzNSwiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIiLCJwYXRoQ29kZSI6IiJ9) " to avoid potential hardware issues and ensure NAS stability.  
![](https://file-us.ugreennas.com/admin/article/2025-09-03/2103977cd6474f4cbd7a0e964790262f.webp)

## To Remove the Hot Spare from the Storage Pool

1. Go to [Storage] > [Storage Pool & Volume], select the storage pool with an active Hot Spare, and click "**Hot spare management**".

2. Click the "**Remove**" button, and confirm the removal. If the storage pool is degraded, it will no longer be automatically repaired by the Hot Spare drive.

![](https://file-us.ugreennas.com/admin/article/2025-09-03/17ae3e3e34264f20b23b034f109289d9.webp)

3. Click "**Confirm**" to save the changes.
