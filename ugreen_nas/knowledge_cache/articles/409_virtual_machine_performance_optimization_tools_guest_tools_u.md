# Virtual Machine Performance Optimization Tools (Guest Tools) User Guide

> **Article ID**: `409`  
> **Category**: `Application Guide > Virtual Machine > FAQ > Virtual Machine Performance Optimization Tools (Guest Tools) User Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/409  

---

> Applicability: This document applies to UGOS Pro firmware version 1.8.20.0012. The screenshots in this document are for reference only. The actual interface may vary depending on the system or application version. Some options and features may differ in different versions. Please refer to the actual interface.

Guest Tools is a driver toolkit specifically designed for "Virtual Machine" to enhance performance and improve user experience:

● Provides more accurate memory display

● Supports virtio disk and network drivers to improve disk I/O and network performance

● Extends graphics resolution support

**Note:** Guest Tools only supports **Windows Virtual Machine** (Win7, Win10, Win11). It is not available for Linux Virtual Machines.

## Download and Upload the Toolkit to the Local Image Repository

1. Download the [Guest Tools package](https://osswaf.ugnas.com/soft/20241009/virtio-win-0.1.262.iso.gz) and extract it to obtain the `.iso` image file.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/ed0c6e3f5acd4af7815f82daf730295e.webp)

2. Open the "Virtual Machine" application, go to **"Manage" > "Image"**, and click **"Add image"** in the "Local image repository" to upload the file.

3. Once uploaded, the driver package will be available in the "Local image repository".

![](https://file-us.ugreennas.com/admin/article/2025-09-04/c11021f412d3414ba81049825cc33d49.webp)

## Mount the Driver Package Image

1. Open the Virtual Machine application, locate the target Virtual Machine, and click **"···" > "Settings"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/0753ebd1d0dd416fba3e0ef76d68b2ce.webp)

If the Virtual Machine is running, click **"Power" button > "Shutdown"** first.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/cf9d8e8e3ed84297b533fcd4c0b9a6f9.webp)

2. On the **"Basic"** configuration page, under the Image section, click **"Add"** and select the uploaded Guest Tools image.

3. Set "Network" to **"virtio"**.

4. Click **"Apply"** to save.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/a916c166ae8e41cc8c2c29e2cadd2e91.webp)

## Install Drivers

### Win10/Win11 – One-Click Installation

1. After mounting the driver image, start the Virtual Machine. In Windows, open **"Computer" > "CD Drive"** (driver image).

![](https://file-us.ugreennas.com/admin/article/2025-09-04/92a8050217894de39853c45307d1b1ca.webp)

2. Locate and run `virtio-win-gt-x64.msi` (64-bit) or `virtio-win-gt-x86.msi` (32-bit).

![](https://file-us.ugreennas.com/admin/article/2025-09-04/5f18af64f2444ecc8f1d2e27d2abf965.webp)

3. Follow the installation wizard to complete installation.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/d4c2b700dd91447098e379d7ee70a65a.webp)

### Win7 – Manual Installation

1. After mounting the driver image, start the Virtual Machine and enter Windows.

2. Press `Win+R`, type `devmgmt.msc`, and open **"Device Manager".**

![](https://file-us.ugreennas.com/admin/article/2025-09-04/538876c50d004dccbd80ba184cf73b4e.webp)

3. Under **"Other devices"**, locate the uninstalled **"PCI Simple Communication Controller"** and **"PCI Device"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/3f36f41ddc98495f9cc474266a11d374.webp)

4. Click the device and select **"Update Driver"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/70ca2e36560c4974a35229d823a5f893.webp)

5. Click **"Browse my computer for driver software"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/cc85d1e3917a4deeb835af415dd9f0b6.webp)

6. Click **"Browse"** and select the mounted **CD Drive** (driver image).

![](https://file-us.ugreennas.com/admin/article/2025-09-04/ecf6689973064b4a89fbab8e23902762.webp)

7. The system will automatically install the drivers. Once both devices are installed, the driver setup is complete.

## Mount the Virtio Disk Driver

### Win7

Ensure the Virtual Machine has no OS installed.

1. After mounting the driver image, start the Virtual Machine and proceed to the "Where do you want to install Windows?" page.

2. Click **"Load Driver" > "Browse"**, locate the mounted CD Drive (driver image), navigate to `\viostor\w7\amd64`, and click **"OK"** to load the driver.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/89c9431a2fd14a689db2ea218d50b943.webp)

3. Click "Next" to begin installing the disk driver.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/5fd632c4dc7a439fb95d280a83df737d.webp)

4. Once loaded, select the newly displayed disk and click **"Next"** to continue Windows installation.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/224d68690fad47ca96e7595085ab153a.webp)

### Win10/Win11

Ensure the Virtual Machine has no OS installed and the driver image is mounted.

1. After mounting the driver image, start the "Virtual Machine" and proceed to the **"Where do you want to install Windows?"** page.

2. Click **"Load driver" > "Browse"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/8f7ac8485dc7420982586dea0d5bcdee.webp)

3. Click **"OK"** to load all drivers.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/ba1f8d9a42f64d9385e5842efb7a6b92.webp)

4. Select the driver matching your OS and click "Next" to install.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/a53369ada7e34cddb690d92e523ad8b8.webp)

5. After installation, the new disk will appear. Click **"Next"** to continue Windows installation.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/ef7b97501fe44f348372bf5fcdda8aee.webp)

## Enable Memory Driver Service on Win7

After installing Guest Tools, memory usage on Win7 may display incorrectly. You need to manually enable the memory driver service:

![](https://file-us.ugreennas.com/admin/article/2025-09-04/62e53678d88d43e9b63557be907a1fcf.webp)

1. In Windows, open **"Computer" > "CD Drive"**, navigate to `\Balloon\w7\amd64`, and copy `blnsvr` to `C:\Windows\System32`.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/5f0cdfc72b91449b9f2b760242732b27.webp)

2. If prompted for permission, click "Continue" to complete the copy.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/e37cf803133c494f8d035b79bf4d48f5.webp)

3. Run **CMD** as administrator.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/a9fa38ea2efe436291407371f6a0899e.webp)

```
blnsvr -i
```

4. Enter `blnsvr -i`. When "Service RUNNING" appears, the service is active.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/971278e641564ee2a8d5c6f02146f05b.webp)

Return to the Virtual Machine management interface, and you will see that memory usage display for the Win7 Virtual Machine is now normal.

![](https://file-us.ugreennas.com/admin/article/2025-09-04/16586904e6464c988ff251466f6896c6.webp)
