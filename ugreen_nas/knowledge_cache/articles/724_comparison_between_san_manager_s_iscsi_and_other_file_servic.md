# Comparison Between SAN Manager's iSCSI and Other File Service Features

> **Article ID**: `724`  
> **Category**: `Application Guide > SAN Manager > FAQ > Comparison Between SAN Manager's iSCSI and Other File Service Features`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/724  

---

## **What is iSCSI?**

**iSCSI** is a block-level storage protocol based on **IP** networks. It allows users to virtualize a portion of NAS storage **as a remote hard disk (LUN)**, **which appears as a local physical drive on the client system.** This can help address local disk space limitations on computers.Clients can partition, format, and use the iSCSI disk just like a native hard drive.

**Key Features of iSCSI:**

● High Compatibility: Ideal for applications that require a "local disk" for data storage.

● No Shared Write Access: iSCSI does not support simultaneous write access from multiple clients (unless using a clustered file system), making it unsuitable for shared environments.

## **Comparison with Other File Services**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Protocol | Type | Main Use Case | Local Disk Mount Support | Multi-user Sharing | Transfer Performance |
| **iSCSI** | Block-level | Virtual hard drive, low latency | ✅ Yes (after formatting) | ❌ No (single-client access only) | High |
| **SMB/CIFS** | File-level | Network sharing with rich permissions | ❌ No (mapped as network drive) | ✅ Yes | Medium–High |
| **WebDAV** | File-level | Web-friendly, cross-platform sharing | ❌ No | ✅ Yes | Medium–Low |
| **NFS** | File-level | Efficient Linux/UNIX file sharing | ❌No | ✅ Yes | High |
| **FTP** | File transfer | Lightweight access with optional anonymity | ❌ No | ✅ Yes | Medium |
| **Rsync** | File sync | Incremental backup and efficient sync | ❌ No | ✅ Yes | High |

## **Recommended Use Cases**

|  |  |
| --- | --- |
| Requirement | Recommended Protocol |
| Mount as a local disk and format | iSCSI |
| File sharing across multiple users/devices | SMB |
| NAS to cloud or external server backup/sync | Rsync |
| Connect to third-party media server software | WebDAV |
| Data mounting on Linux servers | NFS |

## **Notes**

**iSCSI is not a file sharing protocol.**If multiple devices need to access the same data, SMB is strongly recommended instead.Simultaneous read/write access over iSCSI can corrupt the virtual disk and lead to data loss.
