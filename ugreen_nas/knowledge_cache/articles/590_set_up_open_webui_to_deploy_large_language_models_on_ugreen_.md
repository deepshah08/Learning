# Set up Open WebUI to deploy large language models on UGREEN NAS

> **Article ID**: `590`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Set up Open WebUI to deploy large language models on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/590  

---

## **Application Overview**

Open WebUI is an extensible, powerful, and user-friendly self-hosted web interface designed to run completely offline. It is ideal for developers, researchers, and privacy-conscious individuals or teams. The platform supports multiple LLM frameworks, including Ollama and OpenAI-compatible APIs. For more details, please refer to [the official Open WebUI documentation.](https://docs.openwebui.com/)

### **Key Features of Open WebUI**

* **Easy Setup:** Supports Docker and Kubernetes installation with convenient image management.
* **API Integration:** Compatible with Ollama and OpenAI APIs, custom API URLs, and supports multiple LLM services like LMStudio and OpenRouter.
* **Granular Permission Management:** Supports role-based and permission grouping to ensure user security and optimize the management experience.
* **Responsive Design:** Adapts to desktops, laptops, and mobile devices, with PWA offline support.
* **Markdown and LaTeX Support:** Rich formatting features to enhance the interaction experience.
* **Hands-free Voice/Video Calls:** Supports dynamic real-time conversations.
* **Model Generator:** Easily create and customize models via the interface.
* **Native Python Calls:** Integrated code editor for easy expansion of LLM functionality.
* **RAG Integration:** Supports document interaction and retrieval-augmented generation.
* **Web Search and Browsing:** Integrates search engine results and web content into conversations.
* **Image Generation:** Supports APIs like AUTOMATIC1111 and OpenAI DALL-E.
* **Multi-model Conversations:** Enables parallel use of multiple models to improve interaction efficiency.
* **Role-Based Access Control (RBAC):** Ensures secure access to models and data.
* **Multilingual Support:** Supports multiple languages, with contributions welcomed for translations.
* **Plugins and Pipelines Integration:** Supports custom logic and feature extensions.
* **Continuous Updates:** Regularly releases new features and fixes.

## **Deploying Containers with Docker Compose**

On the UGOS Pro system, it is recommended to use the project’s Docker Compose for quick container deployment, which is ideal for scenarios that require managing multiple containers simultaneously. This method simplifies container deployment and management. Below are the detailed steps for deploying Open WebUI using Docker Compose.

Click to learn more: [What is a project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### **Access the Docker Project Interface**

In the UGOS Pro system, open the Docker application, click [Project] > [Create], and start the project creation wizard.

### **Configure the Docker Compose File**

In the project creation wizard, upload the following Docker Compose configuration file for Open WebUI:

```
services:
  open-webui:
    container_name: open-webui
    image: ghcr.io/open-webui/open-webui:ollama # Image name
    restart: always # Restart policy
    ports:
      - 3000:8080 # Web service access port
    volumes:
      - ./ollama:/root/.ollama # Storage for ollama-related data
      - ./open-webui:/app/backend/data # Storage for the Web UI backend data
```

### **Parameter Explanation**

image：Specifies the Docker image version to be used (in this case,  `ollama`).

restart：Container restart policy, where `always`means the container will automatically restart if it stops or crashes.

ports：Web service access port, mapping port 3000 on the NAS to port 8080 in the container.

volumes：Maps NAS file directories to container paths.

`./ollama:/root/.ollama`：The NAS storage directory`./ollama` is mapped to the container's internal path `/root/.ollama`to store ollama-related data. The part before the colon is the NAS storage path.

`./open-webui:/app/backend/data`：The NAS storage directory `./open-webui` is mapped to the container's internal path `/app/backend/data`to store the Web UI backend data files.

**Note**:

* `./` refers to the current directory where the Docker Compose file is located.
* The path before the colon is the NAS storage path, and the path after the colon is the mapping path inside the container.

Related Guide

[[FAQ] How to correctly represent volumes mount paths in the Docker Compose configuration file?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjoxNDQ3LCJhcnRpY2xlSW5mb0lkIjo0ODcsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIn0=)

### **Deploy the Project**

After uploading the configuration file, click [Deploy], and the system will automatically pull the image and start the container.

Once the deployment is complete, access the Open WebUI interface by visiting the following address in your browser:

```
http://<NAS_IP>:3000
```

Please replace `<NAS_IP>` with the actual IP address of your NAS, for example:`http://192.168.22.153:3000`.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250428/6236a7f0-9305-4327-b745-3ff13049f672.png)

## **User Guide**

To access the Open WebUI web interface, follow these steps:

1. Open your browser and visit the deployment address to access the login page.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250428/bdb3c238-c656-4f3b-bcef-9f7828a357aa.png)

