# Get the real path of the NAS folder and mount it to the Docker container.

> **Article ID**: `611`  
> **Category**: `Application Guide > Docker > FAQ > Get the real path of the NAS folder and mount it to the Docker container.`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/611  

---

When using Docker, you may need to mount a folder from the NAS to the Docker container so that the container can access data on the NAS. Below are the detailed steps and considerations to help you complete this operation.

* Docker currently supports mounting shared folders from the NAS, but personal folders are not supported.
* If you need to mount a personal folder, consider moving it to a shared folder.

## **Get the Folder Path**

1. Locate the target folder (e.g., the "media" folder).
2. Right-click on the target folder and select the [Properties] option.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/b8b83764-1193-4db6-bc0f-a38836af7cd7.png)

3. In the opened properties window, copy the folder's location information; this is the real path of the folder. Example:`/volume3/media`

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/66d235c5-3c4f-4da5-b927-fcb5d0347163.png)

## **Configure Docker Compose**

Open your Docker Compose configuration and add the mount path of the NAS folder in the `volumes` section.

The mount path format is:`/NAS real path:/container path`，for example:

```
  volumes:                       
    - ./config:/config                      
    - /volume1/media:/media
```

Explanation:

* `./config:/config`：The configuration structure is `NAS directory: container directory`，meaning that the `config` folder in the current directory is mounted to the`/config` path in the container. `./`indicates that the path is within the directory chosen for the current project.
* `/volume1/media:/media`：Mounts the `media` shared folder from the NAS to the `/media` path in the container.

## Custom Container Directory

The path inside the container can be customized as needed, such as `/media` or `/volume1/media`，to make it easier to locate within the container.

Note:

* The NAS real path in Compose must match the [Location] displayed in the NAS files to avoid mounting failures due to client path differences.

* Left-side path: Paste the NAS real path (e.g., `/volume1/media`）.
* Right-side path: Customize the container path (e.g., `/media`），It is recommended to maintain the same directory structure as the NAS path.

## Permission Management (Optional)

If there are permission issues when the container accesses the shared folder content after mounting the shared folder, you need to add `PUID`, `PGID`, and `UMASK` with values set to `0` under the `environment` section in the `Compose` file. This ensures that the container's permissions match those of the NAS directory.

```
environment:  
  - PUID=0  
  - PGID=0  
  - UMASK=0
```

## Complete Docker Compose Configuration Example

Below is a complete `docker-compose.yaml` example, including the configuration to mount the NAS folder:

```
services:
  emby:
    image: emby/embyserver:beta # Image Name
    container_name: emby-server
    restart: always # Restart Policy
    devices:
      - /dev/dri:/dev/dri # Enable Integrated Graphics
    environment:
      PUID: 0 # Container Running User ID,Root Privileges
      PGID: 0 # Container Running Group ID,Root Privileges
    volumes:
      - ./config:/config # Configuration File
      - ./metadata:/metadata # Media Metadata
      - /volume3/media:media # Movie Storage Path,the container can read the movies from the path.Replace the path on the left side of the colon with the actual path where movies are stored on your NAS,and the right side of the colon is the path inside the container.
    ports:
      - 8096:8096 # Map the container's port 8096 to the NAS's port 8096.
```
