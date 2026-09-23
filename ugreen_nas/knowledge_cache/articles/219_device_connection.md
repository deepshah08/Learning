# Device Connection

> **Article ID**: `219`  
> **Category**: `Application Guide > Control Panel > Device Connection`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/219  

---

**Applicable Version:** UGOS Pro firmware **1.9.0.0062** and above

**Note:** Screenshots and interfaces in this document are for reference only. Actual displays may vary depending on system or application version. Some features may change across versions, please refer to your actual interface.

# Feature Overview

On the "**Control Panel" > "Device Connection"** page, you can centrally manage and configure LAN, remote access, and the Web portal.

● **LAN**: Configure the NAS custom domain access address for quick access to the device within the local network.

● **Remote access**: Supports enabling **UGREENlink remote access**. Once enabled, you can log in and access your home NAS with your UGREENlink ID even when away. Alternatively, you can set up **DDNS support** (requires a public IP network environment) for access via a fixed domain name.

**Operation path:**

1. Open the "**Control Panel"** app and click "**Device Connection"**.

2. Based on your needs, select **LAN**, **Remote access**, or **Portal setting** for configuration.

# Portal setting

In "**Control Panel" > "Device Connection" > "Portal setting"**, you can customize the NAS web login page style, configure HTTP/HTTPS ports, and enable advanced access features.

## Login style

UGOS Pro allows you to customize the background of the web login page for a more personalized experience.

**Steps:**

1. Open the "**Control Panel"** app, go to "**Device Connection" > "Portal setting"**.

2. In the "**Login style"** section, click "**Change background"**.

3. Upload an image from NAS or your local device as the background.

**Notes:**

● Supported image formats: **bmp, jpg, jpeg, png, webp, gif**.

● Maximum file size: **8 MB**.

● The login background only takes effect on the **Web login page**.

## Web service

You can modify the HTTP and HTTPS ports for the Web service and enable automatic redirection.

![](https://file-us.ugreennas.com/admin/article/2025-09-19/b70aac06ce9847d6a9e4555c634d16af.webp)

## Advanced settings

In "**Advanced"**, you can enable the following features to optimize network performance:

**Enable HTTP/2**: Improves page loading speed and efficiency by reducing latency with multiplexing and header compression.

**Enable HTTP compression**: Reduces transmitted data volume, accelerates page loading, and saves bandwidth.

**Enable reuseport**: Allows multiple worker processes to listen on the same port, enhancing concurrency and resource utilization.

**Customize maximum concurrent HTTP connections**: Adjust the number of HTTP connections the system can handle simultaneously based on server load to optimize performance and stability.

**Enable "Server" header in the HTTP response**: Lets clients identify the web server software responding to requests. However, for security considerations, it is generally recommended to disable this option to avoid information disclosure.

# Related Links

● [LAN Connection](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmODUifQ==)

● [Remote Access](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmODYifQ==)
