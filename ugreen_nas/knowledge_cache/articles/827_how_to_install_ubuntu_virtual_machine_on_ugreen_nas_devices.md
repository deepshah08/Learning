# How to Install Ubuntu Virtual Machine on UGREEN NAS Devices

> **Article ID**: `827`  
> **Category**: `Application Guide > Virtual Machine > How to Install Ubuntu Virtual Machine on UGREEN NAS Devices`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/827  

---

**Application Notes**:

● This document applies to UGOS Pro firmware version 1.13.10.0037 and above.

● Screenshots and interfaces in this document are for reference only. Actual displays may vary depending on system or application version. Some features may change across versions, please refer to your actual interface.

### Overview

This guide walks you through the process of deploying an Ubuntu Virtual Machine on UGREEN NAS devices, including image download, upload, creation, and system installation.

**Prerequisites:**

● Ensure the device is connected to the internet and the "**Virtual Machine**" app is installed.

● Verify that your NAS model supports Virtual Machine functionality and check in the App Center whether it is available for installation.

### Step 1: Download the Ubuntu Image

It is recommended to download the Ubuntu LTS (Long-Term Support) version for better stability and compatibility with NAS virtual environments.

1. Visit one of the following mirror sites:

○ Official：`https://ubuntu.com/download`

○ AlibabaCloud: `http://mirrors.aliyun.com/ubuntu-releases/`

○ USTC: `https://mirrors.ustc.edu.cn/ubuntu-cdimage/releases/`

○ Tsinghua: `https://mirrors.tuna.tsinghua.edu.cn/ubuntu-releases/`

2. Download the 64-bit (amd64 architecture) ISO image file (e.g., `ubuntu-24.04.3-live-server-amd64.iso`).

Save the image file to your local computer. It is recommended to use an English-only file name and path, avoiding special characters.

### Step 2: Upload the Image to the NAS Image Repository

1. Log in to the NAS system and open the "**Virtual Machine**" app.

2. In the top navigation bar, click "**Manage**">"**Image**" to open the local image repository.

![](https://file-us.ugreennas.com/admin/article/2026-04-22/bb2514ab26034ca69023b20d97cf10f7.webp)

3. Click "**Add image**" and choose an upload method:

○ **From local computer**: Select the Ubuntu ISO file you just downloaded.

○ **From NAS**: If the image has already been uploaded to the NAS, select it directly from the directory.

![](https://file-us.ugreennas.com/admin/article/2026-04-22/8a96697231e9415da4faa590b29e27be.webp)

4. Assign a simple name to the image and click "**Confirm"** to start uploading.

Do not refresh or close the page during the upload process.

![](https://file-us.ugreennas.com/admin/article/2026-04-22/3a50b29c31514741b95aa0697e2579e9.webp)

### Step 3: Deploy the Ubuntu Virtual Machine

1. Return to the "**Virtual Machine**" app homepage, click "**New VM**" in the top navigation bar, and select "**Create Manually**".

![](https://file-us.ugreennas.com/admin/article/2026-04-22/be31ec72620944a2828c41a45d14cdd0.webp)

2. On the image selection page, choose the uploaded Ubuntu image and click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-04-22/700126926776415cb80aca997e6b761b.webp)

3. Select the storage location for the virtual machine data and click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-04-22/2f01538da4f046028842d07b39d16089.webp)

4. Configure basic information:

○ **VM name**: Set a custom name (e.g., ubuntu-2511) for easy identification.

○ **System type**: Select "**Linux**".

![](https://file-us.ugreennas.com/admin/article/2026-04-22/09e55e3865cd4a898dde924a16ee4e0a.webp)

5. Configure hardware resources:

○ **CPU**: It is recommended to allocate at least 2 cores.

○ **Memory**: It is recommended to allocate at least 4 GB for smooth performance.

○ **Disk**: Select **virtio** and allocate at least 50 GB for system installation and data storage.

![](https://file-us.ugreennas.com/admin/article/2026-04-22/a99f6945798b432cad1afe1846468861.webp)

6. **Configure network settings**: It is recommended to use **Bridge** mode, which assigns an independent IP address to the virtual machine, allowing access from other devices within the local network.

![](https://file-us.ugreennas.com/admin/article/2026-04-22/624bdfa578f8425fae5a3c137754d9bb.webp)

7. **Advanced settings (optional)**: Keep the boot type as the default "**bios**" (supports snapshot functionality). You may enable "**Auto start**" if needed.

![](https://file-us.ugreennas.com/admin/article/2026-04-22/faaa74aca1b54b828f3b7bfaf797b569.webp)

8. After confirming all configurations, click "**Done**" to start deployment. Do not power off or shut down the device during this process.

### Step 4: Install the Ubuntu Operating System

After the virtual machine is deployed, it will be in a powered-off state by default. Follow the steps below to initialize the system:

1. Hover your mouse over the newly created virtual machine and click "**Start**".

![](https://file-us.ugreennas.com/admin/article/2026-04-22/b09bdc0ec14b4c389e68ab697c8f7daf.webp)

2. Once the VM has started, click "**Connect**" to enter the system installation interface.

![](https://file-us.ugreennas.com/admin/article/2026-04-22/13d015aaa90642aba18e355f7b24f7d6.webp)

3. After entering the installation screen, select "**English**" from the language list, then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-04-22/a946b5caab7a4c16904f571141cbf48b.webp)

4. Choose "**English**" for the keyboard layout and click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-04-22/90e27ca6a6674fe38e5452b6b23d5026.webp)

5. Select "**Interactive installation**" and click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-04-22/fa8f04fe376e4692ae65813220bec476.webp)

6. Choose "**Erase disk and install Ubuntu**", then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-04-22/9781075442c44003ad870e91a227ecb4.webp)

7. Select "**Shanghai**" as your location and click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-04-22/d1f436b1ea3c44a08b74a93c37863e41.webp)

8. Set your name and login password, click "**Next**", and wait for the system to complete the installation automatically.

![](https://file-us.ugreennas.com/admin/article/2026-04-22/d5feb5896b8a4c6fa52b5e95bafc3fb1.webp)

9. Once the installation is complete, click "**Restart now**".

![](https://file-us.ugreennas.com/admin/article/2026-04-22/82c16bc2b8a24130911b80d419b55c1b.webp)

10. When the screen turns black and shows the message `Please remove the installation medium, then press ENTER:`*,* press the **Enter** key.

![](https://file-us.ugreennas.com/admin/article/2026-04-22/374f2f52ff644b82904d8dc9c2930cce.webp)

11. After rebooting, click your username and enter the password you set to log in.

![](https://file-us.ugreennas.com/admin/article/2026-04-22/62e388ed387a4c76ac96c644fbfc7684.webp)

### Notes

● Only ISO image files are supported. Do not upload other formats, or deployment will fail.

● When allocating hardware resources, ensure sufficient CPU and memory are reserved for the NAS system to avoid performance issues.

● Hardware configuration cannot be modified while the virtual machine is running. To make changes, power off the VM first, then edit and restart it.

● If a virtual machine exists in a storage pool, that storage cannot be deleted directly. You must delete the VM first to release the storage.
