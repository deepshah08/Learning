# [FAQ] Troubleshoot and Resolve Virtual Machine Network Failures

> **Article ID**: `395`  
> **Category**: `Application Guide > Virtual Machine > FAQ > [FAQ] Troubleshoot and Resolve Virtual Machine Network Failures`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/395  

---

## Problem Description

After switching network modes from the control panel (such as creating or deleting network bridges, link aggregation, restoring default network configurations, etc.), the virtual machine may experience no network access or fail to boot, with some networks in the virtual machine network management appearing in red with an invalid status and a red exclamation mark. As shown in the figure:

![](https://file-us.ugreennas.com/admin/article/2025-09-17/4ac3d8db0aa743c4a134756869d5a49c.webp)

## Troubleshooting

Please refer to the following correspondence between virtual machine network modes. Conflicts in the correspondence will cause the virtual machine network to become ineffective.

![](https://file-us.ugreennas.com/admin/article/2025-09-17/d466fe44c7304d3487cd21e206535b41.webp)

For example: When the NAS network mode is switched from normal to virtual bridge, the virtual machine corresponding to the normal mode's [Bridge Mode - MacVTap] (as shown in the figure, the Windows virtual machine) will not be able to connect to the network. In this case, you can switch the virtual machine's network mode from MacVTap to LinuxBridge here to resolve the issue.

![](https://file-us.ugreennas.com/admin/article/2025-09-17/06c7038ad6474f9da9239415119ef524.webp)

If there are issues with the virtual machine's network connection, you can follow these steps to resolve them:

1. Go to **[Virtual Machine] > [Manage] > [Network]** to enter the network management page.

2. Hover your mouse over the virtual subnet marked in red to view the specific solution提示 in the pop-up window.

3. Based on the information in the pop-up, you can further refer to the detailed steps below to ensure that the network settings meet the requirements.

## Solution

### To use the virtual bridge mode (vnet-bridge) for the virtual machine

1. **Switch network modes:**

If you need to change the virtual machine's network mode to "Bridge Mode - Linux Bridge," first switch the NAS's network mode to [Network Bridge]. In [Control Panel] > [Network], confirm whether the network cards used by the virtual subnet (such as LAN1, LAN2) have enabled network bridge mode (including normal bridge and virtual bridge). If enabled, click "Done" to switch modes.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250917/1824bfb5-645f-49e2-9692-ae0b30f2cb50.gif)

2. **Restart the virtual machine instance:**

After switching, you need to shut down and restart the virtual machine instance to make the changed network mode effective.

Note that restarting the virtual machine is ineffective; it must be completely powered off and then powered on again.

![](https://file-us.ugreennas.com/admin/article/2025-09-17/3d090b6098614cb38b7c5997e5f9d265.webp)

3. **Prompt for Bridging Mode Not Enabled**:

If the network cards (e.g., LAN1, LAN2) used by the virtual subnet do not have bridging mode enabled, switching to "Bridge Mode - Linux Bridge" will prompt you to switch the NAS network to [Network Bridging] mode.

![](https://file-us.ugreennas.com/admin/article/2025-09-17/b9e86ac8ccb947279b04d67ed7eeb8a8.webp)

4. **Confirm Network Mode Status**:

As shown in the figure, change the network mode to Network Bridging.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250917/9cab7748-03f0-4d31-aa18-9cf52fa0f461.gif)

In network settings, check the network mode status. In bridging mode, the virtual bridged network mode is displayed starting with "VBR" (while "BR" indicates a regular bridge).

![](https://file-us.ugreennas.com/admin/article/2025-09-17/6a5a23b2c7844382bd55482a55969ec9.webp)

### Enable Virtual Bridging vnet-nat Mode for Virtual Machines

As shown (iStoreOS2), the current VM's NAT mode displays an abnormal state, preventing the use of virtual subnets.

![](https://file-us.ugreennas.com/admin/article/2025-09-17/0dc07f4839694609a93fcee7e1277443.webp)

Since the default NAT mode cannot be edited, after changing the NAS network mode, if you need to continue using NAT mode for VM networking, follow these steps:

1. **Create a New NAT Mode Virtual Subnet**

● Click "Add Network" to open the Create Virtual Subnet dialog.

● Customize the network name, select [Mode] as NAT, and choose the created network bridging mode (e.g., VBR-prefixed virtual bridge or BR-prefixed regular bridge) for [Map Physical Network].

● By default, enable IPv4 automatic allocation. Optionally, disable auto-allocation and manually configure IP settings, with IPv6 support. After setting, click "Confirm" to create the virtual subnet.

![](https://file-us.ugreennas.com/admin/article/2025-09-17/bf193b4056884879b65c93e91c6ffab0.webp)

2. **Confirm Status**：After saving, return to [Network Management] to check the VM's virtual subnet status, ensuring the VM's network has recovered.

![](https://file-us.ugreennas.com/admin/article/2025-09-17/d0444748d9f540059884ceb1715efddf.webp)

3. **Change VM Network Settings**

● Go back to the VM interface and locate the VM using NAT mode (e.g., iStoreOS2 shown).

![](https://file-us.ugreennas.com/admin/article/2025-09-17/a2ee8ff49f14403b82b8f28d6fd9614e.webp)

● Click the "···" button in the VM column and select "Settings" to enter the VM's settings page.

● In [Basic], under "Network," change the network mode to the newly created NAT mode (e.g., from vnet-nat0 to NAT1). After modification, click "Apply" to save and activate.

![](https://file-us.ugreennas.com/admin/article/2025-09-17/5ad694f325194b2e95a61f5c1d410fbf.webp)

## Additional Notes

1. The default network of UGREEN NAS is regular mode, divided into LAN1 and LAN2, as shown.

![](https://file-us.ugreennas.com/admin/article/2025-09-17/2a82ba0063ef450fb2e61560544238b3.webp)

2. By default, the VM service generates virtual networks (e.g., LAN1, LAN2) for regular mode NAS networks based on the number of physical network cards. The default regular mode corresponds to [Bridge Mode - MacVTap]. To use [Bridge Mode - LinuxBridge], switch the NAS network to bridging mode.

![](https://file-us.ugreennas.com/admin/article/2025-09-17/6de520b2fe83404eb9dc3c9b222b755a.webp)
