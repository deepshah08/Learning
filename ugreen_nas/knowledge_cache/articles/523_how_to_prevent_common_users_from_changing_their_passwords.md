# How to Prevent Common Users from Changing Their Passwords

> **Article ID**: `523`  
> **Category**: `Application Guide > Control Panel > FAQ > How to Prevent Common Users from Changing Their Passwords`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/523  

---

In the UGOS Pro system, newly created user accounts are allowed to change their passwords by default. However, to enhance system security or avoid password management confusion, administrators may wish to restrict common users from modifying their passwords in certain scenarios. You can follow the steps below to disable password changes for common users.

### **Steps**

1. Log in to the UGOS Pro admin console and go to [Control Panel]>[User Management]>[User].
2. In the user list, find the common user you want to configure and click the username or the "Edit" button on the right.
3. On the [Edit User] page, under the Basic Info section, locate and check the option "This user is not allowed to change the password".
4. Click the "Save**"** button at the bottom of the page to apply your changes. The user will no longer be able to change their account password.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250606/f6216356-d1f3-4552-99e3-52736dc22b69.png)

### **Notes**

* By default, common users are allowed to change their own passwords. Once this option is enabled, common users can only use the password set by the administrator and will no longer be able to change it themselves.
* This option is not available for administrator accounts, as they have full password management privileges.
* After enabling this option, make sure the common user is informed about the change in their account permissions to avoid confusion.
* Since common users cannot modify their own passwords, administrators should update passwords regularly to enhance security.
* If a user forgets their password, please contact an administrator for a reset.
