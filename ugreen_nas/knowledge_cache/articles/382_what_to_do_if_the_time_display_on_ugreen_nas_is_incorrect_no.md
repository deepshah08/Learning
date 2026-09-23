# What to Do if the Time Display on UGREEN NAS Is Incorrect (Not Matching the Local Time)?

> **Article ID**: `382`  
> **Category**: `Application Guide > Control Panel > FAQ > What to Do if the Time Display on UGREEN NAS Is Incorrect (Not Matching the Local Time)?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/382  

---

## Issue Description

The time displayed on the UGREEN NAS device is incorrect (does not match the local time).

## Diagnosis

● **Incorrect time zone setting:** If the NAS time zone is not set to match your actual geographic location, the displayed time will be inaccurate. For example, if the device is set to UTC+8 but your actual location is UTC–5, the time will appear 13 hours ahead.

● **Network time synchronization issues:** If the network connection is unstable or the NTP time server cannot be reached, time synchronization may fail, causing the displayed time to be incorrect.

● **System or software errors:** Bugs in the system or related software may also lead to incorrect time display.

## Solutions

1. **Check the time zone settings:** Go to [Control Panel] > [Time & Language] and make sure the time zone matches your current geographic location.

2. **Verify network connectivity:** Ensure the network is working properly, then reconnect to the network and try to synchronize the time again.

3. **Change the time server:** If the default NTP server cannot sync successfully, switch to a different available time server address.1

4. **Restart the device:** Restart the UGREEN NAS to resolve potential system or software glitches.

5. **Update the system:** Make sure the UGREEN NAS is running the latest system version. Update the system if necessary to resolve any known time display issues.

![](https://file-us.ugreennas.com/admin/article/2025-09-03/fe17b465756d41968c41f8e17b8944a0.webp)

By following the steps above, you can effectively resolve the issue of incorrect time display. If the issue persists, we recommend contacting UGREEN Technical Support for further assistance.

Note:

Reference source for time server address1：

1. **NTP Pool Project：**

[NTP Pool Project official website](https://www.ntppool.org/en/)

● Global: `pool.ntp.org`

● North America: `north-america.pool.ntp.org`

● Europe: `europe.pool.ntp.org`

● Asia:`asia.pool.ntp.org`

● China: `cn.pool.ntp.org`

2. **Public NTP Servers:**

Many organizations offer public NTP servers. Here are some commonly used NTP server addresses:

● Google NTP: `time.google.com`

● NIST (National Institute of Standards and Technology): `time.nist.gov`

● Microsoft: `time.windows.com`

● Apple`time.apple.com`

● Cloudflare: `time.cloudflare.com`

3. **NTP Servers Provided by ISPs and Universities:**

● Some Internet service providers (ISPs) and universities also maintain public NTP servers. Check your local ISP’s or university’s official website for details.

4. **Online NTP Server Listings:**

● Some websites specialize in listing available NTP servers, such as：ntp.org or time.is.
