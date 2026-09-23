# Quick Start Guide for Firefox Browser

> **Article ID**: `531`  
> **Category**: `Application Guide > Docker > Container Application > Quick Start Guide for Firefox Browser`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/531  

---

## Getting Started

**Firefox** is an open-source and secure web browser that runs on the UGOS Pro system, enabling web browsing and **access to intranet devices**. With the Firefox application integrated into the App Center, **users can easily manage services and applications within the local network** without the need for external devices. To enhance functionality or install plugins, users can visit the Firefox extension marketplace for additional resources.

**Default Login Information:**

* **Default Password:** Set during application installation

**Default Ports:**

* **Web Access Port:** 5888
* **TCP/UDP Forwarding Port:** 5999

To access the Firefox Web Management interface within the local network, enter `NAS_IP:5888` (e.g., `172.17.20.102:5888`) in the browser's address bar.

**Note: Avoid changing the WebUI port, as doing so may prevent the Firefox application icon from redirecting properly in the administrator panel.**

## **Installation**

1. **Open the App Center**  
   Locate the Firefox application and click "**Install App**."
2. **Select Installation Location**  
   By default, container applications are installed in "Storage Space 1." Users can choose a different storage space during installation. For long-term use, it is recommended to allocate a dedicated storage space for better resource and file management.
3. **Set Login Password**  
   During installation, you will need to set a login password, which will be required each time you access the application. Please keep this password secure to avoid issues with future access.  
   **Note: If forgotten, the app must be reinstalled, erasing all data and requiring reconfiguration.**
4. **Configure Download Directory**  
   You will need to set a resource download directory for Firefox during the installation process. Files downloaded via Firefox will be stored in this directory. It is recommended to choose a storage space with ample capacity to avoid affecting other storage tasks.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250506/dd7ce270-7910-4504-8b65-84985ec6d8db.png)

## **Accessing Firefox**

On the UGOS Pro system, administrators and regular users can access the Firefox application using the following methods:

### **Method 1: Access via the App Center (Administrators Only)**

1. Open the App Center on the UGOS Pro system.
2. Locate and click the Firefox application icon. The system will redirect to the login page.

### **Method 2: Access via Local Network (Administrators and Regular Users)**

1. Within the local network, administrators and users can access Firefox using the NAS IP address followed by port 5888.

* Example: Enter `192.168.22.158:5888` in the browser to access Firefox.

### **Method 3: Access via UGREEN Link Outside the Local Network (Administrators Only)**

1. Firefox supports access to the NAS via UGREEN Link in non-local network environments.
2. When using Firefox on untrusted devices, it is recommended to clear access history promptly to ensure data security.

### **Usage Tips**

1. **Browser Compatibility:** For the best experience, use browsers with better compatibility (e.g., Chrome or Edge) when accessing Firefox within the local network.
2. **Data Security on Public Networks:** When accessing the NAS in public network environments, be mindful of data security to avoid leaking sensitive information.
3. **Password Management:** Administrators should securely manage access passwords to ensure their safety.
4. **Shared Browser Usage:** If multiple people share the Firefox browser, disable the "remember passwords" feature and regularly clear browsing history.
5. **Default Language:** Firefox's default language is English. When accessing the NAS via Firefox, the NAS interface follows the system's default language.
6. **Using Proxy Features:** Exercise caution when adding proxy settings in Firefox. Enabling a proxy will route all access requests through the proxy server, which may prevent direct access to local network resources such as containers and virtual machines.

### **Logging in Firefox**

Enter the login password set during installation and click **"Send Credentials"** to verify your identity. Once verified, you can access the Firefox browser.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250110/c9ba8c5e-a264-4275-8fe1-ccbef04d6944.png)

### Skip the Initial Setup Wizard

When logging into Firefox for the first time, an initial setup wizard will appear. Click **"Skip this step"** to bypass multiple setup pages until **"Start browsing"** is displayed.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250110/4074a7f8-e868-433d-97cf-bda840b464be.png)

● Click **"Start browsing"** to begin using the browser.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250110/4dea6a03-2828-4544-8896-a023f9c5a9d1.png)

## **Using Firefox to Access Local Network Devices and Applications**

1. **Access Local Network Applications**

Firefox can be used to access devices or applications within the local network without requiring public IP, DDNS, or port forwarding configurations. Simply enter the address in the format `NAS_IP:Port` in the browser's address bar. For example:

* After deploying the Firefox container application, enter `NAS_IP:8888` (e.g., `172.17.20.102:8888`) in the Firefox address bar to access the Firefox interface.

2. **Obtain Application IP Address and Port**

The IP address and port information for container applications within the local network can be found on the Docker container management page:

* Open the **Docker** application and locate the corresponding container application.
* View the container details and note the IP address and port.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250820/10283dde-3559-4aa3-a9c0-ef88c6e63eae.png)

Enter the relevant information in Firefox to access it.

3. **Application Limitations**

Some container applications are limited to local network access. For example, in non-local network environments, the system may display a message such as, "Please connect to the device via IP within the local network before opening." Firefox offers an easy solution to this issue—users can simply enter the container's local network IP address in Firefox to access and use the application seamlessly.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250110/becc6520-63c7-40af-ad2f-9b64168e2d91.png)

## **Notes**

To ensure the proper functioning of the UGOS Pro system and container applications, please consider the following:

1. **NAS Path Management:** Avoid migrating, moving, renaming, or deleting NAS paths mounted by container applications to prevent functionality issues or data loss.
2. **Firefox Usage:** Do not repeatedly switch between "**Open NAS > Open Firefox > Open NAS again > Open Firefox again**," as this may cause access errors in the system.
3. **Network Settings:** If accessing container applications via a browser, disable the **Multi-Gateway** option under **Control Panel > Network** to avoid network conflicts.
4. **For Beginners:** Container applications are suitable for novice users. For more flexible file management, consider deploying applications directly using Docker.
5. **Advanced Users:** For greater flexibility and control, deploy applications via Docker to enable custom configuration and advanced features.

**Frequently Asked Questions (FAQs)**

**Does Firefox Support Mobile Devices?**

The current version of Firefox does not support mobile devices. Please use the PC/Web version for access. Mobile support is under development.
