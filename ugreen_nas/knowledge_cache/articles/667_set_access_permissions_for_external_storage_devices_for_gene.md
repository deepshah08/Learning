# Set access permissions for external storage devices for general users (sub-accounts)

> **Article ID**: `667`  
> **Category**: `Application Guide > Files > FAQ > Set access permissions for external storage devices for general users (sub-accounts)`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/667  

---

UGREEN NAS allows the administrator to set default access permissions for external storage devices for general users (sub-accounts), including USB storage devices and external storage arrays. Through permission settings, the administrator can effectively control whether general users can access and use external storage devices, enhancing system security and flexibility in data management.

## **Access Permission Settings Entry**

1. Log in to the UGREEN NAS system as an administrator.
2. Open the [Storage] application.
3. In the left navigation pane, select [External Storage].
4. Click the [Advanced Settings] button in the top-right corner to enter the permission configuration interface for external storage devices.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250509/9c20c640-4bf3-46ba-9bee-dc40871a0c76.png)

## **Set External Storage Access Permissions**

In the [Advanced Settings] interface, you will find the "External Storage Access Permissions" option:

* **Use allowed(default):** General users can access and use external storage devices connected to the NAS, including viewing, reading, and writing files on these devices.
* **Use denied:** General users will be unable to access any external storage devices. These devices will not appear in the "Files" section for general users.

Select the desired permission policy and click [Apply] to save the settings and make them take effect immediately.

## **Notes**

* This permission setting applies only to general users (non-administrator accounts). Administrator accounts always have access to external storage.
* When set to "Use denied," general users will not be able to access data on mounted external devices through any means.
