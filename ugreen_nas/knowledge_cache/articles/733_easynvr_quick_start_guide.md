# EasyNVR Quick Start Guide

> **Article ID**: `733`  
> **Category**: `Application Guide > Docker > Docker Gameplay > EasyNVR Quick Start Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/733  

---

# App Introduction

**EasyNVR** is an NVR (Network Video Recorder) management software compatible with various types of cameras. It supports bulk device access and centralized control, provides **real-time video preview and playback**, and offers device status monitoring with anomaly alerts to help users promptly identify and resolve potential issues.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/7b5aa73374f04714ac08291da470bdf8.webp)

## Supported Devices and Protocols

### Supported Camera Manufacturers

EasyNVR is compatible with a wide range of devices from various manufacturers, including but not limited to Hikvision, Dahua, Uniview, Ezviz, Tiandy, Huawei, and other compatible devices.

### Supported Protocols

● **Access Protocols:** PULL, ONVIF, RTMP, GB28181 (National Standard)

● **Video Output Protocols:** WebRTC, FLV, HLS, WS-FLV

● **Codec Support:** Full support for H.265

**Official Website:** [EasyNVR Official Website](https://www.easynvr.com/)

**Q&A Community:** [EasyNVR Q&A Center](http://faq.tsingsee.com/tags/easynvr)

![](https://file-us.ugreennas.com/admin/article/2025-09-02/99951ffc87f54d92ab90f20e77b2c87d.webp)

## Default Access Information

● **Account:** admin

● **Password:** aadmin

● **Access Port:** 10000

● **LAN Access Example:** Enter `http://172.17.21.112:10000` in the browser's address bar, replacing `172.17.21.112`with the actual NAS IP.

You can find the NAS IP under **"Control Panel">"Network">"Network connection"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/edbcb922cb1e452d93543aa111749a19.webp)

## Install the Application

1. Open **[App Center]**, locate **EasyNVR** in the application list, and click **"Install"** to launch the installation wizard.

2. Follow the wizard instructions step by step to complete the installation.

### EasyNVR Resource Path Description

During the **EasyNVR installation wizard**, you need to select a folder as the resource path (used for mounting recorded videos, etc.). When the application is **installed or restarted**, EasyNVR will clean up the selected folder by removing files that do not belong to EasyNVR. To avoid potential risks, **it is recommended to mount the resource path to an empty folder**.

**Note:**

● Do not delete, move, or rename the recording save path; otherwise, the application may fail to run properly and might require reinstallation.

● Do not store any other files in the `easynvr_records` folder, as EasyNVR will remove any data in the mount directory that does not belong to the application.

● If you are upgrading from an older version of EasyNVR, the new version will not automatically create subdirectories by default (you can manually enable the **Automatically Create Subdirectories** feature). Upgrading will not affect your existing NVR data.

### Automatically Create Subdirectories

Within **EasyNVR settings**, you can enable the "**Automatically Create Subdirectories"** feature. Once enabled, the system will automatically generate an `easynvr_records` folder under the mounted directory, and recorded video files will be saved there.

● When enabling or disabling the **Automatically Create Subdirectories**, the system will clean up any data in the mounted directory that does not belong to NVR.

● The application will only access and manage the contents within the`easynvr_records` folder and will not directly modify the parent folder you selected.

**Steps:**

1. Go to "**Base Configuration"** ＞ "**Distribution and Video"** ＞ "**Recording Configuration"**.

2. Locate the "**Automatically Create Subdirectories"** toggle and switch it on.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/532259137c3b43988fe9e514594a1349.webp)

# User Guide

## Initial Configuration

1. Visit `http://<NAS LAN IP>:10000`in your browser, and replace `<NAS LAN IP>` with the actual NAS IP address.

2. For the first login, use the default account **admin** and password **admin** to sign in to EasyNVR.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/ff065c2da7c74edbb5bb38ab6840712d.webp)

3. After logging in, select the **network environment**. Please choose "**local area network**".

![](https://file-us.ugreennas.com/admin/article/2025-09-02/6281ed0978364eb6ad9c04f9457b8dad.webp)

4. The system will automatically detect the NAS LAN IP. Click **"Certainty"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/55e5900e9c514e4f8a57f29ae118b27a.webp)

5. Set a new account and password, then click **"Certainty"** to complete initialization.

After initialization is completed, the default account will be disabled, and you must log in to the system using the new account and password.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/196a9c3587574c7285b3fdff2766122e.webp)

## Home Overview

On the EasyNVR homepage, you can view the list of connected devices and channels, as well as hardware status information.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/12b8aaebaa48401ca5103fb362e07e8b.webp)

## Add Device

EasyNVR supports four protocols: PULL, ONVIF, RTMP, and GB28181 (National Standard).

Here we demonstrate using the ONVIF protocol with a From1bJMVd0HNYj camera. The camera has been preconfigured in the app with username, password, and IP address.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/b0dae829d4c34aa592730dddb52393ba.webp)

1. On the homepage, click **"Equipment List">"Add to"**.

2. Select **"ONVIF"** as the protocol type.

3. Enter the **device name** (model recommended), **IP address**, **username**, and **password** (consistent with the camera configuration).

4. Click **"OK"**. Once successfully added, the camera will appear in the device list.

5. Click **"List of channels"** to manage the corresponding video channels.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/714e575cb3ff440a8cf3607b0e275587.webp)

## Live Preview

1. In the **List of channels**, click **"Live preview"** to view the real-time video feed.

**Note:** Since the demonstration camera is a dual-lens model, each lens corresponds to an independent video stream, which is shown as two separate channels in the system.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/d1a8382847f5484b977c651cfc5a845b.webp)

2. If the camera supports PTZ (pan-tilt-zoom) functions, you can adjust the camera’s viewing angle in the console.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/62f2d1d1eff64b7ea4caafdc66990498.webp)

## Playback and Video Program

By default, newly added cameras do not store recordings. You need to create a recording program for the camera.

1. Return to the homepage, then click **"Video Playback">"Video Program"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/d2c10b03cccb4010a3918424e08640c5.webp)

2. EasyNVR provides three preset recording programs. Select one, click **"Associate channels"**, check the channels you want to record, and save.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/e76280dd43e74a959b397bdff5d95eec.webp)

3. Go back to **"Video Palyback"** to view the linked recording channels. Click **"view the recording"** to play back recordings.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/adef8b9ef7e14f99b08872fb941915da.webp)

## Video Tutorials

EasyNVR provides video tutorials for multiple protocols. You can find detailed instructions and demo videos for each protocol in the [Easy official tutorial documentation](https://www.easynvr.com/doc.html) .

## Notes

● EasyNVR is a third-party container application. This document is for reference only. UGREEN assumes no responsibility for any risks caused by improper operation, software vulnerabilities, or image updates, including but not limited to file anomalies, data loss, or data leaks.

● For more information on usage, configuration changes, and bug fixes, please refer to official announcements from EasyNVR.

● It is recommended to store the container app's configuration directory in storage created on an **SSD drive**, as mechanical hard drives may reduce performance due to slower read/write speeds.
