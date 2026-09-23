# Deploying the Syncthing Open-Source File Synchronization Tool on UGREEN NAS

> **Article ID**: `372`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Deploying the Syncthing Open-Source File Synchronization Tool on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/372  

---

Syncthing is an open-source file synchronization tool that allows for secure file synchronization between multiple devices without relying on cloud services. Instead, it syncs directly between devices, ensuring data privacy and security. It supports multiple platforms and can run on systems such as Windows, macOS, Linux, etc.

## Search and Download the Image

In the [Image] > [Image Database], enter the keyword `linuxserver/syncthing` to search. Find the container image you want to download in the search results, and click [Download] or double-click the image to download. Fill in the version number as [latest], and click "Confirm" to start pulling. Wait for the image download to complete.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/98ddb197b33b4dd88b5d94f962a4effd.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-04/fd6f70ca9acf4e0da1494f9171dc2701.webp)

## Create and Configure the Container

Once the image is downloaded, you can start creating the container. In the "[Image] > [Local] list, find and select the downloaded image file. You can enter the container creation wizard for configuration by clicking the "+" button or double-clicking the image file.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/167fb95af44d4487989029572aa13d9e.webp)

### Basic Information Configuration

In the "Basic information" section of the container creation wizard, you can customize the container name for easier identification later. It is recommended to enable the [Auto restart] option to ensure that the container can automatically resume running after a system reboot or failure.

For CPU and memory limits, the default values usually meet most needs, but you can adjust them based on specific use cases.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/ecc8930861934452af4a3171dfe90dd8.webp)

**Environment Variable**

Add the following environment variables to ensure proper container operation:

**● PUID:** The user ID for processes inside the container. Click "Add" and enter the variable PUID. By default, this is the ID of the user creating the container, but it can be adjusted as needed.

**● PGID:** The group ID for the processes. Click "Add" and enter the variable PGID. By default, this is the group ID of the current user.

**● TZ:** Time zone settings. Click "Add" and enter the variable TZ. This ensures that the time inside the container is synchronized with the local time. For example, in Asia you may set it to `Asia/Shanghai`, or configure it based on your geographical location (such as `America/New_York` or `Europe/London`).

|  |  |  |
| --- | --- | --- |
| **Enviroment Variable** | **Default Value** | **Description** |
| PUID | User ID of creator | User ID for processes inside the container |
| PGID | User group ID | User group ID for processes inside the container |
| TZ | Asia/Shanghai | Container time zone setting (default: `Asia/Shanghai`, can be adjusted based on region) |

### Volume Configuration

In the volume configuration step, you need to select a data storage path for the container to ensure data persistence. Configure it as follows:

● For `/config`, click Automatic distribution, then select the folder where the container's configuration files will be stored. It is recommended to select a path under `/Shared Folders/docker` on the NAS, and set the type to Read/Write to prevent permission issues during container operation.

● For `/data`, click Automatic distribution, and choose the folder path where the files to be synced are located.

**Example：**

|  |  |  |
| --- | --- | --- |
| **File/Folder Path** | **Container Mount Path** | **Description** |
| `/Shared Folder/docker/syncthing/config` | `/config` | Store the container's configuration files |
| `/Shared Folder/docker/beta` | `/data` | File path for storing synchronized data |

![](https://file-us.ugreennas.com/admin/article/2025-09-04/e97315a3c1674d6fad3f83a518c4409c.webp)

### Network Configuration

In the network configuration section, you need to set the container's network mode and port mapping. It is recommended to use the`bridge`network mode and configure port mapping as follows:

● Customize the NAS port, map the container port `8384`, type as TCP.

● Customize the NAS port, map the container port`22000`, type as TCP/UDP.

● Customize the NAS port, map the container port`21027`, type as UDP.

**Note:** If other programs are already running on your NAS and occupying ports `22000`or`8395`, such as using Pro system synchronization and backup features, it is recommended to choose other unused ports to avoid port conflicts.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/cb263d6c44b44872b5a465bf4b15fd05.webp)

After ensuring the configuration information is correct, click "Finish" to create the container.

## Access the Container WebUI Interface

