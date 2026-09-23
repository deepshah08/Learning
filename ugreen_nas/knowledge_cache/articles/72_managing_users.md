# Managing Users

> **Article ID**: `72`  
> **Category**: `Application Guide > Control Panel > User Management > Managing Users`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/72  

---

The "**Control Panel**" application provides comprehensive user management capabilities. Below is a detailed usage guide.

## Editing Users

On the "**User Management**" page, select "**User**", click the "**···**" button next to the user you want to edit, and choose "**Edit**". You can then perform the following actions:

● **Modify User Information**: Edit user details such as avatar, password, role, and user group.

● **Disable Account**: Enable "**Disable this account**", then choose to disable the account **immediately** or set a specific date. To re-enable the account, simply turn off the "**Disable this account**" option on the same page.

● **Permission Settings**: Configure the user's access permissions for shared folders, including Access denied, Read/Write, or Read only.

![](https://file-us.ugreennas.com/admin/article/2025-12-29/9b8b1d913d9a4e858f336978c732777c.webp)

## Permission Viewer

In the top-right corner of the "**User Management**" page, administrators can use the "**Permission viewer"** to view each user's permissions for shared folders. You can filter the view by user or by shared folder.

![](https://file-us.ugreennas.com/admin/article/2025-12-29/8400fa4e9aaf4126a2c3bb2b799df19d.webp)

## Deleting Users

1. On the "**User Management**" page, select "**User**", click the "**···**" button next to the user you want to remove, and choose "**Delete**".

2. Confirm the deletion. The user will then be removed from the system.

## Advanced Settings

Administrators can use "**Advanced Settings**" to define user password policies, including password strength rules and password expiry rules, to enhance account security.

### Password Strength Rules

1. Open "**User Management**" and select "**Advanced Settings**".

2. Enable the following password strength options as needed:

● **Do not use user names:** When enabled, passwords must not contain the corresponding username.

● **Do not use common passwords:** Prevents the use of high-risk common passwords such as `123456`, `password` or `88888` .

● **Must contain both uppercase and lowercase letters**: Passwords must contain both uppercase and lowercase letters.

● **At least 1 number**: Passwords must include at least one numeric character (0–9).

● **At least 1 special character**: Passwords must include at least one special character (such as `~`, `@`, `#`, `%`, `&`, including spaces).

● **Minimum password length**: This option is enabled by default with an initial value of 6 characters (configurable from 6–127 characters). Empty passwords are not allowed. To improve account security, it is recommended to set a minimum length of 8 characters or more and enable at least three of the first five password strength options listed above.

3. Click "**Apply**" to save the settings.

**Note:** Password strength rules apply only when creating new users or when existing users change their passwords. Passwords of existing user accounts, as well as passwords of users created through import, are not affected by the new rules.

![](https://file-us.ugreennas.com/admin/article/2025-12-29/3a6c79f5e3d34323bbc9392be99ce845.webp)

### Password Expiry Rules

1. Go to "**User Management**"＞"**Advanced Settings**", and enable "**Password expiry rules**".

2. Configure the following options:

● **Password validity period**: Set the duration (in days) for which a password remains valid.

● **Reminder days in advance**: Specify how many days before expiration the system will remind users to change their password.

● **Password change required after expiry**: When enabled, users with expired passwords will be forced to change their password upon login before they can continue using the account.

● **Permanent password users**: Specify users whose passwords never expire. The expiration rules above will not apply to these users. All other users will follow the configured expiration rules.

3. Click "**Apply**" to save the changes.

**Note:** Administrators are advised to regularly review user account status and configure reminder mechanisms appropriately to effectively safeguard device account security.

![](https://file-us.ugreennas.com/admin/article/2025-12-29/8c0ce4aa56ab45a088b7929231ffc184.webp)
