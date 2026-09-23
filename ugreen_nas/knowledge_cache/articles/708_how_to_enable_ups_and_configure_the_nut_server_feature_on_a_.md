# How to Enable UPS and Configure the NUT Server Feature on a UGREEN NAS?

> **Article ID**: `708`  
> **Category**: `Application Guide > Control Panel > FAQ > How to Enable UPS and Configure the NUT Server Feature on a UGREEN NAS?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/708  

---

The content and image examples in this article are based on UGOS Pro system firmware version and Control Panel application version 1.6.1.2846. Due to possible interface or feature differences between firmware versions, please refer to your actual device display.

# NUT Server Overview

When multiple NAS devices use a **UPS (Uninterruptible Power Supply) system**, if one NAS is connected to the UPS via USB, it will serve as the **NUT Server (Network UPS Tools Server)**, responsible for receiving UPS information and forwarding it to other client NAS devices.

# Applicable Scenarios

When multiple devices (e.g., NAS, computers) require automatic shutdown during power outages to ensure safe shutdown and prevent data loss or hardware damage, UGREEN NAS supports UPS monitoring and automatic shutdown via **NUT****①** (Network UPS Tools).

**Configuration Details:**

1. **NUT Server (Master Device)****②**:Set NAS1 (directly connected to the UPS) as the NUT Server.

2. **NUT Client (Slave Device)③**:Configure other monitored **slave④** devices (e.g., NAS2, computers) as NUT clients.

During a power outage, the NUT Server notifies all clients to initiate a safe shutdown. This allows multiple devices to share one UPS for automatic shutdown

**Note**:NUT clients periodically poll the NUT Server for UPS status, typically detecting power loss within ~5 seconds to trigger shutdown.

Usage Examples:

● Home/small office environments where one UPS protects multiple NAS devices.

● During power loss, the NAS notifies other devices to save data and shut down automatically.

● Centralized UPS status display reduces costs by eliminating individual UPS connections per device.

**System Requirements**

● **Network:** All UGREEN NAS devices must be on the same LAN to forward UPS status.

● **Power Protection:** Network equipment (e.g., switches) connected to each NAS must plug into the same UPS. Otherwise, UPS status forwarding will fail during outages.

# Enable NUT Server

1. Log in to the UGREEN NAS connected to the UPS (via USB).

2. Navigate to [Control Panel] > [Hardware & Power] > [UPS], then enable "**NUT Server**".

![](https://file-us.ugreennas.com/admin/article/2025-06-27/8d3bbab297c948a2bd8f730f2711f3a5.webp)

3. Set the protection mode and wait time after power loss:

● **Protection Modes:**Choose "Auto Shutdown" or "Standby".

● **Wait Time****:**Set delay before shutdown (minutes/hours), with "Custom" or "Immediate" options.

4. Click "Apply**"** to save.

# Configure NUT Client Connection

1. Log in to another NAS (not USB-connected to UPS) on the same LAN.

2. Go to [Control Panel]> [Hardware & Power] > [UPS].

3. Under UPS Type, enable "Network UPS Slave".

![](https://file-us.ugreennas.com/admin/article/2025-06-27/ba48afabf2614706a7262e301dd1d1f5.webp)

4. Enter the NUT Server IP (e.g., NAS1’s IP: 172.17.70.69) and Port (default: 3493).

![](https://file-us.ugreennas.com/admin/article/2025-06-27/9b856cc94c254c5f8c680398f92d3290.webp)

5. Set the protection mode and wait time after power loss:

● **Protection Modes:**Choose "Auto Shutdown" or "Standby".

● **Wait Time****:**Set delay before shutdown (minutes/hours), with "Custom" or "Immediate" options.

6. Click "Apply**"** to save.

## Notes

● NAS1: Acts as the NUT Server (Master device)

● NAS2: Operates as the NUT Client (Slave device)

**Key points:**

1. **Independent Settings**: Master/slave configurations are separate but interdependent.

2. **Dependency Requirement**:Slave devices require the master's NUT Server to be actively running.

3. **Shutdown Sequence Logic**:After the master device executes an automatic shutdown operation, its NUT Server service will also terminate, and it will no longer be able to provide UPS status to clients. Therefore, ensure that slave devices shut down earlier or have a shorter wait time.

**Configuration Recommendations****:**

● If the master device is set to Auto Shutdown or Standby Mode, the slave devices should also be configured for Auto Shutdown.

● If both master and slave devices use **Auto Shutdown**, the master's wait time should be **longer** than the slaves' (recommended: slave wait time ≤ master wait time - 10 seconds). This ensures slaves autonomously trigger shutdown by polling the master's UPS status before the master powers off.

In summary.Keep the master's NUT Server operational,configure shutdown timers strategically to guarantee proper slave device shutdown sequencing.

# Verify UPS Status Transmission to Client Devices

● **Check UPS Status:** Navigate to [Hardware & Power]> [UPS] > [About] in UGREEN NAS settings to view current UPS status.

![](https://file-us.ugreennas.com/admin/article/2025-06-27/7d9e4990406742448a5bdf4649be238c.webp)

● **Test Shutdown Function**: Disconnect UPS mains power and observe if UGREEN NAS shuts down safely per configurations.

# Terminology

### NUT ①

An open-source tool for UPS monitoring and management, enabling multiple NAS devices to share UPS status over a network. It allows NAS devices to determine UPS status (e.g., battery level, power input) and execute pre-battery-depletion shutdowns for data safety.

**Note:**Not all UPS models support this feature. Verify NAS compatibility and driver availability before purchase.

### NUT Server (Master Device)②

The **NUT Server**(e.g., NAS1) directly connected to the UPS. Monitors UPS status (power level, grid status),executes shutdowns when required.

### NUT Client (Slave Device)③

**NUT Client** (e.g., NAS2) connected via network to the master. They Rely on forwarded UPS status from the masterAutonomously trigger actions based on polled status.

### Slave④

In the NUT (Network UPS Tools) architecture, **the slave function** refers to the role and operations of subordinate devices. These secondary devices are responsible for receiving UPS status updates from the primary/master device.

# **Related Link**

[How to Connect and Configure a UPS on UGREEN NAS to Ensure Data Safety During Power Outages?](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTMyOCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0NDIsImFydGljbGVWZXJzaW9uIjoiMS4wIn0=)
