# [FAQ] How to Configure a Macvlan Network in Docker Compose

> **Article ID**: `456`  
> **Category**: `Application Guide > Docker > Docker Gameplay > [FAQ] How to Configure a Macvlan Network in Docker Compose`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/456  

---

Adding a macvlan network in the Docker Compose configuration file allows containers to connect to the physical network, enabling them to communicate with other devices as if they were standalone devices. This network mode is ideal for container applications that require independent IPs, such as services needing to communicate with other devices in the local area network (LAN).

## Scenarios for Using Macvlan:

1. **Services requiring independent IPs**  
For example, edge computing services (like OneThing Cloud, Tiantang) need containers isolated from the host machine and using router-provided public IP services. `macvlan` can provide containers with independent IPs, allowing them to enjoy independent router features like UPnP.

2. **Containers requiring bandwidth management**  
When you need to limit the bandwidth of specific containers through a router, `macvlan` allows the router to treat containers as standalone devices, easily implementing speed limits.

## Example for Configuration

Below is a `docker-compose.yaml` configuration example for an `emby` container, demonstrating how to switch the network from `bridge` mode to using a `macvlan` network.

### Original Configuration File:

```
services:
  emby:
    image: emby/embyserver:beta
    container_name: emby-server
    restart: always
    devices:
      - /dev/dri:/dev/dri
    environment:
      UID: 0
      GID: 0
      GIDLIST: 0
    volumes:
      - ./config:/volume1/docker/emby/config
      - ./metadata:/volume1/docker/emby/metadata
      - /volume2/video:/video2
    ports:
      - 8096:8096/TCP
    network_mode: "bridge"
```

### Modified Configuration File:

```
services:
  emby:
    image: emby/embyserver:beta
    container_name: emby-server
    restart: always
    devices:
      - /dev/dri:/dev/dri
    environment:
      UID: 0
      GID: 0
      GIDLIST: 0
    volumes:
      - ./config:/volume1/docker/emby/config
      - ./metadata:/volume1/docker/emby/metadata
      - /volume2/video:/video2
    ports:
      - 8096:8096/TCP
    networks:
      vlan1:
        ipv4_address: 172.17.20.88

networks:
  vlan1:
    external: true
```

### Key Modifications:

1. **Remove** `network_mode: "bridge"`  
Deleted the`network_mode: "bridge"` since we are switching from `bridge` to macvlan.

2. **Define the macvlan network**  
In the `networks` section, defined `vlan1` and marked it as `external: true`, indicating that Docker will not create a new network but will use the pre-configured macvlan network named `vlan1`.

3. **Assign a fixed IP address to the container**  
Since macvlan networks do not support Docker-assigned IP addresses, we manually specified the IP address `172.17.20.88` for the`emby` container. This IP must be within your LAN subnet to avoid conflicts with other devices.

4. **Ensure the macvlan network is created**  
Before using this configuration, ensure you have created a macvlan network named `vlan1` in **"Docker > Network"**. Without it, the container will fail to start.

## How to Create a Macvlan Network in UGOS Pro System

If the macvlan network named `vlan1` has not been created, follow these steps:

### Open the Docker Application

In the UGOS Pro system, go to the **"Docker"** application, click the **"Network"** tab on the left sidebar, then click the "Add" button to open the network configuration wizard.

### Configure Network Parameters

In the Network Configuration Wizard, follow these steps to configure step-by-step:

● **Network Name:** Specify an easily identifiable and descriptive name for the network, such as `vlan1`. Keep the name concise for easy management and retrieval.

● **Network Mode:** Select `macvlan` as the network mode. Macvlan mode allows containers to directly connect to the physical network and communicate with other devices in the LAN as if they were standalone physical devices.

● **Network Interface Selection:** Choose the physical network interface you wish to use. If it hasn’t been configured yet, go to **"Control Panel > Network Settings > Network Connection"** and set up a virtual bridged network interface.

● **IPV4/IPV6 Configuration:** Set the IP address range and gateway information according to your network needs. If you do not plan to manually configure, you can skip this step.

**IPv4/IPv6 Configuration Parameter Description**

● **IPV4 Subnet Mask (optional):** Enter the subnet mask matching your LAN. For example, a standard home network can use `255.255.255.0`.

● **IPV4 Gateway (optional):** Enter the default gateway of the network, such as `192.168.1.1`, which is usually the IP address of the router connecting to the internet.

● **IPV6 Settings (optional):** If you plan to enable IPV6 functionality in the network, you can manually configure IPV6 address ranges and gateway information. Otherwise, skip this step.

**Note:**

● During the network interface selection step, the network interface must already be set to bridge mode in order to be selectable here.

● The subnet mask and gateway information must be consistent with the existing LAN to avoid issues such as containers failing to join the network or IP conflicts.

### Confirm and Create the Network

After checking all settings, click the **"Confirm"** button to complete the creation of the macvlan network. The network will be displayed in the Docker Networks list for subsequent use.

![](https://file-us.ugreennas.com/admin/article/2025-09-01/17994bb5b6b44de49ce3840787939e5f.webp)

## Notes:

● One physical network interface can only configure one macvlan network. Therefore, if multiple macvlan networks are required, ensure the host NAS has sufficient network interfaces or use virtual network interface bridging.

● When using macvlan, ensure the subnet is consistent with the host to avoid network connection issues.
