# [Docker Usage] How to Build the Home Assistant Smart Home System with Docker

> **Article ID**: `475`  
> **Category**: `Application Guide > Docker > Docker Gameplay > [Docker Usage] How to Build the Home Assistant Smart Home System with Docker`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/475  

---

Home Assistant (HA) is an open-source smart home system built on Python, offering integration with various devices and highly customizable configurations. With Home Assistant, you can easily connect smart devices from different brands (such as cameras, fans, air conditioners) and leverage automation, group management, and UI customization features to create a personalized smart space. Additionally, HA supports Siri control, allowing users to manage home devices effortlessly through voice commands.

As open-source software, Home Assistant is available for free and is compatible with thousands of devices and services, enabling you to build a unified, intelligently connected home management system.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/a2a8032959324dc3b227b4b47462cc99.webp)

## Deploy Container Using Docker Compose

To quickly deploy Home Assistant on UGREEN NAS, it is recommended to use Docker Compose for project management. This method is suitable when you need to create and manage multiple containers, making containerized management convenient. The following detailed steps will guide you how to deploy Home Assistant using Docker Compose. [How to Use Docker Compose on UGREEN UGOS Pro?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### Access the Docker Project Interface

In the UGOS Pro system of UGREEN NAS, open the "Docker" app, click [Project] > [Create] to start the project creation wizard.

### Configure the Docker Compose File

In the wizard, you'll need to provide a Docker Compose configuration file. Below is the example configuration file for Home Assistant:

```
services:
    homeassistant:
        container_name: homeassistant  # Container name
        image: homeassistant/home-assistant:latest  # Container image version
        restart: always                # Container restart policy
        network_mode: host             # Container network mode
        volumes:
            - ./homeassistant:/config  # Mount directory for configuration files storage
        environment:
            - TZ=Asia/Shanghai         # Timezone setting
```

### Parameter Details

volumes  
Use the volumes directive to enable shared storage between the NAS main unit and the container. ./ represents the directory where the **Docker Compose** file is located, and the `homeassistant` folder in this directory will be mapped to the`/config`directory in the container. All configuration files and databases for Home Assistant will be stored in this directory.

`container_name`  
Assign the name `homeassistant` to the Docker container to facilitate direct management by container name.

`image`  
Specify the Home Assistant Docker image to use. The `latest` tag ensures that the most recent version is pulled.

`restart`  
Set the container's restart policy to `always`. This ensures the container restarts automatically, regardless of whether it stopped normally or unexpectedly.

`network_mode`  
Configure the container's network mode as `host`, allowing the container to use the NAS host's network interface directly, simplifying communication with external smart devices.

`environment`  
Use the environment variable `TZ=Asia/Shanghai` to set the container's time zone. This is essential for maintaining consistent timestamps for automated tasks and logs. You can adjust the time zone to match your location (e.g., `America/New_York` or `Europe/London`).

### Deploy the Project

After confirming that the configuration file is correct, click [Deploy]. The system will automatically pull the image and start the container. Once the deployment is complete, you can access the Home Assistant console by visiting `http://<NAS_IP>:8123` in your browser.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/a8feab4e1a1c4e2f9474a460cbaf1ca9.webp)

## Access the Home Assistant Console

1. After the deployment is complete, open the browser and enter the NAS IP address and port (e.g., `http://192.168.66.43:8123`) to access the console. Click "CREATE MY SMART HOME" and follow the setup wizard to complete the configuration.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/f02e6373a7a14a2787ac0daf94453f2e.webp)

2. Follow the prompts to enter your name, username, and password to create your Home Assistant account.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/88ce3fb91ae14e9f85014e2f073cb28e.webp)

3. You can set your home's location based on your actual needs, or click "Skip"to proceed.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/8e0eca90b93b400c84fadc784cdb2440.webp)

4. Choose whether to enable specific features as needed, then click "Next"to continue.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/0d077e1c2f8743979beca3cf601fb810.webp)

5. Click "FINISH" to access the Home Assistant home page. You can add devices, configure automation rules, and customize the dashboard here.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/399da42499df4a6d83ff76e7282b1129.webp)

6. If you need to change the language, you can adjust the system language to one you are familiar with in "User settings".

![](https://file-us.ugreennas.com/admin/article/2025-09-11/f289847340a34227a1da9f65091301e9.webp)

## Install the HACS Plugin Store

HACS (Home Assistant Community Store) is a community-driven plugin store of Home Assistant, allowing users to install various integrations and plugins. Follow these steps to install HACS:

1. Open the file manager, create `www` and `custom_components`folders under the`homeassistant`directory, and then create a`hacs`folder inside the`custom_components`directory. # custom\_components is the plugin directory.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/7417a46d7d2e44698c2cbaf89916c1d0.webp)

2. Go to GitHub to download the latest version of the HACS archive. If you don't have a GitHub account, you can register one first and then proceed with the download. <https://github.com/hacs/integration/releases>

![](https://file-us.ugreennas.com/admin/article/2025-09-11/ce4793c638ce4ec3ac5b5997b2e6311d.webp)

3. After downloading, extract the hacs.zip archive and upload the extracted files to the `custom_components/hacs` directory.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/c0f515a04e6f41bbadb7e022b4555608.webp)

4. Restart the Home Assistant container through the [Docker] application or by using the [Developer Tools] on the Home Assistant page.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/645c97436ae3406491b295c047c4c908.webp)

