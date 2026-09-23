# Set Up a Plex Media Server with Docker

> **Article ID**: `360`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Set Up a Plex Media Server with Docker`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/360  

---

Plex is a media server application for organizing and managing local media files, such as movies, TV shows, music, and photos. With Plex, media stored on the NAS can be organized into libraries and streamed to phones, computers, TVs, and other devices.

## Download the Image

1. Open "**Docker**", then go to "**Image**">"**Image Database**".

2. Enter linuxserver/plex in the search box. Once the target image appears, double-click it to start the download.

![](https://file-us.ugreennas.com/admin/article/2026-06-23/7b4058146dc347088f97ea08866e1169.webp)

3. Keep the image version set to the default "**latest**", then click "**Confirm**" to pull the image.

After the download is complete, the Plex image will appear under "**Local**".

## Prepare the Storage Directories

Before creating the container in Docker, create the storage directories it will use.

To avoid permission issues when the container is running, store Docker-related directories under the docker folder in **Shared Folder**. For example, create a folder named plex at:

```
/Shared Folder/docker/plex
```

To keep configuration files and cache files separate, create additional subfolders under this directory as needed.

## Create a Plex Container

After the image has been downloaded, create the container as follows:

1. Open "**Docker**", then go to "**Image**">"**Local**".

2. In the downloaded image list, locate linuxserver/plex.

3. Click "**+**" to the right of the image, or double-click the image, to open the container creation wizard. Then configure the container as prompted.

![](https://file-us.ugreennas.com/admin/article/2026-06-23/ed2e4dc7d2bf4fe9957902b0f67baf29.webp)

## Configure Basic Information

Under "**Basic information**" in the container creation wizard, configure the container name and runtime options.

**Container name:** Enter a custom name to make the container easier to identify and manage.

**Auto restart:** Enabling this option is recommended. If the NAS restarts or the container exits unexpectedly, the system will attempt to restart the Plex container automatically.

**GPU performance:** Enable this option if the device supports GPU acceleration. Plex may then use the device hardware for media processing in supported scenarios. Actual performance depends on the device hardware, Plex settings, and media format.

![](https://file-us.ugreennas.com/admin/article/2026-06-23/fc04f913f95f4dc2b4f8f98034c49c70.webp)

### Configure Environment Variables

Add the following environment variables to help ensure that the container runs correctly:

● **PUID:** The user ID used by processes inside the container. Click "**Add**", enter PUID as the variable name, and set its value to the ID of the user creating the container. The value can also be changed as needed.

● **PGID:** The group ID used by processes inside the container. Click "**Add**", enter PGID as the variable name, and set its value to the group ID of the current user.

● **TZ:** The container time zone. Click "**Add**", enter TZ as the variable name, and specify the appropriate time zone so that the container time matches the local time. For example, use Asia/Shanghai, America/New\_York, or Europe/London.

● **PLEX\_CLAIM:** The Plex claim token used to link the server to a Plex account. Obtain the value from<https://www.plex.tv/claim/>.

|  |  |  |
| --- | --- | --- |
| **Environment Variable** | **Default Value** | **Description** |
| PUID | Container creator's user ID | User ID used by processes in the container |
| PGID | User group ID | Group ID used by processes in the container |
| TZ | Asia/Shanghai | Container time zone. The default is Asia/Shanghai; change it to match the local region if needed. |
| PLEX\_CLAIM | Obtain from Plex | Claim token obtained from <https://www.plex.tv/claim/> |

### Configure Storage

In the storage configuration step, select the data paths to mount to the container so that important data is stored persistently.

● For /config, click the automatic mapping button and select the folder used to store Plex configuration files. Set the access mode to **Read/Write**. It is recommended to use a path under /Shared Folder/docker on the NAS to avoid permission issues while the container is running.

● Click "**Add**", select the folder used for transcoding files, set the mount path to /transcode, and set the access mode to **Read/Write**.

● Click "**Add**", select the folder containing the media files, set the mount path to /video, and set the access mode to **Read/Write**.

**Example Storage Configuration**：

|  |  |  |
| --- | --- | --- |
| **File/Folder Path** | **Mount Path in Container** | **Description** |
| /共享文件夹/docker/plex/config | /config | Stores the container configuration files |
| /共享文件夹/docker/plex/transcode | /transcode | Stores temporary transcoding files |
| /共享文件夹/video | /video | Stores media files |

![](https://file-us.ugreennas.com/admin/article/2026-06-23/2c7489a6597244dc927b298d6a5c3c23.webp)

### Configure the Network

Under "**Network configuration**", set the container network mode and port mappings. `host` mode is recommended.

![](https://file-us.ugreennas.com/admin/article/2026-06-23/696802e03c50487caf346e512016201b.webp)

After confirming that all settings are correct, click "**Confirm**" to create the container.

## Access the Container Web UI

1. After the container starts, open a browser and access the container Web UI at: http://<NAS\_IP>:32400. Use your NAS IP address in place of <NAS\_IP>. Once the Plex page opens, complete the initial setup. The page may take some time to load before the media library configuration page appears.

![](https://file-us.ugreennas.com/admin/article/2026-06-23/e4119568ee1f43c3a8ccb23b5c962c22.webp)

2. Follow the on-screen instructions to configure the server, clicking "**Next**" to proceed through each step.

![](https://file-us.ugreennas.com/admin/article/2026-06-23/e2a9b3390a8c47b2a61d0f8ffc34fee9.webp)

![](https://file-us.ugreennas.com/admin/article/2026-06-23/210d50d7cedf46ce8edc7a05e58a34cf.webp)

![](https://file-us.ugreennas.com/admin/article/2026-06-23/536bdbb4bc3d44979745db26c36dc05f.webp)

3. Click the **Settings** icon in the upper-right corner to configure the media library.

![](https://file-us.ugreennas.com/admin/article/2026-06-23/ba0c2e0b1a1f4b1384dbf75f21ce3ab8.webp)

4. Create the media library and complete the metadata matching process.

![](https://file-us.ugreennas.com/admin/article/2026-06-23/6d0f875dddc14813b63329b60a1b08b7.webp)

## FAQs

### Q1: What should I do if the image download fails?

**Docker registry mirror:** Configure a registry mirror to improve download speeds, especially when using a network connection in mainland China. For setup instructions, refer to [Guide to Configure Docker Image Acceleration and Repository Pull](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjo4OTMsImFydGljbGVJbmZvSWQiOjI5NywiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIiLCJwYXRoQ29kZSI6IiJ9) **.**

**Proxy settings:** In some cases, an HTTP/HTTPS proxy may be required to download the image. For details, refer to [Configuring Docker to Download Images via Proxy on UGREEN](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMDE2LCJhcnRpY2xlSW5mb0lkIjozMzUsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==) .

### Q2: How do I find the actual path of a NAS folder and mount it to a Docker container?

When using Docker, a folder on the NAS may need to be mounted to a container so that the container can access the data stored on the NAS. For instructions, refer to [Get the real path of the NAS folder and mount it to the Docker container](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTkzMCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo2MTEsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==) .

## Notes

● The image used in this guide is developed and maintained by a third party. This guide is provided for reference only. UGREEN is not liable for issues caused by improper operation, software vulnerabilities, or image updates, including file corruption or data breaches. Use images from trusted sources to help protect the system and data.

● Container file paths can be configured as needed. For web access, make sure the container port is mapped to the correct local port. Local ports assigned to different containers must not conflict.

● Container web links are available only when the container uses "bridge" mode.

● This guide covers image setup only. For usage instructions and additional features, refer to relevant resources online. For configuration changes and bug fixes, follow the official documentation and release notes for the image.

● It is recommended to store the Docker configuration directory on an SSD to avoid performance limitations associated with mechanical hard drives.
