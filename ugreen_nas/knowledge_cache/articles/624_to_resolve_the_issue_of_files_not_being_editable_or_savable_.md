# To resolve the issue of files not being editable or savable after connecting to UGREEN NAS using the WebDAV protocol

> **Article ID**: `624`  
> **Category**: `Application Guide > Control Panel > File Service > To resolve the issue of files not being editable or savable after connecting to UGREEN NAS using the WebDAV protocol`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/624  

---

If you experience problems with editing or saving files after connecting to a UGREEN NAS using the WebDAV protocol, the problem may be caused by one of the following reasons. Please follow the steps below to troubleshoot and resolve the problem one by one:

## **Check the permission settings**

* Log in to the NAS management interface, go to the [Files] app, click [Shared Folder], select the target folder, right-click on the properties to view the permission settings.
* Confirm whether the current login account has read and write permissions (not "read only") on the target folder. If you are not the administrator, please contact the administrator to check and handle the issue.

## **Check client support**

* Confirm that the client you are using supports the write function of WebDAV (some software only supports reading). It is recommended to use a third-party professional tool such as RaiDrive or Cyberduck.
* When using Windows Explorer to map a network drive, check "Reconnect at login" and select a path with write permissions (e.g. `https://NAS_IP:5006/docker` ).

## **Check network and firewall settings**

* Ensure that the default WebDAV port ( **HTTP 5005** / **HTTPS 5006** ) is open. The specific port is subject to the port set in the NAS's [Control Panel] > [File Service] > [WebDAV] > [Advanced Settings].
* Check whether the local firewall (such as Windows Defender or a third-party firewall) is blocking WebDAV traffic.
* Use the commands `ping NAS_IP`and `telnet NAS_IP 5006`to verify basic connectivity. If the commands fail, it may indicate a network connection issue or the port being blocked.

## **Restart the WebClient service (Windows system)**

1. Press Win + R to open the "Run" dialog box. Enter `services.msc` and press Enter.
2. Find the WebClient service in the list of services, right-click and select Restart.
3. If the service status is "stopped", you need to change its startup type to "automatic" before restarting it.

## **Note**

* **Path format:** WebDAV addresses must include the protocol and port (e.g. `https://192.168.1.100:5006` ).
* **Troubleshooting with logs**: If the problem persists, go to [Log Center] > [Logs] to check the NAS WebDAV service log.

## **Quick self-check list of permissions**

|  |  |  |
| --- | --- | --- |
| **Problem type** | **Checkpoint** | **Suggestion for resolution** |
| Insufficient permissions | NAS folder permissions, WebDAV mode | Modify the permissions to "read and write". |
| The client does not support writing | Client function verification | Replace with a professional tool (e.g. RaiDrive) |
| Port blocked | Firewall rules, port opening status | Open 5005/5006 ports |