5. After the restart, go to the Home Assistant page, click [Settings > Devices & Services], select "Add Integration", search for and add HACS.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/6b98931333204964b310d64ea3b2dfff.webp)

6. Check all the options and click "SUBMIT".

![](https://file-us.ugreennas.com/admin/article/2025-09-11/6773275d7625490bae79118cb1a7588e.webp)

7. Copy the code, then click the GitHub link on the page to proceed with account binding. If you don't have a GitHub account, you can register one yourself and follow the prompts to complete the account binding process.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/d0cefd89b18945beae093aa4dc799aee.webp)

8. After entering the code, click "Continue".

![](https://file-us.ugreennas.com/admin/article/2025-09-11/29b7f77d54ab4fd1ab353cfdf7776f1c.webp)

9. Click "Authorize hacs".

![](https://file-us.ugreennas.com/admin/article/2025-09-11/63c068e30bf141f59509dba6b30b41bb.webp)

10. This screen indicates that the authorization was successful.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/25348332d97c464c8411349d6af359b0.webp)

11. After completing the binding, you will see the HACS option in the sidebar of Home Assistant.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/e812e3a6ad1d476bac61ecda61790363.webp)

## Install the Xiaomi-Miot Plugin

The Xiaomi-Miot plugin allows you to control Xiaomi smart devices through Home Assistant. Below are the steps to install Xiaomi-Miot via HACS:

1. Search for "Xiaomi Miot Auto" in the HACS store and download the plugin.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/bd05cbef6d7b4670ae81dcf7b07efa0e.webp)

2. Click "Download" to begin the download. After the download is complete, restart the Home Assistant container. You can restart the container from the [Docker] app or by clicking "Restart" in the [Developer Tools] section on the Home Assistant page.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/3ab24915dc2d4419959c1c8c19c8171e.webp)

3. After restarting the container, go to [Settings > Devices & Services] in Home Assistant. Click "Add Integration" and search for "xiaomi miot auto." Once found, click the corresponding icon to complete the integration.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/b14d7bf90c214d7899e32c00d212bd44.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-11/a06a0a5fd3604f9cbf3dc84b07bafd50.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-11/061e518b32a14f1480673d1d7432252d.webp)

4. Select "Add devices using Mi Account" and click "NEXT".

![](https://file-us.ugreennas.com/admin/article/2025-09-11/65e9d3463c66406e99d6f22688941081.webp)

5. Enter your Xiaomi ID and password, select "Automatic", and click "SUBMIT".

![](https://file-us.ugreennas.com/admin/article/2025-09-11/ff8e369682de4dc6b3f6a474657929e3.webp)

6. Based on your needs, select the devices to include or exclude, and complete the integration setup. Include mode allows you to manually select the devices you want to bind, while Exclude mode lets you manually choose devices you don't want to bind.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/c1bbd659145049a5abe07381fc7d78fa.webp)

7. After completion, you can view the added devices on the [Overview] page. From here, you can use Home Assistant to control all Xiaomi devices integrated into the system.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/bc6ca525e1644ed49ec4b188eaf2ccbb.webp)

## Configure Apple Homekit

If you want to add devices from Home Assistant to the Apple Home app, follow these steps:

1. In Home Assistant, go to [Settings > Devices & Services], select "Add Integration", search for "apple", and click on the Apple icon to access the submenu.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/4ec74a18ece341299f1b78677823317d.webp)

2. Then click "HomeKit Bridge". Based on your needs, select the domains you want to include, which can also be understood as different device types. After selecting, click "SUBMIT".

![](https://file-us.ugreennas.com/admin/article/2025-09-11/f5c7bb350ba7450b9b8eb0793ba51f4b.webp)

3. During the "Pair HomeKit" process, follow the guide to click "Submit" > Finish".

![](https://file-us.ugreennas.com/admin/article/2025-09-11/aec4b6b5f49749be84caa298fcb220a3.webp)

4. Click [Notifications] on the sidebar, scan the QR codes with Apple Home and complete pairing.

![](https://file-us.ugreennas.com/admin/article/2025-09-11/688dc7ae0809498b9b52f5989c1bcf12.webp)

## Precautions

● **Container Storage Space**: The provided file or folder path configuration is for reference only. You can adjust it based on your needs.

● **Port Configuration**: Ensure that the server port matches the local port. In case of port conflicts, change to an unused port.

● **Local Port Conflicts between Containers**: Port conflicts may prevent containers from starting properly.

● **Network Access**: Gateway links for quick container access can be established via the bridge mode.

● **Image Source Reliability**: Use images from official or well-trusted sources, and consult relevant tutorials as needed.

● **Third-Party Image Issues**: For changes or bug fixes in third-party images, monitor the official announcements for updates.

● **Recommended Storage Path**: Store the Docker configuration directory on an SSD to avoid performance issues caused by the hard disk failing to enter sleep mode.
