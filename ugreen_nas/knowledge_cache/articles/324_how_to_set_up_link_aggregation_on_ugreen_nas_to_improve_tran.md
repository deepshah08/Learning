# How to Set Up Link Aggregation on UGREEN NAS to Improve Transfer Speed？

> **Article ID**: `324`  
> **Category**: `Application Guide > Control Panel > FAQ > How to Set Up Link Aggregation on UGREEN NAS to Improve Transfer Speed？`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/324  

---

## Applicability

**Applicable Clients:** UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version:** NAS firmware 1.16.0.0042 or later

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

UGREEN NAS supports Link Aggregation, which combines multiple physical network interfaces into a single logical interface to increase overall network bandwidth. Some aggregation modes also provide link redundancy, allowing other links to maintain the network connection if one link fails and improving connection reliability.

**Note:** Link Aggregation increases overall bandwidth and multi-task transfer capacity. It does not mean that every individual transfer task will achieve proportionally higher speeds. Actual performance depends on factors such as the number of clients, transfer protocols, switch configuration, and network environment.

## Access Link Aggregation

You can configure Link Aggregation from the following path:

1. Open "**Control Panel**" and click "**Network**" > "**Network Connection**".

2. Click "**+ Link Aggregation**" to open the setup wizard.

![](https://file-us.ugreennas.com/admin/article/2026-09-10/9c02a1b021f84e78a918017e1187071b.webp)

## Prerequisites

Before configuring Link Aggregation, make sure that:

The NAS has multiple available LAN interfaces.

You have enough network cables to connect the NAS to the switch.

If you plan to use an aggregation mode that requires switch support, make sure the switch supports the corresponding feature, such as IEEE 802.3ad (LACP, Link Aggregation Control Protocol).

You understand the Link Aggregation modes supported by your switch and how to configure them.

Link Aggregation support and setup procedures may vary by switch brand and model. Refer to the switch manufacturer's documentation or contact their technical support for configuration guidance.

## Supported Link Aggregation Modes

● Adaptive Load Balancing (Bond6): Automatically distributes traffic to balance the load and provide failover. No switch support is required.

● Active/Backup (Bond1): Only one interface is active at a time, while the others serve as backups for redundancy. No switch support is required.

● Round-Robin (Bond0): Sends traffic through each interface in turn for basic load balancing. Manual configuration is required, and the switch must support this mode.

● Balance XOR (Bond2): Distributes traffic based on MAC address hashes, keeping traffic between the same pair of devices on the same link. The switch must support this mode.

● Dynamic Link Aggregation (LACP) (Bond4): Supports IEEE 802.3ad for automatic negotiation and dynamic link aggregation. The switch must support this mode.

## Set Up Link Aggregation

1. Open "**Control Panel**" and click "**Network**" > "**Network Connection**".

2. Click "**+ Link Aggregation**" to open the setup wizard, then click "**Start**".

![](https://file-us.ugreennas.com/admin/article/2026-09-10/0931dcaea29e4502a3ccb587310580d8.webp)

3. Select a Link Aggregation mode, such as "**Adaptive load balancing - bond6**", then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-09-10/956552143c5f4b92aedb9892e0eea512.webp)

4. Select the LAN interfaces you want to aggregate, then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-09-10/202c0f295c5e4b09941e564e13fbd148.webp)

5. Configure the IP address, then click "**Apply**" to complete the setup.

![](https://file-us.ugreennas.com/admin/article/2026-09-10/b69a2af630db4363b2c1d6aa1798c985.webp)

Once created, the new Bond virtual interface appears in the Network Connection list. You can edit or unbind the interface from this page later.

![](https://file-us.ugreennas.com/admin/article/2026-09-10/b4a85969f2b54bd2ba9255f8d9bb8064.webp)

## FAQs

### Q1: What Should I Do If I Cannot Access the NAS After Setting Up Link Aggregation?

Check the following:

● Make sure the switch configuration matches the aggregation mode selected on the NAS.

● Make sure the selected LAN interfaces are on the same subnet.

● Make sure the NAS IP address or MAC address is not bound on the router.

### Q2: What Should I Do If the Connection Becomes Unstable After Enabling Link Aggregation?

Make sure the selected physical interfaces are connected to the same switch that supports Link Aggregation and are on the same LAN.

### Q3: What Should I Do If Bandwidth Does Not Improve Noticeably After Setting Up Link Aggregation?

Link Aggregation performance depends on the clients, transfer protocols, and traffic distribution mechanism.

Not every individual task can use the full aggregated bandwidth. To evaluate the overall bandwidth improvement, try using multiple clients or running multiple transfer tasks at the same time.

## Notes

● A brief network interruption may occur while creating or deleting a Link Aggregation group.

● After Link Aggregation is enabled, network rules configured on the original interfaces, such as firewall or traffic control rules, will be cleared. Reconfigure them as needed.

● The selected LAN interfaces must be on the same subnet. Otherwise, network communication may be affected.

● After enabling Link Aggregation, do not bind the NAS IP address or MAC address on the router, as this may prevent access to the NAS.

● Before changing the router or subnet, we recommend switching the network settings back to DHCP (automatic).

● If the configuration is incorrect or the device becomes inaccessible, you can restore the network to DHCP by performing a factory reset. A factory reset is a high-risk operation. Proceed with caution.
