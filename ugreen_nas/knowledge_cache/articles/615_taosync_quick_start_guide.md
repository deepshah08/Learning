# TaoSync Quick Start Guide

> **Article ID**: `615`  
> **Category**: `Application Guide > Docker > Docker Gameplay > TaoSync Quick Start Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/615  

---

**Applicable Version:** UGOS Pro 1.10.0.0092 and above

Screenshots and interfaces in this document are for reference only. Actual displays may vary depending on system or application version. Some features may change across versions, please refer to your actual interface.

## App Overview

TaoSync is an automated synchronization tool designed for OpenList v3, allowing you to set up sync and backup tasks between a NAS and cloud drives, or between multiple cloud drives.

TaoSync supports the following features:

1. **File synchronization and backup**: Supports backing up local files to multiple cloud drives or FTP servers, as well as syncing files between multiple cloud drives. It regularly scans specified directories to detect file differences and performs synchronization accordingly.

2. **Scheduled tasks**: Allows setting specific execution times using `cron` (year, month, day, hour, minute, second). When the system is idle, it automatically downloads files from specified cloud drives to the local NAS.

**Note:** Before using TaoSync, please make sure to install and configure the OpenList application first.

![](https://file-us.ugreennas.com/admin/article/2025-12-01/4ce5f4a7aa104dd9b2fca1c89e4023af.webp)

## Installation Guide

To install the TaoSync application, follow these steps:

1. Open the [App Center], find the TaoSync app in the list, and click the "Install" button.

2. Follow the on-screen instructions to complete the installation. During the installation, please ensure your network connection is stable to avoid any interruptions.

## User Guide

1. After installation, open the TaoSync application, or open a browser within the local network and visit `http://<NAS_IP>:30023`, replacing `<NAS_IP>` with the actual IP address of your NAS.

> You can find your NAS device's IP address by going to [Control Panel] > [Network] > [Network connection].

![](https://file-us.ugreennas.com/admin/article/2025-12-01/197257fbd33542c2909669dabe98bb26.webp)

2. Visit the TaoSync login page and log in using the default username and password.

> Please change the default password as soon as possible upon first use to ensure security.

![](https://file-us.ugreennas.com/admin/article/2025-12-01/d886296f9b4c447d8dc5200c6c2010cd.webp)

## Configure the OpenList Engine

Before creating backup tasks, you need to add OpenList as the engine. **TaoSync does not come with OpenList integrated**, so you must first install and configure it.

1. Go to the **[Engine Management]** page.

2. Click the **"Add"** button, then enter the **OpenList access URL** and **token**.

3. After configuration, click **"Sure"** to save the settings.

![](https://file-us.ugreennas.com/admin/article/2025-12-01/daca6cc03fec4a12a5897b798fca2d06.webp)

4. To obtain the token, go to **"Set up"** > **"Other"**, then click **"Copy the token"** to get it.

![](https://file-us.ugreennas.com/admin/article/2025-12-01/9bf29971c0f24971a5ee962f04ffea08.webp)

## Create a Backup Assignment

After configuring the engine, create a backup task as follows:

1. Go to [Job management], and click "+ Add new assignment" to start a backup task.

2. In the popup window, select the previously added engine.

3. Choose the **[Source Directory]** (the folder to be backed up).

4. Choose the **[Target Directory]** (you can select multiple storage locations).

5. Set the synchronization method: using **scheduled execution (cron)** will run the task automatically at the preset times. Using **interval execution** requires manually starting the first synchronization, then it will run repeatedly at the set intervals.

6. Click **"Confirm"** to start the task.

![](https://file-us.ugreennas.com/admin/article/2025-12-01/80f837b60a1941fe9194cd602aa0a377.webp)

**Note:** If the number or size of backup files is large, the initial synchronization may take a long time. It is recommended to perform this during periods of low system load to minimize impact.

## Change Username and Password

To ensure security, please change the default username and password promptly after the first login. In the sidebar, click **[System Settings]**, enter the **old password**, then set a **new password** and click "Change Password" to apply the changes.

![](https://file-us.ugreennas.com/admin/article/2025-12-01/dd0eec46991a44f085b35bf964eeebff.webp)

## Notes

When using the UGOS Pro system and container applications, please note the following:

● Do not arbitrarily migrate, move, rename, or delete NAS paths mounted by containers, as this may cause functional errors or data loss.

● When accessing container applications via a browser, please disable the "Multiple gateways" option under [Control Panel] > Network to avoid network conflicts.

● Container applications are suitable for beginners to use quickly. If you need more flexible storage and access control, it is recommended to deploy using Docker.
