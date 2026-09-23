# How to Choose the Right RAID Level for Your Needs

> **Article ID**: `132`  
> **Category**: `Application Guide > Storage > How to Choose the Right RAID Level for Your Needs`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/132  

---

## Overview

When setting up a NAS volume for the first time or expanding storage capacity, choosing the right RAID level is one of the most important decisions for users. RAID technology combines multiple independent physical drives into one logical storage space. This can not only improve data read/write performance, but also provide data redundancy to help prevent data loss caused by one or more drive failures.

To help users make the best configuration decision, UGREEN provides two official dedicated tools. We recommend using them together before planning your setup:

● **Configuration and capacity estimation**: [UGREEN NAS Official RAID Calculator](https://nas.ugreen.com/pages/raid-calculator?_pos=1&_psq=RAID&_ss=e&_v=1.0)

● **Drive compatibility**: [UGREEN NAS Official Drive Compatibility List](https://nas.ugreen.com/pages/compatibility) (Before purchasing or installing drives, you can use this tool to check whether the drive model is compatible with your device).

**Applicable platform**: All UGREEN NAS models running UGOS Pro

## RAID Level Overview

Different RAID levels have different strengths in terms of capacity utilization, read/write performance, and data protection level, namely the number of drive failures that can be tolerated. The following describes the main RAID levels supported by UGREEN NAS.

![](https://file-us.ugreennas.com/admin/article/2026-07-23/8d45d871eaf94877a8d3e18cdec4dc1b.webp)

### Basic (Single-drive Mode)

● Fault tolerance: None. If the drive fails, all data will be permanently lost.

● Description: No RAID array is created. Each drive is used independently as a separate volume.

### JBOD

● Fault tolerance: None.

● Description: JBOD combines multiple drives into a single storage pool. The system merges the capacity of multiple drives and uses them as one storage space. If one of the drives fails, data in the storage pool may become corrupted or lost.

### RAID 0

● Fault tolerance: None.

● Description: RAID 0 distributes data across multiple drives to improve read/write performance and maximize the available capacity of multiple drives. However, RAID 0 provides no data redundancy. If any drive fails, all data in the storage pool may be lost.

### RAID 1

● Fault tolerance: Allows one drive to fail.

● Description: Data is fully mirrored between the drives, with both drives written to simultaneously. It significantly improves read speed and provides very high data protection.

### RAID 5

● Fault tolerance: Allows any one drive to fail.

● Description: Balances storage capacity and data protection, making it the most commonly used RAID level for multi-bay NAS devices. When one drive fails, the system can rebuild data in real time using parity information stored on the other drives.

### RAID 6

● Fault tolerance: Allows two drives to fail at the same time.

● Description: Uses dual parity for enhanced data protection. Even if a second drive fails during the vulnerable rebuild process after one drive has already failed, your data remains safe.

### RAID 10

● Fault tolerance: Allows one to two drives to fail, provided that the failed drives are not in the same mirrored pair.

● Description: Creates RAID 1 mirrored pairs first, then combines them into RAID 0. It offers the excellent read/write performance of RAID 0 and the fault tolerance of RAID 1, but with a higher capacity cost.

## Official Tools

### Capacity and Configuration planning

Before purchasing drives, we recommend visiting the [UGREEN Official RAID Calculator](https://nas.ugreen.com/pages/raid-calculator?_pos=1&_psq=RAID&_ss=e&_v=1.0) .

In the calculator, enter the number of drives you plan to purchase and the capacity of each drive, for example, 3 × 4TB HDDs + 1 × 8TB HDD. The page will visually illustrate your available capacity, redundancy protection space, and system reserved space under different RAID levels. This helps you determine your drive purchase budget based on your actual needs.

### Verify Hardware Compatibility

After selecting the capacity, go to the [UGREEN Official Drive Compatibility List](https://nas.ugreen.com/pages/compatibility) before placing an order for drives.

Enter the drive model you are interested in in the search box to confirm that it has passed UGREEN Lab's official compatibility certification with no faults found. Using drives that have not been certified for compatibility may cause unexplained drive dropouts in the underlying array or frequent error messages.

## RAID Selection Recommendations

If you are still unsure after reviewing the technical parameters above, refer to the following recommendations based on your usage needs:

![](https://file-us.ugreennas.com/admin/article/2026-07-23/497a1a88214342dcb01163aea8b79cd5.webp)
