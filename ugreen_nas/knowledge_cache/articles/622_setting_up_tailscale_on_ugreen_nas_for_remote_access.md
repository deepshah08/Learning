# Setting Up Tailscale on UGREEN NAS for Remote Access

> **Article ID**: `622`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Setting Up Tailscale on UGREEN NAS for Remote Access`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/622  

---

## **App Introduction**

Tailscale is a networking tool based on WireGuard technology, designed to help users quickly build secure private networks. With its efficient peer-to-peer technology, Tailscale offers secure and reliable network connections. Here are its main features:

* Based on the WireGuard protocol, all data transmissions are strongly encrypted to ensure data security during transit.
* No complex network configuration is needed; simply install the client and log in to your account to easily achieve direct connections between devices.
* Supports a variety of operating systems, including Linux, Windows, macOS, iOS, and Android.
* Utilizes peer-to-peer connections to bypass central nodes, reducing latency and improving transmission efficiency.
* Supports the creation of private cloud services, such as file servers, gaming servers, etc.

Tailscale is suitable for various scenarios. For instance, when you are away and need to access your home or office computers, NAS, and other devices, you can install the Tailscale client on your phone or computer, log in to the same Tailscale account, and all devices will automatically connect to the same virtual local area network. You can access these devices as if you were local.

## **Preparation Work**

### **Register a Tailscale Account**

1. Open [the Tailscale login page](https://login.tailscale.com/admin/machines).
2. Choose a convenient login method, such as using a Microsoft account or an Apple account, or try other options.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/1728bd60-5b58-4c05-b52b-37f0dffb91b2.png)

### **Download the Client**

After logging in, click on "Skip this introduction" to bypass the initial guide. Click the "Download" button and choose the client version you need.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/888eebe0-f8d2-43f7-b816-589da429734a.png)

### **Generate Authentication Key**

1. On the "Settings" page, click "Generate auth key" to create an authentication key.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/a38c4091-6fc8-4a27-9d95-54527895f1ff.png)

2. Turn on the Reusable switch and click Generate key.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/2e2bdefd-5993-4264-b716-4c8feed3c392.png)

3. Copy the generated key and save it to a text file for future use.
4. After saving, click Done.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/d63b73f6-2b9c-43d4-95a2-72018317ee04.png)

## **Docker Compose Configuration Deployment**

On the UGOS Pro system, it is recommended to use [Docker Compose](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9) for quick deployment of containers, which is suitable for scenarios where multiple containers need to be managed simultaneously. This method simplifies the deployment and management of containers. Here are the detailed steps for deploying with Docker Compose.

1. Open the "Docker" app, click on [Project] > [Create] to launch the project creation wizard.
2. In the project creation wizard, enter the following Docker Compose configuration information for the container. These configurations are for reference only, and you can adjust them according to your own needs.

```
services:
  tailscale:
    container_name: tailscale
    image: tailscale/tailscale:latest # Image Name
    restart: always #Restart Policy
    volumes:
      - ./tun:/dev/net/tun  
      - ./lib:/var/lib  
    environment:
      - TS_AUTH_KEY=tskey-auth-k5msULvKo511CNTRL-odJfJb2aQcKSprp9JpLwcKd58Fws4Pje # Enter the key generated earlier.
      - TS_STATE_DIR=/var/lib/tailscale # Fixed value, no need to change.
      - TS_ROUTES=192.168.31.0/24 #Enter your router's gateway.
    network_mode: host # Use the host networking mode.
    privileged: true # Privileged Mode
