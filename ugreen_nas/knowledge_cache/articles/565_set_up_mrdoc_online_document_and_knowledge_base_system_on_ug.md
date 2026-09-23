# Set up MrDoc Online Document and Knowledge Base System on UGREEN NAS

> **Article ID**: `565`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Set up MrDoc Online Document and Knowledge Base System on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/565  

---

## **Introduction to MrDoc Document**

MrDoc (MrDoc Document) is an open-source online document and knowledge base system. It is a lightweight yet powerful tool. For small teams that need to maintain internal documentation, build product manuals, write tutorials, or establish a knowledge base, it is a highly practical choice.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250430/50e9dfaf-d40d-42fc-96e6-79b759a4d8ce.png)

## **Deploy Containers Using Docker Compose**

On the UGOS Pro system, it is recommended to use the project Docker Compose for quick container deployment, which is ideal for scenarios where multiple containers need to be managed simultaneously. This method simplifies the deployment and management of containers. Below are the detailed steps for deploying MrDoc Document using Docker Compose.

Click to learn more: [What is a project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### **Access the Docker Project Interface**

In the UGOS Pro system, open the Docker app, click on [Project] > [Create], and start the project creation wizard.

### **Configure the Docker Compose File**

In the project creation wizard, you will need to upload the Docker Compose configuration file. Below is the example configuration for MrDoc Document:

```
services:
    mrdoc-alpine:
        container_name: mrdoc   
        image: jonnyan404/mrdoc-alpine:latest
        restart: always #Container restart policy, "always" means the container will automatically restart when it stops or crashes.
        volumes:
            - ./config:/app/MrDoc/config # Configuration files
            - ./media:/app/MrDoc/media # By default, MrDoc searches the media directory for user-uploaded media files (images, attachments, etc.).
        ports:
            - 10086:10086  # Web service access port for MrDoc Document
```

### **Parameter Explanation**

**image：**Specifies the Docker image and its version to use. `latest` means pulling the latest version.

**restart**：Defines the container restart policy. `always`means the container will automatically restart when it stops or crashes.

**volumes：**

`./config:/app/MrDoc/config`

`./` refers to the directory where the Docker Compose file is located. This mounts the host machine's `./config` directory to the container's `/app/MrDoc/config` directory, where all the configuration files are stored.

`./media:/app/MrDoc/media`

By default, MrDoc looks for user-uploaded media files (images, attachments, etc.) in the `media` directory. The `./media` path can be adjusted according to the actual storage location.

**Related Reading**

[[FAQ] How to correctly represent volumes mount paths in the Docker Compose configuration file?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTQ0NywidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0ODcsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

**ports：**Maps the host machine's port 10086 to the container's port 10086. This is the web service access port for MrDoc Document.

## **Deploy the Project**

After confirming that the configuration file is correct, click the [Deploy Now] button. The system will automatically pull the image and start the container. Once the deployment is complete, you can access the MrDoc Document web login interface through your browser at `http://<NAS_IP>:10086`(e.g.,`http://192.168.22.153:10086`).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250430/5b166193-f7e2-4efd-8c3b-a2265f634c6d.png)

## **Access the MrDoc Document Web Interface**

To access the MrDoc Document web interface, please follow these steps:

1. **Access the Web Login Interface**  
   In your browser, enter the address`http://<NAS_IP>:10086`, replacing`<NAS_IP>` with the actual IP address of your NAS device. After entering the address, press Enter to access the MrDoc Document web login interface.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250430/8b052c01-4bd5-43be-b389-0ea084ea6f00.png)

1. After entering the login interface, click the "Login" button in the top right corner of the page. The default administrator username is `admin`. For the first installation, the administrator password can be found in the container logs, with the keyword `pwd`.Use this information to log in.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250430/1068d657-8dff-4c31-9935-5fa1c0faf253.png)

2. After successfully logging in, for security reasons, it is recommended to change the password as soon as possible. Click on the account in the top right corner of the page, select "Change Password," and follow the prompts to proceed.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250430/cf637e2d-6f82-45db-8064-477b46b67907.png)

3. After logging in, you can quickly create new documents, spreadsheets, or collections by clicking the "New" button. Select the appropriate file type to create based on your needs.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250430/e050a847-9e28-4bd3-818a-9ce17f8a0578.png)

4. After logging in, you can click on the account in the top right corner of the page to enter your personal dashboard.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250430/c5b5c6b0-bc4e-4606-8373-e1eee5a6276b.png)

5. If you have multi-device synchronization needs, you can download the MrDoc Document client through the client download page.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250430/59ab5c52-b80c-4ae4-b5d5-d6aed2d3f6e0.png)

6. If you are interested in more features of MrDoc Document, or need further technical support, you can visit its [official documentation](https://www.atom.com/name/MrDoc) to get the latest user guides and help information.

## **Notes**

Please note that the image in this tutorial is developed and maintained by a third party. The tutorial is for reference only. UGREEN does not assume responsibility for risks arising from improper user operation, third-party software vulnerabilities, or image updates, including but not limited to:

· Third-party images may cause accidental modification or deletion of files in your UGOS Pro system.

· Using insecure images may result in data being uploaded to third-party servers, posing risks of privacy and data leakage.

· To ensure system stability and data security, please carefully select third-party images from trusted sources.

**Other notes：**

1. The file/folder paths of the container are for reference only. You can create them based on your personal preferences.

2. The container's web access port and local port should be the same. If there is a conflict, change it to an unused port. Local ports between containers cannot be the same, as port conflicts will prevent the container from starting.

3. The container's web link is only accessible in bridge mode.

4. The image provides a setup tutorial. For specific usage methods and advanced features, please search online for reference.

5. The image is developed by a third party, and changes in configuration or bug fixes should be monitored through official information from the relevant sources.

6. It is recommended to store Docker configuration directories on an SSD to avoid system performance degradation due to mechanical hard disks.
