# How to Deploy the Shinobi Open-Source Video Surveillance System Using Docker

> **Article ID**: `476`  
> **Category**: `Application Guide > Docker > Docker Gameplay > How to Deploy the Shinobi Open-Source Video Surveillance System Using Docker`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/476  

---

## Shinobi: A Powerful Open-Source Video Surveillance Solution

Shinobi is a robust open-source video surveillance system that supports various camera protocols, including the widely used ONVIF (Open Network Video Interface Forum) protocol. By using the official `shinobisystems/shinobi` Docker image, you can easily deploy Shinobi on a UGREEN NAS in minutes, enabling real-time monitoring and playback of ONVIF-compatible devices.

## Key Features of the Shinobi Image

1. **Lightweight Container Deployment**: With Docker, you can easily run Shinobi on a UGREEN NAS without complex installation steps, saving both system resources and deployment time.

2. **Support for Multiple Video Protocols**: Shinobi is compatible with common video streaming protocols such as RTSP, MJPEG, and HLS, and supports the ONVIF protocol, allowing automatic detection and management of ONVIF-compliant cameras.

3. **Real-Time Monitoring and Video Playback**: Shinobi offers real-time video surveillance with recording and storage capabilities, enabling users to play back historical footage at any time.

## Deploy Shinobi with Docker Compose

To quickly deploy Shinobi on a UGREEN NAS, it's recommended to use Docker Compose for containerized deployment, especially when you need to efficiently create and manage multiple containers. The following steps will guide you through deploying Shinobi using Docker Compose. [What is a project(Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### Access the Docker Project Interface

In the UGOS Pro system, open the Docker application, click on [Project] > [Create] to start the project creation wizard.

### Configure the Docker Compose File

When creating a project, you'll need to provide a Docker Compose configuration file. Below is an example configuration file for Shinobi:

```
services:
  Shinobi:
    image: registry.gitlab.com/shinobi-systems/shinobi:dev
    container_name: Shinobi
    restart: always
    devices:
      - /dev/dri:/dev/dri
    ports:
      - "8080:8080/tcp"
    volumes:
      - ./streams:/dev/shm/streams:rw
      - ./config:/config:rw
      - ./customAutoLoad:/home/Shinobi/libs/customAutoLoad:rw
      - ./database:/var/lib/mysql:rw
      - ./videos:/home/Shinobi/videos:rw
      - ./plugins:/home/Shinobi/plugins:rw
      - /etc/localtime:/etc/localtime:ro
```

### Parameter Description

● **image**：Specifies the use of the `shinobisystems/shinobi:dev` image, which is hosted in the GitLab container registry.

● **container\_name：**Assigns a name to the container for easy management, named `Shinobi`here.

● **devices：**Mounts the host's `/dev/dri` device to the container for hardware acceleration, such as video transcoding.

● **ports：**Maps port 8080 on the host to port 8080 in the container, allowing users to access Shinobi's web interface via the host's IP and port 8080.

● **volumes：**Mounts local paths to the container to ensure data persistence.

● `./streams`：Maps the local folder `streams` to `/dev/shm/streams` in the container with read-write (`rw`) permissions, using shared memory to accelerate video processing.

● `./config`：Maps folder `config` to `/config` in the container with read-write permissions to save settings.

● `./customAutoLoad`：Used for loading custom plugins or scripts.

● `./database`：Stores database files in the local `./database` directory.

● `./videos`：Used for storing video recordings.

● `./plugins`：Used for storing plugins.

● `/etc/localtime`：Syncs the time between the host and container, set to read-only.

● **restart：**Configures the container to start automatically after the NAS is rebooted.

### Deploy the Project

After confirming that the configuration file is correct, click [Deploy]. The system will automatically pull the Shinobi image and start the container based on the YAML file. Once deployed successfully, you can access the Shinobi dashboard by visiting `http://<your-server-ip>:8080` in your browser.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/24068f39f59b491eae29a6d59db7cd30.webp)

## Access the Shinobi Admin Panel

After the deployment is complete, open a browser and enter the NAS IP address and port (e.g., `http://192.168.66.43:8080/super`). The default admin username and password can be found in the container logs. Once logged in with the admin credentials, you can access the management dashboard.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/dbe3b5cb8cfd4e3a9b57951cdfe1a59d.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-10/2a99ec64c932445cbb1639f5af253b17.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-10/ea5ef2ed295c45a8ac612cfe93a80f64.webp)

### Create a Monitoring Admin Account

In the admin panel, navigate to the **Accounts** page and click the **+Add** button to create a new monitoring admin account. Set the username, password, video retention period, and other details, then click **Save** to apply the changes.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/d1de994534984a5fa37f0adae1104daf.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-10/d0436d4316374d4c926fd4e1fd785352.webp)

After the monitoring account is successfully created, the following information will be displayed. You can modify or delete the account at any time from this interface.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/2a2fd11f91eb4ed3892cf7ddd16eb0bd.webp)

### Configure ONVIF Cameras

Next, access the Shinobi monitoring interface. In the browser's address bar, remove /super and press Enter to go to the login page for the monitoring interface. Enter the monitoring account username and password you just created, then click "Login" to enter the Shinobi monitoring page.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/b3e9903483a242eab1e3f81ff7f4c033.webp)

Click **ONVIF Scanner** in the left toolbar. Shinobi will automatically scan for ONVIF cameras on the local network, or you can manually enter the camera's IP address, port, username, and password. Click **Search** to find and add the camera.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/fa79c1f7bbff4b9da18b97cbda8e4f37.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-10/96527d14dfcb41fd806bca7718d0670b.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-10/fa4eddeb3ff44d58819623efbcceac19.webp)

### Set Monitoring Mode

Double-click the detected camera to enter the settings page, then set the monitoring mode to **Record**.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/9a611c7e59664d11b3ce87de344986ae.webp)

Scroll down the page, select **Auto** for both **Video Codec** and **Audio Codec**, then click **Save** to apply the settings.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/89080822742b4cdba0851891d9cb3139.webp)

## View Monitoring Recordings

In the Shinobi interface, you can view real-time monitoring feeds and historical recordings. The video files are stored in the `./videos` directory that you configured. By hovering your mouse over the monitoring feed, you can control camera functions such as pan, tilt, and zoom.

Click the camera thumbnail on the left to display the feed on the main screen. If the camera was just configured, the main screen may initially show a black screen, which is normal. Wait a few minutes for the feed to display correctly.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/879ffaebaabd4711b3fea311be267e7f.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-10/2859c20ccec24205a1dbf58efc6c70d8.webp)

When you hover your mouse over the monitoring feed, a toolbar will appear, allowing you to view historical recordings and control the camera's movement direction.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/c976d425690a480c8dc1fabf7413bcfb.webp)

You can also view the recorded surveillance videos in the folder you specified for saving recordings when creating the Shinobi project (such as the `videos` folder in the tutorial).

## Advantages of Supporting ONVIF Devices

ONVIF is an open industry standard that promotes interoperability between network video devices. By supporting the ONVIF protocol, Shinobi offers the following advantages to users:

1. **Automatic Device Discovery**: Shinobi can automatically detect ONVIF-compatible devices on the local network and quickly add them to the system, simplifying the device management process.

2. **Remote Real-Time Control**: Shinobi supports remote operation of PTZ (Pan-Tilt-Zoom) cameras, allowing users to control the camera's direction and zoom functions through the interface.

3. **High Compatibility**: As an open protocol, ONVIF enables Shinobi to be compatible with most IP cameras on the market, providing users with flexibility and scalability.
