# To resolve the issue of file size limitations with WebDAV transfers on Windows, which is a default setting of 50MB

> **Article ID**: `625`  
> **Category**: `Application Guide > Control Panel > File Service > To resolve the issue of file size limitations with WebDAV transfers on Windows, which is a default setting of 50MB`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/625  

---

When you edit or copy files using WebDAV and encounter the error message "The file size exceeds the allowed limit and cannot be saved," this is because in Windows, the default file transfer size limit for WebDAV is 50MB. Files larger than this size cannot be copied or saved. If you need to transfer larger files, you will need to manually modify the registry to increase the file size limit. Here are the specific steps:

1. Press  `Win + R` to open the "Run" dialog box, type  `regedit`，in the input box, and then press "Enter."
2. In the Registry Editor, navigate to the path `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WebClient\Parameters`.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/05f51385-aad9-45c2-bdbf-f61ebbe0ae64.png)

3. In the right pane, locate the `FileSizeLimitInBytes` entry.If the option does not exist, right-click on the empty space and select "New" > "DWORD (32-bit) Value".
4. Rename the newly created value to `FileSizeLimitInBytes` and confirm the creation.
5. Double-click on `FileSizeLimitInBytes`to open the editing window and set the file size limit:
6. Select "Hexadecimal," then enter  `ffffffff`(the maximum value), or choose "Decimal" and enter`4294967295`(the maximum value is approximately 4GB).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/972e344f-8a51-4834-8b35-d41d6bd1877b.png)

7. Click "OK" to save the changes.
8. After completing the above modifications, close the Registry Editor. Please note that you must restart your computer for WebDAV to read the new file size limit.
9. After restarting, try copying or editing large files again to verify whether the changes have taken effect.
