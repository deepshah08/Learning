# Wake up Previously Logged-in Devices on UGOS Pro Using Windows/macOS

> **Article ID**: `584`  
> **Category**: `Application Guide > Control Panel > FAQ > Wake up Previously Logged-in Devices on UGOS Pro Using Windows/macOS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/584  

---

UGOS Pro supports remotely waking previously logged-in devices via the Windows/macOS client. Even if the device is powered off, as long as certain conditions are met, you can easily power it on within the local network (LAN). This allows you to wake the device without physical contact when on the same LAN, significantly improving convenience and operational efficiency.

This article will detail the prerequisites, operating steps, and important notes for using the Wake-on-LAN feature, along with some practical tips to help you make the most of it.

## Feature Overview

With the UGREEN NAS client, you can wake previously logged-in UGOS Pro devices.

This feature is based on Wake-on-LAN (WoL) technology within the same local network and works in conjunction with UGOS Pro’s hardware support. Even if the device is shut down, it can still be powered on through the client under suitable conditions.

## Prerequisites

Make sure all of the following conditions are met before using the Wake-on-LAN feature:

1. **Device and client must be on the same local network：**  
The wake-up operation must be performed within the same network environment. Ensure that the UGOS Pro device and your computer are connected to the same router.

2. **Device must be powered：**  
UGOS Pro must remain connected to a power source. Even when shut down, the hardware requires standby power for wake-up to work.

3. **Wake-on-LAN feature must be enabled：**  
On UGOS Pro, go to the Control Panel and make the following settings:

● **[Hardware & Power] > [Power] > [Auto boot after loss of power]**

● **[Hardware & Power] > [Power] > [Enable wake on LAN (WOL)]**

![](https://file-us.ugreennas.com/admin/article/2025-08-26/805acdfadb3943189e5ea739940981a3.webp)

4. **Client is up to date：**  
Download and install the latest version of the UGREEN NAS client to ensure compatibility with the newest features.

## Steps to Wake the Device

1. Launch the UGREEN NAS client on your Windows or macOS computer.

2. On the login screen, click the "More Connections" button to open the submenu.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/b3e5896284394c2d9ee4c13ac7f2a12f.webp)

3. In the submenu, locate the "LAN Devices" section and click the "Wake-on-LAN" button.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/ac96041bb28340d7864b1528e1b1a7f0.webp)

4. In the "Logged-in devices" section, browse the most recent recorded devices in chronological order (the system filters by MAC address and displays the latest 5 records).

5. Once you find the target device, click the "Wake Up" button to complete the operation.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/828a41faacd1443d9e95c3785375bf89.webp)

## Notes

1. Ensure that both the device and the client are on the same local network to avoid wake-up failures caused by network delays or isolation.

2. If the device fails to wake, verify that it is powered on and that both Auto Power On After Power Restored and Wake-on-LAN are enabled in the "Control Panel".

3. Use the latest version of the UGREEN NAS client to avoid compatibility issues.

4. Only the five most recent login records are saved. It's recommended to regularly manage your device login history to prevent confusion.

5. If the device still cannot be woken, try the following troubleshooting steps:

● Restart the router to refresh the network environment.

● Check if the device’s MAC address is correct.

● Re-enable the Wake-on-LAN feature in the Control Panel.
