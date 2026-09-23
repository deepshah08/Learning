# Storage

> **Article ID**: `313`  
> **Category**: `Application Guide > Storage > Storage`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/313  

---

## Feature Overview

The "**Storage**" application is a core component of the NAS system. It supports viewing system storage status, creating and managing storage pools/volumes, and performing advanced maintenance operations such as SSD cache acceleration, RAID type changes, and data organizing.

## Overview and Status Monitoring

The overview page provides an intuitive display of the health status of storage volumes and hard drives.

### Storage system status

● **Normal**: All storage pools and volumes are operating normally.

● **Warning**: An abnormal condition has occurred in a storage pool/SSD cache or volume/partition. Data is temporarily safe, but it is recommended to investigate and resolve potential issues as soon as possible.

● **Dangerous**: A degradation alert is reported for a storage pool or SSD cache. Please review the impact and address the issue as soon as possible according to the recommendations.

● **Serious**: A serious issue has occurred. The storage pool/SSD cache (damaged) or volume/partition (damaged/read-only) may result in data loss. Immediate action is required.

If a drive status is shown as "**locked**", please refer to [How to Resolve the Issue When Hard Drive Status Shows as "Locked".](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjo4OTAsImFydGljbGVJbmZvSWQiOjI5NiwiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIiLCJwYXRoQ29kZSI6IiJ9)

### Widget Management

Widgets can be used to customize how key information is displayed:

● At the bottom of the overview page, click "**Add widget**" to add widgets such as hard drive status, storage space status, and hard drive performance monitoring.

