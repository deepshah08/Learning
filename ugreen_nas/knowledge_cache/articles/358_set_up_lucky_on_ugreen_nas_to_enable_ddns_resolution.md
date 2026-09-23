# Set Up Lucky on UGREEN NAS to Enable DDNS Resolution

> **Article ID**: `358`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Set Up Lucky on UGREEN NAS to Enable DDNS Resolution`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/358  

---

## Application Overview

Lucky is a Docker container image designed for monitoring and managing DDNS (Dynamic Domain Name System). This tool helps users easily synchronize their dynamic IP address with domain name resolution services, as well as configure reverse proxy and other related services, making external access more convenient and reliable.

**Key Features:**

● IPv6/IPv4 port forwarding

● Web service management

● Dynamic Domain Name System (DDNS)

● Wake-on-LAN

● IPv4 intranet penetration

● Scheduled tasks

● Automatic certificate application and management

**Default username: 666**  
**Default password: 666**

**Default access port: 16601**

Within the LAN, you can access Lucky’s web management interface by entering `NAS_IP:16601` (e.g., `192.168.22.153:16601`) into your browser's address bar.

**Developer website:** https://lucky666.cn/

**Developer documentation:** https://lucky666.cn/docs/intro

## Deploy the Container Using Docker Compose

On the UGOS Pro system, it is recommended to use the Docker Compose project method for quick container deployment. This approach is ideal for scenarios where multiple containers need to be managed simultaneously, as it simplifies both deployment and management. Below are the detailed steps for deploying **container** using Docker Compose.

Click to learn more: [What is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

1. Open the **"Docker"** application, click [Project] > [Create] to launch the project creation wizard.

2. In the project creation wizard, enter the following Docker Compose configuration information for the **container**. These configurations are for reference only; you can adjust them according to your own requirements.

```
services:
    lucky:
        container_name: lucky 
        image: gdy666/lucky:latest #Image name
        restart: always #Restart policy
        network_mode: host # Network mode
        volumes:
            - ./config:/goodluck # Path to store configuration files
```

3. After filling in the configuration file, click "Deploy". The system will automatically pull the image and start the container.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/3c9ec36ed77e4075bd30cb80cc34b5d9.webp)

4. Once the deployment is complete, access the container via a browser by entering `http://NAS_IP:16601` in the browser’s address bar. For example, if the NAS IP is `172.17.70.86`, enter `http://172.17.70.86:16601` in the browser to access it.

You can find the NAS device’s IP address by going to **[Network]** in the Control Panel, clicking **“Network connection”**, and viewing the IP address.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/1177684006ba4d0bae1cd781e5af4fee.webp)

### Compose Configuration Parameters Description

|  |  |
| --- | --- |
| **Parameter** | **Description** |
| **image** | Specifies the Docker image. `latest` indicates the latest version. |
| **restart** | Sets the restart policy to `always`, so the container will automatically restart if it crashes or stops, ensuring continuous service operation. |
| **volumes** | Maps NAS local folders to the container’s mount paths.  `./config`: Used to store the container’s configuration files. |
| **network\_mode** | Sets the container’s network mode to `host`. In host mode, the NAS’s IPv6 address can be used. |
| **Additional Notes** | `./`indicates that the path is within the storage path selected when creating the current project.  `./:/` means mounting the NAS local `./`directory to the container’s`/`directory.  The path before the colon is the NAS folder storage path, and the path after the colon is the corresponding mount mapping path inside the container. |

## User Guide

Before using the Lucky application for the first time, you need to complete the following initial setup:

### Change Username and Password

To ensure application security, please change the default username and password promptly:

1. Click [Settings] in the left sidebar to enter the settings page.

2. Scroll down to the "Login Vertification Settings" section.

3. Enter a new administrator username and password.

4. Click [Save Configuration] at the bottom of the page.

5. The next time you log in, you will need to authenticate using the new username and password.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/5a5a5593a79844fb8258872c5ba1e7c6.webp)

### Configure Dynamic Domain Name Resolution (DDNS)

DDNS allows you to access home network devices using a fixed domain name:

1. In the left-side menu, select [DDNS], then click "Add Task".

![](https://file-us.ugreennas.com/admin/article/2025-09-08/11d9505a8c4c49518435a4a52cdca956.webp)

2. Fill in the following information:

* **Task Name**: Customize as needed, e.g., "Home Network".
* **Operation Mode**: Easy Mode.
* **DNS Provider**: Select your domain registrar (e.g., Alibaba Cloud).
* **AccessKey ID and Secret**: Enter the credentials provided by your DNS provider.
* **Type**: Select either IPv4 or IPv6 based on your public IP type.
* **Public IP Retrieval Method**: Choose "Obtain via Interface".
* **Domain List**: First line: Enter the primary domain (e.g.,  `20241218.xyz`), Second line: Enter the subdomain (e.g., `*.20241218.xyz`).

![](https://file-us.ugreennas.com/admin/article/2025-09-08/ae4cf30636534581aa156c802a7c02ba.webp)

3. Click [Add Task], and after a short moment, if "DNS record matches" is displayed, the setup is successful.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/b2c0debb08494e45807bd488da305ebd.webp)

### Apply for an SSL Certificate

An SSL certificate ensures secure external access:

1. In the left-side menu, select [SSL/TLS Certificates], then click "Add Certificate".

![](https://file-us.ugreennas.com/admin/article/2025-09-08/148a38f4596442a5837b1658b2de3da8.webp)

2. Fill in the following information:

* **Remark**: Customize as needed.
* **Add Method**: ACME.
* **Certificate Authority**: Let's Encrypt.
* **Authentication Validation**: Choose the same service provider as previously.
* **ID and Secret**: Enter the **AccessKey** ID and secret key.
* **Domain List**: Enter the primary domain and subdomains.
* **Email**: Use the system temporary email or your personal email.
* **Algorithm**: Default to RSA2048.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/9c89d6212b204a0d9e7879936dc26ce4.webp)

3. After submission, wait a few minutes. Once the certificate is successfully issued, the ACME information and validity period will be displayed. The SSL certificate is valid for 3 months. Lucky supports automatic renewal, so no manual operation is required.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/dde6a73bfbe24c90b937e5bae8d31e0e.webp)

