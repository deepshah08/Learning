# Unable to recognize USB peripheral mounts?

> **Article ID**: `226`  
> **Category**: `Troubleshooting > System and Software Failure > Unable to recognize USB peripheral mounts?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/226  

---

External Storage Devices - Only the following storage formats are supported for external storage mounting:

* - Multi-partition file systems with common MBR or GPT partitions, with at least one file system recognizable by us.
* - Single-disk LVM devices with file systems supported by us in their LV.
* - Multi-disk array devices, with the array combined into one file system supported by us.
* - Multi-disk array devices with the array combined into an LVM device, and file systems supported by us in their LV.

Supported external storage formats on the current system: btrfs, ext2, ext3, ext4, vfat, exfat, FAT16, FAT32, NTFS, XFS.

Unsupported external storage formats: HFS+, APFS.

Internal Hard Drives - Unsupported Hard Drives for Use

* Hard drives with undetected SMART status, or with SMART formatting that deviates from standard, and hard drives whose health status cannot be determined by the system.
