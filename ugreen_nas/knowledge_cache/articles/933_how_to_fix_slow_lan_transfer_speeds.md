# How to Fix Slow LAN Transfer Speeds?

> **Article ID**: `933`  
> **Category**: `Troubleshooting > Network Failure > How to Fix Slow LAN Transfer Speeds?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/933  

---

## Applicability

**Applicable Version**: NAS Firmware 1.15.0.0032 or later.

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

When accessing a UGREEN NAS over LAN, slow or unstable transfer speeds are usually related to network connections, network adapter link speeds, connection methods, or storage read/write performance.

You can follow the steps in this article to check the network adapter speed of your computer and NAS, and use the iperf3 tool to test the network bandwidth between the NAS and your computer.

## Factors That May Affect Transfer Speed

LAN transfer speeds may be affected by the following factors:

● Computer network adapter link speed.

● NAS network adapter link speed.

● Ethernet cable specifications and quality.

● Switch or router port speed.

● Wired or wireless network connection method.

● Read/Write performance of NAS storage.

● Read/Write performance of the computer's local disk.

Wired networks usually operate in full-duplex mode, while wireless networks usually operate in half-duplex mode. During transmission, wireless networks are more susceptible to interference and device resource usage, resulting in lower speed and stability compared with wired networks.

## Check the Computer Network Card Speed

Using a Windows computer as an example, follow the steps below to check the current network card speed.

1. Open Control Panel, then go to "**Network and Internet**" > "**Network Connections**".

2. Find the network adapter currently in use, right-click it, and select "**Status**".

![](https://file-us.ugreennas.com/admin/article/2026-08-26/14e8919dd8e34286b208bc69c226c42b.webp)

3. In the Ethernet Status window, check the Speed value.

![](https://file-us.ugreennas.com/admin/article/2026-08-26/66894575835743bba9cd3475354718ca.webp)

If the value is displayed as **1.0 Gbps**, it means the network card has negotiated a 1 Gbps link speed.

If the detected speed does not meet expectations, check the network card, Ethernet cable, switch, router, and other network link devices.

## Check the NAS Network Card Speed

If the NAS network card speed does not meet expectations, check whether the NAS network port is properly connected and whether the uplink network devices are operating at the expected speed.

### PC/Web

1. Go to Control Panel, then click "**Network**" > "**Network connection**".

2. Check the current NAS network card speed.

![](https://file-us.ugreennas.com/admin/article/2026-08-26/13acace9699e412a8d3be5273f2b8ce2.webp)

### Mobile

1. Go to ControlPanel, tap "**Network**", then tap the currently used **LAN**.

2. Check the current NAS network card speed.

## Use iperf3 to Test the Transfer Speed Between the NAS and Computer

iperf3 can be used to test the network bandwidth between the NAS and computer. This test is mainly used to determine whether the network link is working properly and does not directly represent file copy speed.

UGREEN NAS terminals include iperf3 by default. During the test, the NAS acts as the server, and the computer acts as the client.

### Start the iperf3 Server on the NAS

1. Go to Control Panel, click "**Terminal device**" > "**SSH**", and select "**Enable**".

2. Log in to the NAS underlying system via SSH using an administrator account.

For details, refer to the related document: [How to Connect to UGOS Pro via SSH with Root Privileges](https://support.ugnas.com/knowledgecenter/detail/article/en-US/481)

After logging in, enter `iperf3 -s` and press Enter to start the server:

![](https://file-us.ugreennas.com/admin/article/2026-08-26/b9ca93ed4bb24a579c2154c893291c68.webp)

If you need to specify a port, use `iperf3 -s -p Port number`.

### Prepare the iperf3 Client on the Computer

1. Visit the [iperf3](https://iperf.fr/iperf-download.php) download page and download the iperf3 client for the corresponding computer operating system.

2. On a Windows computer, press `Win + R`, enter `cmd`, and press Enter to open Command Prompt.

3. Drag the downloaded **iperf3.exe** file into the Command Prompt window.

After dragging the file, the command line will automatically fill in the path of the iperf3 program.

![](https://file-us.ugreennas.com/admin/article/2026-08-26/6f759c7ef220417eac424356e0a3f294.webp)

## Test the Upload Speed from the Computer to the NAS

Enter the following command in Command Prompt on the computer: `iperf3 -c NAS_IPaddress -p Port number`

Example: `iperf3 -c 192.168.71.98 -p 30001`

This command tests the transfer speed from the computer to the NAS.

## Test the Download Speed from the NAS to the Computer

Enter the following command in Command Prompt on the computer: `iperf3 -c NAS_IPaddress -p Port number -R`

Example: `iperf3 -c 192.168.1.100 -p 5201 -R`

`-R` indicates reverse transmission. This command tests the transfer speed from the NAS to the computer.

![](https://file-us.ugreennas.com/admin/article/2026-08-26/109da1818a0149aa891910b659327e71.webp)

## How to Interpret the Test Results?

You can check the **bandwidth** field in the test results. In a 1 Gbps network environment, if the bandwidth is close to **900 Mbits/sec**, it indicates that the network link is basically working properly. Considering the loss caused by cables, switches, routers, and protocols, this result can be considered close to the 1 Gbps speed.

：If both the computer and NAS network card speeds are 1 Gbps or higher, but the file transfer speed is only around **10 MB/s**, continue troubleshooting the following:

● Computer network card configuration.

● Ethernet cable and port connection status.

● Switch or router port speed.

● Whether a 100 Mbps link exists.

● Whether the transfer is performed over Wi-Fi.

● Read/Write performance of NAS storage.

● Read/Write performance of the computer disk.

If the iperf3 test shows normal bandwidth but the actual file transfer speed is abnormal, it usually indicates that the network link is basically working properly. In this case, focus on checking the NAS storage performance, hard disk status, background tasks, and the read/write speed of the computer's local disk.

## Common iperf3 Parameter Descriptions

The following parameters are provided for troubleshooting reference only.

|  |  |
| --- | --- |
| Parameter | Description |
| `-s` | Run in server mode. |
| `-c` | Run in client mode and connect to the specified server IP. |
| `-p` | Specify the port number. It must match the server port. |
| `-R` | Reverse transmission. Sends data from the server to the client. |
| `-t` | Specify the test duration. The default is usually 10 seconds. |
| `-i` | Set the report interval. |
| `-f` | Specify the bandwidth display unit, such as Kbits, Mbits, KBytes, or MBytes. |
| `-P` | Specify the number of parallel connections. |
| `-J` | Output test results in JSON format. |
| `--logfile` | Output test results to a log file. |
| `-u` | Use the UDP protocol for testing. |
| `-4` | Use IPv4 only. |
| `-6` | Use IPv6 only. |

## Notes

● iperf3 tests network bandwidth, which is not the same as file copy speed.

● File copy speed is also affected by hard disk performance, number of files, file size, and system tasks.

● Speed may fluctuate significantly in a Wi-Fi environment. It is recommended to use a wired network for testing whenever possible.

● Before testing, pause high-resource tasks such as downloads, backups, synchronization, and media indexing.

● If the issue still cannot be identified, contact UGREEN NAS technical support and provide screenshots of the network card speed, iperf3 test results, and file transfer speed.
