# Setting Up MKVToolNix Multimedia Processing Tool on UGREEN NAS

> **Article ID**: `546`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Setting Up MKVToolNix Multimedia Processing Tool on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/546  

---

## **Application Introduction**

MKVToolNix is a powerful multimedia processing tool designed for creating, modifying, and inspecting Matroska (MKV) files on Linux, other Unix systems, and Windows. This software integrates a variety of practical utilities, aiming to provide a comprehensive solution for managing MKV files.

### **Features**

* **Creating MKV Files:** Users can merge video, audio, and subtitle tracks in different formats into a single MKV container to produce high-quality multimedia files.
* **Editing Existing MKV Files:** This tool allows users to modify existing MKV files, such as adding or removing audio tracks, adjusting chapter information, and changing metadata.
* **Checking and Repairing:** MKVToolnix also features powerful diagnostic functions that can detect and repair corrupted MKV files, ensuring their integrity and playability.
* **Custom Settings:** Users can customize various output file parameters according to their needs, such as resolution, bitrate, encoding methods, and more, to suit specific usage scenarios.

### Official Link

GitHub: [jlesage/docker-mkvtoolnix — MKVToolNix’s Docker container](https://github.com/jlesage/docker-mkvtoolnix)

## **Deploying Containers Using Docker Compose**

On the UGOS Pro system, it is recommended to use project Docker Compose for quick container deployment, which is suitable for scenarios requiring management of multiple containers simultaneously. This method simplifies the deployment and management of containers. Below are the detailed steps to deploy MKVToolnix using Docker Compose.

Click to learn more: [What is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### **Enter the Docker Project Interface**

In the UGOS Pro system, open the Docker application, click [Project] > [Create] to launch the project creation wizard.

### **Configure the Docker Compose File**

In the project creation wizard, upload the following Docker Compose configuration file for MKVtoolnix:

```
services:
  mkvtoolnix:
    container_name: mkvtoolnix
    image: jlesage/mkvtoolnix:latest #Image name
    restart: always #Restart policy
    volumes:
      - ./config:/config # Stores configuration files
      - ./data:/storage # Stores files to be accessed by the container; the path can be modified
    environment:
      - TZ=Asia/Shanghai # Container timezone
      - ENABLE_CJK_FONT=1 # Default is 0; when set to 1, installs the open-source WenQuanYi Zen Hei font, which includes extensive Chinese, Japanese, and Korean characters
    ports:
      - 5800:5800 # Web access port
```

### **Parameter Description**

**image：**Specifies the Docker image version to use (`latest` indicates the latest version).

**restart：**Container restart policy. `always` means the container will automatically restart if it stops or crashes.

**volumes：**Maps NAS file directories to container paths.

`./config:/config`：Maps the NAS storage directory `./config` to the container path `/config`. Used to store configuration files. The part before the colon is the storage path on the NAS.

`./data:/storage`：Stores media files that the container needs to access. The part before the colon is the storage path on the NAS and can be modified as needed — for example, you can change it to your media storage path on the NAS, such as `/volume1/media`.

Notes:

* `./` refers to the directory where the Docker Compose file is located.
* The path before the colon is the NAS storage path, and the path after the colon is the container’s internal mapping path.

**Related Reading**

[FAQ] How to correctly represent volumes mount paths in the Docker Compose configuration file?

**environment：**

`TZ=Asia/Shanghai` ：Sets the container timezone to Shanghai, China (`Asia/Shanghai`). You can adjust this based on your local timezone, such as `America/New_York` for the U.S. or `Europe/London` for Europe.

`ENABLE_CJK_FONT=1` ：The default is 0. When set to 1, an open-source Chinese font will be installed.

**ports：**Web service access port. Maps port 5800 on the NAS to port 5800 inside the container.

### **Deploy the Project**

After uploading the configuration file, click [Deploy]. The system will automatically pull the image and start the container.

Once deployment is complete, access the MKVtoolnix interface through your browser at the following address:

```
http://<NAS_IP>:5800
```

Replace `<NAS_IP>` with the actual IP address of your NAS.

For example: `http://192.168.22.153:5800`.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250519/cc37aec6-9859-4347-b7d2-225425302456.png)

## **User Guide**

To access the MKVtoolnix web interface, open a browser and go to the deployment address to enter the login page.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250519/da48054e-d505-4273-8fb1-dd63a468eba6.webp)

### **Set Language to English**

Click the top-left menu `MKVToolNix GUI` --> `Preferences` --> `GUI` --> `Interface language`, select “English”, then click “OK” to save and apply the changes.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250519/c839c145-eb53-4ff2-a80c-b1f4900ca2b5.webp)

### **More Usage Tutorials**

For more information on how to use the MKVToolNix Docker container, please refer to the following official resources:

**GitHub repository:** [jlesage/docker-mkvtoolnix](https://github.com/jlesage/docker-mkvtoolnix)

**GitLab Wiki:** [[FAQ · Moritz Bunkus / MKVToolNix · JiHu GitLab]](https://gitlab.com/users/sign_in)

These resources provide detailed documentation, FAQs, and other practical information to help you make better use of MKVToolNix for multimedia file processing.

## **Notes**

Please note that the image used in this tutorial is developed and maintained by a third party. This guide is for reference only. UGREEN assumes no responsibility for risks caused by user misoperation, third-party software vulnerabilities, or image updates, including but not limited to:

· Third-party images may cause unexpected modification or deletion of files in the UGOS Pro system.

· Using insecure images may result in data being uploaded to third-party servers, posing privacy and data leakage risks.

· To ensure system stability and data security, please carefully choose third-party images from trusted sources.

**Other notes:**

1. The file/folder paths for containers are for reference only. You may customize them according to your personal preferences.

2. The container’s web-access port and the local port should remain consistent. If there is a conflict, switch to an unused port. Local ports must be unique between containers—port conflicts will prevent containers from starting.

3. The container’s web link is accessible only in bridge network mode.

4.This image is provided solely for deployment guidance. For specific usage and advanced features, please refer to online resources.

5. Since the image is third-party developed, stay updated on configuration changes and bug fixes by following the relevant official channels.

6.It is recommended to store Docker configuration files on an SSD to avoid performance issues caused by mechanical hard disks.
