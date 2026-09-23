# Migrating Hard Drives to a New UGREEN NAS Device

> **Article ID**: `767`  
> **Category**: `Application Guide > Storage > FAQ > Migrating Hard Drives to a New UGREEN NAS Device`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/767  

---

**Applicable Version:** UGOS Pro System 1.10.0 and above.

**Applicable Devices:** UGREEN NAS devices running the UGOS Pro system.

## Feature Overview

UGREEN NAS supports hard drive migration between different devices, allowing users to retain their original data and storage structure when upgrading or replacing devices.

You can complete the migration in either of the following two ways:

● Method 1: Migration via External Storage Mount

● Method 2: Direct Internal Storage Migration

If you only need to transfer file data (such as documents, photos, or videos), it is recommended to mount as "**External Storage**" — this method is flexible and low-risk.

If you wish to continue using the original NAS storage structure on the new device, it is recommended to migrate as "**Internal Storage**", as the system will automatically recognize the existing data structure.

This document provides preparation steps, detailed procedures for both migration methods, and recommended migration strategies.

## Migrate as Internal Storage

When you want to use the original NAS's storage structure and data directly on a new NAS, you can migrate the old hard drives as internal storage.

### Preparation and Precautions Before Migration

Before performing the hard drive migration, make sure to complete the following steps to ensure data safety and a smooth migration process.

1. **System Requirements**

● Hard drive migration is only supported between UGREEN NAS devices running the UGOS Pro system.

● Ensure that the system versions of the old NAS and the new NAS are the same or close. It is recommended that the version difference does not exceed one major release.

● A large version gap may cause storage pools to be unrecognized or lead to data errors.

2. **Data and Configuration**

● The migration process does not transfer system configurations, user information, or installed applications — only the data drive contents will be migrated.

● User accounts and permissions must be recreated on the new device. If you have a system configuration backup, you can restore it after migration.

● To back up or restore system configurations, go to the **"Control Panel"** and perform the operation under "**Update & Restore**">"**Configuration backup & restore.**"

![](https://file-us.ugreennas.com/admin/article/2026-03-11/7997f2d325eb40c1bf0e1e32c35124d1.webp)

3. **Application Limitations**

Applications such as **Docker** and **Virtual Machine** do not support lossless migration. They need to be reinstalled and redeployed on the new device.

Before migration, if the storage pool status is displayed as "**Degraded**", go to "**Storage**">"**Storage pool & volume**", locate the corresponding storage pool, and perform a "**Storage pool repair**" operation.

4. **Check Hard Drive Health Status**

Before migration, it is essential to check the status of all hard drives to ensure they are functioning properly.

● Open the "**Storage**", select "**Hard Drive**", and verify that all drives show a **"Normal"** status.

● If any drive shows an abnormal status (such as "**Warning**" or "**Damaged**"), replace the drive before migration to avoid data corruption or RAID degradation during the process.

![](https://file-us.ugreennas.com/admin/article/2026-03-11/27a4ac63d899479da66c544c6fcd8efc.webp)

● Shut down the device, and record the slot order of all hard drives. It is recommended to keep the same order when installing them in the new device.

5. **Verify Drive Compatibility and Quantity**

● For RAID arrays, make sure to insert all member drives at once.

● The new device must have a number of drive bays equal to or greater than the old device.

● Refer to the [UGREEN NAS Products Compatibility List](https://nas.ugreen.com/pages/compatibility) for supported hard drive models.

6. **Maintain Stable Power and Network**

● Ensure that the device remains powered on and does not restart during migration.

● It is recommended to connect the NAS to a UPS to prevent unexpected power outages.

### Steps

1. Install the internal hard drives from the old NAS into the new NAS, then power on the device and log in to the system management interface.

2. Open the "**Storage**", go to "**Hard Drive**">"**HDD/SSD**", locate the migrated drives, and click "**···**">"**Use**" on the right side.

![](https://file-us.ugreennas.com/admin/article/2026-03-11/8c9ea7cdc07b434780c5dfde75e7100d.webp)

3. In the "**Use hard drive**" interface, select "**Internal storage**" and follow the on-screen instructions to complete the setup.

![](https://file-us.ugreennas.com/admin/article/2026-03-11/4bdbf0c5625c48cd9ed31447b576c266.webp)

4. After the setup is complete, the new device will automatically recognize the original storage pool, and the existing data will be directly accessible.

## Mount Drives as External Storage

When you only need to access data from the old NAS or copy certain files to the new device, you can mount the drives as external storage.

### Steps

1. Open the "**Storage**", go to "**Hard Drive**">"**HDD/SSD**", locate the migrated drives, and click "**···**">"**Use**" on the right side.

2. In the pop-up window, select "**External storage**."

![](https://file-us.ugreennas.com/admin/article/2026-03-11/a8e059fc19a144f8ab11ef38eb4085bd.webp)

3. Enter your password to verify your identity.

![](https://file-us.ugreennas.com/admin/article/2026-03-11/a2173636978a4439873cab7f93d54cbd.webp)

4. Once mounted successfully, the external drives will appear in "**External Storage**".

![](https://file-us.ugreennas.com/admin/article/2026-03-11/fd61d8eb3f944b368b06a54c300852a7.webp)

You can access the data using either of the following methods:

● Method 1: In "**External Storage**", find the mounted drive and click "**···**">"Open".

![](https://file-us.ugreennas.com/admin/article/2026-03-11/f4d7a2ba63634dafbb1473006f10c168.webp)

● Method 2: Open the "**Files**" and view the file contents under "**Peripheral**".

![](https://file-us.ugreennas.com/admin/article/2026-03-11/bdab38196d2a43d8b33c7ea133db359b.webp)

### Unmount Drives

If you no longer need to use the external storage, open the "**Storage**", go to "**External Storage**", locate the mounted drive, and click "**···**">"**Remove**" to safely unmount the drive.

### Prompt: "Hard drives are insufficient." When Used as External Storage?

If this message appears, it means the drive is part of a RAID array, which requires all member drives to be inserted at the same time for proper recognition. For example, a RAID 5 array must have all 3 drives inserted simultaneously to be detected correctly.
