# Set Up a Transmission Downloader Using Docker

> **Article ID**: `364`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Set Up a Transmission Downloader Using Docker`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/364  

---

## App Overview

Transmission is an open-source, lightweight BT/PT client known for its low resource consumption and high performance. It provides powerful download and management capabilities that can meet the download needs of both home and office environments. Deploying Transmission via Docker simplifies installation and management, delivering a high-quality download experience.

### Deploying the Container Using Docker Compose

On the UGOS Pro system, it is recommended to use Project Docker Compose for quick container deployment. This approach is suitable for scenarios requiring the management of multiple containers simultaneously, simplifying container deployment and management.  
Click to learn more: [Project (Docker Compose)](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9) .

### Access the Docker Project Interface

In the UGOS Pro system, open the Docker application, click [Project] > [Create] to launch the project creation wizard.

### Configure the Docker Compose File

In the project creation wizard, upload the following Docker Compose configuration file for Transmission:

```
services:
  transmission:
    container_name: transmission
    image: linuxserver/transmission:latest # Image name
    restart: always # Restart policy
    volumes:
      - /volume1/media:/downloads # Path for downloaded files
      - ./config:/config # Path for configuration files
      - ./transmission-web-control:/trweb # Custom WEBUI folder path
    environment:
      - PUID=0 # Container user ID, root privileges
      - PGID=0 # Container group ID, root privileges
      - UMASK=0 # File permission mask
      - TZ=Asia/Shanghai # Container timezone
      - TRANSMISSION_WEB_HOME=/config/web # Custom WEBUI folder path
      - USER=ugreen # Login username
      - PASS=ugreen # Login password
      - RPCPORT=9091 # WEB service access port
    network_mode: host # Use host network mode, allowing the NAS IPv6 address.
```

### Parameter Descriptions

● **image**: Specifies the Docker image; `latest` is the newest version.

● **restart**: Defines the container restart policy. `always` automatically restarts the container if it stops or crashes.

● **volumes**: Maps NAS local folders to paths inside the container.

`/volume1/media`: Storage path for downloaded files. Replace `/volume1/media` with the actual folder path on your NAS (e.g., `/volume5/downloads`).

`./config`: Stores transmission configuration files.

`./transmission-web-control`: Custom WEBUI folder path for loading new skins.

**Note:**

● `./` refers to the directory where the current Docker Compose file is located.

● The path before the colon is the NAS storage path; the path after the colon is the mapped path used inside the container.

**Related reading:**  
[How to Correctly Represent Volumes Mount Paths in the Docker Compose Configuration File?](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTQ0NywidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0ODcsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)

**environment**:

`PUID/PGID/UMASK`: Defines container user and group permissions.

`USER/PASS`: Custom login credentials.

`TRANSMISSION_WEB_HOME`: Path for loading the custom WEBUI folder. To load a new Transmission 4.0 skin, unzip the downloaded ZIP package, rename the extracted folder to web, and upload it to the /config folder of Transmission.

`TZ`: Sets the container timezone (e.g., Asia/Shanghai); adjust according to your region (e.g., America/New\_York or Europe/London).

`RPCPORT`: WEB service access port.

**network\_mode**: Sets the container to host network mode, allowing the use of the NAS IPv6 address.

### Deploy the Project

After uploading the configuration file, click [Deploy]. The system will automatically pull the image and start the container.

Once deployment is complete, access the transmission interface via a browser:

```
http://<NAS_IP>:9091
```

Replace `<NAS_IP>` with the actual IP address of your NAS, e.g., `http://192.168.22.153:9091`.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/384b85bb3ce0491ab3eb199da4f82173.webp)

## User Guide

Once the container is running, you can access Transmission’s Web interface through a browser for configuration and management.

#### First Login & Skin Loading

1. On first access, you may see a "404: Not Found" error message.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/5db0be3b4b9c42eab59d363c2e3ffdb1.webp)

2. Download the [Transmission 4.0 skin](https://github.com/jayzcoder/TrguiNG/releases) ZIP file, unzip it, and rename the folder to `web`.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/22d1c268e4104577956aecbc9c8128c8.webp)

3. Upload the `web` folder to the `/config` directory.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/4aacc292c0bd45d3be936d93eb33743d.webp)

4. Refresh the browser page, and the Transmission interface should display correctly.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/7661f0e5f3034bd1b3219dfefdde45df.webp)

### Set the Download Path

1. Click the [Settings] button in the upper right corner.

2. Under [Download Settings]:

● Remove `/complete` from the "Save the catalog by default".

● Uncheck [Enable temporary directories] and [Add the ".part" suffix to the name of the unfinished file].

![](https://file-us.ugreennas.com/admin/article/2025-09-09/cb0dcd26929b427eb033830b49e42aca.webp)

#### Adjust Connection Settings

● **Global Maximum Connections**: Recommended to increase from the default 200 to 500-1000 for seeding scenarios.

● **Maximum Connections per Torrent**: Recommended 10-20 to ensure full speed per torrent.

## Common Issues

### WEBUI Modifications

● When using a custom WEBUI, ensure the uploaded folder is named `web` and placed in the `/config` directory.

● After changing skins, a container restart may be required for changes to take effect.

### Permission Issues

● If the container cannot access the mounted path, check whether the path permissions are set correctly.

● Ensure the read/write permissions of the mounted paths match the configured `PUID` and `PGID`.

## Notes

Please note that the image used in this tutorial is developed and maintained by third parties. This tutorial is for reference only. UGREEN assumes no liability for risks arising from user errors, third-party software vulnerabilities, or image updates, including but not limited to:

● Third-party images may cause accidental modification or deletion of files in the UGOS Pro system.

● Using insecure images may result in data being uploaded to third-party servers, posing privacy and data leakage risks.

● To ensure system stability and data security, carefully select images from trusted sources.

**Additional Notes**

1. The container file/folder paths are for reference only; you may create your own according to personal preference.

2. The container’s web-access port and local port must match. If there is a conflict, use an unused port. Containers cannot share the same local port; port conflicts will prevent containers from starting.

3. The container’s web link is only accessible in bridge mode.

4. The image is provided for setup purposes; for specific usage and advanced features, please search online resources.

5. The image is developed by a third party; monitor official updates for configuration changes and bug fixes.

6. It is recommended to store the Docker configuration directory on an SSD to avoid performance issues caused by mechanical drives.
