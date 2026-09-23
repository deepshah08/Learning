# User Management FAQs

> **Article ID**: `920`  
> **Category**: `Application Guide > Control Panel > User Management > User Management FAQs`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/920  

---

## How can users change their username?

Usernames cannot be changed after creation. If you need to use a different username, it is recommended to create a new user account.

After confirming that the new account works properly, you can delete the old account that is no longer needed.

Before deleting the old account, make sure to check whether the personal files and permissions associated with that account still need to be retained.

## How to create a new user?

Administrators can create new users in Control Panel. Follow the steps below:

1. Open Control Panel, then click "**User Management**" > "**Create user**".

2. Enter the username, password, user role, and other required information according to the instructions on the page, then click "**Next**".

3. Set folder access permissions, then click "**Done**".

After creation, the new user can use the assigned account to log in to the NAS.

## How to delete a user?

Administrators can delete users that are no longer needed in "**User Management**". Follow the steps below:

1. Open Control Panel, then click "**User Management**".

2. Find the user you want to delete, click "**···** "on the right＞"**Delete**".

3. Follow the on-screen instructions to confirm the operation.

## What should I do if I forget my user password?

If a standard user forgets their password, they can contact the administrator to reset it.

Administrators can go to "**Control Panel**" > "**User Management**", find the corresponding user, and reset the password.

If the administrator account cannot be accessed, reset the administrator password using the supported reset method for your device.

Related document: [What should I do if I forget the administrator password when logging in to UGOS Pro?](https://support.ugnas.com/knowledgecenter/detail/article/zh-CN/435?clientType=PC)

## What is the difference between administrators and standard users?

Administrators have device management permissions and can manage users, user groups, shared folders, apps, system settings, and other system functions.

Standard users are mainly used to access authorized files, apps, and services.

Standard users cannot modify core system settings or manage other users.

## Why can't a standard user see a specific shared folder?

In most cases, the user does not have permission to access the shared folder. Administrators can check the shared folder permissions as follows:

1. Open Files, click "**Management**" on the top bar > "**Shared folder management**", then find the target shared folder.

2. Click "**···**" on the right > "**Permissions**".

3. Check whether the user's permission is set to "**Read/Write**" or "**Read-only**".

If the permission is set to"**Deny access**", the user cannot access the shared folder.

## Why can't a standard user see a specific app?

This may be because the app is only available to administrators. Administrators can check the app access permissions in the app settings:

1. Open Control Panel, then click "**About**" > "**Apps**".

2. Find the target app and check its access permission settings.

![](https://file-us.ugreennas.com/admin/article/2026-08-03/37eda19d26334d8e973ff0a09f3d68ae.webp)

If the setting is Admin only, standard users will not see the app icon on the system desktop and cannot use the app.

## How to enable Personal Folder for a user?

Administrators can enable Personal Folder on the user edit page. Follow the steps below:

1. Open Control Panel, click "**User Management**", and find the target user.

2. Click "**···**" on the right > "**Edit**".

3. Select "**Enable** '**Personal Folder**'", then click "**Save**".

![](https://file-us.ugreennas.com/admin/article/2026-08-03/19adfb7fe28f4619b5434b44e8b2a327.webp)

After enabling this feature, the user can use their own Personal Folder in Files.

## Which permission takes priority when user and user group permissions conflict?

When a user belongs to a user group and the user's permissions conflict with the user group's permissions, the system determines the final permission based on the permission priority.

The priority is:

**Deny access > Read-only > Read/Write > Not set**

For example, if a user has Read/Write permission individually, but the user group they belong to is set to Deny access, the user will not be able to access the folder.

Administrators are advised to review both user permissions and user group permissions when configuring access permissions to avoid conflicts.

## How to limit a user's storage space?

Administrators can limit the available capacity of a user's Personal Folder by setting a folder quota. Follow the steps below:

1. Open **Files**, click "**Management**" on the top bar > "**User Folder Management**".

2. Find the target user, set the capacity limit in "**Quota**", then click "**Confirm**".

![](https://file-us.ugreennas.com/admin/article/2026-08-03/94365329fac443bca33f76cbad7dd86b.webp)

If no storage limit is required, keep the setting as **Unlimited**.

The feature names and page layouts may vary slightly between different system versions. Please refer to the actual interface display.
