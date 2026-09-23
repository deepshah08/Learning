# The Tutorial for Locally Deploying the DeepSeek-R1 Large Language Model on UGREEN NAS

> **Article ID**: `589`  
> **Category**: `Application Guide > Docker > Docker Gameplay > The Tutorial for Locally Deploying the DeepSeek-R1 Large Language Model on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/589  

---

## Introduction to DeepSeek

DeepSeek is an inference model developed by Hangzhou DeepSeek Artificial Intelligence Basic Technology Research Co., Ltd. (established on July 17, 2023). This model utilizes reinforcement learning for post-training to enhance its inference capabilities, particularly excelling in complex tasks such as mathematics, coding, and natural language reasoning. On January 20, 2025, DeepSeek officially released the DeepSeek-R1 model and simultaneously open-sourced the model weights. Before deploying DeepSeek, it is necessary to install Ollama, a large language model framework that can be considered the host for AI models. If a visually appealing UI is required, additional applications need to be installed. In this tutorial, we will deploy the OpenWebUI application to run the DeepSeek-R1 model.

OpenWebUI is an extensible, feature-rich, user-friendly self-hosted web interface designed for completely offline operation. It supports multiple LLM runners, including Ollama and OpenAI-compatible APIs. For more details, please refer to [the OpenWebUI official documentation.](https://docs.openwebui.com/)

## Deploying OpenWebUI Container with Docker Compose (Integrating Ollama)

On the UGOS Pro system, it is recommended to use the project’s Docker Compose for quick container deployment, especially when managing multiple containers simultaneously. This method simplifies container deployment and management. Below are the detailed steps for deploying OpenWebUI using Docker Compose.

### Accessing the Docker Project Interface

On the UGOS Pro system, open the Docker application, then click [Project] > [Create] to start the project creation wizard.

### Configuring the Docker Compose File

In the project creation wizard, copy the following Docker Compose configuration file for OpenWebUI:

```
services:
  open-webui:
    container_name: open-webui
    image: ghcr.io/open-webui/open-webui:ollama  # Image name
    #It is recommended to add an accelerator https://docker.nju.edu.cn/
    restart: always  # Restart policy
    ports:
      - "3000:8080"  # Web service access port
    volumes:
      - ./ollama:/root/.ollama  # Store data related to ollama
      - ./open-webui:/app/backend/data  # Store backend data for the Web UI
