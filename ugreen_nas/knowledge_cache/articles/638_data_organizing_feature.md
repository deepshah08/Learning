# Data Organizing Feature

> **Article ID**: `638`  
> **Category**: `Application Guide > Storage > FAQ > Data Organizing Feature`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/638  

---

In the "Storage" application, the data Organizing feature supports periodic data Organizing for specific RAID types (RAID5 or RAID6) in storage pools to maintain data consistency and enhance data security. The following conditions must be met to use this feature:

## **Activation Conditions**

1. **Storage pool type limitations**

The data Organizing feature can only be enabled for "RAID5" or "RAID6" type storage pools.   
**Reason:** RAID 5/6 achieves data redundancy through parity or dual parity, and during the Organizing process, redundant information can be used to optimize data distribution, enhancing storage reliability.

2. **Storage Pool Status Requirements**

The storage pool must be in a normal or warning state. If the storage pool is degraded (e.g., due to an unresolved hard disk failure), the data Organizing feature cannot be enabled.

## **Effect of Data Organizing**

Once the Data Organizing feature is enabled, the UGOS Pro system will perform the following actions to optimize storage performance and extend hard disk lifespan:

1. The system will automatically rearrange the data blocks stored on the hard disk to reduce fragmentation and improve data read/write efficiency.
2. By reducing fragmentation, data blocks can be found and accessed more quickly, enhancing file access and transfer speeds.
3. During the Data Organizing process, the integrity of the data will be checked. This ensures that if a hard disk fails, lost information can be recovered through redundant data, ensuring data availability.
4. Data Organizing reduces frequent read/write operations caused by uneven data distribution, lowering physical wear and tear on the hard disk and extending its lifespan.

### **Activation Steps**

1. Enter the "Storage" application, click [Storage] > [Data Organizing].
2. Select the target storage pool and click the "Start Organizing" button.
3. The system will begin data organizing. Please note that data organizing requires a significant amount of time and consumes computing resources, so it is recommended to perform it during off-peak hours.
4. Follow the prompts to set up the organizing schedule (e.g., periodic execution time, priority, etc.).
5. Click [Edit] to set the organizing schedule, such as the frequency of periodic execution and the time for the first organizing.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250416/5e2d99c9-a327-4313-9a49-1069554e01d5.png)

### **Notes**

* It is recommended to back up important data using the backup feature or manually copy it before organizing to avoid accidental loss.
* If the storage pool status changes to "Degraded" or "Fault," the hard disk must be repaired before re-enabling the organizing feature.
* Storage pools in non-redundant modes such as RAID0/1/10 do not support the Data Organizing feature.
