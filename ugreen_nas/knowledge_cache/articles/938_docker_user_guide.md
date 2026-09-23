# Docker User Guide

> **Article ID**: `938`  
> **Category**: `Application Guide > Docker > Docker User Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/938  

---

## Applicability

**Applicable Clients:** UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version:** UGOS Pro firmware 1.19.1.0126 or later

Installing the Docker app is not recommended on ARM-based devices with 4 GB of RAM or less, as it may affect system performance and stability.

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

The Docker app allows you to create, run, and manage container services on UGREEN NAS. This guide uses a qBittorrent container as an example to introduce the basic workflow for first-time Docker users, including configuring a Registry Mirror, pulling an Image, creating a container, configuring port mappings and storage paths, and accessing the container service.

## Getting Started Steps for New Users

If you are using the Docker app for the first time, we recommend following these steps:

1. Install and open the **Docker** app.

2. Configure "**Registry-Mirrors**".

3. Pull container Image.

4. Create container and configure port mappings and storage paths.

5. Start the container.

6. Access the container Web page through browser.

7. View logs, stop, restart, or delete the container as needed.

## Before You Begin

Before deploying qBittorrent with Docker, make sure that:

● The **Docker** app is installed on the NAS.

● A valid Registry Mirror URL is available.

● You have created folders in "**Files**" for storing qBittorrent configuration files and downloaded files.

● You have confirmed the access port required for the qBittorrent Web page.

**Note:** qBittorrent is a third-party container service. For Image parameters, default accounts, default passwords, port rules, and usage restrictions, refer to the documentation provided by the Image author.

## Installation and Access

1. Open "**App Center**" and find the "**Docker**" app.

2. Click "**Install**" and follow the setup wizard to complete the installation.

3. After installation, click the "**Docker**" icon to open the app.

## Configure Registry-Mirrors

In some network environments, pulling Docker Images directly may fail or be slow. After configuring a Registry Mirror, Docker can use the specified address to optimize the Image pulling process.

1. Open the "**Docker**" app and go to the "**Image**" page.

2. Click "**Settings**" at the top.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/bc2636bb9a1948fcba7741ddfb4ed3dc.webp)

3. On the "**Image Repository**" tab, click "**Registry Settings**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/c888f7de8ca242f391fec9cfbc704c50.webp)

4. Enter an available Registry Mirror URL in the input box.

You can also click "**+**" to select a Registry Mirror recommended by the system.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/95e12ffb0c8349659dc612a056267b20.webp)

5. Click "**Confirm**". The system will restart the Docker engine.

6. Return to the Image page and pull the Image again.

**Note:** Registry Mirror URLs are provided by the corresponding service providers. Availability and access restrictions may vary by service. Refer to the service provider's documentation for details.

## Create Storage Folders

Before creating a container, we recommend preparing folders on the NAS for qBittorrent. You can create folders for the following purposes:

|  |  |
| --- | --- |
| Purpose | Description |
| Configuration folder | Used to store qBittorrent configuration files. |
| Download folder | Used to store downloaded content. |

## Image Pulling

After configuring Registry Mirror, you can pull the qBittorrent Image.

1. Open the "**Docker**" app and go to the "**Image**" page.

2. Enter the qBittorrent Image name in the search box under Image Repository.

3. Select the Image and click "**Download**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/1d3143dfca8b45488e324f2879a8609c.webp)

4. Select the version number and click "**Confirm**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/e58f61a45b9a428d85e9e856a0618360.webp)

After the Image has been pulled, you can view the downloaded qBittorrent Image under "**Local**".

## Create Container

After the Image has been pulled, you can create a container from it.

1. Open the **Docker** app and go to "**Image**">"**Local**".

2. Find the downloaded qBittorrent Image.

3. Click "**+**" on the right to create a container.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/29496eb9afd14363803d2d3900037e77.webp)

### Configure Basic Container Information

When creating a container, configure the basic information.

1. Set the container name.

2. Enable "**Auto restart**".

When Auto restart is enabled, the container automatically starts after the NAS restarts or the Docker service recovers.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/c22ea48066ed49e1a241e2f40b109509.webp)

### Configure Storage

Configure NAS folders for storing qBittorrent configuration files and downloaded files.

|  |  |  |
| --- | --- | --- |
| Purpose | NAS Folder | Path in Container |
| Configuration files | Select the NAS folder used to store configuration files | `/config` |
| Downloaded files | Select the NAS folder used to store downloaded content | `/downloads` |

Configuration notes:

● The container path `/config` must be mapped to the NAS folder used to store configuration files.

● The container path `/downloads` must be mapped to the NAS folder used to store downloaded content.

After configuration, the container can save configuration files and downloaded data through the mapped folders.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/9ef002e78d534c149b491ec518b4d7e6.webp)

### Configure Environment Variables

Enter the required environment variables according to the qBittorrent Image documentation.

Different Images may require different configurations. Refer to the documentation provided by the Image provider.

### Configure Port Mapping

Port mapping maps service ports inside the container to NAS ports, allowing you to access the qBittorrent Web management page through a browser.

When configuring the ports, enter the values according to the qBittorrent Image documentation.

Example:

|  |  |  |
| --- | --- | --- |
| Purpose | Container Port | NAS Port |
| Web management page | Refer to the Image documentation, for example `8080` | Custom port used to access the qBittorrent Web page |

Note: The NAS port cannot be the same as a port already used by another service. If a port conflict occurs, select an unused port.

### Create and Start the Container

After completing the configuration above, click "**Confirm**" and wait for Docker to create and start the container.

After the container starts successfully, you can view its running status on the Docker "**Container**" page.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/f98f5d0ffb6e4346ad88554e3dedbdf4.webp)

## Access the Container Web Page

After the container starts, you can access the qBittorrent Web page using either of the following methods.

### Method 1: Quick Access

1. Open the "**Docker**" app and go to the "**Container**" page.

2. Find the qBittorrent container and click "**Quick Access**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/a53c70cef49142c880f7beca97568bd1.webp)

3. Select the configured Web access port.

### Method 2: Access from a Browser

Enter the following address in the browser address bar: `http://NAS-IP:NAS-port`

