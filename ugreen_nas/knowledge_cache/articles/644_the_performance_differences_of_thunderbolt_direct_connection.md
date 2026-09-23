# The Performance Differences of Thunderbolt Direct Connection Function in Sleep Mode on Windows and Mac Computers and Their Solutions

> **Article ID**: `644`  
> **Category**: `Application Guide > Control Panel > FAQ > The Performance Differences of Thunderbolt Direct Connection Function in Sleep Mode on Windows and Mac Computers and Their Solutions`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/644  

---

The Thunderbolt direct connection function provides Windows and Mac computer users with a fast and convenient data transfer experience. However, when the computer is in sleep mode, the performance of Thunderbolt direct connection can vary depending on the system, device model, and power mode. This article will explain these differences and offer corresponding adjustment suggestions to help reduce connection issues and enhance the user experience.

## **The Performance Differences of Thunderbolt Direct Connection Function in Sleep Mode on Windows and macOS Operating Systems**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Operating System | Device Type | Test Device Model | Power Mode | Thunderbolt Direct Connection Performance |
| Windows | Laptop | Lenovo Xiaoxin PRO 14IAH5R | Sleep Mode | Keeps connection active (NAS device functions properly) |
| Desktop | - | Sleep Mode | Disconnects directly but does not reconnect |
| macOS | Laptop | MacBook Air Apple M2 | Sleep Mode | Disconnects directly but does not reconnect |
| Desktop | MacBook Air Apple M4 | Sleep Mode | Repeatedly disconnects and reconnects |

## **Analysis of Thunderbolt Direct Connection Performance Differences in Sleep Mode**

### **Windows System Characteristics**

1. **Low Power Connection:** On some Windows devices, the Thunderbolt port may maintain a low-power connection in sleep mode (e.g., Lenovo Xiaoxin PRO), allowing the device to remain connected while in sleep mode.
2. **Desktop Disconnect Issue:** Some Windows desktop PCs experience a complete disconnect of the Thunderbolt direct connection in sleep mode, and it fails to reconnect. This is typically related to the power supply strategy for the Thunderbolt port. Some motherboards disable peripheral power by default, and users may need to disable the "ErP Ready" option in the BIOS to ensure continuous power supply to connected devices.

### **macOS System Characteristics**

1. **Deep Sleep Mechanism:** macOS systems, particularly those with M-series chips, employ a deep sleep mechanism that actively cuts off power to non-essential peripherals to conserve energy. This causes the Thunderbolt direct connection to be interrupted in sleep mode.
2. **Multiple Thunderbolt Bridge Conflicts:** When there are multiple Thunderbolt bridges in the system, it may trigger an abnormal wake-up loop in the system’s power management strategy. This issue could be related to macOS's ["Power Nap"](https://support.apple.com/zh-cn/guide/mac-help/mh40773/10.14/mac/10.14) feature or similar settings.

## **Optimization Suggestions and Solutions**

### **System-Level Adjustments**

#### **For Windows Users**

1. **Driver and Settings:**

Install the latest version of [the Thunderbolt Control Center](https://apps.microsoft.com/detail/9n6f0jv38ph1?hl=zh-CN&gl=CN). In the Thunderbolt Control Center, check the options for "Always Connect" and "Allow this device to wake the computer" (similar options may need to be configured in Device Manager).

2. **BIOS Adjustments:**

For desktop users, enter the BIOS settings and enable the options "Always On USB" and "Thunderbolt Wake Support."

#### Fo**r macOS Users**

1. **Power Strategy:**

[Disable Power Nap](https://support.apple.com/zh-cn/guide/mac-help/mh40774/10.14/mac/10.14) and Network Wake through the Terminal (for detailed instructions, refer to [the official documentation](https://support.apple.com/zh-cn/guide/mac-help/mh40774/10.14/mac/10.14)).

2. **Service Configuration:**

Retain only one Thunderbolt bridge to avoid multiple interface IP conflicts. The path to do this is: Mac > System Settings > Network > Remove redundant Thunderbolt bridges.

### **Cable Standards**

Prioritize using Thunderbolt 4 certified cables (which support up to 2 meters in length with stable bandwidth) to avoid signal attenuation caused by non-standard cables.

## **Advanced Troubleshooting**

|  |  |  |  |
| --- | --- | --- | --- |
| **Issue** | **Possible Cause** | **Solution** | **Operation Guide Reference** |
| Windows Repeated Disconnects | PCIe Power Management Conflict | Disable the "Allow the computer to turn off this device to save power" option in Device Manager | Device Manager > Thunderbolt Interface Properties > Power Management |
| Mac Thunderbolt Device Not Reconnecting After Wake-up | System Deep Sleep Cuts Off Power | Disable "Low Power Mode" and use "Turn off display only" instead of sleep | System Settings > Power Management |
| NAS Transfer Speed Degradation | Thunderbolt Driver Bandwidth Allocation Issue | Update chipset drivers for Windows users, reset SMC for macOS | Windows: Download and install the latest chipset drivers;  macOS: Turn off the computer and hold the power button for 10 seconds to reset the SMC |

Note: The operation paths may vary depending on the operating system. For detailed instructions, please refer to the manufacturer's documentation or consult official customer support.

## **Compatibility Upgrade Recommendations**

1. **Device Selection:** Prioritize using Thunderbolt 4 interface devices (such as the UGREEN NAS 8800 series). Its dynamic bandwidth allocation mechanism can reduce data blocking during sleep/wake cycles.
2. **System Version:** Ensure macOS is upgraded to version 15.2 or higher, and Windows is updated to version 22H2 or above, to address known Thunderbolt protocol stack vulnerabilities.

By implementing these adjustments, the stability of Thunderbolt direct connection in sleep mode can be significantly improved. If the issue persists, it is recommended to contact the device manufacturer for a customized power strategy file.

## **Frequently Asked Questions**

**Issue 1: After connecting to Mac, the device fails to recognize Thunderbolt direct connection or the connection is unstable.**

**Solution:** Normally, the Thunderbolt direct connection between Mac and NAS should be automatically recognized. If it is not automatically recognized, you can manually add the service following the steps below. Note: For macOS 11 and later, the corresponding service must be added first to ensure proper use of the Thunderbolt direct connection functionality.

**Operation Guide:**

1. Go to Mac System Settings, then navigate to [Network] > [Other Services] > [Add Service].

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250425/df8485d4-618c-496e-98a8-b64819258541.png)

2. Manually add the "Thunderbolt Bridge" service and complete the creation.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250425/30a387db-873b-4590-8056-dcf03caceaea.png)

**Issue 2: When users attempt to add multiple Thunderbolt Bridges on Mac, they may encounter issues with proper functionality.**

**Possible Cause:** Thunderbolt Bridges may differ due to variations in Thunderbolt interface versions (e.g., Thunderbolt 1 or Thunderbolt 2). If multiple Thunderbolt Bridges exist in the system, it could lead to network conflicts or unstable connections.

**Solution:** Delete the redundant Thunderbolt Bridges, leaving only one, and then unplug and replug the Thunderbolt device.

## **Related Link**

[Thunderbolt Device Not Recognized on Windows – How to Fix It](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTkyNywidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiZW4tVVMiLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo2MDgsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)
