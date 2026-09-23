# Setting up Cloud Backup on UGREEN NAS

> **Article ID**: `545`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Setting up Cloud Backup on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/545  

---

## App Introduction

Cloud Backup is a WeChat cloud backup application that allows users to back up WeChat data to a server and access it via a browser. Users can browse and search their data just like using the WeChat web version. Although sending messages and using certain special features are not available, most other functions can be performed on Cloud Backup.

![](https://file-us.ugreennas.com/admin/article/2025-08-29/02e6680c9edc48c0a2fc598bf56c779d.webp)

### Why Choose Cloud Backup Over WeChat's Built-in Backup?

● **Convenient Data Access:** Even if data is deleted from the phone, it can still be accessed remotely through a PC browser.

● **Multi-Account Management:** Easily switch between and check backup information for multiple WeChat accounts without frequent logins.

● **No Need for WeChat Login:** Even if the account is banned, historical messages can still be viewed, ensuring the availability of data.

● **Data Security & Durability:** Backup data to a server or NAS device for long-term storage and protection, preventing data loss due to device damage or theft.

### Cloud Backup Official Information

● GitHub: [likeflyme/cloudbak: WeChat cloud backup, supports backing up to servers, Docker, and NAS, with web access.](https://github.com/likeflyme/cloudbak)

● Official Website: [Cloud Backup](https://www.cloudbak.org/)

## Deploying the Container with Docker Compose

On the UGOS Pro system, it is recommended to use Docker Compose for quick deployment of containers, especially in scenarios that require managing multiple containers simultaneously. This method simplifies the deployment and management of containers. Below are the detailed steps to deploy Cloud Backup using Docker Compose.

Click to learn more: [What is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### Enter the Docker Project Interface

In the UGOS Pro system, open the Docker app, click on [Project] > [Create], and start the project creation wizard.

### Configure the Docker Compose File

In the project creation wizard, upload the following Docker Compose configuration file for Cloud Backup:

```
services:
    cloudbak:
        container_name: cloudbak
        image: pub.tcp.mk/likeflyme/cloudbak # Image Name
        restart: always                      # Restart Policy
        volumes:
            - ./app/data:/app/data           # Directory to Store WeChat Data Backups
        ports:
            - 9527:9527                      # WEB Service Access Port
```

### Parameter Explanation

**image:** Specifies the Docker image.

**restart:** Defines the container restart policy.`always`means the container will automatically restart if it stops.

**volumes:** Maps the NAS local folder to the container path.

`./app/data:/app/data`: Mounts the `app/data`folder from the NAS to the `/app/data` path inside the container. The path before the colon is the location in the NAS storage space and can be modified as needed.

**ports:** Maps the NAS port 9527 to the container port 9527. If there is a port conflict, you can change the NAS port number before the colon. For example, you can change `9527:9527` to `9528:9527`, so external access will use port 9528, while the container still uses port 9527 internally.

**Note**:

`./` refers to the directory where the current Docker Compose file is located.

The path before the colon is the local NAS path, and the path after the colon is the path inside the container.

**Related Reading**

[[FAQ] How to correctly represent volumes mount paths in the Docker Compose configuration file?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTQ0NywidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0ODcsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

### Deploy the Project

After uploading the configuration file, click [Deploy], and the system will automatically pull the image and start the container.

Once the deployment is complete, access the Cloud Backup interface by visiting the following address in your browser:

```
http://<NAS_IP>:9527
```

Please replace `<NAS_IP>` with the actual IP address of your NAS, for example:`http://192.168.22.153:9527`.

![](https://file-us.ugreennas.com/admin/article/2025-08-29/e9b2a6cb76a447d1a83d0684ab4b24f6.webp)

## Instructions for User

Once the container is up and running, you can access the Cloud Backup web interface through your browser to complete the setup and management. Here are the detailed steps:

1. On the initial screen, create an account by entering your username, email address, and password. Click "Start" to complete the account registration.

![](https://file-us.ugreennas.com/admin/article/2025-08-29/01fae26526494e28be2965361cacc475.webp)

2. Enter the account and password you just created on the login screen.

![](https://file-us.ugreennas.com/admin/article/2025-08-29/f12322918b134aad84064f6c836d9e90.webp)

3. Upon first login, the interface will appear blank as no data has been uploaded yet.

![](https://file-us.ugreennas.com/admin/article/2025-08-29/a157c7cb297b4bdebe8120281487b2c0.webp)

4. You can follow the steps below to download and use the Windows client to back up local data to the server.

### Data Backup Using the Windows Client

1. The client currently supports only the Windows operating system.

2. **Client download link:** [cloudbak-desktop.0.1.0.zip](https://wwij.lanzout.com/imkw02ant6ri)

3. After downloading, unzip the file and double-click to run`CBakWeChatDesktop.exe`。

![](https://file-us.ugreennas.com/admin/article/2025-08-29/57877ca84540466fb32de922495bf96a.webp)

### Configuring the Client to Connect to the Cloud Backup Server

1. After launching the client, you'll need to configure the server information for the first run:

Enter the server address (e.g., `http://192.168.2.185:9527`).

Input the username and password, which should match the account created in the Web interface.

![](https://file-us.ugreennas.com/admin/article/2025-08-29/e2e9d0ff98064bc79549370878ad344a.webp)

2. After logging in, you will enter the main interface of the client.

### Backup Chat History

After logging into the client, click [Add session]:

Make sure you are logged into the WeChat desktop client.

Enter a session name (e.g., "Personal WeChat") to distinguish between multiple sessions.

In the window, select the WeChat process and click "Add" to complete the configuration.

![](https://file-us.ugreennas.com/admin/article/2025-08-29/8a77bce730ad4620b8fb017f58c03dfb.webp)

After the session is successfully added, click the session name in the session list on the left.

Click the [Sync] button at the bottom right (Note: You need to exit the WeChat process at this point).

![](https://file-us.ugreennas.com/admin/article/2025-08-29/ada159e82403460ba7f94dc984992d2f.webp)

The client allows you to view the synchronization progress in real time.

![](https://file-us.ugreennas.com/admin/article/2025-08-29/edaae8b64fb140d0acc50935936e47a3.webp)

Once the synchronization is complete, log in to the Cloud Backup web interface to view the synchronized data. The following is a screenshot of the Cloud Backup web interface for accessing chat records.

![](https://file-us.ugreennas.com/admin/article/2025-08-29/79d72e589d6d474ebde47aee45799b9b.webp)

### Multiple Account Backup

To back up another WeChat account, switch to the corresponding account and repeat the above steps.

### Backup Mobile Chat History

Open WeChat on your mobile phone, go to **"Me" > "Settings" > "Chats" > "Chat History Migration and Backup".**

Select **"Migrate to PC WeChat"**:

Note: The mobile phone and PC need to be on the same local network. After logging into PC WeChat, the chat history migration will be completed.

Once the migration is complete, start the Cloud Backup client and repeat the steps in [Backup Chat History] to complete the synchronization.

### Solution for Unsupported Versions

When adding WeChat data, an error may occur due to the client's lack of support for certain WeChat versions.

![](https://file-us.ugreennas.com/admin/article/2025-08-29/3a1ee54499154053ab2cc78b02d948cd.webp)

You can modify the `version.json` file. Open the `version.json` file located in the client installation directory.

![](https://file-us.ugreennas.com/admin/article/2025-08-29/37af2bf81c5a41998a3421989f9cf50e.webp)

Add the supported version numbers in the following format:

```
,
  "3.9.11.17": [
    93550360,
    93551696,
    93550168,
    0,
    93551632
  ]
```

![](https://file-us.ugreennas.com/admin/article/2025-08-29/f549944387b84fadb3e2e03f1696a6f6.webp)

You can obtain the corresponding version number using one of the following two methods:

● Method 1: [Click here to get it.](https://github.com/xaoyaoo/PyWxDump/blob/master/pywxdump/WX_OFFS.json)

● Method 2: [Obtain it via CE.](https://github.com/xaoyaoo/PyWxDump/blob/master/doc/CE%E8%8E%B7%E5%8F%96%E5%9F%BA%E5%9D%80.md)

After saving the file, restart the client and add the session again.

## Notes

Please note that the images used in this tutorial are developed and maintained by third parties. This tutorial is for reference purposes only. UGREEN is not responsible for risks arising from improper user operations, third-party software vulnerabilities, or image updates, including but not limited to:

· Third-party images may lead to accidental modification or deletion of files in the UGOS Pro system.

· Using insecure images may cause data to be uploaded to third-party servers, posing risks of privacy breaches and data leaks.

· To ensure system stability and data security, please carefully choose third-party images from trusted sources.

**Additional Notes:**

1. The file/folder paths in the container are for reference only. You can create them according to your preferences.

2. The web-accessible container port should match the local port. If there is a conflict, change to an unused port. Containers must not have the same local port, as port conflicts will prevent the container from starting.

3. The container's web link is only accessible in bridge mode.

4. The image only provides setup instructions. For detailed usage methods and advanced functionalities, please search online for references.

5. The image is developed by a third party. For specific configuration changes and bug fixes, please pay attention to the official information.

6.It is recommended to store Docker configuration directories on an SSD to avoid performance issues caused by mechanical hard disks.
