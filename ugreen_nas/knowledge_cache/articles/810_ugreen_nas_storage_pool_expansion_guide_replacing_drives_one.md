# UGREEN NAS Storage Pool Expansion Guide (Replacing Drives One by One)

> **Article ID**: `810`  
> **Category**: `Application Guide > Storage > FAQ > UGREEN NAS Storage Pool Expansion Guide (Replacing Drives One by One)`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/810  

---

## Applicability

**Applicable Version**: UGOS Pro firmware 1.19.1.0126 or later

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

Expanding a storage pool by "**replacing drives with larger-capacity drives one by one**" lets you increase storage capacity while keeping your existing data intact. However, this process requires multiple RAID rebuilds and is considered a high-risk operation.

**Notes**:

● While each drive is being replaced, the storage pool enters a **"Degraded"** state and temporarily loses data redundancy. If another old drive develops bad sectors or fails during this period, all data may be permanently lost.

● You must power off the NAS before removing a drive. Never remove multiple drives at once. Always follow the cycle "**Remove one drive > Replace it > Complete the repair**" before moving on to the next drive.

● We recommend connecting the NAS to a UPS (Uninterruptible Power Supply) to prevent file system damage caused by a power outage during rebuilding.

## Applicable Scenarios and Prerequisites

Before you begin, make sure your storage pool meets the following requirements:

● **Supported RAID Types**: This expansion method supports RAID 1, RAID 5, RAID 6, and RAID 10.

● **Unsupported RAID Types**: Basic, JBOD, and RAID 0 cannot be expanded using this method. Replacing drives in these modes may result in data loss.

● **Storage Pool Status**: The storage pool must currently be in the **"Normal"** state. If it is degraded or damaged, resolve the issue before proceeding.

● **New Drive Requirements**: The new drive must have a capacity equal to or greater than the drive it replaces. For consistent performance, we recommend using NAS-grade drives of the same brand and rotational speed.

**Note**: If you are unsure of the storage pool's RAID type or current status, sign in to UGOS Pro and open the "**Storage**" app to check.

## Full Data Backup

To protect against unpredictable hardware failures, such as URE (Unrecoverable Read Error), we recommend backing up your data before you begin.

### Option 1: Local Cold Backup (Recommended)

Connect a USB external drive enclosure to the NAS as external storage, then copy your important data to the external drive.

**Advantages**: Fast backup, easy recovery, and no dependency on network conditions.

**Disadvantages**: Requires physical storage hardware and may be limited by available capacity.

### Option 2: Cloud or Off-site Backup

Use the "**Sync & Backup**" or "**Cloud Drives**" app to upload data to a cloud storage service or another NAS.

**Advantages**:

● Flexible access to backup data from anywhere.

● Cloud services provide an additional level of data redundancy and security.

**Disadvantages**:

● Requires a stable network connection, and backup speed depends on network performance.

● May incur additional cloud storage costs.

● Relies on third-party services and may involve privacy and security risks.

## Replace and Repair Drives One by One (Repeat Cycle)

Follow the sequence below carefully and perform the "**Disable→ Replace→ Repair**" cycle for each old drive. Replace only one drive at a time, and wait for the repair to finish before replacing the next drive.

## PC Instructions

### Phase 1: Locate and Replace the Drive

1. Open the **"Storage"** app. In the left sidebar, click **"Hard Drive"**, then identify the drive numbers included in the target storage pool (for example, Drive 1 and Drive 4).

2. Select the old drive you want to replace. Click "**···**" on the right > "**Disable**" > "**Confirm**", enter the password for your login account, then click **"Confirm"**.

