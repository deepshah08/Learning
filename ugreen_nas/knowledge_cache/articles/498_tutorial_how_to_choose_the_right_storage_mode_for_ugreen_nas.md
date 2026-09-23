# [Tutorial] How to Choose the Right Storage Mode for UGREEN NAS?

> **Article ID**: `498`  
> **Category**: `Application Guide > Storage > FAQ > [Tutorial] How to Choose the Right Storage Mode for UGREEN NAS?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/498  

---

UGREEN NAS offers various storage modes, each with distinct characteristics in terms of performance, storage capacity, and reliability. This article provides an overview of these storage modes, including their basic requirements, advantages, disadvantages, and selection recommendations.

## **Supported Storage Modes**

The table below summarizes the storage modes supported by UGREEN NAS, detailing the storage capacity of each mode, the minimum number of hard disks required, the number of drive failures allowed before data loss, and the applicable DXP series models.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Storage Mode** | **Number of hard disks** | **hard disk Fault Tolerance** | **Description** | **Available Capacity of Storage Pool** | **Supported DXP Series Models** |
| Basic | 1 | 0 | * Each disk is independent, no redundancy.  * Data loss if the disk fails, not recoverable. | 1 x hard disk capacity | DXP2800  DXP4800  DXP4800 Plus  DXP6800 Plus  DXP6800 Pro  DXP8800  DXP8800 Plus  DXP8800 Pro  DXP480T Plus |
| JBOD | ≧1 | 0 | * Combines disks into one storage space.  * No redundancy; data on the failed disk is lost. If the first disk (with partition table) fails, the entire pool becomes inaccessible. | Total capacity of all disks. | DXP2800  DXP4800  DXP4800 Plus  DXP6800 Plus  DXP6800 Pro  DXP8800  DXP8800 Plus  DXP8800 Pro  DXP480T Plus |
| RAID 0 | ≧2 | 0 | * Stripes data across disks, boosting performance by n times (n = number of disks).  * No redundancy; any disk failure results in total data loss. | Total capacity of all disks | DXP2800  DXP4800  DXP4800 Plus  DXP6800 Plus  DXP6800 Pro  DXP8800  DXP8800 Plus  DXP8800 Pro  DXP480T Plus |
| RAID 1 | 2 | 1 | * Mirrors data on each disk for redundancy.  * Can recover by replacing the failed disk. | Smallest disk capacity | DXP2800  DXP4800  DXP4800 Plus  DXP6800 Plus  DXP6800 Pro  DXP8800  DXP8800 Plus  DXP8800 Pro  DXP480T Plus |
| RAID 5 | ≧3 | 1 | * Stripes data with parity for single-disk fault tolerance.  * Can recover by replacing the failed disk. | (Number of disks - 1) x smallest disk capacity | DXP4800  DXP4800 Plus  DXP6800 Plus  DXP6800 Pro  DXP8800  DXP8800 Plus  DXP8800 Pro  DXP480T Plus |
| RAID 6 | ≧4 | 2 | * Adds extra parity for two-disk fault tolerance.  * Can recover by replacing up to two failed disks. | (Number of disks - 2) x smallest disk capacity | DXP4800  DXP4800 Plus  DXP6800 Plus  DXP6800 Pro  DXP8800  DXP8800 Plus  DXP8800 Pro  DXP480T Plus |
| RAID 10 | ≥4 (must be an even number) | Half the total capacity of all hard disks | * Combines RAID 0 performance with RAID 1 redundancy.  * Can recover if one disk per pair fails. | (Number of disks / 2) x smallest disk capacity. | DXP4800  DXP4800 Plus  DXP6800 Plus  DXP6800 Pro  DXP8800  DXP8800 Plus  DXP8800 Pro  DXP480T Plus |

#### **Notes:**

1. **Compatibility of Storage Modes**: Only "Basic" and "JBOD" modes are universally supported. Other RAID types are available only on specific UGREEN NAS models, depending on the number of drive bays and installed hard disks.
2. **Requirements for JBOD Mode**: JBOD requires a minimum of one hard disk. If any drive fails in this mode, the data on that specific drive will be lost. If the first drive (which typically contains the partition table) fails, the entire storage pool will become inaccessible as the system cannot recognize data on other drives without the partition table.
3. **Storage Capacity Expansion Options**: Different RAID modes provide varying methods for storage expansion. RAID 5 and RAID 10 allow capacity increases by adding new drives or replacing existing drives with larger-capacity ones. RAID 0 does not support any form of capacity expansion.
4. **Fault Tolerance Limitations**: If the number of failed drives exceeds the fault tolerance of the selected RAID mode, all data in the storage pool will be lost and cannot be recovered.
5. **Recommended RAID Mode for Beginners**: RAID 5 is the preferred choice for beginners due to its balance of performance, storage capacity, and data redundancy. Users may also select a RAID mode based on specific needs.
6. **Hard Disk Replacement Requirements**: In RAID 1/5/6/10 modes, replacement drives must have a capacity equal to or greater than the smallest hard disk currently in use.

---

## **Storage Mode Comparison**

Different storage modes are suited to various scenarios and requirements. When selecting an appropriate storage mode, it is essential to consider the features, recommended use cases, and advantages and disadvantages of each type. Below is a detailed description of common storage modes, along with their recommended scenarios and pros and cons:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Storage Mode** | **Description** | **Recommended Use Cases** | **Advantages** | **Disadvantages** |
| **Basic** | Single hard disk as an independent unit without redundancy. | Temporary data or data already backed up on other devices. | Low cost, simple setup, full drive capacity usage.. | No data redundancy; drive failure leads to data loss. |
| **JBOD** | Combines drives into a single storage pool with no redundancy. | Large storage needs with low redundancy and performance requirements, e.g., multimedia storage. | Supports mixed drive capacities, high storage utilization. | Drive failure causes data loss on the affected disk; first drive failure may render the pool inaccessible. |
| **RAID 0** | Stripes data across drives for high performance, no redundancy. | High read/write performance for temporary data or cache storage. | Fast speeds, low cost. | Any drive failure results in total data loss. |
| **RAID 1** | Mirrors data for redundancy; data recoverable if one drive fails. | Ideal for scenarios requiring high data redundancy, such as critical data backup or small file servers. | High data redundancy, good read performance. | 50% capacity usage, requires double the drive capacity, slower write speeds. |
| **RAID 5** | Stripes data and parity for redundancy; rebuilds data if one drive fails. | Business file servers, virtualized storage. | Balances performance, redundancy, and efficiency. | Rebuild impacts performance; requires at least three drives. |
| **RAID 6** | Adds dual parity for higher redundancy; tolerates two drive failures. | Ideal for high-redundancy scenarios, such as enterprise data centers and critical business systems. | Higher redundancy, data recoverable even after two drive failures. | Higher cost, slower writes due to computational overhead. |
| **RAID 10** | Combines RAID 1 redundancy with RAID 0 performance. | Database servers, virtualization requiring performance and redundancy. | High performance and redundancy, good read/write speeds. | High cost, requires many drives, low storage efficiency. |

## **Storage Mode Selection Guide**

Choose the appropriate storage mode based on your requirements:

|  |  |  |  |
| --- | --- | --- | --- |
| **Requirement Type** | **Condition** | **Recommended RAID Mode** | **Description** |
| **Performance** | High performance demand | RAID 0， RAID 5， RAID 6， RAID 10 | RAID 0 offers the best performance but lacks redundancy. RAID 5/6/10 balance performance and redundancy. |
| High performance + redundancy | RAID 10 | Combines RAID 1's redundancy and RAID 0's performance benefits. |
| **Redundancy** | High redundancy demand | RAID 1， RAID 6， RAID 10 | RAID 1 provides basic redundancy but requires double the capacity. RAID 6 and RAID 10 offer advanced redundancy. |
| Low redundancy demand | RAID 0、JBOD | RAID 0 and JBOD are economical choices without redundancy. RAID 0 offers faster performance due to striping. |
| **Cost and Capacity** | Budget constraints | Basic，JBOD | Basic requires only one drive, minimizing hardware cost. JBOD maximizes capacity without redundancy overhead. |
| RAID 0 | RAID 0 is cost-effective but risks total data loss if one drive fails. |
| RAID 1 | RAID 1 requires double the drive capacity for redundancy. |
| RAID 5/6/10 | These modes require some capacity for parity or mirroring, reducing effective capacity. |
| Expandable capacity need | RAID 5， RAID 6 | These modes provide good capacity utilization and support expansion. |
| **Application Scenarios** | High performance + redundancy | RAID 10 | Ideal for database servers and virtualization environments. |
| RAID 5， RAID 6 | Suitable for file storage servers, focusing on cost-efficiency and redundancy. |
| **Fault Tolerance** | Tolerates multiple failures | RAID 6 | Can tolerate up to two drive failures. |
| RAID 10 | Tolerates multiple drive failures depending on the health of mirrored pairs. |

**Note:** To select the most appropriate storage mode, consider factors such as performance, redundancy, cost, capacity requirements, and application scenarios. For tailored recommendations based on specific needs, it is advisable to consult a professional for precise guidance.
