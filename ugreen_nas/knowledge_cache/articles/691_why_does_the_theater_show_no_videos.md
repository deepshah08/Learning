# Why does the Theater show "No videos"?

> **Article ID**: `691`  
> **Category**: `Application Guide > Theater > FAQ > Why does the Theater show "No videos"?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/691  

---

## **[Issue Description]**

After opening the "Theater," users are unable to view the media files stored in it. The interface displays: "No videos, please check library settings"

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250529/ab0480f2-c0d8-47c3-ad3c-171414fa37c3.png)

## **[Cause Analysis]**

This issue typically occurs because the currently logged-in account is a common user. By default, common users have "Block Access" permissions for all libraries. An administrator must manually grant library access to the user.

## **[Solution]**

1. Check the type of the currently logged-in account. If it is a common user account, you need the administrator to configure media library access permissions for your account.
2. If you have administrator privileges, please confirm whether the media library setting for your account has "Allow Access" enabled.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250529/631e7c90-07f4-4bf4-931a-5df1cbc42ab5.png)

3. If you're unsure of your account privileges, you can check the account type on the login screen under user information or contact the device administrator for verification.
4. Log in to the UGOS Pro system using an administrator account and go to the [Settings] page in the Theater.
5. Click [User Management] in the left sidebar menu, find your account in the user list, and click "Set Permissions."

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250529/c2f5af78-7a25-4355-8108-c03a36e59648.png)

6. In the user permission settings, change the media library access permission from "Block Access" to "Allow Access".
7. Click "Apply" to save the settings. After completing the permission setup, refresh the Theater page or log in again to access the media library and view video content.

## **[Notes]**

* Common users cannot change media library access permissions on their own. If frequent permission adjustments are needed, it is recommended to contact the administrator or apply for administrator access.
* If the media library still appears empty, please ask the administrator to check whether video files have been correctly imported and ensure the metadata parsing status of the media files is normal.
* If your UGOS Pro system version is outdated, certain features may not work properly. It is recommended that the administrator check for updates and upgrade to the latest version.
