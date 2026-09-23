# How to Enable and Manage Personal Folder

> **Article ID**: `604`  
> **Category**: `Application Guide > Files > FAQ > How to Enable and Manage Personal Folder`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/604  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS).

**Applicable Version**: NAS Firmware 1.18.0.0032 or later.

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

A Personal Folder is a dedicated space for users to store their personal files. By default, only the user who owns the Personal Folder and administrators can access it. Other standard users cannot access it.

After enabling Personal Folder, users can manage their files through the Personal Folder entry in the Files app.

## Enable Personal Folder

Administrators can enable Personal Folder for users in Control Panel. Follow the steps below:

1. Open the Control Panel app and click "**User Management**".

2. Find the target user in the user list, click "**···**" on the right, and select "**Edit**".

3. On the Edit user page, select "**Enable** '**Personal Folder**'", then click "**Save**".

After saving, the user can use Personal Folder in the Files app.

![](https://file-us.ugreennas.com/admin/article/2026-07-30/70a2468cf0bb4a7bad8abf79e2c47fbd.webp)

## Set Full Rights

Standard users can enable Hide personal files from other users. To use this feature, an administrator must first enable "**Full rights**" for the user.

After Full rights is enabled, users can decide whether to hide their Personal Folder in Personal Folder Management.

If a user enables this setting, other users will not be able to view the user's Personal Folder.

**Note**: If a standard user has enabled "**Hide personal files from other users**", the administrator cannot enable encryption for this user's folder.

## How can administrators enable Full rights?

1. Open the Files app, click "**Manage**" in the top bar ＞"**User Folder management**".

2. Find the target user, select "**Full rights**", and click "**Confirm**".

After the setup is complete, the user can control their own Personal Folder visibility settings.

![](https://file-us.ugreennas.com/admin/article/2026-07-30/a4a8bbe3c3d84080aa6e5c5566c8e4ac.webp)

## How can standard users hide their Personal Folder?

After the administrator enables Full rights, standard users need to enable the hide setting themselves. Follow the steps below:

1. Log in to the NAS using a standard user account.

2. Open the Files app and go to "**Personal folder management**".

3. Select "**Hide personal files from other users**", then click "**Save**".

After saving, the user's Personal Folder will be hidden from other users.

![](https://file-us.ugreennas.com/admin/article/2026-07-30/4e7c8d904445425b9725508055bc1ace.webp)

## Notes

● After an administrator enables Full rights for their own account, other administrators will no longer be able to view the contents of this administrator's User Folder.

● After enabling Full rights for a standard user, the user must also enable "**Hide personal files from other users**" for the hide setting to take effect.

● Administrators can only enable "**Full rights**" for their own accounts and standard user accounts. They cannot control this permission for other administrator accounts.

● After a standard user enables "**Hide personal files from other users**", the administrator can no longer disable Full rights for this user.

● When Full rights is not enabled, the contents of a user's Personal Folder can only be viewed by the folder owner and administrators.
