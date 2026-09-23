# How to Configure Registry Images, Image Sources, and Image Proxy in Docker?

> **Article ID**: `297`  
> **Category**: `Application Guide > Docker > FAQ > How to Configure Registry Images, Image Sources, and Image Proxy in Docker?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/297  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client, Web Browser

**Applicable Version**:  UGOS Pro 1.18.1.0098 or later

The screenshots in this document are for reference only. The actual interface may vary slightly depending on the system or app version, please refer to the actual interface displayed.

## Introduction

When Docker pulls images, it needs to access an image registry. If image pulling is slow or you need to use a custom image registry, you can configure Registry Images, Image Registry, or Image Proxy in the Docker app.

Access Settings:

1. Open the **Docker** app and click "**Image**" in the left sidebar.

2. Click "**Settings**" in the upper-right corner of the page.

![](https://file-us.ugreennas.com/admin/article/2026-08-06/a17fdb6c37da4dc7bb9af98fbdd79cf0.webp)

## Configure Registry Images

Registry Images can help optimize image pull speed. Follow the steps below to configure a Registry Image:

1. On the "**Image Repository**" settings page, click "**Registry Settings**" in the image registry list.

![](https://file-us.ugreennas.com/admin/article/2026-08-06/a6bfecf417d34adb953fc1c53d95aa37.webp)

2. Enter the source registry URL to use and click "**Confirm**" to save.

![](https://file-us.ugreennas.com/admin/article/2026-08-06/0eb76f7455124b359d8261d08339730f.webp)

When entering the URL, the system provides recommended registry Image addresses. To use a recommended address, click "**+**" to add it.

3. After saving, the system will restart the Docker engine. Once the restart is complete, Docker will use the configured Registry Image address to pull images.

## Configure Image Source

The Image Repository in the Docker app uses the official Docker Hub image source by default. If you have a custom image source, you can add it in Image Repository. Follow the steps below:

1. On the **Image Repository** settings page, click "**Add**" in the Image Repository list.

![](https://file-us.ugreennas.com/admin/article/2026-08-06/e6893544d51c4fbda109c26e299f34f1.webp)

2. Enter the image source alias and link, then click "**Confirm**".

![](https://file-us.ugreennas.com/admin/article/2026-08-06/60a52ecb9e134dd38c84909f0dde3e47.webp)

If authentication is required for the image source, enter the username and password.

3. After adding the image source, you can view it in the Image Repository list. You can edit or remove the added image source from this page.

## How to Pull Images from an Image Source?

After adding an Image Source, you can download images from the specified Image Source. Follow the steps below:

1. Open the **Docker** app, click "**Image**" in the left sidebar, and switch to the "**Local**" tab.

2. Click "**New Image**" > "**From package source**".

![](https://file-us.ugreennas.com/admin/article/2026-08-06/00599c6061f84917b8461e7316e06d75.webp)

3. Select a search method and enter the image name or URL as prompted.

If you need to pull a specific version, enter the corresponding version number.

![](https://file-us.ugreennas.com/admin/article/2026-08-06/b26709e7d8184fd893b6af84a3e4093d.webp)

4. After entering the required information, click "**Confirm**". The system will start pulling the image.

After the pull is complete, you can view the image in the **Local Image** list. If the pull fails, go to the "**Log**" page in Docker to check the cause of the failure.

## Configure Image Proxy

Image Proxy allows the Docker app to access specified network resources. Before configuring, make sure the proxy server address is available. An invalid proxy may cause the following issues:

● Image search failure

● Image pull failure

● Docker network access issues

This feature requires basic networking knowledge. For information security reasons, UGREEN does not provide third-party proxy services or setup tutorials. Please prepare a reliable proxy server address on your own.

![](https://file-us.ugreennas.com/admin/article/2026-08-06/dee81d74c7514cec9aba66db9598bc3a.webp)

## Why Is Image Pulling Still Slow After Using a Registry Image or Image Source?

Image pull speed depends on the service status of the Image Source. Some Image services may undergo regular maintenance or upgrades, which may cause service interruptions, slower response times, or pull failures during this period.  
It is recommended to check the provider's official announcements or service status page to confirm whether the service is operating normally. You can also try switching to another available Registry Image or Image Source and pull the image again.

## Notes

● The UGREEN Cloud mobile app currently does not provide an entry for configuring Image Source.

● After modifying the Registry Image settings, the system will restart the Docker engine. Please wait until the restart is complete.

● Incorrect configuration of Registry Image, Image Source, or Image Proxy may prevent images from being searched or pulled.

● The availability, stability, and security of third-party Image Source, Registry Image, and proxy services are subject to the information provided by the service providers.
