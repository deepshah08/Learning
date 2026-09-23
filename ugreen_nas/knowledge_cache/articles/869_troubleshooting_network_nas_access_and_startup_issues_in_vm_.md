# Troubleshooting Network, NAS Access, and Startup Issues in VM Bridge Mode

> **Article ID**: `869`  
> **Category**: `Application Guide > Virtual Machine > Troubleshooting Network, NAS Access, and Startup Issues in VM Bridge Mode`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/869  

---

## Applicability

**Applicable client**: UGREEN NAS desktop client (Windows/macOS)

**Applicable version**: NAS firmware 1.16.0.0042 and later

This article is for reference only. The actual interface and operation paths may vary slightly due to system or app version updates. Please refer to the actual interface.

## Issue Description

When using a virtual machine, network configuration conflicts may cause the following issues:

The virtual machine cannot start, and the system displays the message: "**Network associated with the current virtual machine is invalid.** Please check in network management."

![](https://file-us.ugreennas.com/admin/article/2026-06-04/e3853d4dabf6450f923045899e7a2993.webp)

● In the VM network management panel, the virtual subnet is shown in red as invalid, with a red exclamation mark.

![](https://file-us.ugreennas.com/admin/article/2026-06-04/5a885e308d4448d5a2af3af7e97f47f5.webp)

● The VM itself has a normal network connection and can ping other devices on the local network and the Internet, but it cannot communicate with the UGREEN NAS host.

## Cause Analysis

The network interruption described above may occur for the following reasons:

● When the underlying network status of the NAS changes, such as after creating or deleting a network bridge, enabling link aggregation, or unbinding a network adapter, the existing VM network mapping path becomes invalid.

● The default NAS network in normal mode uses `Bridge Mode - MacVTap`. Due to its underlying architecture, this mode does not support direct communication between the VM and the host machine. To allow the VM to communicate with the NAS, set the NAS network connection to "**Virtual Bridge (VBR-LAN)**" and change the VM virtual subnet mode to `Bridge Mode- LinuxBridge`.

![](https://file-us.ugreennas.com/admin/article/2026-06-04/505470d5def048e0ad6b1f64427b7178.webp)

## Solution

Select the appropriate solution based on the current VM network mode.

### Solution 1: Repair the Bridge Network

Configure "**LinuxBridge**" bridge mode to resolve issues where the VM cannot start or cannot access the NAS host.

1. Open the "**Virtual Machine**" app, then click "**Manage**">"**Network**" in the top bar to open the network management page.

![](https://file-us.ugreennas.com/admin/article/2026-06-04/8f4216557b9b42db9f96c814524a8c2a.webp)

2. Find the virtual subnet currently used by the VM, such as `vnet-bridge1`, and change its mode to Bridge Mode-LinuxBridge.

![](https://file-us.ugreennas.com/admin/article/2026-06-04/4e1c4bb1fd71420e9b25c3177d2118fe.webp)

3. **Check whether a virtual bridge is configured:**

● If no virtual bridge has been configured on the NAS, the system will show "**Current NAS Network: LAN (Unbound)**". Click "**Modify immediately**" in the pop-up window. The system will then open the "**Network Connection**" page in "**Control Panel**".

![](https://file-us.ugreennas.com/admin/article/2026-06-04/64a5051d98794eb29031ff9a73bee0a7.webp)

● If a virtual bridge has already been configured on the NAS, click "**Done**" and skip to Step 7.

![](https://file-us.ugreennas.com/admin/article/2026-06-04/aec061948fe44d85b07b24c68d066b41.webp)

4. On the "**Network Connection**" page, click "**Network Bridging**">"**Virtual Bridging**".

![](https://file-us.ugreennas.com/admin/article/2026-06-04/b0fc700ff1104ee48fec6356f1ff414c.webp)

5. In the pop-up window, select "**Enable Virtual Network Bridging**" and choose the physical network adapter currently in use, such as "**LAN2**". Click "**Apply**", then click "**Continue**" in the confirmation window.

6. After the operation is complete, the original physical port, such as "**LAN2**", will be hidden, and a virtual bridge adapter starting with `VBR` will be created.

![](https://file-us.ugreennas.com/admin/article/2026-06-04/c80b96dc4d994e5fa70a92747df75cdd.webp)

7. Return to the "**Virtual Machine**" app. The switch mode status should now show a green check mark ✅, and the network should be recognized as virtual bridge mode. Click "**Done**".

![](https://file-us.ugreennas.com/admin/article/2026-06-04/f1294f61618e4f0aa7b1f85c66f1e116.webp)

8. In the VM management list, **fully shut down the VM**, **then start it again**. After the restart, communication between the VM and the NAS will be restored.

### Solution 2: Repair the NAT Network

If the VM was created with a NAT network, the default NAT mode assigned by the system cannot be edited again. When the NAT network becomes invalid due to NAS network changes, create a new network to replace it.

1. On the VM network management page, click **"Add network"** at the bottom.

![](https://file-us.ugreennas.com/admin/article/2026-06-04/75060fe39d8842979c6e181f0446fcd1.webp)

2. In the creation window, customize the network name, set "**Mode**" to "**NAT**", and select the created bridge adapter, such as "**VBR-LAN2**", under "**Map physical network**".

3. "**Auto assignment**" is enabled by default for "**IPV4**". If a fixed intranet IP is required, disable it and enter the settings manually. After configuration, click "**Confirm**" to create the subnet.

![](https://file-us.ugreennas.com/admin/article/2026-06-04/84cfcbfc0b2848d5a86f35bbd1b636b5.webp)

4. Return to the "**Virtual Machine**" home page. In the list, find the VM with the network issue, then click "**…**">"**Settings**" on the right.

5. On the **"Basic Configuration"** tab, find "**Network**", replace the old network in the drop-down menu with the newly created NAT subnet, such as "**NAT3**", then click "**Apply**" to save. The VM network connection should then be restored.

## Notes

● Before applying any of the fixes above, check the **"Network"** option in **"Settings"** for the target VM and make sure a vnet-bridge interface has been assigned to it. If not, shut down the VM first, then adjust the network setting manually.

● Changing the network bridge configuration on the NAS host may briefly interrupt network communication for the entire device. Wait a few minutes for the connection to recover. If the network still cannot be reached after a long time, use a pin to press and hold the **Reset** button on the device for about 5 seconds. Release the button immediately after hearing one short beep from the device, then wait for the network connection to recover.
