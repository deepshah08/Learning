# Does the virtual machine support mounting iSCSI?

> **Article ID**: `723`  
> **Category**: `Application Guide > Virtual Machine > FAQ > Does the virtual machine support mounting iSCSI?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/723  

---

Currently, the UGOS Pro system **does not support directly mounting NAS-created iSCSI LUNs as virtual disks for virtual machines.**

## **Explanation**

The UGOS Pro virtual machine module does not yet include the iSCSI Initiator feature, meaning it cannot directly recognize or mount iSCSI block devices at the virtual machine level.

### **Recommended Alternative: Mount Shared Folders via SMB**

If you need to provide additional storage space for a virtual machine, we recommend accessing the NAS storage via the SMB protocol:

1. Enable SMB on the NAS.

2. Mount the SMB-shared folder on the virtual machine operating system (as a network drive).

3. After mounting, you can freely access the data.

For detailed configuration, please refer to: [[Tutorial] How to use SMB protocol to achieve fast multi-terminal file transfer on the LAN?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTA2MiwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjozNTksImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

## **Enable Virtual Bridge Network**

To ensure the virtual machine can access the NAS SMB service, both the virtual machine and NAS must be on the same network:

● Enable "**Virtual Bridge Mode (LinuxBridge)**" before creating the virtual machine.

● Once configured, the virtual machine will obtain an IP address in the same subnet as the NAS, enabling bidirectional access.

For detailed configuration, please refer to: [Enabling Virtual Bridge for Virtual Machines (LinuxBridge Mode)](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6NTUwMiwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo3MTksImFydGljbGVWZXJzaW9uIjoiMS4wIiwicGF0aENvZGUiOiIifQ%3D%3D)
