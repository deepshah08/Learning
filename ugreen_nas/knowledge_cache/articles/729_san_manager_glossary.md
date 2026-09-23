# SAN Manager Glossary

> **Article ID**: `729`  
> **Category**: `Application Guide > SAN Manager > FAQ > SAN Manager Glossary`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/729  

---

In the SAN Manager application, you may come across some technical terms. Below are explanations of common terminology to help you better understand the concepts and features related to SAN Manager:

### LUN (Logical Unit)

A LUN is like a "virtual hard disk" — you can assign a specific size, select a storage space, enable write protection, and configure other settings for each LUN. Once a LUN is mapped to a client (such as Windows or macOS), it behaves like a local hard disk, allowing the client to mount it and read or write data.

### Target (Target Device)

A Target is an "access point" exposed by the NAS via the iSCSI protocol. Clients use the Target address to access the associated LUN. The Target supports security controls such as **CHAP authentication** (④).

### Group (Client Group)

In **SAN Manager**, a **Group** is a logical collection used to manage access permissions for multiple clients. Through a Group, administrators can organize multiple clients (IQNs) and grant them bulk access to a specific LUN.

### Thick LUN (Thick-Provisioned Logical Unit)

A Thick LUN is a storage method where **space is preallocated**.When creating the LUN, the system immediately reserves the specified physical capacity from the storage pool — even if that capacity is not yet used for actual data, it will still be occupied.

**Use Case:** Environments that require higher performance or precise capacity control.

### Thin LUN (Thin-Provisioned Logical Unit Number)

A Thick LUN is a storage method where **space is preallocated**.When a Thin LUN is created, only the logical capacity is defined—no physical space is immediately consumed. The system dynamically allocates physical storage as data is written.

**Use Case:** Ideal when multiple LUNs share the same physical storage pool, allowing for flexible space management and improved utilization.

### IQN（iSCSI Qualified Name）

The IQN is a globally unique identifier used in the iSCSI protocol to distinguish between Target (server) and Initiator (client) devices. The format is as follows:

```
iqn.<year-month>.<reversed-domain>[:custom-identifier]
Example:iqn.2025-03.com.ugreen:target-6.f245963e46
```

Think of the IQN as a device "ID card"—it's essential for establishing a valid iSCSI connection.

### CHAP Authentication （Challenge Handshake Authentication Protocol）

CHAP is one of the authentication methods used in iSCSI to ensure that only authorized clients can access a Target. When a client attempts to connect, the Target sends a challenge value. The client must respond correctly using a preset username and password to verify its identity.

**CHAP provides one-way authentication (server authenticates the client).**

**Recommendation:** Enable CHAP in your iSCSI setup to improve security and prevent unauthorized access.

### Mutual CHAP

Mutual CHAP is an enhanced version of CHAP that supports **two-way authentication**:

● The Target authenticates the Initiator (client device), and

● The Initiator also authenticates the Target (server).  
This helps ensure both sides of the connection are trusted.

### Initiator

An Initiator is a device that connects to and uses an iSCSI virtual disk via the iSCSI protocol. Common client devices include PCs, servers, or virtual machines. These devices must install or enable an **iSCSI Initiator program** to connect to the NAS.

|  |  |
| --- | --- |
| Operating System | Description |
| **Windows** | Built-in iSCSI Initiator; no extra software needed |
| **macOS** | Requires third-party software (e.g., DAEMON Tools) |
| **Linux** | Typically configured using tools like open-iscsi |

> The UGREEN NAS acts as the iSCSI Target (server), responsible for creating and managing logical disks. Client devices (Initiators) connect to the Target to access storage.
