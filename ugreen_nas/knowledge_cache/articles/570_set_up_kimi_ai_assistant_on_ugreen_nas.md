# Set up Kimi.AI Assistant on UGREEN NAS

> **Article ID**: `570`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Set up Kimi.AI Assistant on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/570  

---

## App Overview

Kimi.AI is a domestic AI assistant developed by Moonshot AI Company. Based on a multi-purpose large language model, it provides various services to help improve work and study efficiency. Kimi.AI can be used in various scenarios such as text processing, conversational Q&A, knowledge management, and more. It is a powerful AI tool.

![](https://file-us.ugreennas.com/admin/article/2025-08-28/e2a89b4eac9f4e988b61d1b1736d5273.webp)

GitHub Project URL: [KIMI AI Free Service](https://github.com/LLM-Red-Team/kimi-free-api)

## Deploying Containers Using Docker Compose

On the UGOS Pro system, it is recommended to use Docker Compose for quick container deployment, especially for scenarios where multiple containers need to be managed simultaneously. This method simplifies container deployment and management. Below are the detailed steps for deploying Kimi.AI using Docker Compose.

Click to learn: [What is a project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### Access the Docker Project Interface

In the UGOS Pro system, open the Docker app, click [Project] > [Create], and start the project creation wizard.

### Configure the Docker Compose File

In the project creation wizard, upload the following Docker Compose configuration file for Kimi.AI:

```
services:
  kimi-free-api:
    container_name: kimi-free-api
    image: vinlic/kimi-free-api:latest # Image Name
    restart: always # Container Restart Policy
    ports:
      - "8011:8000" # Web Interface Port
    environment:
      - TZ=Asia/Shanghai # Container Time Zone
```

### Parameter Explanation

Below are the explanations for the key parameters:

**image:** Specifies the Docker image, with `latest` indicating the use of the latest version of the image.

**restart:** Defines the container restart policy, with `always` meaning the container will automatically restart when it stops.

**ports:** Defines the mapping between the container’s internal port and the NAS port.

● `8011:8000` means that NAS port 8011 is mapped to container port 8000, used to access the web application interface.

**environment：**

`TZ=Asia/Shanghai`：Sets the container's time zone to Shanghai, China (Asia/Shanghai). You can adjust this based on your local time zone, such as the U.S. time zone (America/New\_York) or the European time zone (Europe/London).

Note:

● Before deployment, please refer to the official documentation for vinlic/kimi-free-api image. If there are specific deployment guidelines or requirements for this image, please follow the official instructions or README file.

● In the configuration file, `./` represents the current directory path. The mapping between the NAS local path and the container internal path should be adjusted as needed.

### Deploy the Project

After uploading the configuration file, click [Deploy], and the system will automatically pull the image and start the container.

Once the deployment is complete, access the Kimi.AI interface through the following address in your browser:

```
http://<NAS_IP>:8011
```

Please replace `<NAS_IP>` with the actual IP address of your NAS, for example: `http://192.168.22.153:8011`.

![](https://file-us.ugreennas.com/admin/article/2025-08-28/13896eb415974ec39d18cac80609b78a.webp)

## Instructions for User

To access the MKVtoolnix web interface, open your browser and go to the deployment address to reach the login page.

### Get API Token

1. Go to [the Kimi official website](https://kimi.ai/) to register and log in.

2. Start a conversation and press `F12` to open the browser developer tools.

● **For Chrome browser:** Select "Application" > "Local Storage," find the `refresh_token` and copy it for later use.

![](https://file-us.ugreennas.com/admin/article/2025-08-28/e9d25f562d724914b5e7039294a5d666.webp)

● **For Edge browser:** Select "Application" > "Local Storage", find the `refresh_token`, and copy it for later use.

![](https://file-us.ugreennas.com/admin/article/2025-08-28/caec7e6d5bca4611afee446a1c0411f4.webp)

### Multiple Account Access

Free users are limited to 30 long-text Q&A sessions every 3 hours (short-text Q&A is unlimited).

You can achieve multi-account polling by providing multiple `refresh_token`, formatted as follows:

```
Authorization: Bearer TOKEN1,TOKEN2,TOKEN3
```

The service will automatically select an account from the provided tokens for the request.

### Install ChatGPT-Next-Web

After running `kimi-free-api`, you can access the API through clients like LobeChat, NextChat, Dify, etc. Below is the installation guide for using ChatGPT-Next-Web:

1. Go to the Docker image repository, search for `yidadaa/chatgpt-next-web` , and download the latest version of the image.

2. After the download is complete, create a container in Docker:

● **Container name:** Custom name (e.g., `chatgpt-next-web`）.

● **E****nvironment variable configuration:**

```
OPENAI_API_KEY=<refresh_token>
BASE_URL=http://<NAS_IP>:8011
CUSTOM_MODELS=-all,+kimi
```

![](https://file-us.ugreennas.com/admin/article/2025-08-28/5eb0575d3f6c4d65a4ffc41cbdcac613.webp)

● **Port Mapping:** Choose an appropriate port mapping, for example, `3011:3000`.

3. If you have already installed ChatGPT-Next-Web, simply modify the following environment variables:

● **OPENAI\_API\_KEY:** Fill in the obtained `refresh_token` value.

● **BASE\_URL:** Fill in the address and port number of the `kimi-free-api` service.

● **CUSTOM\_MODELS:** Update to `-all,+kimi`.

4. Once the configuration is complete, start the container. Access it through the browser: `http://<NAS_IP>:3011`

5. After entering the settings, you will see that the model has been set to `kimi`.

![](https://file-us.ugreennas.com/admin/article/2025-08-28/f47f9b6289d2434fa4d900f3ae86bc0c.webp)6. Click on "New Chat" on the left to start a chat conversation.

![](https://file-us.ugreennas.com/admin/article/2025-08-28/ae0ddfc55aa1447ebf12b00601e5a1c5.webp)

## Notes

Please note that the image used in this tutorial is developed and maintained by a third party, and the tutorial is for reference only. UGREEN does not assume any risks arising from improper user operations, third-party software vulnerabilities, or image updates, including but not limited to:

· Third-party images may cause accidental modification or deletion of files in your UGOS Pro system.

· Using insecure images may lead to data being uploaded to third-party servers, which poses privacy and data leakage risks.

· To ensure system stability and data security, please carefully select third-party images from trusted sources.

**Additional Notes:**

1. The file/folder paths for the container are for reference only. You can create them according to your personal preferences.

2. The container's web access port and local port should match. If there is a conflict, change it to an unused port. Local ports between containers cannot be the same; port conflicts will prevent the container from starting.

3. The web link for the container is only accessible in bridge mode.

4. The image only provides setup instructions. For specific usage methods and advanced configurations, please search online for further information.

5. The image is developed by a third party. For configuration changes and bug fixes, please follow the official announcements.

6. It is recommended to store Docker configuration directories on an SSD to avoid mechanical hard disks affecting system performance.
