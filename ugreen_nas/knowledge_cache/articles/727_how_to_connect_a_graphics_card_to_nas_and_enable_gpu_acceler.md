# How to Connect a Graphics Card to NAS and Enable GPU Acceleration?

> **Article ID**: `727`  
> **Category**: `Troubleshooting > Hardware Failure > How to Connect a Graphics Card to NAS and Enable GPU Acceleration?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/727  

---

## Applicability

**Applicable client:** UGREEN NAS PC client (Windows/macOS).

**Applicable version:** NAS firmware 1.16.0.0042 or later.

This article is for reference only. The actual interface and operation paths may vary slightly depending on system or app version updates. Please refer to the actual interface.

## Overview

Some UGREEN NAS models with Thunderbolt ports support connecting an external NVIDIA graphics card through a GPU enclosure. With the official driver installed, GPU processing power can be used in supported apps, such as "**Photos**", to significantly improve smart model recognition and data processing performance.

## Supported NAS Models

Before connecting the hardware, make sure the NAS model meets the requirements. If the model is not supported, NVIDIA-related drivers will not appear in "**App Center**", so they cannot be installed.

● DXP series: DXP480T Plus, DXP6800 Pro, and all DXP8800 series models

● iDX series: iDX6011 and iDX6011 Pro

## Preparations

**Hardware requirements**:

● A discrete graphics card compatible with NVIDIA driver version 550.144.03 or later. For the full list of supported GPUs, refer to NVIDIA's official [compatible GPU list](https://www.nvidia.com/en-us/drivers/details/238872/) .

![](https://file-us.ugreennas.com/admin/article/2026-06-10/4482028742c444c1b4ff8cf9ddc93248.webp)

● A GPU enclosure that supports Thunderbolt.

● A standard Thunderbolt data cable.

**Software requirement:** The "**Photos**" app must be updated to **V1.6.0.1289 or later**.

![](https://file-us.ugreennas.com/admin/article/2026-06-10/f6e18c4a81464ce99bbd6188a71ae6c4.webp)

## Hardware Connection and Driver Installation

1. Install the NVIDIA graphics card into the GPU enclosure, then connect the enclosure to power.

2. Connect the GPU enclosure to the Thunderbolt port on the NAS using a Thunderbolt cable.

3. Sign in to the system desktop, open "**App Center**", then search for and install "**NVIDIA Driver**" and "**NVIDIA Toolkit**".

**Note**: Do not hot-plug the graphics card while it is powered on or in use. This may cause system errors, data corruption, or permanent damage to the graphics card.

## Enable GPU Acceleration in Photos

After the driver is installed, GPU acceleration must be enabled inside the app.

1. Open "**Photos**", go to the settings page, then switch to the "**AI settings**" tab in the top bar.

2. Turn on "**GPU acceleration**".

If no graphics card is detected, or if "**NVIDIA Driver**" and "**NVIDIA Toolkit**" are not installed, this option will be hidden.

![](https://file-us.ugreennas.com/admin/article/2026-06-10/af2e1e5d3e0740b691b5c23307b94ba6.webp)

3. In the smart model list below, enable the models that need to run, such as "**People recognition**".

4. After setup, all future recognition tasks in "**Photos**" will use the external GPU for acceleration.

GPU load and working status can be checked at any time in "**Task Manager**".

![](https://file-us.ugreennas.com/admin/article/2026-06-10/1dec9ba9afbb42eeba59f0fdf79b6b06.webp)

## FAQs

If an issue occurs during setup or use, check the following scenarios:

1. **"NVIDIA Driver" or "NVIDIA Toolkit" cannot be found in App Center**

The current NAS model does not support external GPU expansion at the hardware level. Check the supported model list above.

2. **The graphics card is connected, but "GPU acceleration" does not appear in Photos**

The NAS may not have detected the graphics card. Check whether the Thunderbolt cable is firmly connected, whether the GPU enclosure is powered on properly, and whether the graphics card model is included in the compatibility list for the official driver.

3. **Driver installation fails or the app needs to be repaired**

This is usually caused by a driver version conflict or corrupted components due to an interrupted download. In "App Center", uninstall the damaged "NVIDIA Driver" or "NVIDIA Toolkit", then download and install it again.

4. **The graphics card suddenly stops working during use**

This may be caused by a loose Thunderbolt connection or accidental hot-plugging. Check the physical cable connection immediately. If the system process is stuck because of the interruption, reconnect the cable and restart the NAS to recover.