![](https://file-us.ugreennas.com/admin/article/2026-06-05/5ca6eb52d6c14de1b84c799895546626.webp)

● Click the "**…**" in the upper-right corner of a widget to reorder widgets, customize the displayed information, or delete the widget.

![](https://file-us.ugreennas.com/admin/article/2026-06-05/b76947dfca6a4bf68869a13693c7b48c.webp)

## Create a Storage Pool and Volume

Before storing data, a storage pool and volume must be created first.

● **Storage pool:** A set of hard drives managed using RAID technology, providing underlying data protection.

● **Volume:** A logical unit created based on a storage pool and used to store actual data.

**Steps:**

1. Open the "Storage" app and go to "**Storage**">"**Storage Pool & Volume**". Click "Create">"Storage Pool" in the upper-left corner of the page to start the wizard.

![](https://file-us.ugreennas.com/admin/article/2026-06-05/37456ae29afd4255b6bed4dc30474fa2.webp)

2. Select the hard drives to be used for creating the storage pool. Choose a suitable RAID type based on data protection needs, such as Basic, RAID 1, or RAID 5. Choose whether to skip the "**Hard drive test**" as needed, then click "**Next**".

**Note:**

● For more suggestions, see [How to Choose the Right RAID Level for Your Needs](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmMTMyIn0=) .

● When creating a storage pool, the available capacity of each hard drive must be at least 32 GB.

![](https://file-us.ugreennas.com/admin/article/2026-06-05/351fdcbb423348bd9a3c80df0e2002b3.webp)

3. The system will automatically enter the volume creation page. Enter the capacity to allocate to this volume, select the file system type, and click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-06-05/d5b853b56a9540938668032991441c39.webp)

4. Check whether all configuration parameters are correct, then click "**Create**".

![](https://file-us.ugreennas.com/admin/article/2026-06-05/07c0a1ede99447d2bf29b2ce84596b65.webp)

5. A risk warning will appear. After confirming that everything is correct, click "**Format**".

![](https://file-us.ugreennas.com/admin/article/2026-06-05/8d2a00361f4d4b62b8bd19bb4d06c09b.webp)

6. Enter the system password for verification. After verification is successful, the system will start creating the storage pool and volume.

![](https://file-us.ugreennas.com/admin/article/2026-06-05/e137d513798b483ab9ac97ffa3d0ffdd.webp)

**Note:**

● The selected hard drives will be formatted during initialization. Before proceeding, make sure all important data on the drives has been backed up.

● To create multiple volumes under one storage pool, click the "**…**" on the right side of the storage pool and select "**Create Volume**". Make sure the remaining capacity of the storage pool is greater than 10 GB.

## Advanced Storage Pool Management

Administrators can expand existing storage pools, upgrade RAID types, and perform other advanced settings.

![](https://file-us.ugreennas.com/admin/article/2026-06-05/005d3abd42c64fe0986eb3b2d7de7bb5.webp)

### Storage Pool Expansion

If the storage pool uses a RAID type that supports redundancy, such as RAID 1 or RAID 5, its capacity can be expanded by **replacing drives one by one with larger-capacity drives**. For details, see [UGREEN NAS Storage Pool Expansion Guide (Replacing Drives One by One)](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmODEwIiwiY2xpZW50VHlwZSI6IlBDIn0=) .

![](https://file-us.ugreennas.com/admin/article/2026-06-05/5a200a8845044a858d300b853b2a57fe.webp)

### Change RAID Type

UGREEN NAS supports upgrading the RAID type without data loss.

● **Supported upgrade path:** Basic > RAID 1 > RAID 5.

● The upgrade must meet the required number of hard drives. For details, see [Change the RAID Type](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmMzkyIn0=) .

![](https://file-us.ugreennas.com/admin/article/2026-06-05/a2ac65f5dab2418ba14ac2a7d5831532.webp)

### SSD Cache Acceleration

For volumes created on SATA HDDs, M.2 SSDs can be added to improve read/write performance.

1. On the "**Storage Pool & Volume**" page, find the target storage pool and click "**…**" on the right side > "**SSD Cache Management**".

![](https://file-us.ugreennas.com/admin/article/2026-06-05/093ee9a70b10409ba7e282a782593d52.webp)

2. Click "**Create**".

![](https://file-us.ugreennas.com/admin/article/2026-06-05/de3c5ed973e54cae8cea1ff47bbe20bc.webp)

3. Select the target volume and cache mode, then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-06-05/4fe4827ee9ad47e8b8981be84d1f9d40.webp)

4. Select the RAID type for the SSD cache, choose the M.2 drive to be used as cache, and click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-06-05/e759375321af492a91d159c1931199d9.webp)

5. Allocate the cache capacity, then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-06-05/d03cc13ac24d496ea3a9398c5a026e6f.webp)

6. Check whether all configuration parameters are correct, then click "**Apply**".

![](https://file-us.ugreennas.com/admin/article/2026-06-05/bb4d3d484b0246189603d234ff4bc3b5.webp)

7. A risk warning will appear. After confirming that everything is correct, click "**Format**".

![](https://file-us.ugreennas.com/admin/article/2026-06-05/dec44e21510c41da8f4e39bd0b18ae21.webp)

8. Enter the system password for verification. After verification is successful, the system will start creating the SSD cache.

![](https://file-us.ugreennas.com/admin/article/2026-06-05/7d451152dbf74abda2ea0508152a232e.webp)

### Hot Spare

A spare drive can be configured for a storage pool. When a drive in the array fails, the hot spare automatically replaces it to maintain data security. For details, see [How to Add a Spare Hard Drive (Hot Spare) to a Storage Pool?](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTI3MSwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0MjAsImFydGljbGVWZXJzaW9uIjoiMS4wIiwicGF0aENvZGUiOiIifQ==) .

![](https://file-us.ugreennas.com/admin/article/2026-06-05/a35d47985af74e2a8fd7a0395dada18a.webp)

### Volume Management

In the "**Storage**" app, administrators can monitor volume usage in detail and configure the file system warning mechanism.

1. **Access Management Options**

On the "**Storage Pool & Volume**" page, find the target volume and click the "**…**" icon on the right. Select the desired function as needed.

![](https://file-us.ugreennas.com/admin/article/2026-06-05/0cc3569f02d84a698b505bbf1a94aa11.webp)

2. **View Usage Details**

After selecting the usage details view, the following key information can be obtained:

● **Volume usage:** Displays the current volume's "**Used capacity**" and "**Available capacity**" at a glance.

● **Usage analysis:** Lists the actual space used by each shared folder under the volume, helping quickly identify folders that occupy a large amount of space.

![](https://file-us.ugreennas.com/admin/article/2026-06-05/394ca1aabc8143bc8ac5f438e9e2e128.webp)

3. **Set a Capacity Warning**

To prevent business interruption caused by a full volume, enabling capacity warnings is recommended:

● On the "**Storage Pool & Volume**" page, find the target volume and click "**…**">"**Settings**" on the right.

● Set the percentage threshold for "**Insufficient capacity warning**".

![](https://file-us.ugreennas.com/admin/article/2026-06-05/5c77ac60cb764e91be253abae33b9496.webp)

When the remaining capacity of the volume falls below the specified percentage, the system will send a notification to remind the administrator.

## Data Organizing

For RAID 5 or RAID 6 storage pools, regular data organizing is recommended to maintain data consistency.

1. Go to the "**Data organizing**" page, select a storage pool, and click "**Organize**".

![](https://file-us.ugreennas.com/admin/article/2026-06-05/4d608f341f7c4dc683555e45725631a1.webp)

2. Click "**Edit**" to set an automatic scheduled task.

![](https://file-us.ugreennas.com/admin/article/2026-06-05/351542ce0b924cbc98e21ce093324625.webp)

## Advanced Settings

On the advanced settings page of "**Storage**", administrators can fine-tune system performance policies and repair mechanisms to balance device performance and data maintenance efficiency.

![](https://file-us.ugreennas.com/admin/article/2026-06-05/b043feaa93794b639a697fd6b9fc2ea6.webp)

### Performance Options

When a storage pool is performing time-consuming background synchronization tasks, such as repair, data organizing, hard drive replacement, or RAID type change, the system resource priority can be adjusted based on current service needs:

● **Prioritize user read/write:** Select this option when the NAS is playing videos, accessing data, or performing other service tasks, and background tasks should not affect the user experience. The system will prioritize smooth service access to prevent lag. However, RAID repair or synchronization will slow down and take longer to complete.

● **Prioritize RAID synchronization:** Select this option when the storage pool needs to be restored to a healthy state as soon as possible, such as during emergency rebuilding after a drive failure, or when maintenance is performed during off-peak hours, such as late at night. The system will prioritize computing resources and I/O bandwidth for background maintenance tasks, significantly reducing the time required for expansion or repair. However, service access performance will decrease during this period.

### Quick Repair

After this option is enabled, when repairing a storage pool in "**Degraded**" status, the system intelligently identifies and skips unused storage space, repairing only the areas that contain actual data.

It is recommended to keep this option enabled. This can significantly reduce the time required for repair and lower the load on the hard drives.
