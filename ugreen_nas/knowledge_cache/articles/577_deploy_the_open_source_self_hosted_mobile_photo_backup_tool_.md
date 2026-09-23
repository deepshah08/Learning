# Deploy the Open-Source Self-Hosted Mobile Photo Backup Tool Immich on UGREEN NAS

> **Article ID**: `577`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Deploy the Open-Source Self-Hosted Mobile Photo Backup Tool Immich on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/577  

---

## Introduction to the Immich

Immich is an open-source photo backup solution, similar to Google Photos, but completely free and with AI features. It is primarily used for deployment on home servers such as NAS, offering photo backup, management, and intelligent processing capabilities.

**Features**

● **Photo Backup:** Immich can automatically back up photos and videos from devices, ensuring data security and integrity.

● **Intelligent Management:** It has intelligent classification and organization features, which can automatically sort photos and videos based on information like date and location.

● **AI Features:** Immich supports AI image processing, including face recognition, image stitching, AI beautification, and smart editing, improving image quality and management efficiency.

● **Multi-Device Sync:** Users can sync photos and videos across different devices, enabling cross-device access and management.

● **User-Friendly Interface:** The user interface is aesthetically designed and easy to use, making it suitable for home users.

For more detailed features, please refer to [Immich's official website](https://docs.immich.app/overview/quick-start/) .

## Create Immich Folder

1. Open **"Files"** app.

2. Under the shared folders, go to the **Docker** directory and create a new folder named "**immich**".

![](https://file-us.ugreennas.com/admin/article/2026-01-04/f884143adb174c3c96307f806221fdf6.webp)

### Create Subfolders and Save Their Paths

1. Enter the newly created **immich** folder, then create the following three subfolders:

● **postgres**

● **albums**

● **mobile uploads**

2. After creating them, select each folder, right-click "**Properties**", and copy its folder path. Save these paths—you'll need them later when editing the configuration file.

|  |  |  |
| --- | --- | --- |
| **Folder Name** | **Example Folder Path** | **Notes** |
| postgres | `/volume1/docker/immich/postgres` | Store application data |
| albums | `/volume1/docker/immich/albums` | Album directory |
| mobile uploads | `/volume1/docker/immich/mobile uploads` | Directory for uploaded photos |

## Prepare the Configuration Files

Before deploying Immich, you need to prepare the required configuration files.

1. Visit Immich's GitHub repository and download the [docker-compose.yml](https://github.com/immich-app/immich/releases/latest/download/docker-compose.yml) file and the [.env](https://github.com/immich-app/immich/releases/latest/download/example.env) configuration file to your local computer.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/fe1f24e59c00473c9eab9ca0542ab50f.webp)

2. Open the downloaded `example.env` file with a text editor. Locate the `UPLOAD_LOCATION` field and change its value to the actual directory path on your NAS where you want to store the photo library data.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/b6d4f853418d460a966efe97044ffbe4.webp)

3. After confirming the changes are correct, save the file.

### Upload and Configure the Environment File

Next, upload the configured files to your NAS.

1. Open the NAS "**Files**" application and navigate to the "**Docker**">"**immich**" folder (if it does not exist, create it manually). Upload the configuration files you prepared to this directory.

2. After the upload is complete, select the `example.env` file and rename it to `.env`.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/62dc27499a59413d9fc316afe6a834b8.webp)

### Can't see the .env file?

Linux systems treat files that start with a dot (.) as hidden by default. If the file seems to disappear after renaming, follow these steps:

● Go to"**Settings**">"**General**" in "**Files**".

● Uncheck "**Start with (.)**".

● Click "**Save**", and the .env file will appear in the file list.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/eb62561dfdb74d1b93bba829361c4867.webp)

## Deploy Immich Using Docker Compose

On the UGOS Pro system, it's recommended to deploy Immich with **Docker Compose**.

This method is ideal for managing multiple containers at once. By using a single YAML file, you can define and start all related services in bulk, greatly simplifying container creation and maintenance.

### Deployment Steps

1. Open the"**Docker**" app, select "**Project**">"**Create**" from the left navigation panel to launch the project creation wizard.

2. In the wizard, choose "**Import from the local computer**" for the Compose configuration, and upload the previously downloaded **immich.yml** file.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/dde9682e919042e689da1ed5bf1f8291.webp)

3. After the import is completed, the system will automatically recognize the service configurations in the YAML file. Click "**Deploy**". The system will then pull the required images and start all related containers automatically.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/bd48ef82fdcc46b38d7d8fa7d15a0d97.webp)

### Verify the Deployment

After deployment completes, check the status of Immich's services at **"Docker">"Container"**:

● If all services show "**Running**", the deployment was successful.

● If any container failed to start, click the container name to view its logs and troubleshoot the cause.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/1a6b52ba38ae497fa7daa966f1287b4a.webp)

## Access and Use the Immich

1. After deployment, access the container through your browser by entering  
`http://NAS_IP:2283` in the address bar. For example, if your NAS IP is 172.17.70.86, enter`http://172.17.70.86:2283` in the browser.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/ccee0686af8a4c8685d74491cfa4b4d4.webp)

> You can find your NAS device's IP address in "Control Panel">"Network">"Network connection".

