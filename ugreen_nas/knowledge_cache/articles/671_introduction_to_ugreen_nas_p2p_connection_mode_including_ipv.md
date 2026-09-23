# Introduction to UGREEN NAS P2P Connection Mode (Including IPv6 Support)

> **Article ID**: `671`  
> **Category**: `Troubleshooting > Network Failure > Introduction to UGREEN NAS P2P Connection Mode (Including IPv6 Support)`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/671  

---

UGREEN NAS now supports P2P (Peer-to-Peer) connection mode, providing users with a stable, secure, and convenient remote access solution. Compared to public IP access, P2P mode eliminates the need to configure DDNS and domain names.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250716/aea5391c-4102-4ba0-a91d-ebd90d899d5f.png)

# **Introduction to P2P Connection Mode**

P2P is a peer-to-peer networking technology that enables direct connections between devices across different network environments by leveraging UGREEN’s official relay service and the device’s local IPv6 NAT traversal capabilities.

Compared to the traditional public IPv4 + port forwarding method, P2P allows for direct connections without exposing IP addresses, ensuring greater privacy and security for remote access.

# **Connection Mechanism**

When the UGREEN NAS client logs into a device using a UGREENlink ID, the system automatically determines whether the current network environment supports establishing a direct P2P connection. If the conditions are met, the NAS and the client will coordinate via the UGREENlink ID to perform NAT traversal and establish a high-speed IPv6 tunnel.

The conditions required to establish a P2P connection are as follows:

|  |  |
| --- | --- |
| **Condition** | **Requirement** |
| **NAS Network Support** | The network connected to the NAS must support public IPv6 access. |
| **Router Port Settings** | Port 9999 must be forwarded to the NAS on the router. |
| **IPv6 Enabled** | Both the NAS and the client must have IPv6 functionality enabled. |
| **UGREEN Account Login** | Both the NAS and the client must be logged in with the same UGREENlink ID. |
| **Client Network Support** | The client must be connected to an IPv6-enabled network (e.g., IPv6 Wi-Fi or 5G). |

When the above conditions are met, the success rate of P2P NAT traversal can be significantly improved. If the conditions for P2P are not met or NAT traversal fails, the system will automatically switch to relay mode to ensure that remote access remains stable and available at all times.

## **Configuring P2P Mode (Using Home Broadband and a Xiaomi Router as an Example)**

1. Enable IPv6 support on the optical modem and set it to bridge mode.
2. Configure the router to use PPPoE for dialing, enable IPv6, and disable the IPv6 firewall. (If you are familiar with IPv6 firewall configuration, you may keep it enabled and set up the appropriate IPv6 forwarding rules.)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250716/c7b9fa70-3b31-49f9-8049-bb018aebe794.png)

3. Configure port forwarding on the router to forward TCP port 9999 to the NAS's internal IP address.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250716/b93df930-3243-4240-814a-a62c459e9739.png)

4. Enable IPv6 on the NAS by going to [Control Panel] > [Network] > [Network Connection]. Edit the current LAN interface, set IPv6 to “Auto”, then save and apply the settings.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250716/f3df12f8-59a1-46ba-80bd-c7ecb87c98f4.png)

5. Switch to a non-local network environment (e.g., turn off Wi-Fi and use a 5G network), then open the UGREEN NAS client.
6. Log in to the NAS using your UGREENlink ID. The system will automatically detect the network environment and attempt to establish a P2P connection.
7. Wait a few seconds and check whether the connection status is displayed as “P2P Connection.”

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250716/47f09326-7388-46cd-a081-c26e2ea0f509.png)

## **Usage Tips**

* If P2P NAT traversal fails, the system will automatically switch to “Relay Connection Mode” to ensure uninterrupted access.
* To improve the success rate of P2P connections, it is recommended to use a public broadband network that supports “IPv6”.