Example: `http://192.168.1.100:42499`

![](https://file-us.ugreennas.com/admin/article/2026-09-15/a8b1792cafa0441e91617d109ed9dfd5.webp)

`NAS-IP` is the LAN IP address of the NAS, and `NAS-port` is the Web management page port configured when the container was created.

## Manage Containers

After creating a container, you can manage it on the "**Container**" page. The following operations are supported:

● **Start**: Start a stopped container.

● **Stop**: Stop a running container.

● **Restart**: Restart the container.

● **Log**: View container runtime logs.

● **Edit**: Modify the container configuration.

● **Delete**: Delete a container that is no longer needed.

## FAQs

### Q: What Should I Do If an Image Fails to Pull?

Check the following:

● Whether the NAS network connection is working properly.

● Whether valid Registry Mirror has been configured.

● Whether the Image name and tag are correct.

● Whether the Image Repository is accessible.

### Q: What Should I Do If the qBittorrent Container Fails to Start?

Check the following:

● Whether the Image has been completely pulled.

● Whether the port is already in use by another service.

● Whether the storage path exists.

● Whether the folder has read and write permissions.

● Whether the environment variables have been configured according to the Image documentation.

● Whether the container log contains any error messages.

### Q: What Should I Do If I Cannot Access the qBittorrent Web Page?

Check the following:

● Whether the container is running.

● Whether the NAS IP address in the access URL is correct.

● Whether the access port matches the NAS port configured in the port mapping.

● Whether the NAS firewall, router, or browser is restricting access.

### Q: Will Deleting a Container Delete Downloaded Files?

If the downloaded files are stored in a mounted NAS folder, deleting the container will not delete the files in that folder.

If the downloaded files are stored only inside the container, deleting the container will result in data loss.

## Notes

● The NAS port cannot be the same as a port already used by another service. Otherwise, the container may fail to start or become inaccessible.

● When using third-party Images, refer to the documentation provided by the Image author.

## Related Reading

● [Docker App Pages and Features Overview](https://support.ugnas.com/knowledgecenter/detail/article/en-US/236)

● [Docker Project Compose User Guide](https://support.ugnas.com/knowledgecenter/detail/article/en-US/411)

● [How to Configure Registry Images, Image Sources, and Image Proxy in Docker?](https://support.ugnas.com/knowledgecenter/detail/article/en-US/297)
