# What to Do If "No Device Found" Appears During Registration or Scanning?

> **Article ID**: `581`  
> **Category**: `Application Guide > Control Panel > FAQ > What to Do If "No Device Found" Appears During Registration or Scanning?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/581  

---

## Applicability

**Applicable Version**: NAS Firmware 1.18.0.0032 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

When registering a new device or scanning for devices on the local network using a client, you may see the message "**No device found**". This issue is usually related to the network connection, IP address, firewall settings, client version, or device status.

Follow the troubleshooting steps in this article to verify that the NAS is properly connected to the network and can be discovered by your current device.

![](https://file-us.ugreennas.com/admin/article/2026-08-13/06c26755be5d4173a0e3f0d944cb8f5c.webp)

## Check the Physical Connection

First, make sure the NAS is properly connected to the network. If the NAS is connected via an Ethernet cable, check the **LAN indicator**:

● **Flashing white**: Usually indicates that the network connection is working properly.

● **Flashing orange**: Usually indicates a network issue.

If the LAN indicator is abnormal, check the following devices and connections:

● NAS LAN port

● Ethernet cable

● Network switch (if applicable)

● Router

● The entire connection path between the router and the NAS

Try unplugging and reconnecting the Ethernet cable, or replace the cable or switch/router port, then scan for the device again.

## Check Whether the NAS Has Obtained an IP Address

Log in to your router's management interface and check the device list to confirm that the NAS is online and has obtained an IP address assigned by the router. Also check whether the router has any firewall rules or port restrictions, and make sure that your computer or phone is on the same local network as the NAS.

If the NAS does not appear in the router's device list, first check the Ethernet cable, router port, switch, and NAS LAN port connections.

## Test Whether the IP Address Can Be Pinged

If you can see the NAS IP address in the router, use the Ping command to test network connectivity.

Note: There must be a space between `ping` and the IP address.

### Windows Operation Method

1. Press `Win + R` to open the Run dialog, enter `cmd`, and press Enter to open Command Prompt.

2. Enter `ping NAS_IP`, for example, ping 192.168.1.100.

### macOS Operation Method

1. Open **Terminal**.

2. Enter `ping NAS_IP`, for example, ping 192.168.1.100.

### Interpret the Ping Test Results

If a result similar to the following is returned, the network used by your computer or phone can access the NAS normally:

```
Pinging 192.168.1.100 with 32 bytes of data:
Reply from 192.168.1.100: bytes=32 time<1ms TTL=64
Reply from 192.168.1.100: bytes=32 time<1ms TTL=64
Reply from 192.168.1.100: bytes=32 time<1ms TTL=64
Reply from 192.168.1.100: bytes=32 time<1ms TTL=64

Ping statistics for 192.168.1.100:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms
```

If a result indicating failure is returned, there may be a network connection issue. Continue checking the NAS network connection, router device list, Ethernet cable, switch, and firewall settings.

```
Pinging 192.168.1.100 with 32 bytes of data:
Request timed out.
Request timed out.
Request timed out.
Request timed out.

Ping statistics for 192.168.1.100:
    Packets: Sent = 4, Received = 0, Lost = 4 (100% loss),
```

## Check for IP Address Conflicts

If you can ping the NAS IP address but still cannot connect to the device, check whether there is an IP address conflict as follows:

1. Keep your computer continuously pinging the NAS IP address.

2. Unplug the Ethernet cable from the NAS.

3. Check whether the IP address can still be reached.

If the IP address can still be reached after unplugging the NAS Ethernet cable, the IP address may be in use by another device, indicating a possible IP conflict.

If the IP address can no longer be reached after unplugging the NAS Ethernet cable, the IP address is usually not being used by another device. Continue troubleshooting other possible causes.

If an IP conflict is confirmed, it is recommended to manually assign the NAS an IP address outside the router's DHCP automatic assignment range to prevent further conflicts.

## Restart Network Devices

Some temporary network issues can be resolved by restarting the devices. Restart the following devices in order:

1. Router

2. Switch

3. NAS

4. The computer or phone currently in use

After restarting all devices, open the UGREEN NAS client or app again and scan for the device.

## Check Whether the NAS Is Powered On Properly

If the NAS does not appear in the router's device list and the device indicators are abnormal, check whether the NAS is receiving power properly. Confirm the following:

● The power outlet is working properly.

● The power cable is securely connected.

● The power adapter is working properly.

● The NAS can power on normally.

● The device indicators match the expected operating status.

If the power indicator does not light up, check the power connections again. You can also try replacing the power adapter or power cable, then power on the NAS again.

If the NAS still cannot be powered on normally, contact UGREEN technical support or after-sales service for further assistance.

## Update the UGREEN NAS Client or App

Make sure that the UGREEN NAS client or app you are using is updated to the latest version.

● Mobile: Go to the app store on your phone or tablet and update the UGREEN NAS app to the latest version.

● PC: Go to the [UGREEN NAS Official Website](https://ai.ugreen.com/pages/downloads) to download the latest client.

After the update is complete, sign in again and scan for the device.

## Check Firewall Settings

If the NAS can be reached but the client still cannot discover or connect to the device, check the firewall settings on your computer or router.

● Check whether the firewall is blocking NAS discovery requests.

● Check whether security software is restricting the UGREEN NAS client from accessing the network.

● Check whether the router has access control, device isolation, or port restrictions enabled.

You can temporarily disable the firewall or security software and scan again. If the device can be discovered after disabling them, add the UGREEN NAS client to the allowlist.

## Reset the NAS Network Settings

If the network configuration is abnormal or you cannot confirm the current network status, you can use the RESET function to reset the NAS network settings. Resetting the network settings will not delete any personal data stored on the drives.

After the reset is complete, wait for the device to finish starting up, then scan for or register the device again.

Related document: [How to Reset the Network Settings and Administrator Password on Your UGREEN NAS](https://support.ugnas.com/knowledgecenter/detail/article/en-US/294?id=880&type=tag002&clientType=PC)

## What to Do If the Issue Persists?

If the issue persists after following the steps above, contact UGREEN technical support and provide the following information:

● NAS model

● System version

● Current client version

● Screenshot of the router's device list

● NAS indicator status

● Screenshot of the Ping test results

● Screenshot of the error page

● Current network connection method

Technical support contact information:

China: 0755-21044617 (Monday–Sunday, 08:00–24:00)

United States: +1 (888) 820-8830 (Monday–Friday, 09:00–17:00 PST)

Germany: +49 800 989 8988 (Monday–Friday, 09:00–17:00)

Japan: +81-800-170-8375 (Monday–Friday, 10:00–13:00 / 14:30–19:30 JST)

## Notes

● Make sure that your computer or phone and the NAS are on the same local network.

● If AP isolation, a guest network, or device isolation is enabled on the router, the NAS may not be discovered.

● If the NAS uses a static IP address, make sure that the IP address is not being used by another device.

● Page names and feature locations may vary slightly depending on the system version. Refer to the actual interface.