### Set Up Reverse Proxy and HTTPS Access

Enable HTTPS access through the reverse proxy feature:

1. Go to [Web Services] in the left-side menu, then click "Add Web Service Rules".

![](https://file-us.ugreennas.com/admin/article/2025-09-08/678c88fae2fa450b978525f502045f8a.webp)

2. Fill in the following information:

* **Rule Name**: Customize as needed.
* **Operation Mode**: Easy Mode.
* **Listening Type**: Choose IPv4 or IPv6 based on your public IP type.
* **Listening Port**: Default is 16666, can be customized (avoid conflicts with other service ports).
* **Firewall Auto-Allow**: Enable.
* **TLS**: Must be enabled to support HTTPS.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/9d48ec2c24e8437ab7231683117bbc3f.webp)

3. Click [Add Sub Rule] to configure specific services:

* **Sub Rule Name**: Customize, e.g., "nas".
* **Service Type**: Select Reverse Proxy.
* **Front End Domain/Address**: Enter the secondary domain (e.g.,`ugreen.20241218.xyz`).
* **Backend Address**: Enter the internal device’s IP and port (e.g.,  `192.168.31.70:9999`).
* **Other Options**: Keep default settings.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/00b900a1149049c398dc5b99b104b566.webp)

4. After completing the settings, click [Add Sub Rule] to apply.

**Note:** You can add different subrules for multiple services, but ensure that secondary domain prefixes do not conflict.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/20bbbf7eefaf447588bb054f24ab30d8.webp)

### BasicAuth Authentication(optional)

In the "Security Settings" section of the subrule, there is a basic encryption feature called BasicAuth authentication. When enabled, users must enter a username and password before accessing from the external network, adding an extra layer of security. Whether to enable BasicAuth authentication for services that already have password-protected login pages depends on individual needs. However, for services without password-protected login interfaces (such as certain web services), enabling BasicAuth authentication is highly recommended.

**Additional Information:**

1. **What is BasicAuth Authentication?**

BasicAuth authentication is a simple HTTP authentication mechanism that verifies user identity by including the username and password in the request header. Although this method is relatively basic, it provides a fundamental level of security, especially when no other authentication mechanisms are in place.

2. **Why is BasicAuth Authentication Needed?**

* **Additional Security Layer:** Even if the service itself has a password login page, enabling BasicAuth authentication offers extra protection against unauthorized access.
* **Protection of Sensitive Data:** For services without built-in authentication mechanisms, BasicAuth authentication effectively prevents unauthorized users from accessing sensitive data.
* **Simplicity and Ease of Use:** BasicAuth authentication is easy to implement, configure, and use.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/5d633452a3fb491584d3a297fdacad60.webp)

### Automatic Redirect to HTTPS

To enable automatic HTTPS redirection, follow these steps:

1. Add a new rule in [Web Services].

* **Operation Mode:** Customized Mode.
* **Listening Port:** Same as the previously configured listening port.
* **TLS:** Disabled.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/8b2f71ab3b7a445a855017fbfd502b1f.webp)

2. Click "Default Subrule" and configure:

* **Service Type**: Select Redirect.
* **Default Target Address**: Enter `https://{host}:{port}`.
* **Everything is Great Switch**: Enable (automatically adds request headers).

![](https://file-us.ugreennas.com/admin/article/2025-09-08/cc3f4c30d7f14282b4d8312252b6c38d.webp)

3. Save after completion. Once set, users only need to enter the domain name without manually typing `https://`.

## Using Lucky Web Service

**After completing all the settings, you need to map the reverse proxy port through your router to allow normal external access.** Thanks to Lucky’s reverse proxy, you only need to map one reverse proxy port, rather than mapping each service’s internal port individually. Please note that the internal and external port numbers should be the same. Here, we will map the listening port configured earlier.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/92175620e62343cd9c89f84cc50ec6ef.webp)

After completing port mapping, if all settings are correct, you can access the NAS from the external network. For example, when you enter `nas.20241218.xyz:9876`, you will be able to reach the NAS settings page. Additionally, you will notice a lock icon before the domain name, indicating that SSL-secured access is enabled.

![](https://file-us.ugreennas.com/admin/article/2025-09-08/f91f9c04b7ac40f790d1e7834a372c3b.webp)

## FAQ

### Q: Obtain the actual path of a NAS folder and mount it to a Docker container

When using Docker, you may need to mount a folder from the NAS to a Docker container so that the container can access the data stored on the NAS. You can refer to [Get the real path of the NAS folder and mount it to the Docker container](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTkzMCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo2MTEsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==) to help you complete this task.

## Notes

● The images mentioned in this tutorial are developed and maintained by third parties. This tutorial is for reference only. UGREEN does not assume any liability for risks caused by improper operations, software vulnerabilities, or image updates, such as file corruption or data leakage. Please use trusted images to ensure system and data security.

● Container file paths can be customized. When accessing via a web browser, the container port and the local port must be the same, and local ports of different containers must not conflict.

● Container web links are only accessible in bridge mode.

● The images are provided solely for setup guidance. For specific usage and features, please refer to online resources. For configuration changes and bug fixes, follow the official updates.

● It is recommended to store the Docker configuration directory on an SSD to avoid performance degradation caused by mechanical hard drives.
