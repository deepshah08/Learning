# Hard Drive

> **Article ID**: `314`  
> **Category**: `Application Guide > Storage > Hard Drive`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/314  

---

**Applicable Version**: UGOS Pro firmware 1.9.0.0062 and later

**Note**: The screenshots and interfaces in this document are for reference only. The actual display may vary depending on the system or application version. Some features may be adjusted in different versions. Please refer to your actual interface for accuracy.

The Hard Drive module is used to monitor the operating status, health condition, and basic attributes of all physical drives in the NAS. Here, you can perform S.M.A.R.T. tests, create status test plans, locate the physical position of a drive, or erase drive data.

## Feature Differences Across Series

UGREEN NAS provides different storage management features across product series. Before proceeding, please confirm your device model and supported features to ensure proper hard drive and storage management.

● **DXP Series**: Supports the full "**Locate hard drive**" feature, allowing you to quickly identify a specific drive bay within Hard Drive module for easier maintenance and replacement.

● **DH Plus Series**: Does not support the "**Locate hard drive**" feature and cannot directly control the drive indicator lights on the NAS to locate a drive.

**Notes:**

1. If you need to quickly locate a specific drive in a multi-bay device (such as when replacing a failed drive or expanding storage), the DXP Series is recommended.

2. When using the DH/DH Plus Series, please manually identify the corresponding drive by checking the drive number, slot order, and storage pool information.

3. When installing hard drives into a UGREEN NAS, please be aware of the required procedures and potential risks. For for details, please refer to: [Hard Disk Installation Assistant (Hardware Disassembly and Risk Notification)](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmMTM3In0=) .

## Hard Drive List and Status Overview

Go to "**Storage**">"**Hard Drive**" and open the HDD/SSD tab to view information for all drive bays currently installed in the device at a glance:

