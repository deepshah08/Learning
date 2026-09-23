# Setting Up a Personal Blog with Docker Compose: A Halo Deployment Tutorial

> **Article ID**: `424`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Setting Up a Personal Blog with Docker Compose: A Halo Deployment Tutorial`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/424  

---

## **Halo Blog Introduction**

Halo is a modern, open-source blogging and content management system (CMS) that is rich in features and supports Markdown documents, capable of meeting the needs of daily writing and article sharing. For users who enjoy writing, sharing, and building personal blogs, Halo is an ideal choice. This tutorial will introduce how to deploy the Halo blog using Docker Compose.

![](https://ugreen-pro.oss-cn-shenzhen.aliyuncs.com/ugreen-pro/admin/article/20241008/e303cbcc-3406-4cb6-90a5-1cf35118951d.png)

## **Deploy Halo Blog with Docker Compose**

### Step 1: Access the Docker Project Interface

In the UGOS Pro system, open the "Docker" app and click on **"Projects > Create"** to launch the project creation wizard.

![](https://ugreen-pro.oss-cn-shenzhen.aliyuncs.com/ugreen-pro/admin/article/20241008/7a335167-84ed-41f7-b6ca-00435982080c.png)

### Step 2: Configure the Docker Compose File

When creating a project, you need to provide a Docker Compose configuration file. Paste the following Docker Compose configuration:

```
services:
  halo:
    image: halohub/halo:sha-9ffb1bb
    container_name: halo
    restart: always
    ports:
      - "8090:8090"  # Map the container's 8090 port to the host's 8090 port
    volumes:
      - ./halo:/root/.halo  # Mount the container's data directory to a local folder to ensure data persistence
    environment:
      - TZ=Asia/Shanghai  # Set the timezone to Shanghai, adjust as needed
      - HALO_EXTERNAL_URL=http://yourdomain.com  # Replace with your blog's domain or IP address
```

**Parameter Explanation：**

* **image**: Specifies the Docker image used to run Halo.
* **container\_name**: The name of the container for easy identification and management.
* **restart**: Set to `always` to ensure the container restarts automatically after an abnormal exit.
* **ports**: Maps the container's internal 8090 port to the NAS's 8090 port, allowing external access to the blog through this port.
* **volumes**: Mounts the local `./halo` folder to the container's `/root/.halo`directory to persistently save blog data.
* **environment**: Sets environment variables:

  + **TZ**: Sets the container's timezone to ensure log timestamps match local time.
  + **HALO\_EXTERNAL\_URL**: Sets the external access address for the blog, recommended to fill in your blog's domain or NAS's IP address.

### **Step 3: Verify and Create the Container**

After completing the configuration, click "**Deploy Now**" to check the correctness of the configuration file. Once verified, the system will start the Halo container according to the Docker Compose file. After clicking "Finish", you can see the Halo container has started correctly in the "Container List".

![](https://ugreen-pro.oss-cn-shenzhen.aliyuncs.com/ugreen-pro/admin/article/20241008/944e7add-cc87-4451-abad-3e5dfcc626bb.png)

![](https://ugreen-pro.oss-cn-shenzhen.aliyuncs.com/ugreen-pro/admin/article/20241008/2af143bd-45dc-4ae6-bb7d-9b75f948fd17.png)

**Notes:**It is recommended to store the Docker configuration directory on an SSD to prevent mechanical hard drives from not entering sleep mode, which can affect system performance.

### **Step 4: Access and Use the Halo Blog**

1. Enter `http://<NAS-IP>:8090` in your browser, replacing `<NAS-IP>` with the actual IP address of your NAS (e.g., `http://192.168.1.100:8090`). Upon the first visit, you will enter the initialization page of Halo, follow the wizard for configuration.
2. Customize the site name, email, username, password, and click "Initialize".

![](https://ugreen-pro.oss-cn-shenzhen.aliyuncs.com/ugreen-pro/admin/article/20241008/2bc43880-bc32-4856-8d36-2e113196d5ad.png)

3. Enter the username and password to log in to Halo and access the dashboard interface.

![](https://ugreen-pro.oss-cn-shenzhen.aliyuncs.com/ugreen-pro/admin/article/20241008/df7eeb44-32d6-4b37-b521-347aea3ebae3.png)

![](https://ugreen-pro.oss-cn-shenzhen.aliyuncs.com/ugreen-pro/admin/article/20241008/db45dadf-f82f-4faf-8090-0bae80b02fee.png)

4. In the Halo backend management page's **Articles** module, click "**Create**", edit the article, and click "**Publish**". After the article is published, it can be viewed in the article list.

![](https://ugreen-pro.oss-cn-shenzhen.aliyuncs.com/ugreen-pro/admin/article/20241008/d609bcce-0115-4d81-9de1-7acb38a2677d.png)

5. Visit `http://<NAS-IP>:8090` (e.g., [http://192.168.22.153:8090](http://192.168.22.153:8090/)) in your local browser to check the Halo front page, where you will see the published articles. For more tutorials on using Halo, please refer to the official Halo documentation ["User Guide | Halo Documentation".](https://docs.halo.run/category/%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97)

![](https://ugreen-pro.oss-cn-shenzhen.aliyuncs.com/ugreen-pro/admin/article/20241008/9a51623b-a136-4013-b8d5-01275b4768da.png)

## **Frequently Asked Questions**

1. Port Conflict Issues 

If port 8090 is already occupied, you can change `8090:8090` to another available port in the `docker-compose.yml`file, such as `8080:8090`, and then access it via `http://<NAS-IP>:8080`.

2. Data Persistence

Ensure that the Halo data directory (`/root/.halo`) is mapped to a folder on your NAS (e.g., `/volume1/halo`). This way, even if the container is restarted or deleted, the blog's content and settings will not be lost.

3. Environment Variable Configuration

Adjust `HALO_EXTERNAL_URL` and `TZ` according to your needs to ensure the access address and time zone settings are correct. Incorrect time zone settings may cause the blog's timestamps to be displayed incorrectly, affecting the user experience.

4. Container Crash or Failure to Start

If the container fails to start properly, you can view the logs through Docker. Common errors include port conflicts, image pull failures, and other issues.
