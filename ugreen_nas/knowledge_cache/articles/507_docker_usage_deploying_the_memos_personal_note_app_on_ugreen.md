# [Docker Usage] Deploying the Memos Personal Note App on UGREEN NAS for Cross-Platform, Anytime Note-Taking

> **Article ID**: `507`  
> **Category**: `Application Guide > Docker > Docker Gameplay > [Docker Usage] Deploying the Memos Personal Note App on UGREEN NAS for Cross-Platform, Anytime Note-Taking`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/507  

---

## **Introduction to Memos**

Memos is a lightweight, card-based knowledge management tool designed to help users capture, categorize, and organize ideas into a personal knowledge base, thereby improving knowledge management efficiency. Key features include:

1. **Markdown Support:** Allows users to include code blocks, multimedia resources, and more to meet personalized note-taking needs.
2. **Cloud Sync:** Supports cloud backups and synchronization across multiple devices, improving convenience for learning and work.
3. **Powerful Search Functionality:** Offers search and filter tools for quickly finding specific notes.
4. **Cross-Platform Access:** Mobile apps are available, allowing access and editing across devices anytime.

For more features, refer to [the Memos Official Technical Documentation.](https://www.usememos.com/docs)

## **Deploying the Container Using Docker Compose**

On the UGOS Pro system, it is recommended to use **Projects (Docker Compose)** for fast container deployment, especially in scenarios where multiple containers need to be managed simultaneously. This method simplifies both the deployment and management of containers.

Click to learn more: [What is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### **Access the Docker Project Interface**

On the UGOS Pro system, open the Docker application and click [Project] > [Create] to launch the project creation wizard.

### **Configure the Docker Compose File**

In the project creation wizard, you will need to upload the Docker Compose configuration file. Below is an example configuration for Memos:

```
services:
  memos:  
    image: neosmemo/memos:latest  # Image and version used
    container_name: memos  
    volumes:
      - /volume1/memos/:/var/opt/memos  # Map local data storage directory
    ports:
      - 5230:5230  # Port mapping: map container port 5230 to NAS port 5230
```

### **Parameter Explanation**

**image**:

* Specifies the Docker image and its version to be used. `latest` indicates that the latest version will be pulled.

**container\_name**:

* Assigns a custom name to the container, making it easier to identify and manage the container by its name.

**ports**: Configures the port mapping between the container and the host machine.

* # Maps container port `5230` to NAS port `5230`, ensuring that the service can be accessed via port `5230` on the host machine.

**volumes**: Configures data volume mounts to achieve persistent data storage.

* Maps the host NAS path `/volume1/memos/` to the container's `/var/opt/memos/` for storing application data (such as configuration files and persistent data).

* Replace `/volume1/memos/` with the actual configuration storage path on your NAS, or use `./memos/` where `./` refers to the current directory where the Docker Compose file is located.

**Related Reading**

[**[FAQ] How to correctly represent volumes mount paths in the Docker Compose configuration file?**](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTQ0NywidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0ODcsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

## **Deploy the Project**

Once the configuration is confirmed to be correct, click [Deploy]. The system will automatically pull the image and start the container. After the deployment is complete, you can access the Memos homepage through `http://<NAS_IP>:<port>`.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250507/e21944dc-f066-4798-89a1-5c73fd773c2f.png)

## **Access the Memos Interface**

1. Open your browser and visit: `http://<NAS_IP>:5230` (e.g., `http://192.168.1.100:5230`).

* **First-time login:**

  + Click "Sign in", and register your username and password. The first account registered will be the administrator account.
  + You can switch the language at the bottom of the page; here, we select English.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250507/b369ef6e-41b4-40d6-a4dc-a666308aea6c.png)

2. After logging in, you can perform the following actions through the [Settings] menu on the left:

* Click [Edit] to modify your username, nickname, and add a personal email address.
* Click [Members] to add or remove user members and set permissions.
* Click [Manage] to view and manage data storage paths (by default, data is stored in the previously configured`/volume1/memos/`folder).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250507/670f6f35-6ee7-44bb-9c4c-7c5b3371157e.png)

3. To log into Memos on mobile devices (e.g., iPhone, iPad)

* For Apple devices: Search for and download Memos from the App Store, then enter the NAS domain address and your account credentials to log in.

* For Android devices: Due to compatibility limitations, login is only supported through the domain and account credentials.

**Note:** If you need to access Memos from outside your local network, you must configure a public IP and domain, or use a network tunneling service. For more features and detailed instructions, please refer to [the Memos Official Technical Documentation.](https://www.usememos.com/docs)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250507/2aeceb9e-094e-443c-a7a3-4403b0e27e45.png)

## **Notes**

Please be aware that the image used in this tutorial is developed and maintained by a third party. This guide is for reference only. UGREEN assumes no responsibility for risks caused by improper user operations, third-party software vulnerabilities, or image updates, including but not limited to:

ꔷ Third-party images may result in unexpected modifications or deletions of files in the UGOS Pro system.

ꔷ Using unverified images may lead to data being uploaded to third-party servers, posing privacy and data leakage risks.

ꔷ To ensure system stability and data security, please use third-party images from trusted sources with caution.

**Other notes:**

1. The container’s file/folder paths in this guide are for reference only. You can customize them based on your own preferences.

2. The container's web-access port should match the local port. If there’s a conflict, switch to an unused port. Local ports for different containers must be unique to avoid startup failures due to port conflicts.

3. Container web access is only available in bridge network mode.

4. This tutorial only covers deployment. For usage details or advanced features, please search online.

5. Since the image is developed by a third party, please follow the official sources for updates and bug fixes.

6. It is recommended to store the Docker configuration directory on an SSD to prevent performance issues caused by mechanical hard disks.
