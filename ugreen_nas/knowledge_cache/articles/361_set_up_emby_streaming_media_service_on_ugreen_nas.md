# Set Up Emby Streaming Media Service on UGREEN NAS

> **Article ID**: `361`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Set Up Emby Streaming Media Service on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/361  

---

## App Introduction

**Emby** is a powerful streaming media center designed to centralize the management of personal media content and enable playback across various devices. Emby supports a wide range of media formats, including videos, music, and photos. It can automatically transcode and stream media content to ensure smooth playback on any device.

## Docker Compose Deployment

On the UGOS Pro system, it is recommended to use the [Docker Compose](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9) method for quickly deploying containers, especially in scenarios where multiple containers need to be managed simultaneously. This approach simplifies container deployment and management. Below are the detailed steps for deploying Emby using Docker Compose:

1. Open the **"Docker"** app and click [Project] > [Create] to launch the project creation wizard.

2. In the project creation wizard, enter the following Docker Compose configuration for Emby. These configurations are for reference only—you can adjust them according to your needs.

```
Media Storage Path (Replace the path on the left with your actual media storage path on NAS, and the right side is the container's path)services:
  emby:
    image: emby/embyserver:beta # Image Name
    container_name: emby-server
    restart: always # Restart Policy
    devices:
      - /dev/dri:/dev/dri # Enable iGPU Acceleration
    environment:
      PUID: 0 # Container Run User ID (Root Privileges)
      PGID: 0 # Container Run Group ID (Root Privileges)
    volumes:
      - ./config:/config # Configuration File
      - ./metadata:/metadata # Media Metadata
      - /volume3/media:media # Media Storage Path (Replace the path on the left with your actual media storage path on NAS, and the right side is the container's path)
    ports:
      - 8096:8096 # Map container port 8096 to NAS port 8096
```

3. After completing the configuration file, click "Deploy." The system will automatically pull the image and start the container.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/4c6e36f52ac049dd810b649ebf864b87.webp)

4. After deployment is complete, access Emby through a browser. In the browser's address bar, enter `http://NAS_IP:8096`. For example, if the NAS IP is 172.17.70.87, enter `http://172.17.70.87:8096`to access it.

You can find the NAS device's IP address in the Control Panel under **[Network]**, then click "Network Connection" to view the IP address.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/ad36776d7d0b4e65b38dcdc83eb48a8f.webp)

### Compose Configuration Parameter Explanation

|  |  |
| --- | --- |
| **Parameter** | **Explanation** |
| **image** | Specify Docker image,`beta`is the test version. |
| **restart** | Set the restart policy to `always`, so the container will automatically restart if it crashes or stops, ensuring continuous service operation. |
| **devices** | Enable NAS integrated GPU for hardware acceleration, such as video transcoding. By mounting this device, Emby can use the NAS GPU for video transcoding, improving processing efficiency and reducing CPU load. |
| **environment** | Set environment variables to configure services within the container.  `PUID/PGID`：Define the user and group permissions for running the container. |
| **ports** | Port Mapping: Map port 8096 on the NAS to port 8096 on the container. You can access the web interface via `http://NAS_IP:port`. |
| **volumes** | Map local NAS folders to container mount paths.    `./config`：Used to store Emby configuration files.  `./metadata`：Used to store Emby media metadata (such as movie posters, actor information, etc.).  `/volume3/media`：Video storage path. Emby can scan this directory and manage video files, matching movie posters and other data. Replace the `/volume3/media` path on the left side of the colon with the actual path where you store your media files on the NAS. |
| **Additional notes** | `./`Indicates that the path is within the current project's chosen storage path.  `./:/`Means that the local NAS `./` directory is mounted to the container's `/` directory.  The path before the colon is the folder storage path on the NAS, and the path after the colon is the corresponding mount path inside the container. |

## Initial Configuration

When logging into Emby for the first time, you need to complete the initial configuration:

1. Select your preferred language (e.g., "English(United States)") and click "next". Refreshing the browser page will switch to the language you just selected.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/316f96eb11884d53af25100e670a51df.webp)

2. Set the username and password, then click "Next" to continue.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/251a1f0156d34a489751b506cc903d31.webp)

3. You can skip configuring the library during the initialization, click "Next" to continue.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/6ccbbaacd9234caab72de945c0a429d4.webp)

4. Enabling "Automatic Port Mapping" has no impact on functionality and can be skipped.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/d669b74b06a9498686e030c36c09ec73.webp)

5. Check "I accept the terms of use" and click "Next."

![](https://file-us.ugreennas.com/admin/article/2025-09-05/6eb0aac30bcd4221b0089fc1a3fd4331.webp)

6. At this step, as shown in the image, the initialization is complete. Click "Finish."

![](https://file-us.ugreennas.com/admin/article/2025-09-05/c4b699d370d94569953ed83d33ec46b3.webp)

● After initialization is complete, please log into the system using the user account you just created.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/63b7c46effb14ff5881784faafded144.webp)

## Add Library

After logging in, follow these steps to add a library and manage your resources:

1. Click "Manage Emby Server" to enter the "Settings" page.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/95b36d6479ff4ab19f21304c777d901b.webp)

2. In the "Library" option, click "+ New Library". Categorize based on the type of media content (e.g., "Movies" or "TV Shows").

![](https://file-us.ugreennas.com/admin/article/2025-09-05/61ab93fc7a1248afa54c6961ee0b6805.webp)

### Recommended Settings for Movie Library

● Content Type: Select "Movies".

● Display Name: Customize the name.

● Folders: Refer to the path you set in the Compose configuration. For example, if you set the path as /volume3/media in your NAS, the corresponding folder path in Emby should be /volume3/media. Locate the corresponding path here.

● Preferred Metadata Download Language, Certification Country, etc., can be adjusted as needed.

● Other parameters can be adjusted as required.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/cbc351dd69d444c8aa980725acf90b44.webp)

### Recommended Settings for TV Shows/Variety Library

● Content Type: Select "TV Shows."

● Display Name: Customize the name.

● Preferred Metadata Download Language, Certification Country, etc., can be adjusted as needed.

● Folders: Same as the Movie settings.

● Other parameters can be adjusted as required.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/243459dcee2242faa96b24ae6bbf395d.webp)

## Enable Hardware Transcoding

Emby supports hardware transcoding, but it requires an active Emby Premiere subscription. Without this subscription, hardware transcoding cannot be used even if it is enabled.  
When enabling hardware transcoding, select "Advanced" mode. After the GPU drivers are loaded, more decoder options will be unlocked.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/67e5e55610054aae954fda119f7beff5.webp)

## FAQ

### Q: How to obtain the actual path of a NAS folder and mount it to the Docker container

**A:** When using Docker, you may need to mount folders from your NAS to the Docker container so that the container can access data stored on the NAS. You can refer to [Get the real path of the NAS folder and mount it to the Docker container](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTkzMCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo2MTEsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D) to help complete this task.

## Notes

● The images used in this tutorial are developed and maintained by third parties. This tutorial is for reference only. UGREEN assumes no responsibility for risks caused by improper operations, software vulnerabilities, or image updates, such as file anomalies or data leaks. Please use trusted images to ensure system and data security.

● The container file path can be customized. When accessing via a web browser, the container port must match the local port, and the local ports of different containers must not conflict.

● Container web links are only accessible in bridge mode.

● This image is only used to demonstrate the setup process. For specific usage and features, please refer to online resources. For configuration changes and bug fixes, follow the official announcements.

● It is recommended to store the Docker configuration directory on an SSD to avoid performance issues caused by mechanical hard drives.
