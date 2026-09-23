# Why does using RAID 0 result in speeds only equivalent to that of a single hard disk?

> **Article ID**: `586`  
> **Category**: `Application Guide > Storage > FAQ > Why does using RAID 0 result in speeds only equivalent to that of a single hard disk?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/586  

---

RAID 0, in theory, can achieve faster read and write speeds than a single hard disk by performing data striping across multiple hard disks. However, in practice, if the performance of RAID 0 does not meet expectations, it could be due to various factors, including hardware configuration, system settings, network environment, and more. This article will explore these factors and provide corresponding solutions.

## **Ensure consistency in hard disk configuration**

The performance of RAID 0 heavily relies on the consistency of the hard disks in the array. If the hard disks that make up RAID 0 have significant differences in capacity, rotational speed, or cache size, the overall performance may be compromised.

* **Inconsistent capacity:** hard disks with different capacities may result in some space being underutilized, affecting the performance of RAID 0.
* **Inconsistent rotational speed and capacity:** The rotational speed of hard disks directly impacts data access speed. Hard disks with lower rotational speeds can become a bottleneck.

**Solutions:**

* Use hard disks with the same capacity, rotational speed, interface type, and brand to ensure configuration consistency.
* Avoid mixing hard disks with different specifications to prevent impacting overall performance.

### **How to Choose the Right Hard Disk**

When selecting a hard disk, it is recommended to prioritize the following factors:

* **Enterprise-grade hard disks:** Compared to consumer-grade hard disks, enterprise-grade hard disks perform better in terms of both performance and stability.

* **Read/Write Speed:** Check the sequential and random read/write speeds provided by the hard disk manufacturer.

* **Durability (TBW):** Particularly for SSDs, the write endurance is crucial for long-term, high-intensity operation.

## **RAID 0 Space Allocation Issues**

When creating a RAID 0 array with hard disks of different capacities, the UGOS Pro system will allocate the total disk capacity for RAID 0 usage to avoid wasted space. In this case, the extra capacity from the larger disk acts as the read/write capability of a single disk, which may lead to a decrease in performance.

### **Example Scenario**

* **Scenario:** Disk A is 1 TB, Disk B is 900 GB, and after creating RAID 0, the total capacity is 1.9 TB.
* **Issue:** The extra 100 GB on Disk A operates in single-disk mode, and the read/write speed for this portion of data is only as fast as a single hard disk.

**Solution:**

* Try to use hard disks with the same capacity to build RAID 0, avoiding performance degradation caused by excess space.

## **Network Speed Limitations (NAS/Computer Environment)**

The speed of RAID 0 when transmitting over the network may be limited by network bandwidth. For example, if the local read/write speed of RAID 0 is up to 500 MB/s, performance may still be affected if the network bandwidth is insufficient.

### **Transmission Speed Comparison**

* **NAS and computer both using Gigabit Ethernet:** The maximum transmission speed between them is approximately 110 MB/s.

* **NAS and computer both using 2.5 G Ethernet:** The maximum transmission speed between them is approximately 280 MB/s.

* **NAS and computer both using 10 G Ethernet:** The theoretical maximum transmission speed between them can exceed 1 GB/s.

**Solution:**

* Upgrade the network interfaces on both the NAS and client devices to 2.5 G or 10 G network cards.

* Enable Link Aggregation to combine multiple network connections into a single logical connection to increase transmission speed.

* Use high-performance network switches to ensure smooth network communication between devices without bottlenecks.
