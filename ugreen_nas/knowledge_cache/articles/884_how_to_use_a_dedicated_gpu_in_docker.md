# How to Use a Dedicated GPU in Docker？

> **Article ID**: `884`  
> **Category**: `Application Guide > Docker > How to Use a Dedicated GPU in Docker？`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/884  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: NAS Firmware 1.18.0.0060 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

The Docker app supports the use of an external dedicated GPU. This feature is available on UGREEN NAS devices that support external GPUs and can be used with certain containers for AI, graphics processing, video transcoding, or other GPU-accelerated workloads.

### GPU Requirements

Some NAS models support external dedicated GPUs, which can be connected through a GPU enclosure or a PCIe slot on the motherboard.

A GPU enclosure can be connected to the NAS through the following interfaces:

● Thunderbolt

● OCuLink

To check whether your NAS supports an external dedicated GPU, refer to the device’s hardware specifications. In particular, check whether the device has a Thunderbolt port, OCuLink port, or PCIe slot.

You can visit the [UGREEN NAS Product Center](https://nas.ugreen.com/pages/compare) to view the hardware specifications of your device, or contact UGREEN NAS Technical Support for confirmation.

## GPU and GPU Enclosure Compatibility

For GPU enclosure compatibility, refer to the [UGREEN NAS Hardware Compatibility List](https://nas.ugreen.com/pages/compatibility) . For NVIDIA GPU compatibility, refer to the corresponding [driver page](https://www.nvidia.com/en-us/drivers/) .

For NVIDIA GPUs, **RTX 30 Series or later** is recommended.

For AMD GPUs, **6000 Series or later** is recommended.

GPUs with built-in **M.2 expansion slots**, **USB ports**, or other additional interfaces are currently not supported.

Even if a dedicated GPU is connected to the NAS, whether a virtual machine can use it properly also depends on the device hardware, system version, driver support, and virtual machine configuration.

## How to Use an NVIDIA GPU When Creating a Container

1. Open **Docker**, then create a new container or edit an existing one.

2. On the container configuration page, enable "**GPU performance**" and select the NVIDIA GPU.

3. Save the configuration and start the container.

![](https://file-us.ugreennas.com/admin/article/2026-08-13/727c4d3cfb1346c59178d857e3f4166e.webp)

Once enabled, the container can access the NVIDIA discrete GPU connected to the NAS.

Whether the GPU can be used successfully also depends on whether the container image supports NVIDIA GPUs. Images used for workloads such as AI inference, CUDA, or video transcoding may require additional runtime components or configuration.

## How to Configure a Container When Creating It with Compose

When creating containers from a Compose file provided in Project, add the GPU configuration under each service that needs to use the GPU. For example:

```
services:
  app:
    image: your-image:latest      # Docker image name and version
    environment:
      # Specify the NVIDIA GPU devices visible inside the container
      # all allows the container to use all available GPUs
      # You can also specify a GPU index, for example: NVIDIA_VISIBLE_DEVICES=0
      - NVIDIA_VISIBLE_DEVICES=all
    deploy:
      resources:
        reservations:
          devices:
            # Reserve GPU device resources for the container
            - driver: nvidia
              # Specify the GPU devices to use
              # all means using all GPUs
              # Examples:
              # device_ids: ["0"]  uses only GPU 0
              # device_ids: ["0","1"] uses GPUs 0 and 1
              device_ids: all 
              capabilities: [gpu]  # gpu indicates that NVIDIA GPU acceleration is required
```

Replace app and your-image:latest with the actual service name and image name used in the project.

If the original Compose file already contains environment or deploy, merge the configuration above into the existing section.

Do not create multiple fields with the same name under the same service.

After editing the file, use a YAML validation tool to check the indentation. YAML is indentation-sensitive, and incorrect indentation may prevent the Compose file from being deployed successfully.

## What Should I Do If There Is No HDMI Output After Connecting a GPU via PCIe

This procedure applies **when an NVIDIA discrete GPU is installed in the NAS through a PCIe slot and the HDMI port no longer outputs a display signal**. If the GPU is connected through a Thunderbolt or OCuLink GPU expansion dock, the integrated graphics setting in the BIOS usually does not need to be changed.

The HDMI port on the NAS outputs video through the CPU’s integrated graphics. After an NVIDIA discrete GPU is installed through PCIe, the system may prioritize the discrete GPU, preventing the integrated graphics from outputting normally and resulting in no HDMI display. In this case, enable integrated graphics in the BIOS.

**Note:** The BIOS has an automatic timeout mechanism. After entering the BIOS, complete and save the changes within **180 seconds**. Otherwise, the device will restart automatically.

**Steps**：

1. Connect the NAS to a monitor using an HDMI cable, connect a keyboard, and restart the NAS.

2. During startup, press **Ctrl + F2** to enter the BIOS.

3. In the BIOS, open **Chipset**, then go to **System Agent (SA) Configuration**. If this option is hidden, press **Ctrl + F1** to display additional settings.

![](https://file-us.ugreennas.com/admin/article/2026-08-13/a79bb4fd3580441a90e455eaed973eb3.webp)

4. Open **Graphics Configuration**.

![](https://file-us.ugreennas.com/admin/article/2026-08-13/9bc8797e0a8045c7a26ae449c954480d.webp)

5. Locate **Internal Graphics**, set it to **Enabled**, then press **F10** to save and exit.

![](https://file-us.ugreennas.com/admin/article/2026-08-13/68c38486ab184dcd8e750df748cd3c20.webp)

The device will start using the updated BIOS configuration.

## About Internal Graphics

**Internal Graphics** controls whether the CPU’s integrated graphics are enabled. The HDMI port on the NAS relies on the integrated graphics to output video.

When **Internal Graphics** is set to **Enabled**, the HDMI port can continue to output video through the integrated graphics, while the NVIDIA discrete GPU remains available for Docker containers.

## Notes

● Before changing BIOS settings, make sure a monitor and keyboard are connected. BIOS interfaces may vary by device. Refer to the actual interface.

● After installing NVIDIA Driver and NVIDIA Docker Toolkit, restart the NAS if GPU performance is still not available in Docker, then check again.

● Not all Docker images support GPU acceleration. If a container cannot detect the GPU after startup, first confirm that the image supports NVIDIA GPUs, CUDA, or the required hardware acceleration technology.

● In a Compose configuration, NVIDIA\_VISIBLE\_DEVICES=all allows the container to access all visible NVIDIA GPUs. To use only a specific GPU, adjust the configuration according to the project documentation.
