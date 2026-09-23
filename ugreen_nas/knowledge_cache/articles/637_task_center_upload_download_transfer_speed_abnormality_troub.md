# Task Center Upload/Download Transfer Speed Abnormality Troubleshooting Guide

> **Article ID**: `637`  
> **Category**: `Application Guide > Sync & Backup > FAQ > Task Center Upload/Download Transfer Speed Abnormality Troubleshooting Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/637  

---

## Problem Description

When checking the file upload and download transfer speeds in the UGREEN NAS "Task Center" application, it is found that the upload/download speed is slow or the transfer fails.

![](https://file-us.ugreennas.com/admin/article/2025-08-06/12c71c8764f64428848975bc4b3f1155.webp)

## Solution

### Check the NAS Network Connection Type

Confirm whether the NAS's network connection type is bridging. If it is, check the type of bridge (Normal Bridge/Virtual Bridge). **Normal bridging** is typically used for simple network expansion, while **virtual bridging** may involve more complex network configurations that could affect speed. For more details, please refer to: [What is Network Bridging?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTEyMCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjozODcsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

**Operation Guide:**

Open the "Control Panel" app, go to [Network] > [Network Connection] page, and check the connection method of the LAN port. If a virtual network card starting with **BR (Normal Bridge)** or **VBR (Virtual Bridge)** is generated, it indicates that the connection type is in bridge mode.

![](https://file-us.ugreennas.com/admin/article/2025-08-06/e65f76278a974e33af3cc268871e1dee.webp)

![](https://file-us.ugreennas.com/admin/article/2025-08-06/39e07aa0cc7a41b4891c4cc8c554a439.webp)

### Check Computer Performance

**Check Hard Disk Type (HDD / SSD):** Solid-state drives (SSDs) typically offer much faster read and write speeds than hard disk drives (HDDs). You can use hard disk testing tools (such as CrystalDiskMark) to check the actual read and write speeds of your hard disk.

**Operation Guide:**

● **Check the Hard Disk Model via Device Manager:** On a Windows computer, press theWin + Xshortcut to open "Device Manager," expand "Disk Drives," and check the hard disk model. If the model contains "SSD" or "NVMe," it is a solid-state drive; if it contains "HDD" or terms like "Caviar," it is a hard disk drive.

![](https://file-us.ugreennas.com/admin/article/2025-08-06/c45691896c864393989786348bf138a6.webp)

● **Use CrystalDiskMark to Test Hard Disk Read/Write Speed:**

Download and install [CrystalDiskMark](https://crystalmark.info/en/software/crystaldiskmark/) . Open CrystalDiskMark, select the hard disk you want to test, and click the "Start" button to begin the test. After the test is complete, check the results for "Seq Q32T1" (sequential read/write speed) and "4KiB Q8T8" (random read/write speed). The sequential read/write speed of an SSD is typically above 500MB/s, while the sequential read/write speed of an HDD is usually around 100MB/s.

**Check CPU and Memory Usage:** Insufficient CPU performance or available memory may affect data processing speed.

**Operation Guide:**

On a Windows computer, press theCtrl + Shift + Escto open the "Task Manager." Switch to the "Performance" tab to view CPU and memory usage. If the usage is consistently close to 100% or there is insufficient available memory, it will impact speed.

![](https://file-us.ugreennas.com/admin/article/2025-08-06/0a15b7ecba55492199847a32a698b9e1.webp)

### Check Computer Network Connection Type and Port Speed

Confirm the computer's connection type (Wi-Fi / Wired). If using a Wi-Fi network, it is recommended to switch to a wired connection.

**Operation Guide:**

**Confirm the connection type through the system tray icon:**In the bottom-right corner of the Windows taskbar, find the network connection icon (usually a Wi-Fi signal icon or Ethernet icon). Hover your mouse over the icon to display the current connection type and network name.

![](https://file-us.ugreennas.com/admin/article/2025-08-06/05df9db4d3eb45f3bcf8cf70626952a5.webp)

Check the computer's network port speed and NAS network port speed (Gigabit/2.5G/10G, etc.) to rule out any issues with the computer itself and ensure the network connection is functioning properly.

**Operation Guide:**

**Check the computer's network port speed through the Control Panel:**On a Windows computer, press theWin + Rshortcut to open the "Run" dialog, type control paneland press Enter. Click "Network and Internet," then click "Network and Sharing Center." In the left panel, click "Change adapter settings." Double-click the network adapter you want to check (Ethernet or Wi-Fi), and in the pop-up window, you can view the "Speed" information, which shows the network port speed.

![](https://file-us.ugreennas.com/admin/article/2025-08-06/6da7302be0ba458e93429800d0652a4f.webp)

**Test Network Bandwidth Speed Between Computer and NAS Using SMB File Transfer or Third-Party Tools (e.g., iperf3):**

● On a Windows computer, you can directly enter \\<NAS的IP地址>in the address bar of File Explorer to access the shared folder. Copy a test file to your local machine, record the transfer time, and calculate the transfer speed. For example, if transferring a 1GB file takes 10 seconds, the transfer speed would be: 1GB / 10 seconds = 100MB/s. For more detailed steps, refer to: [Efficient File Transfer Across Devices: SMB Protocol Configuration and Usage Guide (supports iPad, iPhone, Windows, macOS).](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTA2MiwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjozNTksImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

● To use a third-party tool like iperf3, download and install the [iperf3](https://iperf.fr/iperf-download.php) client on your computer. Then, press Win + R, typecmd, and pressEnter. Enter the command:iperf3.exe -c <NAS IP address> -p <port number> -t <test duration>. For example:

```
iperf3.exe -c 172.17.70.87 -p 9999 -t 20
```

For more operation details, please search online or refer to this network tutorial (for reference only): [The detailed installation method and usage tutorial for Iperf3](https://blog.csdn.net/weixin_41500064/article/details/135279975)

### Check the method of computer client login to NAS

Confirm the login method of the computer connecting to the NAS (LAN IP / UGREENlink connection / P2P / DDNS, etc.), and check whether it is HTTP or HTTPS. HTTPS is a more secure connection method, and it is recommended to use HTTPS whenever possible.

![](https://file-us.ugreennas.com/admin/article/2025-08-06/59887ddbbcf24e4fa4187147e019f7b3.webp)

If using DDNS to log in, and encountering upload/download errors, it is recommended to visit [ipw.cn](https://ipw.cn/) to check the current IP address and ensure the DDNS resolution is correct. Incorrect DDNS resolution may lead to connection failures or slow speeds.

### Check if security software is blocking

Check if the computer has security software installed (such as 360 Security Guard). If such software is installed, it is recommended to completely exit the software and retry the transfer to rule out the impact of security software on transfer speed.

**Operation Guide:**

● On a Windows computer, press theCtrl + Shift + Escshortcut to open the “Task Manager”.

● In the "Task Manager," switch to the "Process" tab.

![](https://file-us.ugreennas.com/admin/article/2025-08-06/405efdd0ae52439f98ed2cddef218d95.webp)

● Look for security software processes, such as 360tray.exe(the tray program for 360 Security Guard).

● If you find these processes, it means the corresponding security software is installed on your computer.

● Right-click and select "End Task" to exit the security software, then retry the file transfer.

### Check if Network Speed Limits Are Set

Try switching networks and perform the file transfer again to rule out the possibility of bandwidth restrictions on the current network.

**Operation Guide:**

● If you are using a Wi-Fi network, it is recommended to switch to a wired network for testing, or switch from one Wi-Fi network to another.

● In the new network environment, perform the file transfer test again, record the transfer time, and calculate the transfer speed.

To check if there are bandwidth restrictions on the current network

**Operation Guide:**

● Check the configuration of the router network device, especially the bandwidth settings for the ports.

● Log in to the router management interface, check the port settings, and confirm if there are any bandwidth limits.

● Check the load balancing configuration to ensure traffic is evenly distributed across the ports.

### Check File Size and Type

During the file transfer process, the file size and type can significantly affect the transfer speed.

Large files generally have more stable transfer speeds as they occupy more continuous storage space, reducing hard disk addressing time. However, when there are many small files, the transfer speed may decrease due to the large number of files. Each file needs to be handled individually, including opening, reading, transferring, and closing, which adds extra overhead.

If there is an extraction task during the transfer process, the decompression process will consume additional time and computing resources, thus affecting the transfer speed.

### Check Task Queue

Check the task queue in the NAS task center to ensure that there are not too many tasks running simultaneously, as this may cause a slowdown in speed.

If there are too many tasks, it is recommended to pause some non-essential tasks to improve the transfer speed of the current task.

If the above methods do not resolve the issue, it is recommended to contact UGREEN NAS official technical support, providing detailed problem descriptions and troubleshooting information to receive further assistance.
