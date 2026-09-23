# Setting Up the Local Full-Text Search Tool file-search on UGREEN NAS

> **Article ID**: `541`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Setting Up the Local Full-Text Search Tool file-search on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/541  

---

## **Application Introduction**

file-search is a document full-text search and preview tool, released under the Apache open-source license. It is known for its excellent local file search speed — even for large folders containing over 100,000 documents, it can deliver results within seconds. At the same time, file-search features a clean and intuitive user interface and convenient local preview functionality, making it a powerful tool to improve NAS file management efficiency.

### **Core Features**

* **Lightning-fast search:** second-level response time, no fear of massive document volumes.
* **Local file preview:** supports online preview of various file formats, including PDF and image files.
* **Multiple search modes:** supports exact file name matching, intelligent matching, and file content search.
* **Flexible sorting:** offers multiple sorting options by time and size.
* **Fully localized:** no internet connection required, protecting data privacy.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250519/e5f4db48-4ae8-4ba9-aad2-0154d582ff34.png)

## **Deploying the Container Using Docker Compose**

On the UGOS Pro system, it is recommended to use the Project (Docker Compose) method for quickly deploying containers. This approach is ideal for scenarios where multiple containers need to be managed simultaneously, as it simplifies both deployment and management tasks. Below are the detailed steps to deploy file-search using Docker Compose.

Click to learn more: [What is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### **Enter the Docker Project Interface**

On the UGOS Pro system, open the Docker application and click [Project] > [Create] to launch the project creation wizard.

### **Configure the Docker Compose File**

In the project creation wizard, upload the following Docker Compose configuration file for file-search:

```
services:
  file-search:
    container_name: file-search
    image: ayound/file-search:latest #Image name
    restart: always #Restart policy
    volumes:
      - ./files:/fsearch/files # Folder path (customizable)
      - ./cache:/fsearch/cache # Cache path
      - ./data:/fsearch/data   # Index data path
    environment:
      - USER_NAME=admin         # Login username (recommended to change)
      - PASSWORD=123456         # Login password (recommended to change)
    ports:
      - 38012:8012              # Map container port 8012 to NAS port 38012
```

### **Parameter Explanation**

**image：**Specifies the Docker image. `latest` indicates the latest version.

**restart：**Defines the container restart policy. `always` means the container will automatically restart if it stops or crashes.

**volumes：**Maps NAS local folders to paths inside the container.

`./files:/fsearch/files`：Directory to be scanned. The part before the colon is the NAS storage path. Please replace `./files` with the actual folder path you want to scan on your NAS, such as `/volume1/Documents`.

`./cache:/fsearch/cache`：Used to store PDF and image preview files.

`./data:/fsearch/data`：Stores the full-text search index data.

**Note**:

* `./` indicates the directory where the current Docker Compose file is located.
* The part before the colon is the path in NAS storage, and the part after is the mapped path inside the container.

**environment：**Environment variables.

`USER_NAME`and  `PASSWORD`：Login credentials. It is recommended to customize them as needed.

**ports：**Maps NAS port `38012` to container port `8012`, used for accessing the web interface.

**Related Reading**

[[FAQ] How to correctly represent volumes mount paths in the Docker Compose configuration file?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTQ0NywidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0ODcsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

### **Deploy the Project**

After uploading the configuration file, click [Deploy] and the system will automatically pull the image and start the container.

Once deployment is complete, open your browser and access the following address to enter the file-search interface:

```
http://<NAS_IP>:38012/fsearch
```

Please replace `<NAS_IP>` with the actual IP address of your NAS, for example:`http://192.168.22.153:38012/fsearch`.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250519/a2117334-9be7-42fd-b65b-1d5d447f8bb4.png)

## **User Guide**

To access the Web interface of file-search, please follow these steps:

1. Open your browser and visit the deployment address to access the login page.
2. Enter the username and password set in the Docker Compose file.

Note: You must add `/fsearch` at the end of the address, for example: http://192.168.22.153:38012/fsearch.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250519/c1a61d03-e048-4bd1-98c1-7c11470ab1fe.png)

### **Indexing**

After logging in, file-search will automatically index the associated folders. It is recommended to avoid selecting the entire storage space, as indexing too many files may take a long time. Instead, choose smaller folders with clear categorization to optimize indexing speed.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250519/49dd8b69-21f9-4e48-b345-94053f3947f5.png)

### **Search and Preview**

Enter a keyword in the search box to instantly display results:

* **Exact Match:** Directly finds items with filenames or content that fully match the keyword.
* **Intelligent Match:** Performs a fuzzy search for related content.
* **Supports Sorting:** Adjusts the display order based on file time or size.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250519/fdd4a80a-ae30-4705-a939-d361f0a7489b.png)

**Online Preview**

* Supports viewing text files or directly previewing images.
* Click the "Download" button to download files to your local device.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250519/939e1955-5e9d-46dc-a42d-8f99d819d0cc.png)

## **Notes**

Please note that the image in this tutorial is developed and maintained by a third party, and the tutorial is for reference only. UGREEN does not assume any responsibility for risks caused by improper user operations, third-party software vulnerabilities, or image updates, including but not limited to:

· Third-party images may cause accidental modification or deletion of files in the UGOS Pro system.

· Using insecure images may lead to data being uploaded to third-party servers, resulting in privacy and data leakage risks.

· To ensure system stability and data security, please carefully choose third-party images from trusted sources.

**Other notes:**

1. The container’s file/folder paths are for reference only, and you may create them according to your personal preferences.

2. The container’s web-access port and the local port should remain consistent. If there is a conflict, switch to an unused port. Local ports must be unique between containers—port conflicts will prevent containers from starting.

3. The container’s web link is accessible only in bridge network mode.

4.This image is provided solely for deployment guidance. For specific usage and advanced features, please refer to online resources.

5. Since the image is third-party developed, stay updated on configuration changes and bug fixes by following the relevant official channels.

6.It is recommended to store Docker configuration files on an SSD to avoid performance issues caused by mechanical hard disks.
