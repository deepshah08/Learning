# How to Troubleshoot External Access Issues or Frequent Disconnections After Configuring DDNS?

> **Article ID**: `924`  
> **Category**: `Troubleshooting > Network Failure > How to Troubleshoot External Access Issues or Frequent Disconnections After Configuring DDNS?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/924  

---

## Applicability

**Applicable Version**: NAS Firmware 1.15.0.0042 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Problem Description

After configuring DDNS, if UGREEN NAS cannot be accessed from an external network, or the connection is frequently disconnected, the issue may be related to the public IP address, domain name resolution, port mapping, firewall settings, ISP port restrictions, or network connection stability. Follow the steps below to troubleshoot the issue.

## Check Whether Your Network Has a Public IP Address

DDNS remote access requires a public IPv4 or IPv6 address. You can check the WAN IP address on your router and compare it with the IP address obtained from a public IP detection website.

● If the two IP addresses are the same, your network usually has a public IP address.

● If the two IP addresses are different, your network may be behind an ISP NAT, and DDNS direct access may not work properly.

If your network is confirmed to be behind an ISP NAT, contact your ISP to request a public IP address, or use another remote access method.

## Check Whether DDNS Domain Resolution Is Correct

Log in to your domain provider's management console and check the DNS records. Confirm the following information:

● The A record points to the current public IPv4 address.

● The AAAA record points to the current public IPv6 address.

● The IP address resolved by the domain has been updated.

● Cloudflare users should make sure the proxy status is set to **DNS only** and that proxy mode is not enabled.

If the domain resolves to an old IP address, external access may fail or disconnect intermittently.

## Check Router Port Mapping

Log in to your router's management interface and check the port forwarding rules. Confirm the following information:

● The NAS LAN IP address is correct.

● The NAS LAN IP address is fixed.

● The external port is mapped to the correct internal NAS port.

● The external port does not conflict with port forwarding rules for other devices.

If the NAS LAN IP address changes, the existing port mapping will become invalid. Configure a DHCP static IP address reservation or bind the NAS MAC address in the router settings.

## Check the Access Address Format

When accessing the NAS from an external network, make sure to enter the address in the correct format. For direct HTTP access, use: `http://your-domain:external-port`

If HTTPS, an SSL certificate, or a reverse proxy has been configured, use: `https://your-domain:proxy-port`

Make sure the protocol, domain name, and port number are entered correctly.

## Check Firewall and Security Blocking

If domain resolution and port mapping are working correctly but access is still unavailable, check whether the connection is being blocked by firewall or security settings. Check the following:

● NAS system firewall.

● Router security protection settings.

● Security policies on the modem or upstream router.

● Any port blocklists or access restrictions.

If any blocking rules are found, allow the corresponding external port.

## Check Whether Ports Are Blocked by Your ISP

Some ISPs may restrict commonly used service ports, such as 80, 443, and 25. If these ports are used as external ports, external access may fail.

Change the external port to a high-numbered port, such as `30001、40001`. After changing the port, update the router port forwarding rules and login address accordingly.

## How to Troubleshoot Frequent Disconnections?

If the connection works but disconnects frequently, check the following items:

● Whether the public IP address changes frequently.

● Whether DDNS updates the latest public IP address in time.

● Whether the NAS LAN IP address has changed.

● Whether the router port mapping has become invalid.

● Whether the router or modem has restarted or reconnected to the network.

● Whether the current external network environment is unstable.

● Whether the broadband ISP has restrictions on cross-network or cross-region access.

If the connection drops and the domain is resolved again, check whether the IP address resolved by the domain matches the current public IP address. If they do not match, the DDNS update may be delayed or the DNS record may not have taken effect yet.

## What to Do If the Issue Persists?

If all the above items have been checked but access is still unavailable, contact UGREEN NAS technical support and provide the following information:

● NAS model and system version.

● DDNS service provider.

● Current access address.

● Router port mapping screenshot.

● Router WAN IP address screenshot.

● Domain DNS record screenshot.

● NAS remote access settings screenshot.

● Error page screenshot.
