# How to Create User Accounts and Assign Permissions

> **Article ID**: `852`  
> **Category**: `Application Guide > Control Panel > User Management > How to Create User Accounts and Assign Permissions`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/852  

---

**Applicable Models:** DH Series, DX Series, DXP Series, iDX Series

**Applicable Clients:** UGREEN NAS PC Client, Web Browser

**Applicable Version:** UGOS Pro Firmware 1.18.0.0076 or later

Screenshots are for reference only. The actual interface may vary depending on the system or App version, please refer to the actual display.

## Overview

If you want to share your UGREEN NAS device with family members or your team, you can create a dedicated account and password for each user in Control Panel. After signing in through a web browser or the UGREEN NAS client with their assigned account, users can access NAS resources based on the permissions you have granted.

## Creating a New User Account

1. Open the "**Control Panel**" app and click "**User Management**" in the left sidebar.

![](https://file-us.ugreennas.com/admin/article/2026-07-24/695e16d910ed4210b75b0da3fb7ef128.webp)

2. On the "**User**" page, click "**Add**" to expand the drop-down menu. The system provides three methods for creating user accounts:

● Create: Manually enter username, password, and other information—suitable for creating new local users.

● Invite: Register via invitation link or QR code.

● Import: Bulk import user accounts—useful if you already have a list of users.

![](https://file-us.ugreennas.com/admin/article/2026-07-24/0c8157d886484c0ea69b7481d31b1749.webp)

3. Using Manual creation as an example, click "**Create**" to open the configuration page.

4. Enter a username and password for the user, then select a **Role** (Administrator or Standard User).

**Note**: Administrators have the highest level of system privileges. Assign this role with caution.

5. Check "**Enable** '**Personal Folder**'" to automatically create a dedicated personal folder for this user in the Files app.

6. After filling in the basic information, click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-07-24/327c060e9af04291a9a4658a8b491e24.webp)

## Assigning Shared Folder Permissions

In the second step of the creation process, you need to assign access permissions to existing shared folders for the new account. The system provides three levels of permission:

● **Access denied**: The user cannot see or access this folder.

● **Read only**: The user can view and download files but cannot modify, rename, or upload new files.

● **Read/Write**: The user has full permissions to view, modify, upload, and delete files.

![](https://file-us.ugreennas.com/admin/article/2026-07-24/5d78ba46f07243529b5551cc3090a03a.webp)

**Default Permission Rules:**

● **Standard Users**: If no permissions are selected, default is"**Access denied**" for all shared folders.

● **Administrators**: If no permissions are selected, default is "**Read/Write**" for all shared folders.

Locate the target shared folder in the list, select the appropriate permissions, and then click "**Done**".

The new account will appear in the user list. When its status is displayed as "**Normal**", the account is active and ready to use.

![](https://file-us.ugreennas.com/admin/article/2026-07-24/ffc498a1d4214903a0e9f3adaf78e3c5.webp)

## Using User Groups for Bulk Permission Assignment

If your NAS has many shared folders and you need to create multiple users, configuring permissions individually can be inefficient. It is recommended to create a "**User Group**" with standardized permissions and then add users to the group.

1. In the "**User Management**" page, switch to the "**User Group**" tab and click "**Add**".

![](https://file-us.ugreennas.com/admin/article/2026-07-24/2b0c8da4d0b8460bae5b56bf9ae039d3.webp)

2. Enter a name for the user group in the popup page and click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-07-24/8ff55d59133b4d91a5919c3359b70706.webp)

3. On the "**Select member**" page, check the users you want to add to this group. If users are not yet created, you can leave this blank for now. Click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-07-24/909752f7a45841e0949637f41460811b.webp)

4. Assign shared folder permissions for the group. Once configuration is complete, click "**Done**".

![](https://file-us.ugreennas.com/admin/article/2026-07-24/ef3220de7b9c4bab9aa91912086f4544.webp)

### Adding New Members Later

If new members need to be added to an existing user group, double-click the target group name in the "**User Group**" tab to enter edit mode. Switch to the "**Select member**" page, check the new members, and click "**Save**".

![](https://file-us.ugreennas.com/admin/article/2026-07-24/b28ad973abc34404bb24593e8c487c0a.webp)

### Verifying Permission Activation

After saving, return to the "**User**" tab. Double-click the user who was just added to the group and switch to the "**Permissions & Settings**" page to confirm that the user has successfully inherited the shared folder permissions from the group.

![](https://file-us.ugreennas.com/admin/article/2026-07-24/2791482574ef4e9ebd0a1094e8e45fb0.webp)

## Permission Conflicts and Priority Rules

If a user account belongs to both a User Role and a User Group, and the folder permissions assigned by the User Role conflict with those assigned by the User Group, the system resolves the conflict according to the following priority order: **Access Denied > Read Only > Read/Write >Empty (Not set)**

![](https://file-us.ugreennas.com/admin/article/2026-07-24/d27b1b396a394bbebf9c7000be95299d.webp)
