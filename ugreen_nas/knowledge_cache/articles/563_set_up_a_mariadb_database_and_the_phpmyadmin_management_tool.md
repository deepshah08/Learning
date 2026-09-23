# Set up a MariaDB database and the phpMyAdmin management tool on UGREEN NAS

> **Article ID**: `563`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Set up a MariaDB database and the phpMyAdmin management tool on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/563  

---

## **Introduction to MariaDB**

MariaDB is an open-source relational database management system created by Michael "Monty" Widenius, one of the original developers of MySQL, and his team. It is designed to be a fully compatible replacement for MySQL, while enhancing performance and extending functionality. MariaDB supports various storage engines and offers high scalability and reliability, making it suitable for everything from standalone applications to complex distributed systems. Its design ensures seamless migration from existing MySQL databases, allowing users to switch easily and benefit from improved performance.

## **Deploying Containers Using Docker Compose**

On the UGOS Pro system, it is recommended to use Project (Docker Compose) for quick container deployment, especially suitable for scenarios that require managing multiple containers simultaneously. This method simplifies both the deployment and management of containers. Below are the detailed steps to deploy MariaDB using Docker Compose.

Click to learn more: [*What is a Project (Docker Compose)?*](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### **Access the Docker Project Interface**

In the UGOS Pro system, open the Docker app and click [Project] > [Create] to launch the project creation wizard.

### **Configure the Docker Compose File**

In the project creation wizard, you need to upload a Docker Compose configuration file. Below is an example configuration for MariaDB:

```
services:
  mariadb:
    image: mariadb:latest  # Use the official MariaDB image
    container_name: mariadb  # Name the container "mariadb"
    restart: always  # Always restart the container to ensure high availability
    environment:  # Set environment variables to configure the database
      MYSQL_ROOT_PASSWORD: 123456  # Set the password for the root user
      MYSQL_DATABASE: mydatabase  # Create an initial database named "mydatabase"
    volumes:  # Define volume mappings for data persistence
      - ./data:/var/lib/mysql  # Mount a directory from the host to the container's MySQL data directory
    ports:
      - "33306:3306"  # Map port 3306 in the container to port 33306 on the host
    network_mode: bridge   # Use bridge network mode
    
  phpmyadmin:  
    container_name: phpmyadmin  # Name the container "phpmyadmin"
    image: phpmyadmin/phpmyadmin:latest  # Use the latest official phpMyAdmin image
    ports:
      - "39085:80"  # Map port 80 in the container to port 39085 on the host for accessing the phpMyAdmin UI
    restart: always  # Always restart the container
    environment:  # Environment variables
      PMA_ARBITRARY: 1 # Allow manual input of MySQL server IP address
    depends_on:  # Define dependency to ensure MariaDB starts first
      - mariadb
    network_mode: bridge   # Use bridge network mode
```

### **Parameter Explanation**

**image：**Specifies the Docker image and its version to use. `latest` means pulling the latest version.

**restart：**Defines the container restart policy. `always` means the container will automatically restart when it stops or crashes.

**volumes：**

`./data:/var/lib/mysql`

`./`refers to the current directory where the Docker Compose file is located. It mounts the host directory `./data` to the container's `/var/lib/mysql` directory. This directory is the data directory for MariaDB, containing all database files (such as plugins, themes, uploaded files, etc.). By mounting a local directory, MariaDB data is persisted — even if the container stops or restarts, the data will not be lost.

**Related Reading**

[[FAQ] How to correctly represent volumes mount paths in the Docker Compose configuration file?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTQ0NywidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0ODcsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

**environment：**

`MariaDB_DB_HOST`: Configures the MariaDB connection to an external database. For example, `192.168.22.185` is the IP address of the MariaDB container, and `33306` is the mapped MariaDB port on the host. This variable tells the container where to locate the database service.

`MariaDB_DB_NAME`: Specifies the name of the database in use.

`MariaDB_DB_USER`: The username to access the database, typically `root` for the administrator.

`MariaDB_DB_PASSWORD`: The password for the database.

`ports`: Maps port 33306 on the host to port 3306 in the container. This is the port used to access MariaDB’s database service.

`network_mode`: Sets the container’s network mode to `bridge`, allowing the container to communicate with the NAS host via the bridge network.

### **Deploy the Project**

After confirming that the configuration file is correct, click the [Deploy] button. The system will automatically pull the required images and start the containers.

Once deployment is complete, you can access the MariaDB database through a browser by visiting: `http://<NAS_IP>:33306`(for example:`http://192.168.22.153:33306`).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250516/84a700e3-11eb-4c33-946c-5fb0983f0fa6.png)

## **Access MariaDB Using phpMyAdmin**

MariaDB does not provide a built-in web interface, so an external tool is needed for database management. We recommend using phpMyAdmin, which offers a graphical interface that makes it easy to manage the MariaDB database without having to remember complex SQL commands.

1. Open your browser and visit http://<NAS\_IP>:39085 (for example: <http://192.168.22.153:39085>) to access the phpMyAdmin login page.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250516/64655a04-b43c-453d-8c03-1a2096c5067b.png)

2. On the login page, enter the following information:

   * **Server Address:** The IP address and port of the MariaDB container, e.g., `192.168.22.185:33306`.
   * **Username:** The username for the database, which is `root` by default.
   * **Password:** The root password set in the Docker Compose configuration.

If the login is successful, you will see the phpMyAdmin dashboard, indicating that you have successfully connected to the MariaDB database.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250516/910d6e30-181c-40fa-9267-a1c84d2a820e.png)

## **Notes**

Please note that the images used in this tutorial are developed and maintained by third parties, and the tutorial is for reference only. UGREEN shall not be held responsible for any risks arising from improper user operations, third-party software vulnerabilities, or image updates, including but not limited to:

· Third-party images may cause unexpected modifications or deletions of files in the UGOS Pro system.

· Using insecure images may result in data being uploaded to third-party servers, posing risks of privacy breaches and data leakage.

· To ensure system stability and data security, please choose third-party images from trusted sources with caution.

Other notes：

1. The container file/folder paths provided are for reference only; you may create them based on your personal preferences.

2. The container port used for web access should match the local host port. If there is a conflict, use an available port instead. Local ports for different containers must not be the same, as port conflicts will prevent containers from starting.

3. Web access to containers is only available when using the bridge network mode.

4. The image is provided solely for deployment guidance. For specific usage and advanced features, please refer to online resources.

5. As the image is developed by a third party, please refer to the relevant official sources for configuration changes and bug fixes.

6. It is recommended to store Docker configuration directories on an SSD to avoid performance issues caused by mechanical hard disks.
