# Docker Compose Project User Guide

> **Article ID**: `411`  
> **Category**: `Application Guide > Docker > Docker Compose Project User Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/411  

---

## Applicability

**Applicable Clients:** UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version:** UGOS Pro firmware 1.19.1.0126 or later

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

Docker Compose uses a configuration file to centrally define container images, ports, storage paths, environment variables, and restart policies. Compared with manually creating containers item by item, Compose is better suited for saving and reusing deployment configurations. This guide uses qBittorrent as an example to introduce the basic use of Compose.

## Before You Begin

Before creating a qBittorrent project with Compose, make sure that:

● A valid **Registry Mirror** URL has been configured.

**Note:** qBittorrent is a third-party container service. For image parameters, default accounts, default passwords, port rules, and usage restrictions, refer to the documentation provided by the image author.

## What Is Docker Compose?

Docker Compose is a way to create and manage container services through a configuration file. A Compose configuration specifies:

● Which image to use

● The container name

● Whether the container automatically restarts with the system or after an unexpected exit

● Which path in the container a NAS folder is mounted to

● Which environment variables need to be configured

● Which ports need to be opened

## Create a qBittorrent Project

1. Open the "**Docker**" app, go to "**Project**", and click "**Create**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/01eaf2123a644502b78d0d9af3a00d5d.webp)

2. Enter a project name, such as `qbittorrent1`.

The system automatically generates a path for saving the configuration file and creates a folder with the same name under the docker directory in the Shared Folder, for example: `Shared Folder/docker/qbittorrent1`

3. Enter the following example configuration under Compose configuration.

Replace `/path/to/qbittorrent/config` and `/path/to/downloads` in the example with the actual NAS folder paths.

```
services:
  qbittorrent:
    image: lscr.io/linuxserver/qbittorrent:latest
    container_name: qbittorrent1
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Asia/Shanghai
      - WEBUI_PORT=8080
      - TORRENTING_PORT=6881
    volumes:
      - /path/to/qbittorrent/config:/config
      - /path/to/downloads:/downloads
    ports:
      - 38989:8080
      - 6881:6881
      - 6881:6881/udp
    restart: always
```

4. Click "**Deploy**" and wait for the system to pull the image and create the container.

After the project starts, check whether the project status is normal. Then go to the "**Container**" page and make sure the qBittorrent container is Running.

### Path Description

|  |  |
| --- | --- |
| Example Path | Replace With |
| `/path/to/qbittorrent/config` | The NAS folder path used to store the qBittorrent configuration. |
| `/path/to/downloads` | The NAS folder path used to store downloaded content. |

### Compose Parameters

|  |  |  |
| --- | --- | --- |
| Parameter | Example Value | Description |
| `image` | `lscr.io/linuxserver/qbittorrent:latest` | qBittorrent image address and tag |
| `container_name` | `qbittorrent` | Container name |
| `PUID` | `1000` | User ID |
| `PGID` | `1000` | User group ID |
| `TZ` | `Asia/Shanghai` | Time zone |
| `WEBUI_PORT` | `8080` | Web management page port |
| `TORRENTING_PORT` | `6881` | Download connection port |
| `/config` | `/config` | Configuration file path inside the container |
| `/downloads` | `/downloads` | Download file path inside the container |
| `ports` | `38989:8080` | Maps a NAS port to a container port |
| `restart` | `always` | Sets the container restart policy |

**Note:** If you need to change the Web page port, update both the Web port mapping under `ports` and `WEBUI_PORT`. If you need to change the download connection port, update the TCP and UDP port mappings as well as `TORRENTING_PORT`.

## Access the qBittorrent Web Page

After the project starts, you can access the qBittorrent Web page in a browser.

Access format: `http://NAS-IP:38989`

Example: `http://192.168.1.100:38989`

`NAS-IP` is the LAN IP address of the NAS, and `38989` is the Web access port mapped to the NAS in this example.

**Note:** The temporary password for the qBittorrent Web page can be found in the container log. After your first login, we recommend changing the username and password.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/ea444685924b47e29d85337620c03fef.webp)

## View Container Logs

If qBittorrent fails to start or you cannot log in to the Web page, check the container log.

1. Open the "**Docker**" app and go to the "**Container**" page.

2. Find the `qbittorrent1` container and click it to open the details page.

3. Click "**Logs**".

4. Check the configuration based on the log messages.

## Manage Compose Projects

After creating a project, you can manage it on the "**Project**" page. The following operations are supported:

● **Start Project:** Starts the container services in the project

● **Stop Project:** Stops the container services in the project

● **Restart Project:** Restarts the container services in the project

● **Edit Configuration:** Modifies the Compose configuration

● **View Logs:** Views project or container runtime logs

● **Delete Project:** Deletes a Compose project that is no longer needed

## FAQs

### Q: What Should I Do If a Compose Project Fails to Start?

Check the following:

● Whether the Registry Mirror is available

● Whether the image name and tag are correct

● Whether the NAS folder paths exist

● Whether the folders have read/write permissions

● Whether the ports are already in use by other services

● Whether the indentation in the Compose configuration is correct

### Q: What Should I Do If the qBittorrent Web Page Cannot Be Accessed?

Check the following:

● Whether the project has started

● Whether the qBittorrent container is Running

● Whether the NAS IP address in the access URL is correct

● Whether NAS port `38989` is correctly mapped to container port `8080`

● Whether the NAS firewall, router, or browser is restricting access

### Q: What Should I Do If the Web Page Cannot Be Accessed After Changing the Port?

Make sure the following values are both updated in the Compose configuration:

● `WEBUI_PORT`

● The corresponding Web page port mapping under `ports`

For example, if you change the Web page port to `8123`, update the configuration as follows:

```
environment:
  - WEBUI_PORT=8123
ports:
  - 8123:8123
```

### Q: Will Deleting a Compose Project Delete Downloaded Files?

If the downloaded files are stored in a mounted NAS folder, deleting the project will not delete the files in that folder.

If the downloaded files are stored only inside the container, deleting the project will result in data loss.

## Notes

● Before modifying the Compose configuration, make sure you understand the ports, paths, and environment variables in the configuration file.

● When using third-party images, refer to the documentation provided by the image author.

● When using qBittorrent to download content, comply with local laws and regulations and make sure the downloaded content comes from legal sources.

## Related Reading

● [Docker App Pages and Features Overview](https://support.ugnas.com/knowledgecenter/detail/article/en-US/236)

● [Docker User Guide](https://support.ugnas.com/knowledgecenter/detail/article/en-US/938)

● [How to Configure Registry Images, Image Sources, and Image Proxy in Docker?](https://support.ugnas.com/knowledgecenter/detail/article/en-US/297)
