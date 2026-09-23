# How to Set Up a FreeCAD CAD Workstation with Docker?

> **Article ID**: `892`  
> **Category**: `Application Guide > Docker > Docker Gameplay > How to Set Up a FreeCAD CAD Workstation with Docker?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/892  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS).

**Applicable Version**: NAS Firmware 1.17.0.0034 or later.

The descriptions in this document are for reference only. The actual interface and operation paths may vary slightly depending on your system or application version. Please refer to the actual interface.

## Introduction

FreeCAD is an open-source, general-purpose parametric 3D CAD modeling application released under the LGPL license. It is primarily designed for mechanical engineering and product design, and can also be used for architectural design, finite element analysis, 3D printing, and related applications.

UGREEN NAS supports deploying FreeCAD with Docker. After deployment, you can access the FreeCAD web interface from a browser for remote CAD modeling and file viewing.

FreeCAD GitHub repository: <https://github.com/linuxserver/docker-freecad>

## Create a Compose Project

1. Open the **Docker** application. In the left navigation pane, click "**Projects**", then click "**Create**".

2. On the Create Project page, specify a custom project name.

By default, the system creates a folder with the project name under the **docker** shared folder.

The Compose configuration file is stored in the project folder. You can also change the storage path as needed.

3. Enter the Compose configuration.

4. Click "**Deploy**".

The system automatically pulls the required image and deploys the project after the image download is complete.

### Sample Compose Configuration

Use the following Compose configuration as a reference to create a FreeCAD project:

```
services:
  freecad:
    image: linuxserver/freecad:latest
    container_name: freecad
    ports:
      - 3000:3000
      - 3001:3001
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Asia/Shanghai
    volumes:
      - ./config:/config
    shm_size: "1gb"
    restart: always
```

### Parameter Description

`TZ`: Specifies the time zone for the container.

`/config`: Stores the FreeCAD configuration files and runtime data. ./config refers to the config folder in the project directory.

`shm_size`: Specifies the amount of shared memory available to the container.

## What to Do If the Image Pull Fails

If the image fails to download during deployment, check the project deployment logs.

If the following entry appears in the logs, it usually indicates that Docker Hub failed to pull the image:

```
https://registry-1.docker.io/v2/
```

Configure an image registry mirror or proxy, then redeploy the project. For detailed instructions, refer to the UGREEN NAS tutorial on configuring Docker [registry mirrors](https://support.ugnas.com/knowledgecenter/detail/article/en-US/297?clientType=PC) .

## Access the FreeCAD Web Interface

After the Compose project is deployed, enter `https://NAS的IP:3001`in your browser's address bar to access the FreeCAD web interface.

**Note**：

● Use the **HTTPS** protocol. This image uses a self-signed certificate by default.

● You can find the NAS IP address in the widget on the top system bar.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/037fd6c75ef746bb8bd0447c3792a06c.webp)

## What to Do If the Browser Shows a "Not Secure" Warning

Because the FreeCAD image uses a self-signed certificate by default, your browser may display warnings such as:

● **Your connection isn't private**

● **Connection isn't secure**

● **The certificate isn't trusted**

These warnings are expected. Click "**Advanced**", then select "**Proceed**" to continue to the FreeCAD web interface.

The warning message may vary depending on the browser. Please refer to the message displayed in your browser.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/2625de3239094794a729715c12cc0419.webp)

## Configure FreeCAD on First Launch

After opening FreeCAD for the first time, you can customize the interface based on your preferences.

On the initial setup page, you can configure the following:

● Language

● Theme

● Navigation Style

● Units System

To change the interface language, click the "**Language**" drop-down list and select your preferred language.

After completing the configuration, click "**Done**" to close the setup window.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/9d35ac4da504449e905afb337b6c2d75.webp)

## Import a Project File

FreeCAD does not support importing or exporting **DWG** files directly because DWG is a proprietary file format developed by Autodesk and is subject to licensing restrictions.

To open a CAD file in FreeCAD, first use a CAD application to convert the **DWG** file to **DXF**, then import the DXF file into FreeCAD.

Perform the following steps:

1. Open **Files** on the NAS.

2. Locate the configuration folder for the FreeCAD Compose project.

3. Navigate to the following path, then open the "config" > "Desktop". Upload the **DXF** file you want to import to this folder.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/ef1b635a9b3d40e78388ad6e3eaee689.webp)

4. After uploading, return to the FreeCAD web interface. Click "**File"** in the top menu bar > "**Open"**.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/aebfdf7432f54b6f9c7212c5403e348a.webp)

