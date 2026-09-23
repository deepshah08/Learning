# [FAQ] Unable to Connect to UGREEN NAS via WebDAV HTTP Protocol in Windows File Explorer

> **Article ID**: `381`  
> **Category**: `Application Guide > Control Panel > File Service > [FAQ] Unable to Connect to UGREEN NAS via WebDAV HTTP Protocol in Windows File Explorer`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/381  

---

#### **Q3: Unable to Connect to UGREEN NAS via WebDAV HTTP Protocol in Windows File Explorer**

A3：By default, Windows does not support WebDAV mapping over HTTP. You can enable HTTP support by modifying the registry. Please follow the steps below:

1. **Open the Registry Editor:**

   * Type `regedit` in the search box on the taskbar, then select "Registry Editor (Desktop App)."v
   * Alternatively, press  `Win + R` to open the "Run" dialog, type `regedit` and press Enter.
2. **Modify the Registry:**

   * Navigate to the path: `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WebClient\Parameter`.
   * Find the `BasicAuthLevel` entry and change its value from `1` to  `2`. The default value of `1` only supports HTTPS, and changing it to `2` will enable support for both HTTP and HTTPS.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250414/0437d4f8-1b31-48ca-bda1-09bd720148da.png)

3. **Restart the WebClient Service:**

   * Run the "Command Prompt" app as Administrator.
   * Type  `net stop webclient` to stop the WebClient service.
   * Then type `net start webclient` to start the WebClient service.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250414/c7f768f0-c111-4908-b7b4-9c05e1cf1943.png)

4. **Try Connecting Again:**

   * Retry connecting to the UGREEN NAS via WebDAV by mapping the network drive, using the HTTP protocol.
