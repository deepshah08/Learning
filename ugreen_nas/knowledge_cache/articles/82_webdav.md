# WebDAV

> **Article ID**: `82`  
> **Category**: `Application Guide > Control Panel > File Service > WebDAV`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/82  

---

The WebDAV protocol is one of the features of UGREEN NAS that enables efficient file sharing. It is based on the HTTP/HTTPS protocol, allowing users to access, manage, and edit files on the NAS through Web services, suitable for cross-device file operations and network storage management.

## **Enable WebDAV Service**

1. Open the "Control Panel" app, and tap on [File Service] > [WebDAV].
2. Check the box for "Enable Service," and click "Apply" to save and take effect.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/ba7e5f98-5132-4ac7-9051-14857431fb49.png)

3. If necessary, you can adjust the WebDAV access port in [Advanced Settings]. The default ports are HTTP: 5005, HTTPS: 5006.

## **Connecting to NAS via WebDAV on Windows**

Windows does not support WebDAV connections via HTTP by default. You can enable support for the HTTP protocol by [modifying the registry](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjoxMTE0LCJhcnRpY2xlSW5mb0lkIjozODEsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIn0%3D).

Here are the steps to connect to NAS via WebDAV on Windows:

1. Ensure that your computer and NAS are on [the same local network](https://support.ugnas.com/knowledgecenter/#/).
2. Double-click on "This PC" on the Windows desktop to open File Explorer.
3. Click on the "···" option > [Map network drive].

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/09142720-3c4e-4f90-8be4-3c0c80b3da74.png)

4. Enter the WebDAV address in the "[Folder]" field, in the format `http://NAS_IP address:5005` or `https://NAS_IP address:5006`（e.g.,  `http://NAS_IP:5005` or  `https://NAS_IP:5006`），and click "Finish".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/180047f9-0b02-4b9a-98bd-0da727c0d260.png)

5. In the [Login] interface, enter the username and password for the NAS device, and click the "OK" button.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/84fe40b2-0eb6-4bf3-869c-0526ad7d07ba.png)

6. After a successful connection, you can browse and manage files on the NAS just like accessing local folders in File Explorer.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/446dd601-3865-48a1-bde2-881b8e622d81.png)

## **WebDAV Advanced Settings**

In the advanced settings of WebDAV, you can perform the following operations:

* Enable/Disable HTTP/HTTPS: Enable or disable the HTTP/HTTPS protocol as needed.
* Modify Port Number: Customize the HTTP/HTTPS port number.
* Remove 1024-Character Path Length Limit: Enabling this option supports longer file paths to meet the needs of complex directory structures and file names.
* Enable WebDAV Logging: After enabling the logging feature, you can view the transfer logs in the [Log Center] app.

## FAQ

[To solve the issue of Windows failing to connect to NAS via WebDAV (Error Code 0x80070043)](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MjA1NSwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiZW4tVVMiLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo2MjcsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)

[To solve the issue of Windows being unable to connect to UGREEN NAS via the WebDAV HTTP protocol](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MjA1NCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiZW4tVVMiLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo2MjYsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)

[To resolve the issue of file size limitations with WebDAV transfers on Windows, which is a default setting of 50MB](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MjA1MSwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiZW4tVVMiLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo2MjUsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)

[To resolve the issue of files not being editable or savable after connecting to UGREEN NAS using the WebDAV protocol](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MjA1MCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiZW4tVVMiLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo2MjQsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)
