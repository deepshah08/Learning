# How to Manually Update the Firmware of UGREEN UPS

> **Article ID**: `704`  
> **Category**: `Application Guide > Control Panel > FAQ > How to Manually Update the Firmware of UGREEN UPS`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/704  

---

**Applicable Version:** UGOS Pro firmware 1.14.10.0037 and above

**Note:** Screenshots and interfaces in this document are for reference only. Actual displays may vary depending on system or application version. Some features may change across versions, please refer to your actual interface.

## Feature Overview

UGREEN has designed multiple UPS (Uninterruptible Power Supply) models specifically for NAS devices. These UPS units enable seamless power switching during unexpected outages, providing emergency power to the NAS and preventing data corruption or hard drive damage caused by sudden power loss.

To ensure UPS stability, compatibility, and optimal performance, it's recommended to keep the UPS firmware up to date. This article provides a step-by-step guide for manually updating UGREEN UPS firmware.

**Notes:**

● This tutorial applies only to **official UGREEN UPS devices**.

● Please obtain firmware files exclusively from the [UGREEN Download Center](https://nas.ugreen.com/pages/downloads) or official technical support channels. Do not use firmware from unverified sources, as doing so may cause permanent damage to your device.

● If you are using a third-party UPS, contact the manufacturer to confirm whether firmware updates are supported and how to perform them.

● Before starting the update, ensure that the UPS is properly connected to the NAS, and avoid disconnecting the power or data connection during the update process.

## Downloading UPS Firmware

Before performing a system upgrade, you need to obtain the latest firmware file from the official website.

**Prerequisites**: Ensure that your NAS is correctly connected to the UGREEN UPS via a UPS communication cable, and that the NAS system has successfully recognized the UPS device.

![](https://file-us.ugreennas.com/admin/article/2026-04-16/0ba4d665eab34c2a98b89bc705b71970.webp)

**Steps**:

1. Visit the official UGREEN website and navigate to the "[UGREEN Download Center](https://nas.ugreen.com/pages/downloads) ".

2. Under "**Select model**", select "**UPS**". Then, from the "**product model**" list, choose the UPS model you purchased to enter its dedicated page (e.g., **US3000**).

![](https://file-us.ugreennas.com/admin/article/2026-04-16/88f4f85f30b24ca3a5d03b467c0aa33f.webp)

3. After being redirected to the corresponding firmware download page, click the "**Download**" button.

![](https://file-us.ugreennas.com/admin/article/2026-04-16/770eca085aee4334ad6d84d1068eb7f3.webp)

4. Save the latest UPS firmware file to your local computer for the subsequent upgrade. The firmware file typically provided in `.bin` format.

## Updating UPS Firmware

1. Log in to the NAS client and open"**Control Panel**">"**Hardware & Power**">"**UPS**".

2. Verify that the system has successfully detected the UGREEN UPS device. You will view information such as current battery capacity and remaining available time on the interface.

![](https://file-us.ugreennas.com/admin/article/2026-04-16/aee59415b1084fce858d51235b3129c9.webp)

3. In the UPS information section, locate the "**Current firmware version**" field and click "**Manual update**".

4. In the pop-up window, click "**Browse**", select the `.bin` firmware file you downloaded, and click "**Confirm**" to begin verification and upgrading.

Do not operate the device or disconnect the power during the upgrade process.

![](https://file-us.ugreennas.com/admin/article/2026-04-16/1d9842f74965433da4871ada07c8be0d.webp)

## Restart Device

After the firmware has been successfully upgraded, you **must** restart the devices in the following order to ensure the new firmware takes effect properly:

1. Shut down the NAS properly.

2. Unplug the UPS power cord from the AC outlet.

3. Press and hold the power button on the UPS to completely power it off.

4. Wait a few seconds after the UPS is turned off, then plug the power cord back in and press the power button to turn it on.

5. Once the UPS has started up normally, power on your NAS.

**Button Operation Instructions:**

● Power on/Mute: Single press

● Power off: Press and hold for 10 seconds

● Enter power-saving mode: Double press

## FAQs

**Q1: What if the upgrade fails?**

A:Ensure the firmware file is the original one provided by UGREEN and that it is complete. If the issue persists, contact UGREEN technical support.

**Q2: Will data be lost after the upgrade?**

A: No. The firmware upgrade only affects the UPS module and does not impact data stored on the NAS.

**Q3: The UPS battery level is too low to support manual firmware updates**

A: **The UPS battery capacity must be at least 50% before upgrading.** Wait until the battery is above 50% and then try the manual update again.

![](https://file-us.ugreennas.com/admin/article/2026-04-16/03a77e56ff3d4c8fbb87988fc07d62db.webp)
