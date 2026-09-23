# Create Users

> **Article ID**: `69`  
> **Category**: `Video Tutorials > User Guide > How to Add External Subtitles in Theater`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/69  

---

You can create both regular users and administrator users. When creating an administrator account, please proceed with caution as administrators have comprehensive system management privileges, including the ability to modify other users' roles and permissions. These permissions are sensitive, so adhere to the principle of least privilege when assigning them.

## **Create User Account**

1. Log in to your UGREEN NAS as an administrator.

2. Navigate to**Control Panel > User Management > Users.**

3. Click **Add > Create.**

The **Create User** window will appear. Follow the prompts to input relevant user information:

* **Username** (Required): Enter a user name. Use 1-64 characters, including uppercase and lowercase letters, numbers, and Chinese characters. The first character cannot be a hyphen. Note: Once the user is created, the username cannot be modified.
* **Password** (Required): Set a password for the user. The password must be at least 6 characters long and contain both uppercase and lowercase letters.
* **Email Address**: Enter the user's email address. System notifications (e.g., password reset messages) will be sent to this email.
* **Description**: Provide a brief description of the user.
* **Role** (Required): Specify the user's role as an administrator or a regular user.
* **User Group**: Select the user group the user belongs to. This column displays different user groups, which can preset file read/write permissions and administrative authorizations. Choosing a user group automatically assigns its permissions to the user. To create a new user group, go to **User Management > User Groups** and add one.
* **Enable Personal Folder for this User**: Check this option to enable the user's personal folder.. The storage location can be adjusted in "File Manager - Personal Folder Management," and a storage quota can be set (supports MB/GB/TB).
* **Disallow Password Change (Only selectable for regular users)**: Check this option to prevent the user from changing their login password for the UGREEN NAS.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250221/2344ec95-7ba2-4c19-a5d3-03c60ad8d300.png)

Click "**Next**" to proceed to file read/write and authorization management.

4.On the file access rights allocation page, select the shared folders accessible to the new user by modifying their access permissions. Administrators can edit permissions for each shared folder, setting them to **'Access Denied', 'Read/Write', or 'Read Only'**.

**Please note:** In case of a conflict between individual permissions and group permissions, the precedence is **'Access Denied' > 'Read/Write' > 'Read Only'.**

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250221/de2dea58-c2e7-4d4b-805b-0e6ed590f888.png)

## **Create an Administrator Account**

1. Navigate to**Control Panel > User Management > Users.**
2. Click**Add > Create.**
3. The Create User window will appear. Follow the prompts to enter relevant user information.

**Role** (Required): Assign the new user's role as '**Administrator**'.

Refer to the "Create User Accounts" section for more detailed steps.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250221/10bf25b7-8980-4136-91e4-fc1c323b64c5.png)

## **Disable User and Administrator Accounts**

The deactivation feature can be enabled for existing user accounts.

1. Navigate to**Control Panel > User Management > Users > Edit User**.
2. Scroll down and check the "**Disable This Account**" box.
3. Optionally, set the deactivation to be immediate or scheduled for a specific date (X year/month/day). Click "**Save**" to apply.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250221/d5b61f3a-b993-4768-880e-0643a6785163.png)
