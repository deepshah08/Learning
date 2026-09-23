# Setting up HivisionIDPhotos ID Photo Creation Tool on UGREEN NAS

> **Article ID**: `552`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Setting up HivisionIDPhotos ID Photo Creation Tool on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/552  

---

## **Application Overview**

HivisionIDPhoto is a lightweight and efficient AI-powered ID photo creation tool designed to develop practical and systematic intelligent ID photo processing algorithms. If you need to create professional ID photos, you can deploy this tool on your UGREEN NAS to fully leverage its powerful features.

The main features of HivisionIDPhoto include:

1. **Lightweight background removal:** purely offline operation that enables fast inference using only the CPU.
2. **Support for multiple size specifications:** automatically generates various standard ID photo formats and 6-inch layout photos.
3. **Flexible inference modes:** supports fully offline inference or a hybrid edge-cloud inference.
4. **Beautification:** intelligently optimizes portrait appearance.
5. **Intelligent formal attire replacement (under development):** will support personalized formal outfit changes in the future.

**Official GitHub project repository:** [Zeyi-Lin/HivisionIDPhotos](https://github.com/Zeyi-Lin/HivisionIDPhotos)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250522/5fa28a41-2403-4356-85d6-452d066ff21d.png)

## **Deploying the Container Using Docker Compose**

On the UGOS Pro system, it is recommended to use the Project (Docker Compose) for rapid container deployment. This method is especially suitable for managing multiple containers at once and significantly simplifies the process of deploying and managing containers. Below are the detailed steps to deploy HivisionIDPhoto using Docker Compose.

Click to learn more: [What is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjoxMjI4LCJhcnRpY2xlSW5mb0lkIjo0MTEsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiMS4wIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### **Access the Docker Project Interface**

On the UGOS Pro system, open the Docker application and go to [Project] > [Create] to launch the project creation wizard.

### **Configure the Docker Compose File**

In the project creation wizard, upload the following Docker Compose configuration file for HivisionIDPhoto:

```
services:
  linzeyi_hivision_idphotos:
    image: linzeyi/hivision_idphotos:latest # Image name
    container_name: linzeyi_hivision_idphotos
    ports:
      - "7861:7860"  # Web interface port
      - "42553:8080" # API backend port
    environment:
      - PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
      - LANG=C.UTF-8
      - GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D
      - PYTHON_VERSION=3.10.15
      - PYTHON_SHA256=aab0950817735172601879872d937c1e4928a57c409ae02369ec3d91dccebe79
      - USER_ID=1018
      - PUID=1018
      - UID=1018
      - PGID=10
      - GID=10
      - GROUP_ID=10
      - DEFAULT_LANG=en
    command: python3 -u app.py --host 0.0.0.0 --port 7860
    working_dir: /app
    restart: always # Container restart policy
    devices:
      - /dev/dri:/dev/dri # Enable access to integrated GPU
    volumes:
      - ./:/hivision # Mount the project root directory
      - ./creator/retinaface/weights:/hivision/creator/retinaface/weights # Model File Path
```

### **Parameter Description**

Below is an explanation of key parameters used in the Docker Compose configuration:

**image:** Specifies the Docker image. `latest` means the latest version of the image will be used.

**ports:** Defines port mappings between the NAS and the container.

* `7861:7860` Maps port 7860 inside the container to port 7861 on the NAS, used for accessing the web interface.
* `42553:8080` Maps port 8080 inside the container to port 42553 on the NAS, used for API backend communication.

**environment:** Defines environment variables that will be loaded when the container runs.

* `PATH`: System environment path.
* `LANG`: Sets the container's default locale to `C.UTF-8`.
* `PYTHON_VERSION` and  `PYTHON_SHA256`: Specifies the Python version and its corresponding checksum to ensure the security of the Python installation.
* `USER_ID`, `PUID`, `UID`, `PGID`, `GID`, `GROUP_ID`: Define user and group information for running services in the container. This helps avoid running processes as the root user, improving security.
* `DEFAULT_LANG`: Sets the default language of the container environment to English.

**command：**Specifies the command to run when the container starts.

* `python3 -u app.py`: Runs the Python script `app.py`; the `-u` flag enables unbuffered output for easier debugging.
* `--host 0.0.0.0`: Specifies the service to listen on all network interfaces.
* `--port 7860`: Specifies that the service listens on port 7860.

**working\_dir：**Sets the working directory inside the container to `/app`。

**restart：**Defines the container's restart policy; `always` means the container will automatically restart if it stops.

**devices:** Maps hardware devices from the host to the container.

* `/dev/dri:/dev/dri`: Maps the host's GPU driver device into the container, allowing the container to access integrated graphics resources.

**volumes:** Defines mappings between host and container directories for data sharing and persistence.

* `./:/hivision`: Maps the current host directory to `/hivision` inside the container for directory sharing.
* `./creator/retinaface/weights:/hivision/creator/retinaface/weights`: Maps the NAS model file path to the corresponding directory inside the container to enable model access.

**Note:**

`./` refers to the directory where the Docker Compose file is located.

The path before the colon is the local NAS path, and the path after the colon is the corresponding path inside the container.

### **Deploy the Project**

After uploading the configuration file, click [Deploy]. The system will automatically pull the image and start the container.

Once the deployment is finished, open your browser and go to the following address to access the HivisionIDPhoto interface:

```
http://<NAS_IP>:7861
```

Please replace `<NAS_IP>` with the actual IP address of your NAS, for example:`http://192.168.22.153:7861`.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250522/c2277ac3-bacb-4e62-b637-ac25eae6c023.png)

## **User Guide**

After the container starts, access the web interface through your browser to complete configuration and management. Upload the photos you want to process, set the parameters, and then generate your ID photos.

### **Web Interface Features**

1. **Image Upload:** Supports uploading files from your local device.
2. **Parameter Settings:** Allows selection of language, face detection model, and background removal model. Supports adjusting ID photo size, background color, beauty options, and more.
3. **ID Photo Generation:** Displays progress and processing time during generation. Supports output of standard photos, high-definition photos, and background-removed images.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250522/0a2fecb7-ffdf-4a27-881d-4cebe9fa0924.png)

