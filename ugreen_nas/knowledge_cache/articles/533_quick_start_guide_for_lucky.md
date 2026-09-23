# Quick Start Guide for Lucky

> **Article ID**: `533`  
> **Category**: `Application Guide > Docker > Container Application > Quick Start Guide for Lucky`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/533  

---

## **Application Overview**

**Lucky** is a powerful soft/hard router tool designed for home use, ideal for managing and optimizing household network environments. Its main features include:

* IPv6/IPv4 Port Forwarding
* Web Service Management
* Dynamic Domain Name System (DDNS)
* Wake-on-LAN (WOL)
* IPv4 NAT Traversal
* Scheduled Tasks
* Automatic Certificate Application and Management

**Default Username:** `666`  
**Default Password:** `666`  
**Default Access Port:** `16601`

In the local network, access the Lucky Web management interface by entering `NAS_IP:16601` (e.g., `172.17.20.102:16601`) in your browser's address bar.

**Notes:**

1. Do **Not** modify the WebUI port, as doing so will prevent administrators from accessing Lucky via the application icon.
2. **Change** the default username and password after the first login for security (refer to the "**Changing Username and Password**" section for details).

* **Developer Link:** <https://lucky666.cn/>
* **Developer User Guide:** <https://lucky666.cn/docs/intro>

**Installation Guide**

For instructions on installing Lucky, please refer to the following steps.

## **Installation Guide**

Follow these steps to install the Lucky application on the **UGOS Pro** system:

1. Open the **App Center**, locate the Lucky application, and click **"Install"**.
2. By default, the application will be installed on **Storage Space 1**. If necessary, you can select a different storage space during installation. It is recommended to designate a dedicated storage space for long-term use to efficiently manage resources and downloaded files.

## **Accessing Lucky**

On the **UGOS Pro** system, both administrators and regular users can access the Lucky application using the following methods:

### **Method 1: Via Application Center (Administrator Only)**

1. Open the **App Center** in the UGOS Pro system.
2. Locate and click the **Lucky** application icon. The system will redirect to the login interface.

### **Method 2: Access via Local Network (Administrators and Regular Users)**

1. Within the local network, administrators and regular users can access Lucky by using the NAS IP address with port **16601**.

* For example, enter `192.168.22.158:16601` in the browser.

### **Method 3: Access via Firefox in Non-Local Network (Administrator Only)**

Administrators can access container applications outside the local network using the following method:

1. In a non-local network environment, the system might display a prompt: **"Please connect to the device via IP in the local network before opening."** This can be resolved using the Firefox browser. Firefox supports using **UGREEN Link** to log in to the NAS in non-local network environments.

2. Once logged into Firefox, administrators and regular users can access Lucky by entering the NAS IP address with port **16601**. For example, enter `192.168.22.158:16601` in the browser.

**Note:** When logging in on untrusted devices, please clear your browser's history promptly to ensure data security.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250113/6463f399-e09a-4e30-9c50-101f8ae365a5.png)

### **Usage Tips**

1. Use a compatible browser, such as Chrome or Edge, for the best experience when accessing via the local network.
2. Prioritize data security when accessing the NAS in public networks to avoid exposing sensitive information.
3. Manage access passwords carefully to ensure their security.
4. Disable the "remember password" feature and regularly clear browsing history if Firefox is shared among multiple users for accessing container applications.

### **Log in to Lucky**

On the web login page, enter the default account number `666` and the default password`666` to log in. For security purposes, it is recommended to **change the default account and password promptly** after your first login**（****refer to the “Changing Account and Password” section for detailed instructions****)**

If you forget your login password, you will need to reinstall the application.  
**Note:** Reinstalling the application will not retain any application data. You will need to reconfigure all parameters.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250113/91ad310b-f28c-45a5-adbc-e09663c73f41.png)

## **User Guide**

Before using the Lucky application for the first time, complete the following initialization settings:

### **Change Account and Password**

To ensure the security of the application, promptly update the default account and password:

1. Click **Settings** in the left menu bar to open the settings page.
2. Scroll to the **Login Verification Settings** section.
3. Enter the new administrator account and password.
4. Click **Save Configuration** at the bottom of the page.
5. For the next login, use the updated account and password for verification.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250113/ab067822-c654-4638-a850-77b14b022bb3.png)

