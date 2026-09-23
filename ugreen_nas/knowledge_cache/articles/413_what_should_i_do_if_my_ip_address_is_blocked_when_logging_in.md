# What Should I Do If My IP Address Is Blocked When Logging In to UGREEN NAS?

> **Article ID**: `413`  
> **Category**: `Application Guide > Control Panel > FAQ > What Should I Do If My IP Address Is Blocked When Logging In to UGREEN NAS?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/413  

---

## Applicability

**Applicable Version:** NAS firmware 1.18.0.0032 or later

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## Problem Description

When logging in to UGREEN NAS, if you see the message "IP address has been blocked. Please sign in from another device or contact an administrator to unblock it.", the IP address of your current device has been blocked from accessing the NAS.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/5ad01626c1544987ad4da80a7b013686.webp)

## Cause

This happens when the number of failed login attempts reaches the system limit, triggering the IP blocking mechanism.

## Solution

Use another device that is not blocked to log in to the NAS, then remove the blocked IP address.

### Unblock an IP Address on PC

1. Log in to UGREEN NAS from a device that is not blocked using an administrator account.

2. Open "**Control Panel**", then click "**Security**">"**Block management**".

![](https://file-us.ugreennas.com/admin/article/2026-09-07/85b7ded84a5641fa9e58f0196a434fcf.webp)

3. Find the blocked IP address in the block list and click "**Remove**".

![](https://file-us.ugreennas.com/admin/article/2026-09-07/101255bed6d44edda704d85fc0d16627.webp)

Once removed, you can try logging in to the NAS again from that IP address.

### Unblock an IP Address on Mobile

1. Log in to UGREEN NAS from a device that is not blocked using an administrator account.

2. Open "**Control Panel**", then click "**Security**" > "**IP auto block**".

![](https://file-us.ugreennas.com/admin/article/2026-09-07/0b242c6f14574d8eb00bfe8d82d8e5eb.webp)

3. Find the blocked IP address in the blocked list and click it to open the IP details page.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/45ea47d438da49f18e935635e3684431.webp)

4. Click "**Unblock**".

![](https://file-us.ugreennas.com/admin/article/2026-09-07/3a3c950eb6194da2be08fe3784f85fb4.webp)

Once unblocked, you can try logging in to the NAS again from that IP address.
