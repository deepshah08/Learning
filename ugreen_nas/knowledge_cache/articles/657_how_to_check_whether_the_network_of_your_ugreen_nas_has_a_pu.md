# How to Check Whether the Network of Your UGREEN NAS Has a Public IP and Set Up Port Forwarding？

> **Article ID**: `657`  
> **Category**: `Troubleshooting > Network Failure > How to Check Whether the Network of Your UGREEN NAS Has a Public IP and Set Up Port Forwarding？`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/657  

---

## **Check for Public IPv4 Address**

1. Use a phone or computer within the local network to visit websites like [ip138.com] or [IPW.cn] in a browser. The IP address shown on the page is your public IP.
2. Log in to your router’s admin panel and go to the “Internet Info” or “WAN Settings” page to view the WAN IP address.
3. Compare the IP address shown in the browser with the WAN IP in your router: If browser IP = router WAN IP, your NAS is on a network with a public IPv4 address.
4. If the two IPs are different, your current network is using a private IP or has NAT applied by your ISP. You’ll need to contact your ISP to request a public IP.

## **Check for Public IPv6 Address**

1. In the NAS [Network Settings], check the IPv6 address of the LAN network interface. If the address starts with`240e:`(e.g., `240e:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx`), it indicates a public IPv6 address.
2. Visit test websites such as [test-ipv6.com] or [IPW.cn]; the page will display whether your IPv6 connection is functioning properly.

## **Other Notes**

### **Will the Public IP Change?**

* ISPs may change your public IP address periodically. It’s recommended to bind a DDNS (Dynamic DNS) service such as [Aliyun] or [Tencent Cloud] to avoid access issues caused by IP changes.

### **Risks of Public IP Exposure and Protection Measures**

* In a public network environment, exposed ports may be scanned or attacked. It is recommended to change the default NAS port — for example, change the default port (such as 9999) to a less common one (such as 19999).
* Configure a firewall to only allow necessary ports to be exposed externally.

### **How to Set Up Remote Access？**

* If the modem handles the dial-up connection, you need to configure [Port Forwarding] on both the modem and the router.
* If the modem is in bridge mode and the router handles the dial-up connection, you only need to configure [Port Forwarding] on the router.

## **Common Troubleshooting**

### **NAS cannot connect to LAN client devices?**

* Go to your router’s settings page and check whether both the NAS device and the client device IP addresses are visible.

### **Remote access failed?**

* Make sure the router has opened the necessary ports for the NAS (e.g., 8080, 9999) and that the public IP or domain name is correctly bound.

Quick Summary of Steps: Check public IP → Compare with router's WAN IP → Determine whether a public IP is required. For typical home networks, an IPv4 public IP is unlikely, but IPv6 may be available depending on the ISP.
