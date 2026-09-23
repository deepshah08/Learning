# Enable Insecure Guest Logon in Windows to Fix SMB Connection Issues

> **Article ID**: `619`  
> **Category**: `Application Guide > Control Panel > File Service > Enable Insecure Guest Logon in Windows to Fix SMB Connection Issues`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/619  

---

Starting from Windows 10, Microsoft has significantly enhanced the security of the SMB protocol by disabling the insecure guest logon feature by default. This measure effectively prevents unauthorized users from accessing shared resources, providing stronger data protection. However, in some cases, this setting may cause SMB connection failures. If you encounter such issues, you can try enabling the insecure guest logon feature.

**Steps to Enable Insecure Guest Logon:**

1. Press `Win + R` to open the Run dialog, type `gpedit.msc`, and press Enter.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/ae6326cb-752a-423f-8fc9-bdfb974d64ca.png)

2. In the Local Group Policy Editor, navigate to: [Computer Configuration] > [Administrative Templates] > > [Lanman Workstation].
3. Locate" Enable insecure guest logons", and double-click to open it.
4. Select "Enabled", then click "Apply" to save the changes.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250320/289de04f-01cc-4715-a537-bcefd155b89f.jpeg)

5. Close the "Local Group Policy Editor", return to "Files", and try reconnecting to the SMB share to check if the issue is resolved.

## **Notes**

* Enabling insecure guest logon may reduce network security, making shared resources more vulnerable to unauthorized access.

* It is recommended to enable this feature only if no other solutions work and disable it once the issue is resolved.

* For enhanced security, consider additional measures such as enabling firewalls, setting strong passwords, and restricting access to shared resources.

Following these steps, you can quickly resolve SMB connection failures. If the issue persists, further network configuration checks or technical support may be required.
