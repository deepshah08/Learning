# [Docker Usage] Deploying the Aria2 Downloader on UGREEN NAS and Configuring the Browser Extension

> **Article ID**: `497`  
> **Category**: `Application Guide > Docker > Docker Gameplay > [Docker Usage] Deploying the Aria2 Downloader on UGREEN NAS and Configuring the Browser Extension`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/497  

---

## **Introduction to Aria2**

Aria2 is a utility for downloading files. It can be deployed on a NAS and used as a browser-based download manager, serving as an alternative to tools like Xunlei. It supports batch downloads and multiple download protocols, including HTTP(S), FTP, SFTP, BitTorrent, and Metalink. Aria2 can download multiple files simultaneously and attempts to maximize your available download bandwidth. It allows simultaneous downloads via HTTP(S)/FTP/SFTP and BitTorrent, with data downloaded from HTTP(S)/FTP/SFTP sources being shared back to the BitTorrent swarm. When using Metalink, Aria2 automatically verifies data blocks during downloads through checksum validation, similar to BitTorrent. For more details, please refer to [the official documentation on GitHub.](https://github.com/aria2/aria2)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/82a49426-5de9-49af-95fd-227c4f44b927.png)

Please Note: The image used in this tutorial is developed and maintained by a third party and is provided for reference only. UGREEN NAS assumes no responsibility for any risks arising from improper user operations, third-party software vulnerabilities, or image updates. These risks may include, but are not limited to, the following:

* Third-party images may cause unintended modification or deletion of files stored on your UGREEN NAS.
* Using insecure images may result in your data being uploaded to third-party servers, posing risks of privacy breaches and data leaks.
* To ensure system stability and data security, it is strongly recommended that you carefully select trusted sources when using third-party images.

## **Deploying the Container Using Docker Compose**

To quickly deploy containers on your UGREEN NAS, it is recommended to use the *Project (Docker Compose)* feature. This approach is ideal for scenarios that require the creation and management of multiple containers, offering a convenient and organized way to handle containerized applications. Below are the detailed steps for deploying aria2 using Docker Compose. Click to learn more: [What is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### **Access the Docker Project Interface**

On the UGOS Pro system of your UGREEN NAS, open the Docker app, then click [Project] > [Create] to launch the project creation wizard.

### **Configure the Docker Compose File**

In the project creation wizard, you will need to upload a Docker Compose configuration file. Below is an example configuration for aria2:

```
services:
  aria2-ui: 
    restart: always  # Set the restart policy
    image: oldiy/aria2-ui-ng:latest  # Use the latest version of the image
    environment:  # Set environment variables
      - ENABLE_AUTH=true  # Enable authentication so the web interface requires a username and password
      - ARIA2_USER=admin  # Set the username to "admin"
      - ARIA2_PWD=admin  # Set the password to "admin"
      - SECRET=123456 #Specify the token key for connecting to the aria2 service
    ports:  
      - 40086:80  # Map NAS port 40086 to container port 80 (web interface)
      - 46801:6800 #Communication port for aria2
    volumes:
      - ./download:/data  # Storage path for downloaded data
      - ./config:/conf  # Storage path for configuration files
```

### **Parameter Explanation**

**restart：**Defines the container restart policy. `always` means the container will automatically restart if it stops or crashes.

**image：**Specifies the Docker image and its version to be used. `latest` indicates that the latest version will be pulled.

**environment：**

* `ENABLE_AUTH=true`：Enables authentication mode to prevent unauthorized access.
* `ARIA2_USER` and `ARIA2_PWD`：Specify the login username and password.
* `SECRET`：A token key used to connect and control the Aria2 service, enhancing communication security.

**ports：**

* `40086:80` ：Maps NAS port 40086 to container port 80 for accessing the web interface.
* `46801:6800`：Maps NAS port 46801 to container port 6800, used as Aria2’s RPC communication port.

**volumes：**

* `./download:/data`：`./` refers to the directory where the Docker Compose file is located. This line mounts the NAS’s local `./download` directory to the container’s `/data` directory for storing downloaded files.
* `./config:/conf`：Mounts the NAS’s `./config` directory to the container’s `/conf` directory for storing configuration files.

## **Deploy the Project**

After confirming that the configuration is correct, click [Deploy]. The system will automatically pull the image and start the container. Once the deployment is complete, you can access the Aria2 homepage via:`http://<NAS_IP>:port` For example: `http://192.168.22.153:40086`

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/49674f8e-6c8d-4185-afb3-938029402d47.png)

## **Access the AriaNg Interface**

1. In your browser, enter `http://<NAS_IP>:40086` to open the AriaNg web management interface. If the Aria2 status shows "Disconnected," it may be due to a missing authentication token.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/2a736e37-9e4a-40fc-857f-ba71fecf951f.png)

