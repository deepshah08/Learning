# Deploy the Alist Cloud Drive Mount Service on UGREEN NAS

> **Article ID**: `486`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Deploy the Alist Cloud Drive Mount Service on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/486  

---

Alist is an open-source file listing program that supports various storage services (such as local disks and cloud drives) as backend storage. It offers a clean and user-friendly frontend interface for managing and browsing files across these storage locations. Alist features easy deployment, flexible configuration, and broad support for third-party storage services.

Deploying Alist on UGREEN NAS allows you to manage both local files on the NAS and cloud storage services through a unified interface. To ensure a smooth deployment process, please read the following instructions carefully.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/0c2fba2427534c52b32c3315f7f3f099.webp)

Please note that the image used in this tutorial is developed and maintained by a third party and is provided for reference only. UGREEN NAS assumes no responsibility for any risks arising from improper user operations, third-party software vulnerabilities, or image updates. These risks may include but are not limited to the following situations:

● Third-party images may unintentionally modify or delete files stored on your UGREEN NAS.

● Using insecure images may result in your data being uploaded to third-party servers, posing risks of privacy breaches and data leaks.

● To ensure system stability and data security, it is recommended that you exercise caution and choose trusted sources when using third-party images.

## Deploying the Container Using Docker Compose

To quickly deploy a container on UGREEN NAS, it is recommended to use the Project (Docker Compose) feature. This method is ideal for scenarios where multiple containers need to be created and managed, offering a convenient approach to containerized management. Below are the detailed steps to deploy Alist using Docker Compose. [What Is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### Access the Docker Project Interface

Open the Docker application on your UGREEN NAS, go to [Project] > [Create], and launch the project creation wizard.

### Configure the Docker Compose File

During the project setup, you will need to upload a Docker Compose configuration file. Below is a sample configuration for deploying Alist:

```
services:
    alist:
        image: xhofe/alist:latest # The latest image used by the container
    container_name: alist
        container_name: alist 
        volumes:
            - ./alist:/opt/alist/data #Path to store container configuration files
            - ./downloads:/downloads  #Download directory
        ports:
            - 15244:5244 #Map port 15244 on the NAS to port 5244 in the container
        environment:
            - PUID=0
            - PGID=0
            - UMASK=022
        restart: always # Container restart policy: "always" means the container will restart automatically under any circumstance
```

### Detailed Explanation of Parameters

**image：**Specifies the image used by the container. In this case, `xhofe/alist:latest` refers to the latest version of AList.

**volumes：**Defines the data volumes to bind directories on the NAS to paths inside the container.

● `./alist:/opt/alist/data`：Maps the `alist` folder in the current directory on the NAS to `/opt/alist/data` inside the container. This is used to store AList's configuration files and data.

● `./downloads:/downloads`：Maps the `downloads` folder on the NAS to `/downloads` inside the container, serving as the download directory.

**ports：**Configures port mapping between the NAS and the container.

● `15244:5244`：Maps port 15244 on the NAS to port 5244 inside the container. You can access the service in the container by visiting `http://<NAS_IP>:15244`.

#### environment：Environment variables.

● **PUID：**NAS user ID. The default is 0 (root user).

● **PGID：**NAS user group ID. The default is 0 (root group).

**restart：**Sets the container's restart policy.

**always：**The container will automatically restart regardless of the cause—whether it's a crash or a system reboot—ensuring stable and continuous service operation.

### Deploy the Project

After confirming that the configuration is correct, click [Deploy]. The system will automatically pull the image and start the container. Once the deployment is complete, you can access the Alist web interface by entering the NAS IP address and port number in your browser.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/c7a8dc61d3ea4e7b91c17dd1030bd4a4.webp)

## Access the Alist Interface

1. After a successful deployment, open your browser and enter the NAS IP address and port number to access the Alist interface. Replace the NAS IP with your actual NAS IP address. For example: `http://192.168.66.43:15244`

![](https://file-us.ugreennas.com/admin/article/2025-09-10/5f3714254fbb4f868e2293dd61f8c1a7.webp)

2. The default username is admin, and the login password needs to be retrieved from the container logs. Go to the [Container] page in the Docker app, find the container you just created, and open [Console] > [Logs] to view the password.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/87c637427a524487a05a17651aaafb9b.webp)

3. After logging in, click "Manage" to enter the management interface.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/b53e8de067fe4929958070432c1bebd4.webp)

4. Click on Profile to change your account password. After clicking "Save," the changes will take effect and you will need to log in again.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/d0e4e9ba466140bf9f3d5dbe7bcf72f9.webp)

5. Click on [Storages] > [Add] to mount a cloud drive.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/041985d682d148d9b9e9b14de024bd1c.webp)

6. Click on [documentation] to access Alist's help and documentation page.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/eb154f111e0e4110a47501eceffeecc2.webp)

7. On the documentation page, you can change the text to English, then select Storage on the left to view instructions for mounting different cloud drives.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/87ca64a09f0e484197609e0634c423da.webp)

## Notes

1. Ensure the firewall allows external access to port 15244 opened on the NAS.

2. The container's volume and configured file/folder paths are for reference only—you can create them according to your personal preferences.

3. For port configuration, it is recommended to keep the container's web access port and the local port consistent. If the local port conflicts, change it to an unused port.

4. Local ports between containers cannot be the same; port conflicts will prevent containers from starting.

5. The quick access web links for containers are only accessible when using bridge networking mode.

6. The image provides only container deployment tutorials; usage methods and advanced features should be searched for in online tutorials.

7. The image is developed by a third party; for specific configuration changes and bug fixes, please follow the relevant official information.

8. It is recommended to store the Docker configuration directory on an SSD to avoid mechanical hard disks failing to enter sleep mode, which can affect system performance.

That's the basic process for deploying Alist on UGREEN NAS. If you encounter any specific issues or want to explore more advanced configuration options, you can refer to the official Alist project documentation or visit the community forums for assistance.
