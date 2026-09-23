# Why Can't the Camera Be Added to Surveillance Center When the NAS and Camera Are on the Same LAN?

> **Article ID**: `903`  
> **Category**: `Application Guide > Surveillance Center > Why Can't the Camera Be Added to Surveillance Center When the NAS and Camera Are on the Same LAN?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/903  

---

## Description

The NAS and camera are on the same LAN, but the camera cannot be added to Surveillance Center.

## Possible Causes

A camera may fail to connect to Surveillance Center for the following reasons. Check each item in order:

1. **ONVIF is disabled**: Some cameras require ONVIF to be manually enabled in the camera’s management interface. It may be disabled by default.

2. **Incorrect username or password**: Some cameras have separate credentials for the management interface and ONVIF access. Make sure you enter the ONVIF username and password.

3. **Unsupported protocol**: Surveillance Center supports standard ONVIF and RTSP protocols. Some camera brands use proprietary protocols that are not supported by Surveillance Center.

4. **Too many connections to the same camera**: If a camera is accessed by multiple devices simultaneously, it may exceed the maximum number of supported streams, causing new connections to fail. Disconnect unnecessary connections and try again.

## Solution

● Log in to the camera’s management interface, check whether ONVIF is enabled, and make sure you are using the ONVIF username and password.

● If ONVIF is enabled but the camera still cannot be added, contact the camera manufacturer to confirm the protocols supported by this model.

● Reduce the number of devices accessing the camera simultaneously, then try connecting again.

● If the issue persists after trying the methods above, contact UGREEN technical support.
