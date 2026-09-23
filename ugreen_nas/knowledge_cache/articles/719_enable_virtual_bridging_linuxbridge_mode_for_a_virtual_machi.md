# Enable Virtual Bridging (LinuxBridge Mode) for a Virtual Machine

> **Article ID**: `719`  
> **Category**: `Application Guide > Virtual Machine > FAQ > Enable Virtual Bridging (LinuxBridge Mode) for a Virtual Machine`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/719  

---

The content and image examples in this article are based on UGOS Pro system firmware version 1.6.1.2846 and Virtual Machine version 1.5.0.0374. Due to possible differences in interface or features across versions, please refer to the actual display on your device.

To ensure that a virtual machine on the NAS can properly access the local network and external networks, it is recommended to enable and configure the Virtual Bridge (LinuxBridge) mode before creating the virtual machine. This mode allows the virtual machine to obtain an IP address in the same subnet as the NAS, making it possible for the virtual machine and NAS to communicate like physical devices.

## Steps

1. Go to the "Virtual Machine" app homepage and click [Manage] > [Network] in the top right corner.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/9e2b4e93ed64478ba1f4b14d973b0521.webp)

2. Locate the virtual subnet (vnet-bridge) associated with the host network interface (LAN) currently in use, and change its mode to Bridged Mode (LinuxBridge).

Before switching the network mode, you must first enable the NAS’s virtual network bridging feature; otherwise, you won’t be able to set it to LinuxBridge.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/7bd458f64dce4434add5b6f950e7e2e4.webp)

3. The system will prompt you to modify the NAS network settings. Click [Modify Immediately], and you will be redirected to [Control Panel] > [Network Connection].

![](https://file-us.ugreennas.com/admin/article/2025-07-01/b68607ac630048fa91165b3f830d85b4.webp)

4. Click [Network Bridge] > [Virtual Bridging].

![](https://file-us.ugreennas.com/admin/article/2025-07-01/c45f4b86c162415c89345168ffe145b1.webp)

5. Check [Enable Virtual Network Bridging], select the physical network interface to enable bridging (e.g., LAN2), and click [Apply].

![](https://file-us.ugreennas.com/admin/article/2025-07-01/dc0d59b7c14e4c7fa2c92dff97c44e2d.webp)

6. Click "Continue" to create the virtual bridging interface.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/9213aedcc1394914bcc7b551d0833c6b.webp)

7. Wait for the system to display the “Operation Successful” message. The system will create a virtual network interface starting with "VBR" and automatically hide the original physical interface (e.g., LAN2).

![](https://file-us.ugreennas.com/admin/article/2025-07-01/e1f79f22e4bf4478a81799999d638509.webp)

8. Return to [Virtual Machine] > [Manage] > [Network] page, and switch the network interface (e.g., vnet-bridge0) mode to Bridge Mode – LinuxBridge.

![](https://file-us.ugreennas.com/admin/article/2025-07-01/e99763282bab45979f311dd196681e23.webp)

9. After successful configuration, virtual machines using this virtual bridge interface will obtain an IP address within the local network. The virtual machines can access internal network devices normally and connect to external networks through the router.
