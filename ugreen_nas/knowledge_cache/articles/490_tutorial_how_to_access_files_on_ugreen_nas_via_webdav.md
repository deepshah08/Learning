# [Tutorial] How to Access Files on UGREEN NAS via WebDAV?

> **Article ID**: `490`  
> **Category**: `Application Guide > Control Panel > FAQ > [Tutorial] How to Access Files on UGREEN NAS via WebDAV?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/490  

---

WebDAV (Web Distributed Authoring and Versioning) is an extension based on the HTTP protocol designed for remote file management and operations over a network. It allows users to access data on UGREEN NAS as easily as managing a local file system. This article will provide a detailed guide on how to enable the WebDAV service on UGREEN NAS and use the protocol to remotely manage files stored on the NAS.

## **Enable WebDAV Service on UGREEN NAS**

1. Open the [Control Panel] application in the UGOS Pro system, select [File Service], then click on [WebDAV].

2. Check the option to enable "WebDAV Service."

3. Click the [Apply] button to save the settings.

Note: If you need to change the default port, you can adjust it in [Advanced Settings]. The default HTTP port is  `5005`, and the default HTTPS port is `5006`. (Optional)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250414/9caa6f2f-a36a-4639-99ea-4b1165962913.png)

### **Mounting WebDAV Service**

To mount the WebDAV service, use one of the following addresses:

* `http://NAS_IP:5005`
* `https://NAS_IP:5006`

Replace `NAS_IP` with the actual IP address of your NAS. For example: `http://172.17.70.242:5005`

### **To check the NAS IP address**

* In the [Control Panel], go to [Network].
* Click [Network Connection] to view the IP address of your NAS device.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250414/6c20a3e4-af4d-4f90-ac47-f89dafdae31d.png)

## **Connecting to UGOS Pro via WebDAV on Windows**

1. Ensure that your computer and UGREEN NAS are on the same local network. You can refer to ["How to Confirm if Your Computer and NAS are on the Same Area Network."](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTEyMSwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiZW4tVVMiLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjozODgsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)

2. Press `Win + E` to open File Explorer on your Windows computer.

3. In File Explorer, click the "This PC" tab, then select "Map Network Drive."

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250414/99d9dfdc-e078-4f83-b727-1261d99cc1e2.png)

4. Enter the WebDAV address. In the "Folder" field, input the WebDAV address of your UGREEN NAS (e.g., `http://NAS_IP:5005`).

5. Check the option "Reconnect at sign-in," then click "Finish."

6. Enter your credentials. Input the username and password you created on the UGREEN NAS to complete the connection.

7. After a successful connection, the shared folders on your UGREEN NAS will appear under "This PC."

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250414/c77f4387-3d46-440c-90ce-38ae560da0b8.png)

## **Connecting to UGOS Pro via WebDAV on macOS**

1. Ensure that your computer and UGREEN NAS are on the same local network. You can refer to ["How to Confirm if Your Computer and NAS are on the Same Area Network."](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTEyMSwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiZW4tVVMiLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjozODgsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)

2. Click the Finder icon on your desktop to open Finder.

3. In the Finder menu bar, click "Go," then select "Connect to Server."

4. Enter the WebDAV address. In the "Server Address" field, input the WebDAV address of your UGREEN NAS (e.g., `http://NAS_IP:5005`), then click "Connect."

5. Enter your credentials. Input the username and password you created on the UGREEN NAS, then click "Connect."

6. After a successful connection, the shared folders on your UGREEN NAS will appear in the "Locations" section of Finder.

## **WebDAV Advanced Settings**

In the WebDAV advanced settings of UGOS Pro, you can perform the following actions to optimize and control the WebDAV service:

1. Enable HTTP and HTTPS services:

* You can choose to enable or disable the HTTP and HTTPS services. This allows you to configure the WebDAV service based on security requirements and network environment. For example, enabling the HTTPS service is necessary in environments that require encrypted communication.

2. Modify HTTP and HTTPS Port Numbers:

* Customize the port numbers for HTTP and HTTPS services to avoid conflicts with other service ports. By default, HTTP typically uses port `5005`, and HTTPS uses port `5006`. You can change these to other ports based on your network configuration needs.

3. Remove the `1024`Character Path Length Limitation:

* Modern operating systems and file systems typically support file paths longer than `1024`characters. By enabling the "Remove `1024` Character Path Length Limitation" option, you can ensure that the WebDAV service supports longer file paths to accommodate complex directory structures and file names.

4. Enable and Log WebDAV Logs:

* You can choose to enable WebDAV logging to track and analyze access records for the WebDAV service in detail. This is very useful for troubleshooting and security auditing. Logging can help identify potential security threats and optimize the performance of the WebDAV service.
* Once enabled, if you wish to view the WebDAV logs, go to the [Log Center] app. After opening the Log Center, change the log type from "Event Log" to "Transfer Log" under [Logs] > [Current Logs] to view the transfer logs.

If you made changes to the settings, click "Save" to save the changes, then click "Apply" to make the new settings take effect.

## **Enable Windows WebDAV HTTP Support**

By default, Windows does not support WebDAV mapping over HTTP. You can enable HTTP support by modifying the registry. For detailed steps, please refer to [this article.](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTExNCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiZW4tVVMiLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjozODEsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)
