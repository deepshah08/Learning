# [FAQ] why does my hard disk display a lower capacity than what is displayed on the label?

> **Article ID**: `344`  
> **Category**: `Application Guide > Storage > FAQ > [FAQ] why does my hard disk display a lower capacity than what is displayed on the label?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/344  

---

### **Description**

When checking the hard disk capacity in Storage Manager, why does my hard disk display a lower capacity than what is displayed on the label?

### **Diagnosis**

Hard disk manufacturers calculate hard disk capacity based on decimal (base 10). In the decimal system:

* 1 Megabyte (MB) = 1,000,000 bytes
* 1 Gigabyte (GB) = 1,000,000,000 bytes
* 1 Terabyte (TB) = 1,000,000,000,000 bytes

However, operating systems such as system BIOS, Windows, and earlier versions of macOS use a binary (base 2) counting system. In binary:

* 1 Megabyte (MB) = 1,048,576 bytes
* 1 Gigabyte (GB) = 1,073,741,824  bytes
* 1 Terabyte (TB) = 1,099,511,627,776 bytes

**Capacity Calculation Formulas**

**● Decimal capacity / 1,048,576 = Binary MB capacity**

**● Decimal capacity /  1,073,741,824 = Binary GB capacity**

**● Decimal capacity / 1,099,511,627,776 = Binary TB capacity**

**Example**

A 500GB hard disk is approximately 500,000,000,000 bytes (500 × 1,000,000,000). When calculated using binary GB, (500,000,000,000 / 1,073,741,824) results in approximately 465 GB. This is why a 500 GB hard disk is shown as 465 GB in Windows.

Similarly, a 5TB hard disk is approximately 5,000,000,000,000 bytes (5 × 1,000,000,000,000). When calculated using binary TB, (5,000,000,000,000 / 1,099,511,627,776) results in approximately 4.54 TB. This is why a 5 TB hard disk is shown as 4.54 TB in Windows.

**Hard Disk Capacity Comparison Chart**

|  |  |  |
| --- | --- | --- |
| **Product Capacity (Decimal)** | **Mac OS X Output (Decimal)** | **Windows Output (Binary)** |
| 500 GB | 500 GB | 465 GB |
| 1 TB (1,000 GB) | 1 TB (1,000 GB) | 931 GB |
| 2 TB (2,000 GB) | 2 TB (2,000 GB) | 1.81 TB |
| 3 TB (3,000 GB) | 3 TB (3,000 GB) | 2.72 TB |
| 4 TB (4,000 GB) | 4 TB (4,000 GB) | 3.63 TB |
| 5 TB (5,000 GB) | 5 TB (5,000 GB) | 4.54 TB |
| 6 TB (6,000 GB) | 6 TB (6,000 GB) | 5.45 TB |
| 8 TB (8,000 GB) | 8 TB (8,000 GB) | 7.27 TB |
| 10 TB (10,000 GB) | 10 TB (10,000 GB) | 9.09 TB |
| 12 TB (12,000 GB) | 12 TB (12,000 GB) | 10.91 TB |
| 14 TB (14,000 GB) | 14 TB (14,000 GB) | 12.73 TB |
| 16 TB (16,000 GB) | 16 TB (16,000 GB) | 14.55 TB |
| 18 TB (18,000 GB) | 18 TB (18,000 GB) | 16.37 TB |
| 20 TB (20,000 GB) | 20 TB (20,000 GB) | 18.18 TB |
| 22 TB (22,000 GB) | 22 TB (22,000 GB) | 20.00 TB |
| 24 TB (24,000 GB) | 24 TB (24,000 GB) | 21.82 TB |

**Example**

Below is an example of how a 1TB HDD might appear in UGREEN NAS

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250407/27a58af4-be12-4d2a-ac5b-0d49664951c3.png)

**Please note:** The 1TB (1,000 GB) labeled on the hard disk indicates a decimal value, whereas the 931 GB indicated for the NAS hard disk capacity represents a binary value. These two figures represent the display results in different numbering systems. There may be minor differences in the final available space for hard disks of different brands and series. Additionally, the UGOS Pro system will occupy 16GB of space.

### **Conclusion**

**The storage capacity represented in decimal and binary is the same, but due to different units of measurement, the reported values also differ.** For example, the distance from point A to point B is 1 kilometer or 0.621 miles. The distance is the same, but the units are different, and thus the reported values differ as well.

For more details, please refer to [Storage Capacity Measurement Standards](https://www.seagate.com/support/kb/storage-capacity-measurement-standards-002046en/) and National Institute of Standards and Technology website: <http://physics.nist.gov/cuu/Units/binary.html>.
