# Container

> **Article ID**: `289`  
> **Category**: `Application Guide > Docker > Container`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/289  

---

**Applicable Version:** UGOS Pro 1.10.0.0092 and above

Screenshots and interfaces in this document are for reference only. Actual displays may vary depending on system or application version. Some features may change across versions, please refer to your actual interface.

It is not recommended to install this app on ARM-based devices with ≤ 4 GB of RAM, as it may affect system performance and stability.

## Feature Overview

The "**Container"** page is the primary interface for interacting with running applications. Each container represents an independently running application instance.

## Viewing Container List

On this page, the system displays all containers that have been created on the device. Regardless of how a container was created, it will be listed here. The list supports search, filtering, and sorting.

Containers typically originate from the following four sources:

● Containers manually created by the user

● Containers created by importing a JSON configuration file

● Containers deployed via "**Project**" (Docker Compose)

● Containers installed through the "**App Center**" that run as part of an application suite dependent on Docker

## Creating a New Container

You can start a new container instance based on a local image.

● Click the "**Create**" button and select an image from the "**Local**"images list to configure the container.

● If the required image is not available locally, go to the "**Image**" page to download it first, then return to this page to create the container.

## Modifing Container Configuration

Configuration rules vary depending on the container's source. Please note the following distinctions:

● **Directly editable**: For containers created manually or via imported JSON files, you can click "**···**">"**Edit**" on this page to open the container editor and modify its parameters.

● **Edit in project**: Containers created through "**Project**" cannot be edited directly here. Please go to the "**Project**" page, locate the corresponding entry, update the Compose configuration, and redeploy the project for the changes to take effect.

● **Not editable**: For containers associated with apps installed from the "**App Center**", configuration changes are not supported to ensure system stability.

## Common Management Operations

You can perform the following control and monitoring actions on containers in the list:

● **Status control**: Enable, stop, restart, or delete containers.

● **Terminal and logs**: Click a container to access its management page, use the "**Terminal**" for command-line interaction, or view real-time "**Log**" to troubleshoot issues.

● **Basic information**: View service port mappings exposed by the container, as well as the specific paths of mounted volumes (storage).

![](https://file-us.ugreennas.com/admin/article/2026-01-15/f237a8710a2344f78cf1db2ef65754a6.webp)

## Project Update Detection

If you enable update detection on the "**Management**" page, the system will provide a convenient way to keep your projects up to date:

● **Update notifications**: When a new version of an image used by a container is released, a prominent update indicator will appear in the project list.

● **Perform upgrade**: Click "**Update**" to automatically pull the latest images used by the project and rebuild the project's containers.

**Note**: During the rebuild process, services may be briefly interrupted.

## Configuring Desktop Shortcuts

For easier access, you can create desktop shortcuts for containers.

1. Open the Docker application, click "**Container**" in the left sidebar, locate the target container, then click "**···**">"**Desktop shortcut**".

![](https://file-us.ugreennas.com/admin/article/2026-01-15/bf710b6956c94f1ca07c29170537dbc3.webp)

2. A configuration window will appear, where you can customize the shortcut's name, icon, and port number.

![](https://file-us.ugreennas.com/admin/article/2026-01-15/035a82c564ca4c428aed8b75cee70262.webp)

3. After confirming the information, click "**Confirm**". The system will create a shortcut icon on the desktop.

**Notes on shortcut port configuration:**

![](https://file-us.ugreennas.com/admin/article/2026-01-15/56dad458b4c04dc2837298b75a44414d.webp)

● If the container uses the Bridge network and exposes only one port, the system will automatically fill in the port number.

● If the container uses the Host network, or if multiple ports are exposed under the Bridge network, you must manually specify the port number.

● If you are unsure of the correct port, you can check the image's default port on the official Docker Hub page or review the port settings used when the container was created.

## Remotely Access Containers via UGREENlink

If you are logged in with a UGREENlink ID, you can use the desktop shortcut to remotely access the container's web interface. After creating the shortcut, simply click the desktop icon to open the container's web page.

● **Availability**: This feature is only available to users logged in with a UGREENlink ID.

● **Limitations**: If you are currently logged in to the NAS via DDNS or direct IP access, remote access through this shortcut is not supported.