```

**Parameter Explanation**

|  |  |
| --- | --- |
| **Parameter** | **Explanation** |
| **image** | Specifies the container image version as ghcr.io/open-webui/open-webui:ollama, which integrates the Ollama service. If the download speed is slow, it is recommended to add an accelerator by configuring:加 <https://docker.nju.edu.cn/>。 |
| **restart** | Sets the restart policy to always, ensuring that the container will automatically restart if it crashes or stops, maintaining continuous service operation. |
| **ports** | Port mapping: Maps port 3000 on the NAS to port 8080 in the container. The Web UI can be accessed via http://NAS\_IP:3000. |
| **volumes** | Data storage mapping to ensure data persistence: |
| ./ollama:/root/.ollama: Maps the local ./ollama directory on the NAS to /root/.ollama inside the container, storing Ollama data. |
| ./open-webui:/app/backend/data: Maps the local ./open-webui directory on the NAS to /app/backend/data inside the container, storing OpenWebUI backend data. |

**Notes:**

● ./ represents the directory where the Docker Compose file is located.

● The path before the colon is the storage path on the NAS, and the path after the colon is the mapped path inside the container.

● **Image Source**: The ghcr.io/open-webui/open-webui:ollama image is used. This image integrates both OpenWebUI and Ollama, so there is no need to run the Ollama service separately. The system will automatically handle the startup and integration.

● **Port Settings**: The default port for OpenWebUI is 8080, but it can be adjusted using the ports parameter. In this case, it is mapped to port 3000, and the access URL is http://NAS\_IP:3000. The default port for Ollama is 11434, but it does not need to be exposed since the integration is handled internally within the image, allowing OpenWebUI to directly access the Ollama service.

### Deploying the Project

After copying the configuration file, click [Deploy]. The system will automatically pull the image and start the container.

![](https://file-us.ugreennas.com/admin/article/2025-08-27/57c4b5132a594001b969a0b03a8602a5.webp)

![](https://file-us.ugreennas.com/admin/article/2025-08-27/fb878d147023414d8dd8f5288db4ca28.webp)

## Accessing Open WebUI

To access the Open WebUI web interface, follow these steps:

1. Open a browser within the local network and visit http://NAS\_IP\_address:port\_number (for example: http://172.17.70.69:3000).

![](https://file-us.ugreennas.com/admin/article/2025-08-27/d398c2ac71a840f4871df19d53a4bafb.webp)

2. For first-time access, you will need to create an administrator account by setting a username, email, and password.

![](https://file-us.ugreennas.com/admin/article/2025-08-27/d116da6feaeb47729e1710e2c26663cf.webp)

3. Log in using the newly created account.

![](https://file-us.ugreennas.com/admin/article/2025-08-27/ccdec079c78e402791ddaefd4ef0e2ed.webp)

4. Once logged in successfully, you will enter the main interface.

![](https://file-us.ugreennas.com/admin/article/2025-08-27/0aa3454749b94570a63e3df0b375a50d.webp)

**Handling Blank Screen Issue**

When logging into Open WebUI for the first time, you may encounter a blank screen. This happens because the system is waiting for a response from the OpenAI model in the background, which causes a delay. If you prefer not to wait for the loading process, you can resolve this issue by disabling the OpenAI API. Please note: You should disable the OpenAI API only after the interface has successfully loaded for the first time.

![](https://file-us.ugreennas.com/admin/article/2025-08-27/1bbffc41441d426fb1b169e379e22a68.webp)

Method 1: After the Open WebUI interface has successfully loaded for the first time, you can disable the OpenAI API option by going to [Admin Panel] > [Settings] > [Connections]. Once disabled, simply refresh the page to resolve the issue.

![](https://file-us.ugreennas.com/admin/article/2025-08-27/7fbc292e23354c95bc4b66c849b2f50e.webp)

Method 2: You can also check the relevant log files to determine whether the loading process is proceeding normally. Here's how to do it:

● Open the Docker application on UGOS Pro.

● Click [Container] > Select the Open WebUI container > Click [Log].

● Check the logs for any progress information related to model loading, such as "get\_all\_models" or "Loading models." If the logs indicate that the model is loading normally, wait for 1-2 minutes, and the page will automatically refresh and return to normal；If you encounter error messages, refer to the logs for troubleshooting the issue.

![](https://file-us.ugreennas.com/admin/article/2025-08-27/ca442264a6e1487caec4e2c2bd0e46ef.webp)

## Downloading and Using the Deepseek-R1 Model

1. After logging into Open WebUI, enter the model name (for example: ollama run deepseek-r1:1.5b) in the search box located in the upper-left corner. Click on the search result to start the download.

![](https://file-us.ugreennas.com/admin/article/2025-08-27/c5cb12ce3c49428ea536af1145bd76ea.webp)

2. In the new conversation, enter "hello world!" or any other question, and you should see that the model is now working properly.

![](https://file-us.ugreennas.com/admin/article/2025-08-27/8744c6da56174ebfa9bd64c688a1f735.webp)

Please Note: Deploying large models will significantly increase the CPU and memory load on the NAS. It is recommended to avoid using it during high-load tasks.

**The minimum hardware requirements for different versions of the DeepSeek-R1 model are as follows：**

You can choose the model size based on your personal NAS hardware configuration. In this tutorial, we have selected the 1.5B model.

![](https://file-us.ugreennas.com/admin/article/2025-08-27/23d306659aab45488f61609e2b9e1f22.webp)

## Notes

Please note that the image in this tutorial is developed and maintained by a third party. The tutorial is for reference only. UGREEN is not responsible for any risks arising from improper user operations, third-party software vulnerabilities, or image updates, including but not limited to:

· Third-party images may cause accidental modification or deletion of files on your UGOS Pro system.

· Using insecure images may result in data being uploaded to third-party servers, posing privacy and data leakage risks.

· To ensure system stability and data security, please carefully choose third-party images from trusted sources.

**Additional Notes：**

1. The container file/folder paths are for reference only. You can create them according to your personal preferences.

2. The container port for web access and the local port should match. If there's a conflict, change it to an unused port. Local ports between containers must be different; port conflicts will prevent the container from starting.

3. The container's web link is only accessible in bridge mode.

4. The image provides a setup tutorial; for detailed usage and advanced features, please refer to online resources.

5. The image is developed by a third party; for configuration changes and bug fixes, please follow the relevant official information.

6. It is recommended to store the Docker configuration directory on an SSD to avoid performance issues caused by mechanical hard disks.

## Related Links

● [**How to correctly represent volumes mount paths in the Docker Compose configuration file?**](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTQ0NywidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0ODcsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

● [What is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)
