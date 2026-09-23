# How to enable USB device passthrough for virtual machines on UGREEN NAS

> **Article ID**: `642`  
> **Category**: `Application Guide > Virtual Machine > FAQ > How to enable USB device passthrough for virtual machines on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/642  

---

This tutorial will guide users on how to enable the USB device passthrough feature for virtual machine configuration, allowing the virtual machine to directly access external USB storage devices, network devices, or expansion devices, thus avoiding data transfer bottlenecks.

## **What can enabling USB passthrough do?**

* With the USB passthrough feature, the virtual machine can directly access external USB devices connected to UGREEN NAS, eliminating the need for data transfer through the virtualization layer, reducing data transfer latency, and enhancing the overall user experience.
* Some devices, such as high-performance USB storage devices or USB network adapters, may not be perfectly compatible with virtual machines through conventional methods. With USB passthrough, these devices can be directly recognized and used by the virtual machine, expanding the range of supported devices.

## **Supported Device Types**

|  |  |  |
| --- | --- | --- |
| **Device Type** | **Support Status​** | **Typical Device Examples​** |
| Storage Devices | ✅ Supported | USB flash drive, external hard disk, hard disk enclosure, hard disk cabinet |
| Network Devices | ✅ Supported | USB wired network adapter |
| Expansion Devices | ✅ Supported | USB docking station |
| USB Wireless Network Adapters​ | ✅ Supported | USB wireless network adapter (Wi-Fi) |

## **Preparation**

* Please ensure that the UGOS Pro system is updated to the latest version (go to Control Panel > Update & Restore > System Update and click "Check for Updates").
* Make sure the virtual machine application is updated to the latest version (update the virtual machine application from ''App Center'').

## **Steps**

1. Enter the "Virtual Machine" application, select the target virtual machine, and click the "···" on the right side > "Settings."
2. In the settings menu, switch to the [Advanced Settings] option.
3. Enable the [USB Controller] option and set the USB device version (the device version must match the external device).

|  |  |  |
| --- | --- | --- |
| **Type** | **Max Theoretical Speed** | **Features/Use Case** |
| USB 2.0 | 480Mbps | Best compatibility, supports older devices |
| USB 3.0 | 5Gbps | Recommended for large-capacity devices |

4. Click the "Add" button to add a USB device. The system will automatically scan the list of USB devices connected to the current NAS.
5. Select the target device (e.g., [Western Digital 1TB External Hard Disk]), and click "Apply" to save the configuration.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250427/22b97838-86ae-48a2-b4ec-42c7d6cd66e3.png)

### **Notes**

* If set to USB 3.0 but the device only supports USB 2.0, it may result in recognition failure.
* Once a USB device is used by the virtual machine, it will be disconnected from the NAS host. Ensure there are no ongoing file transfer tasks between the USB device and the NAS host to avoid data loss.
* After enabling USB passthrough on the virtual machine, the USB device can only be used within the virtual machine and cannot be used in the NAS file system. If you need to switch the device between the NAS host and virtual machine, it is recommended to safely eject the device from the virtual machine first.
* Passthrough USB devices may have an impact on virtual machine performance, especially when handling large amounts of data transfer.
