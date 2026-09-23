# [FAQ] What to Do If I Failed Access NAS Shared Folders via Windows File Explorer (SMB)?

> **Article ID**: `506`  
> **Category**: `Application Guide > Control Panel > File Service > [FAQ] What to Do If I Failed Access NAS Shared Folders via Windows File Explorer (SMB)?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/506  

---

## Problem

When connecting to and accessing UGREEN NAS files using the SMB protocol, you may encounter shared access failures. Below are the possible causes and corresponding solutions.

## Solution

#### Ensure the UGREEN NAS network connection is stable.

#### Check if the SMB service is enabled:

● Navigate to [Control Panel > File Service > SMB], and ensure the SMB service is **enabled**.

#### Configure the SMB protocol version:

Go to [Control Panel > File Services > SMB > Advanced] to check and set the SMB protocol version:

**Recommended configuration:**

● Maximum SMB Version: **SMB 3** (for better security).

● Minimum SMB Version: **SMB 2** (compatible with most devices).

**Notes:** Some older devices (e.g., legacy computers) may only support the SMB 1 protocol. If compatibility is required, set the minimum SMB version to SMB 1. However, note that SMB 1 has lower security.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/0a3c109c636f4c3cb2f6d3e942930e86.webp)

#### Check Shared Folder Permissions

● Navigate to [Files > Shared Folder > Subfolders], right-click the target folder, and select [Properties > Permissions]. Ensure the current user has been assigned access permissions (e.g., Read/Write or Readonly).

#### Check Firewall Settings

● Go to [Control Panel > Security > Firewall], and ensure that the SMB service is not blocked. If SMB service appears in the "Deny" list, remove it.

#### Ensure Devices Are on the Same LAN

● Verify that the UGREEN NAS and the SMB client (e.g., Windows PC) are on the same local area network. For detailed instructions, refer to [**How to Check if Your Computer and UGREEN NAS are on the Same LAN**](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjoxMTIxLCJhcnRpY2xlSW5mb0lkIjozODgsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIn0=)

#### Check if SMB Support is Enabled on Windows

● Open the [Control Panel] in Windows, go to [Programs > Turn Windows features on or off], check the options related to SMB support, and click [OK] to enable SMB support.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/d0e190b444dc40de83c739fd4d10b20c.webp)

#### Enable Insecure Guest Login

● Press **Windows+R**, type `gpedit.msc` and run it.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/068094bc8fb441c591fdc5fce97caded.webp)

● Navigate to [Computer Configuration > Administrative Templates > Network > Lanman Workstation], double-click [Enable insecure guest logons], select [Enabled], and click [OK].

![](https://file-us.ugreennas.com/admin/article/2025-09-05/1c4dbaca0c8343b48ea11fd14e71bcb9.webp)

#### Clear Old Connection Records

If you see the message "**One or more users are not allowed to access simultaneously**", it may be caused by old connection records:

● Press **Windows+R**, type `cmd`, and run it. In the command prompt, execute the following command multiple times, then try connecting again.

```
net use * /del /y
```

![](https://file-us.ugreennas.com/admin/article/2025-09-05/07166886053746d89c2f4a28d18de970.webp)

#### Reset Saved Windows Credentials

● On your Windows computer, go to [Control Panel > User Accounts > Credential Manager > Windows Credentials], and remove all saved Windows credentials related to the UGREEN NAS, including IP addresses and server names. After completing this, try connecting to the NAS again.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/4b181bc5b8434ba28bcf9d009e71b191.webp)

● If the Windows Credentials list is empty but you still cannot connect to the UGREEN NAS, go back to [Windows Credentials > Add a Windows Credential]. Enter the IP address or server name of the UGREEN NAS, along with the username and password. Then try connecting again.

![](https://file-us.ugreennas.com/admin/article/2025-09-05/c059176d63364f8b9d2adc9abf9900c5.webp)

#### Contact UGREEN NAS Official Technical Support

● If the issue persists, please contact UGREEN NAS official technical support.

**Related Articles**

● [How to use SMB protocol to achieve fast multi-terminal file transfer on the LAN?](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTA2MiwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiZW4tVVMiLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjozNTksImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)
