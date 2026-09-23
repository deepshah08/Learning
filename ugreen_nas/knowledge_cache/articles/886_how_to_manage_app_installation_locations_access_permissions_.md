# How to Manage App Installation Locations, Access Permissions, and App Data Resets?

> **Article ID**: `886`  
> **Category**: `Application Guide > Control Panel > How to Manage App Installation Locations, Access Permissions, and App Data Resets?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/886  

---

## Applicability

**Applicable client:** UGREEN NAS desktop client (Windows/macOS)  
**Applicable version:** NAS firmware 1.17.0.0031 or later

The descriptions in this document are for reference only. The interface and navigation paths may vary slightly depending on the system or app version. Refer to the actual interface for the latest information.

## Overview

UGREEN NAS allows settings for selected apps to be managed in "**Control Panel**". Depending on the options supported by each app, the installation location and access permissions can be changed, or the app can be restarted.

This feature currently supports apps such as "**Photos**", "**Music**", and "**Theater**". Support for additional apps will be added gradually. Available settings vary by app. Refer to the options displayed on the actual page.

## Accessing the Feature

1. Open "**Control Panel**", then go to "**About**">"**Apps**".

2. Locate the app to manage, then change the available settings as needed.

Only installed apps that support app settings will appear in this list. If an app is not listed, first confirm that it has been installed.

If an app is installed but options such as installation location, access permissions, or app restart are not available, the current version does not support those settings for that app.

![](https://file-us.ugreennas.com/admin/article/2026-06-29/e178bb5fffcd4554a6bf35ea1df51d72.webp)

## Change the App Installation Location

Some apps support changing their installation location, including "**Theater**", "**Photos**", and "**Music**". After a new location is selected, the system migrates the app to the selected storage space.

Follow these steps:

1. On the "**Application configuration**" page, click "**Location**".

![](https://file-us.ugreennas.com/admin/article/2026-06-29/f4e7fff51ebd49f980d573935b679b25.webp)

2. Select the target storage space from the drop-down list.

3. Return to the "**Application configuration**" page and click "**Save**", then confirm the operation in the confirmation dialog.

After confirmation, the system closes the app and starts the migration. Wait for the migration to complete.

![](https://file-us.ugreennas.com/admin/article/2026-06-29/db0cef996cab499b989acb638e3641fb.webp)

**Notes**

● The app may be temporarily unavailable during migration. Reopen the app after the migration is complete.

● If the "**Location**" option is grayed out on an app's configuration page, changing the installation location is not currently supported for that app.

## Configure App Access Permissions

Some apps support configurable access permissions, allowing specific user roles to access the app.

Available options include:

● **All users**

● **Admin**

If "**Admin**" is selected, standard users will not see the app icon on the NAS desktop after signing in and will not be able to use the app.

![](https://file-us.ugreennas.com/admin/article/2026-06-29/a8d5aeeefaa14dd09303cda0fb9f2040.webp)

**Note**: Some third-party apps are restricted to administrators only. In such cases, access permissions cannot be changed. Refer to the options displayed on the actual page.

## Reset a Third-Party App

Some third-party apps, such as **Hermes**, support "**Reset app**".

Resetting an app clears its data and restores it to its initial state. This can help resolve issues caused by corrupted data, incorrect settings, or cache problems.

Follow these steps:

1. On the "**Application configuration**" page, click "**Reset app**".

2. Confirm the operation in the confirmation dialog, then wait for the reset to complete.

After the reset, the associated data cannot be recovered.

![](https://file-us.ugreennas.com/admin/article/2026-06-29/26f48d55b8d44f1b8f11b99df6044f32.webp)

## Other Third-Party App Settings

Some third-party apps also support additional permission or configuration options, such as a login password. Available settings vary by app. Refer to the options displayed on the app configuration page.

![](https://file-us.ugreennas.com/admin/article/2026-06-29/9dbd751ee1b64e20992ec32f1e8379c4.webp)
