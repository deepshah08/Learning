# Docker Network

> **Article ID**: `291`  
> **Category**: `Application Guide > Docker > Docker Network`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/291  

---

## Manage Docker Networks

On the"**Network**" page, you can view and manage network settings for your containers. The network mode determines how containers connect to external networks and communicate with one another.

## Common Network Modes

Docker supports three main network modes. Choose the one that best fits the intended use:

1. **Bridge**

Bridge is the default Docker network mode. Docker creates an isolated virtual network for the container. To make a container service accessible from outside this network, configure **port mapping**. For example, map port 8080 in the container to port 80 on the NAS.

Mapped ports can be changed as needed. Container services, such as web interfaces, can then be accessed using the following address format:NAS IP address:port

2. **Host**

In Host mode, the container shares the NAS network directly and uses the NAS IP address. If IPv6 is available on the NAS, the container can also connect over IPv6.

3. **Macvlan**

Macvlan assigns the container its own MAC address and LAN IP address. This allows the container to appear as a separate device on the local network and communicate directly with other devices without NAT.

This mode is suitable when a container needs a dedicated static IP address or when port conflicts need to be avoided.

## Manage Network Configurations

The following actions are available on the "**Network**" page:

● Click "**+ Add**" to create a custom network, such as a Macvlan network, for specific networking requirements.

● Select a network, then click "**View**" to check details such as its subnet and gateway.

● To remove a custom network that is no longer needed, select it and click "**Delete**".

**Note**: Default system networks cannot be deleted.

## Macvlan Networks

Macvlan assigns each container its own LAN IP address, which helps eliminate port conflicts. Follow the steps below to configure and use a Macvlan network.

### Create a Macvlan Network

Before using Macvlan, create a Macvlan network first.

1. Go to "**Network**" and click "**+ Add**" to open the network configuration wizard.

![](https://file-us.ugreennas.com/admin/article/2026-06-25/01f5653c149e4249a06b7648d97b1e37.webp)

2. Enter an easy-to-identify network name, such asmacvlan\_net）。

3. Under "**Mode**", select "**macvlan**".

4. Select the physical network card to use for the network.

5. IPv4 settings are assigned automatically based on the selected network card by default. To enable IPv6, select "**Enable**" under "**IPv6 Configuration**" and complete the required settings.

6. Review the configuration, then click "**Confirm**".

![](https://file-us.ugreennas.com/admin/article/2026-06-25/f62fdd791ab24ed08f84ca712d06939c.webp)

**Note**: Each physical network card can be used to create only one Macvlan network. If no network card is available, go to "**Control Panel**">"**Network**">"**Network connection**" and check whether the network port is already being used by "**Network bridging**".

### Configure a Container to Use a Macvlan Network

After creating a Macvlan network, assign it to a container as follows:

1. In the "**Container**" list, find the target container, then click "**…**">"**Edit**".

2. Editing is locked by default. In the message at the top of the page, click "**Edit**" to unlock the settings.

![](https://file-us.ugreennas.com/admin/article/2026-06-25/93694abb990f4e7dbe3194e4ea0fa42e.webp)

3. Set the network mode" to "**macvlan**".

4. From the **"Network"** drop-down list, select the Macvlan network created earlier, then assign the container a static **IPv4 address**.

> Make sure the IP address is not already in use by another device on the local network.

![](https://file-us.ugreennas.com/admin/article/2026-06-25/9141097275c04e938994bb5363361e26.webp)

5. Click **"Save"**. After the container restarts, it will use the new dedicated IP address.

## Notes

● Containers created through **"Project"** using Docker Compose cannot have their network settings changed directly from the container page. To assign a Macvlan network, manually edit the Compose configuration for the corresponding project.

● Container apps installed directly from **"App Center"** cannot be switched to Macvlan mode.

![](https://file-us.ugreennas.com/admin/article/2026-06-25/fa6576512c144b9787fc53a154dbec12.webp)
