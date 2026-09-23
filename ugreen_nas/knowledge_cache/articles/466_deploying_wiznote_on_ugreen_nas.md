# Deploying WizNote on UGREEN NAS

> **Article ID**: `466`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Deploying WizNote on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/466  

---

WizNote is a cross-platform cloud note-taking software that supports operating systems such as Windows, Mac, Linux, Android, and iOS. It allows users to efficiently collect, manage, and share information. By deploying WizNote on UGREEN NAS using Docker, you can set up a secure and convenient personal note server.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250408/20ac2d9c-d83f-4674-a485-1469cea460da.png)

Please note that the images referenced in this tutorial are developed and maintained by third parties and are for reference only. UGREEN NAS is not responsible for any risks caused by user error, third-party software vulnerabilities, or image updates. These risks may include, but are not limited to, the following situations:

* Third-party images may cause files stored on UGREEN NAS to be accidentally modified or deleted.
* Using unsafe images may lead to your data being uploaded to third-party servers, posing privacy and data leakage risks.
* To ensure system stability and data security, it is recommended to carefully choose trusted sources when using third-party images.

## Deploying Containers with Docker Compose

To quickly deploy containers on UGREEN NAS, it is recommended to use Docker Compose for the project. This method is ideal for scenarios where you need to create and manage multiple containers, offering a convenient way to handle containerized management. Below are the detailed steps for deploying WizNote via Docker Compose.

[What is a project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### **Enter the Docker Project Interface**

In the UGREEN NAS UGOS Pro system, open the Docker application, click [Project] > [Create], and start the project creation wizard.

### **Configure the Docker Compose File**

In the project creation wizard, you need to upload the Docker Compose configuration file. Below is an example configuration for WizNote:

```
services:
  wiznote:
    image: wiznote/wizserver    # The image used by the container is wiznote/wizserver
    restart: always             # The container restart policy is set to "always," meaning the container will automatically restart under any circumstances.
    ports:
      - "30802:80" # Map the host NAS's port 30802 to the container's port 80.
    volumes:
      # Mount the directory by mapping the wiz directory from the current directory to the container's /wiz/storage directory.
      - ./wiz:/wiz/storage
    network_mode: bridge         # Set the container's network mode to bridge.
```

### **Detailed Explanation of Parameters**

`image: wiznote/wizserver` specifies that the service will use the `wiznote/wizserver` image for deployment.

`restart: always`This sets the container's restart policy to`always`，meaning that the container will automatically restart regardless of whether it stops due to system reboot or a crash.

`ports:` This configures port mapping. The host machine's (UGREEN NAS) **30802** port is mapped to the container's **80** port. You can access the WizNote service in the container by visiting`http://<NAS_IP>:30802`in your local network.

* `"30802:80"` means that the host's **30802** port is mapped to the container's`80` port, which is the default port for HTTP services.

`volumes:` This configures`volume`to mount the host machine's file system to the container's file system, ensuring data persistence. `./` denotes the directory where the current Docker Compose file is located.

* `./wiz:/wiz/storage`：Maps the `wiz`folder from the current directory to the `/wiz/storage`directory inside the container. The contents of the `wiz` folder on the host machine will be synchronized to the `/wiz/storage`directory inside the container, and WizNote's storage data will be saved in this path.

`network_mode: bridge` Configures the network mode as `bridge`，meaning the container communicates with the outside through Docker's bridge network. The bridge network allows the container to communicate with the host machine and other containers on the same network while maintaining a level of isolation.

### **Deploy the Project**

After confirming the configuration is correct, click [Deploy]. The system will automatically pull the image and start the container. Once the deployment is complete, you can access the WizNote web interface via `http://<NAS_IP>:30802` .

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250408/b59803f6-2634-4f5c-8fc7-d3bddb71f6ca.png)

---

## Accessing WizNote

After successful deployment, open your browser and enter the NAS IP address and port number (e.g.,`http://192.168.66.43:30802`）to access the WizNote login page. If the following page is displayed, it means the container service has not finished loading. Please wait a moment and try refreshing the page again.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250408/de0ac6ae-3e5c-4aec-bd66-7e8a4803d736.png)

After logging in with the default administrator account `admin@wiz.cn`and password `123456`, it is recommended to change the password immediately.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250408/060fb520-e8e7-4fe9-98ca-90fe75e52686.png)

To change your password, click on the user avatar on the left side of the page and select "Account Setting" to modify your password.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250408/12e4e55a-11cb-4b62-adca-b0aa70e345ee.png)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250408/a7acaac8-8f01-4591-8231-9679d88d66ba.png)

The WizNote we set up is the server version. You will also need to download the corresponding client to use it. Click the link at the bottom left to download the client for your operating system. [Download the client.](https://www.wiz.cn/zh-cn/download.html)  
![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250408/211b3a0a-4f1e-4c04-a7e6-4b391c640ab1.png)

Download the client that suits your device. Here, we will use the Windows version (restructured) as an example.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250408/ff98ee81-1636-4443-8e4c-57ca8396358f.png)

After installing the client, choose to switch to the private server.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250408/66111c42-f5f4-4b17-97bf-751b0a8fb201.png)

Enter your account name, password, and the IP address of the WizNote server you just set up (e.g., `192.168.66.43:30802`），then log in and sync your notes.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250408/85533fd5-9061-49a8-8583-9fc3e920d7b6.png)

## Notes

* The container's storage space and the configured file/folder paths are for reference only; you can create them according to your preferences.
* For port configuration, it's recommended to keep the container's web access port and the local port consistent. If there's a conflict with the local port, change it to an unused one.
* The local ports of different containers must not be the same. Port conflicts will prevent the container from starting.
* The web link for quick access to the container is only available in bridge mode.
* The image only provides a tutorial for setting up the container. For usage methods and advanced features, please refer to online tutorials.
* The image is developed by a third party. For changes in configuration or bug fixes, please follow the relevant official information.
* It’s recommended to store the Docker configuration directory on an SSD to avoid issues with mechanical hard drives not entering sleep mode, which may affect system performance.
