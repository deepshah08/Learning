# Why does the actual transfer speed only reach the network port limit when using SMB mounting over Thunderbolt Direct Transfer?

> **Article ID**: `757`  
> **Category**: `Troubleshooting > Network Failure > Why does the actual transfer speed only reach the network port limit when using SMB mounting over Thunderbolt Direct Transfer?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/757  

---

## Problem Description

When a NAS device is directly connected via a Thunderbolt interface, it should theoretically deliver the high-bandwidth transfer capabilities of the Thunderbolt protocol (typically 20–40 Gbps, depending on hardware). However, when using Samba (SMB protocol) to mount shared directories for file transfer, the speed is capped at the NAS network port's upper limit, failing to leverage the full potential of the Thunderbolt connection.

## Cause Analysis

This issue stems from the interplay between the Samba protocol and the Windows client’s routing priority logic:

**Samba Multi-NIC Announcement & Windows Routing Priority**

● During negotiation, the Samba service announces all active network interface IP addresses on the NAS device (including the Thunderbolt interface IP and regular network port IPs) to the Windows client.

● Windows selects the transfer path based on its system routing table. If the regular network port (e.g., eth0) appears earlier in the announcement list, Windows prioritizes that interface over the Thunderbolt connection.

**Resulting Bottleneck**

● The bandwidth of a regular network port is significantly lower than that of the Thunderbolt interface. Consequently, the actual transfer speed is constrained by the physical bandwidth of the regular network port, rather than utilizing the Thunderbolt link’s full performance.

## Solution

You can disable the SMB3 multichannel feature to prevent Windows from automatically selecting the wrong channel:

1. Open the "Control Panel" application, navigate to "File Service" > "SMB" to enter the SMB page.

2. Click "Advanced" on the page to access the Advanced Settings page.

![](https://file-us.ugreennas.com/admin/article/2025-08-25/d723562127b443c18859efaadbc01df6.webp)

3. On the "General" tab, scroll down to locate the "Enable SMB3 multichannel" option and uncheck it.

![](https://file-us.ugreennas.com/admin/article/2025-08-25/ef5b5cd915a148d4856dc5fe2229cd12.webp)

4. Click "Save", then "Apply".

Once complete, the Windows client will prioritize the Thunderbolt direct link for SMB file transfers, restoring the high-speed performance of the Thunderbolt interface.
