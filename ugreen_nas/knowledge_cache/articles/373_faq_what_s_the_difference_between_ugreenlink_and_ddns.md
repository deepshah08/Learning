# [FAQ] What’s the difference between UGREENlink and DDNS?

> **Article ID**: `373`  
> **Category**: `Application Guide > Control Panel > FAQ > [FAQ] What’s the difference between UGREENlink and DDNS?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/373  

---

## **What is UGREENlink?**

UGREENlink is a service designed to let you easily access your NAS device at home via the internet, no matter where you are. It enables seamless data connectivity and remote management. Once UGREENlink is enabled, you can conveniently access your NAS device from your phone or computer. For more details, please refer to: [Enable UGREENlink Service](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmODYifQ==)

## **What is DDNS?**

DDNS (Dynamic Domain Name System) is a service that maps a dynamic IP address to a fixed domain name, allowing you to access your NAS device from anywhere.

For more details, please refer to: [Enable DDNS Support](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmODYifQ==)

## **UGREENlink vs. DDNS**

UGREENlink and DDNS both allow you to remotely access your UGREEN NAS device. While they offer similar functionality, they differ fundamentally in how the network connection is established.

* **UGREENlink：**The UGREEN NAS device connects indirectly via UGREEN cloud servers to UGREEN products (such as UGOS Pro).
* **DDNS：**The device is accessed directly using a personal domain name through dynamic DNS resolution.

**Comparison Between UGREENlink and DDNS**

|  |  |  |
| --- | --- | --- |
| **Feature** | **UGREENlink** | **DDNS** |
| Router Configuration | Not required | Required |
| Setup Complexity | Simple setup | Takes more time to configure |
| Let's Encrypt Certificate | Automatically applied | Needs to be added manually |
| Third-party Certificates | Not supported | Supported |
| Domain Name | UGREENlink provides domain and custom ID | You need to prepare your own domain |
| DDNS Providers | Not required | Currently supported: noip.com, duckDNS, Alibaba Cloud, Tencent Cloud, Peanut Shell |
| Target Users | Beginner users | Advanced users |

**Notes:**

1. To connect to your UGREEN NAS device via DDNS or public IP address (including a specific port such as `https://10.xxx.xxx.xxx:9999`), you must configure port forwarding for the device on your router.
2. When connecting through the UGREENlink server, a Let's Encrypt certificate will be automatically applied.

**Note**

Let's Encrypt Certificate¹: Let's Encrypt is a free SSL/TLS certificate used to encrypt data transmission, ensuring secure connections and website authentication.