1. After the container is started, you can access the container web interface for configuration and management via a browser. Visit the URL `http://<NAS_IP>:8384`, replacing <NAS\_IP> with your NAS IP address.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/a23cc6f8c1bc4e86ab9c32ec2ec58030.webp)

2. For security reasons, it is recommended to set up a username and password for login. Click on "Settings > Graphical User Interface", set the username and password for the graphical management interface on the page, and click "Save" to take effect.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/30a33fa004b640c39ef80345f9390238.webp)

3. If necessary, you can change the device name for easy recognition, and click "Save" to take effect.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/db4ef9cca80045c1a86ad0bca82d1bc3.webp)

4. The default folder templates can be removed. Go to the folder options and click "Remove".

![](https://file-us.ugreennas.com/admin/article/2025-09-04/13bccdbc8f3e4594af3f236a543abd92.webp)

## Add File Sync Shared Devices

1. To use Syncthing for file synchronization, we need to download the software for the corresponding system environment from the [syncthing](https://syncthing.net/) official website for backup setup. Here, we use the Windows system as an example to illustrate the use of the Syncthing software. For other systems, please refer to the Syncthing official documentation.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/c34e9e55c9bb4111af17360d10435180.webp)

2. Download the required Windows version software package. After the download is complete and the package is unzipped, run `syncthing.exe` to use it. The software will automatically open a browser, and the `127.0.0.1:8384` page will appear, showing the same interface as the one deployed on the NAS. The only difference is that the current device name displayed is the name of your Windows system device. Next, click the top right corner "Operations > Show ID" button.

3. Copy this ID, which is the Syncthing ID of this computer. You will add this ID to the NAS deployed Syncthing web page later.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/63b0a1d4a32d4ff999bf1cdada2b4f86.webp)

4. Open the NAS container web page, click "Add Remote Device" on the page, paste the copied Windows Syncthing ID, and click "Save" to take effect.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/101bb933e5a241e6ae961e515bad6e7d.webp)

5. Go back to the Syncthing web page running on the Windows system, and you will see a new device addition request. Click "Add Device", and then click "Save" in the addition window to take effect. After adding devices on both sides, they can connect.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/8a8ab5dd422c46ac91ec711587135099.webp)

## Use Syncthing for File Sync

1. After adding the devices, you can set up the folders you need for backup according to your needs and start synchronizing the files in the folders. For example, I added the D drive's `work` folder for synchronization testing. You only need to create this `work` folder on both the NAS and the Windows system's Syncthing, and share it with each other for data synchronization.

2. Open the Windows Syncthing web page and click "Add Folder".

![](https://file-us.ugreennas.com/admin/article/2025-09-04/21b995d53ebb45eabb2d44778aecfc1b.webp)

3. For example, I added the `work`folder. The folder path should be the actual path of the folder you need to synchronize, such as `D:work` here.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/6d6754e5e9564c2b98e25dbafe207c46.webp)

4. After adding the folder, it is displayed as "Not Shared". We also need to enable sharing for this folder, click on this folder, then click "Options > Share", check the device you want to share, and click "Save" to take effect.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/f8ea6f91cfc24baf850c1da3c92535c3.webp)

5. Return to the NAS Syncthing web page, and the folder to be synchronized will appear. Click "Add".

![](https://file-us.ugreennas.com/admin/article/2025-09-04/2567ae9699174b68ad35752d8533d595.webp)

6. Note that the "Folder Path" should be filled with the "File path for synchronized data" set when creating the container. After adding, click "Save".

![](https://file-us.ugreennas.com/admin/article/2025-09-04/553e212596504c9da8e840c5b76502a1.webp)

7. Then you can start syncing files happily.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/f268a5ce595848a292a78a7063d6cee5.webp)

## FAQ：

Q: When synchronizing, I encountered an error: "Error on folder 'story' (fej6a-snqqz): folder marker missing (this indicates potential data loss, search docs/forum to get information about how to proceed)". How to solve it?

A: If you encounter this error, you need to create a `.stfolder`folder in the folder where the data is being synchronized, and then scan again to sync.
