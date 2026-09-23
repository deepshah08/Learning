# Relationship Between Hard Disk, Storage Pool, and Storage Volume

> **Article ID**: `418`  
> **Category**: `Application Guide > Storage > FAQ > Relationship Between Hard Disk, Storage Pool, and Storage Volume`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/418  

---

In the UGOS Pro system of UGREEN NAS, **Hard Disk, Storage Pool, and Storage Volume** are the three core concepts for building and managing data storage. They are closely related, and understanding their relationships is crucial for optimizing NAS configuration, enhancing data security, and improving system performance.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/bac9ebe26d6a4766a54d3834c8b2bb70.webp)

### Hard Disk

Hard disk is a physical device used to store data. UGOS Pro supports both Hard Disk Drive (HDD) and Solid State Drive (SSD). The primary function of a hard disk is to provide basic storage capacity. To flexibly expand storage capacity and improve data security, the system supports multiple hard disks working together.

Common Hard disk types:

● **HDD (Hard Disk Drive):** Large capacity, cost-effective, suitable for massive data storage.

● **SSD (Solid State Drive):** Fast speed, ideal for scenarios requiring high-performance reading and writing, such as running virtual machines or Docker.

### Storage Pool

Storage pool is a virtual storage pool created by combining one or more physical hard disks using **RAID** technology. The primary purpose of a storage pool is to consolidate the storage resources of multiple hard disks and provide data redundancy protection.

Different RAID modes provide the following functions through storage pools:

● **Performance Optimization**: For example, RAID 0 stores data blocks across multiple physical disks, enhancing read and write speeds.

● **Data Redundancy**: For example, RAID 1 ensures that even if one physical disk fails, data is not lost through data mirroring.

● **Volume and Data Protection Balance**: For example, RAID 5 and RAID 6 provide data protection while maintaining efficient storage utilization.

### Storage Volume

Storage volume is a logical storage area used by users to manage and operate data. After a storage pool is created, users can create one or more storage volumes on it. This is similar to partitioning a hard disk in a Windows system into multiple logical drives. For example, users can divide a storage pool into different storage volumes for storing personal files, shared files, or application data.

Each storage volume is equivalent to an independent "virtual hard disk", allowing users to flexibly allocate and manage storage resources based on their needs. storage volumes in the UGOS Pro system provide the following advantages:

● **Flexible Data Management:** Users can divide different storage volumes according to application needs, facilitating the independent management of different data.

● **Access Control:** Enhance data security by assigning access permissions to different users and applications.

● **Quota Management:** Administrators can set capacity quotas for each storage volume to prevent resource waste.

### The relationship among the three is summarized as follows

1. **From hard disks to storage pools**: Physical hard disks are added to a storage pool, and the system combines them into a single storage unit based on the RAID configuration to improve performance or enhance data redundancy. Different RAID modes determine the storage pool's capacity utilization and level of data protection.

2. **From storage pools to storage volumes**: After a storage pool is created, the system allows users to create multiple storage volumes on it. These storage volumes are provided for actual user access and are equivalent to virtualized hard disk areas. Different storage volumes can be used for different tasks or users, enabling independent data management.

3. **From Storage Volumes to user data**: A storage volume is a logical area where users store data. Users can create folders, upload files, and configure access permissions and storage quotas within a storage volume. Data is managed through the file system to ensure efficient utilization of storage resources.

**Additional Notes**:

● **Data security and redundancy**: The RAID mechanism helps protect data recovery in the event of partial hard disk failures. For critical data, RAID 5 or higher RAID levels are recommended.

● **Performance optimization**: For scenarios that require high performance, such as running Docker or virtual machines, using SSDs to create a storage pool can significantly improve read and write speeds.

### Storage Volume and Folder Management

In the UGOS Pro system, a **storage volume** is equivalent to a virtualized hard disk partition or logical storage volume. Users can create multiple folders within each storage volume to classify and manage files according to their needs. Different folders can provide dedicated storage areas for different applications, users, or tasks.

#### Creation and Purpose of Folders

● **Flexible Data Organization**: Users can create any number of folders within each storage volume to store different types of data. For example, you can create folders for personal files, company project files, video or multimedia materials, etc.

● **Data Classification Management**: Dividing folders within a storage volume can effectively classify and manage data, improving the efficiency of finding files and providing a better organizational structure for different types of data.

● **Access Control**:You can set individual access permissions for each folder, ensuring that different users or user groups only access folders related to their work. For example, you can set up dedicated folders for different departments within a company, controlling the data access permissions among employees.

#### The Role of Folders in Conjunction with Storage Volume

● **Storage Quotas:** Within a storage volume, administrators can set quotas for each folder or group of folders, limiting their storage capacity and preventing one folder from occupying too many resources and causing insufficient space in other folders.

● **Backup & Sync:** The UGOS Pro system supports automatic backup and synchronization of folders within storage volumes. Regular backup schedules ensure data safety, and folders can be synchronized with remote servers or other devices, enhancing data availability.

● **Cross-Platform Access:** Folders within storage volumes can be accessed in various ways, such as through SMB/CIFS, FTP, and other protocols, allowing users to flexibly access data in folders on different devices and providing a convenient cross-platform file management experience.

#### The Relationship Between Folders and Storage Volumes

● **Storage Volume** provide a logical "container" where users can create and manage folders.

● **Folders**, as the basic units of storage volumes, are the direct objects for user operations and data storage. Each folder is equivalent to a directory in a daily operating system, and users create folders to divide data.

● **Data Sharing:** Multiple users can share a storage volume, but manage their data independently through folders, ensuring that different users' data does not mix or conflict.
