# Deploying a Qbittorrent Downloader on UGREEN NAS

> **Article ID**: `348`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Deploying a Qbittorrent Downloader on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/348  

---

## App Introduction

**QBittorrent** is an open-source, lightweight, feature-rich, and easy-to-configure BT/PT download tool. It supports the BitTorrent protocol as well as private trackers, and is widely favored for its powerful features and flexible settings. By using a Docker image, you can quickly deploy qBittorrent on the UGREEN NAS running the UGOS Pro system, enabling efficient torrent downloading and management.

## Deploying the QBittorrent Image Using Docker Compose

To quickly deploy qBittorrent on the UGOS Pro system, it is recommended to use [**Project (Docker Compose)**](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9) for containerized deployment. This method is especially suitable for scenarios where you need to quickly create and manage multiple containers. The following steps will guide you through deploying qBittorrent using Docker Compose.

1. Open the Docker app and click [Project] > [Create] to launch the project creation wizard.

2. In the project creation wizard, upload the following Docker Compose configuration file for qBittorrent. These configurations are for reference only; you can adjust them according to your own needs.

```
services:
    qbittorrent:
        image: linuxserver/qbittorrent
        container_name: qbittorrent
        restart: always
        ports:
            - '8091:8091'   # Web UI access port
            - '16881:16881'   # TCP port
            - '16881:16881/udp'   # UDP port
        volumes:
            - ./config:/config  # Mount configuration directory
            - /volume1/downloads:/downloads  # Mount download directory
        environment:
            - 'PUID=0'  # Set user ID
            - 'PGID=0'  # Set group ID
            - 'TZ=Asia/Shanghai'  # Set time zone
            - 'WEBUI_PORT=8091'  # Web UI port
            - 'QBITTORRENT_WEBUI_PORT=8091'  # Ensure consistency of Web UI port
```

3. After filling out the configuration file, click "Deploy". The system will automatically pull the image and start the container.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250908/3ae8e7f1-eb1f-4373-8ab0-0301f233a119.png)

4. After deployment is complete, access the container through a browser by entering `http://NAS_IP:8091` in the address bar. For example, if the NAS IP is `172.17.70.86`, enter `http://172.17.70.86:8091` in the browser to access it.

You can find the NAS IP address in the Control Panel under [**Network]** by clicking [**Network Connection]**.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/ed959517fd31457d95a4b740826b9a39.webp)

### Compose Configuration Parameter Explanation

**image:** Image Version

● Specifies the Docker image. `latest` refers to the newest version.

**restart:** Restart Policy

● Set the restart policy to `always` so that the container automatically restarts if it crashes or stops, ensuring continuous service.

**ports:** Port Mapping

● Map the container's port 8091 to the NAS port 8091 to access the web interface via `http://NAS_IP:port`.

● Map the container's port 16881 (both TCP and UDP) to the NAS port 16881 for BitTorrent P2P data transfer, supporting both TCP and UDP protocols.

**volumes:** Map NAS Local Folders to Container Mount Paths

● **./config**: Stores qBittorrent configuration files.

● **/volume1/downloads**: Directory for downloaded files. Replace the left-side path `/volume1/downloads` with the actual path on your NAS where media files are stored.

**environment:** Set Environment Variables to Configure Services Inside the Container

● **PUID/PGID**: Define the permissions for the container's running user and group. A value of `0` means using root user privileges.

● **TZ=Asia/Shanghai**: Set the container's timezone. Here it is set to Shanghai, China (Asia/Shanghai) to ensure the container time matches the local time. You can adjust it according to your timezone, e.g., America/New\_York or Europe/London.

● **WEBUI\_PORT=8091**: Web interface access port of the container.

● **TORRENTING\_PORT=16881**: Download listening port of the container.

**Additional Notes:**

● `./` indicates that the path is within the project's selected storage directory.

● `./:/`means mounting the NAS local `./` directory to the container's `/` directory.

● The path before the colon is the NAS folder storage path, and the path after the colon is the corresponding mount path inside the container.

## User Guide

To access the QBittorrent Web UI, please follow these steps:

1. Open your browser and visit the deployment address to enter the login page.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/54e394c5fef143e0b0fea40a53916124.webp)

2. The default username and password can be found in the logs. It is recommended to change the password immediately after the first login to ensure security.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/74715c9ced7a43b097761e36e3fea61a.webp)

### Set Language

Go to [Tools] > [Options] > [Behavior], change Language to English, then click "Save" at the bottom to apply the settings.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/bce1aa2041e64b92a078af24a4b24972.webp)

### Change the Default Listening Port

Some ISPs may throttle common BT/PT ports such as `6881`, and most PT sites will reject requests using these ports. To change the port, go to [Tools] > [Options] > [Connection], set the listening port to another random port, then click "Save" to apply the changes.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/1163c4dbc73548e29b8ec72ef2cfce3d.webp)

### Enable Appending Extension to Incomplete Files

![](https://file-us.ugreennas.com/admin/article/2025-09-08/80ae1dcd7f7d49c2805d155e4ac60cb7.webp)

### Set Username and Password, Disable Host Header Validation

![](https://file-us.ugreennas.com/admin/article/2025-09-08/f3c15c1f64064a67be7554aeeff2f94c.webp)

## FAQ

### Q: Obtain the actual path of a NAS folder and mount it to a Docker container

When using Docker, you may need to mount a folder from the NAS to a Docker container so that the container can access the data stored on the NAS. You can refer to [Get the real path of the NAS folder and mount it to the Docker container](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTkzMCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo2MTEsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==) to help you complete this task.

## Notes

● The images mentioned in this tutorial are developed and maintained by third parties. This tutorial is for reference only. UGREEN does not assume any liability for risks caused by improper operations, software vulnerabilities, or image updates, such as file corruption or data leakage. Please use trusted images to ensure system and data security.

● Container file paths can be customized. When accessing via a web browser, the container port and the local port must be the same, and local ports of different containers must not conflict.

● Container web links are only accessible in bridge mode.

● The images are provided solely for setup guidance. For specific usage and features, please refer to online resources. For configuration changes and bug fixes, follow the official updates.

● It is recommended to store the Docker configuration directory on an SSD to avoid performance degradation caused by mechanical hard drives.
