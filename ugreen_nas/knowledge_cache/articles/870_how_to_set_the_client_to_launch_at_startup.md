# How to Set the Client to Launch at Startup?

> **Article ID**: `870`  
> **Category**: `Application Guide > UGOS Pro > How to Set the Client to Launch at Startup?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/870  

---

## Applicability

**Applicable client**: UGREEN NAS PC client (Windows/macOS).

**Applicable version**: NAS firmware 1.16.0.0042 and later.

**Requirement**: To enable this feature, the PC client must be updated to V1.16.0.77937 or later. If the client version is earlier than this, update the client first.

This article is for reference only. The actual interface and operation path may vary slightly due to system or app version updates. Please refer to the actual interface.

## Overview

After this feature is enabled, the UGREEN NAS client will launch automatically each time the computer starts, allowing file sync tasks and background backups to continue seamlessly.

## Enable or Disable Launch at Startup

The autostart behavior can be managed directly in the client settings:

1. Log in to the UGREEN NAS desktop. In the top-right corner, click "**Me**" > "**Client**".

![](https://file-us.ugreennas.com/admin/article/2026-06-05/1e220df36ee14c7ea33cf0b9d26792b8.webp)

2. On the settings page, find and turn on "**Autostart after booting**".

![](https://file-us.ugreennas.com/admin/article/2026-06-05/86c351f213994ecab7719d86f4d4ce8b.webp)

To prevent the client from launching automatically when the system starts, return to this page and turn off the feature.

## Why doesn't the client launch automatically at startup after "Autostart after booting" is enabled?

This is usually because the operating system has blocked the client's startup request. Check and fix the issue according to the system on your computer:

**Windows:**

1. Press the shortcut key `Ctrl + Shift + Esc` to open "**Task Manager**".

2. Switch to the "**Startup apps**" page from the left sidebar.

3. Find **UGREEN NAS** in the app list and check whether the status on the right is "**Disabled**".

4. If it is disabled, **right-click** the app and select "**Enable**".

![](https://file-us.ugreennas.com/admin/article/2026-06-05/e212015eb8bc497e84d68bd3fa32b91e.webp)

**macOS:**

1. In the **Dock** at the bottom of the Mac screen, find the running **UGREEN NAS** app icon.

2. **Right-click** the icon, or tap it with two fingers, then select "**Options**" > "**Open at Login**" from the pop-up menu.

If this option has a check mark (✓), system-level startup permission has been enabled successfully.

![](https://file-us.ugreennas.com/admin/article/2026-06-05/db4a219a87e0408e80fac04406509004.webp)
