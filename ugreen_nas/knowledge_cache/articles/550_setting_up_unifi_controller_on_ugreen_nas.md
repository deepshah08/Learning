# Setting Up UniFi Controller on UGREEN NAS

> **Article ID**: `550`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Setting Up UniFi Controller on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/550  

---

## **Application Overview**

The UniFi Controller is a network management software developed by Ubiquiti Networks, specifically designed for managing UniFi series devices such as access points (APs), switches, and routers. With the UniFi Controller, users can easily perform the following tasks:

**Configure network devices;**

**Monitor network status;**

**Manage firmware upgrades.**

After setting up the UniFi Controller, you can efficiently manage multiple UniFi devices through a unified platform and optimize your network performance.

## **Deploying a Container Using Docker Compose**

On the UGOS Pro system, it is recommended to use the **Project (Docker Compose)** method for quickly deploying containers. This approach is ideal for scenarios that require managing multiple containers simultaneously, as it simplifies both deployment and management.

Click to learn more: [What is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjoxMjI4LCJhcnRpY2xlSW5mb0lkIjo0MTEsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiMS4wIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### **Access the Docker Project Interface**

In the UGOS Pro system, open the Docker application and click [Project] > [Create] to launch the project creation wizard.

### **Configure the Docker Compose File**

In the project creation wizard, upload the following Docker Compose configuration file for UniFi:

```
services:
  unifi:
    container_name: unifi
    image: jacobalberty/unifi #Image name
    restart: always # Restart policy
    init: true
    ports:
      - "8080:8080" # HTTP access port; if there's a conflict, you can change the NAS-side port (the part before the colon)
      - "8443:8443" # HTTPS access port; keep the default value
      - "3478:3478/udp" #  Default port for WebRTC STUN/TURN protocols
      - "10001:10001" # Default port for UniFi Controller to discover unmanaged UniFi devices
    volumes:
      - ./config:/unifi # Stores UniFi configuration files and database
    environment:
      - TZ=Asia/Shanghai # Container time zone
      - BIND_PRIV=false 
      - RUNAS_UID0=false
      - UNIFI_HTTPS_PORT=8443
    user: unifi # Run container processes as user "unifi"
```

### **Parameter Descriptions**

**image：**Specifies the Docker image version to be used.

**restart：**Container restart policy. `always` means the container will automatically restart if it stops or crashes.

**init：**

`init: true`：Enables `tini` as the container’s init process, responsible for managing subprocesses within the container to prevent resource leaks.

**ports：**

`8080:8080`：Maps the HTTP interface port, used for accessing the Web UI.

`8443:8443`：Maps the HTTPS interface port, used for secure (encrypted) Web UI access.

`3478:3478/udp`：Supports the STUN/TURN protocols for WebRTC.

`10001:10001`：Used by the UniFi Controller to discover unmanaged UniFi devices (such as access points or switches).

**volumes：**Maps NAS file directories to container paths.

`./config:/unifi`：Maps the NAS storage directory `./config` to the container path `/unifi`, which is used to store all configuration files and data. The path before the colon refers to the storage location on the NAS.

**Note:**

* `./` refers to the directory where the current Docker Compose file is located.
* The path before the colon is the storage path on the NAS, and the path after the colon is the corresponding path inside the container.

**Related Reading**

[[FAQ] How to correctly represent volumes mount paths in the Docker Compose configuration file?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTQ0NywidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0ODcsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

**environment：**

`TZ=Asia/Shanghai`：`TZ=Asia/Shanghai`: Sets the container time zone to Asia/Shanghai (China). You can adjust this based on your own time zone, such as `America/New_York` for the U.S. or `Europe/London` for Europe.

`BIND_PRIV=false`：Disables binding to privileged ports (e.g., ports below 1024), allowing non-root users to bind to service ports.

`RUNAS_UID0=false`Prevents the container from running as the root user, enhancing container security.

`UNIFI_HTTPS_PORT=8443` Sets the HTTPS port. The HTTP port will automatically redirect to this HTTPS port. If you need to change the HTTPS port, modify this environment variable accordingly.

**user：**

`user=unifi`：Specifies that the program inside the container runs as the `unifi` user, which enhances security by avoiding the use of the default `root` user.

### **Deploy the Project**

After uploading the configuration file, click [Deploy], and the system will automatically pull the image and start the container.

Once the deployment is complete, open a browser and visit the following address to access the UniFi interface:

```
http://<NAS_IP>:8080
```

Please replace `<NAS_IP>` with the actual IP address of your NAS, for example:`http://192.168.22.153:8080`.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250522/cff0aaed-2452-4686-97a9-4937a4ce99c6.png)

## **User Guide**

After deployment is complete, use the UniFi Controller by following these steps:

1. Open your browser and go to `http://<NAS_IP>:8080`to access the login page. Follow the on-screen instructions to complete the initial setup.

2. Give your UniFi network server a name;

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250522/b80f1156-638c-4561-95fd-0619cb8c1f62.webp)

3. Log in to your UniFi account or register a new one (if you don’t have an account, click "Create a UI Account" to create a new user).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250522/f152276c-2224-491b-87ba-542df85e177e.webp)

4. After logging in successfully, you can manage your UniFi network devices through the web interface, including:

**Configuring wireless networks;**

**Managing connected devices;**

**Monitoring network status;**

**Upgrading device firmware.**

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250522/23582b7d-a6f4-44a0-99fb-e209eae3e531.webp)

## **Notes**

* The image used in this tutorial is developed and maintained by a third party. This tutorial is for reference only. UGREEN is not responsible for any risks caused by improper operations, software vulnerabilities, or image updates, such as file anomalies or data leaks. Please choose trusted images to ensure system and data security.
* You can set container file paths according to your preference. When accessing via web, the container port and the local port must be the same. Local ports of different containers must not conflict.
* Container web links are only accessible in bridge networking mode.
* The image only provides deployment instructions; for specific usage and advanced features, please search online. For configuration changes and bug fixes, follow official updates.
* It is recommended to store the Docker configuration directory on an SSD to avoid performance issues caused by mechanical hard disks.
