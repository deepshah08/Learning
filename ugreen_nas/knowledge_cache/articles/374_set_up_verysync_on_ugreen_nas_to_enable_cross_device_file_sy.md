# Set Up VerySync on UGREEN NAS to Enable Cross-Device File Sync and Sharing

> **Article ID**: `374`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Set Up VerySync on UGREEN NAS to Enable Cross-Device File Sync and Sharing`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/374  

---

VerySync is a tool for cross-device file synchronization and sharing, utilizing P2P technology to achieve file synchronization and backup, providing secure and efficient file transfer. VerySync can be used across platforms, supporting operating systems such as Windows, macOS, Linux, etc. Using Docker to set up a VerySync mirror is a flexible and easy-to-manage method.

### Advantages of Docker Deployment for VerySync

1. **Simplicity**: Docker allows for quick deployment and configuration of VerySync without manual environment setup.

2. **Isolation**: The container environment is isolated from the host system, reducing interference with other system components.

3. **Portability**: Containers can be easily migrated and deployed on different systems.

4. **Easy Management**: Containerized applications facilitate updates, backups, and recovery.

### Search and Download the Image

In the [Image > Image Database], enter the keyword `jonnyan404/verysync` to search. Find the container image you want to download in the search results, and click [Download] or double-click the image to download. Choose the version [latest], click "OK" to start pulling. Wait for the image download to complete.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/9f0f7cd2766d4b5ca6623152d21661f8.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-04/d654690971fc42128c13ea8c7b2f10a2.webp)

## Create and Configure the Container

After the image is downloaded, we start creating the container. In the "Image > Local" list, select the image you just downloaded. Click`+`or double-click the image file to create a container and configure container parameters.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/334f69ad807647d39d2a0913b5acce5c.webp)

### Basic Information Configuration

In the "Basic information" section of the container creation wizard, you can customize the container's name for easy subsequent identification. It is recommended to enable the [Auto restart] option to ensure the container can automatically recover after a system restart or failure.

For CPU and memory limits, the default values usually meet most needs, but you can adjust them according to specific usage scenarios.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/1308bcc2155641c4abc024343e51ee8d.webp)

### Volume Configuration

In the volume configuration step, you need to select a data storage path for the container to ensure persistent storage of data. Configure as follows:

● Click the auto-assign button for `/work`, select the folder to store work materials, and choose **Read/Write** as the type. It is recommended to choose a path under the `/Shared Folder/docker`directory on the NAS, and select "Read/Write" as the type to prevent permission issues during container operation.

● Click the **Automatic distribution** for `/learn`, select the folder to store code, and choose **Read/Write** as the type.

**Volume configuration example:**

|  |  |  |
| --- | --- | --- |
| **File/Folder** | **Mount Path** | **Description** |
| shared folder/docker/VerySync/work | /work | Synchronization folder 1 |
| shared folder/docker/VerySync/dm | /learn | Synchronization folder 2 |

![](https://file-us.ugreennas.com/admin/article/2025-09-04/7e1b384e69c741a4b5054f133b4328cb.webp)

### Network Configuration

In the network configuration section, you need to set the container's network mode and port mapping. It is recommended to use the `bridge` network mode and configure port mapping as follows:

● Customize the NAS port, container port `8666`, and choose **TCP/UDP** as the port type.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250904/34036c5a-9723-47d9-8b9a-1554e4a28fbf.png)

After ensuring the configuration information is correct, click "Confirm" to create the container.

## Access the Container WebUI Interface

1. **Access the Web Interface**: After the container is started, you can access its Web interface through a browser for configuration and management. The access URL is `http://<NAS_IP>:8886`, replace `<NAS_IP>` with your NAS IP address. On the settings page, accept the agreement, set a device name, and then click "GET STARTED".

