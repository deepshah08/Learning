# Remote Access

> **Article ID**: `86`  
> **Category**: `Application Guide > Control Panel > Remote Access`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/86  

---

### Applicability

**Applicable clients**: UGREEN NAS desktop app (Windows/macOS)

**Applicable version**: NAS firmware 1.16.0.0042 or later.

This article is for reference only. The actual interface and operation path may vary slightly depending on your system or app version. Please refer to the actual interface.

### Overview

**Remote access** makes it possible to open and manage your UGREEN NAS from outside your local network, such as when the computer or device in use is not connected to the same network as the NAS. UGREEN NAS supports **UGREENlink** and **DDNS** for remote access. After setup, access the NAS by entering the custom domain name in a browser.

**There are two ways to enable remote access:**

1. Create a custom ID or address with **UGREENlink**.

2. Set a hostname for the NAS IP address using **DDNS**.

### Enable UGREENlink Remote Access

UGREENlink is a remote access feature provided by UGREEN NAS. It allows a NAS at home to be accessed from a phone, computer, or web browser anytime and anywhere. Unlike traditional remote access methods, UGREENlink does not require a public IP address or complex port forwarding, making remote access much easier to set up and use.

1. Open "**Control Panel**" on the UGREEN NAS, then go to "**Device Connection**">"**Remote access**".

2. Turn on **"UGREENlink remote access**". When prompted to verify the UGREEN Cloud account, click "**OK**".

