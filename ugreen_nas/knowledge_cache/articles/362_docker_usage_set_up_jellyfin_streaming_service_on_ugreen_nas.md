# [Docker Usage] Set Up Jellyfin Streaming Service on UGREEN NAS

> **Article ID**: `362`  
> **Category**: `Application Guide > Docker > Docker Gameplay > [Docker Usage] Set Up Jellyfin Streaming Service on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/362  

---

**Jellyfin,** a fully open-source media server, offers functionalities similar to those of Plex and jellyfin. It enables users to organize and stream locally stored media files, such as movies, music, photos, and more, to various devices. Installing the Jellyfin image via Docker simplifies the deployment and management process, providing greater flexibility and convenience.

## Deploy Jellyfin Image Using Docker Compose

For rapid container deployment on the UGOS Pro system, it is recommended to use Docker Compose, especially suitable for scenarios requiring the quick creation and management of multiple containers. The following steps will guide you through deploying a container using Docker Compose. [How to Use Docker Compose on UGREEN UGOS Pro?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### Enter the Docker Project Interface

On the UGOS Pro system, open the Docker application, click on [Project] > [Create] to initiate the project creation wizard.

### Configure the Docker Compose File

When creating a project, you need to provide a Docker Compose configuration file. Below is an example configuration file for Jellyfin:

```
services:
  jellyfin:
    image: jellyfin/jellyfin:latest
    container_name: jellyfin
    restart: always
    devices:
      - /dev/dri:/dev/dri  # Integrated graphics
    environment:
      PUID: 0
      PGID: 0
    volumes:
      - ./config:/config
      - ./cache:/cache
      - /volume2/video:/video2 #Library location
    ports:
      - 9096:8096/TCP
    network_mode: "bridge"
```

### Parameters Explanation

**image:**

● `nyanmisaka/jellyfin:latest` specifies the latest version of the Jellyfin server image.

**container\_name:**

● Sets a specified name for the container `jellyfin` for easy management.

**restart:**

● `always` means that the container always restarts, automatically if it stops unexpectedly.

**devices:**

● `/dev/dri:/dev/dri`mounts the host's `/dev/dri` device into the container for hardware acceleration, such as video transcoding.

**environment:**

Sets environment variables to configure services within the container.

● `PUID: 0`：Sets the user ID inside the container, `0`means running with root privileges.

● `PGID: 0`：Sets the group ID inside the container, `0`means running with the root group.

**volumes:**

● **Feature:** Mount local folder paths to the container to ensure data persistence.

● `./config`：./ represents the directory where the current Docker Compose file is located. The `config` folder in this directory is mounted to the `/config` directory inside the container, which is used to store Jellyfin's configuration files. This ensures that configuration data is not lost even if the container is restarted or recreated.

● `./cache`：The `cache` folder in the current directory is mounted to the `/cache` directory inside the container, which is used to store Jellyfin's cache.

● `/volume2/video:/video2`：The `/volume2/video` folder on the NAS is mounted to the `/video2` directory inside the container, serving as the source directory for the library. Note that the path before the colon is the path on the NAS, and the path after the colon is the path inside the Docker, which is the path you need to enter during Jellyfin configuration. You can replace `/volume2/video` with other folder paths on the NAS according to your actual needs.

**ports:**

● `8096:8096/TCP`maps the container's 8096 port (TCP protocol) to the 9096 port on the UGREEN NAS. This is used for the Jellyfin web management interface for library management and playback operations.

**network\_mode:**

● `bridge`：Sets the container's network mode to bridge mode.

● **Feature:** Bridge mode allows the container to share the network with the host and be accessible via the host's IP. That is, the container provides services through the mapped ports and can communicate with other devices on the same network.

### Deploy the Project

After confirming that the configuration file is correct, click [Deploy Now], and the system will automatically pull the Jellyfin image according to the YAML file and start the container. After successful deployment, you can access the Jellyfin console by visiting `http://<NAS_IP>:8096` in your browser.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/6039f4ec22fc427788790d9079a091b1.webp)

## Access the Container WebUI

1. After the container is started, you can access the container's Web UI through a browser by visiting the URL `http://<NAS_IP>:9096`, replacing the NAS's IP with your NAS's IP address. After entering the Jellyfin page, proceed with the initial configuration. The Jellyfin page may take time to load before entering the library configuration.

2. Choose`English`as the preferred display language and click "Next".

![](https://file-us.ugreennas.com/admin/article/2025-09-05/97f932ad3cc54473981f37379059b1d6.webp)

3. Create a **username and password**, customize the username and password according to your preference, and click "Next".

![](https://file-us.ugreennas.com/admin/article/2025-09-05/c04d64e968924cda9cb8ae3d550c2b1d.webp)

4. Do not set up the library yet, click "Next".

![](https://file-us.ugreennas.com/admin/article/2025-09-05/062c151a491b45d281b78f3888328f5c.webp)

5. The preferred metadata language is set to default, click "Next".

![](https://file-us.ugreennas.com/admin/article/2025-09-05/c7508445194644698b9d56095d51557e.webp)

6. Set up remote access, no need to modify by default, click "Next".

![](https://file-us.ugreennas.com/admin/article/2025-09-05/90c613aad8cc42a6af84ab3937d4084e.webp)

7. The initial configuration is complete, click "Finish", and you will be redirected to the login page.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/abbd269c741e431bac6d82474f1b03e6.webp)

8. Log in with the administrator username and password created during initialization.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/7dc68f5136de4117850eab3d67b0be06.webp)

9. Start creating your library and scraping.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/b9e93e352e904bf38f2a5f5b6e51da3b.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-05/87a727baf8a9451ea85d90667301b678.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-05/bc87767ac8c04228b54f66eb1bbdbed0.webp)

10. Set up transcoding, and select QSV for hardware acceleration.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/b4b6b9c066ec430e97f645f2096f92af.webp)

## Notes

● The container's volume and the configured file/folder paths are for reference only. You can create them according to your personal preferences.

● Port configuration, it is recommended to keep the container's web-accessible port and the local port consistent. If there is a local port conflict, change it to an unused port; non-web access defaults to automatic.

● The local ports between containers must not be the same; port conflicts can prevent containers from starting.

● The quick access web link is only available for access in bridge mode.

● The image only provides a tutorial for building the container. For usage methods and in-depth play, please search for tutorials online.

● The image is developed by a third party. For specific configuration changes and bug fixes, please pay attention to the relevant official information.

## Configuration Recommendations

1. **Set up regular backups:** Since Jellyfin configurations and library information are very important, it is recommended to regularly back up the `/config` directory.

2. **Optimize performance:** If you are using a mechanical hard drive to store media files, it is recommended to place the configuration on an SSD to improve access speed and transcoding performance.
