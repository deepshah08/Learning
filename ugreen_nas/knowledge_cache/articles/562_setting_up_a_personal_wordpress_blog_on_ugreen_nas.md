# Setting Up a Personal WordPress Blog on UGREEN NAS

> **Article ID**: `562`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Setting Up a Personal WordPress Blog on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/562  

---

## **App Introduction**

WordPress is a powerful, free, open-source content management system (CMS) widely used to create various types of websites, ranging from personal blogs to large enterprise sites. Its popularity mainly stems from its ease of use, high flexibility, and extensive community support. With numerous customizable themes and plugins, users can achieve personalized web design and functionality without requiring in-depth programming knowledge.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250516/ee5c325c-4507-4515-92cf-c0c925e430e2.png)

Before setting up WordPress, make sure that the database service has been deployed and properly configured. WordPress relies on a database to store content and settings, and here we recommend using MariaDB as the database management system.

## **Docker Compose Configuration and Deployment**

On the UGOS Pro system, it is recommended to use [Docker Compose](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9) projects for quick container deployment. This approach is ideal for scenarios that require managing multiple containers at once, as it simplifies both deployment and management tasks. Below are the detailed steps to deploy wordpress using Docker Compose:

1. Open the Docker application and click on [Project] > [Create] to launch the project creation wizard.
2. In the wizard, enter the following Docker Compose configuration. These settings are for reference only and can be adjusted according to your needs.

```
services:
  wordpress:
    container_name: wordpress
    image: wordpress:latest
    restart: always
    volumes:
      - ./wordpress/data:/var/www/html
    environment:
      WORDPRESS_DB_HOST: 172.17.70.69:33308
      WORDPRESS_DB_NAME: wordpress
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: 123456
    ports:
      - "38010:80"
    network_mode: bridge

  wordpressdb:
    image: mariadb:10.6
    restart: always
    volumes:
      - ./mariadb/data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: 123456
    ports:
      - "33308:3306"  # Map port 3306 in the container to port 33308 on the host.
    network_mode: bridge
```

3. After filling in the configuration file, click “Deploy” and the system will automatically pull the image and start the container.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250516/70d4b8be-ea09-4ef0-ad30-ca54479808ca.png)

4. After the deployment is complete, access the container through your browser by entering `http://NAS_IP:38010` in the address bar. For example, if the NAS IP is `172.17.70.69`, enter `http://172.17.70.69:38010` in the browser to access it.

You can find [Network Settings] in the Control Panel, click "Network Connection" to view the IP address of the NAS device.

### 

### **Docker Compose Configuration Description**

|  |  |  |
| --- | --- | --- |
| Configuration | Value | Description |
| `container_name` | `wordpress` | Specifies the container name for easier management and identification. |
| `image` | `wordpress:latest` | Uses the official latest WordPress image. |
| `restart` | `always` | Automatically restarts the container on failure to ensure high availability. |
| `volumes` | `./wordpress/data:/var/www/html` | Mounts a directory from the host to the WordPress installation directory in the container for data persistence. |
| `environment.WORDPRESS_DB_HOST` | `172.17.70.69:33308` | WordPress database connection address (IP:Port), should point to the `mariadb` container. Note: Ensure the IP and port are reachable. |
| `environment.WORDPRESS_DB_NAME` | `wordpress` | Specifies the database name used by WordPress. |
| `environment.WORDPRESS_DB_USER` | `wordpress` | Database username, must match the one set in the database service. |
| `environment.WORDPRESS_DB_PASSWORD` | `123456` | Password for the database user, must match the one set in the database service. |
| `ports` | `"38010:80"` | Maps port 80 inside the container to port 38010 on the host, allowing access to WordPress via browser. |
| `network_mode` | `bridge` | Uses Docker's default bridge network mode. Services cannot communicate directly via service names. |

