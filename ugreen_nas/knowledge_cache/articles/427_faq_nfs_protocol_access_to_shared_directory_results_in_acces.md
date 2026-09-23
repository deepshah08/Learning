# [FAQ] NFS Protocol Access to Shared Directory Results in "Access Denied" Notification

> **Article ID**: `427`  
> **Category**: `Application Guide > Control Panel > File Service > [FAQ] NFS Protocol Access to Shared Directory Results in "Access Denied" Notification`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/427  

---

## Problem Description

When mounting and accessing the shared folders of UGREEN NAS using the NFS protocol, you may encounter a system message stating "Access Denied." This often leads to an inability to read from or write to shared files. The causes of this issue can be varied, primarily including improper NFS permission configuration of the shared folder or incorrect network and permission settings on the client computer. The following are possible reasons and corresponding solutions.

## Solutions

### Incorrect NFS server-side permission configuration

On UGREEN NAS, the permission configuration of NFS shared folders is crucial. If improperly configured, client devices will not be able to mount or access shared directories correctly.

#### Please check and ensure the following configurations are correct:

* **Server address:** Confirm whether the IP address of the computer allowed to mount and access the shared folder has been filled in correctly. If the IP address is incorrectly configured, the client will not be able to connect to the NFS shared directory.
* **Permission settings:** Ensure that the permission settings for the NFS shared folder are set to "read-only" or "read-write." If the "Access Denied" option is mistakenly selected, the client will not be able to perform any operations.
* **Squash settings:** Enable the "Log all users in as admin" option to ensure that the client accesses the shared folder with the correct permission level. This can prevent access issues caused by unsynchronized user permissions.

* ![](https://ugreen-pro.oss-cn-shenzhen.aliyuncs.com/ugreen-pro/admin/article/20240929/5285543c-2c11-423f-8b34-d398ceff501e.png)

### NFS client configuration issues

Even if configured correctly on the UGREEN NAS side, incorrect network or permission settings on the client device can still lead to an inability to access shared folders.

#### Client configuration checks**：**

* **Firewall settings:** Check the firewall rules on the client computer. Ensure the firewall allows NFS protocol traffic. If you are unsure about the firewall configuration, you can temporarily disable the firewall to test if access can be achieved normally.
* **Network configuration:** Confirm that the client computer and the UGREEN NAS device are on the same local area network and can communicate with each other. If there are network isolation, VLAN, or other network configuration issues, it may result in restricted NFS access.

### Other possibilities

* **NFS version mismatch:** Ensure that both the client and server sides are using compatible NFS versions. For example, if UGREEN NAS uses NFSv3 and the client device tries to mount using NFSv4, compatibility issues may arise. It is recommended to use the same NFS version.
* **Permission mapping issues:** If the user permissions on the client device do not match those on the UGREEN NAS, access may also be restricted. Ensure that the client's users have the corresponding read-write permissions on the UGREEN NAS side.

## Additional knowledge

To check the firewall rules between the client computer and the UGREEN NAS and ensure that NFS protocol traffic can pass through, you can follow the steps below. You can also refer to the steps on how to temporarily disable the Windows firewall.

### **Check firewall rules**

1. **Open firewall settings:**

   * Press `Win + R`, type `control` to open Control Panel.
   * In the Control Panel, find and click on **"Windows Defender Firewall."**
2. **Check inbound and outbound rules:**

   * Click on **"Advanced settings"** on the left, which will open the **Windows Defender Firewall with Advanced Security** window.
   * In the menu on the left, click on **"Inbound Rules,"** which represents network traffic from the outside to the computer.
   * Look for rules related to the **NFS service** or related ports (usually port 2049) in the list.
   * Similarly, click on **"Outbound Rules"** to ensure that outbound traffic is allowed by the relevant rules.
3. **Ensure port 2049 is open:**

   * The **NFS service** typically uses port **2049** for communication. Check for allow rules for this port. If none exists, you can manually add a firewall rule.
   * To add a new rule:

     + On the right side of **Inbound Rules** or **Outbound Rules**, click **"New Rule."**
     + Choose **"Port,"** then click **"Next."**
     + Select **"TCP,"** and enter **2049** in the **Specific local ports**, then click "Next."
     + Choose **"Allow the connection,"** click **"Next."**
     + Select the network types the rule applies to (Public, Private, or Domain), and then continue to click **"Next."**
     + Name the rule and complete the creation.

### **Temporarily disable Windows Firewall**

1. **Open Windows Firewall settings:**

   * Press `Win + R`, type `control`, and press Enter.
   * In the Control Panel, click on **"Windows Defender Firewall."**
2. **Disable the firewall:**

   * Click on **"Turn Windows Defender Firewall on or off"** in the left-hand menu.
   * Under **Private network settings** and **Public network settings**, select **"Turn off Windows Defender Firewall (not recommended)."**
   * Click **"OK."**
   * ![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250903/091416af-4720-49bf-8a0a-dd60ea24d090.png)
3. **Test the connection:**

   * After disabling the firewall, try to access the shared folders of UGREEN NAS using the NFS protocol again to test if access is normal.
4. **Restore firewall settings:**

   * After completing the test, it is recommended to re-enable the firewall to avoid leaving your computer unprotected for a long time.
   * Follow the steps above to open the firewall settings again, select **"Turn on Windows Defender Firewall,"** and click **"OK."**