![](https://file-us.ugreennas.com/admin/article/2026-02-28/d30726af717d44d39190459448c6c2bd.webp)

● **Basic Information**: Displays the drive icon, slot name (such as Hard Drive 1), health status (such as "**Normal**"), drive type (HDD/SSD), total capacity, real-time temperature, and the storage pool it belongs to.

● **Action Menu**: Click the "**···**" icon on the right side of a drive to open the function menu, where you can view detailed information, perform status tests, locate the drive, disable it, or erase data.

## Hard Drive Operation Features

The available operations vary depending on whether the drive has been assigned to a storage pool.

### For "Unused" Drives

![](https://file-us.ugreennas.com/admin/article/2026-02-28/507c98c135094b258b4bd16bcfdb0be0.webp)

When a drive status is shown as "**Unused**", you can assign it or perform basic maintenance operations.

1. **"Use" Option**

After clicking "**Use**" in the drive action menu, the system will provide the following options based on the current NAS storage environment:

● **Create Storage Pool**: Use this drive to create a brand-new storage pool.

● **Repair Storage Pool**: This option appears only when there is a RAID storage pool in a "**Degraded**" state. It allows you to add this healthy drive to the array to repair the degraded storage pool.

![](https://file-us.ugreennas.com/admin/article/2026-02-28/cd5ae7f5b41d4444954cb3d6dba1070b.webp)

**Hot Spare Drive**: This option appears when there is a RAID storage pool in the NAS. It allows you to assign the drive as a hot spare. If a drive in the storage pool becomes at risk or fails, the system will automatically activate the spare drive to replace it, significantly improving data security.

**Note**: The target storage pool must be in a "**Normal**" state. If it is degraded or in another abnormal state, this feature cannot be configured.

● **Change RAID Type**: Used to adjust the RAID type of an existing storage pool. For example, you can upgrade a storage pool from Basic mode to RAID 1 without data loss, or from RAID 1 to RAID 5.

● **Add to Storage Pool**: Add this drive as an expansion drive to an existing JBOD storage pool to increase overall storage capacity.

● **Replace Hard Drive in the Storage Pool**: This option appears when there is a RAID storage pool in the NAS. You can use it to seamlessly replace an existing drive in a RAID storage pool with a new one.

**Note**: As with a hot spare drive, the target storage pool must be in a "**Normal**" state to perform the replacement.

● **External Storage**: If the drive was removed from another (non-UGREEN NAS) device and installed in the current NAS, you can use this option to mount it directly as external storage to access the files stored on it.

● **Internal Storage**: If the drive was removed from another UGREEN NAS device and installed in the current NAS, you can use this option to fully migrate the original data on the drive to the current NAS. For details, please refer to [Migrating Hard Drives to a New UGREEN NAS Device](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmNzY3In0=) .

![](https://file-us.ugreennas.com/admin/article/2026-02-28/3b93bb0c884e4bc6a9b2a54288b37a35.webp)

### For "In-Use" Drives

When a drive already belongs to a storage pool or SSD cache, the following operations are available:

● **Disable**: Safely remove the drive from the current storage pool, SSD cache, or external storage.

Disabling a drive will cause the corresponding storage pool or SSD cache to enter a "**Degraded**" state. Please proceed with caution, as this may increase the risk of data loss.

![](https://file-us.ugreennas.com/admin/article/2026-02-28/d94d268ac32c4d49bafa3856c9ad1bd0.webp)

● **Other Basic Features**: Including detailed information, status tests, and locate hard drive.

## Basic Features

In addition to assigning usage, you can perform the following routine management operations on "**Unused**" drives:

● **Detailed Information**: View the drive's brand, capacity, temperature, and S.M.A.R.T. attribute parameters.

● **Status Tests**: Manually run a drive diagnostic to detect potential bad sectors or hardware failures.

● **Locate Hard Drive**: Make the indicator light of the corresponding physical slot blink to prevent removing the wrong drive in multi-bay models (Note: Not supported on the DH Plus Series).

● **Data Erasing** : Completely destroy all data on the drive by overwriting it with random data to prevent privacy leaks.

### View Hard Drive Detailed Information

In the hard drive list, click the "**···**" icon on the right side of any drive and select "**Details**" to view its detailed parameters:

**Operating Status:**

● Displays health status, temperature, power-on time, reallocated sector count, and other data.

● Provides key data charts (such as reallocated sector count and spin retry count) to help assess drive stability.

![](https://file-us.ugreennas.com/admin/article/2026-02-28/c84501122a2f42faa4e747e5748151ed.webp)

**Basic Attributes:**

● Lists hardware information including brand, model, serial number (SN), firmware version, rotation speed, and interface protocol.

● You can also click "**Test**" on this page to evaluate the drive's read and write performance.

![](https://file-us.ugreennas.com/admin/article/2026-02-28/010e2cf1da544276af25314327a048a3.webp)

**S.M.A.R.T. Information:**

● Displays the drive's underlying S.M.A.R.T. attribute parameters (such as underlying data read error rate and spin-up time).

● Supports switching between "**Basic**" and "**Advanced**" views for professional troubleshooting.

![](https://file-us.ugreennas.com/admin/article/2026-02-28/baa802c0a5c842b381de190a85450917.webp)

### Hard Drive Status Test

Regular drive checks help detect potential failures early and protect data security. You can run a one-time manual test or configure a scheduled automatic status test plan.

**Manual Test:**

1. In the hard drive list, click the "**···**" icon on the right and select "**Status test**".

![](https://file-us.ugreennas.com/admin/article/2026-02-28/b8834ec61a6c46afb2d13fe0f5d2cdb1.webp)

2. In the pop-up window, click "**Test**". The system will perform a S.M.A.R.T. test and generate a report.

3. After the test is completed, you can view previous records under "**History**".

![](https://file-us.ugreennas.com/admin/article/2026-02-28/c0f3d0f12c2f449c90b25fa775432773.webp)

**Scheduled Automatic Test Plan**

1. Click the "**Status test plan**" tab in the top navigation bar, then click "**New plan**".

![](https://file-us.ugreennas.com/admin/article/2026-02-28/8f650bb2f0304f1787429e9ceecc1468.webp)

2. Set a plan name and select the target hard drives.

3. Choose the test type (such as rapid test or full test) and the test frequency (such as one-time or monthly).

4. It is recommended to schedule the test during periods of low drive activity (such as late at night or in the morning) to avoid affecting read and write performance.

![](https://file-us.ugreennas.com/admin/article/2026-02-28/38136aa4de1d44309378358e5e18af1d.webp)

### Locate Hard Drive (Physical Identification)

When physically removing or inserting a drive, this feature helps prevent removing the wrong one. After it is enabled, the indicator light of the corresponding slot on the NAS will turn **green** and blink. You can set the blinking duration (for example, 1 minute).

![](https://file-us.ugreennas.com/admin/article/2026-02-28/db3f978a2b6f45b393d88b27f2780990.webp)

### Data Erasing

This feature applies only to unused drives. The system will overwrite the drive with random data, mainly used to prevent privacy leaks when retiring old drives. For more information, please refer to [What is Data Erasure?](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmMzEwIn0=)

● **Operation**: In the hard drive list, click the "**···**" icon on the right and select "**Data Erasure**".

● **Warning**: This operation is irreversible. Once erased, the data cannot be recovered through conventional methods.

![](https://file-us.ugreennas.com/admin/article/2026-02-28/be9177b2ed5c431bbfa220ed0c142981.webp)

## Advanced Settings

In the "**Advanced settings**" tab, you can manage global drive warning policies:

● **Bad Sector Warning**: It is recommended to keep this option "**Enabled**". When enabled, if the number of bad sectors on a drive increases significantly, the system will send a notification indicating a potential sign of drive failure.

![](https://file-us.ugreennas.com/admin/article/2026-02-28/f225088276f54a32a92969a00fa9b974.webp)
