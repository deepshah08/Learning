# Build a SiYuan Knowledge Base with Docker

> **Article ID**: `419`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Build a SiYuan Knowledge Base with Docker`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/419  

---

## Introduction

SiYuan is a widely used Markdown editor and knowledge management application. It helps users connect different notes through a graph-based structure to build a personal knowledge network, making it suitable for creating a customized knowledge management system.

**Note**: This guide uses Docker Compose deployment as an example. Pages and parameters may vary slightly depending on the system version, Docker app version, or SiYuan version. Refer to the actual interface and the project documentation for details.

## Docker Compose Configuration

Create a Compose project in the Docker app and enter the following configuration:

```
services:
  main:
    image: b3log/siyuan
    container_name: siyuan
    user: '0:0' # User and user group used for read/write access
    command: ['serve','--lang=zh_CN','--workspace=/siyuan/workspace/', '--accessAuthCode=123456']   # Specify the workspace directory/siyuan/workspace/，and the access password (set your own password)
    environment:
      - TZ=Asia/Shanghai  # Time zone
      - LANG=zh_CN.UTF-8  # Language
    ports:
      - 6806:6806  # Port mapping
    volumes:
      - ./workspace:/siyuan/workspace
    restart: always # Restart policy
```

## Deploy SiYuan

1. Open the "**Docker**" app, go to the "**Project**" page, and click "**Create**".

2. Enter a project name and paste the Compose configuration.

3. Click "**Deploy**".

After deployment is complete, wait for the container to start successfully.

## Access SiYuan

After deployment is complete, enter `http://NAS_IP:6806` in your browser to access SiYuan. Replace `NAS_IP` with the actual LAN IP address of your NAS.

Example: `http://192.168.1.100:6806`

Enter the access password, then click "**Unlock Access**".

If you cannot access SiYuan, check the following:

● Whether the container is running properly

● Whether port 6806 is already in use

● Whether the NAS IP address is correct

● Whether your computer and NAS are on the same LAN

● Whether there are any errors in the Docker project logs

![](https://file-us.ugreennas.com/admin/article/2026-08-14/f92b650d70fd423796536a406f2ae873.webp)

## Initial Setup and Usage:

Since the language was set to Chinese in the startup command, the system automatically displays the Chinese version of the user guide after you enter the interface. The guide provides detailed instructions on how to use SiYuan.

![](https://file-us.ugreennas.com/admin/article/2026-08-14/741cee6a1c624781aa31fa68c396a112.webp)

## What Should I Do If the Image Pull Fails

If the image fails to pull during deployment, check the project deployment logs.

If the following appears in the logs, it usually indicates an issue pulling the image from Docker Hub:

```
https://registry-1.docker.io/v2/
```

Configure a registry mirror or image proxy, then redeploy the project. For details, refer to "[How to Configure Registry Images, Image Sources, and Image Proxy in Docker?](https://support.ugnas.com/knowledgecenter/detail/article/en-US/297?clientType=PC) ".
