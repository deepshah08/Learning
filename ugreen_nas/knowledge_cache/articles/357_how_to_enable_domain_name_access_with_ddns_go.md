# How to Enable Domain Name Access with DDNS-GO?

> **Article ID**: `357`  
> **Category**: `Application Guide > Docker > Docker Gameplay > How to Enable Domain Name Access with DDNS-GO?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/357  

---

## Applicability

**Applicable Clients**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: UGOS Pro firmware 1.20.0.0127 and higher

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

DDNS-GO is a Dynamic DNS tool that automatically synchronizes the current network's public IP address with a DNS service provider. When the public IP address changes, DDNS-GO automatically updates the DNS record. After configuration, you can use a fixed domain name to access the device or services with open ports.

This guide uses Docker deployment of DDNS-GO as an example to explain how to update a dynamic public IP address with a DNS service provider, allowing you to access the device or container services on the device through a fixed domain name.

## Before You Begin

Before configuration, make sure the following requirements are met:

● A valid Registry Mirror has been configured in the Docker app

● A valid domain name is available

● The AccessKey ID and AccessKey key from the domain service provider have been obtained

● The current network has a public IP address

● You know where to configure port forwarding on the router

● A folder for storing DDNS-GO configuration files has been created in "Files"

**Note**:

● For instructions on purchasing a domain and obtaining an AccessKey, see "[How to Purchase a Domain and Obtain an AccessKey?](https://support.ugnas.com/knowledgecenter/detail/article/en-US/939) "

● To access the device or container services from outside the local network, you also need to configure port forwarding on the router

● DDNS-GO is a third-party tool. Service provider fields, authorization methods, and page content are subject to the actual DDNS-GO interface

## Pull the Image

1. Open the "**Docker**" app and go to "**Image**".

2. On the "**Image Database**" page, search for `jeessy/ddns-go` and click "**Download**".

![](https://file-us.ugreennas.com/admin/article/2026-09-18/7415805d60fd47b68173e6d36f7fd649.webp)

3. Keep the default version `latest`, click "**Confirm**", and wait for the image to finish downloading.

## Create a Folder for Configuration Files

1. Open "**Files**" and go to the `docker` shared folder.

2. Create a `ddnsgo` folder inside the `docker` folder.

This folder is used to store the DDNS-GO configuration files. When creating the container later, you need to mount this folder to the container directory.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/78f7049bf07b4e22b56ce7aaed2a82a9.webp)

## Create and Configure the Container

1. Open the "**Docker**" app and go to "**Image**">"**Local**".

2. Find the downloaded `jeessy/ddns-go` image.

3. Click "**+**" on the right to create a container.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/457be9de934f4fcdb329102110eb00f3.webp)

4. Set the container name and enable "**Auto restart**".

![](https://file-us.ugreennas.com/admin/article/2026-09-18/d031be7bb76e4721b7ab08d40a1e6685.webp)

5. Under "**Volume**", add a NAS directory/file and select the `ddnsgo` folder created earlier. Enter `/root` for Container directory/file and select "**Read/Write**" for Container permissions.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/6bfa257b85c1471b861798e33e945fef.webp)

6. Under "**Network configuration**", select `bridge`.

7. Configure Port mapping.

Container port: `9876`

NAS port: `39191`

Note:

● If the NAS port is already in use, change it to another port.

● If you change the NAS port, use the new port when accessing the DDNS-GO page.

● To use IPv6, change the network mode to `host` and make sure IPv6 is enabled on the device's network interface.

8. After confirming that the configuration is correct, click "**Confirm**".

After the container is created, you can view and manage the DDNS-GO container on the "**Container**" page.

## Access the Container Web Page

After the container starts, you can access the DDNS-GO page using either of the following methods.

### Method 1: Quick Access

1. Open the "**Docker**" app and go to the "**Container**" page.

2. Find the DDNS-GO container, click "**Quick access**", and select the configured Web access port.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/034c68d5e0e941b28e87937da64b0e95.webp)

### Method 2: Access via Browser

Enter `http://NAS-IP:NAS-port` in the browser address bar.

