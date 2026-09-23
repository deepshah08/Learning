# How to Adjust Fan Mode and Fan Speed Curves？

> **Article ID**: `882`  
> **Category**: `Application Guide > Control Panel > Hardware & Power > How to Adjust Fan Mode and Fan Speed Curves？`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/882  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: NAS Firmware 1.17.0.0034 or later

**Feature Support**: Currently, only the **DXP4800** supports custom fan speed curves. Support for additional models will be added in future updates

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

UGREEN NAS allows users to adjust the device's fan mode. Some models also support custom fan speed curves, allowing different fan speeds to be set based on the device temperature.

## Configure Cooling Fan Settings

1. Open "**Control Panel**", click "**Hardware & Power**", then find "**Cooling fan**" under the "**General**" tab and click "**Settings**" on the right.

![](https://file-us.ugreennas.com/admin/article/2026-08-19/b14443618d904f45b024b127023a42eb.webp)

2. On the Cooling fan page, you can adjust the fan speed curve under Custom or switch to a Preset mode.

![](https://file-us.ugreennas.com/admin/article/2026-08-19/99342c6673ea41bf82ace50417e3e478.webp)

## Customize the Fan Speed Curve

Under the Custom tab in Cooling Fan settings, the system displays a fan speed curve. The horizontal axis represents device temperature, and the vertical axis represents fan speed. Drag the control points on the curve to set the fan speed for different temperature ranges. After adjustment, click "**Confirm**" to save.

## Custom Fan Speed Limit Description

To ensure adequate cooling and system safety, the following limitations apply to custom fan speed curves:

● After a temperature range reaches its upper limit, the fan speed cannot be reduced beyond the allowed limit.

● Fan speeds assigned to higher temperature ranges cannot be lower than those assigned to lower temperature ranges.

If a control point cannot be moved, the current settings have reached a system protection limit.

The system continuously monitors the temperatures of the CPU, HDD, SSD, and other hardware components, and adjusts the fan speed according to the highest detected temperature.

Temperature thresholds:

● CPU: 80°C

● HDD: 55°C

● SSD: 70°C

When any component reaches its threshold, the system displays a notification and automatically switches the fan to Full Speed mode. Fan speed curve adjustments are unavailable until the temperature returns to a safe range.

## Select a Preset Fan Mode

On the Cooling Fan settings page, click "**Preset mode**" and choose one of the following modes:

● Auto: The system automatically adjusts the fan speed based on device temperature. Recommended for daily use.

● Quiet: The fan runs at a lower speed to reduce device noise. Cooling efficiency may be reduced in this mode.

● Full speed: The fan runs at full speed to improve cooling efficiency. This mode may produce louder noise.

After selecting a mode, click "**Confirm**" to save the settings.

![](https://file-us.ugreennas.com/admin/article/2026-08-19/973d92fa2240458a9d16cf2d0fa07940.webp)

## Fan Mode Recommendations

● For daily use, **Auto** mode is recommended.

● If the device is placed in a quiet environment, such as a bedroom or study, use **Quiet** mode.

● If the device runs under heavy load for a long time, or if the ambient temperature is high, use **Full speed** mode.

To balance noise and cooling performance, use "**Custom**" mode on supported models.
