# Setting Up pgAdmin on UGREEN NAS as a General Database Management Tool

> **Article ID**: `467`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Setting Up pgAdmin on UGREEN NAS as a General Database Management Tool`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/467  

---

pgAdmin is a popular, graphical management tool specifically designed for managing and maintaining PostgreSQL databases. It offers users powerful features, including creating and modifying database objects (such as tables, indexes, functions, etc.), executing SQL queries, managing user permissions, backing up and restoring data, and monitoring database performance. Due to its user-friendly interface and extensive functionality, pgAdmin has become the tool of choice for many PostgreSQL database administrators and developers.

## Deploy pgAdmin Container with Docker Compose

To quickly deploy the pgAdmin container, especially in scenarios requiring management of multiple containers, it is recommended to use Docker Compose for containerized deployment. Docker Compose provides a simple way to manage multiple containers, making complex service deployment more efficient and straightforward. It is particularly suitable for the UGOS Pro system. The following will provide a detailed introduction on how to deploy the pgAdmin container with Docker Compose.

#### What is Docker Compose?

Docker Compose is a tool for defining and running multi-container Docker applications. By writing a `docker-compose.yaml` file, you can create and manage multiple container instances with simple commands, making the deployment of complex services easier and more efficient. For more detailed information, please click [What is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

## Docker Compose Deployment Steps

### Access the Docker Project Interface

In the UGOS Pro system, open the Docker application and click on [Project] > [Create] to enter the project creation wizard.

### Configure the Docker Compose File

When creating a project, you need to provide a Docker Compose file to define the container configuration. Below is an example of the `docker-compose.yaml` file used for deploying pgAdmin:

```
services:
    pgadmin4:
        image: dpage/pgadmin4
        container_name: pgadmin4
        ports:
            - '55433:80'
        environment:
            - 'PGADMIN_DEFAULT_EMAIL=ugreen@123.com'
            - 'PGADMIN_DEFAULT_PASSWORD=123456'
```

### Parameter Description

● **image:**

Deploy using the official Docker image of `dpage/pgadmin4`, which provides a visual management interface for PostgreSQL.

● container\_name:

Assign the name `pgadmin4` to the container for easy management and control through the name.

● ports:

Map the container's internal port `80` to the NAS's port `55433`. This allows users to access the `pgAdmin 4` web management interface via `http://<NAS_IP>::55433`. `pgAdmin`uses port `80` by default to provide services within the container.

● environment:

`PGADMIN_DEFAULT_EMAIL=ugreen@123.com`：You can customize the default administrator email for`pgAdmin`. You will need to use this email to log in, with the email address serving as the `pgAdmin`username.

`PGADMIN_DEFAULT_PASSWORD=123456`：Set the default administrator password for `pgAdmin`. Log in with this password, and it is recommended to change it later to a more complex one for enhanced security.

### Deploy the Project

After confirming that the `docker-compose.yml` file is correctly configured, click [Deploy]. The system will automatically pull the pgadmin4 image and start the container.

![](https://file-us.ugreennas.com/admin/article/2025-09-15/1b8746aaed424567ba2f1852885e54d9.webp)

After successful deployment, you can access the pgadmin4 console by visiting `http://<NAS_IP>:55433` in your browser.

![](https://file-us.ugreennas.com/admin/article/2025-09-15/231e09b375414d66b1b0e4c57fddaddb.webp)

### Notes

● The container's volume and configured file/folder paths are for reference only; you can create them according to your personal preferences.

● Port configuration, it is recommended to keep the container's web-accessible port and the local port consistent. If there is a local port conflict, change it to an unused port; non-web access defaults are set automatically.

● Local ports between containers must not be the same; port conflicts will prevent containers from starting.

● Quick access web links for containers are only accessible in bridge mode.

● The image only provides a tutorial for building the container; for usage methods and advanced techniques, please search online for tutorials.

● The image is developed by a third party; for specific configuration changes and bug fixes, please follow the official information.

## Related Link

[Setting Up PostgreSQL Database on UGREEN NAS](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMzk4LCJhcnRpY2xlSW5mb0lkIjo0NjgsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)
