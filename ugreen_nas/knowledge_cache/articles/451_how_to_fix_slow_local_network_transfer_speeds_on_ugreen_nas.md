# How to Fix Slow Local Network Transfer Speeds on UGREEN NAS?

> **Article ID**: `451`  
> **Category**: `Application Guide > Control Panel > FAQ > How to Fix Slow Local Network Transfer Speeds on UGREEN NAS?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/451  

---

## Issue Description

When accessing a UGREEN NAS over the local network, slow or unstable upload and download speeds are usually related to the network path, connection method, Ethernet cable category, file type, storage performance, or background tasks.

If local network transfer speeds remain at only a few MB/s, or stay around 10–14 MB/s in a 2.5GbE network environment, follow the troubleshooting steps below.

## 1 Check for a 100 Mbps Bottleneck

Local network transfer speed depends on the entire network path. If any device or connection in the path supports only 100 Mbps, or negotiates down to 100 Mbps, actual transfer speeds will typically be limited to around **10–12.5 MB/s**.

Check the following:

● NAS Ethernet port

● Computer network adapter

● Router port

● Switch port

● Ethernet cable

● USB network adapter or docking station

For example:

100 Mbps ÷ 8 = 12.5 MB/s

If transfer speeds in a Gigabit or 2.5GbE local network remain close to 10–14 MB/s, first check whether any device or connection has fallen back to 100 Mbps.

## 2 Check the Negotiated Link Speed

Check the connection speed of the NAS, computer, router, and switch.

Common link speeds include:

● 100 Mbps

● 1000 Mbps

● 2.5 Gbps

● 10 Gbps

If the connection speed is shown as **100 Mbps**, the current network path has not reached Gigabit or higher speeds.  
Try replacing the Ethernet cable, switching to another router or switch port, and restarting the NAS, computer, and network devices before testing again.

## 3 Check the Ethernet Cable Category and Condition

The category and condition of the Ethernet cable can affect transfer speeds. A **Category 6 (CAT6)** or higher-rated cable is recommended. Low-quality, aging, or damaged cables may cause the connection to negotiate at a lower speed, drop packets, or become unstable.

If transfer speeds are abnormal, test again with a cable confirmed to support Gigabit or higher speeds.

## 4 Prefer a Wired Network Connection

Transfer speeds may fluctuate significantly when a computer or mobile device accesses the NAS over Wi-Fi.

Wi-Fi performance can be affected by:

● Signal strength

● Distance between the device and router

● Obstructions such as walls and appliances

● Nearby wireless interference

● Multiple devices using Wi-Fi at the same time

For large file transfers or speed tests, connect both the computer and NAS to the network using Ethernet cables. A wired connection is generally more stable and provides a more accurate indication of actual local network performance.

## 5 Confirm That the NAS Is Accessed Through Its Local IP Address

Confirm that the current access path is within the local network. Whenever possible, access the NAS using its local IP address, such as through an SMB shared path.

If a public domain name, remote access address, relay connection, or external network address is used, transfer speeds may be limited by the internet connection and will not reflect local network performance.

## 6 Test with a Single Large File

The number and size of files can affect transfer speeds. When a large number of small files is transferred at once, the system must repeatedly create, read, and write files, which can result in significantly lower speeds than transferring a single large file.

For testing, use one large file, such as a video file or archive larger than 5 GB.

If a single large file transfers at a normal speed but a large number of small files transfers more slowly, this is usually expected behavior. Multiple small files can be compressed into a single archive before transfer.

## 7 Check NAS Storage Performance and Background Tasks

If the network connection is normal but transfer speeds are still low, continue by checking the NAS storage status and background tasks.

The following may affect transfer speeds:

● Low drive read/write performance

● Use of SMR drives or other lower-performance drives

● Drive health issues or bad sectors

● Storage space synchronization, verification, or rebuilding

● Background download, backup, or sync tasks

● Media library scanning, scraping, or indexing

● Multiple users or apps accessing the same storage space at the same time

Pause background tasks such as downloads, backups, synchronization, and media scanning, then test again using a single large file.

## 8 Check Network Device Performance and Port Status

Issues with the router, switch, or network ports may also reduce local network transfer speeds.

Common causes include:

● Insufficient router or switch performance

● Network congestion caused by multiple devices accessing the NAS at the same time

● Loose, oxidized, or poorly connected network ports

● Unstable USB network adapters, docking stations, or other intermediate devices

When possible, connect the computer and NAS to the same switch and bypass intermediate devices before testing again.

## 9 Reduce the Impact of Network Congestion

When multiple devices use the network at the same time, local network transfer speeds may decrease.

Try the following:

● Pause high-bandwidth downloads or uploads on other devices.

● Avoid having multiple users access large files on the NAS at the same time.

● Configure QoS on the router to prioritize local file transfers.

● Avoid running resource-intensive downloads, backups, or sync tasks during file transfers.

## 10 Reference Speeds for Different Network Connections

The theoretical maximum transfer speed varies by network type:

● **100 Mbps network:** Approximately 12.5 MB/s

● **1 Gbps network:** Approximately 125 MB/s

● **2.5GbE network:** Approximately 312.5 MB/s

● **10GbE network:** Approximately 1,250 MB/s

Actual speeds are usually lower than these theoretical values because of protocol overhead, drive performance, device performance, file type, and network conditions.

## 11 Recommended Troubleshooting Order

Follow these steps in order:

1. Confirm that both the computer and NAS are connected through Ethernet.

2. Confirm that the NAS, computer, router, and switch ports are not operating at 100 Mbps.

3. Replace the Ethernet cable with a CAT6 or higher-rated cable.

4. Try another router or switch port.

5. Access the NAS using its local IP address.

6. Test the speed using a single large file.

7. Pause background tasks such as downloads, synchronization, backups, and media scanning.

8. Check drive health and storage space status.

9. Bypass USB network adapters, docking stations, and other intermediate devices, then test again.

## 12 What to Do If the Issue Persists

If local network transfer speeds remain abnormally low after completing the checks above, contact UGREEN NAS technical support.

When submitting feedback, provide the following information:

● NAS model

● System version

● Screenshot of the computer network adapter speed

● Screenshot of the NAS Ethernet port speed

● Router or switch model

● Ethernet cable category

● Current access method, such as SMB, Files, or browser download

● Test file size

● Screenshot showing the actual transfer speed
