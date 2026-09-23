# External Storage

> **Article ID**: `254`  
> **Category**: `Application Guide > Storage > External Storage`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/254  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS).

**Applicable Version**: NAS Firmware 1.17.0.0031 or later.

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

UGREEN NAS supports managing external storage devices in the Storage App. After connecting a USB storage device, you can view device information, access files, format the device, or safely eject the device.

External storage devices include:

● USB flash drives

● Portable hard drives

● SD cards

● TF cards

● Other recognizable USB storage devices

## Supported External Storage Device File System Formats

Supported file system formats: btrfs, ext2, ext3, ext4, vfat, exfat, FAT16, FAT32, NTFS, and XFS.

Unsupported file system formats: HFS+ and APFS (mainly macOS-exclusive file systems).

## Accessing External Storage

1. Open the Storage App.

2. Click "**External Storage**" in the left sidebar to enter the external storage page.

## View External Storage Devices

After entering the External Storage page, you can view the connected external storage devices. The page displays the following information:

● External storage name

● Manufacturer

● Product name

● Total capacity

● Partition information

● File system

● Used capacity and total capacity

If the device contains multiple partitions, the system displays each partition separately.

Click the "**···**" icon on the right side of the external storage device to view more options.

![](https://file-us.ugreennas.com/admin/article/2026-07-28/e5fca51ef3e841949911698e213a1d96.webp)

## Access Files on External Storage

1. Go to "**External Storage**" > "**External storage**".

2. Find the external storage device you want to access, then click "**···**" on the right side of the device ＞ "**Access file**".

The system will redirect you to the Files page, where you can view, copy, move, or manage files on the external storage device.

### Format an External Storage Device

1. Go to "**External Storage**" > "**External storage**".

2. Find the external storage device you want to format, then click "**···**" on the right side of the device ＞ "**Format**".

3. Select the format target and file system, then click "**Confirm**".

![](https://file-us.ugreennas.com/admin/article/2026-07-28/32c5f9a579a64678bbb466d688e3c98b.webp)

4. A confirmation window will appear. Click "**Confirm**" to start formatting.

**Note**: Formatting will erase all data on the external storage device. Make sure important files have been backed up before proceeding.

### Eject an External Storage Device

1. Go to "**External Storage**" > "**External storage**".

2. Find the external storage device you want to remove, click "**···**" on the right side of the device ＞ "**Eject**".

3. Wait until the system prompts that the operation is complete before disconnecting the device.

Directly disconnecting the device may cause file corruption or data loss, especially during file transfer, writing, or formatting. Do not remove the device directly during these operations.

## Advanced Settings

On the "**External Storage**" page, click "**Advanced settings**" at the top to manage external storage-related policies.

![](https://file-us.ugreennas.com/admin/article/2026-07-28/541653b3a54e43229a274bea222fa77d.webp)

### Ext4 latency configuration

**Ext4 latency configuration** can improve the write performance of external storage devices. After enabling this feature, write performance will be improved. However, you must use "**Eject**" before removing the external device. Failure to properly eject the device may result in data loss.

If there are no specific performance requirements, it is recommended to keep the default settings.

### USB storage device settings

You can configure whether to allow USB storage devices to connect to the NAS. The following options are available:

● **Allow**

● **Deny**

If set to "**Deny**", the system will block access to USB storage devices, such as USB flash drives, external hard drives, SD cards, and TF cards.

This setting is suitable for scenarios where access to external devices needs to be restricted.

### External storage access permissions

You can configure the default file access permissions for standard users on external storage devices. The following options are available:

● **Allow**

● **Deny**

This permission applies to external storage devices, including USB storage devices and external storage arrays.

If set to "**Deny**", standard users cannot access files on external storage devices.

## Mount a Third-Party System Drive as External Storage

UGREEN NAS supports mounting drives containing third-party system data as external storage. After mounting, you can access the data on the drive in External Storage.

This feature supports the following access modes:

● **Read-only**: Allows viewing and copying files only. Data on the drive cannot be modified.

● **Read/Write**: Allows viewing, copying, writing, modifying, and deleting files.

### Before Use

This feature only applies to drives installed in the drive bays of the NAS device. The drive must also contain recognizable third-party system data.

If the drive is not installed in the NAS drive bay, or the drive does not contain recognizable third-party system data, it cannot be mounted as external storage using this method.

### Steps

1. Open the **Storage** App, then click "**Hard Drive**" in the left sidebar.

2. Find the hard drive you want to mount, click "**···**" on the right side of the hard drive ＞ "**Use**".

3. In the **Use hard drive** window, select "**External storage**".

![](https://file-us.ugreennas.com/admin/article/2026-07-28/3b79ca1d0d664e719f9fcb37d6cac512.webp)

4. In the access mode window, select "**Read-only**" or **"Read/Write**", then click "**Confirm**".

![](https://file-us.ugreennas.com/admin/article/2026-07-28/12d3d910a6234e47ae4dd5af913142a7.webp)

5. The system will require password verification. Enter the password of the currently logged-in administrator account. After successful verification, the system will mount the hard drive to **External Storage**.

After mounting is complete, you can go to **External Storage** to view and access the hard drive.

## What to Do If an External Storage Drive Cannot Be Formatted?

When formatting an external storage drive, if the system indicates that formatting cannot be performed or the Format button is grayed out and unavailable, it may be related to the device status, connection status, or drive type. Check the following possible causes one by one.

### The External Drive or Partition Is Being Formatted

If a formatting task is already in progress, the system cannot perform another formatting operation at the same time.

Wait until the current formatting task is complete, then try again.

### The Array Device Does Not Support Direct Formatting

If the external storage device is an array device, such as a hardware RAID array, the system cannot format it directly.

For these devices, it is recommended to use the array device's own management tools for formatting or initialization.

### The External Drive Is Locked

Some drives have security encryption, write protection, or locking features. If the drive is locked, the system may not be able to format it.

Disable encryption, remove write protection, or unlock the drive before trying to format it again.

### The Drive Does Not Exist or Is Not Properly Connected

If the external drive is not recognized by the system or the connection is abnormal, formatting may not be available.

Check the following:

● Whether the drive is properly connected.

● Whether the USB port is working properly.

● Whether the drive has a stable power supply.

● Whether the data cable is loose or damaged.

● Whether the device is displayed on the External Storage page.

If the above issues have been ruled out but the drive still cannot be formatted, try the following methods:

1. Reconnect the external drive and try formatting again.

2. Change the USB port or data cable and try again.

3. Connect the drive to a computer to check and repair partition issues.

4. Check whether the drive has physical damage.

5. Confirm whether the drive is encrypted, locked, or write-protected.

## Related Links

● [How to Mount a Hard Drive from Another UGREEN NAS Device as External Storage in UGOS Pro?](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTMyNSwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0MzksImFydGljbGVWZXJzaW9uIjoiMS4wIiwicGF0aENvZGUiOiIifQ==)

● [Migrating Hard Drives to a New UGREEN NAS Device](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmNzY3IiwiY2xpZW50VHlwZSI6IlBDIn0=)

● [UGREEN NAS Private Cloud Compatibility Guide](https://www.ugnas.com/compatible)
