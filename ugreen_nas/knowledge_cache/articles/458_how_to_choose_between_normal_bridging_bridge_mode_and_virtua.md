# How to Choose Between Normal Bridging (Bridge Mode) and Virtual Bridging (Macvlan Mode)? What’s the Difference Between the Two?

> **Article ID**: `458`  
> **Category**: `Application Guide > Control Panel > FAQ > How to Choose Between Normal Bridging (Bridge Mode) and Virtual Bridging (Macvlan Mode)? What’s the Difference Between the Two?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/458  

---

In the UGOS Pro system on UGREEN NAS, network bridging is a key configuration option within Docker container networking. Whether to choose Virtual Bridging (Macvlan Mode) or Normal Bridging (Bridge Mode) depends on your networking requirements and specific use case. The following explains the differences between the two modes and helps you decide which to use.

### **1. Normal Bridging (Bridge Mode)**

Normal Bridging is one of the most commonly used network modes. It allows containers to share the host’s network interface while remaining isolated from each other. At the same time, they can still communicate with the host.

#### **Features**:

* **Network isolation from the host:** In Bridge Mode, each container has an independent IP address, which is valid only within Docker’s internal network. External networks outside the host cannot directly access the containers.
* **Use case suitability:** This mode is ideal when you do not want containers to be directly exposed to the local network but still need them to communicate with the host and other containers.

#### **Applicable Scenarios:**

* Isolated communication between containers.
* Communication between the NAS host and its containers.

### **2. Virtual Bridging (Macvlan Mode)**

Virtual Bridging (Macvlan) is a more advanced networking mode that allows containers to connect directly to the physical network. In this mode, containers behave like independent devices within the LAN, each with its own IP address, enabling direct communication with other network devices.

#### **Features:**

* **Independent IP addresses:** In Macvlan mode, containers are assigned IP addresses in the same subnet as the host. External devices can access containers as if they were standalone devices.
* **Isolated from the host:** Containers using Macvlan cannot communicate directly with the NAS host, but they can communicate freely with other devices on the LAN.
* **Use case suitability:** Macvlan is ideal when you want containers to act as independent devices and interact directly with external networks—such as other LAN devices or the internet.

#### **Applicable Scenarios:**

* Containers that need to communicate directly with other devices on the local network or be exposed to external networks (such as when running edge computing services like NetHeart Cloud or TianTian) are best suited for Virtual Bridging.
* Virtual Bridging is commonly used to configure a Macvlan network and is especially ideal for running containers like Emby or qBittorrent. This is because Macvlan allows each container to have its own unique IP and MAC address, making the container behave like a standalone physical device on the network. Other network devices can access these containers just like they would access any independent device. In addition, Virtual Bridging allows you to assign individual network policies—such as bandwidth limits—to these containers, greatly enhancing flexibility and network management.

### **Key Differences Between Normal Bridging and Virtual Bridging:**

|  |  |  |
| --- | --- | --- |
| **Function** | **Normal Bridging (Bridge Mode)** | **Virtual Bridging (Macvlan)** |
| **IP Address Allocation** | Containers use internal network IPs | Containers are assigned LAN IPs |
| **Communication with Host** | Host can communicate with containers | Host is isolated from containers |
| **Access by External Devices** | Requires port mapping | External devices can directly access containers |
| **Use Case** | Container isolation, simple internal services | Containers need to communicate with LAN devices |

### **How to Choose:**

* **Choose Normal Bridging:** If the containers only need to communicate with the host or with each other, and do not require direct interaction with other devices on the local network or external networks, Normal Bridging (Bridge Mode) is a simple and effective choice. For example, if your containers only need to exchange data internally or communicate with the NAS host without being exposed to the LAN, normal bridging is sufficient.
* **Choose Virtual Bridging:** If you want your containers to function as independent devices on the local network and communicate directly with other devices—especially when running media services through your NAS—Virtual Bridging (Macvlan Mode) is the better option. For instance, if you're running applications that need to be directly accessible on the LAN (such as Emby, Plex, or other multimedia services), it's recommended to use virtual bridging (Macvlan), so that other devices on the network can easily discover and access these services.
