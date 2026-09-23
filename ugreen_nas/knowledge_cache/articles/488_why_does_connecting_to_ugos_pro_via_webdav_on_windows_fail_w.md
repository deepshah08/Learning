# Why does connecting to UGOS Pro via WebDAV on Windows fail with an 'cannot access' error?

> **Article ID**: `488`  
> **Category**: `Application Guide > Control Panel > File Service > Why does connecting to UGOS Pro via WebDAV on Windows fail with an 'cannot access' error?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/488  

---

## **Issue Description**

When attempting to connect to UGOS Pro via the WebDAV protocol on a Windows computer, the system displays the message: “Cannot access the UGREEN NAS IP address.”

**Possible Causes:**

1. **Devices are not on the same local network**  
   If you're using the internal IP address of the UGREEN NAS, but the computer and the NAS are not on the same local network, the connection will fail.
2. **Incorrect external network configuration**  
   To use WebDAV over an external network, you need to configure a public IP address or DDNS domain and ensure that port forwarding is properly set up on your router. Otherwise, the connection cannot be established.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250618/c96de8a8-7e6c-4c8f-b15c-d2f32b884104.png)

## **Solution**

To access files on your UGREEN NAS via WebDAV using a local account over an external network, follow the steps below:

### **Step 1: Ensure the WebDAV service is enabled on UGOS Pro**

1. Go to [Control Panel] > [File Service].
2. Make sure the WebDAV service is enabled, and take note of the service port numbers (the default ports are `5005` for HTTP and `5006` for HTTPS). You can view or modify the port settings under [WebDAV] > [Advanced].

### **Step 2: Obtain the External Access Address of the UGREEN NAS**

1. **Access within the Local Network**

When your computer is on the same local network as the UGREEN NAS, you can connect directly using the NAS's internal IP address, such as: `http://192.168.x.x:5006`

2. **Access from an External Network**

To connect from an external network, use one of the following methods to obtain the NAS access address:

* **Public IP Address:**

* Obtain the NAS's public IP address through your router or ISP.
* If using a public IP, ensure that your router is properly configured with port forwarding rules to map the WebDAV service ports to the internet.
* **DDNS Domain Name (Recommended):**
* Enable the built-in DDNS service provided by UGOS Pro to get a dynamic domain name linked to your NAS’s public IP.
* For setup instructions, refer to the guide: [Enable DDNS Support](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmODYifQ==)

### **Step 3: Configure the WebDAV Connection in Windows**

1. **Open File Explorer**

   * Press`Win + E`to open File Explorer.
   * In the left sidebar, click on “This PC”, then select “Map network drive” from the top menu.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250618/8218575b-1bcd-442a-bb17-aeca3085e729.png)

2. **Enter the WebDAV Address**

   * In the pop-up window, enter the WebDAV address of your UGREEN NAS in the “Folder” field. Use one of the following formats:

     + **HTTP (Unencrypted):** `http://[NAS_Public_IP_or_DDNS]:5005`
     + **HTTPS (Encrypted):** `https://[NAS_Public_IP_or_DDNS]:5006`
   * Check the box “Reconnect at sign-in”, then click “Finish”.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250618/6382b8bc-18b2-462a-acde-3b8e50e19561.png)

3. **Enter UGREEN NAS User Credentials**

   * In the dialog box that appears, enter the username and password of the account created on the UGREEN NAS. Click “OK” to complete the connection.
4. **Access Shared Folders**

   * Once connected successfully, the shared folders on your UGREEN NAS will appear under “This PC” in File Explorer. You can access and manage them just like local folders.

## **Notes**

* If the WebDAV service fails to connect, first confirm that the service is enabled and that the specified ports are not being used by other applications. If you detect service errors or port conflicts, adjust the settings and restart the related service promptly.
* HTTPS offers stronger encryption and overall security. It is recommended to connect to the WebDAV service via an HTTPS address.
* By default, Windows does not support mapping WebDAV drives using HTTP. You can enable HTTP support by modifying the system registry. For detailed steps, please refer to [the relevant guide.](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMTE0LCJhcnRpY2xlSW5mb0lkIjozODEsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)
* Firewall and Security Software: Check Windows Firewall or any third-party security software to ensure WebDAV connections are not being blocked. You may try temporarily disabling the firewall to troubleshoot connection issues.

* User Permissions: Ensure the entered username and password are correct, and that the account has the necessary permissions to access the WebDAV share.
* Third-Party Clients: If the built-in Windows WebDAV client fails to work properly, consider using third-party WebDAV tools such as Cyberduck or WinSCP.

* 如If the issue persists, contact UGREEN technical support or try the following:

* Use the ping command to check the connectivity of the NAS device, either via its public IP address or DDNS domain name.
* Review the WebDAV service log files in UGOS Pro to identify potential error messages.
