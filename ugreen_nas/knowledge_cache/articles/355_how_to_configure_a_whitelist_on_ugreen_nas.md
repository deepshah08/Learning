# How to Configure a Whitelist on UGREEN NAS？

> **Article ID**: `355`  
> **Category**: `Application Guide > Control Panel > FAQ > How to Configure a Whitelist on UGREEN NAS？`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/355  

---

If you want to only allow trusted IP addresses to access your NAS and protect your UGREEN NAS from unauthorized access, you can configure a whitelist. Go to [Control Panel] > [Security] > [Security] to set up a whitelist. Read this article to learn how to configure a whitelist on your UGREEN NAS.

## **Configuring a Whitelist**

When setting up security on your NAS, creating a whitelist is an effective way to restrict access so only specific IP addresses or IP ranges can connect to the NAS.

To create a whitelist of trusted IP addresses,

follow these steps:

1. Go to [Control Panel] > [Security] > [Security], click the "Block Management" button, and open the [Block Management] > [Settings] page.
2. Click the "+ New Whitelist" button to create a whitelist entry, and enter the IP address of a single host (for example: 192.168.50.xxx).
3. After setting, click "Confirm" to apply the changes.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250623/a018e7a9-aa72-4796-899b-c1eb3f8090b2.png)

You can configure an IP address range by entering a subnet address and a network prefix length, or by directly entering an IP range.

To create a whitelist entry and add a trusted IP address range,

follow these steps:

1. Go to [Control Panel] > [Security] > [Security], click the "Block Management" button, and open the [Block Management] > [Settings] page.
2. Click the "+ New Whitelist" button to create a whitelist entry, and enter a subnet IP address with a network prefix length (for example: 192.168.1.0/16) or an IP range (for example: 192.168.1.1~192.168.1.10).
3. After setting, click "Confirm" to apply the changes.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250623/36691221-6d33-4bc2-be9b-4f1911744e8d.png)

**Notes**

1. **Confirm the network prefix length:** Make sure you enter the correct network prefix length to avoid unexpected access restrictions.
2. **Regularly review the whitelist:** Check and update the whitelist periodically to ensure only trusted IP addresses can access your NAS.
3. **Combine with other security measures:** Whitelisting is an effective security measure, but it is recommended to use it alongside other security settings (such as firewall rules and user permission settings) to provide multi-layered protection.

———————————————————————————————————————————————————————————————————————————————————————————

**Additional Knowledge:**

**What are a Subnet IP Address and a Network Prefix Length?**

**Subnet IP Address**: A subnet IP address is used to identify the range of IP addresses belonging to a network or subnetwork. It is a standard IPv4 address, such as: 192.168.1.0.

**Network Prefix Length**: The network prefix length is the length of the subnet mask expressed in bits. It determines how many bits of the IP address are used for the network portion. For example, a prefix length of 24 means the subnet mask is 255.255.255.0.

This prefix length determines how many available host IP addresses are within the subnet. When entering an IP address for IPv4, valid prefix lengths range from 1–32. When entering an IP address for IPv6, valid prefix lengths range from 1–128.

#### **Example Explanation**

**IP Address**: 192.168.1.0 — This identifies the network portion of the subnet.

**Network Prefix Length**: 24 — This prefix length corresponds to the subnet mask 255.255.255.0, which means the IP range is from 192.168.1.0 to 192.168.1.255.

#### **Example Configuration**

**IP Address: 10.0.0.0, Prefix Length: 16** — Allowed IP range: 10.0.0.0 to 10.0.255.255

**IP Address: 192.168.0.0, Prefix Length: 24** — Allowed IP range: 192.168.0.0 to 192.168.0.255
