# Why is inbound traffic shaping not taking effect?

> **Article ID**: `658`  
> **Category**: `Troubleshooting > Network Failure > Why is inbound traffic shaping not taking effect?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/658  

---

In the network traffic control feature of UGREEN NAS, traffic limits currently apply only to outbound traffic for all protocols.

"Outbound traffic" refers to data sent from the UGREEN NAS to external devices (such as computers, mobile devices, or another NAS). Therefore, when you download files from the NAS or copy files to a local computer, the traffic control restricts the NAS’s upload speed (i.e., outbound).

"Inbound traffic" means data sent from external devices to the NAS (for example, uploading files to the NAS). Currently, inbound traffic is not subject to traffic control policies, so limiting upload speed to the NAS is not supported.

### **Example:**

* ✅ **Restricted scenario:** Downloading files from NAS to a computer over LAN is limited by the set outbound speed limit.
* ❌ **Unrestricted scenario:** Uploading files from a computer to NAS is not affected by any speed limits.

## **How to handle uncontrolled inbound traffic？**

Although the system does not support limiting inbound traffic at present, you can consider the following alternatives to manage bandwidth:

1. **Use router-based QoS (Quality of Service) management:** On some high-performance routers, you can set upload and download speed limits at the device or port level. By applying a QoS policy to the NAS device, you can indirectly control inbound traffic.
2. **Use port rate limiting on a switch (if available):** Some managed switches offer port-level bandwidth control, allowing you to directly set a bandwidth cap on the port connected to the NAS to manage both inbound and outbound traffic.
3. **Limit the number or timing of upload tasks:** In scenarios involving frequent uploads of large files to the NAS (such as sync or backup), you can use scheduling or time-restricted execution to avoid consuming too much bandwidth during peak hours.
