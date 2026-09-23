# [Docker Usage] Deploying Speedtest-X Speed Test Tool on UGREEN NAS

> **Article ID**: `529`  
> **Category**: `Application Guide > Docker > Docker Gameplay > [Docker Usage] Deploying Speedtest-X Speed Test Tool on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/529  

---

## **Speedtest-X Introduction**

Speedtest-X is a Docker-based network speed testing tool image. It features a user-friendly interface and provides efficient speed testing services.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250519/d6c8193b-8c3f-42b1-bc69-cc67a2428299.png)

**Main Features**

1. Network Speed Testing: Quickly and accurately measures network download and upload speeds.
2. Data Storage: Records speed test history, allowing users to compare network performance at different times.
3. Cross-Platform: Supports multiple operating systems and architectures, such as AMD64 and ARM64.
4. IP Resolution: Provides IP information.

GitHub Open Source Repository: <https://github.com/BadApple9/speedtest-x>

## **Deploying the Container Using Docker Compose**

On the UGOS Pro system, it is recommended to use project Docker Compose for quick container deployment. This approach is suitable for scenarios where multiple containers need to be managed simultaneously, simplifying the deployment and management of containers. Below are the detailed steps to deploy the speedtest-x service using Docker Compose.

Click to learn more: [What is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### **Access the Docker Project Interface**

In the UGOS Pro system, open the Docker app, then click [Project] > [Create] to launch the project creation wizard.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250819/50510e59-5c69-421b-961f-e1ef2bd38f12.png)

### **Configure the Docker Compose File**

In the project creation wizard, you need to enter the project name, storage path (auto-generated), and upload the Docker Compose configuration file. Below is an example configuration for speedtest-x:

```
services:
 speedtest-x:
     image: badapple9/speedtest-x # Use the image name
     container_name: speedtest-x # Specify the container name
     ports: 
         - '9001:80' #  Map container port 80 to host port 9001; you can also change the NAS host port to another port as needed
     restart: always # Set the container restart policy to always restart
```

### **Parameter Explanation**

**image**

* Specifies the image used as `badapple9/speedtest-x`. The image source is usually Docker Hub. Since no version is specified here, the latest version is used by default.

**container\_name**

* Sets the container name as `speedtest-x` for easier management through a fixed name.

**ports**

* `'9001:80'`：Maps port 80 inside the container to port 9001 on the UGREEN NAS. You can also change it to another port so that devices on the local network can access the container’s service via port 9001 on the NAS.

**restart**

* `always`：Configures the container to automatically restart no matter why it stops, ensuring high service availability.

## **Deploy the Project**

After confirming the configuration is correct, click [Deploy]—the system will automatically pull the image and start the container. Once deployment is complete, you can access the speedtest-x homepage via: `http://<NAS_IP>:port`

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250519/cb1f6fa4-799f-4c0a-bdde-902dd6e39fe7.png)

## **Accessing the speedtest-x Page**

1. After successful deployment, you can access the speedtest-x interface by opening a browser and visiting `http://<NAS-IP>:port`, replacing `<NAS-IP>` with the actual IP address of your NAS (for example, http://192.168.22.153:9001).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250519/d53f4208-0d39-4668-acdb-e28a8bc826e1.png)

2. Click “Start” to begin the speed test. You can measure the current network’s download and upload speeds and check for significant latency and jitter. speedtest-x can test both internal network speeds and external network access speeds.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250519/1463b238-0498-493d-8e1a-989060666de2.png)

## **Notes**

Please note that the image used in this tutorial is developed and maintained by a third party, and the tutorial is for reference only. UGREEN does not assume any responsibility for risks caused by improper user operations, third-party software vulnerabilities, or image updates, including but not limited to:

ꔷ Third-party images may cause accidental modification or deletion of files in the UGOS Pro system.

ꔷ Using insecure images may lead to data being uploaded to third-party servers, posing privacy and data leakage risks.

ꔷ To ensure system stability and data security, please carefully choose third-party images from trusted sources.

**Other notes:**

1. The file/folder paths for containers are for reference only. You may customize them according to your personal preferences.

2. The container’s web-access port and the local port should remain consistent. If there is a conflict, switch to an unused port. Local ports must be unique between containers—port conflicts will prevent containers from starting.

3. The container’s web link is accessible only in bridge network mode.

4.This image is provided solely for deployment guidance. For specific usage and advanced features, please refer to online resources.

5. Since the image is third-party developed, stay updated on configuration changes and bug fixes by following the relevant official channels.

6.It is recommended to store Docker configuration files on an SSD to avoid performance issues caused by mechanical hard disks.
