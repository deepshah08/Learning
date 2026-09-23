# Why Does Baserow Run Properly with Docker Compose but the Container Automatically Stops When Created Directly?

> **Article ID**: `484`  
> **Category**: `Application Guide > Docker > FAQ > Why Does Baserow Run Properly with Docker Compose but the Container Automatically Stops When Created Directly?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/484  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client, Web Browser

**Applicable Version**: NAS Firmware 1.18.0.0032 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Issue Description

When creating a Baserow instance using Docker Compose, it runs normally. However, when pulling the image and creating the container directly through Docker, the container automatically stops and the service cannot be accessed successfully.

## Image Name

Image name: baserow/baserow:latest

## Diagnostic Information

When deploying Baserow using containers, you need to mount a host directory and ensure that the directory has the appropriate permissions. Since the PostgreSQL database creates and runs under the `postgres` user, the mounted directory permissions should be set to 700 or 750. If the permissions are lower than this standard, the container will fail due to insufficient permissions and automatically stop.

## Solutions

### Solution 1

If you do not need to map the database directory to a NAS directory/file, simply add the environment variable `DISABLE_VOLUME_CHECK=yes` when creating a new container. **Please note that** if no directory mapping is configured, all data inside the container will be deleted when the container is removed; if directory mapping is configured, the database data will still be retained even if the container is removed.

### Solution 2

If you need to map database files or other files to the host or network storage, follow these steps:

1. Before creating the container, open **Files** and create a subfolder named `baserow_data` under the docker directory in the shared folder.

2. Select `baserow_data`, right-click to view its properties, and copy the location (actual path).

3. Use an SSH terminal to modify the permissions of the actual `baserow_data` path. For example, run `chmod 755 /volume1/docker/baserow_data` to ensure proper access permissions.

4. Create the container. In Storage settings, specify the NAS directory/file `docker/baserow_data` to be mapped to the container directory/file path `/baserow/data`, with the container permission set to Read/Write.

5. After completing the above configuration, create the container.
