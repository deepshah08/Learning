# How to Run a Container on Docker's Macvlan Network

> **Article ID**: `457`  
> **Category**: `Application Guide > Docker > Docker Gameplay > How to Run a Container on Docker's Macvlan Network`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/457  

---

## What is Macvlan?

In simple terms, Macvlan is a virtual network interface technology on Linux that allows users to create multiple virtual network interfaces on a single physical NIC, with each virtual interface assigned a unique MAC address. These virtual interfaces behave like independent devices on the network. Docker uses Macvlan technology to configure container networks, enabling containers to reside on the same local network as the host machine (such as a NAS).

## When Should You Use Docker's Macvlan?

In certain scenarios, containers require a network environment that is isolated from the host, or they need independent network interfaces to handle specific tasks. In such cases, using Macvlan instead of the `host` mode can be beneficial. Here are some common use cases:

1. **Edge computing service containers (e.g., OneThingCloud, TipTime, etc.):**

These services often require containers to share the host's network environment while also needing a publicly mapped IP address. If using the `bridge` mode, the container runs on Docker’s virtual network and is limited by port mapping, even if the router has a public IP. By using a Macvlan network, the container behaves like an independent device, allowing the router to provide UPnP (Universal Plug and Play) services and bypass port restrictions.

2. **Network traffic control:**

If you want to apply independent bandwidth limitations to a container, Macvlan is a great choice. By treating the container as a standalone device, the router can enforce separate traffic rules without modifying the host NAS's network configuration.

## How to Configure Docker’s Macvlan Network

To configure and use a Macvlan network in Docker, follow these steps:

### Create a Macvlan Network

● **Step 1:** Open the Docker application interface. Click on [Network] > [Add] to enter the "Add Network – Network Configuration" screen.

● **Step 2:** Define a custom network name for easier identification and management later.

● **Step 3:** In the "Network Mode" field, select "Macvlan", and in the "Network Interface Card" field, choose the physical network interface to be used for creating the Macvlan network. If there are no available interfaces, go to [Control Panel] > [Network] > [Network Connection], and click **[Network Bridging]** to configure one.

**Note:**

In the network bridging settings, you can choose between normal bridging and virtual bridging. If you don’t require normal bridging, it is recommended to use virtual bridging. When creating a virtual bridge, select the physical network interface card(s) to be bridged and click "Apply." The system will generate a virtual bridge network interface card. Each physical network interface card can only be associated with one virtual bridge network interface card.

In addition, each physical network interface card can be used to create only one Macvlan network. To create a Macvlan network, the network interface card must already be in bridging mode. If the card is already used by another Macvlan network, it cannot be selected again.

● **Step 4:** Configure the IPv4 and IPv6 addresses for the Macvlan network. By default, an IPv4 address will be assigned automatically, and the network will be set to use the same subnet and gateway as the NAS. If you need to enable IPv6, check the corresponding option and configure the related parameters.

● **Step 5:** After confirming that all settings are correct, click "OK" to complete the creation of the Macvlan network.

### Connecting a Container to the Macvlan Network

● **Step 1:** In the Docker application, click [Container], select the container you want to configure with the Macvlan network, and click "···" > "Edit" to enter the container editing interface.

● **Step 2:** Note: By default, the network mode of an existing container cannot be modified directly. If you wish to proceed, click the "Edit" button in the prompt at the top, then modify the network settings.

![](https://file-us.ugreennas.com/admin/article/2025-09-01/b82147fdb7aa4f229e75daee888fec95.webp)

● **Step 3:** Change the container’s network mode to Macvlan and select the Macvlan network you just created. Once done, click "Save" to apply the changes.

## Related Links

// [How to Configure a Macvlan Network in Docker Compose](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMzYwLCJhcnRpY2xlSW5mb0lkIjo0NTYsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)
