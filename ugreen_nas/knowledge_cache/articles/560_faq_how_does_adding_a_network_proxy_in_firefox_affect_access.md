# [FAQ] How Does Adding a Network Proxy in Firefox Affect Access to Devices on the Local Network?

> **Article ID**: `560`  
> **Category**: `Application Guide > Docker > FAQ > [FAQ] How Does Adding a Network Proxy in Firefox Affect Access to Devices on the Local Network?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/560  

---

When the network proxy feature is enabled, all browser network requests are routed through the proxy server. While this can help with privacy protection and access across regions, it also alters the access path and may cause the following issues:

1. **Inaccessible Local Devices**: Since requests are forwarded to an external server, devices on the local network—such as containers and virtual machines—may become inaccessible.
2. **Abnormal Connection Paths**: Services that rely on local network communication (e.g., file sharing, remote desktop) may stop functioning properly due to proxy interception.
3. **Performance Degradation**: Using a proxy can introduce latency or even connection failures, especially if the proxy server has limited capacity or the network is congested.

## **Solution:**

If you need to access local network resources, consider adjusting your proxy settings as follows:

1. **Disable the proxy：** In Firefox, go to [Settings] > [Network Settings], and select "No proxy" to disable proxy usage.
2. **Set exceptions：** If you need to keep the proxy enabled, you can add exceptions for specific address ranges (e.g.,`192.168.*.*` or`10.*.*.*`) in Firefox’s network settings to allow direct access to local resources.
3. **Use a different browser：** If you frequently access local devices, consider using a browser without proxy settings enabled (such as Chrome or Edge) to avoid interference with local network access.

## **Notes：**

1. Make sure you understand the intended use of a network proxy. It is not recommended to enable proxy functionality unless necessary.
2. When using a proxy, it is advisable to test connectivity for critical services to ensure that access paths and device resources are not restricted.
3. If you are using the Firefox browser on an untrusted device, never save proxy-related configuration information, and promptly clear your browsing history to protect data security.

By properly managing your network proxy settings, you can effectively avoid issues with limited LAN access while ensuring the normal operation of the UGOS Pro system and related services.
