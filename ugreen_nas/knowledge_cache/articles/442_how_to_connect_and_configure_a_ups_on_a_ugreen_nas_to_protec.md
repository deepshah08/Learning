# How to Connect and Configure a UPS on a UGREEN NAS to Protect Your Data Protection During Power Interruptions？

> **Article ID**: `442`  
> **Category**: `Application Guide > Control Panel > FAQ > How to Connect and Configure a UPS on a UGREEN NAS to Protect Your Data Protection During Power Interruptions？`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/442  

---

## **What is a UPS?**

A UPS (Uninterruptible Power Supply) is a device that provides temporary backup power when the main electrical supply is interrupted. It is commonly used to protect NAS devices and the data they contain from loss or hardware damage caused by unexpected power outages.

This guide will show you how to properly connect and configure a UPS on a UGREEN NAS, ensuring seamless power protection and allowing the device to shut down safely in the event of a power loss, minimizing the risk of data loss.

## **Connecting a UPS to a UGREEN NAS (Example: UGREEN US3000)**

1. Choose a UPS model that is compatible with your UGREEN NAS. For more details, see [the UPS Compatibility List](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDA0IiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxNDQsImFydGljbGVJbmZvSWQiOjEzNiwiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIiLCJwYXRoQ29kZSI6IiJ9).
2. Power off the NAS and disconnect its power adapter. Note: Make sure to stop all data transfers before shutting down the NAS to avoid data loss.
3. Plug the original NAS power adapter into a wall outlet, and connect the other end to the UPS’s DC IN port.
4. Use a USB data cable to connect the UPS’s USB port to the USB port on the back of the NAS.
5. Connect the UPS’s DC OUT cable to the NAS’s power input.
6. Once connected, the UPS’s LED indicator will flash white. Log in to the UGOS Pro system to check the UPS’s battery level and status information.

For more details, please refer to the official user manual of your UPS device.

## **Configure the UPS in UGOS Pro**

1. Log in to UGOS Pro, then go to [Control Panel] > [Hardware & Power] > [UPS]. The system will automatically detect any connected UPS device.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250624/84313ef3-8bb6-4765-bea3-dfb45d75370f.png)

2. Click "Connect", and the UPS page will display the device’s vendor and model information.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250624/9bb8d2ff-b869-4769-831c-f00ca7ded8ec.png)

3. Once connected, you can view the UPS’s current battery capacity and estimated remaining runtime.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250624/8cb3db40-122e-4d3e-8cd4-3d3b8e6733d4.png)

4. Set the NAS protection method when the UPS loses mains power. The following two options are available:

|  |  |
| --- | --- |
| **Protection Mode** | **Description** |
| Standby Mode | After a power loss, the NAS will stop all services to prevent data loss and shut down once the UPS battery is depleted. If [Power On Automatically When Power Is Restored] is enabled, it will restart automatically when mains power returns. |
| Auto Shutdown | The NAS will initiate a normal shutdown. If [Power On Automatically When Power Is Restored] is enabled, it will automatically restart when mains power is restored. |

5. Set the delay time before the NAS protection mode activates after a mains power outage:

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250624/d144d520-497f-417a-93d5-9b2ccb1502d1.png)

* **UPS battery below 15%:** Check this option to have the NAS enter Standby Mode or Auto Shutdown when the UPS battery level falls below 15%.
* **Custom time:** Check this option to have the UGREEN NAS enter Standby Mode or Auto Shutdown after the configured power supply duration is reached.
* **Execute now:** Check this option to have the UGREEN NAS enter Standby Mode or Auto Shutdown immediately.

**Note:** Regardless of the protection mode selected, the UGREEN NAS will automatically shut down once the UPS battery is fully depleted.

6. After completing the above settings, click "Apply" to save.
7. It is recommended to simulate a power outage after UPS installation and configuration to ensure that the UGREEN NAS properly switches to UPS power and safely shuts down when battery is low.

## **Frequently Asked Question**

#### **Q: Do I need to manually connect and configure the UPS in the UGREEN NAS system?**

**A:** Yes, you need to manually connect and configure the UPS in the system to ensure a valid connection with the NAS. If you do not require UPS support, you can also manually disconnect the UPS connection.
