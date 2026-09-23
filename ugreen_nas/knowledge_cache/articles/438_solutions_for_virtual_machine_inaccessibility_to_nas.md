# Solutions for Virtual Machine Inaccessibility to NAS

> **Article ID**: `438`  
> **Category**: `Application Guide > Virtual Machine > FAQ > Solutions for Virtual Machine Inaccessibility to NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/438  

---

## Problem Description

When using UGREEN NAS, the virtual machine cannot access the NAS. The virtual machine can ping all devices in the home network but cannot ping the NAS. Although the virtual machine can connect to the internet without issues, it cannot establish a connection with the NAS. The virtual machine's network settings are configured to use the vnet-bridge bridged adapter, but communication with the NAS is still unavailable.

## Solution

The issue may be caused by a mismatch between the virtual machine's network settings and the NAS's network bridge configuration. Although vnet-bridge is selected in the virtual machine instance, the virtual subnet mode in the NAS [Virtual Machine] application has not been adjusted to [Bridge Mode - LinuxBridge]. Below are the detailed steps to resolve the issue based on different scenarios:

### Scenario 1: Virtual Machine Instance Using MacVTap Mode

**Issue Description**

If your virtual machine instance (e.g., Windows) is using the virtual subnet [vnet-bridge0] with the network mode set to [Bridge Mode - MacVTap], the virtual machine cannot communicate with the NAS.

![](https://file-us.ugreennas.com/admin/article/2025-09-18/d9e285333a43465c983e409cb3a9d170.webp)

**Solution**

1. Go to the [Virtual Machine] on UGREEN NAS, and click "Manage" > "Network" to open the network management interface.

2. Locate the virtual subnet used by the virtual machine instance (e.g., vnet-bridge) and switch the network mode from [Bridge Mode - MacVTap] to [Bridge Mode - LinuxBridge].

3. If network bridging is not currently enabled on the NAS, you will see a "LAN ( Already Unbound)" prompt during the mode switch. In this case, click the "Modify Immediately"button to navigate to [Control Panel] > [Network].

![](https://file-us.ugreennas.com/admin/article/2025-09-18/49eccc01f1174ddb8a15231a42d09336.webp)

4. In the Network Connections page, click "Network Bridging" > "Virtual Bridging". Check the option "Enable Virtual Network Bridging" and select the LAN port to bridge (e.g., LAN1). After making your selection, click "Apply" to create the virtual bridge.

![](https://file-us.ugreennas.com/admin/article/2025-09-18/c1e9d28a8aee49928555d0cc811a9c75.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-18/a776091ecd8c469694dfed1517643ced.webp)

5. Once created successfully, you will see a virtual bridge network interface prefixed with "VBR" in the network connections.

![](https://file-us.ugreennas.com/admin/article/2025-09-18/142faaad4cee4d39b5dbab7744ab35a4.webp)

6. Return to the [Virtual Machine]. Confirm that the virtual machine network connection is now functioning. Click "**Done"** to complete the network mode switch. The virtual machine should now be able to communicate with the NAS.

![](https://file-us.ugreennas.com/admin/article/2025-09-18/283bad42f13d40da8245cb4d640b0bb3.webp)

### Scenario 2: Virtual Machine Instance Using LinuxBridge Mode but Experiencing Abnormal Status

**Issue Description**  
If your virtual machine instance (e.g., Windows) is using the virtual subnet [vnet-bridge0] with the mode set to [Bridge Mode - LinuxBridge], but the subnet status is indicated as red (abnormal), it suggests that the configuration of the virtual subnet or its network bridging with the NAS has issues.

![](https://file-us.ugreennas.com/admin/article/2025-09-18/b82ac1628d8f4c62aceb1d1666440fca.webp)

**Solution:**

1. Go to [Control Panel] > [Network] > [Network Connection].

2. On this page, click "Network Bridging" > "Virtual Bridging" and check "Enable Virtual Network Bridging".

3. Select the LAN port to be bridged (e.g., LAN1) and click "Apply" to create the virtual bridge.

![](https://file-us.ugreennas.com/admin/article/2025-09-18/8e17bcd18c4345c1a04cbb3c755a1547.webp)

4. After the creation, you will see a virtual bridge network interface prefixed with "VBR" in the Network Connection interface.

![](https://file-us.ugreennas.com/admin/article/2025-09-18/ade20ecfdd5148b882716a4308f9c1f7.webp)

5. Return to the [Virtual Machine] and reopen the network settings interface. You can confirm that the virtual subnet status has returned to normal. At this point, communication between the virtual machine and the NAS should be restored.

![](https://file-us.ugreennas.com/admin/article/2025-09-18/c3dfaba609654cdfbb58c7744952d32f.webp)

## Notes

● If your virtual machine instance is not set to [vnet-bridge] mode, shut down the virtual machine and manually configure the network to vnet-bridge mode to enable network communication between the virtual machine and the NAS host.

![](https://file-us.ugreennas.com/admin/article/2025-09-18/56c14fbeef4040b7ad8be3892aa8cece.webp)

● If the NAS is using network bridging mode (e.g., BR-LAN1 or VBR-LAN1), simply click the "Apply" button to complete the network mode switch.
