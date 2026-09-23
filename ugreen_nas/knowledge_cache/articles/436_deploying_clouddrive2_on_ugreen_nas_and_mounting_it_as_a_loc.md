# Deploying CloudDrive2 on UGREEN NAS and Mounting It as a Local Directory

> **Article ID**: `436`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Deploying CloudDrive2 on UGREEN NAS and Mounting It as a Local Directory`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/436  

---

## Introduction to CloudDrive

CloudDrive is a comprehensive cloud storage management platform designed to seamlessly integrate multiple cloud storage services into a unified interface. With CloudDrive, you can easily manage and access all your cloud storage accounts without the need to switch between different applications and interfaces. One of CloudDrive’s key features is its ability to mount multiple cloud storage services as local drives, allowing direct access to files without the need to download them in advance. This enables you to use cloud storage as an extension of your local file system, greatly improving convenience and efficiency.

In addition, CloudDrive offers advanced features such as high-speed cloud-to-cloud file transfers, real-time file change notifications, and application-level permission controls—catering to a wide range of cloud storage management needs. For more information, please refer to [the official documentation](https://www.clouddrive2.com/index.html) .

![](https://file-us.ugreennas.com/admin/article/2025-09-16/11cebe5ec44b452b9bd1f0585d458977.webp)

## Deploying CloudDrive2 Using Docker Compose

To quickly deploy CloudDrive2 on your UGREEN NAS, it is recommended to use Project (Docker Compose) for containerized deployment. This method is especially suitable for scenarios where you need to efficiently create and manage multiple containers. The following steps will guide you through deploying CloudDrive2 using Docker Compose. For more details, please refer to [What is Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9) .

### Step 1: Enter the Docker Project Interface

In the UGOS Pro system, open the Docker application and navigate to [Project] > [Create] to launch the project creation wizard.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/563ffc22b64f49e1a72ea10157beb153.webp)

### Step 2: Configure the Docker Compose File

During the project creation process, you will need to provide a Docker Compose configuration file. Paste the following Docker Compose configuration:

```
services:
  clouddrive2:
    image: cloudnas/clouddrive2:latest
    container_name: clouddrive2
    environment:
       - TZ=Asia/Shanghai
       - CLOUDDRIVE_HOME=/Config
    volumes:
      - /volume1/Docker:/Docker:shared
      - ./Config:/Config
    devices:
      - /dev/fuse:/dev/fuse
    restart: always
    pid: "host"
    privileged: true
    network_mode: host
    ports:
      - 19798:19798
```

**Parameter Explanation:**

● `services`: Defines a service named `clouddrive2`.

● `image`: Specifies the image to use — `cloudnas/clouddrive2` with the latest version (`latest`) pulled.

● `container_name`: Names the container `clouddrive2` to make it easier to identify during management or inspection.

● `environment`: Defines environment variables:

* `TZ=Asia/Shanghai`: Sets the container’s time zone to Shanghai. This ensures the time inside the container is synchronized with the local system. You can modify it according to your region (e.g., `America/New_York` or `Europe/London`).
* `CLOUDDRIVE_HOME=/Config`: Specifies the configuration directory inside the container as `/Config`.

● `volumes`: Defines file mounts between the host and the container:

* `/volume1/Docker:/Docker:shared`: Mounts the `/volume1/Docker` folder from the UGREEN NAS to the `/Docker` directory inside the container. Here, you can access the cloud drives and folders mounted locally by clouddrive2. The `shared` option means that file system changes (such as mounting or unmounting) are synchronized between the container and the UGREEN NAS.
* `./Config:/Config`:`./` refers to the current directory where the Docker Compose file is located. This mounts the local `Config` folder to the `/Config` directory inside the container, enabling persistent storage of configuration files.

● `devices`: Uses the `/dev/fuse` device on the UGREEN NAS, allowing the container to perform file system mounting operations (e.g., mounting cloud storage).

● `restart`: Sets the automatic restart policy to `always`, so the container will restart automatically if it crashes or if the host system is rebooted.

● `privileged`: Enables privileged mode, granting the container elevated system permissions.

● `ports`: Maps port 19798 on the UGREEN NAS to port 19798 inside the container, allowing external access to services within the container via the NAS’s 19798 port. If `network_mode: host` is enabled, port mapping can be omitted.

### Step 3: Verify and Create the Container

After completing the configuration, click **"Deploy"** to verify the correctness of the configuration file. Once the verification is successful, the system will launch the clouddrive2 container based on the Docker Compose file. After clicking "Finish", you will see the clouddrive2 container running properly in the Container List.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/7f24c05a6deb4ba9af445bfb7c8d301a.webp)

**Notes:**

● The container's storage space and configured file/folder paths are for reference only — feel free to customize them according to your personal preferences.

● For port settings, it is recommended to keep the container port and local port consistent for web access. If a local port conflict occurs, change it to an unused port. For non-web access, the default automatic setting is usually sufficient.

● Local ports used by different containers must not be the same. Port conflicts will prevent containers from starting.

● The quick-access web links for containers are only accessible in bridge networking mode.

● The image only provides instructions for container setup. For usage details and advanced features, please refer to tutorials available online.

● The image is developed by a third party. For changes in configuration or bug fixes, please refer to official sources from the developer.

● It is recommended to store Docker configuration directories on an SSD to avoid mechanical hard disks from preventing system sleep and impacting performance.

## Accessing and Configuring clouddrive2

1. After a successful deployment, you can access the web interface of clouddrive2 via your browser at `http://<NAS-IP>:port`. Replace `<NAS-IP>` with the actual IP address of your NAS (e.g., `http://192.168.22.153:19798`). The first time you access it, you will need to register and log in.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/fc70c31e228f490180ba146557819a32.webp)

2. After registering and logging in, bind the cloud drive you want to mount locally (Note: free accounts can bind up to 2 cloud drives & mount 1 cloud drive locally). Here, using "Baidu Netdisk" as an example, select it and follow the on-screen instructions to complete the binding process.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/4a85c01c58e84f57ab9f86e87c40cad7.webp)

3. After successfully binding the cloud drive, click the "little TV" icon at the top of the page to add a mount point.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/bc83d9ecaeff4fe48d35d2a86f970d97.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-16/7ed1a62b43f04c27bb7e54fcae7f63ca.webp)

4. After clicking to select, another pop-up window will appear. Choose the `Docker` directory, then click "Select" at the bottom, and finally click "Mount".

![](https://file-us.ugreennas.com/admin/article/2025-09-16/6ec75651848145888b38ef558c5e253a.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-16/7dcd868f25e14b21af9624765ebdb279.webp)

5. Check the mount status by clicking the "little TV" icon in the upper right corner. If there is no error message, the mount was successful.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/4a9565549cc745e98000bc1b3418719d.webp)

6. Go to the File Management on your UGREEN NAS, and you will see the successfully mounted Baidu Netdisk under the docker directory.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/562c2dc1c40c49ab8c91b09d8fa180cf.webp)

7. After the mount is complete, the cloud drive can be used like a local directory. For example, when creating a library in the UGREEN NAS Theater, you can select the Baidu Netdisk path as the media folder.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/01e7ec1d35674634a4f1c3cec58da7da.webp)