|  |  |  |
| --- | --- | --- |
| Configuration | Value | Description |
| `image` | `mariadb:10.6` | Uses the official MariaDB 10.6 image, compatible with WordPress. |
| `restart` | `always` | Automatically restarts the container after unexpected exit to ensure continuous database operation. |
| `volumes` | `./mariadb/data:/var/lib/mysql` | Mounts the database data directory to the host for data persistence. |
| `environment.MYSQL_ROOT_PASSWORD` | `rootpassword` | Sets the root administrator password for MariaDB. |
| `environment.MYSQL_DATABASE` | `wordpress` | Automatically creates a database for WordPress. |
| `environment.MYSQL_USER` | `wordpress` | Automatically creates a database user. |
| `environment.MYSQL_PASSWORD` | `123456` | Password for the database user. Must match the credentials in the WordPress configuration. |
| `ports` | `"33308:3306"` | Maps port 3306 inside the container (database port) to port 33308 on the host for WordPress to connect. |
| `network_mode` | `bridge` | Uses the default bridge network mode. WordPress cannot access this container via the service name `wordpressdb`; it must connect using the IP:port. |

## **Access the WordPress Interface**

1. Open a browser and enter `http://<NAS_IP>:38010` to access the WordPress admin interface.
2. On the WordPress installation page, select English as the language and click "Continue".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250516/5c07dfc3-301d-4d6c-8ecf-8cade48ad7ec.gif)

3. Set the site title, admin username, password, and other information, then proceed with the installation process.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250516/b1c5ea99-17fb-4242-a426-e283db372d6d.png)

4. After the installation is complete, log in to the WordPress dashboard using the username and password you created.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250516/1df64adf-8bee-4056-8328-e8495f6746d3.png)

5. After logging in successfully, you can manage the WordPress dashboard on this page.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250516/0dd33f7a-7e23-4edf-ab44-cadc2dfc1c41.png)

### **Changing and Uploading Blog Themes**

If you are not satisfied with the default theme, you can change the theme as follows:

1. In the WordPress dashboard, click [Appearance] > [Themes] > [Add New Theme].
2. Browse and select the theme you like, then click [Install] and activate it.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250516/79d3ccab-2129-43c6-b89c-7d353e7f8bb6.png)

### **Removing the Upload Media File Size Limit**

By default, WordPress limits upload file size to 2MB, but you may need to upload larger files. You can resolve this by installing the “Big File Uploads” plugin.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250516/d275e17d-5d42-45bc-9b9f-3260e202eaeb.png)

1. In the WordPress admin dashboard, go to the Plugins installation page and search for the `Big File Uploads` plugin to install it. Alternatively, you can download it from the official directory at <https://wordpress.org/plugins/tuxedo-big-file-uploads/>and upload it manually for installation.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250516/7a03b135-e84c-47d6-ab1a-6473843f0496.png)

2. After installation, activate the plugin and click on [Settings] to configure the maximum upload file size.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250516/2a52dec4-e381-4e63-9ff0-ab1b3197b117.png)

3. In [Settings], you can set the maximum upload size to the desired value, for example, 200MB, and save the settings.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250516/67a64480-9e9c-4c8b-90a4-83976d34d6fa.png)

4. Returning to the media upload page, you can see that the file size limit has been changed to 200MB.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250516/d73df9d5-444f-4648-89e7-f436c9f60629.png)

## **Frequently Asked Questions**

### **Q1: How to get the real path of a NAS folder and mount it to a Docker container**

When using Docker, you may need to mount a folder from your NAS to a Docker container so that the container can access data stored on the NAS. You can refer to [Get the real path of the NAS folder and mount it to the Docker container](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTkzMCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo2MTEsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D) to help you complete this operation.

## **Notes**

1. The images mentioned in this tutorial are developed and maintained by third parties. The tutorial is for reference only. UGREEN does not assume any risks caused by improper operations, software vulnerabilities, or image updates, such as file anomalies or data leakage. Please choose trusted images to ensure system and data security.
2. Container file paths can be set according to personal preference. When accessing via a web interface, the container port and the host port must be consistent, and local ports for different containers must not conflict.
3. Container web links are only accessible under the bridge network mode.
4. The images provide only deployment tutorials. For specific usage and advanced features, please search online. For configuration changes and bug fixes, please follow official announcements.
5. It is recommended to store Docker configuration directories on an SSD to avoid performance impact caused by mechanical hard disks.