5. In the file selection window, navigate to`config/Desktop`，select the uploaded "**DXF**" file, and click "**Open**".

![](https://file-us.ugreennas.com/admin/article/2026-08-27/ea59536306ff46ffaaa544de7e8a19f6.webp)

6. Choose the import method and click "**OK**".

![](https://file-us.ugreennas.com/admin/article/2026-08-27/309d53ba7d314896ac111557217f8194.webp)

After the import is complete, you can view and edit the file in FreeCAD.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/16286f50baa547e389a9b9565860ef67.webp)

## Use an NVIDIA Dedicated GPU

Some UGREEN NAS models support external NVIDIA discrete GPUs. After the GPU is connected, you can enable NVIDIA GPU support in Docker to provide hardware acceleration for FreeCAD, such as graphics rendering.

Before use, ensure that the NAS is properly connected to an NVIDIA discrete GPU, and that the NVIDIA drivers and NVIDIA Docker toolkit are installed.

For detailed instructions, refer to the tutorial on [How to Use a Dedicated GPU in Docker？](https://support.ugnas.com/knowledgecenter/detail/article/en-US/884?clientType=PC)

### Sample Compose Configuration

After connecting the GPU, it is recommended to create a new Compose project to avoid conflicts between the existing project configuration and the new GPU settings.

You can use the following configuration as a reference to create a FreeCAD project:

```
services:
  freecad:
    image: lscr.io/linuxserver/freecad:latest
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Asia/Shanghai
      - PIXELFLUX_WAYLAND=true
      - AUTO_GPU=false
      - DRINODE=/dev/dri/renderD128
      - DRI_NODE=/dev/dri/renderD129
      - NVIDIA_VISIBLE_DEVICES=all
      - NVIDIA_DRIVER_CAPABILITIES=all
    volumes:
      - ./config:/config
    ports:
      - "3000:3000"
      - "3001:3001"
    devices:
      - /dev/dri:/dev/dri
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu, compute, video, graphics, utility]
    security_opt:
      - seccomp=unconfined
    shm_size: "4gb"
    restart: always
```

### GPU-Related Parameter Description

`TZ`: Sets the time zone for the container.

`/config`: Used to store FreeCAD configuration files and runtime data.

● Example: `./config:/config`

● Here, `./config` refers to the config folder in the project directory.

`shm_size`: Specifies the amount of shared memory available to the container.

`AUTO_GPU=f`alse: Disables the automatic GPU detection script at container startup and instead forces the use of a specified GPU device via environment variables.

NVIDIA\_VISIBLE\_DEVICES=all: Passes NVIDIA GPUs from the host to the container. When set to all, the container can access all available NVIDIA GPUs.

NVIDIA\_DRIVER\_CAPABILITIES=all: Enables NVIDIA driver capabilities. When set toall, it enables compute, video encoding/decoding, and graphics rendering capabilities.

DRINODE 和 DRI\_NODE: Specifies the Linux Direct Rendering Infrastructure (DRI) device node path.

● Example: DRINODE=/dev/dri/renderD128，DRI\_NODE=/dev/dri/renderD129

● renderD128 typically refers to the Intel integrated GPU node, whilerenderD129usually refers to the NVIDIA discrete GPU node. Actual device node numbers may vary depending on the system. Please refer to the NAS detection results.

security\_opt: Used to relax certain system call restrictions in Docker’s default Seccomp security profile.

● Example: security\_opt:`-`seccomp=unconfined

● Some graphics rendering or GPU-related features may require this setting to function properly.

For more parameters, refer to the linuxserver/freecad GitHub repository documentation.

### How to Verify Whether FreeCAD Is Using the Dedicated GPU

After deployment is complete and you have entered FreeCAD, perform actions such as modeling or switching views in the FreeCAD interface. If the dedicated GPU is being used correctly, you will be able to observe changes in NVIDIA GPU usage in the NAS Task Manager.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/ec3806ac726248dab84ac6b46733dc33.webp)

## Notes

● The FreeCAD web page must be accessed via **HTTPS**. If you use `http://<NAS_IP>:3001`, the page may not load properly.

● The first deployment requires downloading the image. The time required depends on network conditions. If the download is slow or fails, configure a Docker image registry mirror or proxy first.

● Before importing CAD files, ensure the file format is supported by FreeCAD. If you need to import DWG files, it is recommended to convert them to DXF format first.
