# How to Configure a DDNS Domain Name to Log In to UGREEN NAS?

> **Article ID**: `862`  
> **Category**: `Application Guide > Control Panel > How to Configure a DDNS Domain Name to Log In to UGREEN NAS?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/862  

---

### Applicability

**Applicable Clients:** UGREEN NAS PC Client (Windows/macOS)

**Applicable Version:** NAS firmware 1.16.0.0042 or later

**Requirements:** A home broadband network with a public IPv4 or public IPv6 address, and a DDNS domain name.

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

### App Overview

When you are away from home, such as at the office, traveling, or using a mobile network, you can configure "**DDNS+router port forwarding"** to access files and apps on your UGREEN NAS remotely through a direct connection without relay speed limits.

### Why Choose DDNS

Compared with the UGREENlink relay service, DDNS can provide significantly faster remote access:

● **Direct NAS access:** DDNS connects your remote device directly to the NAS through a peer-to-peer (P2P) connection instead of routing traffic through UGREEN relay servers.

● **Faster transfer speeds:** Transfer speeds are no longer limited by the bandwidth of the official servers. Instead, they depend on the **bandwidth available on the network where your NAS is located** (such as the upload bandwidth provided by your ISP), which can provide faster upload and download speeds.

**Note:** Actual speeds may still vary depending on the network you are using and whether your broadband provider applies cross-network or cross-region transmission restrictions.

### Check for Public IP Address

Before making any network-related changes, make sure your network supports direct remote access.

1. Open <https://test-ipv6.com/index.html.en_US>Firefox on the NAS or in a browser on a computer connected to the same LAN.

2. If the page shows "**have IPv6 Internet access**", your network supports public IPv6 access and you can use IPv6 for the remaining configuration.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/5153e19164514834bff3771001ea4b28.webp)

3. Log in to the admin page of your home router, locate the WAN IP address, and compare it with the IP address shown on <https://test-ipv6.com/index.html.en_US>.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/526e96155e1945aa9dd05d527caba6d1.webp)

**If the two IP addresses match**, you have a native public IP address and can continue with the setup. **If they do not match**, your network is behind your ISP's NAT. Contact your broadband provider for assistance.

### Purchase a Domain Name and Configure DDNS for the NAS

Because your public IP address may change when the router restarts or your ISP refreshes the address, you need to bind a fixed domain name to the NAS. The following example uses Cloudflare (CF).

1. Log in to [Cloudflare](https://dash.cloudflare.com/) , and click "**Domain registration">"Register domains**" in the left sidebar to search for and purchase a domain name.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/4cb9a91b95ce4b0085a0efbaa8883a1e.webp)

2. Return to the Cloudflare dashboard and click the domain you just purchased. Find the Account **ID** on the right side of the page and copy it for later use. (This ID corresponds to the *AccessKey ID* in UGREEN NAS.)

3. Click "**Get your API token**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/71d642afa96b4dfd9265cc9909683e6f.webp)

4. Click "**Create Token**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/752b876c48d24e588a0e6c744525f35d.webp)

5. Find the "**Edit zone DNS**" template and click "**Use template**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/77dbe764e12d4c4980e463a498100cd9.webp)

6. Under "**Zone Resources**", select the domain you just purchased and click "**Continue to summary**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/a523c3e38deb45a1a65c404ce3af38aa.webp)

7. Click "**Create Token**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/a889b2bb0ff54cc8b8d695ae3d250051.webp)

8. Click "**Copy**" to copy the token. (This token corresponds to the *AccessKey* *Secret* in UGREEN NAS.)

![](https://file-us.ugreennas.com/admin/article/2026-09-15/9f9a9bb6126a40caa0047efa37f7502c.webp)

### Bind DDNS in UGREEN NAS

1. Log in to UGREEN NAS, open "**Control Panel**", and click "**Device Connection**".

2. Switch to the "**Remote access**" tab at the top.

3. Find and check "**Enable DDNS support**", then click "**Add**" below.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/4bcdd5695ee44ea983379220c8c8186d.webp)

4. Select the platform where you purchased the domain name as the service provider, then enter the required key and domain information according to the provider's requirements.

5. When finished, click "**Connection test**". Once the connection status shows "**Normal**", click "**Apply**" to save the settings. The NAS will automatically update the domain name with your latest public IP address in the background.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/af5bdd8938744fdc86201942cdb1cfe1.webp)

### Router Configuration

To access the NAS from an external network, external access requests must pass through the router and be forwarded to the specified NAS device. Complete the following configurations:

● Assign a fixed local IPv4 address to the NAS

● Configure a port forwarding rule for the NAS

This guide uses the Verizon 5G Home Gateway as an example to introduce the required router-side configurations.

### Assign a Fixed Local IP Address to the NAS

After assigning a fixed IPv4 address to the NAS on the LAN, the NAS local IP address and port forwarding rule will remain valid even after the router or NAS restarts.

1. Log in to the router admin page, click "**Advanced**">"**Network Settings**">"**IPv4 Address Distribution**", then click "**Connection List**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/3db7a996d95d454ebda72bc76ee2622b.webp)

2. View and record the IP information of the target device.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/e0bd1dedf5f94fe7b18926d4aaccb20a.webp)

3. On the DHCP Connection Settings page, select **Static Lease Type** and enter the IP information of the target device recorded earlier.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/48820cad974d4cb09e37b0ba885bb3b8.webp)

4. Click "**Apply**" to save the settings.

**Note:**

● After the configuration is complete, the currently displayed IPv4 address will be permanently assigned to the device. You can then use this IP address for port forwarding configuration.

● Router admin pages and feature names may vary slightly by brand. If you cannot find the corresponding option, refer to the router user manual or contact the router manufacturer's technical support.

### Configure Port Forwarding

1. Log in to the router admin page and click "**Security & Firewall**">"**Port Forwarding**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/1cecb9f2b7934137b6946e5e0ee5c0e5.webp)

2. Click "**Add to list**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/6d74ed14095a4118bd8d65f7f7d84dd6.webp)

3. Enter the port forwarding parameters:

● Service Name: Custom service name, such as UGREEN NAS.

● Original Port / External Port: The port used for external access, such as 9999.

● Protocol: Select TCP.

● Forward to Address: Enter the fixed local IP address reserved for the NAS, such as 192.168.1.154.

● Forward to Port / Internal Port: Enter the actual port used by the NAS service, such as 9999.

● Schedule: Select Always.

After entering the information, click "**Apply Changes**" to save.

### External Access and Troubleshooting

After configuring port forwarding, you can access the NAS from an external network using the DDNS domain name and external port. Use the following format:

http://your-DDNS-domain:external-port

Example:

http://myNAS123.com:9999

The port number must match the external port configured in the router's port forwarding rule.

### FAQs

#### Q: What Should I Do If I Still Cannot Access the NAS from an External Network After Configuring Port Forwarding?

Check the following:

● Whether DDNS resolution is working properly

● Whether the correct public IP address type is selected

● Whether your Internet service provider or firewall restricts the relevant port

#### Q: What Should I Do If the NAS Cannot Be Accessed After the Router or Device Restarts?

Check whether the device's local IPv4 address has changed.

If the local IP address changes, the original port forwarding rule will become invalid.  
We recommend assigning a fixed local IPv4 address to the device before configuring port forwarding.

### Notes

● For security reasons, only open the ports that are actually required. Do not expose all router ports directly to the NAS.

● Port forwarding configuration paths may vary depending on the router brand, model, and firmware version. Refer to the router's actual interface and official documentation.
