# Virtual Machine User Guide

> **Article ID**: `909`  
> **Category**: `Application Guide > Virtual Machine > Virtual Machine User Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/909  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS).

**Applicable Version**: NAS Firmware 1.18.0.0073 or later.

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

GREEN NAS supports creating and managing virtual machines through the Virtual Machine app. Users can run operating systems such as Linux and Windows on their NAS for testing environments, lightweight office tasks, or other virtualization scenarios.

The Virtual Machine app provides features including virtual machine management, image management, volume management, network management, and log viewing.

## Virtual Machine Overview

After opening the "**Virtual Machine**" app you will be directed to the virtual machine list page by default. The top of the page displays an overview of current virtual machine resources, including:

● **Number of running virtual machines**

● **Total CPU usage**

● **Used/Total RAM**

The virtual machine list displays all created virtual machines. Each virtual machine shows its name, system icon, and running status.

On the right side of each virtual machine, click "**Start**" to power on the virtual machine. Click "**···**" to view more actions.

![](https://file-us.ugreennas.com/admin/article/2026-07-27/e7f257d0c3fb4807b3c3dda57c12e022.webp)

## Create a Virtual Machine

1. Open the Virtual Machine app, go to the virtual machine page, and click "**Create manually**".

2. Follow the setup wizard to configure the virtual machine name, operating system type, image, CPU, memory, storage, network, and other parameters.

3. Confirm that all settings are correct, then complete the creation process.

After creation, the virtual machine will be displayed in the virtual machine list.

## Import a Virtual Machine

If you already have a virtual machine file, you can import it into the Virtual Machine app. Follow the steps below:

1. Open the Virtual Machine app, go to the virtual machine page, and click "**Import virtual machine**".

![](https://file-us.ugreennas.com/admin/article/2026-07-27/43fe31b1db044817b002693e1353d294.webp)

2. Select the import source and storage space based on the location of the image file, then click "**Next**".

3. Configure the virtual machine settings, such as CPU, memory, and network, as needed. Click "**Complete**".

4. After the import is complete, view the virtual machine in the virtual machine list.

## Image Management

The Image page is used to manage ISO images required for installing operating systems on virtual machines. After entering the "**Image**" page, you can view the image name, size, format, type, and available actions.

The following methods are supported for adding images:

● **Add image from NAS**: Select an image file from the NAS file system.

● **Add image from local**: Upload an image file from a local computer.

![](https://file-us.ugreennas.com/admin/article/2026-07-27/3433b3e874764169907c56f6fc478fd4.webp)

### Add an Image

1. Open the "**Virtual Machine**" app and click "**Image**" in the left sidebar.

2. Select "**Add image from NAS**" or "**Add image from local**" based on the image file location.

3. Select the ISO image file to add and follow the on-screen instructions to complete the process.

After the image is added, it will be displayed in the image list, where you can view the image name, size, format, and type. When creating a virtual machine, you can select this image as the system installation image.

### Manage Images

In the image list, you can manage existing images. Available actions include:

● **Edit**: Modify image information.

● **Delete**: Delete images that are no longer needed.

Before deleting an image, make sure it is not being used by any virtual machine. Otherwise, the installation or startup of the virtual machine may be affected.

## Volume Management

The Volume page is used to manage the volumes used by virtual machines. After entering the **Volume** page, you can view the status, file system, number of virtual machines, and capacity usage of different volumes.

The page displays:

● Volume name

● Volume status

● File system type

● Number of virtual machines

● Used/Total capacity

● Capacity usage of different virtual machines

If the volume status shows "**Warning**", it is recommended to check the available capacity or the status of related virtual machine files in a timely manner.

![](https://file-us.ugreennas.com/admin/article/2026-07-27/faa5fd86209543928f48ba35cb79114f.webp)

### Add Volume

1. Open the Virtual Machine app and click "**Volume**" in the left sidebar.

2. Click "**Add volume**", select a volume, and click "**Confirm**".

3. After completion, view the newly added volume in the volume list.

When creating a virtual machine, you can store the virtual machine disk file in the corresponding volume.

## Network Management

The Network page is used to manage virtual machine networks. After entering the **Network** page, you can view virtual subnets, network modes, host network adapters, and associated virtual machines.

Common network modes include:

● **Bridge Mode-LinuxBridge**

● **Bridge Mode-MacVTap**

● **Host-only Mode**

● **NAT Mode**

![](https://file-us.ugreennas.com/admin/article/2026-07-27/3e91bc4a232044eaaa80091e6a511e16.webp)

## Add a Network

1. Open the Virtual Machine app and click "**Network**" in the left sidebar.

2. Click "**Add network**" and configure the network name and mode.

3. Save the configuration.

When creating or editing a virtual machine, you can select a created virtual network.

## Network Mode Description

### Bridge Mode

Bridge Mode connects the virtual machine to the same network as the host machine. It is suitable for scenarios where other devices on the local network need to access the virtual machine.

### NAT Mode

NAT Mode forwards the virtual machine's network traffic to the host machine's network interface and enables communication with external networks through the host's network connection. Communication between the virtual machine and external networks is forwarded and managed by the host machine.

### Host-only Mode

Host-only Mode directly connects the virtual machine's network interface to the host machine. The virtual machine and the host machine share the same network interface. The virtual machine can communicate directly with the host machine but cannot communicate directly with external networks.

## View Logs

The Log page is used to view operation records and error information of the Virtual Machine app. The log list includes the following information:

● Level

● Operator

● Date

● Log content

![](https://file-us.ugreennas.com/admin/article/2026-07-27/c4d3e8b19c294cfcb2da8e40f3617c57.webp)

Common logs include:

● Create virtual machine

● Delete virtual machine

● Start virtual machine

● Shut down virtual machine

● Modify virtual machine information

● Virtual machine startup failure reasons

If a virtual machine fails to start, you can go to the **Log** page first to check the error information.

## Search, Export, and Clear Logs

On the Log page, you can use the search box to find specific logs. The top-right corner of the page provides the following options:

● **Export**: Export logs for saving or providing to technical support for troubleshooting.

● **Clear**: Clear historical log records.

If you need to contact technical support, it is recommended to export the relevant logs first.

## Notes

● Before creating a virtual machine, make sure that the NAS has sufficient CPU, memory, and volume capacity.

● Before installing an operating system, add the ISO image on the Image page. When creating a virtual machine, select the corresponding image as the installation media.

● If the virtual machine needs to be accessed by other devices on the local network, Bridge Mode is recommended. If only regular network access is required, select NAT Mode.

● If a virtual machine fails to start, check the error information on the Log page first. Common causes include missing image files, unavailable volume files, or USB devices being occupied by other virtual machines.

## Frequently Asked Questions

### Why can't I create a virtual machine?

The inability to create a virtual machine may be related to the image, volume capacity, network configuration, or permissions.

### Why can't the virtual machine start?

You can go to the Log page to view the failure records. The logs record the reasons why the virtual machine failed to start.

### Where can I add images?

You can select "**Add image from NAS**" or "**Add image from local**" on the Image page.

### Are image formats other than ISO supported?

Yes. When adding images in the Virtual Machine app, the following formats are supported in addition to ISO:

● **iso.gz**

● **img**

● **vmdk**

● **qcow2**

● **vdi**

When adding an image, select the import option based on the actual image file format. After the import is complete, you can view and manage the image on the **Image** page.
