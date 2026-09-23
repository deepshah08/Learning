# After restoring from a snapshot, files cannot be copied to a directory mounted via NFS. How to fix this?

> **Article ID**: `666`  
> **Category**: `Application Guide > Snapshot > After restoring from a snapshot, files cannot be copied to a directory mounted via NFS. How to fix this?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/666  

---

## **Issue Description**

After restoring a directory using the snapshot feature on UGREEN NAS, if the directory is mounted on a client device via the NFS protocol, the client may be unable to write or copy files to that directory.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250716/cb72900d-e8d0-4fdc-b0cd-079640aca5aa.webp)

## **Cause Analysis**

The snapshot feature relies on the Btrfs file system’s volume management and its read-only/read-write snapshot mechanisms. However, Btrfs is not fully compatible with certain aspects of NFS mounting, such as permission inheritance and handle caching. During the snapshot restore process, changes to the underlying subvolume structure may occur, while the inode information or file handles associated with the mount point are not updated accordingly. This leads to an inconsistent NFS connection state between the client and the NAS, preventing proper write operations.

## **Solution**

As shown in the illustration, go to the "Files" app on the UGREEN NAS and locate the shared folder with NFS permissions configured. Delete the existing mounted client and then remount it. This process refreshes the client cache and re-establishes valid NFS file handles, restoring normal read and write access.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250716/658adc5a-1d6a-4371-ab87-b726916bfecf.png)

## **Notes**

* If you are using NFS on a Windows system, you may also need to restart the mount or refresh the network drivers to restore access.