## **Model File Download**

This chapter introduces the download and usage instructions for models optimized for CPU acceleration, covering both background removal models and face detection models. Please select the appropriate model according to your actual needs.

### **Background Removal Models**

Store the downloaded model files in the `/creator/retinaface/weights` directory. Below is the list of supported background removal models:

**MODNet**

* Features: Efficient background removal model, suitable for portrait cutouts in various scenarios.
* Download Link: [Click to download.](https://github.com/Zeyi-Lin/HivisionIDPhotos/releases/download/pretrained-model/modnet_photographic_portrait_matting.onnx)

**hivision\_modnet**

* Features: A portrait cutout model designed specifically for solid color backgrounds, providing precise cutout results.
* Download Link: [Click to download.](https://github.com/Zeyi-Lin/HivisionIDPhotos/releases/download/pretrained-model/hivision_modnet.onnx)

**rmbg-1.4**

* Features: A cutout model based on the open-source BRIA AI, supporting multi-scene portrait segmentation.
* Note: After downloading, rename the file to `rmbg-1.4.onnx`.
* Download Link: [Click to download.](https://huggingface.co/briaai/RMBG-1.4/resolve/main/onnx/model.onnx?download=true)

**birefnet-v1-lite**

* Features: A high-precision segmentation cutout model suitable for scenarios requiring accurate segmentation.
* Note: After downloading, rename the file to `birefnet-v1-lite.onnx`.
* Download Link: [Click to download.](https://github.com/ZhengPeng7/BiRefNet/releases/download/v1/BiRefNet-general-bb_swin_v1_tiny-epoch_232.onnx)

If the download speed is slow, you can also download from [SwanHub](https://swanhub.co/ZeYiLin/HivisionIDPhotos_models/tree/main).

### **Face Detection Models**

The main function of face detection models is to quickly locate facial regions in portrait images. Below are the details of the available models:

**RetinaFace**

* **Features:** Works offline, with fast inference speed and high detection accuracy.
* **Configuration Path:** After downloading, please store the model file in the `/creator/retinaface/weights` directory.
* **Download Link:** [Click to download.](https://github.com/Zeyi-Lin/HivisionIDPhotos/releases/download/pretrained-model/retinaface-resnet50.onnx)

**Face++**

* **Features:** Online face detection API, suitable for integration with cloud services.
* **Usage Instructions:** Requires registration and API access approval. For detailed steps, please refer to [the user documentation.](https://github.com/Zeyi-Lin/HivisionIDPhotos/blob/master/docs/face++_CN.md)

### Instructions for Use

**1. Model Storage Path:** Please ensure that all downloaded model files are stored in the designated `/creator/retinaface/weights` directory; otherwise, loading may fail.

**2. File Naming Convention:** For models that require renaming (such as `rmbg-1.4` and `birefnet-v1-lite`), strictly follow the specified names before placing them in the designated directory.

**3. Network Issues Solution:** If the download links are unavailable or the speed is slow, try switching your network environment or obtain the resources via image sites such as SwanHub.

## **Notes**

Please note that the images used in this tutorial are developed and maintained by third parties. This tutorial is for reference only. UGREEN is not responsible for any risks arising from improper user operation, third-party software vulnerabilities, or image updates, including but not limited to:

· Third-party images may cause unintended modification or deletion of files on your UGOS Pro system.

· Using insecure images may result in data being uploaded to third-party servers, posing privacy and data leakage risks.

· To ensure system stability and data security, please carefully choose images from trusted sources.

**Other notes：**

1. The file/folder paths within the container are for reference only; you may customize them according to your preferences.

2. The container’s web access port and the local port must match. If there is a conflict, change to an unused port. Local ports for different containers must not be the same; port conflicts will prevent container startup.

3. Container web links are only accessible under bridge networking mode.

4. The images provide deployment tutorials only. For specific usage and advanced features, please refer to online resources.

5. Images are developed by third parties; for configuration changes and bug fixes, please follow the official sources.

6. It is recommended to store the Docker configuration directory on an SSD to avoid performance issues caused by mechanical hard disks.