```

3. After filling in the configuration file, click "Deploy", and the system will automatically pull the image and start the container.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/acd3bd28-21fb-4e57-a732-8d2781fe75c2.png)

### **Compose Configuration Parameter Explanation**

|  |  |
| --- | --- |
| Parameter | Explanation |
| image | Specify the Docker image, with `latest` indicating the use of the most recent version of the image. |
| restart | Set the restart policy to  `always` so that the container will automatically restart when it crashes or stops, ensuring continuous service operation. |
| environment | Set environment variables to configure services within the container.  `TS_AUTH_KEY`: The authorization key for authentication, generated in the Tailscale control console.  `TS_STATE_DIR`: The state directory for Tailscale, fixed to  `/var/lib/tailscale`inside the container.  `TS_ROUTES`: Used to configure routing settings to manage specific LAN traffic via Tailscale. Please fill in the correct subnet range based on your actual network configuration. For example, if your router's gateway address is  `192.168.31.1`, you should enter`192.168.31.0/24`here. |
| ports | Port mapping: Map the NAS's port 8096 to the container's port 8096, and access the Web interface via `http://NAS_IP: port`. |
| volumes | Map local NAS folders to the mount paths inside the container.  `./tun:/dev/net/tun`: The TUN virtual network is required for Tailscale to access the TUN virtual network device. The `./tun`on the left side of the colon is the relative path on the NAS (relative to the directory where the Compose file is located). The `/dev/net/tun`on the right side is the path inside the container.  `./lib:/var/lib`:`./lib` on the left side of the colon with the actual path on your NAS where you store media files. This is the directory where Tailscale stores its state. |
| network\_mode | Host networking mode, which allows direct access to the host's network resources and also supports the use of the NAS's IPv6 address. |
| privileged | Enable privileged mode to allow the container to access the host's network devices. |
| Supplementary Explanation | `./` indicates that the path is within the directory chosen for the current project's storage location.  `./:/`indicates mounting the local  `./` directory on the NAS to the `/`directory inside the container.  The path before the colon is the storage path of the folder on the NAS, and the path after the colon is the corresponding mount mapping path inside the container. |

## **Guide for Use**

After the container is deployed and running, log in to [the Tailscale management console.](https://login.tailscale.com/admin/machines) Check if the NAS appears in the Machines list. If it is displayed, it indicates that Tailscale has been successfully deployed.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/6efee73b-5c88-4cc3-9776-645619dd2511.webp)

### **Disable Device Key Expiry Policy**

By default, device keys have an expiration date. To reduce the need for repeated configurations, you can disable the automatic key expiry policy in the console.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/fb20f763-c210-4d39-a49e-2e75a7693025.webp)

### **Set Up Networking Routes**

In the device console, click "Edit route settings" and check the corresponding gateway addresses.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/5fad34fc-9edd-45ff-aecb-1500dbcdbc10.webp)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/a6751012-854c-41a2-8e29-3e99b3abbaf3.webp)

### **Using Tailscale and NAS for Networking**

1. Download the client from [the Tailscale download page.](https://tailscale.com/download) For example, for Windows, select the required client to download and install.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/122f6b39-db73-4ab7-991f-d966280ecf58.webp)

2. After the client is installed, in the Windows system, right-click the Tailscale icon in the taskbar and select "Log in." The system will open the Tailscale login interface in your browser.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/b95580a7-e407-4e74-bc33-6a57f37d5b05.webp)

3. After successful login, click "Connect," and the device will appear in the "Machines" list.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/d1b8076b-6f12-488d-acf4-898d96deb569.webp)

4. To simplify management, you can choose to disable the automatic expiration policy for device keys. This operation is the same as the method mentioned earlier for disabling the automatic key expiration on the NAS device.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/6a99e5ae-8daf-4fe7-a132-5d8e6faff5c1.webp)

### **Accessing NAS via Tailscale**

Make sure the client device is logged in and running Tailscale. Enter the NAS's internal IP address in the browser's address bar to access the Web services provided by the NAS.

Example: Accessing the Sun-panel service on the NAS.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/36cedd18-97b8-4f36-a437-35c9436a4d0a.webp)

### **For more information**

For more features and advanced configurations, please refer to [the Tailscale official documentation.](https://tailscale.com/kb)

## **Precautions**

* The images involved in this tutorial are developed and maintained by third parties. The tutorial is for reference only, and UGREEN does not assume any risks caused by improper operations, software vulnerabilities, or image updates, such as file abnormalities or data leaks. Please use trusted images to ensure the security of your system and data.
* Container file paths can be set by yourself. When accessing via the web, the container port and the local port must be the same, and local ports of different containers must not conflict.
* Container web links are only accessible under the bridge networking mode.
* The image only provides setup instructions; for specific usage and methods, you can search online. For configuration changes and bug fixes, please pay attention to official information.
* It is recommended to store the Docker configuration directory on an SSD to prevent mechanical hard drives from affecting performance.
