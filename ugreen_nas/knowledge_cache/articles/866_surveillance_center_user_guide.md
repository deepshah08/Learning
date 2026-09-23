# Surveillance Center User Guide

> **Article ID**: `866`  
> **Category**: `Application Guide > Surveillance Center > Surveillance Center User Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/866  

---

**Applicable models**: DH Series (excluding DH2600), DX Series (excluding DX4600 Series), DXP Series, and iDX Series.

**Applicable clients**: UGREEN NAS PC client and web browser

**Applicable version**: UGOS Pro firmware 1.18.0.0049 and later

The screenshots in this article are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

**Surveillance Center** is a professional security monitoring app that turns your NAS device into a powerful network video recorder (NVR). You can use this app to add IP cameras, record videos, play back historical recordings, and manage user access permissions.

## Installation and Access

1. Open the "**App Center**" and find "**Surveillance Center**".

2. Click "**Install**" and follow the on-screen instructions to complete the setup.

3. Once installed, click the icon on the desktop or in "**All**" to open it.

## Add Cameras

Surveillance Center supports network cameras that use standard ONVIF and RTSP protocols. Some cameras that use manufacturers' proprietary protocols may not be supported.

After entering the app interface, you can add cameras in either of the following ways: "**Search cameras**" or "**Add manually**".

![](https://file-us.ugreennas.com/admin/article/2026-07-29/b3251f7073734bd4a813815e0a7802dd.webp)

### Method 1: Search Cameras

1. Click the "**Search cameras**" button. The system will automatically search for cameras on the LAN that support and have enabled the ONVIF protocol.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/66984bd7342546dc9a43b7b4fb291d6e.webp)

2. Select the target camera, then enter the username and password for authentication.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/8a9390f376fe4c2294e57d21cece064b.webp)

3. Once verified, set the camera's "Video storage location", "Retention period", "Capacity limit", "Event type" (recording mode, such as all events), and "Location" (such as bedroom). Then click "**OK**" to finish adding the camera.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/1fb940d1383047b781a62d6a1083ecca.webp)

### Method 2: Add Manually

If the camera is on a different network segment, it may not be found through automatic search. In this case, you can add it manually.

1. Click the "**Add manually**" button.

2. Select the protocol type (ONVIF, for example), enter the camera's "**IP address**", "**Username**", and "**Password**", then click "**Next**" to connect.

**Note**: ONVIF and RTSP are communication protocols used by cameras. Select the corresponding protocol based on the protocols supported by your device. If you are unsure whether your camera supports these protocols, contact the camera manufacturer for confirmation. Some camera brands use proprietary protocols and cannot be connected through standard protocols.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/0da9a978f98a470dabb7c75ad136d870.webp)

3. **Optional**: Once connected, if the camera has multiple channels, select the channel you want to add on the camera settings page, then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-07-29/e37e70355dba49d0952bc7309c67d69b.webp)

4. Set the camera's "Video storage location", "Retention period", "Capacity limit", "Event type" such as all events, and "Location" such as bedroom. Then click "**OK**".

![](https://file-us.ugreennas.com/admin/article/2026-07-29/4664d5d253c24a45a28c4e90facceae3.webp)

5. Click "**Done**". The camera is added successfully.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/0cd018c533244dfd9a921dc783c86d79.webp)

**Note**: To add more cameras, click the "**+**" button on the left side of Surveillance Center.

## View Live Monitoring and Playback

### Live Monitoring

On the app homepage, you can view the live feeds from all cameras. Cameras will also start recording automatically.

● Supports switching between **multiscreen view** and **single-camera view**.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/742a91be371f4e0e8dcb394f75121a5d.webp)

● In multi-channel mode, you can view **all channels** or **switch to a specific channel**.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/3af2ffe4107945379595d5fc39c13894.webp)

● Hover over the video feed to **mute** or unmute audio, adjust the **video resolution**, take **screenshots**, and hide or show **Pan-Tilt-Zoom** controls, if available.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/857224891c554036a1f93334c8e4b3ba.webp)

● Supports remote control of the camera direction and zoom level through **Pan-Tilt-Zoom** control (requires camera support for this feature).

![](https://file-us.ugreennas.com/admin/article/2026-07-29/6fe0a202b24749948d76988053307844.webp)

### Video Playback

Click the specified camera to view the live recording. Hold Ctrl and scroll the mouse wheel to quickly zoom in or out on the timeline at the bottom. Move the timeline to a specific point in time to view the recorded footage.

● Click the "**View Playback**" button to switch between **Live** mode and **Playback** mode.

● In **Playback** mode, playback speed can be adjusted from 0.5X to 16X.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/eb32cd906df1446f82cd95bb20862f57.webp)

● On the right side of the surveillance playback timeline, different colors are used to indicate event detection types, making it easier to quickly locate and filter recordings.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/71af4a278941449b9d3ab5c4c25ded39.webp)

● Click the **Date** in the lower-left corner to open the calendar and jump to a specific time. Dates with recordings available are marked. You can also drag the timeline to view recordings.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/b3086451be8f4d1eabf19d9d1cacbcff.webp)

## View All Events and Recent Events

### View All Events

Click "**All events**" on the app homepage to access the All Events list. The following operations are supported:

![](https://file-us.ugreennas.com/admin/article/2026-07-29/476a677922e040cd87adac4e98a994a0.webp)

● Search for specific events quickly using **keywords** (such as names).

● Filter and find events by combining conditions such as **channels**, **times**, **events**, or **identities.**

### View Recent Events for a Single Camera

Click "**Recent events**" on the right side of the target camera view to open the Recent Events list. The following operations are supported:

● Search for specific events quickly using **keywords** (such as names).

● Filter and find events by combining conditions such as **times**, **events**, or **identities**.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/f74e2d23042f4b5fb0147b9486938a9a.webp)

## Video File Management

By default, the system generates a new recording file every 10 minutes. On the homepage, select the target camera and click "**View videos**" in the upper-right corner to display the list of recorded videos.

● Supports entering keywords (such as names) to quickly search for recording files.

**Note**: The AI detection feature must be enabled first.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/4a12c98bca524a4ea732a922b6fd3e0f.webp)

● Click the **time** to switch dates.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/7c8f9c6af6ed42849de5db0ec2278b6c.webp)

● Supports filtering the recording list by channel, if multiple channels are available.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/a94e31560ac84286af060578d4403f8e.webp)

● Click the "**Edit**" icon and select multiple recording files to archive them in batches by copying the files to a specified NAS folder, download them to your local device, or delete them.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/ec3687686131448682599d8806c6e1a6.webp)

● Click the "**Filter**" icon to filter recordings by "**All videos**" or "**Events only**". Event-only recordings can also be filtered by event type.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/f7912a0f73f849428e445c648187ebd9.webp)

**Additional Information**:

● **Event recordings** refer to recordings that are specially marked as "**Event**" when the camera detects abnormal situations.

● **The 9 supported general event detection types include**: Flame detection, Detection zone entry, Detection zone exit, Face detection, Scene change, People detection, Vehicle detection, Package detection, and Pet detection.

● **Events supported by local AI detection include**: People detection, Vehicle detection, Package detection, and Pet detection.

● Supports viewing the recording list between "**Grid**" view and "**List**" view.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/2d3e6b2b3ccd4e209784e196eab96aa5.webp)

### Sort Multiscreen Layout

On the app homepage, select the "**Multiscreen**" display area. For a multi-channel camera, click the "**Sort**" icon in the upper-right corner, then drag the channels to adjust their order.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/6c895d865c554d9f966fcb6f0b93fd47.webp)

## Camera Settings

On the app homepage, select the target camera and click the "**Camera Settings**" icon in the upper-right corner to enter the settings page. You can view camera information and modify settings.

**Storage Settings**

You can modify the recording storage location, storage duration limit (for example, automatically overwrite recordings after 7 days), storage capacity limit (for example, automatically delete the oldest recordings when storage reaches 500 GB), and recording event type (for example, 24/7 recording or event recording only).

![](https://file-us.ugreennas.com/admin/article/2026-07-29/2185cce343874537be14570f354dd2c1.webp)

**Other Camera Settings**

● Supports setting or changing the camera location name.

● Supports enabling or disabling Smart Detection.

● Supports removing a single camera or all cameras in Camera Management.

**Note**: Removing a device does not delete its historical recording files by default. To view these recordings, click "**Video files of removed camera**" on the app homepage.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/7ec20ed986a44dc5ae83ce7c189a0948.webp)

## Global Settings

Administrators can configure Surveillance Center access permissions, notification settings, and AI detection-related features on the settings page.

### Access Permission Settings

1. Click the "**Settings**" icon in the lower-left corner of the interface.

2. Select "**Surveillance Center access permissions**", choose the target standard user, and enable the corresponding permissions:

● **View only**: Users can view surveillance and playback, but cannot modify any settings.

● **Access denied**: Users cannot access the Surveillance Center app.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/cfa172325b8f4c4eb1508c265ea42250.webp)

### Notification Settings

On the settings page, select "**Surveillance Center notification**" and enable the notification types you want to receive. The system will automatically send notifications when events are detected.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/1308c85c692a4ed488e46b778d1edf4d.webp)

### Enable AI Detection in Surveillance Center

After enabling AI detection, recordings will be analyzed by UGREEN NAS local AI models to identify key events and generate notifications or alerts without uploading any data to the cloud.

**Note**:

● When using the AI detection feature in Surveillance Center for the first time, you need to enable the model in the "**Model Management**" app and authorize it for Surveillance Center. After authorization, you can enable the corresponding AI detection capabilities for cameras as needed in the camera settings.

● Cameras connected through ONVIF and RTSP protocols currently support enabling local real-time AI detection.

On the settings page, select "**Local AI Detection**". In the device list, select the camera for which you want to enable AI detection, then click "**Not enabled**" to open the AI detection options list.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/36d86fd2e09141678816f478a5a2f61f.webp)

Select the AI detection options you want to enable, such as People detection (Face recognition), Pet detection, and Vehicle detection. The supported AI detection capabilities depend on the actual camera model.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/7043425b67d3405cbeb303df3dbde5de.webp)

**Additional Note**:

Different NAS models have different AI computing capabilities. Therefore, the supported AI detection features and the number of cameras that can enable AI detection simultaneously (that is, the number of AI detection tasks) may vary. When the maximum number of tasks is reached, disable AI detection for an existing camera before enabling it for a new camera.

#### View AI Detection Results

After enabling AI detection, when key events are detected, the corresponding AI indicators will be displayed on the camera view. Click "**Recent Events**" to view AI detection details.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/c13cbc980f4647308cf700eeb417458e.webp)

### Face Recognition

On the "**Face recognition**" page, you can view and register all faces captured by cameras, and manage them by categories: "**Known people**" and "**Strangers**".

On the "**Strangers**" list page, select the face you want to register and enter a name to complete the registration. The face will then be automatically moved to the "**Known people**" list.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/e05e2c9d934a4600bb9b7a067becdfd3.webp)

On the "**Known people**" list page, click the "**pencil**" icon on the target face avatar to edit person information, including renaming, moving the person to Strangers, and deleting the person.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/5b90956d68234eed857f7d787ea699f2.webp)

Select multiple face avatars to batch merge or delete the corresponding faces.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/80678ca009f742c6bc413699eb5f473e.webp)

#### Manually Add Known People

If a face is not automatically captured, you can add known people by taking photos with your phone or uploading local images.

1. Click the "**Settings**" icon, select "**Face recognition**", and click the "**Manual Add**" icon in the upper-right corner of the page.

**Note**: Follow the on-screen instructions to allow "**Surveillance Center**" to enable the Large Language Model and Multimodal Model.

2. According to the image upload requirements, click "**Upload**" to upload a photo of the "Known people" from your local device.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/049153728bc0486e80dbe74b38479079.webp)

3. After the upload is complete, enter the person's name to register the person. Click "**Done**" to view the registered person in the Known people list.

![](https://file-us.ugreennas.com/admin/article/2026-07-29/74cd25db8ff340b7a75b504ee650a02c.webp)

## Related Articles

[Surveillance Center FAQs](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmODc5IiwiY2xpZW50VHlwZSI6IkNPTU1PTiJ9)