Example: `http://192.168.1.100:9876`

![](https://file-us.ugreennas.com/admin/article/2026-09-18/a3a7f36b64f2447899430d71331e1bfa.webp)

`NAS-IP` is the LAN IP address of the NAS, and `NAS-port` is the Web management port configured when creating the container.

## Initialize DDNS-GO

1. Set an account and password, then click "Log and configure as an administrator account".

![](https://file-us.ugreennas.com/admin/article/2026-09-18/f11c96baca864f71906857aab4001c7f.webp)

2. Select "cloudflare" as the DNS Provider, then enter the obtained AccessKey ID in Token.

3. Configure the settings based on your public IP type.

If you use a public IPv4 address:

● Enter the configured domain name in Domains.

● Make sure the DNS service provider, AccessKey, and DNS record are correct.

If you use IPv6:

● It is recommended to obtain the IP address through the network card.

● Make sure IPv6 is enabled on the device's network card.

● Enter the domain name whose DNS record needs to be updated in Domains.

4. Click "**Save**" on the page.

5. Check the log on the right and confirm that DNS resolution is successful.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/2c09db9e7c194ba2acf105276d02b80d.webp)

## Configure Port Forwarding

To access the device or container services from outside the local network through a domain name, configure port forwarding on your router. On the router management page, forward the external access port to the device's LAN IP address and the corresponding service port.

Example:

|  |  |
| --- | --- |
| Item | Example |
| Internal IP Address | `192.168.31.34` |
| External Port | `9876` |
| Internal Ports | `9876` |
| agreement | TCP |

The port forwarding entry and configuration method vary by router. Please refer to the actual router interface or the router manufacturer's official instructions.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/7f4ba034d5e1473abfa8ead6df6c65f9.webp)

## Access the Service via Domain Name

After configuration is complete, use the domain name and port to access the target service.

Access format: `http://domain:external-port`

Example: `http://example.com:9876`

If you use a subdomain, access the service using the complete configured domain name.

## FAQs

### Q1: What Should I Do If the Image Fails to Pull?

Check the following:

● Make sure the device network connection is working properly

● Make sure the image name `jeessy/ddns-go` is correct

● Make sure the Docker Registry Mirror is available

● Check whether an HTTP/HTTPS proxy is required to pull the image

### Q2: What Should I Do If the DDNS-GO Log Does Not Show Successful DNS Resolution?

Check the following:

● Make sure the AccessKey ID and AccessKey key are correct

● Make sure the AccessKey has permission to modify DNS records

● Make sure DNS resolution has been configured for the domain in the service provider's console

● Make sure the current network has a public IPv4 or IPv6 address

● Make sure the IP acquisition method selected in DDNS-GO matches the actual public IP type

### Q3: Why Can't I Access the Service from Outside the Local Network Even Though DNS Resolution Is Successful?

Check the following:

● Make sure port forwarding is configured correctly on the router

● Make sure the external port matches the port in the access address

● Make sure the target container or service is running

● Check whether the device firewall, router firewall, or ISP is restricting the relevant port

● Check whether the current network uses multiple layers of routing or carrier-grade NAT

## Notes

● AccessKey IDs, AccessKey key, and API Tokens are sensitive information. Store them securely and do not disclose them

● Opening ports to the public internet increases the risk of external access. Open only the ports you actually need and set strong passwords for the related services

● DDNS-GO and related images are maintained by third parties. Refer to the third-party project documentation for feature changes, image updates, and security risks

● Authorization methods, DNS rules, and access restrictions may vary by domain service provider. Refer to the service provider's actual instructions

## Related Reading

● [How to Purchase a Domain and Obtain an AccessKey?](https://support.ugnas.com/knowledgecenter/detail/article/en-US/939)

● [How to Configure Registry Images, Image Sources, and Image Proxy in Docker?](https://support.ugnas.com/knowledgecenter/detail/article/en-US/297)

#####
