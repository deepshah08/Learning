# To solve the issue of Windows failing to connect to NAS via WebDAV (Error Code 0x80070043)

> **Article ID**: `627`  
> **Category**: `Application Guide > Control Panel > File Service > To solve the issue of Windows failing to connect to NAS via WebDAV (Error Code 0x80070043)`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/627  

---

If you encounter error code 0x80070043 when connecting to UGREEN NAS via WebDAV in Windows File Explorer, follow these steps for troubleshooting and resolution:

## Check the network connection

Ensure that the Windows device and NAS are accessible to avoid connection failures due to network issues:

● Access within the same local network: Make sure the Windows device and NAS are connected to the same network and that the NAS device's IP address is accessible.

● Access from the outside network: If you are trying to access the NAS from an external network, ensure that the broadband used by the NAS has a public IP address and that external access permissions are enabled.

## Confirm that the WebDAV service is enabled

1. In the UGOOS Pro system, open the "Control Panel" app, and tap on [File Service] > [WebDAV].

2. Check if WebDAV is enabled and confirm that the HTTP and HTTPS port numbers are set correctly (default ports: HTTP 5005, HTTPS 5006).

3. Save the settings and restart the NAS to ensure the WebDAV service takes effect.

## Verify the WebDAV address format

When mapping a network drive in Windows, ensure that the entered URL address format is correct:

● HTTP method (default port 5005）：

```
http://NAS_IP:5005
```

● HTTPS method (default port 5006）：

```
https://NAS_IP:5006
```

Please note:

● Avoid using backslashes \ (for example,  \\NAS\_IP\），as WebDAV requires the use of  http:// or https:// address formats.

● When accessing from an external network, use DDNS or a public IP address, for example: https://your-nas.ddns.com:5006.

## Check the WebClient Service (which is required for WebDAV connections)

The Windows WebClient service is responsible for managing WebDAV connections. Ensure that this service is running properly:

1. Press Win + R，enter  services.msc，and then press Enter to open the Services.

2. In the list of services, find the "WebClient" service.

![](https://file-us.ugreennas.com/admin/article/2025-08-06/4b588fda6ae74685910e0a5192140a8b.webp)

3. Right-click on "WebClient" and select "Start" (if it's already started, choose "Restart").

## Restart the WebClient service as administrator.

If the WebClient service has started but you still cannot access the NAS via WebDAV (especially if HTTPS connections fail), you should try to manually restart the WebClient service as administrator:

1. Press Win + S to search for “Terminal” or “Command Prompt”, right-click and choose “Run as administrator”.

2. Enter the following command to stop the WebClient service:

```
net stop webclient
```

3. Then enter the following command to restart the WebClient service:

```
net start webclient
```

4. Retry the WebDAV connection to see if it has returned to normal.

![](https://file-us.ugreennas.com/admin/article/2025-08-06/d878551175d245f59fdb5fb17c997ae1.webp)
