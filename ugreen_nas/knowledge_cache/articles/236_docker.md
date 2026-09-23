# Docker

> **Article ID**: `236`  
> **Category**: `Application Guide > Docker > Docker`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/236  

---

**Applicable Version:** UGOS Pro 1.10.0.0092 and above

Screenshots and interfaces in this document are for reference only. Actual displays may vary depending on system or application version. Some features may change across versions, please refer to your actual interface.

It is not recommended to install this app on ARM-based devices with ≤ 4 GB of RAM, as it may affect system performance and stability.

# Feature Overview

On UGREEN NAS, Docker can be used to quickly deploy various services and applications, such as personal blogs, download tools, private cloud notes, DDNS resolution services, and more.

With Docker, users can flexibly create, run, and manage multiple independent application containers on the NAS, achieving "multiple uses on a single device." This allows the NAS to function not only as a storage device but also as a powerful multi-application platform.

## Install the App

1. Open [App Center], locate the Docker app in the app list, and click "**Install"** to start the installation wizard.

2. Follow the wizard prompts to complete the installation setup step by step.

# Setting Up Docker Container Desktop Shortcuts and Enabling Remote Access

Docker Containers Support Desktop Shortcuts. Users can quickly access containers via desktop shortcuts. After logging in with a UGREENlink ID, remote access to container web interfaces is enabled for a more convenient operational experience.

### Configuring Desktop Shortcuts

1. Open the "Docker", select [**Containers**], and choose your target container.

2. Click the **"**···**"** (More)button next to the container, then select **"Desktop shortcut"** to open settings.

![](https://file-us.ugreennas.com/admin/article/2025-10-21/fa669afec4bc4beab646154051a8c4a0.webp)

3. In the pop-up window,you can customize the name, access port, and icon.For bridge network containers, the port auto-populates.

4. If the container uses host network or uses bridge network but has multiple ports, you need to manually configure the port.

> If you are unsure about the port number, you can check the official Docker Hub page to view the default port of the container image;

> You can also check the port settings when creating the container in Docker.

![](https://file-us.ugreennas.com/admin/article/2025-10-21/621df66fcec04b71a306e9d5a45798b7.webp)

5. Click **"Confirm"** to create the desktop shortcut.

![](https://file-us.ugreennas.com/admin/article/2025-10-21/5bfef24171ff4aebb6a69eada2269484.webp)

### Remote Access via UGREENlink

After creating the desktop shortcut, click the shortcut icon to access the container's web interface. Docker containers support remote access, but you must log in to the system **using your UGREENlink ID to enable this functionality**.

**Restrictions:**

● Remote access is **only available to users logged in via UGREENlink**;

● If you log in using **DDNS or other methods**, you cannot use UGREENlink remote access.

## Common Docker Terminology

Before using Docker on UGREEN NAS, it is essential to understand some common Docker terminology:

● **Docker Compose**  
Docker Compose is a tool designed to define and manage multi-container Docker applications. It simplifies the deployment of complex applications. By using a YAML file, you can describe multiple services, networks, and storage configurations for an application and start all services with a single command.

● **Container**  
A container is a running instance of an image and serves as the execution entity of Docker. Containers run applications in isolated environments, ensuring they do not interfere with one another.

● **Image**  
An image serves as the foundation of a Docker container. It is a template that contains all files and environments required for an application to run. Containers are created based on images, which are read-only. You can obtain images from public repositories like Docker Hub or create your own.

● **Network Mode**  
Docker supports various network modes. You can configure a container to share the host's network or isolate it from the external network using bridge mode.

● **Port Mapping**  
To enable communication between a containerized application and the external environment, Docker allows port mapping. For example, when running a web server, you can map a container port to a specific port on the host (UGREEN NAS) to allow external access.

● **Volume**  
Volumes provide a persistent storage mechanism in Docker. Since containers are temporary (data is lost when the container is deleted), volumes ensure important data is saved on the NAS storage, remaining intact even if the container is restarted or removed.

● **Data Usage**  
This refers to the total space occupied by containers and images.
