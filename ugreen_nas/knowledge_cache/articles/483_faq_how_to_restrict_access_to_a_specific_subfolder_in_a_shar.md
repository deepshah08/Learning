# [FAQ] How to Restrict Access to a Specific Subfolder in a Shared Folder?

> **Article ID**: `483`  
> **Category**: `Application Guide > Files > FAQ > [FAQ] How to Restrict Access to a Specific Subfolder in a Shared Folder?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/483  

---

## Problem Description

If an administrator wants to grant specific regular users access to certain subfolders within the "Shared Folder" directory on a device, while restricting access to others, for example, in Shared Folder A, which contains subfolders A1, A2, and A3, the administrator intends for a particular regular user to be able to access only A2 and A3, but not view A1.

![](https://file-us.ugreennas.com/admin/article/2025-08-29/9b794386396244298cec0dfda0a946af.webp)

## Solution to the Problem

1. Go to [Files] > [Shared Folder], locate and select the primary shared folder (e.g., Folder A), then right-click and select "Properties".

2. In the "Permissions" section, set the access permission for regular users to "Read Only", and check the option "Hide subfolders and files from users who do not have permission" to ensure that regular users can only see the subfolders they are authorized to access.

3. After making the changes, click "OK" to apply the settings.

![](https://file-us.ugreennas.com/admin/article/2025-08-29/d2fb7868791648d3854e5b8289a4e14c.webp)

4. Locate the subfolder (e.g., A1) within the Shared Folder directory that you want to restrict access to for regular users, right-click and select "Properties". In the “permission” settings, set the user's access permission to "Access denied".

![](https://file-us.ugreennas.com/admin/article/2025-08-29/9ab7f0ceb6e94d79a3b41a31452a04e6.webp)

5. After completing the permission settings, click "OK" to save the configuration. Once the settings are applied, regular users will only be able to view the subfolders they are allowed to access (e.g., A2, A3), and will be unable to view the restricted subfolders (e.g., A1).

#### Notes

● **Hide Function:** Checking the option "Hide subfolders and files from users who do not have permission" is the most necessary thing, ensuring that users cannot see unauthorized folders. If this option is not checked, regular users may still be able to see the folder but won’t be able to access it.

● **Permission Priority:** If a user has "Read Only" access to the primary shared folder, the "Access Denied" setting for subfolders will take precedence, effectively restricting the user's actual access to those subfolders. Click to view the [**"Shared Folder Permission User Guide"**](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMDcwLCJhcnRpY2xlSW5mb0lkIjozNjMsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D) for more details.

● **Administrator Privileges:** Only administrator users have the ability to configure shared folder permissions.
