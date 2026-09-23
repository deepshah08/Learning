# UGREEN NAS Feature Comparison: Sync & Backup, Snapshots, File Version Explorer, and RAID

> **Article ID**: `651`  
> **Category**: `Troubleshooting > System and Software Failure > UGREEN NAS Feature Comparison: Sync & Backup, Snapshots, File Version Explorer, and RAID`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/651  

---

UGREEN NAS offers a range of powerful data management features, including Sync & Backup, Snapshots, File Versioning, and RAID. Below is an introduction to these features and an explanation of their differences:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Feature** | **Sync** | **Backup** | **RAID** | **File Version Explorer** | **Snapshots** |
| **Definition** | Maintain data consistency across multiple storage locations in real‑time or on a schedule | Create data copies to protect against loss of the original data | Achieve data redundancy and performance optimization through disk arrays | Record historical changes to files and directories | Preserve a complete state of files and folders at a specific point in time |
| **Core Mechanism** | Bi‑directional or one‑way data mirroring | Mirroring, incremental, or multi‑version backup strategies | Striping with redundant parity (e.g., RAID 1 mirroring, RAID 5 parity) | Hash‑based change tracking | Incremental snapshots / Copy‑on‑write (CoW) technology |
| **Data Protection Capabilities** | Supports one-way real-time synchronization of local files to prevent accidental deletion | Protects original data from loss by storing backups on independent media | Guards against single disk failures (requires at least 2 disks) | Prevents accidental operations by allowing rollback to any previous version | 1. Instant rollback mechanism (recovery within minutes) 2. Supports up to 1024 historical snapshot points |
| **Use Cases** | Multi-device collaboration (e.g., file synchronization between NAS and PC) | 1. Backup important files from mobile phones and computers to NAS 2. Backup important NAS files to other NAS devices or servers | High-performance storage clusters | Ensures every change is traceable, eliminates version confusion, and improves file management and collaboration efficiency | 1. Take snapshots before critical data updates to create data anchors 2. Quickly build isolated test environment copies using snapshots 3. Provides millisecond-level data rollback to recover from ransomware attacks |
| **Storage Usage** | Low (only transfers data differences) | High (retains complete copies) | **Medium** (Varies with RAID level, affecting space utilization) | **High** (Retains all historical versions) | **Low** (Initially only stores metadata differences using copy‑on‑write technology, with storage usage growing linearly as files are modified or deleted) |
| **Dependencies** | Requires source and target storage to be available | Requires backup storage (local or cloud) | Requires multiple physical disks | Requires UGREEN NAS File Version Explorer app | Requires a storage system that supports snapshots (Btrfs) |

## **Comparison**:

### **Sync vs. Backup**

|  |  |  |
| --- | --- | --- |
| **Term** | **Description** | **Example** |
| Sync | Bi-directional or multi-directional data mirroring to ensure data consistency across nodes | Team collaboration editing files |
| Backup | One-way data copying that creates independent copies | Scheduled backups to other servers |

### **RAID vs** **Snapshots**

|  |  |  |
| --- | --- | --- |
| **Term** | **Description** | **Example** |
| RAID | Provides physical-layer protection through hardware redundancy, guarding against disk failures | RAID 1 mirroring configuration |
| Snapshots | Provides storage subsystem-level data protection through file system metadata tracking and copy-on-write technology, requiring no additional hardware | Capturing the state of a folder at a specific point in time |

### **File Version Explorer vs. Snapshots**

|  |  |  |
| --- | --- | --- |
| **Term** | **Description** | **Example** |
| File Version Explorer | Records a complete change history of files | Tracking the edit history of an important document |
| Snapshots | Preserves the data state at a specific point in time | Capturing the disk state of a folder at a certain moment |

### **Backup vs. Snapshots**

|  |  |  |
| --- | --- | --- |
| **Term** | **Description** | **Example** |
| Backup | A complete copy of the data, can be stored off‑site | Daily backups to an off‑site server |
| Snapshot | Depends on the original storage and cannot protect against physical media failures | Capturing the disk state of a folder at a specific point in time |
