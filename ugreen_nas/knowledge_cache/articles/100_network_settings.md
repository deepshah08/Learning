# Network Settings

> **Article ID**: `100`  
> **Category**: `Application Guide > Control Panel > Network Settings`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/100  

---

In the "**Control Panel**" application, "**Network**" settings are divided into three main pages: General, Network connection, and Data control. Each page provides different functions and configuration options to help you comprehensively manage and optimize your network connections. Below is a detailed description of each page and its related features.

## General

The General page is mainly used to view and edit basic network settings, including the configuration of the default gateway and DNS servers, as well as several advanced options.

![](https://file-us.ugreennas.com/admin/article/2025-12-30/342885f617624bd8bc6c331d5930e9c4.webp)

### View and Edit the Default Gateway

Users can view the currently active IPv4 and IPv6 default gateways. If multiple network connections have obtained different gateway addresses, you can adjust the default gateway by clicking the "**Edit**" button. Network connections can be reordered by dragging them with the left mouse button; the connection with the highest priority (listed first) will be used as the default gateway.

### View and Modify DNS Servers

On the "**General**" page, users can view the configured DNS server addresses. To change the DNS servers, select "**Configure DNS server manually**", enter the new DNS addresses in the DNS field, and then click "**Apply**" to activate the changes.

### Advanced Settings

● **Enable multiple gateways**: Allows multiple gateways to be used simultaneously, improving network redundancy.

● **IPv4 adress is perferred for domain name resolution**: Gives priority to IPv4 addresses during DNS resolution.

● **Enable IP conflict detection**: When enabled, the system automatically detects and reports IP address conflicts.

## Network Connection

In a networked environment, effective management and optimization of network connections are critical to ensuring system stability and performance. UGOS Pro provides a set of powerful network management features that enable users to easily configure and manage network interfaces, link aggregation, and network bridging. The following is a brief overview of these functions.

### Manage Network Interfaces

On the "**Network connection**" page, you can view and manage detailed information about currently connected network interfaces (LAN). By default, IP addresses are obtained automatically via [DHCP (Dynamic Host Configuration Protocol)](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmMzg0In0=) , which is a network protocol for automatic IP address assignment. You may also choose to configure IP addresses manually. By clicking the "**Edit**" button for a network interface (such as LAN1 or LAN2), you can modify its network configuration, including manually setting the IP address, [MTU](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmMzg1In0=) value, and choosing whether to designate it as the default gateway.

**IPv4 and IPv6 Settings**

1. **IPv4**

● **Auto (DHCP)**: The system automatically assigns an IP address.

● **Manual**: If your network service provider specifies a fixed IP address, you can manually enter the required information, including the IPv4 address, subnet mask, gateway, and DNS server.

![](https://file-us.ugreennas.com/admin/article/2025-12-30/d817a59eb1b746ad9fcd8d85b7ad95e8.webp)

2. **IPv6**

● **Auto**: When selected, the system automatically generates an IPv6 address based on LAN Router Advertisements (RA).

● **Close**: Disables IPv6 support for the selected network interface.

● **Manual**: Allows you to manually enter the IPv6 address, prefix length, default gateway, and other related parameters.

![](https://file-us.ugreennas.com/admin/article/2025-12-30/39490168e5824160b3916f0fb0220157.webp)

### Link Aggregation

Configuring link aggregation allows multiple physical network ports to be bundled together, increasing overall network bandwidth and providing redundancy protection (the network remains available if one port fails). This feature requires coordination between the NAS and the network switch (for example, the switch must support the IEEE 802.3ad LACP protocol).

● **Network Environment Requirements**

To ensure proper operation, please confirm that your environment meets the following conditions:

**Interface connections**: All LAN ports used for link aggregation must be connected to the **same VLAN on the same switch**. Cross-VLAN connections are not supported.

**Hardware support**: Your network switch must support link aggregation protocols.

● **Configuring Link Aggregation on the NAS**

Follow the steps below to create an aggregated interface in the UGOS Pro system:

1. Open the "**Control Panel**" app, go to "**Network**"＞"**Network connection**", then click "**Link Aggregation**"＞"**Start**" to enter the link aggregation setup wizard.

![](https://file-us.ugreennas.com/admin/article/2025-12-30/5275475dee3141d789adcab53219db4b.webp)

2. Select the desired link aggregation mode (such as Bond 1, Bond 4, etc.), then click "**Next**".

3. Select the physical network interfaces to be bonded (such as LAN1, LAN2). At least two ports must be selected. Click "**Next**" when finished.

4. Configure the IP address for the virtual network interface. You may choose "**Automatically get network(DHCP)**", or manually configure the IPv4 address, subnet mask, default gateway, and DNS servers.

5. After confirming that all settings are correct, click "**Apply**" to complete the configuration.

● **Configuring the Network Switch**

After completing the configuration on the NAS, the required switch settings depend on the selected aggregation mode:

**Modes that do not require switch configuration**: If you select Bond 1 or Bond 6, no additional configuration on the switch is usually required. Simply connect the network cables.

**Modes that require switch configuration (Bond 0 / Bond 2 / Bond 4)**: If you select Bond 0, Bond 2, or Bond 4, corresponding link aggregation settings must be configured on the switch.

**Notes:**

● Bond 1 and Bond 6 modes appear on the network as "**one logical IP address associated with multiple MAC addresses**". Some routers—especially consumer-grade devices—may incorrectly interpret this as "**an IP address conflict**", which can lead to unstable connections. If this occurs, it is recommended to switch to a different aggregation mode.

● If the switch is not correctly configured for the corresponding LACP or static aggregation mode, network connectivity issues may occur.

● Because configuration interfaces vary significantly among switch manufacturers, please follow the technical guidance or official documentation provided by your switch vendor when performing the setup.

● **DH series** products do not support link aggregation.

### Network Bridging

● **Normal Bridging:** UGOS Pro provides a normal bridging feature that allows multiple network interfaces to be combined into a single logical network. By connecting the UGREEN NAS to external network devices (such as a router) and a computer, the computer can access the internet through the UGREEN NAS while maintaining high-speed data transmission with the NAS.

For Example, If a computer has only one Ethernet cable connected, network bridging allows the UGREEN NAS to act as an intermediary between the computer and the router. This enables the computer connected to the UGREEN NAS via Ethernet to access the internet, while still preserving high-speed data transfer between the computer and the NAS.

● **Virtual Bridging:** Virtual bridging allows virtual machines to be bridged to physical network interfaces, enabling them to access the network directly, just like the NAS. In virtual bridging mode, virtual machines share the same network interface as the NAS and other network devices, allowing them to communicate with external devices such as routers and switches.

![](https://file-us.ugreennas.com/admin/article/2025-12-30/688b5836fa4748448acb77aa01b3381e.webp)

**Note:**

● **Creating a normal bridge**: normal bridging requires at least two wired network interfaces. If you have connected two wired NICs but are still unable to create a bridge, please check whether one of the network interfaces is already occupied by a virtual machine and has been used to create a virtual bridge interface.

● **Creating a virtual bridge**: On devices with dual network interfaces, normal bridging and virtual bridging cannot be used at the same time. This means you must decide which bridging mode to use before creating it and select the network mode that best suits your needs. Be sure to clearly understand the purpose of each network interface in the network settings to avoid connection conflicts or feature failures.

● For instructions on how to configure network bridging, please refer to [What is Network Bridging](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmMzg3In0=) .

## Data Control

On the data control page, users can define data control rules to limit port bandwidth, thereby controlling the inbound or Outbound data of services running on UGOS Pro. This helps prevent certain applications or services from consuming excessive bandwidth.

### Creating a Data Control Rule

1. Open the "**Control Panel**" app, select "**Network**">"Data **control**", then click "**Add**" to open the "**Add data control rules**" window.

![](https://file-us.ugreennas.com/admin/article/2025-12-30/a416c2a1e9924dc5a6f8e2adac46d9df.webp)

2. Select the ports to be controlled. The following three options are supported:

● **All**: Apply bandwidth limits to traffic on all ports.

● **Select a port from the list of built-in services**: Choose ports used by common services (such as SMB or WebDAV) from the list.

● **Custom**: Manually enter specific ports or port ranges for precise control.

If "**Custom**" is selected, you can further configure the following parameters:

● **Port type**: Specifies the direction to which the rule applies, such as source port or target port.

● **Communication protocol**: Specifies the network protocol to which the rule applies, such as All, TCP, or UDP.

● **Port number**: Specifies a single port (for example, `8080`), multiple ports (for example, `80,443,5000`), or a port range (for example, `10000-10100`).

![](https://file-us.ugreennas.com/admin/article/2025-12-30/e37611c33166429d9cba6b07f7e90697.webp)

3. Select the physical network interface to which the rule applies:

● **ALL**: All network interfaces

● **LAN1 / LAN2**: A specific interface

4. Configure the bandwidth limits (Outbound data only):

● **Minimum bandwidth**: Sets the minimum outbound speed for traffic matching the rule. This ensures that the matched traffic is guaranteed at least the specified bandwidth and does not fall below this value.

● **Maximum bandwidth**: Sets the maximum outbound speed for traffic matching the rule. This prevents the matched traffic from consuming excessive bandwidth.

**Note**: "**Outbound data**" refers to data sent from the NAS to other devices.

5. After confirming that all settings are correct, click "**OK**" to complete the creation of the data control rule.

**Explanation: Target Port vs. Source Port**

**Target port (most commonly used):**

● **Definition**: The port on which the NAS service listens. It is the target port that external devices connect to when accessing a service on the NAS. This is typically used to limit the bandwidth of services provided by the NAS.

● **Typical scenarios**: When accessing a website hosted in a container via HTTP, the destination port is commonly **8080**; accessing an SMB (file sharing) service uses destination port **445**; and accessing WebDAV typically uses destination ports **5005** or **5006**.

● Limiting the destination ports allows you to control the outbound bandwidth of these services.

**Source port:**

● **Definition**: The port used by the device that initiates the connection, usually randomly assigned by the client system.

● **Typical scenarios**: When an external computer accesses a NAS service via a web browser, its source port might be `52345` (a random port).

● Source ports change frequently and are generally not suitable as a basis for data control rules unless you clearly know that the client application uses a fixed port.

**How to Choose**

● To limit traffic for a specific service (such as container-based HTTP services, FTP, or SMB), select "**Target port**".

● Unless you have an in-depth understanding of the client’s communication behavior, it is generally not recommended to use "**Source port**".

**Examples**

|  |  |  |  |
| --- | --- | --- | --- |
| **Access Scenario** | **Source Port** | **Destination Port** | **Recommended Data Control** |
| A local computer accesses the Lucky service (port 8080) on the NAS via a browser | 52345 (random) | 8080 | Use a destination port rule to limit outbound data on port 8080 |
| A client mounts a NAS folder using the SMB protocol | 45678 (random) | 445 | Set the destination port to 445 to control file-sharing traffic |

### Enabling and Managing Data Control Rules

● After creating a data control rule, you must select (enable) the rule and click "**Apply**" for it to take effect.

● All created rules can be viewed, edited, or deleted on the "**Data control**" page.

● When multiple rules exist, rules positioned higher in the list have higher priority. You can adjust the order of the rules to ensure that higher-priority rules are placed at the top. The system evaluates and applies rules sequentially based on this order.
