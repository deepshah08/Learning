# Solution for Virtual Machine Boot Failure Caused by Network Issues

> **Article ID**: `396`  
> **Category**: `Application Guide > Virtual Machine > FAQ > Solution for Virtual Machine Boot Failure Caused by Network Issues`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/396  

---

## Problem Description

When using a virtual machine with a bridged network configuration, if the corresponding NAS network undergoes changes (such as link aggregation or unbinding operations), it may cause the virtual machine using that bridged network to fail to start, and the following error message may appear:

![](https://file-us.ugreennas.com/admin/article/2025-09-16/ae71c7ec9fde4e3d9f6bd8b97d2ea2e4.webp)

## Solution

1. Go to the "Virtual Machine" application homepage, then click the [Manage] > [Network] option in the top-right corner.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/613a78e086fd4dcabc76fec71a628780.webp)

2. Locate the virtual subnet vnet-bridge that corresponds to the host network interface (LAN) currently in use. Change its mode to **Bridged Mode – LinuxBridge**.

> Before switching the network mode, make sure that the NAS's Virtual Network Bridging feature is enabled; otherwise, you won't be able to set it to LinuxBridge.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/3df507040be94b06ac73893c79c8845b.webp)

3. The system will prompt you to modify the NAS network settings. Click [Modify immediately], and it will redirect you to the [Control Panel] > [Network Connection] page.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/be1f958fbec940a8a9a29134c29b4247.webp)

4. Click [Network bridging] > [Virtual Bridging].

![](https://file-us.ugreennas.com/admin/article/2025-09-16/a41a228d8cf240bea5356207908f8c86.webp)

5. Check [Enable Virtual Network Bridging], select the physical network interface to bridge (e.g., LAN1), and click [Apply].

![](https://file-us.ugreennas.com/admin/article/2025-09-16/c61fb456d4cc4aaab429e2e7d318fc33.webp)

6. Click "Continue" to create the virtual bridge network adapter.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/e1651872656f44dfa200b098154503f6.webp)

7. Wait for the system to display the message "Operation Successful." The system will create a virtual network adapter starting with VBR and automatically hide the original physical interface (e.g., LAN1).

![](https://file-us.ugreennas.com/admin/article/2025-09-16/36d02fd1c2fa46f98c8ed552e2c40bf2.webp)

8. Return to [Virtual Machine] > [Manage] > [Network] page, and switch the network interface (e.g., vnet-bridge0) mode to Bridged Mode – LinuxBridge.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/786dcfa4b4bf45d1b4c5c55bdfa4f194.webp)

9. After successful configuration, virtual machines using this virtual bridge network adapter will obtain an IP address within the local network. The virtual machine can access internal network devices normally or access the external network via the router.

## Notes

● Adjusting NAS network settings may cause brief network interruptions. It is recommended to wait a few minutes. If the connection cannot be restored after a long time, please reset the network using the reset button. For detailed steps on resetting the network, refer to [Reset Network & Password](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjo4ODAsImFydGljbGVJbmZvSWQiOjI5NCwiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIiLCJwYXRoQ29kZSI6IiJ9)

● Ensure that the selected bridging network mode (macvtap or linuxbridge) is compatible with the virtual machine and NAS network configuration.
