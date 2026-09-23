# Deploy an Online Music Scraper (Music Tag Web) on UGREEN NAS

> **Article ID**: `500`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Deploy an Online Music Scraper (Music Tag Web) on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/500  

---

## Introduction to Music Tag Web

The [Music Tag] Web version is an application that allows you to edit song information such as title, album, artist, lyrics, and cover art. It supports a wide range of audio formats, including FLAC, APE, WAV, AIFF, WV, TTA, MP3, MP4, M4A, OGG, MPC, OPUS, WMA, DSF, and DFF. For more details about its features, please refer to the ["Music Tag Web Official Documentation".](https://xiers-organization.gitbook.io/music-tag-web-v2)

![](https://file-us.ugreennas.com/admin/article/2025-09-09/888fdc7e6f884844a0cca6937749539a.webp)

## Deploying the Container Using Docker Compose

On the UGOS Pro system, it is recommended to use Docker Compose for quickly deploying containers. This approach is ideal for managing multiple containers at once and simplifies the deployment and management of containerized applications. Below are the detailed steps for deploying the Music Tag Web service using Docker Compose.

Click to learn more: ["What is a Project (Docker Compose)?"](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### Access the Docker Project Interface

On the UGOS Pro system, open the Docker application, and go to [Project] > [Create] to launch the project creation wizard.

### Configure the Docker Compose File

In the project creation wizard, you need to upload a Docker Compose configuration file. Below is an example configuration for Music Tag Web:

```
services:
  music-tag:
    image: xhongc/music_tag_web:latest # Use the latest image
    container_name: music-tag-web # Assign a name to the container
    ports:
      - "8002:8002" # Map container port 8002 to NAS port 8002
    volumes:
      - /volume1/music:/app/media #Mount the NAS music directory to the container's music directory for access and management
      - ./config:/app/data # Mount a NAS directory to the container's data directory for persistence
    restart: always # Always restart the container to ensure high availability
```

### Parameter Description

**services:**

● Defines a list of services, each corresponding to a container instance. In this case, it's `music-tag`.

**image:**

● Specifies the container image name and version. Here, `xhongc/music_tag_web:latest` indicates using the latest version of the `Music Tag Web` image.

**container\_name:**

● Assigns a custom name to the container for easier identification and operation during container management.

**ports:** Configures the port mapping between the host and the container.

● NAS port 8002 is mapped to container port 8002. This allows you to access the service via `http://<NAS_IP>:8002`.

**volumes:** Configures volume mounting for persistent storage.

● Maps the NAS music directory to `/app/media` inside the container, enabling the container to access and manage music files.

● Please replace `/path/to/your/music` with the actual music storage path on your NAS, for example, `/volume1/Music`.

● Maps the configuration directory on the host to `/app/data` in the container, used to store service configuration and database files to avoid data loss when the container restarts.

● Please replace `/path/to/your/config` with the actual config storage path on your NAS, such as `/volume1/Config/music-tag-web` or `./config`. `./` refers to the directory where the Docker Compose file is located.

**restart:** Configures the container's restart policy.

● The container will automatically restart regardless of the reason for stopping (except when stopped manually).

## Deploy the Project

After confirming that the configuration is correct, click [Deploy], and the system will automatically pull the image and start the container. Once deployment is complete, you can access the Music Tag Web homepage via `http://<NAS_IP>:port` (for example: `http://192.168.22.153:8002`).

![](https://file-us.ugreennas.com/admin/article/2025-09-09/ceafc703f3c34e808080223acfb75d43.webp)

## Access the Music Tag Web Interface

1. Open your browser and enter `http://<NAS_IP>:8002` to open the Music Tag Web login page. For the first login, enter the default username/password: admin/admin.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/0d0f37b18e8f4ab485a6c7ca3b325d49.webp)

2. After successfully logging in, you will be taken to the main interface. The left sidebar will display the music folders from your NAS. These folders correspond to the music directory you mapped earlier when setting up the Music Tag service.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/30792aea1aec4fc9a0125f0bdfdde26d.webp)

3. Click on a music folder on the left side, check one of the songs within it, and the music file will be displayed on the "Operation table" on the right side.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/6b5926e933154f2691181f27fe87b725.webp)

4. In the Operation table, click on the music file to manually edit music information (such as title, artist, album, etc.).

![](https://file-us.ugreennas.com/admin/article/2025-09-09/ddbda62c08fb4012b1739cddd356e83d.webp)

5. Use the automatic scraping function, no need to check the songs, just click directly on the music name, and the interface will switch to a three-screen mode. Click the **"Search"** button to the right of "Title", Music Tag will search for relevant information about the song based on the pre-selected scraping source (such as the global database).

● Auto-fill information: Click on the **small arrow** next to the search result to automatically fill in album name, cover, release year, and other information into the corresponding fields.

● Scrape lyrics: The system will also capture lyric information, making it convenient for subsequent playback display.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/414ba5df141c44c6b13197b1d4c2bd6e.webp)

6. After completing the editing, click "Save Information". By checking the song files on the left, you can preview the detailed information after saving, including newly added album covers or lyrics, etc.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/1513df55cdf44682acee333f79d71202.webp)

7. Music Tag supports batch operations on entire music folders. You can directly check the entire folder and then select the batch operation settings you need, including batch automatic scraping, organizing folders, converting between traditional and simplified Chinese, deleting empty folders, splitting file names, and replacing text, among other operations. This greatly improves the efficiency of music file management.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/26a60f8bc2c140559cf9a966362da6a8.webp)

8. For instance, if you choose batch automatic scraping here, after setting the parameters as needed, click save to initiate batch automatic scraping.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/0171d9de06b94666a07fe433cda0df44.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-09/b917d246ef634bc7ac4ba2b607a2f93f.webp)

9. Click on "Operation log" to view the batch operation logs. If some files fail, you can individually or manually supplement the scraping.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/d7abba888a1e49f0acf388af3ead61ca.webp)

**Related Reading**

[[Docker Usage] Set Up Navidrome on UGREEN NAS to Build Your Private Music Library](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6NDI2MSwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiZW4tVVMiLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo1MDIsImFydGljbGVWZXJzaW9uIjoiMS4wIn0=)

## Notes

Please note that the image used in this tutorial is developed and maintained by a third party. The tutorial is for reference only. UGREEN does not take responsibility for risks arising from improper user operations, third-party software vulnerabilities, or image updates, including but not limited to:

● Third-party images may cause unexpected modification or deletion of files in your UGOS Pro system.

● Using insecure images may result in data being uploaded to third-party servers, posing privacy and data leakage risks.

● To ensure system stability and data security, please carefully choose third-party images from trusted sources.

**Other notes:**

1. The file/folder paths in the container are for reference only. You can create them according to your personal preferences.

2. The container's web access port and local port should match. If there is a conflict, change it to an unused port. Local ports between containers cannot be the same, as port conflicts will prevent containers from starting.

3. The container's web link is only accessible in bridge mode.

4. The image only provides a setup tutorial. For specific usage methods and advanced features, please refer to online resources.

5. The image is developed by a third party, and for specific configuration changes or bug fixes, please follow official information from the relevant developers.

6. It is recommended to store the Docker configuration directory on an SSD to avoid system performance issues caused by mechanical drives.
