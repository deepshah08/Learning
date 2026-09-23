# SMB

> **Article ID**: `78`  
> **Category**: `Application Guide > Control Panel > File Service > SMB`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/78  

---

The SMB protocol is a core feature of UGREEN NAS for file sharing, allowing users to mount shared folders on local computers (Windows/macOS), mobile devices, and TVs within a local network. This enables centralized storage and cross-device access.

## **Features of SMB Service**

* Cross-Platform Compatibility: Supports Windows, macOS, iOS, Android, and TV boxes for seamless access across multiple devices.
* High-Speed Large File Transfers: Optimized for batch read/write operations, ensuring faster data transmission.
* Multi-Version Protocol Support: Compatible with SMB1, SMB2, SMB2.1, and SMB3 to meet different system requirements.

## **Enable SMB Service**

1. Open the "Control Panel" app and go to [File Service] > [SMB].
2. Check "Enable SMB Service", then click "Apply" to save the settings.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/d35da1c4-294c-4154-983d-2ec486a75bfd.png)

**Note:** You can quickly copy the address for later use by clicking the copy button in the "How to Use" section.

## **Mount UGREEN NAS as a Local Drive via SMB on Windows**

Prerequisite: Ensure that both the NAS and the Windows device are connected to the same local network.

### **Method 1: Map Network Drive**

1. Open This PC, click the "..." button in the top-right corner, and select "Map network drive".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/84342e69-49ea-4b58-957b-070e2160ee52.png)

2. In the folder address field, enter the NAS IP address (e.g., `\\172.17.70.242`), then click "Browse" to select the device. In the network credentials prompt, enter your NAS account credentials for authentication.
3. Once verified, select the specific folder to map, then click "OK" > "Finish". The mapped drive will now appear in This PC.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/69736097-af6a-425b-aaa0-6fddfa29a1c8.png)

### **Method 2: Create a Shortcut**

1. Right-click on an empty area of the desktop, select "New" > "Shortcut".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/a02f59ce-58cd-4e52-9f87-6e3d3cc8c458.png)

2. In the pop-up window, enter the NAS IP address (e.g., `\\172.17.70.242`) in the address field, then click "Browse" to select the device.
3. When prompted, enter your NAS account credentials for authentication. Once verified, select the specific folder and click "Next".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/ed8c5e61-5437-4704-b94c-1f0b932129cc.png)

4. Name the shortcut and click "Finish" to create it.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/3aaf2604-85a0-4826-8efb-626c6dc54681.png)

5. Double-click the desktop shortcut to quickly access the NAS folder.

### **Method 3: Mount a Network Location**

1. Open This PC, right-click on an empty area, and select "Add a network location".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/9eb74215-ac2c-4e94-86ef-f98e09d3e8f5.png)

2. Follow the setup wizard and choose" Custom network location". In the address field, enter the NAS IP address (e.g., `\\172.17.70.242`), then click "Browse" to "select the device". Enter your NAS account credentials in the authentication prompt.
3. Once verified, select the specific folder and click "Next".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/962a6e74-59cb-4255-81f1-9fc82710da10.png)

4. Name the network location and click "Next".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/ec5591ad-44c1-4d2e-9055-93b0c4bfe435.png)

5. The setup is complete, and you can now access the shared folder.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/f39a2f77-c8b4-459f-adfd-6c3e4facb90c.png)

## **Mount an SMB Shared Folder on macOS**

1. Open [Finder], click on "Go" in the top menu bar, and select "Connect to Server".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/5527a63e-73c6-42fd-8170-cba2ccbf7a8d.png)

2. In the "Connect to Server", enter `smb://NAS_IP` (e.g., `smb://172.17.70.242`), then click "Connect".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/ccfd2482-c12c-43da-b9e7-4f3eb5c512dc.jpeg)

3. Enter your NAS username and password for authentication. Once verified, the list of available shared folders will be displayed.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/481b0f76-47af-4aa0-aee3-6dd104734ead.jpeg)

4. Select the shared folder you want to access and click to enter. You can now store and edit files within the folder.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/56efe1e2-c82e-48c9-844f-7b6559be43a6.jpeg)

## **Access an SMB Shared Folder on iOS**

1. Open the "Files" app, tap the “…” button in the top left corner, and select "Connect to Server".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/ab4b199c-9c5f-41dd-9873-bf83254e24e1.png)

2. In the pop-up window, enter the NAS access address in the format `smb://IP_address`. For example, if the NAS IP address is `192.168.31.70`, enter `smb://192.168.31.70` and click "Connect".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/02c8b9ae-0626-47ab-a734-f910ab192eef.png)

3. Enter your NAS username and password for authentication.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/618b8a2e-7632-49f7-a8b6-1572bda47a8b.png)

4. Once connected, you can find the NAS shared folder in the "Files"app. Click on the folder to access and transfer files.

## **Related Links**

* [[Tutorial] How to use SMB protocol to achieve fast multi-terminal file transfer on the LAN?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjoxMDYyLCJhcnRpY2xlSW5mb0lkIjozNTksImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIn0=)

* [Enable Insecure Guest Logon in Windows to Fix SMB Connection Issues](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTk4NSwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiZW4tVVMiLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo2MTksImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)
