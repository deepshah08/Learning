# To solve the issue of Windows being unable to connect to UGREEN NAS via the WebDAV HTTP protocol

> **Article ID**: `626`  
> **Category**: `Application Guide > Control Panel > File Service > To solve the issue of Windows being unable to connect to UGREEN NAS via the WebDAV HTTP protocol`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/626  

---

By default, Windows does not support using the HTTP protocol for WebDAV mapping and requires modifying the registry to enable HTTP access. Here are the specific steps:

1. Press`Win + R` to open the "Run" dialog box, enter  `regedit`，and then press "Enter" to open the Registry Editor.
2. In the Registry Editor, navigate to the path `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WebClient\Parameters`

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/2df81b38-4d79-4a21-a9b5-d35cfdaabb7a.png)

3. Locate the `BasicAuthLevel`entry and change its value from `1` to `2`. The default value  `1` only supports HTTPS; changing it to `2`will support both HTTP and HTTPS.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/54944349-5f67-42a8-9e8e-1abe4a7d80b8.png)

4. Press  `Win + S` to search for “Terminal” or “Command Prompt”, right-click and choose “Run as administrator”.
5. Enter the following command to stop the WebClient service:

```
net stop webclient
```

6. Then enter the following command to restart the WebClient service:

```
net start webclient
```

7. Retry the WebDAV connection to see if it has returned to normal.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/0c8b10aa-f48b-49e4-a57f-50659b139213.png)
