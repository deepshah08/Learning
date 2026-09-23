# UGREEN NAS Hardware Passthrough

> **Article ID**: `911`  
> **Category**: `Application Guide > Virtual Machine > UGREEN NAS Hardware Passthrough`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/911  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS).

**Applicable Version**: UGOS Pro firmware 1.19.0.0093 or later

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

UGREEN NAS supports assigning certain physical devices directly to virtual machines through "**Hardware Passthrough**". This feature is suitable for scenarios where a virtual machine needs direct access to hardware capabilities.

For example, you can pass through an external dedicated GPU for graphics processing, compute acceleration, or other GPU-dependent tasks.

## Before Using Hardware Passthrough

Before using Hardware Passthrough, ensure that the following requirements are met:

● The NAS firmware has been upgraded to **V1.18.0.0073** or later.

● The NAS model supports passthrough for the corresponding hardware.

● The target hardware is properly connected to the NAS.

● The target hardware is not being used by another virtual machine or application.

● The virtual machine operating system supports the hardware and allows the corresponding driver to be installed.

USB port passthrough is currently not supported. Support will be gradually introduced in future updates. Please refer to the actual system version for availability.

## Requirements for GPU Passthrough

Some NAS models support external dedicated GPUs. A dedicated GPU can be connected to the NAS through a GPU enclosure or PCIe slot.

A GPU enclosure can connect to the NAS through:

● Thunderbolt

● OCuLink

● PCIe slot

To confirm whether your NAS supports an external dedicated GPU, check the hardware specifications of your device. Pay particular attention to whether the device has a Thunderbolt port, OCuLink port, or PCIe slot.

