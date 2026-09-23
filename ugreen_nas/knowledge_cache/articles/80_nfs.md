# NFS

> **Article ID**: `80`  
> **Category**: `Application Guide > Control Panel > File Service > NFS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/80  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS).

**Applicable Version**: NAS Firmware 1.18.0.0032 or later.

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

NFS (Network File System) is a widely used network file sharing protocol known for its simple configuration, high performance, strong security, broad compatibility, and flexible deployment.

It enables efficient access to shared folders on your NAS across different operating systems and devices, meeting file sharing needs in a wide range of scenarios.

## Enable the NFS Service

1. Open the "**Control Panel**" app, then go to "File Service" > "NFS".

2. Select "Enable NFS service", then click "Apply" to save the changes.

![](https://file-us.ugreennas.com/admin/article/2026-07-22/eb84dd64ec574f01813bf4fc24777981.webp)

3. After the NFS service is enabled, open the "**Files**" app, select the folder you want to share, right-click it, and choose "Properties".

![](https://file-us.ugreennas.com/admin/article/2026-07-22/1303670bde9744a89b15e373ae173a29.webp)

4. Switch to the "NFS Permissions" tab, then click "Add" to configure an NFS permission rule.

![](https://file-us.ugreennas.com/admin/article/2026-07-22/3161163180534fe69f8f6b183cfb773f.webp)

5. In the Add NFS Permission Rule dialog, enter the IP address of the client computer that will mount the NFS share in the Server address field to ensure that only authorized devices can access it. Set the permission to Read only or Read/Write as needed.

![](https://file-us.ugreennas.com/admin/article/2026-07-22/132c41358987452393c9236126422f2c.webp)

6. After verifying the settings, click "Confirm" to save the changes. You can modify the NFS permission rules for the shared folder at any time.

![](https://file-us.ugreennas.com/admin/article/2026-07-22/05119495322642f7af592b7d719e01a9.webp)

## Connect to Your NAS via NFS on Windows

Before you begin, make sure the following requirements are met:

● Your Windows edition supports the NFS Client feature (available in Windows 10 Pro and later).

● The NFS service is enabled on your NAS, and NFS permissions have been configured for the shared folder.

### Enable the NFS Client

1. Open "**Control Panel**", then go to "Programs" > "Programs and Features".

![](https://file-us.ugreennas.com/admin/article/2026-07-22/27947bca314a4fca8e172516d08d5937.webp)

2. Click "Turn Windows features on or off" in the left pane.

![](https://file-us.ugreennas.com/admin/article/2026-07-22/dbeb62aa3d4b42759a11fcfb4dded03a.webp)

3. In the "Windows Features" dialog, locate Services for NFS, select all of its subfeatures, and click "OK" to save the changes.

![](https://file-us.ugreennas.com/admin/article/2026-07-22/fae05d593599490b944f1912f0219cb1.webp)

### Mount an NFS Share

1. Press `Win + R` to open the Run dialog, type `cmd` and press Enter.

![](https://file-us.ugreennas.com/admin/article/2026-07-22/fda972d428e0452a9cd0068e630881e9.webp)

2. In the Command Prompt window, enter the following command and press Enter to mount the NFS share. Command syntax:

```
mount -o anon "\NAS_IP/path/to/share" Drive_Letter:
```

● **NAS\_IP**:The IP address of your NAS.

● **/path/to/share**:The path of the shared folder configured for NFS on the NAS.

● **Drive\_Letter**: The drive letter to assign to the mounted share, such as `N`.

**Example**:

If the shared folder is `/volume1/music`, the NAS IP address is `172.17.70.64`, and you want to assign drive letter `N`, use the following command:

```
mount -o anon "\172.17.70.64/volume1/music" N:
```

![](https://file-us.ugreennas.com/admin/article/2026-07-22/410175ebd3bf4f179e7b3cedf1d4879a.webp)

3. After the share is mounted successfully, you can access it in File Explorer using the assigned drive letter (for example, `N:`).

![](https://file-us.ugreennas.com/admin/article/2026-07-22/925aef1a13f84eb58228b3b8c6c0d784.webp)

## Advanced NFS Settings

The advanced NFS settings help optimize performance and compatibility. You can configure the maximum supported NFS protocol version and specify fixed ports for `statd` and `nlockmgr`. Using fixed ports simplifies firewall configuration and ongoing maintenance.

**Maximum NFS Protocol**:

The "Maximum NFS Protocol" setting determines the highest NFS protocol version that clients can use when connecting to the NAS. Currently, only NFSv3 is supported.

**NFSv3**

● Advantages: Widely supported, offers good performance, supports large files, and features improved file locking and asynchronous write operations.

● Limitations: Does not support enhanced security features (such as Kerberos authentication) or state recovery.

**statd port**

● Function: Manages NFS lock status, tracks the state of NFS clients, and restores file locks after a client or server restarts following a crash.

● Default Port: Dynamic. Assigning a fixed port simplifies firewall configuration.

**nlockmgr port**

● Function: Manages NFS file locks to prevent data conflicts when multiple clients access the same file simultaneously.

● Default Port: Dynamic. Assigning a fixed port simplifies firewall configuration.

## Feature Descriptions

**Server Address**

● The IP address or hostname of the NFS client that is allowed to access the shared folder.

● You can specify a single IP address, an IP address range, or a subnet (such as `192.168.1.0/24`) to control which clients can access the shared folder.

**Permission**

● Access denied: The client cannot access the shared folder.

● Read-only: The client can read files but cannot modify or delete them.

● Read/Write: The client can read, modify, and delete files.

**Squash**: Controls how client users and groups are mapped when accessing the shared folder.

● **Map root to guest**: Maps the root user on the NFS client to the guest user on the server. Operations performed by the client are executed with guest privileges, improving system security.

● **Map all users to admin**: Maps all remote users and their groups to the anonymous user. All operations on the server are performed using the same anonymous user account, further restricting user privileges and enhancing security.

**Security**

● **AUTH\_SYS**: Uses UID- and GID-based authentication. This is the default security mode commonly used by NFSv3.

**Asynchronous**

● Enabling asynchronous write operations can improve NFS server performance. Data is first stored in the cache before being written to disk in batches.

● If the system crashes before cached data is written to disk, data loss may occur.

**Allow Connections from Non-Privileged Ports (Above 1024)**

● By default, the NFS server accepts connections only from privileged ports (below 1024), as these ports are typically used only by the root user.

● Enabling this option may increase security risks because non-privileged ports can be used by regular users, making it easier for malicious users to launch attacks.

## Why Can't I Access a Folder Through NFS

If a folder is encrypted and the file system of the volume where it is stored is **Btrfs**, the folder cannot be accessed through **NFS**.

If the folder needs to remain encrypted, it is recommended that you use another supported access method, or store the data that needs to be shared over NFS in an unencrypted folder.

### How to Identify the Volume Where a Folder Is Stored

1. Open the **Files** and locate the folder that cannot be accessed or shared through NFS.

2. Right-click the folder and select "**Properties**".

3. Check the path shown in the **Location** field.

The number following `volume` in the path indicates the volume where the folder is stored.

For example:

● `volume1`: The folder is stored on **Volume 1**.

● `volume2`: The folder is stored on **Volume 2**.

### How to Check the File System of a Volume

1. Open the **Storage** and go to the "**Volume**" page.

2. Locate the corresponding volume and check its file system type.

If the file system is **Btrfs** and the folder is encrypted, the folder cannot be accessed through NFS.

## Related Articles

[NFS Protocol Access to Shared Directory Results in "Access Denied" Notification](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMjk0LCJhcnRpY2xlSW5mb0lkIjo0MjcsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)

[Folder names in Chinese display garbled characters after mounting NFS using Windows File Explorer](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTI5NSwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0MjgsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)

[NFS Mounting Prompts "'mount' Is Not Recognized as an Internal or External Command, Operable Program or Batch File"](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMjkzLCJhcnRpY2xlSW5mb0lkIjo0MjYsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)
