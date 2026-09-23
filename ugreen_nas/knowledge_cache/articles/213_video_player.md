# Video player

> **Article ID**: `213`  
> **Category**: `Application Guide > Theater > Video player`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/213  

---

**Applicable Version:** UGOS Pro firmware 1.12.0.0095 and above

Screenshots and interfaces in this document are for reference only. Actual displays may vary depending on system or application version. Some features may change across versions, please refer to your actual interface.

## Feature Overview

The built-in video player of the UGREEN NAS system provides a comprehensive set of playback features and flexible configuration options, designed to meet your viewing needs across different devices.

## Basic Playback Features

On the playback interface, you can perform the following basic operations:

1. **Quick Fast Forward / Rewind**

When playing videos on a PC, quick time-jump controls are supported:

● **Fast forward:** jump forward by **15 seconds**

● **Rewind:** jump backward by **15 seconds**

During playback, users can use the corresponding controls to quickly adjust the playback position.

2. **Volume Control:** Drag the volume slider to quickly adjust the audio level.

3. **Resolution Switching:**

● **Web:** Supports up to 1080P playback.

● **Windows and macOS:** Supports "**Original**" resolution playback, providing the highest video quality experience.

4. **Playback Speed:** Supports speeds from 0.5× to 3.0×, allowing fast-forward or slow-motion playback as needed.

5. **Playlist:** Manage the current playback history. For series videos, quickly locate specific episodes.

![](https://file-us.ugreennas.com/admin/article/2025-12-24/99d5ffd7a9d648618ccb8572ce87be8d.webp)

## Full-Screen and Picture-in-Picture (PiP) Mode

1. **Full-Screen:** Tap the "**Full Screen**" button to expand the video to fill the entire screen for an immersive experience.

2. **PiP Mode:** Allows the video to be minimized into a floating window while performing other tasks.

● **Window adjustment**: The PiP window can be freely dragged and resized (If the PiP window becomes too large, it automatically reverts to normal window mode).

● **Basic controls**: In mini-window mode, only "**Play/Pause**" and "**Previous/Next episode**" controls are available.

● **Limitations**: On the Web version, **external subtitles are not displayed** in PiP mode. It is recommended to use the UGREEN NAS client on Windows or macOS for full functionality.

![](https://file-us.ugreennas.com/admin/article/2025-12-24/dda14234b0254e56b8e208fc921b43cc.webp)

## Subtitle Features

The player supports **embedded subtitles** and **external subtitles**.

Loading Methods:

● **Embedded Subtitles:** Automatically load subtitles included in the video file.

● **External Subtitles**(automatic): When the subtitle file is in the same folder as the video and has the same filename,it will be loaded automatically.

**Example:**

Video:`Breaking.Bad.S01E01.2008.1080p.x265.mkv`

Subtitle:`Breaking.Bad.S01E01.2008.1080p.x265.srt`

**Local Import:** Supports importing subtitle files from your local computer.

**Online Download:** Use the "**Download subtitles online**" feature in the "**subtitle menu**" to search for and download subtitle files.

> Searching with the video's English title for higher matching accuracy (You can visit [TheMovieDB](https://www.themoviedb.org/) to obtain the correct English title of a video).

![](https://file-us.ugreennas.com/admin/article/2025-12-24/dc082d837db545438aabcd866f439e33.webp)

**Adjusting Subtitles (PC):**

● Supports adjusting subtitle size and height.

● Supports setting subtitle time offsets to synchronize with video playback.

![](https://file-us.ugreennas.com/admin/article/2025-12-24/289c2758c0ac486486753e86867f9a3f.webp)

## Smart Feature: Skip Intro and Outro

The player can automatically detect and skip repetitive segments in episodes, providing a smoother viewing experience.

### Step 1: Enable System Detection

This feature requires enabling the recognition task in the background:

1. Open the "**Theater**" app.

2. Go to "**Settings**"icon >"**Background Management**".

3. Turn on "**Identify intros & outros**". The system will automatically analyze the episodes in your media library.

![](https://file-us.ugreennas.com/admin/article/2025-12-24/7881fbd042f9459aa89b4dae231a2583.webp)

### Step 2: Enable in the Player

1. Open the video playback interface.

2. Go to "**Settings**"icon >"**Identify intros & outros**".

3. Once enabled, you can view the specific time ranges that will be skipped.

![](https://file-us.ugreennas.com/admin/article/2025-12-24/8cc0c409be124e3d982b31ff39abc91a.webp)

● **Opening:** When playback reaches the intro segment, the system automatically skips it.

![](https://file-us.ugreennas.com/admin/article/2025-12-24/4f2fd3c9f3ae481abe1bb8bfcfa0fac2.webp)

● **Ending:** When playback reaches the outro segment, the system will prompt "**Skipped outro automatically**".

![](https://file-us.ugreennas.com/admin/article/2025-12-24/26752cf0bcfb4e66a9b5f7984a142b14.webp)

## General Player Settings

● **Sound Track**: For videos with multiple audio tracks, you can freely switch between different languages or versions during playback.

● **Playback Modes**: Supports play in order, play one episode, random loop, repeat all, repeat one.

● **Compatibility Mode**: If issues such as black screens, transparent windows, or sound without video occur, enabling "**Compatibility Mode**" may help resolve them.

![](https://file-us.ugreennas.com/admin/article/2025-12-24/7670deadacb4494cb2df1806b78396ee.webp)

## Client-Exclusive Features (Windows/macOS)

The following advanced features are only available in the UGREEN NAS Windows or macOS clients:

### Video and Display

**HDR Playback Mode:**

● **Activation:** Enabled when the video supports HDR and the connected display (e.g., monitor) also supports HDR.

● **Status Indicator:** An **HDR** icon will automatically appear on the left side of the player control bar, indicating that High Dynamic Range playback is active.

![](https://file-us.ugreennas.com/admin/article/2025-12-24/7c4521fcce1e44e19397ad8315469749.webp)

**Aspect Ratio:**

● **Original Aspect Ratio:** Displays the video in its original aspect ratio.

● **Full Screen:** Stretches the video to fill the entire screen.

● **Fixed Ratio:** Allows manual selection of common ratios such as 16:9, 21:9, or 4:3.

**Color Adjustment**: Supports manual adjustment of brightness, contrast, and saturation.

![](https://file-us.ugreennas.com/admin/article/2025-12-24/9b04eddf414045248403880633f328a6.webp)

### Decoding Method

● **Hardware Decoding(recommended):** Uses the device GPU for video decoding, providing smoother playback and lower power consumption. Recommended for most cases.

● **Software Decoding:** Uses the CPU for decoding, suitable for formats or specially encoded videos that are not compatible with hardware decoding.

![](https://file-us.ugreennas.com/admin/article/2025-12-24/3193953e3c05489c82e5e08814ee4f36.webp)

### Audio Output (Only for Windows)

In the Windows player settings, the following audio output modes are supported:

**Stereo:** Default mode with the best compatibility.

**Audio Passthrough:** Directly transmits original audio signals such as TrueHD, DTS, or AC3 to external decoding devices (e.g., amplifiers or home theater systems) for high-fidelity surround sound.

**Requirements for Audio Passthrough:**

● An external device that supports audio passthrough must be connected.

● The video’s audio track must be compatible with passthrough (e.g., 5.1 or 7.1 channels).

> When passthrough is enabled, the player cannot adjust volume or playback speed. If playback is currently at a non-standard speed, switching to passthrough mode is not supported.

![](https://file-us.ugreennas.com/admin/article/2025-12-24/cf7f0ef49546486e914ab60a06990840.webp)
