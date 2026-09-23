# How to Perform Shutdown/Reboot and Set Power Schedules on Your NAS

> **Article ID**: `855`  
> **Category**: `Application Guide > UGOS Pro > How to Perform Shutdown/Reboot and Set Power Schedules on Your NAS`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/855  

---

## Applicability

**Supported Platforms**: UGREEN NAS PC Client (Windows/macOS), Web browser, UGREEN NAS Mobile App (iOS / Android), and NAS physical device.

**Supported Versions**:UGOS Pro firmware version 1.15.12.28676 or later.

This document is for reference only. Actual interfaces and operation paths may vary depending on system or application version updates. Please refer to the actual interface displayed on your device.

## Feature Overview

For daily system maintenance, you can manage NAS power operations through multiple platforms or by using the physical power button on the device. You can also configure scheduled power on/off plans to automatically turn the device on or off at specific times, helping reduce power consumption.

## PC / Web

### Manual Shutdown and Reboot

1. On the NAS desktop, click the "**Me**" button (profile avatar icon) in the upper-right corner of the top navigation bar.

2. In the drop-down menu, click "**Shutdown**" or "**Reboot**".

![](https://file-us.ugreennas.com/admin/article/2026-05-18/1c115c11a8624a4d86bee5dcf481f0c0.webp)

3. In the confirmation dialog that appears, click the button again to confirm. The system will then begin the safe shutdown or reboot process.

### Configure Scheduled Startup and Shutdown

1. Open the "**Control Panel**" application on the system desktop, then click "**Hardware & Power**".

![](https://file-us.ugreennas.com/admin/article/2026-05-18/d5bffcb9524f43d6ac794fac2ad2ed49.webp)

2. At the top of the main panel on the right, switch to the "**Power**" tab. Locate the "**Scheduled startup and shutdown**" section and enable the feature.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/3dfe4fa330dd4a64ac0edcb76f3dbe4d.webp)

3. The system will then display the "**Add shutdown & startup plan**" window. Configure the following settings as needed:

● Frequency: Choose from Everyday, Weekdays, Weekends, or specify custom dates.

● Time: Set any exact time between 00:00 and 23:59.

● Action: Choose whether the task should "**Boot**" or "**Shutdown**" the device.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/68673cb3d8ea4839926dfc9888acd7cf.webp)

4. After completing the configuration, click "**OK**". The plan will be added to the task list.

5. Click the "**Apply**" button in the lower-right corner of the Control Panel to save the plan to the system configuration.

**Note:** Be sure to click the "**Apply**" button in the lower-right corner of the Control Panel. Otherwise, the plan will not be successfully saved to the system configuration.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/81acadd93cad4306827a1180ef78ebaa.webp)

To modify or delete a schedule later, locate the corresponding schedule entry in the "**Scheduled startup and shutdown**" section and click "**Edit**" or "**Delete**" on the right side.

## Mobile App

### Manual Shutdown and Reboot

1. Open the UGREEN NAS App and tap the device name at the top of the home page to enter the device details page.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/dba72700484c49bea6281277d5a0f5e7.webp)

2. On the device information page, tap "**Reboot**" or "**Shutdown**", then confirm the action in the pop-up dialog.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/f0b80bc60b814334b2dd1c88d75e53ba.webp)

### Configure Scheduled Startup and Shutdown

1. Open the "**Control Panel**" application in the UGREEN NAS App and tap "**Hardware & Power**".

![](https://file-us.ugreennas.com/admin/article/2026-05-18/7bb10b384b7442ac8099cc6ab13b5dcb.webp)

2. Locate and enter the "**Scheduled startup and shutdown**" page, then enable the master switch in the upper-right corner.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/80c483dd4490452b82ef181419e797b2.webp)

3. The schedule configuration window will appear. Configure the frequency, time, and action (Boot or Shutdown), then tap "**OK**".

![](https://file-us.ugreennas.com/admin/article/2026-05-18/e7b6e44fea6d4744a880deef77cb75de.webp)

4. The system will add the schedule to the list and automatically execute it at the specified time.

To modify or delete a schedule later, simply tap the existing schedule on the "**Scheduled startup and shutdown**" page.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/bfc6417f83b74edd906b585992ad1be3.webp)

## Using the Physical Power Button

If you are near the NAS device, you can use the physical button on the chassis to shut it down.

**Steps**:

Locate the Power button on the device. **Press and hold** the button for approximately **10 seconds** until you hear a "**beep**" from the device, then release the button. The NAS will automatically begin the safe shutdown process.

**Note**: To protect hard drive data integrity, it is recommended to use the software-based "**Shutdown**" function whenever possible, except in emergency situations where the device becomes unresponsive.
