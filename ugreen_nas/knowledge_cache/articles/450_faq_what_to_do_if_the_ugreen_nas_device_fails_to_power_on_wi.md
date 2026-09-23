# [FAQ] What to Do if the UGREEN NAS Device Fails to Power on within the Internal Network Environment?

> **Article ID**: `450`  
> **Category**: `Application Guide > Control Panel > FAQ > [FAQ] What to Do if the UGREEN NAS Device Fails to Power on within the Internal Network Environment?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/450  

---

## **Problem Description**

In a LAN environment, the UGREEN NAS device fails to start up via network wake-on-LAN (WOL). This issue may arise due to the wake-up initiator and NAS device not being on the same LAN segment, or the wake-up packet failing to be sent properly. For more details, please refer to the tutorial ["How to Power On UGREEN NAS within the Internal Network?"](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMzQ5LCJhcnRpY2xlSW5mb0lkIjo0NDksImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)

#### **Possible Causes**

1. **LAN Configuration Issues**: The wake-up initiator and NAS device may not be on the same LAN segment, preventing the wake-up packet from being sent correctly. For more details, please refer to the tutorial ["How to Confirm if Your Computer and NAS Are on the Same LAN."](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMTIxLCJhcnRpY2xlSW5mb0lkIjozODgsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)
2. **Interference from Network Devices:** Settings on switches and routers may intercept wake-up packets, and certain VLAN or firewall rules may block the passage of wake-up requests.
3. **Incorrect Settings on the Wake-Up Initiator:** The client on the wake-up initiator may fail to send wake-up packets due to firewall restrictions, permission settings, etc. For example, the Windows firewall may intercept wake-up requests, or iOS devices may not grant local network access permissions.
4. **Wireless Connection Limitations**: If the NAS device uses a wireless network connection (including built-in or external USB wireless adapters), it cannot be woken up via a wireless connection within the internal network.

## **Solutions**

1. **Check Network Configuration**:

   * Ensure that the wake-up initiator and NAS device are on the same LAN segment. If they are on different segments, adjust router settings or connect the devices to the same subnet.
2. **Troubleshoot Network Devices**:

   * Check whether switches and routers within the LAN have configured rules that block wake-up packets. Specifically, review VLAN settings and firewall rules to ensure that wake-up packets can be transmitted normally.
3. **Check Settings on the Wake-Up Initiator**:

   * On the wake-up initiator, ensure that the client software can send wake-up packets.
   * Disable the firewall on the wake-up initiator or set wake-up packet communication as an exception rule.
   * iOS devices need to grant local network permissions to the application, as failure to do so may block the sending of wake-up packets.
4. **Avoid Using Wireless Network for Wake-Up**:

   * Try to connect the NAS device using a wired network and avoid using wireless adapters for internal network wake-up, as wireless connections typically do not support WOL functionality.

#### **Advanced Troubleshooting**

* **Use Packet Capture Tools**: Use network packet capture tools such as Wireshark or tcpdump on the computer to analyze whether wake-up packets are sent properly and reach the UGREEN NAS device. If wake-up packets do not arrive, it may be due to issues with network devices or client settings.

#### If the problem persists, please contact UGREEN official technical support for assistance.
