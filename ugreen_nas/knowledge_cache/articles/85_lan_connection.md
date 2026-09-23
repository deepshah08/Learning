# LAN Connection

> **Article ID**: `85`  
> **Category**: `Application Guide > Control Panel > LAN Connection`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/85  

---

You can point the custom domain to your local NAS, eliminating the need to remember the IP address, and directly access it via a browser link.

UGOS Pro supports accessing your local NAS through the browser using the device's IP address and port (e.g., 172.17.10.248:9999) within the LAN. When the IP address is dynamically assigned via DHCP, access failures may occur due to IP changes. It is recommended to enable the [Custom Domain] feature to facilitate device access.

**Custom Domain Access Methods:**

* **Browser:** Use `http://<Custom Domain>.local`
* **PC & Mobile:** Use `http://<Custom Domain>.local:9999`

**Note**: To prevent domain conflicts, manually append port `9999` for custom domain access to ensure successful connections.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250305/adfcd7a8-d469-4294-abcd-ef5f8567a1a0.png)