2. On your first visit, you will need to create an administrator account by setting a username, email, and password.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250428/16b86de9-b467-4cf2-88fc-6921282233d6.png)

3. Log in using the newly created account.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250428/0956c283-b053-43f4-86d6-41297884f992.png)

**Note**: After deployment, the page may initially show an internal error or a connection refusal. Please wait a few minutes for the page to load.

### **Solution for Blank Page Issues**

When logging into Open WebUI for the first time, you may encounter a blank page. This is due to a delay while the system waits for the OpenAI model to return data. If you do not want to wait for the loading process, you can resolve the issue by disabling the OpenAI API. Note that disabling the OpenAI API should only be done after the interface has successfully loaded for the first time.

Solution Steps:

1. During the first login, the system will attempt to connect to the OpenAI model and load the related data, which may cause a brief blank page. Please be patient until the loading completes.
2. Once logged in and the loading is complete, go to the "Admin Panel".
3. In the "Admin Panel", click "Settings" in the left menu.
4. In the "Settings" page, select the **"**Connections" option.
5. On the "Connections" settings page, you will see the "OpenAI API" configuration option.
6. Disable the "OpenAI API" option. Once disabled, Open WebUI will no longer wait for the OpenAI model's return data on the next load.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250428/5dee1ef7-6fa5-4707-ad5d-89471a809fc4.png)

You can also check the relevant log files to determine if the loading process is proceeding normally. The steps are as follows:

1. Go to the Docker application in UGOS Pro.
2. Click [Container] > Select the Open WebUI container > Click [Log].
3. Check the logs for progress information related to model loading, such as "get\_all\_models" or "Loading models." If the logs show normal loading, wait a few minutes and refresh the interface. If error messages appear, refer to the log information to troubleshoot the issue.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250428/99459403-b4fd-4127-a702-2c7523662877.png)

Check the logs to confirm the loading progress, then wait a few minutes and refresh the page.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250428/f8f14568-d9ee-402e-8209-2715006b54d8.webp)

### **Download and Deploy Models**

1. Open [the Ollama model library](https://ollama.com/search) to view the supported models.
2. Select the desired model and copy the pull command (e.g., `ollama run qwen2.5:7b`).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250428/5f13368b-adf5-4ccb-ab66-91f1732cbd4b.webp)

3. Return to the Docker application in UGOS Pro, go to [Container] > Select the Open WebUI container > Click [Terminal] > Add a new Bash connection.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250428/3b3bcc7e-7406-4d23-a87c-c5df80a0c8c6.png)

4. Paste the pull command in the Bash terminal and wait for the model to download.

```
ollama run qwen2.5:7b
```

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250428/370ac6a7-c563-44c0-bd2d-97577dcb9b5a.png)

5. If "success" is displayed, it indicates that the model has been successfully downloaded. Restart the container.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250428/aeff8397-cf9c-48b6-b563-7452e355855b.png)

6. Log in to Open WebUI and confirm whether the model has been successfully loaded.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250428/b9cd4da8-1eb8-4e05-97c4-25473f43509d.png)

### **Using the Model**

In a new conversation, ask the model to introduce itself, and you should be able to see that it is ready for use.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250428/06588f6c-e26b-4412-8689-faacf33607a6.png)

## **Usage Tips**

Deploying large models will significantly increase the CPU and memory load on the NAS. It is recommended to avoid using it during high-load tasks.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250428/99163b7a-1cb4-4fab-b43d-8c18a09b884f.png)

## **Notes**

Please note that the images used in this tutorial are developed and maintained by third parties. This tutorial is for reference only. UGREEN does not bear any risks caused by improper user operations, third-party software vulnerabilities, or image updates, including but not limited to:

· Third-party images may cause accidental modification or deletion of files in your UGOS Pro system.

· Using insecure images may result in data being uploaded to third-party servers, posing privacy and data leakage risks.

· To ensure system stability and data security, please carefully choose third-party images from trusted sources.

**Other notes:**

1. The file/folder paths for containers are provided for reference; you can create them according to your personal preferences.

2. The container's web access port and local port should be the same. If there is a conflict, change it to an unused port. Local ports for containers cannot be the same; port conflicts will prevent the container from starting.

3. The container’s web link is only accessible in bridge mode.

4. The image only provides the setup tutorial; for specific usage methods and advanced features, please search online for references.

5. The image is developed by a third party, and for configuration changes and bug fixes, please refer to relevant official information.

6. It is recommended to store Docker configuration directories on an SSD to avoid performance issues caused by mechanical hard disks.