![](https://file-us.ugreennas.com/admin/article/2026-06-08/d0189648bb4e4b2a9cd3c029e036dcb2.webp)

3. Sign in with your UGREEN Cloud account and password. If you do not have an account yet, click "**Register**" to create one, then sign in.

**Note**: For better remote access security, it is recommended to set a strong password for the NAS account.

![](https://file-us.ugreennas.com/admin/article/2026-06-08/533f0701d9ec493f948eedd3fafb324e.webp)

4. After signing in, enter a custom ID in the "**UGREENlink ID**" field, then click "**Apply**" to save.

5. After the ID is verified, the system will generate a web access link and a client ID.

![](https://file-us.ugreennas.com/admin/article/2026-06-08/d174dccdcb524547b14efabf51225194.webp)

#### Access the NAS from a Browser

The NAS system can be accessed remotely by entering the UGREENlink web access link in a browser.

Steps**：**

1. Go to "**Control Panel**">"**Device Connection**" and make sure "**UGREENlink remote access**" is enabled.

For example, if the "**UGREENlink ID**" is set to myNAS123, the web access link will be:

https://ug.link/myNAS123

2. Open a browser on your computer and enter the generated web access link in the address bar.

3. Press "**Enter**". Once the "**UGREENlink ID**" is verified, the "**UGOS Pro login page**" will open.

4. Enter the username and password created on the NAS. Once signed in, files on the NAS can be accessed and managed.

![](https://file-us.ugreennas.com/admin/article/2026-06-08/6d1462f1eb2d41879efedfa467da36c6.webp)

Once signed in, you can access and manage files on your UGREEN NAS.

#### Access the NAS from the Client

The NAS system can also be accessed remotely by entering the "**UGREENlink ID**" in the client.

**Steps：**

1. Download and install the UGREEN NAS client on a PC, or install the UGREEN NAS app on a mobile device.

2. Open the client. On the login page, enter the "**UGREENlink ID**" that was set earlier.

3. Enter the username and password created on the NAS, then click "**Login**". The system will verify the account information.

4. Once signed in, you can access and manage files on your UGREEN NAS.

**Example：**

![](https://file-us.ugreennas.com/admin/article/2026-06-08/9bb4ea175cbe410e984fb55050913dcd.webp)

### Enable DDNS Support

To access your UGREEN NAS at home from an external network, such as from the office, while traveling, or over a mobile network, configure **DDNS** and set up **port forwarding** on the router. This allows direct remote access to files and applications without relying on relay access or speed limits.

### Why Choose DDNS?

Compared with UGREENlink's official relay service, DDNS can offer a significant speed advantage:

● **Direct NAS access:** With DDNS, remote access no longer goes through UGREEN's relay servers. Instead, the remote device connects directly to your NAS through a peer-to-peer (P2P) connection.

● **Faster transfer speeds:** Transfer speeds are no longer limited by the bandwidth of UGREEN's relay servers. Instead, they depend mainly on **the network where your NAS is located**, such as the upload bandwidth provided by your ISP. This usually delivers a faster download and upload experience.

**Note:** Actual speeds may still vary depending on the current network environment and whether the broadband provider applies cross-network or cross-region transmission restrictions.

### Check for a Public IP Address

Before making any network-related changes, confirm that the network supports direct remote access.

1. Open <https://test-ipv6.com/>in the Firefox browser on the NAS, or in a browser on a computer connected to the same local network.

2. If the page indicates that **IPv6 is available**, the network supports public IPv6 access. IPv6 can then be used for the remaining setup.

![](https://file-us.ugreennas.com/admin/article/2026-06-08/a98f53c6d52e4726847eb7d80d31e8b8.webp)

3. Sign in to the admin page of the home router, find the WAN port IP address, and compare it with the IP address obtained from <https://test-ipv6.com/>.

![](https://file-us.ugreennas.com/admin/article/2026-06-08/5c4c8813c64648a7bf692616324ad66d.webp)

**If the IP addresses match**, a native public IP is available and the setup can continue. If they do not match, the network is behind the carrier's NAT. In this case, contact the broadband provider, such as China Telecom, China Unicom, or China Mobile, for assistance.

### Purchase a Domain Name and Configure DDNS for the NAS

Because the public IP address may change after the router restarts or the ISP refreshes it, a fixed domain name needs to be bound to the NAS.

#### Option: Cloudflare (CF)

1. Sign in to [Cloudflare](https://dash.cloudflare.com/) , then go to "**Domain registration**">"**Register domains**" in the left sidebar to search for and purchase a domain name.

![](https://file-us.ugreennas.com/admin/article/2026-06-08/531491a4efc0402d8108a5f12107ee47.webp)

2. Return to the Cloudflare dashboard and select the domain name you just purchased. Find the "**Account ID**" on the right side of the page, then copy and save it. This ID corresponds to "**AccessKey ID**" in the UGREEN NAS system.

3. Click "**Get your API token**" below.

![](https://file-us.ugreennas.com/admin/article/2026-06-08/544bbc4b5cc34c0f87be37f36a3d8a52.webp)

4. Click "**Create Token**".

![](https://file-us.ugreennas.com/admin/article/2026-06-08/5b3bc27ecc6749a198416ff7f87f8845.webp)

5. Find the "**Edit zone DNS**" template and click "**Use template**" on the right.

![](https://file-us.ugreennas.com/admin/article/2026-06-08/5dac028da2234321898b3f5357f070f1.webp)

6. Under "**Zone Resources**", select the domain name you just purchased, then click "**Continue to summary**".

![](https://file-us.ugreennas.com/admin/article/2026-06-08/6056146aa598450f90952f53b7f0448e.webp)

7. Click "**Create Token**".

![](https://file-us.ugreennas.com/admin/article/2026-06-08/3ef4bfd04918461a8c9170114cc78e4c.webp)

8. Click "**Copy**" to copy the token. This token corresponds to "**AccessKey Secret**" in the UGREEN NAS system.

![](https://file-us.ugreennas.com/admin/article/2026-06-08/19481147fd4247d690a081d54622ff2a.webp)

### Bind DDNS in UGREEN NAS

1. Sign in to the UGREEN NAS system, open "**Control Panel**", and click "**Device Connection**".

2. Switch to the "**Remote access**" tab in the top bar.

3. Find and select "**Enable DDNS support**", then click "**Add**" below.

![](https://file-us.ugreennas.com/admin/article/2026-06-08/1eeff50545d24e289986082c9fce051b.webp)

4. Select the service provider for the domain name, then enter the required key and domain information according to the parameter requirements provided by the service provider.

5. After completing the settings, click "**Connection Test**". When the connection status shows "**Normal**", click "**Apply**" to save. The NAS will automatically update the changing public IP address to the domain name in the background.

![](https://file-us.ugreennas.com/admin/article/2026-06-08/047377b0bad34de7ac08c0ddcc4c4cf7.webp)

### Router Configuration

To allow external network access requests to pass through the router and reach the specified NAS device, two router-side settings are usually required. The following example uses the **Verizon 5G Home Gateway**:

1. Configure port forwarding, also known as port mapping.

2. Reserve a Local IP Address for the NAS

#### Reserve a local IP address for the NAS.

To prevent the NAS local IP address from changing after the router or NAS restarts, we recommend reserving a fixed local IP address for the NAS on the router. This helps ensure that the port forwarding rule always points to the correct NAS device.

General steps:

1. Connect your computer or phone to the Verizon 5G Home Gateway network.

2. Open a browser and log in to the router admin page. Common login addresses may include http://192.168.1.1 or http://my.router.

3. Log in with the router admin password. The admin password is usually printed on the Verizon gateway label.

4. Go to Advanced > Network Settings > IPv4 Address Distribution, then click Connection List.

![](https://file-us.ugreennas.com/admin/article/2026-06-08/6fbe8d8c767c46e8919b32ea1ffa0857.webp)

5. Locate the NAS and note its current local IP address and MAC address.

![](https://file-us.ugreennas.com/admin/article/2026-06-08/7338ae6047734ce08e3938cfa9bdbbb1.webp)

6. On the DHCP Connection Settings page, select the Static Lease Type checkbox, then enter the static IP address you want to assign to the NAS.![](https://file-us.ugreennas.com/admin/article/2026-06-08/80cc177503754568b64ede450d790e17.webp)

7. Click Apply to save the settings.

After this is configured, the router will always assign the same local IP address to the NAS. This prevents the port forwarding rule from becoming invalid due to an IP address change.

Please note that the menu names may vary depending on the router model and firmware version. If you cannot find the exact same menu, please look for similar options such as LAN, DHCP, IPv4 Address Distribution, Address Reservation, Static DHCP, or IP Reservation.

#### Configure Port Forwarding

After reserving the NAS local IP address, you need to create a port forwarding rule on the router. This rule tells the router which external port should be forwarded to the NAS inside your local network.

General steps:

1. Log in to the Verizon 5G Home Gateway admin page.

2. Go to Security & Firewall > Port Forwarding.

![](https://file-us.ugreennas.com/admin/article/2026-06-08/270a6e64630c47249f6aafbc040e92bb.webp)

3. Click Add to list.

![](https://file-us.ugreennas.com/admin/article/2026-06-08/2b8c9a1c97044b598de258261a05f36e.webp)

4. Enter the required information:

Service Name: Custom name, such as UGREEN NAS.

Original Port / External Port: The external access port, such as 9999.

Protocol: TCP, or TCP/UDP if required.

Forward to Address: The reserved local IP address of the NAS, such as 192.168.1.154.

Forward to Port / Internal Port: The actual NAS service port, such as 9999.

Schedule: Always.

1. Save the rule.

2. Click Apply Changes to make the rule take effect.

Example:

External Port: 9999

Protocol: TCP

Forward to Address: 192.168.1.154

Forward to Port: 9999

Schedule: Always

This means that when an external request reaches the router on port 9999, the router will forward the request to the NAS at 192.168.1.154:9999.

**Notes**

Port forwarding requires a reachable public IP address. If the internet connection is behind carrier-side NAT, double NAT, or does not provide a public IPv4 address, external access through port forwarding may not work even if the router rule is configured correctly.

#### UPnP Automatic Port Mapping

Not recommended to enable

### Use a DDNS Domain Name to Log In to the NAS from an External Network

After port mapping is configured on the router and DDNS is set up successfully, use the following methods to remotely sign in to the UGREEN NAS system from an external network, such as an office network or mobile data.

The following login rule applies to the UGREEN NAS PC client, web browser, and UGREEN NAS app.

#### Standard Login Format: HTTP Direct Connection

On the login page, enter the dedicated address in the "**Device address/IP**" field using the following format:

http://your-domain:external-port

**Example:**

If the purchased and configured domain name is `myNAS123.com`, and the external port mapped on the router for NAS access is `9999`, the complete login address should be: `http://myNAS123.com:9999`

![](https://file-us.ugreennas.com/admin/article/2026-06-08/b1f49a1926a149729c41383228bda560.webp)

#### Encrypted Login Format: HTTPS / Reverse Proxy

If you have some network troubleshooting experience and have configured an **SSL certificate** or **reverse proxy service** for the NAS, make sure to update both the protocol and port number:

https://your-domain:proxy-port

● The URL must start with `https://` instead of `http://`. Otherwise, the client will still send an unencrypted handshake request.

● If the reverse proxy forwards external traffic to another port, for example if the original mapped port `9999` is handled by the proxy, enter **the external port opened by** **the reverse proxy** instead of the NAS default internal port.

![](https://file-us.ugreennas.com/admin/article/2026-06-08/337c9c3441c244c294e6b0a7c3d881b7.webp)

### Troubleshooting External Access Issues

If external access fails, check the following items one by one:

**Check 1: Verify that DDNS resolution is working**

● **Cloudflare users:** Sign in to the Cloudflare dashboard, go to the "**DNS**" menu for the corresponding domain, and check whether the IP address in the DNS record has been updated. Also make sure the cloud icon is set to "**DNS only**" in gray instead of "**Proxied**" in orange. Otherwise, the standard web port may not pass through correctly.

![](https://file-us.ugreennas.com/admin/article/2026-06-08/0202a1745e62455d8d3cf26dda014749.webp)

**Check 2: Verify the router port mapping rules**

Check the router's port forwarding list and confirm whether the NAS internal IP has changed because no static IP was bound. Also make sure the external port does not conflict with mapping rules for other devices.

**Check 3: Check whether the firewall is blocking access**

Check the home network devices, including the NAS system firewall and the router security settings, and make sure the custom external port, such as `9999`, is not blocked or excluded by a blacklist rule.

**Check 4: Check whether the ISP blocks special ports**

Due to domestic compliance requirements, most broadband providers **strictly block ports 80 and 443** on public IP connections. If the external port is set to 80 or 443, access may fail completely. Use a high-numbered custom port that is less likely to conflict, such as `9999` or `8888`.
