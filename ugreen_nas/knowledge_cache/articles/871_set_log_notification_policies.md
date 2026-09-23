# Set Log Notification Policies

> **Article ID**: `871`  
> **Category**: `Application Guide > Logs > Set Log Notification Policies`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/871  

---

## Applicability

**Applicable client:** UGREEN NAS PC client (Windows/macOS).  
**Applicable version:** NAS firmware 1.16.0.0042 and later.

This article is for reference only. The actual interface and operation path may vary slightly due to system or app version updates. Please refer to the actual interface.

## Overview

To receive real-time alerts, select “Enable automatic notification policy” in the “Logs” app and allow “Logs” to send system notifications. Logs that trigger the policy will then be pushed to the system message list.

## Enable Automatic Notification Policy

When the system triggers a serious error or a specified sensitive operation occurs, this feature allows the system to send automatic unattended alerts.

1. In the left sidebar, click “**Notification**” to go to the “**Policy Configuration**” tab, then select “**Enable automatic notification policy**”.

2. Configure the content filter conditions as needed. Filters by “Keyword”, “Level” (for example, only “Serious”), “Module”, or “User” are supported. Click “**Apply**” to save the settings.

After the rule takes effect, when a new log matches the configured conditions, the system will automatically send a system notification. Switch to the “Notification Records” tab to view the full history of triggered automatic alert logs in chronological order.

![](https://file-us.ugreennas.com/admin/article/2026-06-05/2ef198a0c6074e75a04daa3c11cd3955.webp)

## Manage System Message Notifications

1. Log in to the system desktop and click “**Notifications**”>“**Settings**” in the top bar to open the notification management page.

![](https://file-us.ugreennas.com/admin/article/2026-06-05/0820c0db8d464d2d90f48e12bffadfe1.webp)

2. In the list of apps allowed to send notifications, find “**Logs**” and turn on the switch on the right.

![](https://file-us.ugreennas.com/admin/article/2026-06-05/2fab422f780b4a14849f30424f94ae1a.webp)

The setting takes effect immediately. Any future logs that meet the alert conditions will be pushed to this message center, so important system notifications will not be missed.
