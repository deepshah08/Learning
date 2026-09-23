# What to Do if a Windows Computer Cannot Access SMB via IP Address?

> **Article ID**: `512`  
> **Category**: `Application Guide > Control Panel > File Service > What to Do if a Windows Computer Cannot Access SMB via IP Address?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/512  

---

## **Problem Description**

On a Windows system, SMB shares cannot be accessed via IP address, but accessing via NAS hostname works fine. Restarting the computer temporarily resolves the issue.

## **Cause Analysis**

The computer has cached the SMB authentication information locally. If the username used to log in to SMB changes, or if a user is deleted on the NAS, it may affect the SMB login during the next attempt.

## **Solution**

### **Deleting Credentials in Windows System**

1. Press Windows + R on your keyboard to open the "Run" window.
2. In the "Run" window, type `control /name Microsoft.CredentialManager` and press Enter.
3. In the "Credential Manager", click on "Windows Credentials" to view the stored Windows credentials.
4. Locate the credentials related to the NAS IP address, click the dropdown arrow next to them, and select "Remove".
5. Double-check the records under Windows Credentials to ensure that the credentials have been successfully removed.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250716/cd33f228-f237-47c5-a733-7c7116ec491d.png)

### **Deleting Network Connections in Windows System**

1. Deleting Network Connections in Windows System
2. In the "Run" window, type `cmd` and press Enter. This will open the Command Prompt window.
3. To view existing network connections, type the `net use` command in the Command Prompt and press Enter.
4. In the network connection list, find `\\NAS IP\IPC$`, then copy this remote address and use the `net use \\NAS IP\IPC$ /del` command to delete the connection.
5. Type the `net use` command again to view the network connections and confirm whether `\\NAS IP\IPC$` has been removed from the list.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250716/aee21603-5486-4f4e-b3e2-110307a84eda.png)

### **Restart and Reconnect**

If the above two steps have not resolved the issue, try restarting the computer. After the restart, attempt to reconnect to the SMB share to check if the issue has been resolved.
