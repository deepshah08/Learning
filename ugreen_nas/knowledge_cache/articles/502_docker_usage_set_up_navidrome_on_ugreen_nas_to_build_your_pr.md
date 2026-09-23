# [Docker Usage] Set Up Navidrome on UGREEN NAS to Build Your Private Music Library

> **Article ID**: `502`  
> **Category**: `Application Guide > Docker > Docker Gameplay > [Docker Usage] Set Up Navidrome on UGREEN NAS to Build Your Private Music Library`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/502  

---

## Introduction to Navidrome

Navidrome is an open-source web-based music streaming server, specifically designed for users who wish to host their music collections on personal devices and enjoy convenient access. It supports playing personal music libraries through web browsers or mobile devices. Inspired by projects such as Subsonic and Ampache, Navidrome adopts a more modern technical architecture to deliver a lightweight and easy-to-deploy service.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/88dc314f58be497b84e3130157cd30e8.webp)

## Deploying Containers Using Docker Compose

On the UGOS Pro system, it is recommended to use *Projects (Docker Compose)* for quickly deploying containers. This approach is ideal for scenarios where multiple containers need to be managed simultaneously, as it simplifies the deployment and management process. Below are the detailed steps to deploy Navidrome using Docker Compose.

Click to learn more: [What is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### Access the Docker Projects Interface

On the UGOS Pro system, open the Docker application and click [Project] > [Create] to launch the project creation wizard.

### Configure the Docker Compose File

In the project creation wizard, you will need to upload a Docker Compose configuration file. Below is a sample configuration for Navidrome:

```
services:
  navidrome:
    image: deluan/navidrome:latest
    restart: always
    volumes:
      - ./data:/data  #Custom cache path
      - /path/to/your/music/folder:/music:ro  #Custom path to your music folder; adjust based on actual location
    environment:
      ND_ENABLETRANSCODINGCONFIG: true  #Enable transcoding settings in the UI
      ND_TRANSCODINGCACHESIZE: 0 #Size of the transcoding cache; set to "0" to disable caching
      ND_SCANSCHEDULE: 1h  #Schedule regular library scans using "cron" syntax; set to "0" to disable
      ND_LOGLEVEL: info  #Log level, useful for troubleshooting
      ND_SESSIONTIMEOUT: 24h #Duration Navidrome waits before closing an idle session
      ND_BASEURL: ""  #Base URL for Navidrome when used behind a proxy (e.g., /music or https://music.example.com)
      ND_ENABLESHARING: true  #Enable the sharing feature
    ports:
      - 4533:4533 #Map host port 4533 to container port 4533; this is the default web port for Navidrome
```

### Parameter Description

**image:** Specifies the Docker image and version to use. `latest` means the latest version will be pulled.

**restart:** Defines the container restart policy. `always` means the container will automatically restart if it stops or crashes.

**volumes：**

`./data:/data`：`./` refers to the current directory where the Docker Compose file is located. It mounts the container's `/data` directory to the NAS host's `./data` path to store Navidrome's config files and cache. This ensures the data persists even if the container is deleted or rebuilt.

`/path/to/your/music/folder:/music:ro`: This mounts the NAS host’s music directory (`/path/to/your/music/folder`) to the container’s `/music` directory. The mount is set to read-only (`ro`), preventing the container from modifying the music files on the host. Please replace `/path/to/your/music/folder` with the actual path where your music files are stored.

● For example: Modify the path `/path/to/your/music/folder:/music:ro` to match your actual storage location. If your music files are stored in the `music` folder under volume 5 on the NAS host, you should change the path to `/volume5/music:/music:ro`. Here, `/volume5/music` is the music directory path on your host, while `/music:ro` is the mount point inside the container. The `ro` option ensures that the directory is mounted in read-only mode, preventing the container from modifying the music files on your host.

**environment：**

`ND_ENABLETRANSCODINGCONFIG`: Set to `true` to enable the audio transcoding configuration feature in Navidrome's web UI. Transcoding allows music files to be dynamically converted to specific formats (such as MP3) to meet client playback requirements.

`ND_TRANSCODINGCACHESIZE`: Specifies the size of the transcoding cache. A value of `0` disables caching, meaning transcoded data will not be temporarily stored.

`ND_SCANSCHEDULE`: Defines the interval for periodically scanning the music library. This uses a `cron`-like syntax for scheduling; here it is set to scan every hour. Set to `0` to completely disable automatic scanning.

`ND_LOGLEVEL`:Sets the logging level, which determines the amount of detail included in logs. Typical values include `info` (default) and `debug` (for detailed troubleshooting).

`ND_SESSIONTIMEOUT`: Specifies the session timeout duration for inactive users. Setting it to `24h` means the web interface will automatically log out the user after 24 hours of inactivity.

`ND_BASEURL`: Sets the base URL for accessing Navidrome behind a reverse proxy, e.g., `/music` or `https://music.example.com`. If left as an empty string (`""`), the default root path will be used.

`ND_ENABLESHARING`: Enables the sharing feature, allowing users to share music or playlists.

**ports:** Maps port 4533 on the host to port 4533 in the container, which is Navidrome’s default web service port.

### Deploy the Project

After confirming that the configuration is correct, click [Deploy]. The system will automatically pull the image and start the container. Once deployment is complete, you can access the Navidrome homepage via `http://<NAS_IP>:port` (for example: `http://192.168.22.153:4533`).

![](https://file-us.ugreennas.com/admin/article/2025-09-09/a39fc4f388c14499bbf0a3ec1515e7c5.webp)

## Accessing the Navidrome Interface

1. Open a browser and enter `http://<NAS_IP>:4533` to launch Navidrome’s web management interface. You’ll be prompted to create the first user, who will act as the superuser with full administrative access to all aspects of Navidrome, including the ability to manage other users. Enter your desired username and password, confirm the password, and click the "Create Admin" button.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/dad34be4a58640818a39aaee156b0d79.webp)

2. After creating the account, click the avatar in the upper-right corner > Personal, then change the language to English.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/5b975dccd15648ccaffcf99dd1517594.webp)

3. Here, you can see the scanned directories. It usually takes a few minutes for your music to begin appearing in the Navidrome UI. You can check the logs to monitor the scanning progress. If you encounter any errors, feel free to [contact the official Navidrome team](https://www.navidrome.org/community/) for assistance.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/e90371d30a054e20985386cdaee0ef39.webp)

4. Once the scan is complete, you can browse and listen to all your music.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/d6317120dab041c29ce0639ca4492b31.webp)

## If your music files are missing covers, tags, and other information, you can use Music-tag for online scraping

Music-tag is a powerful music tag management tool that automatically retrieves and updates the metadata of music files, such as album covers, artist information, track order, and more. If you want to keep your music library tidy with accurate metadata, Music-tag is a great choice.

On UGREEN NAS, you can deploy the Music-tag Web version to enable automatic scraping of music files. This allows you to manage and update the music stored on your NAS directly through Music-tag, making the process both convenient and efficient.

Click to learn more: [[Docker Usage] Deploy an Online Music Scraper (Music Tag Web) on UGREEN NAS](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjoxNDYxLCJhcnRpY2xlSW5mb0lkIjo1MDAsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIn0=)

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
