# How to Fix the Issue of OVA Failing to Start After Importing into a Virtual Machine

> **Article ID**: `588`  
> **Category**: `Application Guide > Virtual Machine > FAQ > How to Fix the Issue of OVA Failing to Start After Importing into a Virtual Machine`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/588  

---

In the UGOS Pro system, virtual machines imported using OVA files may sometimes fail to start. For example, an imported Debian 12 virtual machine may boot into the UEFI Shell. This issue is usually caused by a missing bootloader configuration. Below is a detailed solution.

## **Issue Description**

1. A virtual machine created using the Debian 12.7.0 ISO image works normally with the following configuration:

* Boot type: UEFI
* Disk: Virtio disk
* Graphics: Virtio graphics

2. After exporting this VM as an OVA file and importing it again to create a new VM, the VM fails to boot and enters the UEFI Shell, showing an error that the bootloader file cannot be found.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/a83d5714-6442-4d13-9268-24c8465eb606.webp)

3. If you try changing the boot type to BIOS, the system will hang when "Booting from Hard Disk."

## **Solution**

### **Enter UEFI Settings**

1. Power on the machine and access the console. During the loading screen, press F2 to enter the UEFI settings interface.

2. In the UEFI settings, select Boot Maintenance Manager, then press Enter to proceed to the next page.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/d845f4a7-2c98-4b66-a146-ac47baf832e7.webp)

### **Add a Boot Option**

1. Select "Boot Options" to enter the boot options page.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/a017ac92-2bb9-48e7-8628-dbb1adc56323.webp)

2. Click "Add Boot Option" to enter the file browsing page (File Explorer).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/505ffbac-6b38-4660-a2e0-ff8913ad6523.webp)

3. Press Enter to go to the next level page.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/37622f82-ab22-4e9f-9b54-a5ab688a4404.webp)

4. In the file browsing page, select the EFI folder.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/878834db-efad-47ea-a94c-ffd569da59d1.webp)

5. Enter the folder corresponding to your operating system (e.g., `debian`).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/91072a88-ba98-4760-a47f-3235a748b816.webp)

6. Locate the file [shimx64.efi] and press Enter to confirm.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/af3d43cf-ff05-4e2f-927a-269555b79263.webp)

7. Select “Input the description” to set the boot description (e.g., set it to `debian`), then choose “Commit Changes and Exit” to save the configuration.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/690d4a79-fe4d-4817-9204-acae6ae4c5f8.webp)

### **Change Boot Order**

1. After setting the boot description, you will enter the "Boot Options" screen. Here, select Change Boot Order to modify the boot sequence.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/837da758-03a7-45f7-96be-212da63b135b.webp)

2. Set the newly added boot option (e.g., `debian`) as the first boot priority.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/25c82e35-803f-444a-a8c9-ae8f1f286b9f.webp)

3. Press F10 to save the configuration and exit.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/7e5c1ac3-36d0-4580-900e-d1e1b235d3fc.webp)

### **Start the Virtual Machine**

1. Return to the UEFI settings screen and select “Continue” to enter the boot menu.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/b7f0ef73-5e44-4c36-b9a6-23cf320c0575.webp)

2. In the boot menu, select the newly added boot option (e.g., `debian`), and the system should boot normally.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/b5793913-109c-43d7-806b-d083bb5c8456.webp)
