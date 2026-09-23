# [FAQ] Docker Network Modes and Their Applications: Bridge, Host, and Macvlan

> **Article ID**: `461`  
> **Category**: `Application Guide > Docker > FAQ > [FAQ] Docker Network Modes and Their Applications: Bridge, Host, and Macvlan`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/461  

---

Docker provides multiple network modes for containers, allowing users to configure container network environments based on different needs. Among them, Bridge, Host, and Macvlan are the three most common modes, each suited to specific application scenarios.

1. Bridge Mode

**Bridge mode** is Docker's default network mode. In this mode, Docker creates a virtual bridge, through which containers communicate. Containers can communicate with each other within the bridge, while communication with the external network relies on NAT (Network Address Translation). Port mapping is used to expose container ports to the NAS host, enabling external access.

**Use case:** Suitable for environments where multiple containers need to communicate with each other but remain isolated from the NAS host network. For example, running a downloader container and exposing it externally via port mapping.

2. Host Mode

**Host mode** allows the container to share the host's network stack directly. The container uses the host's IP address and ports, so there is no need for traffic forwarding via a virtual bridge, resulting in higher network performance. In this mode, no port mapping is required as the container directly uses the host’s network interface.

**Use case:** Ideal for applications with high network performance requirements, such as real-time data processing or streaming services, especially those requiring low latency.

3. Macvlan Mode

**Macvlan mode** assigns each container a unique IP and MAC address, allowing containers to appear as standalone devices on the network. These containers no longer rely on the virtual bridge or the host’s network stack—they have independent network interfaces and IP addresses. This mode is suitable for scenarios where containers need to run as independent devices on the LAN, such as edge computing services or bypass routing devices.

**Use case:** Ideal for situations where containers must operate independently from the host’s network, such as running an OpenWRT bypass gateway or services requiring a dedicated IP (e.g., Qbittorrent).

### **Comparison and Selection of the Three Network Modes**

* Bridge Mode is the best choice if you need to place multiple containers in an isolated environment and manage external access through port mapping.
* Host Mode offers better performance for applications that are highly sensitive to network latency.
* Macvlan Mode is ideal when you want containers to operate as independent devices on the network and require fixed IP addresses.
