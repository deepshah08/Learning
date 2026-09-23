# Connect External Storage Devices (SD Cards/USB Flash Drives) and Manage Files

> **Article ID**: `923`  
> **Category**: `Application Guide > Files > Connect External Storage Devices (SD Cards/USB Flash Drives) and Manage Files`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/923  

---

## Applicability

**Applicable Version**: NAS Firmware 1.18.0.0093 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

NAS supports connecting external storage devices such as SD cards, USB flash drives, and external hard drives. After a device is successfully connected, users can directly browse files stored on the device and perform file management operations such as copying, moving, and deleting files, making data migration and backup more convenient.

The supported and unsupported file system formats for external storage devices are as follows:

● Supported file system formats: btrfs, ext2, ext3, ext4, vfat, exfat, FAT16, FAT32, NTFS, XFS.

● Unsupported file system formats: HFS+ and APFS (file systems primarily used by macOS).

## Preparation Before Use

● Make sure the NAS is powered on and running properly.

● Prepare an SD card or USB flash drive.

## Steps

1. **Connect an external storage device**

Insert the SD card or USB flash drive into the corresponding port on the NAS (insert SD cards into the SD card slot, and USB flash drives into the USB or Type-C port), then wait for the system to automatically detect the device.

2. **Open Files**

Log in to the UGOS Pro system interface and open the "**Files**" app.

3. **View the external storage device**

Select "**External Device**" in the left navigation bar and find the connected external storage device.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/45bcba4bbd184d89887624eaa7fa4688.webp)

Alternatively, go to "**Storage**" > "**External Storage**" to find the connected external storage device.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/d850714dbac04467bb81decf537d599d.webp)

4. **Browse files**

Open the corresponding device to browse files and folders stored on it. The system supports previewing common file types, including images, documents, audio, and videos.

5. **Manage files**

Users can perform the following operations as needed:

● Create and upload files

● Copy, move, and rename files

● Delete and add files to favorites

● Share and collect files

After completing Files operations, it is recommended to safely remove the device from the system first (right-click and select Eject). Wait until the system indicates that the device can be removed before disconnecting the external storage device to prevent data corruption or loss.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/8963acf7cc1e48ccbec3af564918036b.webp)

## FAQs

### External storage device cannot be recognized

Please check the following:

● Whether the external storage device is properly connected.

● Whether the USB port or SD card slot is working properly.

● Whether the file system format of the external storage device is supported by the NAS.

● Check whether the use of external storage devices is disabled in the advanced settings of Storage.

### Unable to access or copy files

Please check the following:

● Whether the current account has access permissions.

● Whether the external storage device is damaged or write-protected.

● Whether the external storage device has sufficient free space.

## Tips

● Before importing important data, make sure that the NAS has sufficient storage space.

● When copying large files, keep the connection stable and do not power off or disconnect the storage device during the process.

● To ensure data security, use the safe removal feature after completing file operations, and then disconnect the external storage device.

## Related Reading

[External Storage。](https://support.ugnas.com/knowledgecenter/detail/article/en-US/254)
