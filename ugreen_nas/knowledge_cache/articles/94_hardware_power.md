# Hardware & Power

> **Article ID**: `94`  
> **Category**: `Application Guide > Control Panel > Hardware & Power > Hardware & Power`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/94  

---

**Applicable Version:** UGOS Pro 1.10.0.0092 and above

Screenshots and interfaces in this document are for reference only. Actual displays may vary depending on system or application version. Some features may change across versions, please refer to your actual interface.

# Feature Overview

In [Control Panel] > [Hardware & Power], you can configure the following settings:

● Enable memory compression

● Control buzzer alerts

● Adjust fan speed modes

● Adjust LED indicator brightness

● Configure power management modes

You can also set up scheduled startup and shutdown, enable hard drive sleep, and connect a UPS device.

# General

In the [General] page, you can configure the device's buzzer notifications, cooling fan speed modes, LED indicator brightness, and power management mode. Click the corresponding option to make adjustments.

![](https://file-us.ugreennas.com/admin/article/2025-10-21/25bf5982aa544327999e79aba3077d1b.webp)

## Memory Compression

The memory compression feature improves memory utilization and system performance by compressing part of the data stored in memory. When memory usage reaches a certain threshold, the system automatically performs compression to reduce memory consumption and lower disk swap frequency, thus enhancing overall system performance.

**Access path:**

● **PC:** Open [Control Panel] > [Hardware & Power] > [General], then enable **"Memory compression"**.

● **Mobile**: Open [Control Panel] > [Hardware & Power] > [Memory compression], then enable **"Memory compression"**.

**Note:**  
Under high workloads or in specific application scenarios, the compression and decompression process may introduce some system load. The actual performance improvement may vary depending on the type of applications and system load.

# Power

In the [Power] page, you can configure NAS boot and shutdown settings (such as auto power-on when power is supplied and wake on LAN (WOL)), set scheduled startup and shutdown, and enable hard drive sleep and USB hard drive sleep.

![](https://file-us.ugreennas.com/admin/article/2025-10-21/9c61040148fd4c15bef641ca110d1be2.webp)

## Auto Power-on When Power is Supplied

When this feature is enabled, the NAS will automatically start up after a power outage once power is restored.

When used together with smart plugs or similar tools, it allows remote power-on control, enhancing convenience.

## Wake on LAN (WOL)

The wake on LAN feature allows the NAS to be powered on remotely through the network. Once enabled, you can use a WOL-supported program within the local network to send a wake-up command to the NAS by entering its **MAC address**, for example, through a compatible router or client tool.

**To wake up the device via the UGREEN NAS client:**

● **PC:** Open the UGREEN NAS client. On the login screen, click [More Connections], then select [Wake on LAN]. The client saves previously connected devices, allowing you to wake them up with one click or by entering their MAC address.

![](https://file-us.ugreennas.com/admin/article/2025-10-21/d1b3dd7c4e7e4234b5db0c55ff9b9707.webp)

● **Mobile:** Open the UGREEN NAS client. On the login screen, tap the dropdown button next to the device address bar, then select [Wake on LAN]. You can also wake up devices from history or enter a MAC address manually.

![](https://file-us.ugreennas.com/admin/article/2025-10-21/b1a17f3241b34814b1aa8e611dd7a259.webp)

**Note:**

● When using a third-party WOL program to wake up your UGREEN NAS, do not set the **broadcast address** to `255.255.255.255`. For example, if your router address is `192.168.31.1`, you should use `192.168.31.255` as the broadcast address.

● The NAS device's **MAC address** can be found in [Control Panel] > [About].

## Scheduled Startup and Shutdown

The system supports scheduled startup and shutdown, allowing it to automatically power on or off at preset times. This helps users save energy and optimize the usage experience.

**Steps:**

1. Open the [Control Panel] and click [Hardware & Power].

2. Under [Power], check **"Enable Scheduled Startup and Shutdown"**.

3. Configure the following options:

● Frequency: Choose from every day, weekdays, weekends, or custom time.

● Time: Set using the 24-hour format.

● Action: Choose boot or shutdown.

4. Click **"OK"** to add the schedule.

**Notes:**

● Multiple scheduled tasks can be created.

● Once this feature is enabled, **"Auto Power-on When Power is Supplied"** will be automatically activated to ensure the device resumes operation after a power outage.

● If a system update is available, the NAS will prioritize completing the system upgrade before executing the scheduled shutdown.

● If there are ongoing non-interruptible tasks (such as system updates, data migration, or snapshot operations), the system will skip the current scheduled shutdown.

## Hard Drive Sleep Settings

On this page, you can configure hard drive sleep for internal drives and USB hard drive sleep for external USB drives.

When a drive remains idle beyond the specified time, the system will automatically put it into sleep mode to reduce power consumption and extend its lifespan.

**Notes:**

● "Idle" refers to the state when there are no read or write operations on the drive.

● The drive will automatically wake up when an access request occurs.

● This feature only takes effect if the hard drive supports sleep mode. Please consult the drive manufacturer for confirmation.

![](https://file-us.ugreennas.com/admin/article/2025-10-21/86dc84f6056f4fe6b5fbb71f3d1f224a.webp)

# Uninterruptible Power Supply (UPS)

A UPS is a backup power device that provides temporary power to your UGREEN NAS in the event of a power outage, preventing data loss or system shutdown caused by sudden power failure.

**Supported UPS Connection Types:**

The system supports the following three UPS connection methods:

● **USB:** Connect the UPS directly to the NAS via a USB cable.

You can refer to the [UGREEN NAS Products Compatibility List](https://nas.ugreen.com/pages/compatibility) for supported UPS models.

● **SNMP:** Communicate with a network-based UPS device via the SNMP protocol.

● **Network UPS Slave:** Connect to a master UPS device over the network to share UPS power status information and enable coordinated protection for multiple NAS units.

## Enable USB UPS

UGREEN NAS supports connecting a UPS via a USB interface to provide backup power. Follow the UPS manufacturer's instructions to properly connect the communication and USB data cables to the NAS, then complete the setup as follows:

**Steps:**

1. Open the [Control Panel] and navigate to [Hardware & Power] > [UPS].

The system will automatically detect any connected UPS device.

2. Once detected, click **"Connect"**.

![](https://file-us.ugreennas.com/admin/article/2025-10-21/babe3ea068d6411a8828b3209a03d155.webp)

After successful connection, you can view the UPS's battery capacity, remaining available time, and configure UPS protection mode.

![](https://file-us.ugreennas.com/admin/article/2025-10-21/fb2fe73fb6ff45cba8234c7d12469607.webp)

**Protection Modes**

When a power outage occurs, the UPS provides temporary power to the NAS and executes one of the following protection modes (a waiting time can be set):

● **Standby Mode:** The NAS stops all services to prevent data loss and automatically shuts down when the UPS battery is depleted.

● **Auto Shutdown:** The NAS automatically shuts down once the preset waiting time is reached.

**Notes:**

● Regardless of the selected mode, the NAS will automatically shut down when the UPS battery is exhausted.

● If auto power-on when power is supplied is enabled, the NAS will automatically restart once power is restored.

## Enable SNMP UPS

Using SNMP (Simple Network Management Protocol), your UGREEN NAS can communicate with a UPS device that supports the SNMP protocol to monitor power status and perform automatic shutdown management.

Before connecting, ensure the following conditions are met:

● The UPS device supports the SNMP protocol and the SNMP service is enabled on its management interface.

● The NAS and the UPS are on the same local network.

● You have obtained the UPS device's SNMP IP address, MIB name, SNMP version (v1/v2c), and SNMP community information.

![](https://file-us.ugreennas.com/admin/article/2025-10-21/2990f6f8b78b4be08add4fe97c2eb75f.webp)

**Steps:**

1. Open the [Control Panel] and go to [Hardware & Power] > [UPS], then select **SNMP UPS** as the UPS type.

2. Enter the following information:

● **Device IP Address:** The IP address of the UPS SNMP management interface.

● **MIB Name:** The management information base identifier provided by the UPS, used to retrieve UPS status data.

● **SNMP Version:** Select the SNMP protocol version used by the UPS (v1 or v2c).

● **Community:** The authentication string for SNMP access, typically set to "public" or a custom value defined by the manufacturer.

3. Click **"Apply"**. The system will attempt to establish communication with the UPS.

4. Once connected, you can configure the power protection mode (standby mode or auto shutdown) and set a waiting time as needed.

**Notes:**

● Ensure that the SNMP service on the UPS is enabled; otherwise, the NAS will not be able to connect.

● MIB file naming conventions may vary by manufacturer — refer to your UPS manual or the official website for accurate information.

● UGREEN NAS does not support the SNMP v3 protocol.

● If "Auto Power-on When Power is Supplied**"** is enabled, the NAS will automatically restart once power is restored.

## Enable NUT Server and Network UPS Slave Services

When multiple NAS devices share the same UPS, you can enable the NUT Server service to achieve centralized power management.

If one NAS device is connected to the UPS via USB, it can act as the Network UPS Master (NUT Server) — communicating directly with the UPS and broadcasting real-time power status information to other NAS devices. The remaining NAS devices function as NUT Slaves, receiving UPS status updates over the network and automatically performing the configured power protection actions.

Once the NUT Server is enabled, if the UPS detects a power outage or low battery, the master NAS will immediately send notifications to all connected slave NAS devices. This ensures that all systems in a multi-device setup can safely shut down in sync, preventing data corruption or system errors during unexpected power failures.

For detailed configuration steps, please refer to [How to Connect and Configure a UPS on UGREEN NAS to Ensure Data Safety During Power Outage?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6NTQ1NCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo3MDgsImFydGljbGVWZXJzaW9uIjoiMS4wIn0%3D) .

### **Update UGREEN UPS Firmware**

When using a UGREEN NAS connected to a UGREEN UPS via USB, the system supports manual firmware updates for the UPS.

For detailed update instructions, please refer to [How to Manually Update the Firmware of UGREEN UPS?](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6NTA0MywidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo3MDQsImFydGljbGVWZXJzaW9uIjoiMS4wIn0=)
