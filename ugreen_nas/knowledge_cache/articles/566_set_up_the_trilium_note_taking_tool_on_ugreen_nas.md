# Set up the Trilium note-taking tool on UGREEN NAS

> **Article ID**: `566`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Set up the Trilium note-taking tool on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/566  

---

Trilium is a highly flexible note-taking tool that supports bidirectional linking, unlimited nesting, note maps, and more. It also allows for complex logic through custom JavaScript. By deploying the container with Docker Compose, Trilium can be quickly installed on UGREEN NAS for easy management.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250411/b9ec0222-7d3f-4c47-9265-728f41a476af.png)

Please note that the images referenced in this tutorial are developed and maintained by third parties, and are for reference only. UGREEN NAS is not responsible for any risks caused by improper user actions, third-party software vulnerabilities, or image updates. These risks may include, but are not limited to, the following:

* Third-party images may cause files stored on UGREEN NAS to be accidentally modified or deleted.
* Using insecure images may result in your data being uploaded to third-party servers, posing risks to privacy and data security.
* To ensure system stability and data safety, it is recommended to carefully select trustworthy sources when using third-party images.

## **Deploy Containers with Docker Compose**

To quickly deploy containers on UGREEN NAS, it is recommended to use the project Docker Compose. This method is suitable for scenarios that require the creation and management of multiple containers, offering a convenient way to manage containers. Below are the detailed steps for deploying the Trilium note-taking tool via Docker Compose. [What is project（Docker Compose）？](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### **Access the Docker Project Interface**

In the UGREEN NAS UGOS Pro system, open the Docker application, then click [Project] > [Create] to launch the project creation wizard.

### **Configure the Docker Compose File**

In the project creation wizard, you will need to upload the Docker Compose configuration file. Below is an example configuration for the Trilium note-taking tool:

```
services:
  trilium-cn:
    image: nriver/trilium-cn    # Container image version
    restart: always             # Container restart policy
    ports:
      - "30801:8080"
    volumes:
      # Mount directory, map the trilium-data directory from the same folder to the container
      - ./trilium-data:/root/trilium-data
    environment:
      # Environment variable indicating the storage path of note data inside the container
      - TRILIUM_DATA_DIR=/root/trilium-data
```

### **Detailed Explanation of Parameters**

`volumes`

By using the `volumes` directive, the NAS host and the container share storage. `./` refers to the directory where the current Docker Compose file is located，and maps the `trilium-data` folder in that directory to the `/root/trilium-data` directory in the container. The container's configuration files and database will be stored in this directory.

`image`

Use the `nriver/trilium-cn` image to create the container.

`restart`

The restart policy is set to  `always`, meaning that the container will automatically restart regardless of whether it exits abnormally or the system is rebooted.

`ports`

Map port 30801 on the host to port 8080 in the container, allowing external access to the container's services through port 30801 on the host.

`environment`

Set the environment variable `TRILIUM_DATA_DIR` to specify the storage path for container data as `/root/trilium-data`.

### **Deploy the Project**

Once the configuration is confirmed, click [Deploy]. The system will automatically pull the image and start the container. After deployment is complete, you can access the Trilium note-taking tool's web interface at  `http://<NAS_IP>:30801`.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250411/075c8d35-a8b2-4f23-92c3-97a7d025ef5a.png)

## **Access Trilium Notes**

1. After a successful deployment, open your browser and enter the NAS IP address and port number (e.g., `http://192.168.66.43:30801`) to access the Trilium notes web interface.
2. For first-time use, select 'I’m a new user, I want to create a new Trilium document to save my notes' to create a new Trilium document. Then, click 'Next.'"

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250411/fed80a13-1728-4776-bb5f-39fb5916ebf0.webp)

3. After setting and confirming your password, enter the Trilium notes interface.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250411/e052005e-7b6e-4ce5-a6c8-ffb180749a71.webp)

4. Enter the password and click 'Login' to access the Trilium notes web interface.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250411/2850fba3-2990-4a0a-9303-b448edf300b0.webp)

5. You can learn how to use Trilium from the example notes on the homepage.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250411/2555f249-0b20-4470-bf8b-7cbf4a8c0a71.png)

## **Notes**

* **Note Database Path:** All data is stored in the `trilium-data` folder.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250411/f57dd001-8ee1-4642-9349-82d869cab9ef.png)

* **Reverse Proxy Issues:** If you encounter issues accessing the web interface due to reverse proxy, it is recommended to refer to [the official reverse proxy documentation](https://github.com/zadam/trilium/wiki/Server-installation) for adjustments.
* The container's storage space and the configured file/folder paths are for reference only. You can create them according to your personal preferences.
* Port configuration: It is recommended to keep the container port for web access and the local port consistent. If there is a port conflict on the local machine, change it to an unused port.
* Local ports for containers cannot be the same. Port conflicts will prevent the containers from starting.
* The quick access web links for containers are only accessible in bridge mode.
* The image only provides instructions for setting up the container. For usage and advanced features, please search for online tutorials for reference.
* The image is developed by a third party. For specific configuration changes and bug fixes, please refer to the official information.
* It is recommended to store the Docker configuration directory on an SSD to avoid mechanical hard disks failing to enter sleep mode, which could affect system performance.
* Please note that the images in this tutorial are developed and maintained by a third party and are for reference only. UGREEN NAS is not responsible for any risks caused by improper operations, third-party software vulnerabilities, or image updates. These risks include, but are not limited to, the following: modification or deletion of files stored on UGREEN NAS, uploading your data to third-party servers, security risks caused by attacks on the UGREEN NAS system, or system crashes due to container overload.
