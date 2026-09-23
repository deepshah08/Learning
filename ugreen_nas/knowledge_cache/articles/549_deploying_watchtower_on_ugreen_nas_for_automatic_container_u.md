# Deploying Watchtower on UGREEN NAS for Automatic Container Updates

> **Article ID**: `549`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Deploying Watchtower on UGREEN NAS for Automatic Container Updates`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/549  

---

## **Application Overview**

Watchtower is an open-source tool designed for automatically updating Docker containers. It monitors running containers and updates them when a new version of the image is available, thereby enhancing security and stability.

**Features**

**Automatic Container Updates:** Regularly checks for container image updates and upgrades them automatically.

**Scheduled Checks:** Supports configurable check intervals to ensure containers always stay up to date.

**Notification Support:** Sends update notifications via email or other methods.

**Flexible Exclusion:** Allows specific containers to be excluded from automatic updates.

**Logging:** Keeps detailed logs of all update operations for easy reference.

**Multi-Registry Support:** Compatible with Docker Hub and other image registries to meet different needs.

## **Deploy Containers Using Docker Compose**

On the UGOS Pro system, it's recommended to deploy containers using Docker Compose, especially in scenarios that involve managing multiple containers. This method simplifies both deployment and management of containers. Below are the detailed steps for deploying Watchtower using Docker Compose.

Click to learn more: [What is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### **Access the Docker Project Interface**

On the UGOS Pro system, open the Docker application, go to [Project] > [Create], and launch the project creation wizard.

### **Configure the Docker Compose File**

In the project creation wizard, upload the following Docker Compose configuration file for Watchtower:

```
services:
    watchtower:
        container_name: watchtower
        image: containrrr/watchtower:latest # Use the latest Watchtower image
        restart: always #  Automatically restart the container on failure or reboot
        volumes:
            - '/var/run/docker.sock:/var/run/docker.sock'
            - '/etc/localtime:/etc/localtime:ro'
        environment:
            - WATCHTOWER_CLEANUP=true # Automatically remove old images after updates
            - WATCHTOWER_ROLLING_RESTART=true # Container Restart Mode
            - WATCHTOWER_POLL_INTERVAL=86400 # Check for updates every 24 hours
            - WATCHTOWER_NO_STARTUP_MESSAGE=true #  Disable startup message when Watchtower starts
```

### **Docker Compose Configuration Explanation**

|  |  |  |
| --- | --- | --- |
| Configuration Item | Value | Description |
| `container_name` | `watchtower` | Sets the container name to `watchtower`for easy identification and management |
| `image` | `containrrr/watchtower:latest` | Uses the latest Watchtower image to automatically get the newest features and updates |
| `restart` | `always` | Ensures the container restarts automatically after crashes or system reboots to improve service availability |
| `volumes[0]` | `/var/run/docker.sock:/var/run/docker.sock` | Grants Watchtower permission to manage Docker containers on the host (required mount) |
| `/etc/localtime:/etc/localtime:ro` | Synchronizes the container’s time with the host to ensure accurate logging timestamps |
| `environment` | `WATCHTOWER_CLEANUP=true` | Automatically deletes old image versions to save disk space |
| `WATCHTOWER_ROLLING_RESTART=true` | Enables rolling restart, updating containers one by one to minimize service downtime |
| `WATCHTOWER_POLL_INTERVAL=86400` | Sets Watchtower to check for image updates every 86400 seconds (24 hours) |
| `WATCHTOWER_NO_STARTUP_MESSAGE=true` | Disables startup messages for cleaner logs |

For more configuration options, please refer to the official Watchtower documentation: [Watchtower Arguments](https://containrrr.dev/watchtower/arguments/)

### **Deploying the Project**

After uploading the configuration file, click [Deploy]. The system will automatically pull the image and start the container.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250520/5d5b9ca5-dc1d-4889-ac02-7f0acdd42144.png)

### **Disabling Automatic Updates for Specific Containers**

If certain containers do not need to be updated, you can disable Watchtower’s monitoring function by configuring the `labels` node.

Example Instructions:

1. Add a `labels` node in the `docker-compose.yaml` file of the target container (e.g., `jellyfin`).

2. Use the label `com.centurylinklabs.watchtower.enable=false` to disable Watchtower’s update monitoring for that container.

```
services:
    jellyfin:
        container_name: jellyfin
        image: jellyfin:8
        。。。
        # Adding this label will disable update monitoring for the container
        labels:
            - com.centurylinklabs.watchtower.enable=false
```

## **View Container Updates**

You can check update information in the Watchtower container logs. At the interval specified by the environment variable, Watchtower will start checking for and updating container images.

Open the log page of the Watchtower container to view recent update records and statuses.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250520/e012f491-3b70-4588-9797-277bcc8f2d21.png)

**Fllow this tips**

Make sure that the environment variables for Watchtower are correctly configured to enable scheduled checks and updates of container images.

A common environment variable is `WATCHTOWER_POLL_INTERVAL`, which sets the time interval for checking updates.

## **Using DockerCopilot for Visual Update Management**

DockerCopilot is a user-friendly Docker management tool that allows you to visually check whether container images have updates and perform one-click updates.

If you prefer a graphical management interface, you can deploy DockerCopilot on your UGREEN NAS.

For detailed instructions, please refer to: [[Docker Usage] Setting Up DockerCopilot on UGREEN NAS to Achieve Real-Time Container Image Updates](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTA1NCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjozNTEsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

## **Frequently Asked Questions**

### **Q1：****Get the real path of the NAS folder and mount it to the Docker container**

When using Docker, you may need to mount folders from your NAS into a Docker container so the container can access data stored on the NAS.

You can refer to [Get the real path of the NAS folder and mount it to the Docker container](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTkzMCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo2MTEsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)to help you complete this operation.

## **Notes**

1. The images used in this tutorial are developed and maintained by third parties. This guide is for reference only. UGREEN shall not be held responsible for risks caused by improper operations, software vulnerabilities, or image updates, such as file errors or data leakage. Please use trusted images to ensure system and data security.
2. Container file paths can be customized. For web access, container ports must match the local ports. Avoid port conflicts between different containers.
3. Web access to containers is only available when using bridge network mode.
4. This guide only provides steps for deploying the image. For detailed usage and features, please refer to online resources. Stay informed about configuration changes and bug fixes through official channels.
5. It is recommended to store Docker configuration files on an SSD to avoid performance issues caused by mechanical hard disks.
