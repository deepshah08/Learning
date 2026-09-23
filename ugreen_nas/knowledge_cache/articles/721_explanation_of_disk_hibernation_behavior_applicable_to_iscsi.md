# Explanation of Disk Hibernation Behavior (Applicable to iSCSI Services)

> **Article ID**: `721`  
> **Category**: `Application Guide > SAN Manager > FAQ > Explanation of Disk Hibernation Behavior (Applicable to iSCSI Services)`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/721  

---

When using the iSCSI service, you may notice that even if the client does not perform any actual read/write operations, the disks on the NAS used to create the LUN **do not enter hibernation**. This is not a system error, but a **behavior inherent to the iSCSI protocol** (not limited to UGREEN NAS).

### Why Doesn't the Disk Hibernate After iSCSI Connection?

iSCSI is a **block-level storage protocol with persistent connections**, and its working mechanism leads to the following behaviors:

● **Persistent sessions**: Once a client (Initiator) connects to the NAS's iSCSI Target, the system maintains a persistent session—even if the client is idle, the connection remains active.

● **Persistent sessions**: Once a client (Initiator) connects to the NAS's iSCSI Target, the system maintains a persistent session—even if the client is idle, the connection remains active.

● **No awareness of access intent**: iSCSI lacks the intelligence to determine whether access is truly needed at any moment, so it cannot safely spin down disks for hibernation.

● **System-level design for data integrity**: Random read/write operations on a hibernating disk may lead to response delays or I/O errors. Therefore, the system **by default prevents disks associated with iSCSI LUNs from hibernating**.

### Notes

● If you want to allow the disk to enter hibernation for energy saving, pause or disconnect the iSCSI connection from the client.

● If energy saving is not a priority, it is recommended to disable sleep settings on the client device to ensure stable access.
