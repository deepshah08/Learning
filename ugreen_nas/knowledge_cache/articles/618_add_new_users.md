# Add New Users

> **Article ID**: `618`  
> **Category**: `Application Guide > Control Panel > User Management > Add New Users`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/618  

---

In the "**Control Panel**" app, click "**User Management**" to choose from several methods for adding a new user. The following are detailed steps and explanations:

![](https://file-us.ugreennas.com/admin/article/2026-01-06/88cf32f8671d45ce8e292e6100f8f53e.webp)

## Create a User

1. Log in to the system with an administrator account.

2. Open the "**Control Panel**" app, navigate to "**User Management"**>"**User"**>"**Add**". In the pop-up window, select the "**Create**" option to manually enter the new user's information.

3. Fill in the user information:

● **User name:** Enter the new user's username, ensuring it is unique.

● **Password:** Enter the new user's password and confirm it.

● **Role:** Choose the user's role—either common user or administrator.

● **Enable personal folder:** Decide whether to enable a personal folder for the user and set the storage quota if applicable.

● **Password Change Permission:** Decide whether the user is allowed to change their own password.

4. Click "**Next**" to continue. Configure the user's access permissions for shared folders (**Access denied**, **Read/Write**, **Read Only**).

5. After verifying that all information is correct, click "**Done**". The new user can now log in to the system using their username and password.

## Invite Users

1. On the "**User Management**" page, click "**User**">"**Add**". In the pop-up window, select the "**Invite**" option to invite a new user to the system.

2. The system will generate an invitation link or QR code. The administrator can share it with the new user via email, SMS, or social media.

3. The invited user must click the link or scan the QR code and follow the prompts to complete registration and log in.

**Note:** If you need to invite users from outside the local network, make sure the **UGREENlink** feature is enabled so new users can access the invitation link smoothly.

![](https://file-us.ugreennas.com/admin/article/2026-01-06/f189328e75554e6c909e9d6c82758c44.webp)

4. Administrators can review new user requests on the "**Application list**" page and approve them.

![](https://file-us.ugreennas.com/admin/article/2026-01-06/4fadcc7b78e04b1a93fdf5c73a5f4af2.webp)

## Import Users

1. On the **User Management**" page, click "**User"**>"**Add**". In the pop-up window, select the "**Import**" option to add multiple users in bulk.

2. In the **Import Users** pop-up, click the "**Download template**" button to download an Excel or CSV template containing the required user information.

![](https://file-us.ugreennas.com/admin/article/2026-01-06/21c1bfba8dfb4c4fa94c815207077e0e.webp)

3. Fill in the user information according to the template format, including mandatory fields such as username, password, and role.

4. After completing the template, save the file, then click "**Browse**" in the "**Import users**" window to upload it, and click "**Next**" to continue.

5. You can choose whether to require new users to change their password on first login.

![](https://file-us.ugreennas.com/admin/article/2026-01-06/e6621f46fc244810af260586935491ad.webp)

6. After verifying that all information is correct, click "**Import**" to complete the user import. Imported users can log in to the system using their username and password.

**Import Template Example:**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **\*Username** | **\*Password** | **Description** | **E-mail** | **\*Role（admin/users）** | **User Group（Separated by ","）** |
| aaa | Aa112233 | Colleague | aaa@a.com | users | group1,group2 |
| bbbb | Aa112233 | Family | Bbbb@b.com | admin | group1 |
| cccc | Aa112233 | Friend A | Cccc@c.com | users | group2 |
| dddd | Aa112233 | Friend B | Dddd@d.com | users | group1,group2 |

## Usage Tips

1. Administrators have the highest level of permissions and can access and manage all system settings. Assign administrator privileges with caution to ensure system security and stability.

2. When a user's individual permissions conflict with the permissions of their user group, the system follows the following permission priority rules:

3. **Access denied**> **Read Only** > **Read/Write**

4. For example, if a user group has "**Access denied**" but the individual user is granted "**Read/Write**", the user's effective permission will be set to "**Access denied**".

5. For more details, please refer to: [Priority Between Individual and User Group Permissions](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTUyMiwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo1MjQsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==) .

6. When creating standard users via import, personal folders are disabled by default. If the user does not belong to any user group, they will not have access to shared folders. To adjust shared folder access or enable a personal folder, you can manually add the user to an appropriate user group or assign permissions individually after import.
