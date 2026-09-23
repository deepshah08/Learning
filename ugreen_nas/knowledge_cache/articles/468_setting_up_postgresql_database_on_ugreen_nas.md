# Setting Up PostgreSQL Database on UGREEN NAS

> **Article ID**: `468`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Setting Up PostgreSQL Database on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/468  

---

PostgreSQL, often simply referred to as Postgres, is an open-source object-relational database management system (ORDBMS) with a long history and an excellent reputation in the field of databases. PostgreSQL is renowned for its high extensibility, strong concurrency control, strict data integrity, and extensive support for SQL standards.

## Deploy a PostgreSQL Container with Docker Compose

To quickly deploy a PostgreSQL container, especially in scenarios where you need to manage multiple containers, it is recommended to use Docker Compose for containerized deployment. Docker Compose provides a simple way to manage multiple containers, making it particularly suitable for the UGOS Pro system. The following will provide you with a detailed introduction on how to deploy a PostgreSQL container using Docker Compose.

## What is Docker Compose?

Docker Compose is a tool for defining and running multi-container Docker applications. By writing a `docker-compose.yaml` file, you can use simple commands to create and manage multiple container instances, making complex service deployment more relaxed and efficient. For more detailed information, please click on [What is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

## Docker Compose Deployment Steps

### Access the Docker Project Interface

In the UGOS Pro system, open the Docker application and click on [Project] > [Create] to enter the project creation wizard.

### Configure the Docker Compose File

When creating a project, you need to provide a Docker Compose file to define the container configuration. Below is an example of the `docker-compose.yml` file used for deploying PostgreSQL:

```
services:
  postgres:
    image: postgres
    container_name: postgres
    restart: always
    ports:
      - '55432:5432'
    volumes:
      - './data:/var/lib/postgresql/data'
    environment:
      - POSTGRES_PASSWORD=123456
      - LANG=C.UTF-8
```

### Parameter Description

**image:**

● Use the official PostgreSQL image `postgres` to create and run a PostgreSQL database instance.

**container\_name:**

● Assign the name `postgres` to the container for easy management and control through the name.

**restart:**

● Set to `always` to ensure the container will automatically restart regardless of the reason for its stoppage.

**ports:**

● `55432:5432` maps the NAS's port 55432 to the container's internal port 5432, allowing users to access the PostgreSQL service within the container via NAS's `http://<NAS_IP>:55432`.

**volumes:**

● ./ represents the directory where the current Docker Compose file is located. Mapping the NAS's `./data` directory to the container's `/var/lib/postgresql/data` ensures the persistent storage of the PostgreSQL database data. Even if the container is deleted or restarted, the data will be retained.

**environment:**

● **POSTGRES\_PASSWORD**: Set the password for the PostgreSQL database superuser `postgres` to `123456`.

● You can also set the environment variable `POSTGRES_USER` to specify the username for the superuser.

● **LANG**: Set the default language environment of the container to `C.UTF-8` to ensure character set compatibility for database operations.

### Deploy the Project

After confirming that the `docker-compose.yml` file is correctly configured, click [Deploy]. The system will automatically pull the PostgreSQL image and start the container. After successful deployment, you can connect to PostgreSQL using a database management tool (such as pgAdmin).

![](https://file-us.ugreennas.com/admin/article/2025-09-15/e9162e008ba7483a8331a5d3735060ea.webp)

### Notes

● The storage space for the container and the configured file/folder paths are for reference only. You can create them according to your personal preferences.

● For port configuration, it is recommended to keep the container port for web access and the local port the same. If there is a conflict with the local port, change it to an unused port. The default auto configuration is fine for non-web access.

● Local ports between containers cannot be the same. Port conflicts will prevent the container from starting.

● The shortcut access webpage link for the container is only accessible in bridge mode.

● The image only provides the container setup tutorial. For usage methods and advanced features, please search online tutorials for reference.

● The image is developed by a third party. For specific configuration changes and bug fixes, please follow the official updates.

● It is recommended to store the Docker configuration directory on an SSD to avoid preventing the mechanical hard disk from entering sleep mode, which could affect system performance.

### Access the PostgreSQL Web UI

After deployment, you can use database management tools such as pgAdmin to access PostgreSQL. When connecting, enter the container's IP address, port number, username, and password. Once connected successfully, you can manage the database.

## Related Link

[Docker Setup for pgAdmin as a Universal Tool for Managing Postgres Databases](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMzk1LCJhcnRpY2xlSW5mb0lkIjo0NjcsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)
