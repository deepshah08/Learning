# How to Set the Outbound Traffic Speed for a Port?

> **Article ID**: `660`  
> **Category**: `Application Guide > Control Panel > FAQ > How to Set the Outbound Traffic Speed for a Port?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/660  

---

The traffic control feature of UGREEN NAS is designed to provide fine-grained management of outbound traffic for specific services or ports, helping to ensure network stability through bandwidth allocation strategies.

This feature allows administrators to set independent bandwidth thresholds for multiple services or specific ports, defining both a guaranteed minimum bandwidth and a maximum bandwidth limit. When network load is high, the system prioritizes the minimum bandwidth requirements of critical services while capping peak traffic for non-core services, preventing any single service from monopolizing bandwidth and degrading the performance of others.

## **What Is Outbound Traffic?**

"Outbound traffic" refers to the process of the UGREEN NAS sending data to external devices (such as computers, mobile devices, or another NAS). When you download files from the UGREEN NAS or copy files to your local computer, what is being limited is the upload speed of the NAS—that is, the outbound traffic.

## **Configure Traffic Rules**

1. Open the "Control Panel" application and go to [Network] > [Data Control].
2. Click the [Add] button to launch the rule configuration wizard.
3. Traffic control rules support three methods: all ports, built-in service list (select from predefined service ports such as SMB, NFS, etc.), and custom ports (manually enter the target port or port range, up to 14 ports separated by commas).
4. Select the network connection used by the port (such as "LAN1", "LAN2", etc.).
5. Configure bandwidth limits: the "Minimum Bandwidth" ensures that the service can use at least this amount of traffic when system bandwidth is sufficient; the "Maximum Bandwidth" limits the service’s peak traffic to prevent overuse.
6. After confirming that the settings are correct, click "OK" to save and apply.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250709/09b14738-9896-4e6d-b147-ae285b008f36.png)

**Note:** When multiple traffic control rules exist, you can drag to adjust their priority. The rule at the top of the list has the highest priority.
