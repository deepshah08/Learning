# [FAQ] Folder names in Chinese display garbled characters after mounting NFS using Windows File Explorer

> **Article ID**: `428`  
> **Category**: `Application Guide > Control Panel > FAQ > [FAQ] Folder names in Chinese display garbled characters after mounting NFS using Windows File Explorer`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/428  

---

## **Problem Description**

After mounting the NFS shared directory using File Explorer on a Windows system, Chinese folder names appear as garbled characters. This issue is typically caused by a mismatch in character encoding between the NAS and the Windows client. By default, NFS may not properly handle non-ASCII characters, such as Chinese, leading to file name garbling.

## **Solution**

When this issue occurs, it can be resolved by adjusting character encoding settings or using a more suitable NFS client. The following are the specific steps:

### **Modify the language and region settings in Windows**

Ensure that the computer system's language and region settings match those of the NAS, especially when handling Chinese characters, and make sure that the client computer system supports UTF-8 encoding.

#### **Procedure:**

1. **Open the Control Panel:**

   * Press `Win + R`, type `control`, Press Enter to open the Control Panel.
2. **Set the language and region:**

   * Select "**Clock and Region**", then click the "**Region**" option.
   * Confirm that the current system language and region are set to "**Chinese (Simplified, China)**".
   * ![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250401/9e326fd6-4833-46b0-a97f-9d88f292b157.png)
3. **Adjust the language for non-Unicode programs:**

   * Click on the "**Administrative**" tab.
   * Under "**Language for non-Unicode programs,**" click on "**Change system locale**."
   * Set the system locale to "**Chinese (Simplified, China).**"
4. **Enable UTF-8 support:**

   * In the "**Region Settings**" window, check "**Beta: Use Unicode UTF-8 for worldwide language support.**"
   * Click "**OK**" and restart the system as prompted by Windows to ensure the changes take effect.
   * ![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250401/9e1960be-94f4-4152-bc47-2b550e92ed55.png)

---

## **Additional Notes**

The built-in NFS client in Windows may have compatibility issues when handling non-ASCII characters (such as Chinese), which can cause abnormal file name displays. To avoid this, it is recommended to consider using third-party NFS client tools, as they typically offer better support for various character encoding formats, including UTF-8.
