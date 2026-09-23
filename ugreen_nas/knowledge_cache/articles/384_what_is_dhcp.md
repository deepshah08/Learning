# What is DHCP?

> **Article ID**: `384`  
> **Category**: `Application Guide > Control Panel > FAQ > What is DHCP?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/384  

---

### **What is DHCP?**

Dynamic Host Configuration Protocol (DHCP) is a network management protocol that automatically assigns IP addresses and other network configuration parameters, such as subnet mask, default gateway, and DNS servers. This allows network administrators to centrally manage devices, simplifying the configuration process and improving network management efficiency.

### **Advantages of DHCP**

* **Automated Management:** DHCP automatically allocates IP addresses, reducing manual configuration workload.
* **Configuration Accuracy:** Prevents errors caused by manual input and ensures devices receive correct network settings.
* **Conflict Reduction:** Assigns unique IP addresses to each device, avoiding IP address conflicts.
* **Flexible Changes:** Centralized management enables easy and quick adjustments across multiple network segments.

### **How DHCP Works**

1. **Discovery Phase (DHCP Discover):** When a client device starts up, it sends out a DHCP Discover broadcast packet to find available DHCP servers.
2. **Offer Phase (DHCP Offer):** Upon receiving the Discover request, the DHCP server responds with a DHCP Offer packet, providing an available IP address and related configuration information.
3. **Request Phase (DHCP Request):** The client selects one offer from the multiple DHCP servers (if any) and sends a DHCP Request packet to request the allocation of the offered IP address.
4. **Acknowledgment Phase (DHCP Acknowledgment):** After receiving the Request, the DHCP server sends a DHCP Acknowledgment packet, confirming the assignment of the IP address to the client.

### **Common Scenarios for DHCP**

1. **Home Networks:** Routers usually come with a built-in DHCP server that automatically assigns IP addresses to all connected devices.
2. **Enterprise Networks:** In large-scale networks, DHCP simplifies IP address management — especially in environments where devices frequently join or leave the network.
3. **Public Spaces:** In places like cafés and airports, DHCP is used to automatically assign IP addresses to devices connecting to public Wi-Fi.

### **Common Issues and Solutions**

* **IP Address Conflicts:** Check the DHCP server settings and make sure that there are no statically assigned IP addresses within the DHCP address pool.
* **Devices Cannot Obtain IP Addresses:** Verify the network connection and ensure that both the device and the DHCP server are on the same subnet.
* **Unstable Connections:** Check the DHCP lease time settings and make sure the lease duration is appropriate to prevent frequent renewals.
