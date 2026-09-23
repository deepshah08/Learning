# File Service

> **Article ID**: `77`  
> **Category**: `Application Guide > Control Panel > File Service > File Service`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/77  

---

The File Service module in the [Control Panel] is a core feature for data sharing and management, supporting multiple protocols, including SMB, FTP, WebDAV, NFS, and rsync. Below is an overview of file services:

### **File Service Features**

* **SMB Protocol**: Allows users to mount shared folders on their local computers within a LAN, enabling centralized file storage and unified management. Supports SMB1, SMB2, SMB2.1, and SMB3, ensuring secure and stable file transfers.
* **FTP Protocol**: Provides a simple and convenient method for file transfer, supporting FTPS encryption for secure data transmission. Ideal for automatically backing up files such as camera photos to the NAS.
* **WebDAV Protocol**: Enables users to manage files directly over the web, making it suitable for integration with web applications (e.g., Alist Xiaoya), allowing seamless file management and access.
* **NFS Protocol**: Primarily used in Unix/Linux environments, facilitating file sharing between different machines. Suitable for using the NAS as a network storage device for other systems.
* **rsync Protocol**: Supports efficient data synchronization and backup, ideal for users who require regular data backups.

### **How to Use the File Services Module**

* **Enable and Configure Services**: Log in to UGOS Pro, open the "Control Panel", go to [File Services], enable the required services (SMB, WebDAV, FTP, etc.), and configure the relevant settings.

* **Mount Shared Folders**: In Windows: Use "Map Network Drive" to mount NAS shared folders as local disks. In macOS: Use "Connect to Server" to establish a connection.

* **Manage Permissions**: Configure user and user group permissions in [User Management] to control access to shared folders, ensuring data security.
