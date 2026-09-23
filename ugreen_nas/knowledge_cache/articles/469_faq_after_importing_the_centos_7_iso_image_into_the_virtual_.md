# [FAQ] After importing the CentOS 7 ISO image into the virtual machine and starting it up, the system enters rescue mode.

> **Article ID**: `469`  
> **Category**: `Application Guide > Virtual Machine > FAQ > [FAQ] After importing the CentOS 7 ISO image into the virtual machine and starting it up, the system enters rescue mode.`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/469  

---

## **Problem Description**

A CentOS 7 ISO image was used to install the system on another virtualization platform. After exporting the OVA and uploading it to a NAS, it was then imported into a virtual machine. Upon startup, the system booted into rescue mode.

![](https://ugreen-pro.oss-cn-shenzhen.aliyuncs.com/ugreen-pro/admin/article/20241107/646c7c2d-b47f-4a4f-b919-7e663cc7863e.png)

## **Solution**

This issue can be resolved by changing the disk type to IDE. The specific steps are as follows:

"Virtual Machine Settings > Basic Configuration > Disk 1", change the disk type to IDE.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250829/d7277cac-174b-478e-94cc-d30a1862a3f1.png)
