# Quick Start Guide for Siyuan Notes

> **Article ID**: `534`  
> **Category**: `Application Guide > Docker > Container Application > Quick Start Guide for Siyuan Notes`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/534  

---

## **App Introduction**

Siyuan is a privacy-focused personal knowledge management system that supports fine-grained block references and a WYSIWYG Markdown editing mode, providing users with an efficient knowledge management experience.

**Default Login Information:**

* **Default Access Code:** Set by the user during the installation of the Siyuan Notes application.
* **Default Access Port:** `6806`
* **Local Network Access:** Access the Siyuan Notes Web management interface by entering `NAS_IP:6806` in the browser address bar (e.g., `192.168.22.158:6806`).

**Note**: Do not modify the WebUI port. Changing it will cause the Siyuan Notes application icon redirection in the administrator panel to fail.

**Developer Link:** [GitHub Project Page](https://b3log.org/siyuan/)

## **Installation**

To install the Siyuan Notes application on the UGOS Pro system, follow these steps:

1. **Open the App Center**  
   Locate the **"Siyuan"** application in the app list and click **"Install"**.
2. **Choose Storage Location**  
   By default, the Siyuan Notes application will be installed in **"Volume 1"**. If needed, you can select a different volume during installation. For long-term use, it is recommended to allocate a dedicated volume to facilitate unified management of resources and downloaded files.
3. **Set Access Authorization Code**  
   During the installation process, you need to set an access authorization code (this will be the login password required for the Siyuan Web login interface). This password will be required each time you log in to Siyuan Notes, so please keep it safe to avoid any disruption to future use.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250714/bb30306d-e0bf-419a-9fe6-a596a8ab6235.png)

**Note**: If the password is forgotten, the application must be reinstalled. Reinstallation will erase all application data, requiring reconfiguration.

## Accessing Siyuan

The UGOS Pro system provides the following three access methods:

### **Method 1: Access via the App Center (Administrators Only)**

1. Log in to the UGOS Pro system and open the "App Center".
2. Locate and click the **"Siyuan"** application icon. The system will automatically redirect to the login page.

### **Method 2: Access via Local Network (Administrators and Regular Users)**

1. Within the local network, administrators and regular users can access Siyuan by entering the NAS IP address followed by port 6806.

* Example: Enter `192.168.22.158:6806` in the browser to access.

### **Method 3: Access via Non-Local Network (Administrators Only)**

1. Use UGREEN Link to log in to the UGOS Pro system and open Firefox.
2. After logging into Firefox, enter `NAS_IP:6806` (e.g., `192.168.22.158:6806`) in the browser to access Siyuan Notes.

**Note:** For security purposes, clear your browser history promptly after logging in on untrusted devices to protect your data.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250714/e5270ca0-6378-4bd6-bebf-c0aa78d7f8a9.png)

### **Tips**

1. **Local Network Access:** Use a compatible browser like Chrome or Edge for optimal performance.

2. **Public Network Access:** Protect sensitive information by ensuring data security.
3. **Password Management:** Administrators should safeguard passwords to prevent unauthorized access.
4. **Shared Browser Use:** Disable "Remember Passwords" and clear browsing history regularly.

## Configuring Siyuan

1. Enter the access authorization code (login password) set during installation on the Web login page to log in.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250714/7ffcd29d-6b8d-4ade-9edb-a9cf4dff4111.png)

2. If the authorization code is forgotten, the application must be reinstalled. Please note thatData cannot be retained, and reconfiguration and task addition will be required.
3. Once the authorization code is verified successfully, you can access Siyuan.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250714/2474e44d-bbaa-41df-8956-814eeda55253.png)

## **Change Language Settings**

1. The default interface language of Siyuan Notes is Simplified Chinese.
2. Click the “sy” icon in the top-left corner and select “Settings” to enter the settings page.
3. Under the “Appearance” section in the left sidebar, scroll down to the “Language” dropdown menu. Select your preferred language, and the system will automatically refresh and switch to the selected language.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250714/6d0e19f2-b5e1-42bc-a469-c5c1b5e97551.png)

## **Notes**

When using the UGOS Pro system and container applications, please pay attention to the following:

1. Do not arbitrarily migrate, move, rename, or delete NAS paths mounted by containers, as this may cause malfunctions or data loss.
2. If you need to access container applications via a browser, please disable the multi-gateway option in [Control Panel] > [Network] to avoid network conflicts.
3. Container applications are suitable for beginner users. For more flexible file management configuration, it is recommended to deploy containers directly using Docker.
4. If you require more advanced configuration and management options, it is advisable to use Docker for deployment, which allows for custom configuration files and advanced features.
