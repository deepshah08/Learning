# What should I do if I forget the administrator password when logging in to UGOS Pro?

> **Article ID**: `435`  
> **Category**: `Application Guide > Control Panel > FAQ > What should I do if I forget the administrator password when logging in to UGOS Pro?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/435  

---

If you forget the administrator password for UGOS Pro on your UGREEN NAS and are unable to log in, you can regain access by resetting the device. Please follow the steps below:

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250709/b5a293b9-b060-4341-a9f1-d99e74f03886.png)

Press and hold the "Reset" button on the back of the device for about 5 seconds. Release it when you hear a beep — this will reset the following settings:

**Note:** If you continue holding the button for up to 8 seconds, until the device emits three short beeps and then release it, the system will automatically reboot and restore factory settings. Restoring factory settings will erase all custom configurations, including network settings, user accounts, system preferences, and personal folder data — but will not delete data stored on the hard disks.

### **1. Reset Network Settings and Administrator Password**

The device will restore the default network configuration. You can log in to the UGOS Pro system using a temporary administrator account: admin (with a blank password). Then, set a new secure password for the administrator account you forgot.

### **2. Clear the IP Blocklist**

All previously blocked IP addresses will be removed (Control Panel > Security > Block Management > Blocked IP List). This helps prevent access issues caused by IP restrictions.

### **3. Disable the Firewall**

The firewall will be turned off (Control Panel > Security > Firewall). If previous network access was blocked by the firewall, access will be restored after the reset.

### **4. Reset HTTP/HTTPS Ports**

The system’s HTTP and HTTPS ports will be reset to their default values: HTTP to 9999 and HTTPS to 9993. After the reset, you can access the device’s management page via these default ports.

### **5. Clear Large Files (When EMMC Storage Is Low)**

If the device’s EMMC storage capacity falls below 4GB, the system will automatically delete large non-system files (files larger than 100MB) stored on the EMMC. This does not affect system files and helps free up space to ensure stable system operation.
