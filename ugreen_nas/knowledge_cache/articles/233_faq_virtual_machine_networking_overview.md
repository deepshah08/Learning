# [FAQ] Virtual Machine Networking Overview

> **Article ID**: `233`  
> **Category**: `Application Guide > Virtual Machine > FAQ > [FAQ] Virtual Machine Networking Overview`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/233  

---

What are the differences between Virtio, e1000, and rtl8139, and how should I choose when creating a virtual machine?

Virtio, e1000, and rtl8139 are three different types of virtual network adapters, each with differences in performance, compatibility, and functionality. When creating a virtual machine, you can choose the appropriate network adapter type based on your actual needs and environment.

Differences and selection recommendations:

Virtio:

Performance: Virtio is a high-performance virtual network adapter, typically providing the best performance.

Compatibility: Virtio is suitable for most modern virtualization platforms and has good compatibility in supported operating systems.

Functionality: Virtio supports advanced features such as multi-queue (multi-core processing) and congestion control.

e1000:

Performance: e1000 is a common type of virtual network adapter with stable performance, suitable for most standard scenarios.

Compatibility: e1000 is widely supported across various virtualization platforms and has good compatibility with most operating systems.

Functionality: While e1000 does not support some advanced features, it is sufficient for normal network connections.

rtl8139:

Performance: rtl8139 is a relatively traditional type of virtual network adapter with relatively lower performance, unsuitable for high-performance scenarios.

Compatibility: rtl8139 usually has good compatibility but may be limited on some newer virtualization platforms.

Functionality: It offers basic functionality without support for some advanced features, suitable for simple network connections.

How to choose:

Performance requirements: If you have high-performance requirements for networking, it is recommended to choose Virtio.

Compatibility considerations: If you need to ensure good compatibility across different virtualization platforms and operating systems, you can choose e1000.

Simple application scenarios: For simple network connection requirements, rtl8139 may be sufficient for your needs.

Overall, for most situations, Virtio or e1000 are better choices, while rtl8139 is suitable for specific simple application scenarios.

What are the differences between vnet-bridge, vnet-nat, and vnet-host? How should I choose when creating a virtual machine?

vnet-bridge, vnet-nat, and vnet-host are three different network connection modes, each with differences in how virtual machines communicate with the host and external networks. When creating a virtual machine, you can choose the appropriate network connection mode based on your network environment and requirements.

Differences and selection recommendations:

vnet-bridge (Bridge Mode):

Features: Bridge mode bridges the virtual machine's network interface to the host's physical network interface, allowing the virtual machine to communicate directly with other devices on the LAN as an independent device.

Use: Suitable for scenarios where the virtual machine needs to communicate with other devices on the LAN or needs to run as an independent device in the network.

vnet-nat (NAT Mode):

Features: NAT mode forwards the virtual machine's network traffic to the host's network interface, allowing communication with external networks through the host's network connection. Communication between the virtual machine and external networks is managed and forwarded by the host.

Use: Suitable for virtual machines that need to communicate with external networks but do not need to appear as independent devices on the LAN.

vnet-host (Host Mode):

Features: Host mode directly connects the virtual machine's network interface to the host, allowing direct communication between the virtual machine and the host. However, direct communication with external networks is not possible.

Use: Suitable for scenarios where the virtual machine needs to communicate directly with the host but does not need to communicate directly with external networks.

How to choose:

Communicating with external networks: If the virtual machine needs to communicate with external networks, choose either vnet-bridge or vnet-nat mode, depending on whether the virtual machine needs to appear as an independent device on the LAN.

Communicating with the host: If the virtual machine needs to communicate directly with the host, choose either vnet-bridge or vnet-host mode, depending on whether communication with external networks is necessary.

LAN requirements: If the virtual machine needs to appear as an independent device on the LAN, choose vnet-bridge mode; if the virtual machine only needs to communicate with external networks but does not need to be independent on the LAN, choose vnet-nat mode.

Constructing a Virtual Network Environment: Recommended Pairings of Network Adapters and Connection Modes

In summary, we have learned about the differences between different network adapters (Virtio, e1000, and rtl8139) and connection modes (vnet-bridge, vnet-nat, and vnet-host). When creating a virtual machine, you can flexibly choose the appropriate virtual network adapter type and connection mode based on your network environment, performance requirements, and communication between the virtual machine, external networks, and the host. Here are some recommended pairing schemes:

Virtio + vnet-bridge:

Scenario: When you need the virtual machine to run as an independent device in the LAN and require high network performance.

Features: Virtio provides a high-performance virtual network adapter, and vnet-bridge directly bridges the virtual machine to the host's physical network interface, enabling direct communication between the virtual machine and other devices on the LAN.

e1000 + vnet-nat:

Scenario: When your virtual machine needs to communicate with external networks but does not need to appear as an independent device in the LAN.

Features: e1000 is a stable virtual network

adapter, and vnet-nat forwards network traffic through the host's network connection, ensuring connectivity between the virtual machine and external networks.

rtl8139 + vnet-host:

Scenario: When the virtual machine needs to communicate directly with the host but does not need direct communication with external networks.

Features: Although rtl8139 has lower performance, it is more usable for direct communication with the host, and vnet-host directly connects the virtual machine's network interface to the host, enabling direct communication between the virtual machine and the host.

You can also flexibly combine and choose based on specific circumstances. For example, if you need the virtual machine to communicate with external networks while appearing as an independent device on the LAN, you can choose Virtio + vnet-bridge.

The best combination depends on your specific requirements, including performance needs, network environment, and communication between the virtual machine, external networks, and the host.
