# Connect to the NAS via NFS on macOS

> **Article ID**: `620`  
> **Category**: `Application Guide > Control Panel > File Service > Connect to the NAS via NFS on macOS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/620  

---

## **Prerequisites**

Before you begin, make sure the following conditions are met:

1. **NFS Service Enabled:** The NFS service is enabled in UGOS Pro, and the NFS permission rules have been configured for the shared folders.
2. **Create a Local Mount Point:** Create or select a local folder on macOS to use as the NFS mount point.
3. **Get the local mount point path:** In the "Applications" folder, open "Utilities" > "Terminal". Drag and drop the target mount point folder into the Terminal command line, and the actual path of the folder will be shown in the Terminal. Copy this path.

## **Connect to the NFS share**

Follow the steps below to connect to the NFS share:

1. In the Terminal on macOS, enter the mount command in the following format:

```
sudo mount -t nfs -o resvport NAS_IP:/path/to/share /local/mount/point
```

* **NAS\_IP:** Enter the IP address of the NAS device.
* **/path/to/share：**Enter the path of the NFS shared folder configured on the NAS.
* **/local/mount/point：**Enter the path you want to use as the local mount point on macOS.

**Example:**

If the NAS shared folder is "`bak`", the NAS IP address is "`172.17.70.242`", and the local path on macOS is the "`abc`" folder under "`Downloads`", the command will be as follows:

```
sudo mount -t nfs -o resvport 172.17.70.242:/volume1/bak /Users/ugreen/Downloads/abc
```

2. After a successful mount, the local folder will be replaced by the NAS shared path. You can view and access the NAS share through Finder in the "Downloads" folder, just as you would browse and manage local files.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250624/fcef89e3-306a-4261-8c86-dcfeca2e05a2.png)

3. If you encounter compatibility issues, you can try specifying the NFS version in the mount command. For example:

```
sudo mount -t nfs -o resvport,nfsvers=3 NAS_IP:/path/to/share /local/mount/point
```

## **Notes**

* Make sure the NFS service is enabled on the NAS device, and that the permission rules for the shared folders are configured correctly.
* Ensure that your macOS device and NAS device are on the same network and that the network connection is working properly.
* Confirm that both the NAS share path and the local mount point path are accurate.
