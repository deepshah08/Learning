# Deploy Personal Navigation Page Sun-panel on the UGREEN NAS

> **Article ID**: `472`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Deploy Personal Navigation Page Sun-panel on the UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/472  

---

## Introduction to Sun-panel

Sun-panel is a lightweight and minimalist personal navigation program, specifically designed for NAS users to collect and manage project bookmarks efficiently. By leveraging UGREEN NAS, users can simplify bookmark management and access the navigation page through an independent system, ensuring privacy protection. Additionally, Sun-panel operates independently of browsers, eliminating concerns about potential privacy breaches.

![](https://file-us.ugreennas.com/admin/article/2025-09-15/98bbdcdd2db340d5a5435470695f08bc.webp)

Note: The images mentioned in this tutorial are developed and maintained by third parties and are provided for reference only. UGREEN NAS does not assume responsibility for any risks arising from improper user operations, third-party software vulnerabilities, or image updates. These risks may include, but are not limited to, the following:

● Third-party images may inadvertently modify or delete files stored on your UGREEN NAS.

● Using insecure images may result in your data being uploaded to third-party servers, posing privacy and data leakage risks.

● To ensure system stability and data security, it is recommended to exercise caution and select trusted sources when using third-party images.

## Deploy the Container via Docker Compose

To quickly deploy containers on UGREEN NAS, the recommended approach is to use Docker Compose. This method is ideal for scenarios requiring the creation and management of multiple containers, offering a convenient way to handle containerized applications. Below are the detailed steps to deploy Sun-panel using Docker Compose.

Click to learn more: [What is Docker Compose?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### Access the Docker Project Interface

In the UGOS Pro system on your UGREEN NAS, open the Docker application. Click [Project] > [Create] to launch the project creation wizard.

### Configure the Docker Compose file

During the project creation process, you will need to upload a Docker Compose configuration file. Below is a sample configuration file for deploying Sun-panel:

```
services:  
    sun-panel: 
        image: hslr/sun-panel:latest # The image and version of the container to be used
        container_name: sun-panel # Container name
        volumes: # Storage space mount, mounts the host NAS directory to a specific path in the container to ensure data persistence
            - './sun-panel/database:/app/database' # Path where the database file is stored
            - './sun-panel/uploads:/app/uploads' # Path where uploaded files are stored
            - './sun-panel/conf:/app/conf'  #Application configuration file
        ports: # Configure port mapping to map the container port to the host NAS port
            - '3002:3002'
        restart: always  # Restart policy for the container, automatically restart when the container stops or crashes
```

**Parameter explanation:**

● **image**: specifies the image and image version to be used by the container.`hslr/sun-panel:latest` indicates the use of the latest version of `sun-panel`.

● **container\_name**: a custom container name for easy identification and management of specific container instances.

● **volumes**: defines the storage space for persistent storage:

● `./sun-panel/database:/app/database` ：`./`indicates the directory where the current Docker Compose file is located. It maps the `sun-panel/database`directory on the host to the `/app/database`directory inside the container, which is used to store database files.

● `./sun-panel/uploads:/app/uploads`：maps the `sun-panel/uploads`directory on the host to the `/app/uploads`directory inside the container, which is used to save uploaded files.

● `./sun-panel/conf:/app/conf`：maps the `sun-panel/conf` directory on the host to the `/app/conf` directory inside the container, which is used to store the application configuration file.

● **ports**: configures the port mapping between the host NAS and the container. Here, the container's port 3002 is mapped to the host NAS's port 3002, so that the service can be accessed externally through the host port.

● **restart**: Set the container restart policy to automatically restart the container when it fails, ensuring high availability of the service.

### Deploy Project

After confirming the configuration, click [Deploy]. The system will automatically pull the image and start the container. Once the deployment is complete, you can access the Sun-panel web interface at `http://<NAS_IP>:3002`.

![](https://file-us.ugreennas.com/admin/article/2025-09-15/1b3e79d6b2e64040a4326982c7517274.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-15/36f95a0dca814530831d735df108fbd9.webp)

## Access and use sun-panel

1. Access the sun-panel homepage at`http://<NAS_IP>:3002`. For the first login, you need to log in with the default account and password. The default account is`admin@sun.cc`and the password is`12345678`. Enter the account and password to log in.

![](https://file-us.ugreennas.com/admin/article/2025-09-15/5bd99b5a07c649779b2d8fb545779bb4.webp)

2. After logging in, it is recommended that you create a new account password and then switch to logging in with the new account password (Note: Data is not shared between accounts).

![](https://file-us.ugreennas.com/admin/article/2025-09-15/9734a5901d1d402a92ab9d726d5affc7.webp)

3. On the homepage, click "Add", and fill in the project settings as needed, including the project title (e.g., emby, s-pdf), icon, internal address, etc. You can also organize bookmarks into groups (e.g., Movies, Study Materials). Once the setup is complete, click "Save" to display the project on the homepage.

**Please note:**

● The recommended method for uploading icons is to upload them locally. Online icon loading may be affected by the network and result in a loading failure.

● The icon address supports the addition of both Internet and intranet addresses, and you can switch between access methods with a single click. In addition, you can click the switch link button on the homepage or right-click the icon to select the access method.

![](https://file-us.ugreennas.com/admin/article/2025-09-15/d07a2ff0de804315affb8c9054d26fae.webp)

This article only introduces some of the functions of sun-panel, and you can explore more ways to use it. If you have many docker projects on your UGREEN NAS, you can deploy the sun-panel navigation page to organise the projects on the NAS for quick access and management.

## Notes

● The storage space of the container, the configured file/folder path is for reference only, you can create it according to your personal habits.

● For port configuration, it is recommended that the container port for web access and the local port be the same. If the local port conflicts, change it to an unused port.

● The local ports between containers cannot be the same. Port conflicts will prevent the container from starting.

● The web links for quick access to containers are only accessible in bridge mode.

● The images only provide tutorials on how to set up containers. For information on how to use them and in-depth gameplay, please search online for tutorials.

● The images are developed by third parties, so please pay attention to relevant official information for specific configuration changes and bug fixes.

● It is recommended that the Docker configuration directory be stored on the SSD hard disk to avoid the mechanical hard disk from failing to enter sleep mode, which in turn affects system performance.
