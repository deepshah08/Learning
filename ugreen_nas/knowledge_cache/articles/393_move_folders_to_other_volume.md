# Move Folders to Other Volume

> **Article ID**: `393`  
> **Category**: `Application Guide > Storage > FAQ > Move Folders to Other Volume`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/393  

---

## Applicability

**Applicable client**: UGREEN NAS PC Client (Windows/macOS).

**Applicable version**: NAS firmware 1.17.0.0031 and later.

The descriptions in this document are for reference only. The actual interface and operation paths may vary due to system or App updates, please refer to the actual interface.

## Introduction

UGREEN NAS supports changing the Storage location of folders. Personal folder and shared folders can be moved to other Volume.

The system does not support directly migrating storage pools. Since folders are created under Volume, you need to move folders to the target Volume instead.

If you replace or add a new hard disk and want to migrate folders to the new disk, complete the following steps first:

1. Create a storage pool using the new hard disk.

2. Create a Volume in the storage pool.

3. Move Personal folder or shared folders to the new Volume.

## Move the Storage Location of Personal Folder

1. Open the Files App, click "**Management**" ＞ "**User Folder management**" in the top bar.

![](https://file-us.ugreennas.com/admin/article/2026-07-28/0d7f53732848462586078263adbaa915.webp)

2. In the **User Folder management** window, find "**Storage location**".

3. Click the Storage location drop-down menu, select the target Volume, and click "**Confirm**".

![](https://file-us.ugreennas.com/admin/article/2026-07-28/234c2d2afbe2457f9bbf4c3405fd4f25.webp)

4. In the risk warning pop-up window, select "**I understand the risks for this operation and agree to continue**", then click "**OK**".

![](https://file-us.ugreennas.com/admin/article/2026-07-28/4f248369f2a04e56ad751bf3b8e3b603.webp)

The system will check the available capacity of the target Volume and start the migration.

During the migration process, all users’ Personal folder will be temporarily unavailable. Please wait until the migration is complete before accessing Personal folder.

![](https://file-us.ugreennas.com/admin/article/2026-07-28/d8d2df0a74364c5a93d2d622840e7066.webp)

## Move the Storage Location of Shared Folder

1. Open the Files App, click "**Management**" ＞ "**Shared folder management**" in the top bar.

2. In the **Shared folder management** window, find the shared folder you want to migrate. Hover over the shared folder and click "**Edit**".

3. In the **Edit shared folder** window, go to the "**General**" tab and find "**Storage location**".

4. Click the Storage location drop-down menu, select the target Volume, and click "**Confirm**".

5. In the risk warning pop-up window, select "**I understand the risks for this operation and agree to continue**", then click "**OK**".

![](https://file-us.ugreennas.com/admin/article/2026-07-28/9514765e8b834206b1267179c33e7096.webp)

The system will check the available capacity of the target Volume and start the migration.

During the migration process, the shared folder being migrated will be temporarily unavailable. Please wait until the migration is complete before accessing the shared folder.

## Why Can’t I Change the Storage Location of Personal Folder?

If the system indicates that snapshot files exist in Personal folder, you need to delete the related snapshots before continuing to migrate Personal folder. Follow the steps below:

![](https://file-us.ugreennas.com/admin/article/2026-07-28/48b784f3468946d19a662314d813d410.webp)

1. In the prompt pop-up window, click "**Go to delete**". The system will redirect to the Snapshot App.

2. In the User Folder list of the Snapshot App, find the folder that displays the number of snapshots, and click "**Snapshot list**" in the folder’s operation menu.

![](https://file-us.ugreennas.com/admin/article/2026-07-28/4cd47434332441a2909709762f676ab7.webp)

3. In the Snapshot list, click "**···**" ＞ "**Delete**" on the right side of the snapshot.

4. In the secondary confirmation pop-up window, click "**Delete**" again.

5. Repeat the above steps to delete all snapshots of user folders that contain snapshots.

After deletion, return to the Files App and perform the Personal folder Storage location migration operation again.

**Note**: After deleting snapshots, the related snapshot data cannot be restored through the Snapshot App. Please make sure you no longer need these snapshot files before deleting them.

## Notes

● Before migration, make sure the target Volume has sufficient available capacity. Insufficient capacity on the target Volume will cause the migration to fail.

● During the migration process, keep the device powered on. Do not manually shut down or restart the device.

● Moving folders requires transferring data between different physical locations. The migration speed is affected by hard disk performance, the number of files, file size, and file system processing.

● If the amount of data to be migrated is large, organize and migrate files in batches to reduce the load of a single migration.
