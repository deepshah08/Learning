# About Container Application

> **Article ID**: `539`  
> **Category**: `Application Guide > Docker > FAQ > About Container Application`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/539  

---

The container applications in UGOS Pro offer users a diverse and flexible range of application services. Compared to deploying containers directly with Docker, the container applications simplify the process, providing an easier entry point for users new to UGREEN NAS and Docker.

This guide covers the essential operations for container applications, including installation, uninstallation, updates, activation, deactivation, and troubleshooting.

## Introduction to Container Applications

#### **1. Source and Identification**

* **Source:** Container applications integrate high-quality applications from the Docker ecosystem, allowing users to easily install and use them through the App Center.
* **Identification:** Container applications are marked with a **"Dependency Package"** label in their detailed descriptions, helping users distinguish them as container-based app

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250114/6ed892d5-5e72-46ff-bdec-d1f724ded7cf.png)

**2. Default Permission Settings**  
By default, container applications have administrator-level access permissions, allowing only administrators to manage and access them.

* For certain applications that support access by all users, permissions can be configured based on specific needs.

**3. Strong Dependency on Docker**

Operations such as installation, uninstallation, activation/deactivation, and updates for container applications rely on Docker’s runtime environment.  
If Docker is not installed or is deactivated, container applications will not function properly. It is essential to ensure Docker is running to maintain the normal operation of container applications.

## Installation Guide for Container Applications

**Preparation Before Installation**

* **Ensure Docker is Installed and Enabled:** Container applications rely on Docker. If Docker is not installed, first install and enable it through the App Center.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250114/f02d52a1-db08-4df9-bb5f-28ef9b098e52.png)

**Confirm Storage Volume:**  
Container applications and Docker can be stored in different storage spaces. During installation, users can customize the storage space as needed.

**Installation Steps**

**1. Open the App Center**

Log in to the UGOS Pro management interface and navigate to the **App Center**.

**2. Select the Container Application**

Locate the desired container application in the App Center.

**3. Choose a Storage Space**

The default storage space is **"Volume 1"**. During installation, users can select a different storage space if desired.

If the option **"Always install applications on this storage space"** is selected, subsequent installations will skip the storage space selection step.

**4. Install and Start**

Click **"Install"** and wait for the system to complete the installation and deployment automatically. After installation, the corresponding container for the application will be created in Docker.

**5. Solution to Installation Failure**

* If an error message appears: **"Installation failed! Error processing package data, please reinstall,"** this may be due to Docker being disabled.
* Check the Docker status, ensure it is enabled, and then retry the installation.

## Management Operations for Container Applications

In the **App Center**, container applications are closely integrated with Docker. Operations such as installation, uninstallation, activation/deactivation, updates, repairs, and launching depend on the presence of Docker to function properly.

### **Uninstall Container Applications**

**How to Uninstall:** Container applications can only be uninstalled through the **App Center** and cannot be directly removed via Docker.

**Notes:** If Docker is uninstalled, all associated container applications will be deleted simultaneously. After uninstallation, the application and its configuration data will be permanently cleared and cannot be recovered.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250114/77d50724-5aa8-43ff-829e-65fff10f4f65.png)

### Update Container Applications

**How to Update:** Container applications can only be updated via the **App Center** and cannot be directly updated in Docker.

**Update Process:** When updating Docker, all associated container applications will be automatically deactivated. After the update is complete, you can manually reactivate the applications.

### Activate/Deactivate Container Applications

* **Support for Bidirectional Operations:** Container applications can be deactivated, restarted, or activated via both the **App Center** and **Docker**. The status of the application will automatically sync between the two platforms after any operation.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250114/a5ff605a-2db8-425b-bb1f-e9f7c1f6b320.png)

**Note:** When Docker is deactivated, all associated container applications will be deactivated simultaneously. Upon reactivating Docker, only the container applications that were deactivated due to Docker being stopped will be reactivated. Applications that were manually deactivated will not be automatically reactivated.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250114/7b5fda22-1d17-40a0-9c79-9160d273d903.png)

### Repair Container Applications

Repairing container applications is only supported through the **App Center**. Users can select the **"Repair"** function in the application details to fix abnormal container applications.

## Access Container Applications

### **Open Container Applications**

* **Supported Methods:**  
  Container applications can be opened via both the **App Center** and Docker.

  + On mobile devices, the built-in browser is used.
  + On Web or desktop clients, third-party browsers are used to open applications.
