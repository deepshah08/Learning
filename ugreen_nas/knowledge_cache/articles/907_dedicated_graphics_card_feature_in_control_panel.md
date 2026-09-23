# Dedicated Graphics Card Feature in Control Panel

> **Article ID**: `907`  
> **Category**: `Application Guide > Control Panel > Hardware & Power > Dedicated Graphics Card Feature in Control Panel`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/907  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS).

**Applicable Version**: NAS Firmware 1.18.0.0073 or later.

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

Some UGREEN NAS models support external Dedicated graphics cards. A Dedicated graphics card can be used by Docker containers or assigned to virtual machines through the "**Hardware passthrough**" feature.

The NAS device must be equipped with a Thunderbolt port, OCuLink port, or PCIe slot. The discrete GPU can be connected to the NAS through a GPU expansion dock or directly through a PCIe slot.

## Before Use

Before using a Dedicated graphics card, make sure the following requirements are met:

● The NAS firmware version has been updated to **V1.18.0.0073** or later.

● The Dedicated graphics card is connected to the NAS through a graphics card expansion dock or PCIe slot.

● The NAS device supports the corresponding interface and Dedicated graphics card capabilities.

To check whether your NAS supports an external Dedicated graphics card, refer to the hardware specifications of your device. Make sure the device is equipped with one of the following interfaces:

● Thunderbolt port

● OCuLink

● PCIe slot

You can check the hardware specifications of your device in the[UGREEN NAS Private Cloud Product Center](https://www.ugnas.com/products?pg=1&product_type=nas&category=) , or contact UGREEN Cloud Technical Support for confirmation.

## Graphics Card and Graphics Card Expansion Dock Compatibility

For compatibility information about graphics card expansion docks, refer to the [UGREEN Cloud Hardware Compatibility Instructions](https://www.ugnas.com/compatible) .

Actual compatibility depends on the NAS hardware, graphics card model, connection method, driver version, and system version.

Even if a Dedicated graphics card is connected to the NAS, whether it can be properly used by a virtual machine still depends on the device hardware, system version, driver support, and virtual machine configuration.

## Check Whether the Dedicated Graphics Card Is Detected

After connecting a Dedicated graphics card to the NAS, you can check its detection status in Control Panel. Follow the steps below:

1. Open **Control Panel** and click "**Hardware & Power**".

2. Go to the **Dedicated graphics card** page.

If the Dedicated graphics card information is displayed, the NAS has successfully detected the graphics card.

If the **Dedicated graphics card** entry is not displayed, the system has not detected the Dedicated graphics card. Check the graphics card connection, graphics card expansion dock connection, power supply status, and device compatibility.

## Dedicated Graphics Card Work Mode Description

The default work mode of the Dedicated graphics card is **NAS system**.

The corresponding work modes for different usage scenarios are as follows:

● **Docker containers using Dedicated graphics card**: Keep the work mode as **NAS system**.

● **Virtual machines using Dedicated graphics card through Hardware Passthrough**: Switch the work mode to **VM passthrough (VFIO)**.

The same Dedicated graphics card cannot be used by both Docker containers and virtual machines at the same time.

![](https://file-us.ugreennas.com/admin/article/2026-07-28/0179ab72ff8248faa699433f95d7deeb.webp)

## Set Dedicated Graphics Card to VM Passthrough (VFIO) Mode

After connecting the Dedicated graphics card, you need to switch the graphics card work mode to **VM passthrough (VFIO)** in Control Panel. Follow the steps below:

1. Open Control Panel, go to "**Hardware & Power**" > "**Dedicated graphics card**", and change the graphics card work mode to "**VM passthrough (VFIO)**".

![](https://file-us.ugreennas.com/admin/article/2026-07-28/f456c58306ba492e8feec62f210f20e5.webp)

2. Read the disclaimer displayed by the system, select "**I have read and fully understand the above disclaimer**", and click "**Agree and continue**".

3. Click "**Apply**" to save the settings.

4. When the system prompts that the NAS needs to be restarted, click "**Restart**".

![](https://file-us.ugreennas.com/admin/article/2026-07-28/864dbf211afc40b0b1e7309cc2079e59.webp)

After the NAS restarts, go to "**Control Panel**" > "**Hardware & Power**" > "**Dedicated graphics card**" again. If the graphics card work mode is displayed as "**VM passthrough (VFIO)**", the mode switch is successful.

## Notes

● Switching the graphics card work mode requires restarting the NAS.

● After Dedicated graphics card is switched to **VM passthrough (VFIO)**, Docker containers cannot use the graphics card.

● To allow Docker containers to use the graphics card, switch the work mode back to **NAS system**.

● If the Dedicated graphics card entry is not displayed in **Control Panel**, check the graphics card connection, power supply, and compatibility first.

● Page names and feature entries may vary slightly between different system versions. Refer to the actual interface display.
