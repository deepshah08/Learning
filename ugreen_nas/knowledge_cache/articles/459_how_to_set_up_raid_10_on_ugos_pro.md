# How to Set up RAID 10 on UGOS Pro?

> **Article ID**: `459`  
> **Category**: `Application Guide > Storage > FAQ > How to Set up RAID 10 on UGOS Pro?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/459  

---

RAID (Redundant Array of Independent Disks) is a technology that combines multiple hard drives into a single storage space, enhancing data storage security and read speed. Among all RAID types, RAID 10 is a configuration with high requirements for both data protection and system performance. In this article, we will introduce in detail how to create RAID 10 in UGOS Pro and help you understand its advantages and disadvantages.

## RAID 10 Application Scenarios

RAID 10 combines the high performance of RAID 0 with the data redundancy protection of RAID 1, making it an ideal choice for scenarios requiring high performance and stringent data security.

**Main Features**:

● **High Performance:** With RAID 0 technology, multiple hard drives work together to accelerate data read and write speeds.

● **Data Security**: The mirroring function of RAID 1 ensures that data on each hard drive is backed up on another. Even if one drive fails, data can still be recovered from the mirror.

**Illustration**: Assume you have four hard drives: Drive 1, 2, 3, and 4. When creating RAID 10, the system automatically forms a RAID 1 mirror set with Drive 1 and Drive 2, and another with Drive 3 and Drive 4. These two RAID 1 mirror sets are then combined into RAID 0, achieving RAID 10's high performance and data redundancy.

![](https://file-us.ugreennas.com/admin/article/2025-08-29/05bc2e0d93e047e19e5422b1ff73f282.webp)

## UGREEN NAS Compatible Devices

The following UGREEN DXP series NAS devices support creating RAID 10 storage pools:

● DXP4800 Series: DXP4800, DXP4800 Plus

● DXP6800 Series: DXP6800 Plus, DXP6800 Pro

● DXP8800 Series: DXP8800, DXP8800 Plus, DXP8800 Pro

● DXP480T Plus

## Hard Drive Requirements

Creating a RAID 10 storage pool requires installing a sufficient number of hard drives. Here are the specific requirements and fault tolerance explanations for RAID 10:

|  |  |  |  |
| --- | --- | --- | --- |
| **RAID Type** | **Minimum Number of Hard Drives** | **Usable Storage Pool Capacity** | **Fault Tolerance** |
| RAID 10 | ≥4 (even number)） | (Number of Drives / 2) x Smallest Drive Capacity | Half of Total Drive Capacity |

● **Number of Drives**: RAID 10 requires at least 4 hard drives, and the number must be even.

● **Storage Capacity**: Approximately half of the total number of drives. For example, with four 1TB drives in RAID 10, the usable space is 2TB.

● **Fault Tolerance**: Allows one drive failure within the same mirror set, but data will be lost if two drives in the same set fail simultaneously.

**Example for Fault Tolerance**:

Assume we have four hard drives forming a RAID 10 storage pool:

● Drive 1 and Drive 2 form one mirror pair.

● Drive 3 and Drive 4 form another mirror pair.

This configuration **allows only one drive failure per mirror pair.**

Example:

● **Fault Tolerance**: If Drive 2 and Drive 4 fail, data remains intact.

![](https://file-us.ugreennas.com/admin/article/2025-08-29/6a8088f60ba14e02b5f295efdfc6ae38.webp)

● **Data Loss**: If Drive 1 and Drive 2 (same mirror pair) fail simultaneously, all data will be lost.

![](https://file-us.ugreennas.com/admin/article/2025-08-29/e06c8c0b622945d3908d1306b31757b4.webp)

## Steps to Create RAID 10

RAID 10 combines the performance benefits of RAID 0 with the data protection of RAID 1. Here are the specific steps to create RAID 10:

1. In the UGOS Pro system, go to the **"Storage > Storage"** page and select to create a storage pool.

2. In the "Create storage pool" pop-up window, select the RAID 10 type and ensure the system detects a sufficient number of hard drives (at least 4).

![](https://file-us.ugreennas.com/admin/article/2025-08-29/a93a78dd93c24bb38be2907165ec9b34.webp)

3. Select the hard drives for RAID 10, ensuring an even number. Optionally, choose to perform a hard drive check.

4. Click "Confirm," and the system will automatically form mirror arrays with the hard drive pairs.

## Advantages and Disadvantages of RAID 10

**Advantages**

● **High Performance**: With RAID 0 technology, multiple hard drives work together to accelerate data read and write speeds.

● **High Fault Tolerance**: Data backup through mirroring ensures that even if one drive fails, data is not lost, maintaining system stability.

**Disadvantages**

● **Low Storage Capacity**: The total usable capacity of RAID 10 is half of all drive capacities.

● **Drive Failure Limitation:** Each mirror set allows only one drive failure. If both drives in the same mirror pair fail simultaneously, data cannot be recovered. For example, with four drives forming RAID 10 (A1-A2 and B1-B2), if A1 and B1 fail, the mirrored A2 and B2 still retain intact data, and the storage pool can operate normally. However, if A1 and A2 or B1 and B2 fail simultaneously, due to the loss of mirror copies, RAID 10 cannot recover the data for that set, resulting in data loss.

## Related Links

● [【FAQ】How to Choose a RAID Type?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjo5MDksImFydGljbGVJbmZvSWQiOjMwMiwiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIiLCJwYXRoQ29kZSI6IiJ9)

● [[Tutorial] How to Change the RAID Type of a Storage Pool?](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmMzkyIn0=)
