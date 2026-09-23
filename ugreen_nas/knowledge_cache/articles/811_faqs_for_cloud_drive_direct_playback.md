# FAQs for Cloud Drive Direct Playback

> **Article ID**: `811`  
> **Category**: `Application Guide > Theater > FAQ > FAQs for Cloud Drive Direct Playback`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/811  

---

## What is cloud drive direct playback?

Cloud drive direct playback refers to a playback method where the NAS directly retrieves the actual streaming URL of a file through official cloud drive APIs, enabling playback without downloading or local caching.

● Does not consume local NAS storage space.

● No NAS transcoding required, reducing device load.

● Playback speed is closer to the native cloud drive speed, offering better stability.

● Can be used with the Theater app to generate a poster wall, delivering a local viewing experience for cloud-based content.

## Device and Version Requirements

To ensure proper functionality, please make sure your devices meet the following requirements:

● **UGREEN NAS firmware**: Version 1.14.1.0107 or later.

● **Theater app**: Version 1.14.0.0050 or later.

● **PC client**: UGREEN NAS client version 1.14.0.76802 or later.

● **iOS devices**: UGREEN NAS app version V1.14.0.3073 or later.

● **Android devices**: UGREEN NAS app version V1.14.0.21386 or later.

## Playback Capabilities and Platform Differences

UGREEN NAS currently supports cloud drive direct playback for 115 Drive and Quark Drive. Due to differences between clients, playback capabilities may vary:

### 115 Drive

Supports both original quality playback and transcoded playback.

● **PC & Mobile**: Supports both original and transcoded playback.

● **Web**: Only supports transcoded playback.

● **TV**: Not supported.

### Quark Drive

Currently supports transcoded playback only.

● **PC, Mobile & Web:** Only supports transcoded playback.

● **TV:** Not supported.

All clients currently do not support "**original quality playback**" for Quark Drive. This feature is under active development—stay tuned for future updates.

## Why does playback fail?

When using cloud drive direct playback for videos, playback failures or issues are usually caused by the following four reasons. You can troubleshoot them based on the corresponding suggestions below:

### Cloud drive risk control or account limitations

Cloud drive platforms impose strict limits on concurrent access. Logging in from multiple IP locations or playing content on multiple devices simultaneously may easily trigger risk control mechanisms, resulting in API rate limiting or abnormal account status.

**Solution**:

● Avoid sharing the same cloud drive account among multiple users, and try to minimize simultaneous playback across multiple devices.

● It is recommended to enable cloud drive direct playback only for frequently used accounts in the Theater app.

### Unstable local network

Poor network conditions or insufficient bandwidth may prevent proper video loading.

**Solution**:

● Check your current network connection status of your device.

● It is recommended to switch to a more stable network environment, such as using a wired connection or connecting to a stronger Wi-Fi signal.

### Abnormal video file status

The target video file may have been deleted or moved from its original location in the cloud drive, or the retrieved direct playback link may have expired.

**Solution**: Please first check in the official cloud drive client whether the file can still be accessed normally. If the file is intact, try remounting the cloud drive or refreshing the media library in the Theater app.

### Browser security restrictions (Web)

When playing on the web (Web), the player may be blocked by the browser's Content Security Policy (CSP). For example, on HTTP pages, the browser may prevent certain video resources from loading due to protocol restrictions.

CSP is a built-in browser security mechanism designed to prevent web pages from loading unsafe or untrusted content, or from making cross-protocol resource requests.

**Solution**: If playback fails on the web, it is recommended to use the UGREEN NAS desktop or mobile app for playback instead.

## What are transcoded playback and original quality playback?

In the video playback interface, the system displays the current video quality.

![](https://file-us.ugreennas.com/admin/article/2026-04-01/f298aff8017d4b65aa2c193e10e0a29b.webp)

● **Transcoded playback**: Tap the quality option to switch between different resolutions (such as 4K or 1080P) from the pop-up menu. The process of re-encoding the video to output different quality levels is referred to as transcoded playback.

● **Original quality playback**: If the cloud drive video supports lossless direct streaming, an "**Original**" option will appear in the quality list. Selecting it allows the system to play the uncompressed original video directly.

## Why is there no "Original" option?

This may be due to:

● **Cloud drive limitations**: Some cloud drives (such as Quark Drive) currently only support transcoded playback and do not provide direct links for original-quality streaming.

● **Missing file metadata**: When processing network-mounted resources, the system may not be able to retrieve the video's resolution in advance, preventing accurate matching of the original-quality stream.

## Should all users enable cloud drive direct playback?

Not recommended. If multiple users access the cloud drive simultaneously via direct links, it will rapidly increase the number of IP requests, which can easily trigger risk control mechanisms on third-party cloud platforms and lead to account rate limiting.

It is recommended to strictly control the scale of concurrent access and enable cloud drive direct playback only for a small number of frequently used core accounts.

## About quality and resolution settings

Transcoded playback is used to switch between different resolutions. If the cloud resource supports original output, you can select "**Original**" directly in the quality settings.

![](https://file-us.ugreennas.com/admin/article/2026-04-01/f433ab8ce78c4f7bbbc05c5d8532b83a.webp)

## How to troubleshoot playback issues?

It is recommended to troubleshoot step by step in the following order:

1. Check whether the UGREEN NAS system, the Theater app, and the client apps are all updated to the latest versions.

2. Confirm whether the cloud drive you are using supports cloud drive direct playback.

3. Check whether the device's network connection is stable and whether the bandwidth is sufficient.

4. Try playing other videos to verify whether the original file is still valid.

5. Switch the playback mode to "**Transcoded playback**" and check whether the lag or errors are resolved.

6. If the issue persists, please contact official technical support and provide specific error messages or screenshots.

## What to do if cloud drive direct playback is slow or frequently buffers?

Mainstream cloud drive platforms impose strict speed limits on non-premium users. When playing large high-definition videos, insufficient loading and buffering speeds may result in poor playback performance.

**Solutions**:

1. Go to the corresponding cloud drive app or official website and upgrade to a premium or super premium membership to unlock higher download and streaming speeds.

2. After upgrading, playback performance can improve significantly. For specific speed improvements, bandwidth limits, and peak speeds, refer to the official membership comparison pages of each cloud drive or contact their customer support.

## Playback still slow after subscribing to Quark Drive 88VIP?

Quark Drive 88VIP membership is subject to bandwidth limitations and speed control. During peak hours or when playing large files, throttling may occur, preventing full-speed playback.

**Solutions**:

1. These speed policies are defined by Quark Cloud Drive. It is recommended to contact their customer support to confirm the actual speed benefits of your current membership.

2. For a smoother, full-speed cloud drive direct playback experience on your NAS, it is recommended to upgrade to Quark Drive SVIP or a higher-tier membership.

## Notes

● The cloud drive direct playback experience is largely affected by the third-party cloud drive provider. Some speed limits or risk control issues are beyond local control.

● The overall stability of network-mounted resources is lower than that of NAS local storage. For the best viewing experience, it is recommended to prioritize playing videos stored locally on the NAS.

● Due to different cloud drive API policies, certain advanced features (such as original quality output or automatic quality detection) may be restricted depending on the type or version of the cloud drive.
