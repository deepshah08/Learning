# [FAQ] How to Check If Your UGREEN NAS is Assigned a Public IP Address？

> **Article ID**: `496`  
> **Category**: `Application Guide > Control Panel > FAQ > [FAQ] How to Check If Your UGREEN NAS is Assigned a Public IP Address？`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/496  

---

## **Problem**

UGREEN NAS supports multiple remote access methods, including the universal UGREENlink service, public IP addresses, or DDNS domain access to the UGOS Pro system. To verify whether your NAS is on a network with a public IP address, please follow the steps below, along with the relevant considerations.

## **Solution**

**Checking IPv4 Public IP**

1. Check Public IP with Online Tools

   * Open a browser and visit [ipw.cn](http://ipw.cn) to view the device's external IPv4 address.
2. Check Public IP with Router or Modem WAN IP

   * Log in to the management interface of your router or gateway to check the **WAN IP** address.
   * Compare the two addresses:

     + **If they are the same**: The network has a public IPv4 address.
     + **If they are different**: The network may be using NAT (Network Address Translation), indicating there is no public IPv4 address.

**Checking IPv6 Public IP**

1. Open the NAS **Control Panel**, and go to **Network > Network Connection**.
2. Select the LAN interface and check the assigned **IPv6 address:**

   * If the address prefix starts with `240e:`, it indicates a public IPv6 address is being used for external access.
   * If the address starts with other prefixes (e.g.,`fe80::`), it is a private address, which cannot be used as a public IP.

**If a Public IP is Needed**

If your Current Network Does not Have a Public IP and You Need One to Support Remote Access, please Contact Your Internet Service Provider (ISP) to Inquire About the Following Options:

* **Request a public IPv4 address** (if available).
* **Enable IPv6 support**: Many ISPs now offer native IPv6 service, which is recommended for long-term support. For more information, refer to the guide "[How to Enable IPv6 Network Access for Personal Broadband](https://ipw.cn/doc/ipv6/user/enable_ipv6.html)".

**Additional Information**

If Your Network Does Not Have a Public IP, You Can Still Access Your UGREEN NAS Remotely Using the Following Methods:

* **Enable UGREEN link Remote Access Service (Recommended)**

  + If your ISP provides a dynamic public IP, you can enable DDNS to bind a domain name to your dynamic IP, allowing the access address to be updated automatically.
  + Configure port forwarding on your router to forward incoming requests to your UGREEN NAS. For more details, refer to the section [**How to Enable DDNS Support?**](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6OTQsInR5cGUiOiJ0YWcwMDEiLCJsYW5ndWFnZSI6ImVuLVVTIiwiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZUluZm9JZCI6ODgsImFydGljbGVWZXJzaW9uIjoiMS4wIiwicGF0aENvZGUiOiJwcm8wMDEsdXJjYWJpLGZhbDN2bCx0bHY2YTIsN2F5eWl0In0=)
* **Enable Dynamic Domain Name Service (DDNS) + Port Forwarding**

  + If you cannot obtain a public IP, you can use UGREENlink service to enable remote access without a public IP address. For more information, refer to[【FAQ】How to Remotely Access UGREEN NAS via UGREENlink and FAQs?](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTM1NiwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiZW4tVVMiLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0NTQsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250826/80e4cd0b-6fec-43a5-b670-2cb89602f8c8.png)