2. Click "AriaNg Settings", then click the tab next to "Global" to reconfigure the RPC parameters. After making changes, click "Reload Page":

* **RPC Address**: Enter the IP address or domain name of your NAS, followed by the RPC port specified in the Compose file.
* **RPC Protocol**: Select the default **HTTP** protocol.
* **RPC HTTP Request Method**: Use the default POST method.
* **RPC Secret Token**: Enter the Aria2 RPC token defined in the Compose file.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/161508b8-9d9b-48e8-9824-89c50ce7c6ed.png)

3. After reloading the page, if the token is configured correctly, the Aria2 status will show Connected.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/3d135bc0-a39f-4c3b-a7f6-dc46380937a5.png)

### **Test the Download**

1. On the top of the AriaNg page, click "➕New" to create a download task. You can either paste a direct download link or upload a torrent file. Click "Start Download" to begin the task.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/55f3910a-06dd-4784-95b2-3e45c7f7550b.png)

2. You can view the download progress and speed on the "Downloading" page.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/9998939c-625e-4d68-ac34-2cf14154952a.png)

### **Browser Extension Configuration**

1. To quickly download files directly to your NAS, take Microsoft Edge as an example: open the “Extensions” menu in the browser toolbar, search for “Aria2 Explorer,” and click “Get” to install it.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/7058efe2-a9dd-4510-8ed9-4cae77f30556.png)

2. On the extension configuration page, check “Monitor Aria2 download status” and adjust other options as needed. In the `Aria2-RPc-Server`settings, enter the RPC server token (which we set as 123456), the RPC service address, and port (e.g., `http://<NAS_IP>:46801/jsonrpc`). After completing the settings, click Save.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/3f2975c3-48e9-495a-8e9b-5b332ac961c1.png)

3. After configuring the extension, simply right-click on a download link and select “Export to Aria2” to add the task to Aria2 and start downloading automatically. If you previously enabled “Automatically intercept download tasks to Aria2” in the settings, clicking a download link will also automatically add the task to Aria2.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/580b8b6c-060b-4c2d-9294-8a9697e721fa.png)

4. You can also set the `Aria2 Explorer` extension to appear in the browser’s address bar. The icon will display the number of current download tasks, and hovering over it will show information such as download speed. Clicking the icon will open the Aria2 Web UI with one click.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/74d341d3-f9bc-4eda-875d-b32ca64ddc53.png)

### **Notes**

* The container’s volume and configured file/folder paths are for reference only; you can create them according to your personal preference.
* For port configuration, it’s recommended that the container’s web access port and the local port be the same. If the local port conflicts with another service, change it to an unused port.
* Local ports of different containers must not be the same; port conflicts will prevent containers from starting.
* Quick access web links for containers are only available when using the bridge networking mode.
* The image only provides a tutorial for container setup; for usage and advanced features, please refer to online tutorials.
* The image is developed by a third party; for configuration changes and bug fixes, follow the relevant official information.
* It is recommended to store the Docker configuration directory on an SSD to avoid mechanical hard disks from failing to enter sleep mode, which can impact system performance.
