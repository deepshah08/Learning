# Introduction to Sync & Backup

> **Article ID**: `237`  
> **Category**: `Application Guide > Sync & Backup > Introduction to Sync & Backup`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/237  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client, Web Browser

**Applicable Version**: UGOS Pro 1.18.1.0098 or later

The screenshots in this document are for reference only. The actual interface may vary slightly depending on the system or app version, please refer to the actual interface displayed.

## Introduction

UGOS Pro provides data sync and backup features to help keep your data consistent across multiple devices and provide additional protection for important files.

● **Data Sync**: Establishes sync connections between UGREEN NAS and other devices (such as a local computer or another UGREEN NAS). Any data changes made on one device will be automatically synced to other devices, ensuring **data consistency** across all devices and preventing version conflicts.

● **Data Backup**: Supports backing up data to various destinations, including local UGREEN NAS, local computers, other devices that support rsync services, and between storage pools. This meets different **data protection** needs and helps prevent data loss caused by unexpected situations.

**Note**: In the Sync & Backup app, "**Sync**" and "**Backup**"are two independent modules. Sync is mainly used for **real-time file synchronization** between multiple devices, while Backup is used for **one-way data protection**. You can use both features together according to your needs to improve data security.

## Overview

● **Overview**: On the Overview page, you can view the status of all current sync and backup tasks, as well as connected device information and online status (including local and remote UGREEN NAS devices, remote file servers, and more). You can also remove connected devices.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/8534d00ebfa54539b08b1a504313e736.webp)

**Note**: When removing a device connection, all sync and backup tasks associated with that device will also be deleted. Please confirm carefully before removing a device to avoid affecting important data protection tasks.

● **Sync**: Click "**Sync**" in the sidebar to create sync tasks, view task details and running status, edit or delete tasks, stop tasks, or run tasks immediately.

● **Back up & Restore**: Click "**Back up & Restore**" in the sidebar to create backup tasks, view task details and running status, edit or delete tasks, stop tasks, run tasks immediately, and restore backup tasks or files.

● **Log:** Click "**Log**" in the sidebar to view all transfer and operation records of sync and backup tasks, helping you track task execution and quickly troubleshoot issues.

● **Administrator Settings**: On the Administrator Settings page, you can centrally manage advanced settings for sync and backup tasks. These settings mainly include General settings and Speed limit, allowing administrators to flexibly adjust configurations according to different scenarios and optimize system performance.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/d216074968c94dcba1f69689d3275925.webp)

**Notes**:

● After enabling administrator mode, administrators can view and manage other users' connections on the overview page.

● After enabling version retention, the system will automatically retain historical file versions for personal folder andshared folder associated with sync tasks to protect synced data. For more settings, refer to "[File Version Explorer](https://support.ugnas.com/knowledgecenter/detail/article/zh-CN/316) ".
