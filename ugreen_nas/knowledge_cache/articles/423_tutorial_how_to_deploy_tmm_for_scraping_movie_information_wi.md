# [Tutorial] How to Deploy TMM for Scraping Movie Information with Docker Compose to Create the Perfect NAS Poster Wall?

> **Article ID**: `423`  
> **Category**: `Application Guide > Docker > Docker Gameplay > [Tutorial] How to Deploy TMM for Scraping Movie Information with Docker Compose to Create the Perfect NAS Poster Wall?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/423  

---

TinyMediaManager (abbreviated as TMM) is an open-source multimedia management tool primarily used for scraping metadata of video files from the internet, such as movie information, covers, posters, etc. TMM can download this information locally to facilitate better management and presentation of movies in multimedia software like UGREEN NAS "Theater", Kodi, Jellyfin, Emby, Plex, etc. TMM supports multiple platforms, including Windows and Mac clients, and also provides a Docker version suitable for NAS users to deploy.

## How to Deploy TinyMediaManager via Docker Compose？

Docker Compose is a tool for defining and running multi-container Docker applications. By writing a YAML file, users can configure the application's services, networks, volumes, etc., making it easy to quickly launch and manage complex application environments. For more details.

To accommodate the specific configuration requirements of TinyMediaManager, it is recommended to use Docker Compose for deployment to ensure more flexible and manageable configurations. The following are the detailed deployment steps:

### Step 1: Access the Docker Project Interface

Enter the UGOS Pro system, open the Docker application, and click on **[Project]** > **[Create]**" to launch the project creation wizard.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/9d3a94d2d75f4a5d9ef1f43ae9192b5e.webp)

### 

### 2: Configure the Docker Compose File

When creating a project, you need to provide a Docker Compose configuration file. Here is an example of the configuration file:

```
services:
    tinymediamanager:
        image: 'dzhuang/tinymediamanager:latest-v5'
#Specify the Docker image to pull, `dzhuang/tinymediamanager:latest-v5` is the image for TinyMediaManager. `latest-v5` indicates the latest version 5.
        extra_hosts:
            - 'api.themoviedb.org:13.35.67.86'
            - 'image.tmdb.org:104.16.61.155'
            - 'api.themoviedb.org:13.224.161.90'
#extra_hosts configures some custom DNS resolution records inside the container. Here, domains related to themoviedb.org are resolved to specific IP addresses, which is typically used to resolve DNS resolution issues or to speed up access.
        ports:
            - '5900:5900'
            - '5800:5800'
#Map the host's port 5900 to the container's port 5900, typically used for VNC remote access.
#Map the host's port 5800 to the container's port 5800, typically used for web interface access.
        environment:
            - ENABLE_CJK_FONT=1 
#Enable support for Chinese, Japanese, and Korean fonts.
            - TZ=Europe/Madrid 
#Set the container's timezone; the default is Asia/Shanghai, which can be adjusted according to your region
            - USER_ID=0 #The username for read/write operations
            - GROUP_ID=0 #The user group used by the container 
#Set the user ID and group ID inside the container; `0` typically represents the root user with administrative privileges.
        volumes:
            - '/volume1/media:/media'  
#Map the media folder that needs to be scraped for movies in the NAS storage space to /media (access media files).
            - './config:/config' 
#Map the folder where configuration data files are stored in the NAS storage space to /config. The path before the “:” can be set by yourself; “./” represents the directory where the current Docker Compose file is located
        container_name: tinymediamanager
```

**Parameter Description:**

● `image`：Specifies the Docker image used to run TMM.

● `container_name`：The name of the container for identification and management.

● `extra_hosts`: Configures custom DNS resolution records for acceleration or resolution of domain name issues.

● `ports`：Maps the ports inside the container to the outside of the NAS, allowing you to access TMM through a web browser.

● `volumes`：Maps local media folders and configuration folders on the NAS to the container to ensure data persistence.

● `environment`：Sets environment variables such as font support, time zone, user permissions, etc.

### Step 3: Deploy the Project

After confirming that the configuration file is correct, click "Deploy Now", and the system will automatically pull the Docker image and create and run the container based on the YAML file.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/bc8f2577ffc4485695f26b48c144f2f1.webp)

**Notes:**

1. If the image fails to pull, it may be due to network, proxy, or firewall issues. We provide a Baidu Netdisk download link for the image package, which you can manually download and import as a local image. Access path: [Baidu Netdisk link](https://pan.baidu.com/s/1vi65COwmR9afNu9d__WRxg?pwd=9j19) extraction code: 9j19

2. It is recommended to store the Docker configuration directory on an SSD to prevent mechanical hard drives from not entering sleep mode, which can affect system performance.

### Step 4: Access TinyMediaManager

After successful deployment, enter the NAS IP address and port number in the browser's address bar, for example: `http://192.168.66.43:5800`, or click the "Quick Access" button in the Docker container interface to enter the TMM interface.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/058c9dc769014bdfaf923d6f061fdda7.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-05/a654f9b0ed18426088b5c8125ddac8be.webp)

## How to Configure TinyMediaManager

After the first login to TMM, you need to perform some basic configurations, such as setting the media library path, selecting scrapers, etc. For detailed initial setup steps, please refer to[【Tutorial】Everyone Can Learn, Step by Step Guide to Building the 'Simplest' NAS Media Library by Using TMM Scrap Movie Information.](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMjgxLCJhcnRpY2xlSW5mb0lkIjo0MjIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)
