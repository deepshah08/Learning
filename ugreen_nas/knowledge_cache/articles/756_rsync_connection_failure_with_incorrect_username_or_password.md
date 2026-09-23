# Rsync Connection Failure with "Incorrect Username or Password" Error – Troubleshooting

> **Article ID**: `756`  
> **Category**: `Application Guide > Control Panel > File Service > Rsync Connection Failure with "Incorrect Username or Password" Error – Troubleshooting`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/756  

---

## Problem Description

When configuring Rsync remote synchronization between multiple NAS devices, a one-way connection failure occurs:

● Observed Issue: NAS Device A cannot connect to NAS Device B, while Device B can connect to Device A normally.

● Error Message: When initiating a connection from Device A, the system displays "Incorrect username or password", despite the password being confirmed as correct.

## Cause Analysis

This issue is often caused by modified DNS settings (e.g., changes to the router or NAS itself), resulting in a conflict between UGREENlink's DNS and the device's domain name resolution. As a result, the target device address cannot be resolved correctly, and the connection request is sent to the wrong address, causing authentication failure.

![](https://file-us.ugreennas.com/admin/article/2025-08-25/fc4fc12bc8e441d4b31049e7e55dffc6.webp)

## Solution

Modify the NAS DNS server address to resolve this issue:

1. Open the "Control Panel" application and go to "Network" > "General".

2. Locate the DNS Server setting and update it to a valid public DNS.

3. Click "Apply" to save the settings.

**Recommended Public DNS Addresses:**

● **Mainland China Users:** Tencent Cloud DNS: 119.29.29.29 or Aliyun Drive DNS: 223.5.5.5

● **Overseas or Other Regions:** Google DNS: 8.8.8.8
