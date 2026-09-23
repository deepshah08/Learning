# How to Add a Virtual Network for a Virtual Machine

> **Article ID**: `910`  
> **Category**: `Application Guide > Virtual Machine > How to Add a Virtual Network for a Virtual Machine`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/910  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS).

**Applicable Version**: NAS Firmware 1.18.0.0073 or later.

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

The Virtual Machine app supports creating virtual networks. After a virtual network is created, you can select it in the virtual machine configuration, allowing the virtual machine to access the NAS or external networks according to the specified network mode.

On the **Add network** page, you can create the following types of virtual networks:

● **NAT Mode**

● **Host-only Mode**

Different network modes are suitable for different scenarios. Before creating a network, select the appropriate mode based on whether the virtual machine needs to access external networks.

## Access

1. Open the Virtual Machine app and click "**Network**" in the left sidebar.

2. Click "**Add network**" to enter the network creation page.

![](https://file-us.ugreennas.com/admin/article/2026-07-27/3adbc4d2df324af6a40159a9e3611aa2.webp)

## Add a Virtual Network

Follow the steps below:

1. Enter a name for the virtual network in **Name**.

2. Select a network mode in **Mode**.

3. Select the host network to use in **Map physical network**.

4. Enable or disable **IPv4** and **Auto assignment** as needed.

5. If Auto assignment is disabled, manually enter the Subnet, Gateway, and DHCP address range.

6. Enable or disable **IPv6** as needed.

7. Click "**Confirm**".

![](https://file-us.ugreennas.com/admin/article/2026-07-27/f8ecdc8a2ec74f0cbc3de2a3ba2a3f8c.webp)

After creation, the virtual network will be displayed in the network list. When creating or editing a virtual machine, you can select this virtual network.

## Page Options

### Name

Used to identify the virtual network, for example:

● `vnet-nat`

● `vnet-host`

● `test-network`

### Mode

Used to select the working mode of the virtual network.

● NAT Mode: Forwards the virtual machine's network traffic to the host machine's network interface and enables communication with external networks through the host machine's network connection. Communication between the virtual machine and external networks is forwarded and managed by the host machine.

● Host-only Mode: Directly connects the virtual machine's network interface to the host machine. The virtual machine and the host machine share the same network interface. The virtual machine can communicate directly with the host machine but cannot communicate directly with external networks.

### Map physical network

Used to select the host network associated with the virtual network. If the NAS has multiple network interfaces, select the network interface currently in use.

### IPv4 Configuration

When enabled, IPv4 network parameters can be configured for the virtual network.

### Auto assignment

When "**Auto assignment**" is enabled, the system automatically assigns a fixed subnet, gateway, and DHCP parameters. After creation, you can view the actual parameter values.

If there are no special network planning requirements, enabling Auto assignment is recommended. When "**Auto assignment**" is disabled, network parameters must be entered manually. When configuring parameters, avoid conflicts with the subnet of the current local network or other virtual networks.

### Subnet

Used to set the IP address range of the virtual network. For example: `192.168.1.0/24`, When setting manually, make sure that the subnet is not used by other networks.

### Gateway

Used to set the gateway address of the virtual network. For example:`192.168.1.1`. The gateway address must be within the subnet range. It should also avoid conflicts with the DHCP address range.

### DHCP

Used to set the IP address range automatically assigned to virtual machines. Enter the DHCP start IP and end IP. After connecting to this network, virtual machines can automatically obtain an IP address from this range.

### IPv6 Configuration

To use IPv6, enable **IPv6** configuration. The available configuration options may vary depending on the options displayed on the page.

## Notes

● If you are unfamiliar with subnet, gateway, and DHCP settings, enabling "**Auto assignment**" is recommended. Before manual configuration, check the subnets of the current local network and existing virtual networks to avoid IP conflicts.

● When manually configuring IPv4 parameters, avoid conflicts with existing local network subnets.

● The DHCP start IP and end IP must be within the same subnet.

● It is not recommended to set the gateway address within the DHCP allocation range.

● After creating a virtual network, you need to select this network in the virtual machine configuration before the virtual machine can use it.

● Page names and configurable options may vary slightly between different system versions. Refer to the actual page display.
