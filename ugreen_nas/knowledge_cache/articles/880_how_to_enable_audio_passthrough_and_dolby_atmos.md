# How to Enable Audio Passthrough and Dolby Atmos?

> **Article ID**: `880`  
> **Category**: `Application Guide > Theater > How to Enable Audio Passthrough and Dolby Atmos?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/880  

---

## Overview

Audio passthrough means the player does not decode audio on the local device, such as the NAS or TV. Instead, it sends the original audio stream through an HDMI cable to an external AV receiver or soundbar, where the audio is decoded by dedicated audio equipment. This allows multi-channel audio, such as 5.1 and 7.1 surround sound, as well as Dolby Atmos, to be reproduced properly and makes full use of a high-end audio system.

## How to Enable Audio Passthrough

When playing a video on the TV client, such as Apple TV or Android TV, the audio output mode can be changed directly from the playback screen:

1. During playback, press the remote control button to open the playback controls at the bottom of the screen.

2. Go to "**Audio**".

3. Under "**Audio output**", select "**Audio passthrough**".

After this option is selected, the system will automatically check whether the current HDMI connection and the connected audio device support passthrough. If supported, passthrough takes effect immediately, and audio decoding will be handled by the connected AV receiver or soundbar.

![](https://file-us.ugreennas.com/admin/article/2026-06-29/a4d6b36b94154f428d21532706885752.webp)

## Apple TV (tvOS) Passthrough Rules

On Apple TV, audio passthrough uses "**Auto**" detection. Supported behavior is as follows:

● **Supported formats**: **EAC3**, including Dolby Atmos metadata, and **AC3** are supported. If the full device chain, including the TV and audio system, supports passthrough, playing an EAC3 audio track can trigger the "**Dolby Atmos**" indicator on the TV or soundbar.

● **Unsupported formats**: Due to tvOS system-level limitations, lossless passthrough formats such as TrueHD and DTS-HD MA are not supported.

● **Fallback**: If the current device chain does not support passthrough, the player automatically falls back to multi-channel PCM output to ensure normal audio playback.

● **Playback speed compatibility**: On Apple TV, passthrough and playback speed adjustment can work at the same time. Playback speed can still be adjusted after passthrough is enabled.

## Android TV Passthrough Rules

Android TV and PC allow more direct access to system-level audio output, so they support higher-spec lossless audio bitstream passthrough. Formats such as TrueHD, DTS-HD, and DTS:X can be passed through to an AV receiver, allowing the receiver to decode the audio and deliver more accurate surround sound positioning.

## Why Is There No Sound After Enabling Passthrough?

This issue is usually caused by device chain compatibility or insufficient HDMI cable bandwidth.

**Solutions**:

● Check whether the AV receiver or soundbar supports hardware decoding for the current audio track, such as TrueHD.

● Make sure the HDMI cable is HDMI 2.0 or later to support high-bitrate audio transmission.

● If the issue persists, contact UGREEN NAS technical support for assistance.

## How to Confirm Whether Dolby Atmos Is Enabled

Check the display panel on the connected AV receiver or soundbar, or check the prompt shown on the TV screen. When passthrough is active, the audio device usually shows a dedicated "**Dolby Atmos**" indicator. If "**PCM 5.1**" or "**Stereo**" is displayed, the system has fallen back to a lower audio output mode.

**Note:** Apple TV users should make sure the current source audio track is in EAC3 format.

## Does Audio Passthrough Affect Playback Speed?

This depends on the platform in use.

● **Apple TV**: No. Passthrough and playback speed adjustment can work at the same time.

● **Android TV**: Due to hardware decoder limitations on some devices, playback speed adjustment may become unavailable after passthrough is enabled. Choose whether to enable passthrough based on the current viewing need, such as maximum audio quality or faster episode browsing.