You can visit the [UGREEN NAS product center](https://ai.ugreen.com/collections/all?utm_source=chatgpt.com) to check the hardware specifications of your device, or contact UGREEN NAS technical support for confirmation.

## Graphics Card and Graphics Card Expansion Dock Compatibility

For GPU enclosure compatibility, refer to the"[UGREEN Cloud Hardware Compatibility Instructions](https://ai.ugreen.com/pages/compatibility?utm_source=chatgpt.com)". For NVIDIA GPU compatibility, refer to the corresponding"[NVIDIA official driver page](https://www.nvidia.com/en-us/drivers/details/252481/?utm_source=chatgpt.com)"on the NVIDIA official website.

The following GPU models are recommended:

● NVIDIA: **RTX 30 Series or later**

● AMD: **6000 Series or later**

Even if a dedicated GPU is connected to the NAS, whether it can be use1d properly by a virtual machine still depends on the device hardware, system version, driver support, and virtual machine configuration.

### Test Environment

The following test results are based on the specified system environments and are provided for reference when selecting and configuring hardware.

|  |  |
| --- | --- |
| **Test System** | **Version** |
| Windows 11 | Windows 11 24H2 Chinese Simplified x64, OS Build: 26100.9168 |
| Ubuntu | Ubuntu 26.04 LTS，ubuntu-2604-desktop-amd64 |

**Note:** When running Windows 11 on a device with 8 GB of memory, horizontal lines may appear in the HDMI output, and the overall user experience may be affected.

### External GPU Compatibility Test Examples

|  |  |  |
| --- | --- | --- |
| **GPU Model** | **Windows 11 Thunderbolt Passthrough** | **Ubuntu 26 Thunderbolt Passthrough** |
| AMD Radeon 5500XT | PASS | PASS |
| AMD Radeon 6900XT | PASS | PASS |
| AMD Radeon 7900XT | FAIL（display artifacts） | PASS |
| AMD Radeon 9060XT | FAIL（display artifacts） | PASS |
| NVIDIA GeForce 1660 | PASS | PASS |
| NVIDIA GeForce 2060S | PASS | PASS |
| NVIDIA GeForce 2080Ti | PASS | PASS |
| NVIDIA GeForce 3060Ti | PASS | PASS |
| NVIDIA GeForce 3060 | PASS | PASS |
| NVIDIA GeForce 3070 | PASS | PASS |
| NVIDIA GeForce 3080 | PASS | PASS |
| NVIDIA GeForce 3090 | PASS | PASS |
| NVIDIA GeForce 4060Ti | PASS | PASS |
| NVIDIA GeForce 4070Ti | PASS | PASS |
| NVIDIA GeForce 4080S | PASS | PASS |
| NVIDIA GeForce 5070Ti | PASS | PASS |
| NVIDIA GeForce 5080 | PASS | PASS |
| NVIDIA GeForce 5090 | PASS | PASS |

**Notes:**

● **PASS** indicates that the GPU passed testing in the specified test environment.

● **FAIL** indicates that the GPU encountered an issue in the specified test environment.

● The above test results are for reference only. Actual compatibility of an external GPU in a virtual machine may vary depending on the **GPU model**, **virtual machine** **operating system** **version**, **virtual machine configuration**, **driver version**, and other factors.

● A GPU marked as PASS only indicates that it worked properly in the corresponding test environment. **It does not mean that the GPU is compatible with all Windows 11 or Ubuntu versions and configurations**.

● GPUs that are not listed or have not yet been tested **are not necessarily unsupported**. We recommend testing based on your actual environment and referring to the final test results.

## Set the Dedicated GPU to VM Passthrough Mode

After connecting the dedicated GPU, you need to switch the GPU work mode to **VM passthrough (VFIO)** in Control Panel. Follow the steps below:

1. Open the Control Panel App, go to "**Hardware & Power**">"**Dedicated graphics card**", and change the GPU work mode to "**VM passthrough (VFIO)**".

![](https://file-us.ugreennas.com/admin/article/2026-09-11/bad8910028c24e7abcf4788d3a31bc81.webp)

2. Read the disclaimer displayed by the system, select "**I have read and fully understand the above disclaimer**", and click "**Agree and continue**".

3. Click "**Apply**" to save the settings.

4. When the system prompts you to restart the NAS, click "**Restart**".

![](https://file-us.ugreennas.com/admin/article/2026-09-11/5afdc9e6da0e43b78f8f64dc67e129e5.webp)

After the NAS restarts, go to "**Control Panel**">"**Hardware & Power**">"**Dedicated graphics card**" again. If the GPU work mode is displayed as "**VM passthrough (VFIO)**", the mode switch is successful.

## Add a Dedicated Graphics Card to a Virtual Machine

After switching the graphics card to VM Passthrough Mode, you can assign the graphics card to a specified virtual machine in the virtual machine settings. Follow the steps below:

1. Open the Virtual Machine app and find the virtual machine that needs to use the Dedicated graphics card in the virtual machine list.

2. Click "**···**" on the right＞"**Edit**".

3. On the edit page, find the **Hardware Direct Access** section, then click "**Add hardware**">"**Add PCIe devices**".

![](https://file-us.ugreennas.com/admin/article/2026-09-11/803a1c727aea49ae8784fda9c53d9f0e.webp)

4. In the **Select PCIe devices** window, select the GPU you want to use and click "**Confirm**".

![](https://file-us.ugreennas.com/admin/article/2026-09-11/098e8b1d2be544b8925f45c0fa50933c.webp)

5. Return to the virtual machine edit page and click "**Confirm**" to save the configuration.

![](https://file-us.ugreennas.com/admin/article/2026-09-11/950e2cecb79d4548a173e18dd307eab4.webp)

After saving the configuration, start the virtual machine. Enter the virtual machine operating system and install the corresponding GPU driver to use the GPU.

**Note:** Hardware Passthrough will gradually support additional types of hardware devices in future updates. If the device list in the Select PCIe device window is empty, no currently supported hardware is connected to the NAS. This is normal. Please wait for future updates.

## GPU Driver Instructions for Virtual Machine Systems

Hardware Passthrough allows a virtual machine to directly access a dedicated GPU. Therefore, you do not need to install the NVIDIA driver from the NAS App Center. Instead, install the corresponding GPU driver within the virtual machine operating system.

Common Cases:

● Windows virtual machine: Install the official driver for the corresponding GPU model.

● Ubuntu virtual machine with an AMD GPU: You can use the driver included with the operating system.

● Ubuntu virtual machine with an NVIDIA GPU: Install the NVIDIA driver within the virtual machine operating system.

For specific driver installation instructions, refer to the documentation provided by the virtual machine operating system and GPU manufacturer.

## Edit Hardware Passthrough Configuration for an Existing Virtual Machine

To modify the Hardware Passthrough configuration of an existing virtual machine, shut down the virtual machine first. Follow the steps below:

1. Open the Virtual Machine App, find the target virtual machine in the virtual machine list, and click "**Shutdown**".

2. After the virtual machine is shut down, click "**···**" on the right > "**Edit**" to enter the virtual machine editing page.

![](https://file-us.ugreennas.com/admin/article/2026-09-11/872a3a83be834d409f644192009195dc.webp)

3. Modify the Hardware Passthrough-related settings and save the changes.

4. Restart the virtual machine.

## FAQs

### Q1: Why can't the virtual machine start?

The passthrough device may already be in use by another virtual machine or application. Close the virtual machine or application currently using the device, then try starting the virtual machine again.

### Q2: Why can't the passthrough device be detected in the virtual machine?

This may be caused by one of the following:

● The dedicated GPU work mode has not been switched to "**VM passthrough (VFIO)**".

● The required driver is not installed in the virtual machine operating system.

● The device is already in use by another virtual machine.

● The passthrough configuration has not been saved.

### Q3: When using Hardware Passthrough with a dedicated GPU, do I need to install the NVIDIA driver from the NAS App Center?

No. Hardware Passthrough allows the virtual machine to directly access the dedicated GPU. You only need to install the corresponding GPU driver in the virtual machine operating system.

### Q4: After switching the GPU to VM passthrough mode, can Docker containers still use the GPU?

No. The GPU cannot be used by a virtual machine and Docker containers at the same time.

If you need Docker containers to use the GPU, switch the GPU work mode to "**NAS system**". After switching, save the settings and restart the NAS as prompted.