![](https://file-us.ugreennas.com/admin/article/2026-09-10/885a7575d3ce40bea4026ad6a8ad9268.webp)

**Note**: Once the drive is disabled, the storage pool will enter the **"Degraded"** state. The system may sound a warning beep, which can be turned off in Control Panel.

![](https://file-us.ugreennas.com/admin/article/2026-09-10/e8d1eb7b6f0f46a39b7d113d5e9aeb72.webp)

3. Power off the NAS, remove the disabled old drive, and insert the new larger-capacity drive. Make sure the new drive is securely installed, then power the NAS back on.

### Phase 2: Repair the Storage Pool

1. After the NAS starts, open the **"Storage"** app. The system will notify you that the storage pool is degraded.

![](https://file-us.ugreennas.com/admin/article/2026-09-10/f37a8a6bbdcb47619823bffafbac0d4e.webp)

2. Click the affected storage pool to open its details page, then click "**Repair**".

![](https://file-us.ugreennas.com/admin/article/2026-09-10/d8d40bfb4907480e888a2a4bf9193017.webp)

3. In the wizard, select the newly inserted drive as the replacement drive, then click **"Apply"**.

![](https://file-us.ugreennas.com/admin/article/2026-09-10/4d23da45b72b4cedb1896bc5b602cd04.webp)

4. Click "**Format**", verify the password for your login account, then click "**Confirm**". The system will begin rebuilding the data.

![](https://file-us.ugreennas.com/admin/article/2026-09-10/0d6973d86b914c0097af03f5d3bf7f3a.webp)

**Notes**:

● Wait for the rebuild to complete. This may take several hours to several days, depending on drive capacity and the amount of data.

● Do not remove the next drive until the progress reaches **100%** and the storage pool returns to the **"Normal"** state.

![](https://file-us.ugreennas.com/admin/article/2026-09-10/d7834af735ea4706a00ffbde41fdb88b.webp)

### Phase 3: Repeat the Process

After the first drive has been replaced and the repair is complete, repeat the **"Disable→Replace→Repair"** process for the next old drive in the storage pool. Continue until all old drives have been replaced.

### Phase 4: Expand the Storage Capacity

After all drives in the storage pool have been replaced with larger-capacity drives and the final repair is complete:

1. Go to **"Storage" > "Storage"** and check whether the storage pool capacity has been updated automatically.

2. If the storage pool has expanded but the Volume capacity has not changed, locate the Volume and click "**···**" on the right > "**Expand**". Expand the file system to the maximum available capacity, then click "**Apply**".

![](https://file-us.ugreennas.com/admin/article/2026-09-10/35c7940460ec4bf3b82a24d2aee29ad2.webp)

## Mobile Instructions

### Phase 1: Locate and Replace the Drive

1. Open the **"Storage"** app and click **"Hard Drive"** at the bottom to open the drive list. Find the target storage pool and confirm the drive numbers it contains (for example, Drive 1 and Drive 2).

2. Select the old drive you want to replace and click it to open the details page. Click **"Disable"** > **"Disable"**, enter the password for your login account, then click **"Submit"**.

![](https://file-us.ugreennas.com/admin/article/2026-09-10/c53ae445f1184637b8830ad953926929.webp)

**Note**: Once the drive is disabled, the storage pool will enter the **"Degraded"** state. The system may sound a warning beep, which can be turned off in Control Panel.

![](https://file-us.ugreennas.com/admin/article/2026-09-10/6d10ae7218c0428a8656d3eec7f455a1.webp)

3. Power off the NAS, remove the disabled old drive, and insert the new larger-capacity drive. Make sure the new drive is securely installed, then power the NAS back on.

### Phase 2: Repair the Storage Pool

1. After the NAS starts, go to **"Storage" > "Storage"**. The system will notify you that the storage pool is degraded.

2. Click the affected storage pool to open its details page, then click "**Repair**".

![](https://file-us.ugreennas.com/admin/article/2026-09-10/37afcbec4e0f40e1b15b30d927886aba.webp)

3. In the wizard, select the newly inserted drive as the replacement drive. Click **"Repair"**.

![](https://file-us.ugreennas.com/admin/article/2026-09-10/d3de77810e00492c89b6bdc828864cd9.webp)

4. Click "**Continue**", verify the password for your login account, then click "**Submit**". The system will begin rebuilding the data.

![](https://file-us.ugreennas.com/admin/article/2026-09-10/1d69721242194852b6ad8e436b690ff1.webp)

**Notes**:

● Wait for the rebuild to complete. This may take several hours to several days, depending on drive capacity and the amount of data.

● Do not remove the next drive until the progress reaches **100%** and the storage pool returns to the **"Normal"** state.

![](https://file-us.ugreennas.com/admin/article/2026-09-10/14ae566899004d5682079b5e4290f5c9.webp)

### Phase 3: Repeat the Process

After the first drive has been repaired, repeat the **"Disable > Replace > Repair"** process for the next old drive in the storage pool. Continue until all old drives have been replaced.

### Phase 4: Expand the Storage Capacity

After all drives in the storage pool have been replaced with larger-capacity drives and the final repair is complete:

1. Open the **"Storage"** app and check whether the storage pool capacity has been updated automatically.

2. If the storage pool has expanded but the Volume capacity has not changed, click the Volume to open its details page, click **"Expand"**, expand the file system to the maximum available capacity, then click "**Confirm**".

![](https://file-us.ugreennas.com/admin/article/2026-09-10/f3162898a10b4c55bbed4a9c33bc5a40.webp)

## Risk Notice

To help you fully assess whether this operation is suitable for your environment, the following section explains the key risks and technical principles involved:

1. **Secondary Failure Risk**

● **Principle**: During RAID rebuilding, the system performs intensive full-drive reads on all remaining old drives to reconstruct data. This places significant stress on the existing drives.

● **Risk**: If a remaining old drive contains latent bad sectors that have not been detected during normal use, reading one of these sectors during rebuilding may trigger an "**Unrecoverable Read Error (URE)**". This can cause the RAID rebuild to fail and may even result in complete storage pool failure.

2. **File System Failure Due to Power Loss**

● **Principle**: The rebuild process involves extensive metadata writes and parity calculations.

● **Risk**: An unexpected power outage during rebuilding may cause logical sector corruption and prevent the file system from mounting. We recommend equipping the NAS with a UPS (Uninterruptible Power Supply).

3. **Sector Format Compatibility Issues**

● **Principle**: Some large-capacity enterprise drives use the 4Kn sector format, while older drives may use 512e.

● **Risk**: Mixing drives with different sector formats in the same RAID group may prevent the array from being created or significantly reduce performance. Contact customer support to confirm compatibility before purchasing new drives.

4. **Time Cost**

● **Explanation**: Rebuilding more than 10 TB of data typically takes 10-20 hours or longer. With four drives, the entire expansion process may take 3-4 days. NAS performance may be significantly reduced during this period, affecting normal use.

## FAQs

### Q1: Why Didn't the Capacity Increase After I Replaced a Drive?

RAID capacity is limited by the **smallest** drive in the array. For example, in a three-drive RAID 5 array, replacing only one drive with a larger drive will not increase the total capacity. The capacity increases only after **all** three drives have been replaced one by one.

### Q2: If I Remove One Drive During RAID 5 Expansion, Will My Data Still Be Available?

Yes. RAID 5 can tolerate one missing drive. After one drive is removed, the system reconstructs the missing data in real time using parity information from the remaining drives, so the data remains accessible. However, the array has no fault tolerance during this period. If another drive fails, all data may be lost.

### Q3: Can I Access Files During the Expansion Process?

Yes. However, because the system is performing intensive data rebuilding in the background, read and write speeds may be noticeably slower and temporary lag is normal. Minimize large file read/write operations to avoid extending the rebuild time.

### Q4: Why Is the NAS Beeping During the Expansion Process?

When the storage pool is in the "**Degraded**" state, the NAS beeps to alert you to the device status. You can turn off the buzzer in "**Control Panel**" > "**Hardware & Power**", but we recommend keeping it enabled so you can quickly notice device issues.
