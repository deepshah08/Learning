# Setting Up the Kavita Comic Management Tool on UGREEN NAS

> **Article ID**: `547`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Setting Up the Kavita Comic Management Tool on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/547  

---

## **App Introduction**

Kavita is a fast, feature-rich, cross-platform reading server that offers a one-stop solution for managing comics, books, and novels, tailored for personal and household use.   
With Kavita, you can not only efficiently manage your personal collection, but also easily share it with family and friends. It supports a wide range of file formats, including CBZ, CBR, and PDF, and offers the following key features:

**User-Friendly Interface:** Simple and intuitive operation.

**Feature-Rich:** Supports multi-user environments and highly customizable settings.

**Cross-Platform:** Well-suited for both personal and home users.

Official Installation Guide: [Kavita Wiki](https://wiki.kavitareader.com/installation/docker/)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250520/97375011-581f-4b70-9011-30eb9cb63ef4.webp)

## **Deploying the Container Using Docker Compose**

On the UGOS Pro system, it is recommended to use the **Project (Docker Compose)** feature to quickly deploy containers. This method is ideal for scenarios where multiple containers need to be managed simultaneously, simplifying both deployment and management. Below are the detailed steps for deploying **Kavita** using Docker Compose.

Click to learn more: [What is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### **Access the Docker Project Interface**

On the UGOS Pro system, open the Docker app, click on [Project] > [Create] to launch the project creation wizard.

### **Configure the Docker Compose File**

In the project creation wizard, upload the following Docker Compose configuration file for Kavita:

```
services:
    kavita:
        image: jvmilazz0/kavita:latest  # Image name
        container_name: kavita
        restart: always # Restart policy
        volumes:
            - ./manga:/manga            # Path for storing comics (customizable)
            - ./books:/books            # Path for storing e-books (customizable)
            - ./data:/kavita/config     #  Stores configuration files and database
        environment:
            - TZ=Asia/Shanghai # Container time zone
        ports:
            - "15000:5000" # Web service access port
```

### **Parameter Explanation**

**image：**Specifies the Docker image (`latest` indicates the latest version).

**restart：**Defines the container's restart policy. `always` means the container will automatically restart if it stops.

**volumes：**Maps local NAS folders to paths inside the container.

`./manga:/manga`: Mounts the NAS's comics folder to the `/manga` path inside the container. The path before the colon refers to the directory on your NAS and can be customized. For example, you can change it to your actual manga storage path, such as `/volume1/manga`.

`./books:/books`: Mounts the NAS e-book folder to the `/books` path inside the container. The path before the colon refers to the storage location on your NAS and can be modified as needed — for example, you can replace it with your actual manga storage path on the NAS, such as `/volume1/books`.

`./data:/kavita/config`: Specifies the path where Kavita stores its configuration files and database.

Note:

* `./` refers to the directory where the Docker Compose file is located.
* The path before the colon is the local path on the NAS, and the path after the colon is the path inside the container.

**Related Reading**

[[FAQ] How to correctly represent volumes mount paths in the Docker Compose configuration file?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTQ0NywidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0ODcsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

**environment：**

`TZ=Asia/Shanghai`：Sets the container’s time zone to Shanghai, China (`Asia/Shanghai`). You can modify this based on your region — for example, set it to a U.S. time zone (`America/New_York`) or a European time zone (`Europe/London`).

**ports****：**

`15000:5000`：Maps port **15000** on the NAS to port **5000** inside the container. If a port conflict occurs, you can modify the NAS-side port (the number before the colon).

### **Deploy the Project**

After uploading the configuration file, click [Deploy]. The system will automatically pull the image and start the container.

Once the deployment is complete, open your browser and visit the following address to access the Kavita interface:

```
http://<NAS_IP>:15000
```

Please replace `<NAS_IP>` with the actual IP address of your NAS. For example:

`http://192.168.22.153:15000`

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250520/92f29745-8f84-43f3-8d63-995947dda202.png)

## **User Guide**

After the deployment is complete, open your browser and visit `http://<NAS_IP>:15000` to access the login page. Follow the on-screen instructions to complete the registration and initial setup.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250520/395a018a-3653-488a-8be6-405191fe9a7a.webp)

### **Set Language to English**

1. Click the [Settings] button in the top-right corner.
2. On the [Preferences] page, locate the "Locale" option.
3. Select English. The interface will switch to English automatically.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250520/ba847cb9-55a3-48d1-a43b-47f037c17f83.webp)

### **Add a Library**

1. In the left sidebar of the settings interface, click [Libraries] > [Add Library].

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250520/0402b66a-8d32-431f-b620-338e81e07097.png)

2. In the pop-up window, select the type (e.g., Manga), enter a custom name for the library, then click "Next" to continue.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250520/5c507f66-b543-4d82-a26b-5ab0b1644c77.png)

3. Select the mount path (e.g., `/manga`), click "Share" to add it. After adding, click "Next" to continue.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250520/07388a5e-5f58-4640-8cc9-3459fef47457.png)

4. (Optional) Upload a cover image, then click "Next" to continue.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250520/d9ee8642-0605-4224-acbe-a7732c12ab2a.png)

5. Keep the Advanced Settings as default, then click [Save]. Kavita will scan and add eligible files to the library.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250520/9077ae2d-19e8-4e1c-abf0-e627ee6503fd.png)

## **File Scraping and Naming Rules**

To better organize and scrape your resources, it’s recommended to use the suggested naming format:`Title vNumber.cbz`；

For more naming conventions, please refer to the [Kavita Official Naming Guide](https://wiki.kavitareader.com/guides/metadata/comics/).

### **Example Directory Structure:**

mangas is the **main folder** for storing comics. superman is a **subfolder** that contains comic files. superman.cbr is a **single comic file**. If the same comic has multiple volumes, you can name them using the following format:

* **superman -v01.cbr**
* **superman -v02.cbr**
* And so on.

```
mangas/ # This is the main folder for comics.
└── superman/ # This is a subfolder containing comic files.
    ├── superman -v01.cbr #  Comic file
    ├── superman -v02.cbr
    └── superman -v03.cbz
```

### **Version Number Rules**

Version numbers can follow various formats such as:

* `v01`
* `Vol. 1`
* `Volume 2`
* `Volume 1`
* `Volume 3`

### **Supported File Formats**

Kavita supports multiple formats, including:

* `.cbr`
* `.cbz`

## **Notes**

Please note that the image used in this tutorial is developed and maintained by a third party, and the tutorial is for reference only. UGREEN does not assume any responsibility for risks caused by improper user operations, third-party software vulnerabilities, or image updates, including but not limited to:

ꔷ Third-party images may cause accidental modification or deletion of files in the UGOS Pro system.

ꔷ Using insecure images may lead to data being uploaded to third-party servers, posing privacy and data leakage risks.

ꔷ To ensure system stability and data security, please carefully choose third-party images from trusted sources.

Other notes:

1. The file/folder paths for containers are for reference only. You may customize them according to your personal preferences.

2. The container’s web-access port and the local port should remain consistent. If there is a conflict, switch to an unused port. Local ports must be unique between containers—port conflicts will prevent containers from starting.

3. The container’s web link is accessible only in bridge network mode.

4.This image is provided solely for deployment guidance. For specific usage and advanced features, please refer to online resources.

5. Since the image is third-party developed, stay updated on configuration changes and bug fixes by following the relevant official channels.

6.It is recommended to store Docker configuration files on an SSD to avoid performance issues caused by mechanical hard disks.
