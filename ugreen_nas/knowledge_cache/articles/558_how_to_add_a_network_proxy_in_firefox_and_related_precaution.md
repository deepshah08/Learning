# How to Add a Network Proxy in Firefox and Related Precautions

> **Article ID**: `558`  
> **Category**: `Application Guide > Docker > FAQ > How to Add a Network Proxy in Firefox and Related Precautions`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/558  

---

## Introduction

When using the Firefox app on UGOS Pro, configure network proxy settings in Firefox with caution. After a network proxy is added, access requests may be routed through the proxy server, which can prevent access to resources on the local network, such as containers and virtual machines. This article explains how to add a network proxy in Firefox and provides related precautions and solutions.

## Add a Network Proxy

1. Open Firefox, click the menu button (≡) in the top-right corner, and select "**Settings**".

2. In the General section, scroll down to "**Network Settings**", and click "**Settings**".

3. **Configure Proxy Access to the Internet**:

4. Select "**Manual proxy configuration**".

5. Enter the proxy server address and port number.

6. Click "**OK**" to apply the settings.

![](https://file-us.ugreennas.com/admin/article/2026-08-11/6445f376e1214c9ab60b5d3a93ed23e3.webp)

## About Network Proxy

1. **Disable the network proxy**:

If you need to access resources on the local network, temporarily disable the network proxy settings in Firefox. You can find and disable the proxy option in the browser’s Network Settings.

2. **Set exception rules**:

If you must use the network proxy, add addresses or address ranges that do not use the proxy in the browser’s Network Settings, such as 192.168.*.* or 10.*.*.\*, to ensure that local network resources can be accessed properly.

## Notes

● After adding a network proxy in Firefox, all network requests may be routed through the proxy server. This may prevent direct access to devices on the local network, such as containers and virtual machines, because requests are redirected to the proxy server.

● Due to proxy server routing, you may be unable to access resources on the local network, including but not limited to NAS devices, containers, and virtual machines. This is because the proxy server cannot access private IP addresses within the local network.
