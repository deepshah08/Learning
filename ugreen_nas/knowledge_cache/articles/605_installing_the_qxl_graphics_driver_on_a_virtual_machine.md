# Installing the QXL Graphics Driver on a Virtual Machine

> **Article ID**: `605`  
> **Category**: `Application Guide > Virtual Machine > FAQ > Installing the QXL Graphics Driver on a Virtual Machine`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/605  

---

QXL is a virtualization graphics technology specifically designed to enhance the graphical performance of Windows virtual machines. It significantly improves mouse smoothness and display responsiveness. This tutorial provides guidance on installing the QXL graphics driver for virtual machines running on the UGOS Pro system.

● Supported versions: Firmware version 1.2.0.2121 or above, and Virtual Machine application version 1.2.0.0313 or above.

● Application features vary across different UGREEN NAS product series. The Virtual Machine application is not supported on devices from the [DH Plus Series]. Please confirm your device model before use to ensure a complete and seamless experience.

## Prerequisites

Before beginning the installation, please ensure the following conditions are met:

1. The virtual machine is running a Windows operating system (Linux does not support the QXL driver).

2. Confirm your Windows version: Installation Method 1 is applicable to modern systems such as Windows 10/11 and Windows Server 2016/2022, while Installation Method 2 is intended for older systems such as Windows 7.

3. Ensure that the [Virtual Machine] application supports QXL graphics configuration (it is recommended to upgrade to the latest firmware and Virtual Machine application version).

## Configure the Virtual Machine Graphics Type

● If you are creating a new virtual machine, go to the [Advanced] page during the setup process, then locate the [Graphics card] setting and select qxl as the graphics type.

● If you have already installed a virtual machine but haven’t configured the QXL graphics card yet, follow the steps below:

1. Log in to your UGREEN NAS and open the [Virtual Machine] application.

2. Shut down the target Windows virtual machine (if it is currently running).

3. Click the [···] > [Settings] button next to the target virtual machine.

4. In the settings interface, go to the [Advanced] tab and locate the [Graphics Card] setting.

5. Change the graphics card type to qxl.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/b34524527dc74ef0a9af5a12a4a57472.webp)

6. Click [Apply] to save the configuration, then start the virtual machine.

7. After the virtual machine is started, you can access the Windows system interface from either of the two locations shown in the image.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/6bc471313d2f4f4cb5c4c1d3d239c8d0.webp)

![](https://file-us.ugreennas.com/admin/article/2025-08-26/8a502c205c2641da9f80b9cafd1c8245.webp)

## Install the QXL Graphics Driver

Depending on your Windows version, choose one of the two installation methods below.

### Method 1: Direct Installation of the QXL Driver (Recommended)

**Applicable systems:** Windows 10/11, Windows Server 2016/2022, and other modern systems.  
**Steps:**

1. Download the driver installation package: [QXL Driver Installation Package](https://osswaf.ugnas.com/soft/qxl/spice-qxl-wddm-dod-0.21.zip)

2. Upload the downloaded driver archive to "Files" on your UGREEN NAS. Then, use the SMB protocol to copy the driver package to the Windows virtual machine.

3. If you're not familiar with the SMB protocol, refer to the guide: [[Tutorial] How to use SMB protocol to achieve fast multi-terminal file transfer on the LAN?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTA2MiwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjozNTksImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

![](https://file-us.ugreennas.com/admin/article/2025-08-26/314f5ca18cc0404b9ba924e091485a43.webp)

4. After copying the package to the virtual machine, extract the driver archive and locate the appropriate installer:

● For 64-bit systems: QxlWddmDod\_0.21.0.0\_x64.msi

● For 32-bit systems: QxlWddmDod\_0.21.0.0\_x86.msi

![](https://file-us.ugreennas.com/admin/article/2025-08-26/f2f2f480259e4efe8ac5e1c4053c9b0d.webp)

5. Double-click the installer to run it and wait for the installation to complete.

6. After installation, restart the Windows system to activate the driver.

7. To verify the installation, press Win + R to open the Run dialog, enter devmgmt.msc and press Enter to open Device Manager.

8. Expand [Display adapters] and confirm that the device name is shown as Red Hat QXL controller。

9. If there are no warning or question marks on the device, the driver has been installed successfully.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/ef8a6839857c4ca0adae034f34e086b4.webp)

### Method 2: Manual Installation via Windows Guest Tools ISO (For Older Systems)

**Applicable systems:** Windows 7 and other older versions.  
**Steps:**

1. Download the ISO image: [Windows Guest Tools ISO](https://osswaf.ugnas.com/soft/20241009/virtio-win-0.1.262.iso.gz)

2. In the NAS virtual machine management interface, click [Manage] > [Image] > [Add Image].

![](https://file-us.ugreennas.com/admin/article/2025-08-26/b68b1764714c400f918ec73a36a13c0f.webp)

3. Upload the previously downloaded ISO image file. You may customize the image name as desired.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/64b4ce3db56843929481b0fbd8f0abc9.webp)

4. Mount the ISO image to the virtual machine: select the target virtual machine, click [···] > [Settings] > [Basic], locate the [Image] option. Add the uploaded ISO image and click [Apply] to save the configuration.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/ff27d803d8a44ff08b8962043f5cb098.webp)

5. Start the virtual machine. Once inside the Windows system, press Win + R to open the Run dialog, type devmgmt.msc, and press Enter to open Device Manager.

6. Expand [Display adapters], right-click the current graphics device (which may show as Microsoft Basic Display Adapter), and select [Update driver] > [Browse my computer for drivers].

![](https://file-us.ugreennas.com/admin/article/2025-08-26/e5a48afdf0ee4beea5dffa8e27a770e2.webp)

![](https://file-us.ugreennas.com/admin/article/2025-08-26/9668eb92358f4290a7d81689c02c3d36.webp)

7. Select the CD drive corresponding to the mounted ISO image (e.g., D:\), then click [OK] > [Next], and wait for the system to locate and install the driver.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/dfc4d4ec96b34f28b839cd059e6f66e6.webp)

![](https://file-us.ugreennas.com/admin/article/2025-08-26/5d4f4e5c0c794a4eaa7272d42b04851e.webp)

8. When the installation is successful (as shown in the image), restart the system.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/c333480fd87346d2a9c52aab111c0408.webp)

9. After restarting, confirm in Device Manager that the graphics card model has changed to Red Hat QXL GPU. This indicates the driver installation was successful.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/f4cb3691c6694c31888811ca10fbf7fd.webp)
