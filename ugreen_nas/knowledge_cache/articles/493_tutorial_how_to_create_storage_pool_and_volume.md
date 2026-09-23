# [Tutorial] How to Create Storage Pool and Volume?

> **Article ID**: `493`  
> **Category**: `Application Guide > Storage > FAQ > [Tutorial] How to Create Storage Pool and Volume?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/493  

---

## Introduction

A **Storage Pool** is a collection of hard drives managed through RAID technology, providing data protection and centralized storage resource management. A **Volume** is a logical storage unit created from a Storage Pool and can be directly used to store data. Multiple Volumes can be created within a single Storage Pool, and each Volume can have its own file system (e.g., Btrfs, EXT4).

## Steps

1. Open the Storage and navigate to "**Storage**" > "**Storage pool & volume**".

2. Click "**Create**" > "**Storage pool**" to enter the storage pool creation wizard.

![](https://file-us.ugreennas.com/admin/article/2026-07-23/4a99857e44e9462cbb2b48c42edb76dc.webp)

3. Select the hard drives and RAID type, then click "Next." Different RAID types offer varying levels of data protection and functionality; refer to "[How to Choose the Right RAID Level for Your Needs](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmMTMyIn0=) " for guidance.

4. Optionally, choose whether to perform a disk check and click "Next".

![](https://file-us.ugreennas.com/admin/article/2026-07-23/2322fdaee9f3480eabcb6c3926a18684.webp)

5. After creating the storage pool, the system will automatically create a volume. You need to set the volume capacity (default is the maximum available capacity, but you can adjust as needed) and select a file system. Then, click "Next" to proceed.

![](https://file-us.ugreennas.com/admin/article/2026-07-23/1f75593500f34f469c4df392f8df5216.webp)

6. Click "Create" to begin initialization.

**Note:** Initialization will format the hard drives, so make sure to back up important data before proceeding.

![](https://file-us.ugreennas.com/admin/article/2026-07-23/23b7692f6dde4e7588e26ea175bac2f6.webp)

7. After confirming the risk warning, click "Format", enter your password to verify, and click" Confirm" to complete the creation process.

![](https://file-us.ugreennas.com/admin/article/2026-07-23/7955f2ff53964ecd8f5944b453b48c6b.webp)

![](https://file-us.ugreennas.com/admin/article/2026-07-23/c2007d637f5b4a409871eeeb3c15ad62.webp)

8. You can continue creating volume based on the remaining capacity of the storage pool. Click **"···"** on the right side of the storage pool and select [Create Volume] to repeat the above steps.

**Note**:Ensure the remaining capacity of the storage pool is greater than 10GB to create a new volume.

![](https://file-us.ugreennas.com/admin/article/2026-07-23/0aaa4a756d394855ae38f887ce593a7a.webp)

## Related Links:

[[FAQ] The relationship between physical disks, storage pool, and storage space](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTI1NywidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiZW4tVVMiLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0MTgsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)
