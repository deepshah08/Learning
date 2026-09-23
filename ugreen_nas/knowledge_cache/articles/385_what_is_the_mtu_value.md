# What is the MTU value?

> **Article ID**: `385`  
> **Category**: `Application Guide > Control Panel > FAQ > What is the MTU value?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/385  

---

### **What is the MTU Value?**

The Maximum Transmission Unit (MTU) refers to the largest packet size, in bytes, that a network device can handle in a single transmission. Setting the correct MTU value can optimize network performance by reducing fragmentation and transmission delay.

### **Importance of the MTU Value**

1. **Performance Optimization:** The correct MTU value reduces packet fragmentation and improves transmission efficiency.
2. **Transmission Efficiency:** A larger MTU allows more data to be sent in one transmission, reducing overhead.
3. **Network Stability:** An inappropriate MTU value may cause packet loss or increased network latency.

## **How to Determine the Optimal MTU Value**

1. **Ping Test Method:**

   * Open Command Prompt or Terminal.
   * Use the following command to test different MTU values (decreasing by 28 bytes each time).
   * Find the largest MTU value that does not cause fragmentation.
2. **Consult Your ISP:** Some Internet Service Providers (ISPs) may recommend the optimal MTU value.

### **Detailed Step-by-Step Example**

#### **Detailed Steps for the Ping Test Method**

1. **Open the Command Prompt:**

   * On Windows: Press`Win + R`, type`cmd`, and press Enter.
   * On macOS or Linux: Open the Terminal application.
2. **Run the Ping Command:**

   * Enter the following command to test the MTU value:

```
ping www.example.com -f -l 1472
```

* If a fragmentation warning appears, reduce the packet size by 28 bytes and test again:

```
ping www.example.com -f -l 1444
```

### **Setting the MTU Value on UGOS Pro**

1. **Access Network Settings:**

   * In the UGOS Pro control panel management interface, go to the "Network Settings" page.
   * Click on the "Network Connection" option, select the network interface (e.g., LAN1, LAN2) for which you want to modify the MTU, then click "Edit."
2. **Modify the MTU Value:**

   * In the network interface (LAN) edit page, scroll down to find "Manual MTU Setting."
   * Check "Enable," then enter the desired MTU value. The default MTU value is 1500.
   * Click "Apply" to save the settings.

### **Common Issues and Solutions**

* **Network Instability:** Lower the MTU value to avoid fragmentation caused by oversized packets.
* **Unable to Access Specific Websites:** Adjust the MTU value to ensure packets are transmitted correctly.
