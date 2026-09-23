# [Docker Usage] Deploying CloudDrive2 on UGREEN NAS to Mount 115 Cloud Drive

> **Article ID**: `511`  
> **Category**: `Application Guide > Docker > Docker Gameplay > [Docker Usage] Deploying CloudDrive2 on UGREEN NAS to Mount 115 Cloud Drive`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/511  

---

## Introduction to CloudDrive

CloudDrive is an all-in-one cloud storage management platform that seamlessly integrates multiple cloud storage services through a unified interface. It allows users to easily manage and access all their cloud storage content without the need to constantly switch between different applications. One of CloudDrive’s most notable features is its ability to mount multiple cloud storage services as local drives, enabling direct access to files without requiring pre-downloads, which greatly enhances convenience.

In addition, the platform offers advanced features such as fast cloud-to-cloud file transfer and application permission control, meeting a wide range of user needs. For more details, please refer to [the official documentation](https://www.clouddrive2.com/index.html) .

![](https://file-us.ugreennas.com/admin/article/2025-09-10/a3190708ed344e6cbfd33971798e9209.webp)

## Deploying the Container Using Docker Compose

On the UGOS Pro system, it is recommended to use Project (Docker Compose) for quick container deployment, especially suitable for scenarios where multiple containers need to be managed simultaneously. This method simplifies both the deployment and management of containers. Below are the detailed steps to deploy the clouddrive2 service using Docker Compose.

Click to learn more: [What is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### Access the Docker Project Interface

On the UGOS Pro system, open the Docker application and click [Project] > [Create] to launch the project creation wizard.

### Configure the Docker Compose File

In the project creation wizard, you will need to upload a Docker Compose configuration file. Below is a sample configuration for clouddrive2:

```
services:
  clouddrive2:
    image: cloudnas/clouddrive2:latest # The image and version being used
    container_name: clouddrive2
    environment:
       - TZ=Asia/Shanghai # Specify the time zone
       - CLOUDDRIVE_HOME=/Config  # Set the CloudDrive home directory to /Config inside the container
    volumes:
      - /volume1/CloudNas:/CloudNAS:shared   #  Map /volume1/CloudNas on the NAS to /CloudNAS in the container with "shared" mode enabled
      - ./Config:/Config #Specify the path for saving CloudDrive configuration files
    devices:
      - /dev/fuse:/dev/fuse  # Mount /dev/fuse from the host to the container to support filesystem operations
    restart: always # Set the container restart policy to always
    pid: "host"  # Use the host’s PID namespace to allow the container to access host processes
    privileged: true #  Enable privileged mode to allow the container more system-level access
    network_mode: host # Use host network mode to share the host’s network directly
    ports:
      - 19798:19798  # Map port 19798 of the container to port 19798 of the host
```

### Parameter Description:

**image****:**

Specifies the use of the `cloudnas/clouddrive2` image and pulls the latest version (`latest`).

**container\_name:**

Names the container `clouddrive2` making it easier to manage or identify the container.

**environment:** Defines environment variables

`TZ=Asia/Shanghai`: Sets the container's time zone to Shanghai. This ensures the time inside the container is synchronized with the local time. For example, you can set `Asia/Shanghai` for Asia, or other appropriate zones like `America/New_York` or `Europe/London`.

`CLOUDDRIVE_HOME=/Config`: Specifies `/Config` as the directory inside the container for storing configuration files.

**volumes:** Defines mount paths between the NAS host and the container

`/volume1/CloudNas:/CloudNAS:shared`: Mounts the `/volume1/CloudNas` folder on the UGREEN NAS to the `/CloudNAS` directory in the container. Here, you can view the cloud drives and folders mounted locally by clouddrive2. The `shared` option ensures changes to the file system (such as mount/unmount actions) are synchronized between the container and the NAS.

● Please replace `/volume1/CloudNas` with your actual NAS path for config storage, or use `./CloudNas`. `./`refers to the directory where the Docker Compose file is located.

`./Config:/Config`: Mounts the `Config` folder in the current NAS directory to the `/Config` directory in the container, used for persisting configuration files.

**devices:**

Uses the `/dev/fuse` device from the UGREEN NAS, allowing the container to use filesystem mounting features (e.g., mounting cloud storage).

**restart:**

Restart policy. Set to `always`, meaning the container will automatically restart if it crashes or if the host restarts.

**privileged:**

Enables privileged mode, allowing the container to gain elevated system permissions.

**ports:**

Maps port 19798 on the UGREEN NAS to port 19798 in the container, enabling external access to the container's services via this port on the NAS. If n`network_mode: host` is enabled, this port mapping can be omitted.

**Related Reading**

[How to Correctly Represent Volumes Mount Paths in the Docker Compose Configuration File?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTQ0NywidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0ODcsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

## Deploy the Project

After confirming that the configuration is correct, click [Deploy]. The system will automatically pull the image and start the container. Once deployment is complete, you can access the clouddrive2 homepage via: `http://<NAS_IP>:<port>`

![](https://file-us.ugreennas.com/admin/article/2025-09-10/6285d2d90641499da6d282a5c79f2f95.webp)

## Accessing CloudDrive2

1. After successful deployment, you can access CloudDrive2 via a web browser: `http://<NAS-IP>:<port>`，Replace `<NAS-IP>` with the actual IP address of your NAS (for example: `http://192.168.22.153:19798`). On your first visit, you will need to register and log in to the CloudDrive2 web interface.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/655c27da7eda402b8fcf71dc26d72030.webp)

2. After registration and login, bind the cloud drive you want to mount locally. CloudDrive currently supports Aliyun Drive, Baidu Netdisk, 115 Drive, Tianyi Cloud, 123 Cloud, OneDrive, Google Drive, Thunder Drive, WebDAV, and local folders. (Note: A free account allows binding up to 2 cloud drives & mounting 1 cloud drive locally.) Here we select to mount "**115 Drive**"; after selection, follow the instructions to complete the binding process.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/0bbd61be13f642ed8aeb5ad5a7755bce.webp)

## Mounting 115 Drive

1. Select the option [Add Cloud Drive > 115 Drive]. Here, use the mobile app to scan the QR code and log in to your 115 Drive account. Please note: If you have not registered a 115 Drive account yet, please download the 115 Drive client or visit [the official 115 website](https://115.com/) to complete the account registration first.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/7c9384ed9d7944769bd8e3431e5908b7.webp)

2. After successfully binding the cloud drive, click the "small TV" icon at the top of the page to mount the 115 Drive to the local system.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/6ee94cffd89f43b7a055f3c1257986fd.webp)

3. To add a mount point, click "Select," then in the pop-up window, choose the `cloudNas`directory, click "Confirm" below, and finally click "Mount."

![](https://file-us.ugreennas.com/admin/article/2025-09-10/9306d1d852cf4cf1b6a341cc31c45a9b.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-10/fef216fa578c4d7089578b8501002457.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-10/9b4f0f6b792e4fe0956b41b9e2cf01d6.webp)

4. Check the mount status by clicking the "small TV" icon at the top right. If there are no error messages, the mount was successful.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/c36782227849459cadb21c14fb89abbb.webp)

5. Go to the UGOS Pro system’s [Files] section. You can find the successfully mounted 115 Drive under the `cloudNas` directory.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/ce5f31d284df4436874ce75eac7d031b.webp)

6. After mounting is complete, the 115 Cloud Drive can be used like a local directory. For example, when creating a media library in UGREEN NAS Theater, you can select the 115 Drive path as the media folder.

**Note:** The Theater supports users to customize and add media folders, and will perform recognition scans after adding. Frequent scanning may trigger abnormal monitoring mechanisms by cloud storage providers (such as 115 Drive), which could lead to account restrictions or bans. It is recommended to avoid adding a large number of folders from the same account as media folders.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/f326d80c4e6940f7a4957bf42150571e.webp)

## Notes

Please note that the image used in this tutorial is developed and maintained by a third party, and the tutorial is for reference only. UGREEN does not assume any responsibility for risks caused by improper user operations, third-party software vulnerabilities, or image updates, including but not limited to:

● Third-party images may cause accidental modification or deletion of files in the UGOS Pro system.

● Using insecure images may result in data being uploaded to third-party servers, posing privacy and data leakage risks.

● To ensure system stability and data security, please carefully select third-party images from trusted sources.

**Other Notes:**

1. The file/folder paths inside the container are for reference only. You can create your own paths according to personal preference.

2. The container’s web access port and the local port must be consistent. If there is a conflict, please change to an unused port. Local ports for different containers cannot be the same; port conflicts will cause containers to fail to start.

3. The container’s web interface is only accessible under bridge networking mode.

4. This image only provides deployment instructions. For detailed usage and advanced features, please search online for references.

5. The image is developed by a third party. For configuration changes and bug fixes, please follow the relevant official information.

6. It is recommended to store the Docker configuration directory on an SSD to avoid performance issues caused by mechanical drives.