![](https://file-us.ugreennas.com/admin/article/2025-09-04/bc4efd9e06aa4cafaa9827c4d286d300.webp)

2. **Login**: Click the "LOGIN" button in the upper right corner and log in with your VerySync account. If you don't have an account, you can click "Register now" to create a new one.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/0828c12d8649446396998c0f3f764999.webp)

## VerySync PC Guide

1. **Download the Software:**

● Visit the [VerySync official website](https://www.verysync.com/download.html) and download the software version that matches your computer's system. For example, for the Windows system, choose [Windows 7 or higher] and select 64-bit for download.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/076e1a64ffd2480a85a4a4d6872c807d.webp)

2. **Installation and Setup:**

● After downloading, extract the compressed file, locate the `.exe`file, and click to open it.

● Similar to the container's Web interface, click to accept the agreement and set a device name before proceeding to the main interface.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/470f74630fe24bf8b82818373983bb64.webp)

## Sync Tutorial

Refer to this article for the VerySync tutorial：<https://www.verysync.com/manual/users/start.html#add-folder>

Here's an example of syncing a computer to a NAS:

1. Create a Sync Directory: Open the VerySync software on your computer, click the "Create a new sync" button, and select "Standard folder" from the pop-up menu. Then, choose the folder you wish to share and sync.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/df4c3c1526a84502b1409a047f3ff936.webp)

### Tips

When creating a directory, VerySync defaults to using the selected folder name as the sync directory's name, but you can modify it later in the settings.

2. Upon successful creation of the sync directory, a link and a key for connection will immediately display. You can choose between "read only" and "Read and write" permissions.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/6e0162f113834bd8afc3ccbde82a48f7.webp)

● Read-Only Key: Typically used for sharing with friends or colleagues without granting them the ability to modify or delete your files. If other devices connect using this key, any file additions or modifications to the directory will not sync to other computers, and the data will not affect devices with read-write access keys.

● Read-Write Key: Commonly used for syncing data between multiple devices of the same user, ensuring all operations on the directory are applied to all computers. If other devices connect using this key and perform file additions, modifications, or deletions, the results will sync to all devices connected to that directory.

3. You can also close this first, as it will reappear when you click the "share" button.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/5aaf4cd7c95f489ab95dae197194c8ae.webp)

4. Click the Settings button to make changes, such as modifying the scanning time.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/6be936b808224e2bab96484a3b52e333.webp)

5. In the VerySync app on your NAS, click the "Create a new sync" button and select "Connect key or link" from the pop-up add menu.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/d9db648b11ce4267887fa8b9acd118aa.webp)

6. Enter the link/key that was just displayed, check the box to start syncing immediately after adding, and click "Next."

![](https://file-us.ugreennas.com/admin/article/2025-09-04/1c789a0040ec453abc1f583d452618a7.webp)

7. Change the save path and click "CONNECT".

![](https://file-us.ugreennas.com/admin/article/2025-09-04/312d93880e6244e680130a1537ed71a4.webp)

8. Wait a moment to see the sync status complete, or click Devices to view connected devices.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/d8b38df3cee64b2194e906291f751aca.webp)

9. By following the above steps, you can easily deploy and manage the "VerySync" image on your Greenlink NAS, achieving efficient file synchronization management.

## Tips

● The container's s volume and configured file/folder paths are for reference only; you can create them according to your personal preferences.

● For port configuration, it is recommended to keep the container port and local port for web access consistent. If there's a local port conflict, change it to an unused port. For non-web access, the default is automatic.

● Local ports between containers cannot be the same; port conflicts will prevent container startup.

● The quick access web link is only accessible in bridge mode.

● The image only provides instructions for setting up the container; please search online for tutorials on usage and advanced features.

● The image is developed by a third party; please follow relevant official information for specific configuration changes and bug fixes.

## FAQ

● **Image Download Failure:** If you encounter issues downloading the image, configure Docker's image registry or proxy.

● **Permission Issues:** Ensure that the directory mounted in the container has appropriate read-write permissions to avoid permission denied errors.

● **Connection Issues:** Ensure that firewall and router configurations allow port communication for the container.
