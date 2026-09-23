# FTP

> **Article ID**: `79`  
> **Category**: `Application Guide > Control Panel > File Service > FTP`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/79  

---

FTP (File Transfer Protocol) is a standard protocol used for file transfer over a network. You can access and manage files stored on NAS through FTP protocol. FTP protocol is simple, fast and efficient, widely used in file sharing and transferring.

## **Feature**

* **Encrypted Transmission:** Support FTPS to provide encrypted transmission to ensure the security of data in the transmission process.

* **Detailed Logs:** Record FTP transfer operations for easy troubleshooting.

* **Access Restriction:** Administrators can set up upload and download speed limitations to prevent a single user from taking up too much bandwidth to affect other users.

* **Cross-platform Multi-client:** FTP protocol is compatible with a variety of operating systems, including Windows, macOS, and supports a variety of FTP client software, such as FileZilla, WinSCP, and Cyberduck, so that users can choose the right client to access UGREEN NAS according to their needs.

## **Scenario**

* **File Sharing:** If you need to share files frequently among team members, FTP service can provide a centralized file storage and sharing platform, which makes it easy for employees to access and manage files, and improves collaboration efficiency.

* **Multimedia File Storage:** You can use FTP service to store multimedia files such as photos, videos and music on NAS devices for centralized management and access.

* **Centralized Storage:** You can use FTP service to centralize the storage of files scattered on different devices on NAS devices for easy management and access.

## **Enable FTP service on UGOS Pro**

1. Go to [Control Panel] > [File service].
2. Click "FTP" and check Enable FTP or Enable FTPS.
3. Click" Apply" to take effect.

### **Connect to NAS via FTP/FTPS on Windows**

#### **Connect to FTP using Windows Resource Manager**

1. **Open Resource Manager:**

   * Press`Win + E` to open File Explorer
2. **Enter FTP address:**

   * Type`ftp://<NAS_IP address>` in the address bar and click Connect. For example: `ftp://192.168.1.100`
3. **Enter the user name and password:**

   * You will be prompted to enter your user name and password. Enter the account information of the NAS device and click **Login**.
4. **Access files:**

   * After successfully logging in, you can browse and manage files on the NAS as if they were local folders.

#### **Connect to FTP/FTPS using the FileZilla client**

1. **Download and install FileZilla:**

   * Download and install the FileZilla client from the official FileZilla website.
2. **Open FileZilla:**

   * Launch the FileZilla client.
3. **Enter connection information**

   * Enter the following information in the Quick Connect field at the top:

     + **Host:** `<NAS_IP address>` (e.g. 192.168.1.100)
     + **User name:** FTP account user name
     + **Password:** FTP account password
     + **Port**: 21 (FTP/FTPS default port)
4. **Connect to the server:**

   * Click "Quick Connect". For FTPS connection, you may need to accept the server's SSL certificate.
5. **Browse and manage files:**

   * After successfully connecting, you can browse and manage files on the NAS in the FileZilla interface.

### **Connect to NAS via FTP/FTPS on macOS**

#### **Connect to FTP via "Finder"**

1. **Open Finder:**

   * ClickFindericon on the desktop.
2. **Connect to the server:**

   * Click **[**Go]> [Connect to Server] in the menu bar (or press `Command + K`).
3. **Enter FTP address:**

   * Type`ftp://<NAS_IP address>` in the address bar and click **"**Connect"**.** For example: `ftp://192.168.1.100`
4. **Enter the user name and password:**

   * You will be prompted to enter your user name and password. Enter the account information of the NAS device and click Login.
5. **Access files:**

   * After successfully logging in, the folders on the NAS will be displayed in the Finder, and you can browse and manage files as if they were local folders.

**Connect to FTP/FTPS via Cyberduck client**

1. **Download and install Cyberduck:**

   * Download and install the Cyberduck client from the official Cyberduck website.
2. **Open Cyberduck:**

   * Launch theCyberduck client.
3. **Create a new connection:**

   * Click the Open Connection
4. **Enter the connection information:**

   * Select the connection type (FTP or FTPS) in the pop-up window, and then enter the following information:

     + **Server**: <NAS\_IP address> (e.g. `192.168.1.100`)
     + **User name**: FTP account user name
     + **Password:** FTP account password
     + **Port:** 21 (FTP/FTPS default port)
5. **Connect to the server:**

   * Click Connect. For FTPS connection, you may need to accept the SSL certificate of the server.
6. **Browse and manage files:**

   * After successfully connecting, you can browse and manage files on the NAS in Cyberduck's interface.

## **FTP Advanced Settings**

In FTP advanced settings, you can customize a variety of parameters to optimize and control the behavior of FTP service better. These advanced settings not only improve the security and performance of FTP service, but also enhance user experience and management efficiency. You can configure the following advanced features:

### **Customize FTP service port**

* **Function:** By default, the FTP service uses port 21, but you can change this port to improve security or to meet specific network configuration requirements. The changed port number must be between 1 and 65535.
* **Application Scenario:** Changing the default port can reduce the risk of malicious scanning and attacks, especially in an open network environment.

### **Enable FTP log**

* **Function:** Enable this function to log all file transfer operations via FTP protocol.
* **Application Scenario:** Logging is useful for troubleshooting and security monitoring. Administrators can use logs to understand user activities and detect abnormal behavior.

### **Set Timeout Value**

* **Function:** The timeout setting defines the duration for which an FTP connection is maintained in an inactive state. If this time value is exceeded, the connection will be automatically disconnected.
* **Application Scenario:** Setting a proper timeout value can release idle connection resources, improve server performance and security, and prevent connections from being occupied for a long period of time.

### **Enable or disable "UTF-8 encoding**

* **Function:** UTF-8 encoding supports multi-language character sets to ensure that file names and directory names are displayed correctly in different languages.
* **Application Scenario:** In multi-language environment, enable UTF-8 encoding to avoid the problem of garbled file names and ensure the correct display and processing of file names.

### **Set Passive FTP Port Range**

* **Function:** Passive mode (PASV) FTP requires the use of a range of ports for data transfer. You can customize these port ranges.
* **Application Scenario:** In a firewall or NAT environment, setting the passive FTP port range can ensure the stability and availability of FTP connections and avoid port conflicts.

### **Limit maximum number of connections per IP source**

* **Function:** This setting allows you to limit the maximum number of FTP connections that each IP address can establish at the same time.
* **Application Scenario:** Limiting the maximum number of connections per IP source prevents a single user from taking up too many resources to improves server fairness and stability ,and prevents DDoS attacks.

### **Enable FTP transfer speed limitation for a single connection**

* **Function:** This function allows you to limit the maximum transfer speed of each FTP connection.
* **Application Scenario:** Limiting the transfer speed of a single connection prevents one user from taking up too much bandwidth, ensures normal use by other users, and optimizes network resource allocation.
