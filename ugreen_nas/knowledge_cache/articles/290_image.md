# Image

> **Article ID**: `290`  
> **Category**: `Application Guide > Docker > Image`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/290  

---

> Application Notes: This document applies to UGOS Pro firmware version 1.7.0.3056. The screenshots provided are for reference only; the actual interface may vary slightly depending on the system or application version. Certain options and features may change across different versions. Please refer to the actual interface for accuracy.

## Feature Overview

The Docker app provides comprehensive image management capabilities. You can search for and download official Docker images at any time, import images from local files, and configure network acceleration to ensure smooth and reliable downloads.

## Searching for and Downloading Images

By default, the Docker app integrates the official Docker Hub repository. You can also add third-party image sources if needed.

1. Go to the "**Image**" page and switch to the "**Image Database**" tab.

2. Enter the image name in the search box (for example, mariadb) and press **Enter** to start searching.

3. Select the desired image from the search results and click "**Download**".

![](https://file-us.ugreennas.com/admin/article/2025-12-23/533cdcbe74ce4f638c07cdb053943a97.webp)

4. After clicking "**Download**", the system selects **latest** (the newest version) by default. Click "**Confirm**" to begin downloading.

**Notes:**

● If you need a specific version (such as lts-ubi), click the version tag and select the required version from the drop-down list.

● Once the download is complete, the image will automatically appear in the "**Local**" image list, where it can be used to create containers at any time.

![](https://file-us.ugreennas.com/admin/article/2025-12-23/6f76b3ac1a8547baa84b3a41fe62bb9f.webp)

## Managing Local Images

On the "**Local**" page, you can view all downloaded images and perform actions such as importing, exporting, or deleting images.

### Importing Images

In addition to downloading from repositories, you can add images in the following ways:

1. **Download from package source:** Click "**New Image**">"**From package source**".

![](https://file-us.ugreennas.com/admin/article/2025-12-23/7fd22788f10e4221a11e9f973858905c.webp)

● **By Image Name:** Manually enter the exact image name and version.

● **By URL:** Enter the direct download URL of the image. If the source requires authentication, provide the username and password.

2. **Import from NAS:** If you already have a local image file, click "**New Image**">"**From NAS**", then select the corresponding image file in Files to load it.

![](https://file-us.ugreennas.com/admin/article/2025-12-23/fc49a86cfd8641338048a38131d25e6d.webp)

### Exporting and Deleting Images

● **Export Image:** Select the image and click "**Export Image**" icon, then choose a storage path on the NAS to back up the image as a file.

![](https://file-us.ugreennas.com/admin/article/2025-12-23/422a8cef5a274e7ea1471fa54c436ce3.webp)

● **Delete Image:** Select the image you no longer need and click "**Delete**" icon. A confirmation dialog will appear; click "**Confirm Clearing**" to complete the operation.

![](https://file-us.ugreennas.com/admin/article/2025-12-23/0418837ede4a47528ba49e7bd31b3e5c.webp)

## Network Configuration (Registry and Proxy)

If you experience slow image downloads or see a message such as "**Download failed, please check the current NAS network and image repository configuration**",

![](https://file-us.ugreennas.com/admin/article/2025-12-23/8b92f06df40b4828be8e3af5bf3d1b09.webp)

this is usually because the network cannot connect to the official Docker Hub service (common error logs include https://registry-1.docker.io/v2/).

![](https://file-us.ugreennas.com/admin/article/2025-12-23/efcdee0eb8a14593bc4a90e9d0c51b4c.webp)

You can resolve this using one of the following methods:

### Method 1: Configure an Image Registry

By configuring a domestic or third-party image accelerator, you can significantly improve download speeds.

1. On the "**Image**" page, click "**Settings**" icon in the upper-right corner and select "**Registry Settings**".

![](https://file-us.ugreennas.com/admin/article/2025-12-23/2805171173734b0985e08b6a32694c0c.webp)

2. Add an accelerator address. You can either select a system-provided registry or manually enter a custom registry URL, then click "**Confirm**" to add it.

![](https://file-us.ugreennas.com/admin/article/2025-12-23/6021277463434230b3ee1de0c1ae5430.webp)

The system will prompt you to restart the Docker engine. Click "**Confirm**". After the restart is complete, try downloading the image again.

![](https://file-us.ugreennas.com/admin/article/2025-12-23/d3624a9c1cc94558877439660a66c6eb.webp)

### Method 2: Configure an Image Proxy

If you have your own proxy server, you can route Docker image downloads through the proxy.

1. On the image settings page, switch to the "**Proxy**" tab.

![](https://file-us.ugreennas.com/admin/article/2025-12-23/7df06bb6ff804475b2ee45e6f125a34e.webp)

2. Enable the Proxy option and enter the proxy address (it must start with http:// or https://).

3. Click "**Confirm**" to save. The system will restart the Docker engine. After the restart, all image download requests will be forwarded through the configured proxy server.

**Notes:**

● UGREEN NAS does not provide proxy services. You must set up and maintain your own proxy server.

● Any potential network security risks introduced by using a proxy are the responsibility of the user.

## Adding Image Source

If you need to download images from a private registry or a specific third-party source, you can add the registry address manually.

1. On the image settings page, go to the "**Image Repository**" section and click "**Add**".

![](https://file-us.ugreennas.com/admin/article/2025-12-23/96393dd319354e8f97e0c290e891688a.webp)

2. Enter an alias (a recognizable name) and the registry link. If the registry is private and requires authentication, be sure to provide the correct username and password.

![](https://file-us.ugreennas.com/admin/article/2025-12-23/aff4f8134e614c29aee4e72118f446d8.webp)

3. Click "**Confirm**" to complete the setup. Once added, you can search for images from this registry.
