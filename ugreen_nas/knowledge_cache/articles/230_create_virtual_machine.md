# Create Virtual Machine

> **Article ID**: `230`  
> **Category**: `Application Guide > Virtual Machine > Create Virtual Machine`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/230  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS).

**Applicable Version**: NAS Firmware 1.18.0.0073 or later.

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

The Virtual Machine app supports creating Windows, Linux, and other types of virtual machines on NAS. Before creating a virtual machine, prepare the system image and make sure that the NAS has sufficient CPU, memory, and volume capacity.

This article uses creating a virtual machine from an ISO image as an example.

## Create a Virtual Machine

1. Open the Virtual Machine app and click "**Virtual Machine**" in the left sidebar.

2. Click "**Create manually**" to open the virtual machine creation wizard.

![](https://file-us.ugreennas.com/admin/article/2026-07-27/4dc3a712a9924514ba5a39c591447d19.webp)

3. On the Select image page, select the image file used to install the operating system.

4. After selecting the image, choose the volume for storing the virtual machine and click "**Next**" to enter the configuration page.

![](https://file-us.ugreennas.com/admin/article/2026-07-27/bf4639a3cb1441e7b9e8cde9b8364e0f.webp)

## Configure the Virtual Machine

On the configuration page, you can configure the virtual machine name, operating system type, CPU, memory, ISO image, disk, and network.

### Basic Information

![](https://file-us.ugreennas.com/admin/article/2026-07-27/490be9acbcf84b5483e9dc10ed8c8f64.webp)

**VM name**: Used to identify the current virtual machine, such as`ubuntu`.

**System type**: Select the operating system type to be installed on the virtual machine. Select the appropriate type based on the actual operating system. For example, select **Linux** when installing systems such as Ubuntu or Debian.

**CPU (Core)**: Set the number of CPU cores allocated to the virtual machine. Allocating more CPU cores can improve virtual machine performance but will consume more NAS system resources.

**Memory (GB)**: Set the memory capacity allocated to the virtual machine. Insufficient memory may cause the virtual machine to run slowly or fail to install.

**Auto start**: When enabled, the virtual machine will automatically start according to system policies. Enabling this option is recommended.

**Configure ISO image**: In the **ISO image** section, you can view the currently selected installation image. To add more images, click "**Add**". The virtual machine will boot from the selected ISO image and start the operating system installation process.

**Configure Disk**: In the **Disk** section, you can configure the virtual machine disk. A virtual disk is created by default. You can adjust the disk capacity as needed or click "**Add**" to create additional disks.

**Configure Network**: In the **Network** section, you can select the virtual network used by the virtual machine. One network device is added by default. To use multiple network adapters, click "**Add**" to add more network devices.

### Advanced Options

In the **Advanced** section, you can configure the USB controller, virtual graphics card, boot type, and other options. The available settings may vary depending on the options displayed on the page.

![](https://file-us.ugreennas.com/admin/article/2026-07-27/db5084bcf42b42d5b6df63a18c1a6736.webp)

If you do not need to use USB devices in the virtual machine, you can keep the default settings. If you need to use USB devices, select an available controller type based on your requirements.

### Hardware Passthrough

When creating a virtual machine, you can use "**Hardware Passthrough**" to assign certain physical devices to the virtual machine. Hardware passthrough is suitable for scenarios where the virtual machine needs to directly access hardware capabilities.

Such as using an external dedicated GPU for graphics processing, computing acceleration, or other GPU-dependent tasks.

![](https://file-us.ugreennas.com/admin/article/2026-07-27/053cc7113e3e4edd9876be984681d6fb.webp)

**Before using hardware passthrough, make sure that:**

● The NAS supports the corresponding hardware passthrough capability.

● The target hardware is properly connected to the NAS.

● The target hardware is not being used by another virtual machine or app.

● The virtual machine operating system supports the hardware and can install the corresponding drivers.

Some NAS models support external dedicated GPUs. A dedicated GPU can be connected to the NAS through a GPU expansion dock or PCIe slot. A GPU expansion dock can be connected to the NAS through a Thunderbolt interface, OCuLink, or PCIe slot.

To confirm whether your device supports external GPUs, check the device hardware specifications or contact UGREEN NAS technical support.

**USB Device Passthrough**:

USB device passthrough support will be gradually added in future updates. If the USB device passthrough option is not available in the current version, refer to the actual system version.

**Notes**:

● GPU passthrough capability depends on the NAS model, GPU model, connection method, system version, and virtual machine operating system drivers.

● After a hardware device is passed through to a virtual machine, it may no longer be available for other virtual machines or NAS apps at the same time.

● If the virtual machine fails to start, check whether the target hardware is being used by another virtual machine or app.

## Complete Creation

After confirming that all configurations are correct, click "**Complete**" in the bottom-right corner.

After creation, the virtual machine will appear in the virtual machine list. Click "**Start**" to power on the virtual machine.

When starting the virtual machine for the first time, the system installation interface will be displayed. Follow the installation wizard of the corresponding operating system to complete the system installation.
