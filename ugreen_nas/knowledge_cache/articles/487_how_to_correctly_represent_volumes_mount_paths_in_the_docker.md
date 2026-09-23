# How to Correctly Represent Volumes Mount Paths in the Docker Compose Configuration File?

> **Article ID**: `487`  
> **Category**: `Application Guide > Docker > FAQ > How to Correctly Represent Volumes Mount Paths in the Docker Compose Configuration File?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/487  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client, Web Browser

**Applicable Version**: NAS Firmware 1.18.0.0032 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Problem Description

When configuring the Docker `docker-compose.yml` file, it is necessary to mount the data directory inside the container to a local folder on the NAS for data persistence. However, sometimes we may not be clear on how to correctly represent the local folder path, especially when dealing with the volume of the NAS.

## Solution

To simplify path mounting in Docker Compose configurations, UGOS Pro provides the **Copy storage path** feature in "**Files**", allowing users to quickly obtain the paths of shared folders or personal folders on the NAS. The following steps provide detailed instructions (using TMM container deployment as an example):

### Understanding the volumes Mount Path Format

In the Docker Compose file, the mount path for`volumes` is typically represented in the following format:

```
Local path: Container path
```

● The left side of the colon `(:)`is the **local path**, which represents the actual folder location on the host (NAS).

● The right side of the colon `(:)` is the **container path**, which represents the folder location inside the container.

![](https://file-us.ugreennas.com/admin/article/2026-08-10/2cc5afe4c51743dcaa761d1b108203ad.webp)

There are two types of mount paths:

**Relative path**

![](https://file-us.ugreennas.com/admin/article/2026-08-10/c57cc1d8a4994a50a43c76a46b5f14dd.webp)

A relative path is based on the directory where the `docker-compose.yml` file is located. For example:

```
./config:/config
```

● `./config`：`./`represents the directory where the `docker-compose.yml`file is located, and`config` is a subfolder within that directory.

● Inside the container `/config`：This mounts the local `config` folder to the `/config`folder inside the container.

This method is suitable for quickly creating and managing the necessary folders for the container in the current working directory.

**Absolute path**

An absolute path directly specifies the exact folder location on the host (NAS). For example:

```
/volume1/docker/tmm/config:/config
```

● `/volume1/docker/tmm/config`：Represents the absolute path on the NAS volume.

● Inside the container `/config`：This mounts the contents of this path to the `/config` folder inside the container.

This method is more suitable for explicitly specifying shared folders or user-specific folders on the NAS.

![](https://file-us.ugreennas.com/admin/article/2026-08-10/eb125c200d4841148e96a81402157863.webp)

### How to Copy the Folder Path on NAS

#### Copy the path of a secondary shared folder

Shared folder paths are typically used for collaboration and sharing data:

1. Go to "**Files**" > "**Shared Folder**", and find the target subfolder.

2. Right-click on the folder, select "**Properties**", and click "**Copy Storage Path Location**" to get the path.

**Note**: The path copying feature is not supported for the top-level shared folder directory.

Example path: `/volume1/Shared Folder/Subfolder`

![](https://file-us.ugreennas.com/admin/article/2026-08-10/c6b02b68064e479ea8f7f29c63e85521.webp)

#### Copy the Path of a Personal Folder

Personal folder paths are commonly used for individual user data storage:

Go to "**Files**" > "**Personal Folder**", and similarly, copy the path via "P**roperties**".

Example path: `/home/username/Personal Folder`

![](https://file-us.ugreennas.com/admin/article/2026-08-10/d297771335af4ee39fe7eb301fd58b33.webp)

### Using Paths in the Docker Compose File

After copying the path, you can directly insert it into the `volumes` configuration in the `docker-compose.yml` file. For example:

```
services:
    tinymediamanager:
        image: 'dzhuang/tinymediamanager:latest-v5'
        extra_hosts:
            - 'api.themoviedb.org:13.35.67.86'
            - 'image.tmdb.org:104.16.61.155'
            - 'api.themoviedb.org:13.224.161.90'
        ports:
            - '5900:5900'
            - '5800:5800'
        environment:
            - ENABLE_CJK_FONT=1 
            - TZ=Europe/Madrid 
            - USER_ID=0 
            - GROUP_ID=0 
        volumes:
            - /volume1/media:/media 
#Mount the media folder from the NAS storage to the container's /media directory，so that TMM inside the container can access these files.
            - /volume1/docker/tmm/config:/config
#Mount the folder used for saving configuration data from the NAS storage to the container's /config directory to save settings, logs, and other data.
        container_name: tinymediamanager
```

**Note**: Please ensure that the local paths used in the Docker Compose file actually exist. Otherwise, it may result in the container deployment failure.