### **Set Up DDNS**

DDNS allows you to access your home network devices using a fixed domain name:

1. **Navigate to the DDNS**

In the left menu, select **"DDNS"**, and click **"Add Task"**.

2. **Fill in the Following Information**:

* **Task Name**: Customize the name, e.g., "Home Network".
* **Operation Mode**: Select **Simple Mode**.
* **Hosting Provider**: Choose your domain registrar (e.g., Ali Cloud).
* **AccessKey ID and Secret**: Enter the keys provided by your service provider.
* **Type**: Choose **IPv4** or **IPv6** based on your public network type.
* **Method to Obtain Public IP**: Select **"Obatin via Interface"**.
* **Domain List**:

  + First row: Enter the primary domain (e.g., `20241218.xyz`).
  + Second row: Enter the subdomain (e.g., `*.20241218.xyz`).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250113/c7b48bc6-4cb9-473b-a093-47ac64c152a9.png)

3. Save and Verify the Configuration Click **"Add Task"**. After a short wait, if "**DNS Record Consistent**" appears, the setup is successful.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250113/6e90452b-c8b1-4d77-bf68-54c8b8941d63.png)

### **Apply for SSL Certificate**

An SSL certificate ensures the security of external network access:

1. In the left menu, select **"SSL/TLS Certificate"**, and click **"Add Certificate"**.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250113/6c7fbec7-08f4-4200-b98f-1667722ce10b.png)

2. Provide the Required Information:

* **Certificate**: Customize the name as needed.
* **Add Method**: Select **ACME**.
* **Certificate Authority**: Choose **Let's Encrypt**.
* **Verification Method**: Select the same service provider as used earlier.
* **ID and Secret**: Enter the AccessKey ID and Secret.
* **Domain List**: Add both the primary domain and subdomain.
* **Email**: Use either the system's temporary email or your personal email.
* **Algorithm**: The default choice is **RSA2048**.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250113/4174165f-c856-47c1-af2b-ab723e4c659e.png)

3. After submission, wait a few minutes. Once the certificate is successfully issued, the ACME information and validity period will be displayed.

**Note**: The SSL certificate is valid for 3 months. Lucky supports automatic renewal, so no manual action is required.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250113/7e1d5002-2687-48e8-8b9e-a08c2877af38.png)

### **Set Up Reverse Proxy and HTTPS**

Use the reverse proxy feature to enable HTTPS access by following these steps:

1. In the left menu, go to **"Web Services"** and click **"Add Web Service Rule"**.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250113/089efde3-67a8-43b1-9e86-6e6b08ba19d4.png)

2. Configure the Basic Rule

* **Web Service Rule Name**: Customize a name for easy identification.
* **Operating Mode**: Select **Simple Mode**.
* **Listening Type**: Choose based on the public IP type (e.g., IPv4 or IPv6).
* **Listening Port**: Use the default port `16666` or customize it (ensure it does not conflict with other service ports).
* **Firewall auto-allow**: Enable this option.

* **TLS:** Enable TLS to support HTTPS.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250113/374aabf2-e36e-4709-943a-73172ea9a90a.png)

3. Click **"Add Sub Rule"** to configure specific services:

* **Sub Rule Name**: Customize it, such as "nas".
* **Service Type**: Select **Reverse Proxy**.
* **Front End Address**: Enter the subdomain (e.g., `ugreen.20241218.xyz`).
* **Backend Address**: Enter the internal device's IP and port (e.g., `192.168.31.70:9999`).
* **Others**: Keep the default settings.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250113/57e32958-08e4-4ea7-a4cc-874d4c61d9f7.png)

4. Click **"Add Sub Rule"** to apply.

**Note**: You can add different sub-rules for multiple services, but ensure that subdomain prefixes do not conflict.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250113/6ea8ca5a-cc16-44cf-9842-ded25ed600b5.png)

### **BasicAuth Authentication**

In the "Security Settings" section of a subrule, there is a basic encryption feature called BasicAuth authentication. When enabled, users must first enter a username and password when accessing from an external network, adding an extra layer of security. For services that already have a password-protected login interface, enabling BasicAuth authentication is optional and can be based on personal preference. However, for services without a login interface (such as certain web services), enabling BasicAuth authentication is highly recommended.

