# Theater Offline Caching and Data-Free Playback

> **Article ID**: `864`  
> **Category**: `Application Guide > Theater > Theater Offline Caching and Data-Free Playback`  
> **Client Compatibility**: `MOBILE`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/864  

---

## Applicability

**Applicable client:** UGREEN NAS mobile app (iOS/Android).

**Applicable version:** UGOS Pro firmware 1.15.12.28676 or later.

**Requirements:** This feature is currently available only on the UGREEN NAS mobile app. The PC client is not supported yet. Please use the mobile app to perform this operation.

The descriptions in this article are for reference only. The actual interface and operation paths may vary slightly due to system or app version updates. Please refer to the actual interface.

## Feature Overview

To help save mobile data and provide smoother playback in poor network conditions, the **"Theater"** app on mobile includes an intelligent local cache matching mechanism.

When you tap a video in the app to play it, the system checks whether the same video already exists in the "**Downloaded**" list under "**My downloads**". If available, the system will prioritize the offline file for data-free playback.

## View and Manage Offline Videos

Videos must first be downloaded locally through the Theater app before this data-free playback mechanism can take effect. You can view downloaded videos as follows:

1. Open "**Theater**" in the UGREEN NAS app.

2. Tap "**Settings**" in the bottom navigation bar.

3. On the Settings page, tap "**My downloads**".

4. Switch to the "**Downloaded**" tab at the top of the page. You can then view all fully cached video resources on the current device.

**Note:** In the "**Downloaded**" list, resolution is displayed differently depending on the type of video resource:

● **Movie files:** The system displays the video resolution **directly on the movie thumbnail**.

![](https://file-us.ugreennas.com/admin/article/2026-06-02/e11a3a49a7cb4cf8be76e49405553420.webp)

● **Episode files:** The system **does not display** the resolution directly. If you do not remember the quality selected when the episode was downloaded, tap the episode to play it. You can view the specific video quality, such as **720P**, **1080P**, or **Original**, in the lower-right corner of the player interface.

![](https://file-us.ugreennas.com/admin/article/2026-06-02/f103dcbf0fd846b882410f54ed03578f.webp)

## How Data-Free Playback Works

When matching offline resources, the system checks the video title and follows the principle of **matching the same resolution**. The logic is as follows:

● **Matching video resolution (offline playback triggered):** If the playback quality currently selected in the player, such as **Original**, is the same as the quality of the video in the "**Downloaded**" list, the system will play the downloaded file. No mobile data will be used during playback.

● **Mismatched video quality (network streaming triggered):** If the quality currently selected in the player is different from the quality of the video in the "**Downloaded**" list, the match will fail.

**Example:** If you previously downloaded the **720P** version to save storage space, but later select "**Original**" quality when playing the video in Theater, the system will determine that the video quality does not match. It will not use the offline **720P** file and will continue to stream the **Original** video from the NAS, consuming network data.

## FAQ

**1. I have already downloaded this movie to my phone. Why does it still use a large amount of data when I play it outside?**

● **Check 1:** Check whether the quality currently selected in the player, such as **1080P** or **Original**, matches the quality you downloaded. Since the download list does not display the quality, we recommend briefly playing the video once from "**Downloaded**" to confirm its resolution. Then manually switch your usual playback quality to the same resolution. The system will then switch back to data-free playback.

● **Check 2:** Check the client you are using. Make sure you are using the UGREEN NAS app on your phone or tablet. If you play the video on a computer, either through the PC client or the web version, network data will still be used to stream the video from your NAS because offline downloads for Theater are not currently supported on desktop.

● **Check 3:** Go to "**Theater**">"**Settings**">"**My downloads**">"**Downloaded**" and check whether this resource is listed. If you have deleted or moved the local file using the built-in file manager on your phone, Theater may no longer be able to read it from the specified path, and offline playback cannot be triggered.
