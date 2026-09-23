# What is Network Bridging?

> **Article ID**: `387`  
> **Category**: `Application Guide > Control Panel > FAQ > What is Network Bridging?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/387  

---

In network configuration, network bridging is a key feature. UGREEN NAS provides two modes: normal bridging and virtual bridging.

* **Normal Bridging** combines multiple physical network interfaces into a single logical network, allowing external devices (such as routers) to connect to a computer via the UGREEN NAS. For example, if the router only has one available Ethernet port and both the NAS and computer need to connect to the internet, you can connect the computer to the UGREEN NAS with an Ethernet cable, and then connect another Ethernet cable from the NAS's other port to the router. This way, the computer can access the internet while maintaining high-speed data transfer with the NAS, improving overall network resource utilization.
* **Virtual Bridging** allows virtual machines to bridge with physical network interfaces, enabling them to access the network directly, just like the NAS. In virtual bridging mode, the virtual machine can share the same network interface as the local NAS and other network devices, allowing the virtual machine to communicate with the outside world.

These bridging modes provide users with versatile network management options, catering to different application needs and ensuring efficient and stable network connections.

### **Common Network Bridging Scenarios**

**Normal Bridging:**

* **Network Integration:** Use the two network interfaces of the UGREEN NAS, connecting one to the router and the other to the computer. Through the bridging configuration in UGOS Pro, these two network interfaces form a virtual bridging network, enabling seamless communication between devices.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250418/6ca19bc6-69c7-4034-a56d-a939d337d9df.png)

* **Temporary Network Expansion:** When there is a need to temporarily extend the network to devices that are difficult to directly connect to the router, the NAS's network bridging function provides a solution.
* **High-Performance Demands:** In scenarios such as video editing, data backup, and other tasks requiring high bandwidth and low latency, normal bridging ensures fast data transfer.

**Virtual Bridging：**

* **Multiple Device Access:** Through virtual bridging, multiple virtual machines can communicate directly with the physical network, just like real devices connecting to the network. This is ideal for complex network environments.
* **Multiple Network Interface Management:** Suitable for situations where different virtual machines need access to different networks. Through virtual bridging, the NAS can ensure security while enabling isolation and management of internal and external networks. For example, when the NAS needs to connect to both an internal and an external network, virtual bridging can connect specific virtual machines to the external network while keeping other devices connected to the internal network.

### **Configuration Steps for Normal Bridging**

**1.Enable Normal Bridging:**

* Connect one physical network interface of the UGREEN NAS to the router and the other to the computer.

* Log in to the UGOS Pro management interface, navigate to [Control Panel] > [Network] > [Network Connection] > [Network Bridging], and click on "Normal Bridging" to enter the setup wizard.
* In the wizard, check "Enable Normal Bridging," select the two network interfaces to be bridged (e.g., LAN1 and LAN2), and add them to the bridge interface.
* Click "Apply" and wait for the system to prompt "Operation Successful." After successful creation, the original network interfaces will disappear, and the system will automatically generate a virtual network card starting with "BR."

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250418/4710dfcf-1396-428e-80b8-31891c2fb2f3.png)

**2.Configure the IP Address for the Bridged Network Card (Optional)：**

* By default, the system automatically obtains the IP address via DHCP. You can manually configure the settings, including IP address, subnet mask, default gateway, and DNS.

* After completing the configuration, click "Apply" to save the settings.

**3.Configure Computer Network:**

* Set the computer's network interface to obtain an IP address via DHCP, or manually configure a static IP address within the same subnet as the NAS.

* After connecting the computer to the network interface of the UGREEN NAS, double-check that the computer's network interface is set to obtain an IP address via DHCP, or manually set a static IP. To learn how to set up DHCP on your computer, please click on ["How to Set Up DHCP on a Computer."](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjoxMTE5LCJhcnRpY2xlSW5mb0lkIjozODYsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIn0%3D)
* Check if the computer successfully obtains an IP address, and verify the internet connection through the UGREEN NAS.

### **Virtual Bridging Configuration Steps**

* **Enter Virtual Bridging Settings:** Go to [Control Panel] > [Network] > [Network Connection] > [Network Bridge], then click "Virtual Bridge" to open the creation popup.
* **Enable Virtual Bridging:** In the creation wizard, check "Enable Virtual Bridge" and select the network interface to use (e.g., LAN1 or LAN2).
* **Apply Settings:** Click "Apply" to create the virtual bridge, and wait for the system to confirm the creation is successful.
* **Check the Result:** Once successful, the original network interface will be hidden, and the system will automatically generate a virtual network card starting with "VBR."

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250418/10da3fb6-f7bc-4f8b-b6ca-f717fa1a5748.png)

### **Steps to Delete Network Bridge:**

1. **Select the Bridged Network Interface:** In the [Network Connection] page, select the bridged network interface you want to delete.
2. **Click "Unbind":** Find the "Unbind" button and click it.
3. **Confirm the Operation:** Carefully read the prompt in the popup, ensuring you understand the impact of the unbinding operation. After confirming, click "OK."
4. **Wait for Completion:** The unbinding process will take some time as the system loads. Wait until the prompt shows "Operation Successful." At this point, the bridged network interface has been successfully unbound.

### Notes

1. **Compatibility of DXP480T Series and DXP2800 Series:** Please note that the DXP480T series and DXP2800 series devices do not support normal bridging functionality. If your network requirements require normal bridging, please choose a device model that supports this feature.
2. **Wait for Operation to Take Effect:** After creating or unbinding a network bridge, the system may take some time to complete the operation. Please be patient until the page displays "Operation Successful." Once the operation is successful, you will be able to view the latest status of the network interfaces (e.g., the status of LAN1 and LAN2 after creating a bridge or the restored default settings after unbinding the bridge). During this process, please avoid making other network settings to ensure the operation completes smoothly.
3. **Performance Impact:** Network bridging may increase network latency and load, especially when handling large amounts of traffic.
4. **Network Conflict:** If the bridged interface has a manually set IP address, please ensure that the IP address and network configuration of the bridged interface do not conflict with the existing network to avoid network conflicts and communication interruptions.