![](https://file-us.ugreennas.com/admin/article/2026-01-04/52a16ced94cc40598ccfa4a3c2928566.webp)

2. **Create an account:** After Immich is installed and launched, the first user you create will automatically become the administrator. Enter your email, password, and name in sequence, then click "**Sign up**" to complete the account setup.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/da33ae87d6fe41edbb2402fe0bb6878b.webp)

3. Then, use the newly created account and password to complete the login.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/8d0ca60682e0475086ea913b2783dd1f.webp)

4. Before enabling the service, some general settings need to be configured, such as theme, privacy, and storage template settings (disabled by default). Select as needed and click "**Done**" to complete.

● **Theme Settings:** Follow the prompts to set the application's theme. Currently, only Day and Night modes are available.

● **Privacy Settings:** Enable privacy protection if needed.

● **Storage Template Configuration:** This feature is disabled by default. According to the official documentation on [Asset Types and Storage Location](https://immich.app/docs/administration/backup-and-restore/#asset-types-and-storage-locations) , enabling it allows customization of the image storage structure.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/8e5b78d91014417697d8a3b0d8cf1de2.webp)

![](https://file-us.ugreennas.com/admin/article/2026-01-04/5479a915e69e43fb8e5eaa7cebfcc4ac.webp)

5. After the storage template is set up, you can access the Immich user interface. You can choose the corresponding features in the left menu bar to categorize and organize your images or videos. For example:

![](https://file-us.ugreennas.com/admin/article/2026-01-04/852f2d3a408d4db0b810394f41ebf26c.webp)

● In the **Photos** tab, you can perform actions such as uploading photos, sharing, downloading, deleting, and editing photos.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/9ed23ee2370e42fd9b0b770b737f9507.webp)

● In the **Albums** tab, you can perform actions such as manually creating albums, editing albums, or sharing albums with others.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/ea483904b22c4597a8671cee4aed806e.webp)

### Add External Libraries to Immich

You can also add external libraries by moving photos stored on the NAS or previously stored photos to the "**albums**" folder created earlier in the files section. After adding an external library, Immich will automatically recognize it. The steps to add an external library are as follows:

1. In the Immich main interface, click the avatar in the top-right corner, select "**Adminstration**," and then click "**External Libraries.**"

![](https://file-us.ugreennas.com/admin/article/2026-01-04/b4f3a5d6d7b94e34beaded66a959735a.webp)

2. In the external libraries interface, click "**Create Library,**" select the library owner, and click "**Create.**"

![](https://file-us.ugreennas.com/admin/article/2026-01-04/3732bcb39f55493d99aca3ba3292ccb5.webp)

3. After the creation is successful, click the "More Options" button on the right, and select "**Edit Import Paths**."

![](https://file-us.ugreennas.com/admin/article/2026-01-04/cf9851387021421796fe873918ec0730.webp)

![](https://file-us.ugreennas.com/admin/article/2026-01-04/07a53c5ae9a3462a9814359410de37c5.webp)

4. In the pop-up "**Add import path**" window, enter the path: `/usr/src/app/External Albums`, and then click "**Add**."

![](https://file-us.ugreennas.com/admin/article/2026-01-04/3261471f0d4c467c9e502bb90c1a7208.webp)

5. After adding, the interface will display a ☑ icon indicating successful addition, confirming the path was entered correctly. Then, click "**Save**" to continue.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/1ba10b7635ba47239f17d00b912e6e20.webp)

6. After successfully adding the external library, you can view the photos stored on the NAS in the Immich album.

### Install Models for Immich

In the Immich main interface, click "**Administration**">"**Settings**">"**Machine Learning Settings**" to view the currently supported intelligent models or install models based on your needs. For more details, please refer to [the Immich official tutorial.](https://docs.immich.app/overview/quick-start/)

**Note**: Due to the large size of the models, you will need to use a proxy to facilitate the download.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/6ca2cd58b81740179f4f19852b72bf88.webp)

### Log in and Upload/Synchronize Photos Using the Mobile App

Download the Immich app on your mobile device; it is available for both iOS and Android systems.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/cb1a7b80dc7e4e9b952384a08f07c06b.webp)

**Note**: Non-public network users need to use it within the local area network. For more features and detailed usage instructions, please refer to [the Immich official documentation.](https://immich.app/docs/overview/quick-start/)

## FAQs

### Q: How to obtain the actual NAS folder path and mount it to a Docker container?

When using Docker, you may need to mount NAS folders to a container so that the container can access data stored on the NAS. Refer to [Get the real path of the NAS folder and mount it to the Docker container](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTkzMCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo2MTEsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==) for detailed instructions.

## Notes

● The images used in this tutorial are developed and maintained by third parties. This tutorial is for reference only. UGREEN is not responsible for risks caused by improper operations, software vulnerabilities, or image updates, such as file issues or data leaks. Please choose trusted images to ensure system and data security.

● Container file paths can be customized. When accessing via a web browser, container ports must match the host ports, and local ports of different containers must not conflict.

● Container web pages are accessible only when using "bridge" network mode.

● This guide only covers how to set up the environment. For usage instructions or gameplay, please search online. For configuration changes and bug fixes, follow the official updates.

● It is recommended to store the Docker configuration directory on an SSD to avoid performance issues caused by mechanical hard drives.
