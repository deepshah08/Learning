# [FAQ] How to Enable Network Wake and Wake on LAN (WOL) in UGREEN NAS?

> **Article ID**: `449`  
> **Category**: `Application Guide > Control Panel > FAQ > [FAQ] How to Enable Network Wake and Wake on LAN (WOL) in UGREEN NAS?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/449  

---

In the UGOS Pro system of your UGREEN NAS, you can achieve remote booting through the Wake-on-LAN (WOL) feature. Here are the specific steps to enable this feature:

## Enable Network Wake Feature

1. Open the [Control Panel].

2. Click on "Hardware & Power" > "Power".

3. In the "Boot and shutdown settings" check the boxes for "Auto boot after loss of power" and "Enable wake on LAN (WOL)".

4. Click "Apply" to make the settings effective.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/95288221ca614749b23dc9ad95a518fa.webp)

## Auto Power-on in LAN

When your UGREEN NAS has "Auto boot after loss of power" enabled, you can use a smart plug (e.g., Xiaomi Smart Plug) to control the power supply of your UGREEN NAS, thus achieving automatic booting. For detailed usage of the smart plug, please refer to the manufacturer's instructions.

## Use Wake on LAN (WOL)

Both the PC client and mobile client of UGREEN NAS support WOL network wake-up features. Here are the specific steps:

**Wake up UGREEN NAS from PC:**

1. Open the "UGREEN NAS" client.

2. On the login page, click "More Connections" to access the submenu.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/c186ff4ac2e9474ea9416a88906e3c7f.webp)

3. Find and click the "WOL" button.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/97058d942cee4330a056cc13ffefbc5e.webp)

4. Click "WOL through the MAC address", then enter the MAC address of your UGREEN NAS and tap the "Wake up the device" button; the system will send a request to attempt to wake up the NAS.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/eb383862445a474a8c4e36dd9276209d.webp)

5. If the wake-up is successful, you will see the online UGREEN NAS device in the local network device list. The MAC address of the device can be viewed in the search results of the local network devices.

**Wake up NAS from Mobile:**

1. Open the "UGREEN NAS" mobile client.

2. On the login page, tap the "Drop-down Button" to access the submenu and select the logged-in NAS device.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/71fceb19274548bf96b1daa7c4eb58ba.webp)

3. Tap the "Network Wake Up" button.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/38ae4c66fd6049dabf3c2017d7f1b2ff.webp)

4. If the device is already logged in, you can directly select the device and tap the "Wake-up" button to initiate the wake-up operation.

![](https://file-us.ugreennas.com/admin/article/2025-09-02/f7a5cf09de754d89943be00e6305a740.webp)

5. If you need to wake up via MAC address, click "WOL through the MAC address," enter the NAS's MAC address, and then tap the "Wake up the device" button. The system will send a request to attempt to wake up the NAS.

6. After a successful wake-up, you can view the online UGREEN NAS device in the local network devices.

### Additional: Achieving WOL Network Wake-up with Other Devices and Software

In addition to the PC and mobile clients of UGREEN NAS, you can also use routers or third-party software that support WOL wake-up features to remotely wake up your NAS. Here are several common methods:

#### Wake up through routers with WOL capability

Some routers support the WOL feature, which can help you remotely wake up your NAS. Common router brands that support WOL wake-up include:

● **Huawei routers (require plugin installation from the app market)**

● **Asus routers**

● **iKuai software routers**

Simply log in to the router's management page, find the Wake-on-LAN (WOL) feature, enter the MAC address of the NAS, and you can remotely send a WOL wake-up request. For specific operation steps, please refer to the user manual of the router.

#### Wake up through third-party software

You can also use third-party software to wake up your NAS in the local network or remote network. Common WOL wake-up software includes:

● **wake on lan**: A simple and easy-to-use WOL wake-up tool.

When using these software, you just need to enter the MAC address of the NAS and send a wake-up request to attempt to remotely wake up the device.

#### Remote network wake-up

To achieve remote network wake-up, in addition to using the local network, you also need the following conditions:

● **Public IP:** Your network needs to have a fixed public IP, or you can access your local network devices through Dynamic Domain Name System (DDNS).

● **Remote access tools:** You can also use software that can access local network devices to remotely operate the NAS, such as remote desktop tools.

These methods can help you achieve remote wake-up without relying on the client, further enhancing the flexibility of network management.

## Related Link

[【FAQ】What to do if your UGREEN NAS device cannot boot in the local network environment?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMzUyLCJhcnRpY2xlSW5mb0lkIjo0NTAsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)