**Extended Content**

1. **What is BasicAuth Authentication?**

BasicAuth is a simple HTTP authentication mechanism that validates user identity by including a username and password in the request header. Although relatively basic, it provides an essential level of security, especially for services lacking other authentication mechanisms.

**2. Why is BasicAuth Authentication Needed?**

* **Additional Security Layer**:  
  Even if the service has a password-protected login interface, enabling BasicAuth adds an extra layer of protection to prevent unauthorized access.
* **Protect Sensitive Data**:  
  For services without built-in authentication, BasicAuth effectively prevents unauthorized users from accessing sensitive information.
* **Simple and Easy to Use**:  
  BasicAuth is easy to configure and use, making it a straightforward solution for enhancing security.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250113/0491fa4e-76fc-47a0-af7b-d87995d84c98.png)

### **Redirect to HTTPS**

To implement an automatic redirect to HTTPS, follow these steps:

1. **Add a New Rule in Your Web Service:**

* **Operation Mode:** Customized mode.
* **Listening Port:** Ensure it matches the listening port mentioned earlier.
* **TLS:** Disable TLS.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250113/b68d15f5-6a23-448a-840d-22486c3912e2.png)

2. Click **"Default Rule"** and configure the following:

**Service Type:** Select Redirect.

**Default Target Address:** Enter `https://{host}:{port}`.

**“Everything is great” Switch:** Enable (automatically adds request headers).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250113/359f26d9-9299-44ed-bf91-f65457dd64f9.png)

3. Save the configuration after completing the steps. Once set up, users only need to enter the domain name without manually typing `https://`.

## **Using the Lucky Web Service**

**After completing all configurations, the reverse proxy port needs to be mapped through the router to allow normal access from the external network.** Using Lucky's reverse proxy, you only need to map a single reverse proxy port instead of mapping the internal ports of each service individually.

**Note:** The internal and external port numbers must remain consistent. In this step, map the listening port configured earlier.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250113/e53181f6-56ab-40a4-bab2-937837e74d6c.png)

Once the port mapping is complete and all settings are correct, you can access the system from the external network. For example, entering `nas.20241218.xyz:9876` in the browser will take you to the NAS settings page. Additionally, you will notice a padlock icon in front of the domain name, indicating that SSL secure access has been successfully enabled.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250113/b664acaa-d76e-4624-b122-d681572886e6.png)

## Enable Remote Access Function

UGREEN NAS supports enabling remote access for containerized applications. Users can remotely control and manage these apps via a web browser, PC client, or mobile device, enjoying a seamless cross-device experience.

* The **Lucky** app supports remote access via both Web and PC clients.
* Make sure your **UGOS Pro system** and container applications are updated to the latest version. Older versions do not support remote access.
* The remote access feature is **only available when logged in with a UGREENlink ID**.
* Users logging in via **DDNS or other methods** will not be able to use this feature.

### **Remote Access to Container Applications**

After logging in, click the [Container Applications] icon. The system will automatically redirect to its remote access interface.

### Why Did Remote Access Fail?

If remote access fails, please check whether the following two settings in the **Lucky** app are **disabled**:

* **Force HTTPS**

* **Secure Entry**

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250626/3a8754fe-9435-47c1-873d-17b52222d83e.png)

When accessing via a browser, please avoid using third-party plugins or ad blockers.

## Notes

When using the UGOS Pro system and container applications, please take the following precautions:

#### 1. Avoid Modifying NAS Paths

Do not arbitrarily migrate, move, rename, or delete the NAS paths mounted by containers to prevent functional issues or data loss.

#### 2. Disable Multi-Gateway Option

If you need to access container applications via a browser, disable the Multi-Gateway option under Control Panel > Network Management to avoid network conflicts.

#### 3. Suitable for Beginners

Container applications are suitable for beginner users. For more flexible file management configurations, it is recommended to deploy applications directly using Docker.

#### 4. Advanced Management with Docker

For greater flexibility in configuration and management, consider deploying Lucky directly using Docker. This enables customization of configuration files and access to advanced features.