* **Local Network Restriction:**  
  Some container applications are limited to local network access only. These applications will display a **"Only Available on LAN"** notice on their details page.

### Access Permissions Management

By default, container applications are accessible only to administrators.

## Overview Table: Status of Container Application Installation and Management

|  |  |  |
| --- | --- | --- |
| **Operation** | **Method** | **Notes** |
| **Installation** | **App Center** | Automatically creates a corresponding container in Docker; allows storage space selection. |
| **Uninstallation** | **App Center** | Managed exclusively through the App Center; uninstalling Docker removes all associated applications. |
| **Updating** | **App Center** | Actions synchronize between both platforms; stopping Docker deactivates associated applications. |
| **Activation/Deactivation** | **App Center & Docker** | Actions synchronize between both platforms; stopping Docker deactivates associated applications. |
| **Repairing** | **App Center** | Repair functions are accessible for abnormal applications within the App Center. |
| **Opening** | **App Center & Docker** | Applications can be opened from both platforms; some applications are limited to local network access. |

## Notes

#### **1. Data Security**

Uninstalling Docker or container applications will permanently delete all application data, and recovery will not be possible. Please back up important data in advance.

#### **2. Network Environment**

Some container applications only support access within a local network. Ensure your UGREEN NAS and client devices are on the same local network.

#### **3. System Resources**

Using multiple container applications may consume significant system resources. It is recommended to allocate storage space and network bandwidth wisely to ensure system stability.

## Frequently Asked Questions (FAQs)

**Q1: Do container applications support multiple instances?**  
**A1:** Each container application supports only one instance. For similar functionality, manually deploy multiple identical Docker instances.

**Q2: How do I update container applications?**  
**A2:** Container applications are customized and cannot be updated by manually updating images. Check the **App Center** for system-pushed updates.

**Q3: Can container applications conflict with manually deployed Docker containers?**  
**A3:** Port conflicts may occur. Avoid using the same ports as container applications when deploying Docker containers. Adjust ports in the Docker container configuration if needed.

**Q4: How do I add folders to a container application?**  
**A4:** During installation, you can set the download or resource folder path. Plan your storage requirements in advance to select appropriate folder paths.

**Q5: Can folders be added after installing a container application?**  
**A5:** You cannot add folders directly after installation. To modify settings, uninstall and reinstall the application, reconfiguring the folder paths. Note that uninstalling will erase all previous data.

**Q6: Can I customize the access port for a container application?**  
**A6:** Customizing access ports for container applications is currently not supported. Consider deploying similar containers manually via Docker to adjust port settings.

**Q7: Where are container applications installed and stored?**  
**A7:** Container applications are installed in the selected storage space during installation, with all data stored in the same location. Choose a large-capacity storage space to avoid running out of space during operation.

**Q8: Do container applications support plugins, and where are plugins stored?**  
**A8:** Plugins are not supported for container applications. For extended functionality, consider deploying Docker containers that support plugins.

**Q9: Can container applications be accessed remotely via UGREEN Link?**  
**A9:** Remote access to container applications via UGREEN Link is currently supported only through the Firefox browser. Ensure your network environment is secure.

**Q10: Can multiple folders be mounted to container applications?**  
**A10:** Some container applications, support mounting multiple folders.

**Q11: Can the icons of container applications be changed?**  
**A11:** Changing icons for container applications is not supported at this time.

**Q12: Can data from an existing Docker container be migrated to a corresponding container application in the App Center?**  
**A12:** Container applications are customized and do not support direct data migration. To achieve similar functionality, manually back up the Docker container's data and reconfigure it in the new application.

**Q13: Can the storage space of a container application be changed?**  
**A13:** Changing storage space is not directly supported. To use a different storage space, uninstall and reinstall the application, selecting the desired storage location. Uninstalling will result in data loss.

**Q14: Can container applications be migrated across devices?**  
**A14:** Direct migration to other devices is not supported. To migrate, manually deploy the application on the target device and reconfigure it.

## Solutions for Container Application Installation Failure

If you encounter the error message: **"Installation failed! Error processing package data, please reinstall,"**

* Ensure the Docker application is installed and enabled, as container applications depend on Docker to function.

* If Docker is not enabled, activate it through the **App Center**.
