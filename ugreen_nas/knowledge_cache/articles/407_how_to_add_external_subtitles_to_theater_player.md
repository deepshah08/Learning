# How to Add External Subtitles to Theater Player

> **Article ID**: `407`  
> **Category**: `Application Guide > Theater > FAQ > How to Add External Subtitles to Theater Player`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/407  

---

> ## Applicability
>
> **Applicable platforms**: UGREEN NAS PC client and Web browser.
>
> **Applicable versions**: UGOS Pro firmware 1.15.0.0114 and later.
>
> The document is for reference only. Actual displays may vary depending on system or application versions. Please refer to your actual interface for accuracy.

When using the UGREEN NAS Theater, adding external subtitles to videos without embedded subtitles can greatly improve the viewing experience. This document provides a detailed introduction to supported subtitle formats, subtitle sources, automatic recognition rules, and manual subtitle management operations.

## Supported External Subtitle Formats

Theater is fully compatible with mainstream local external subtitle formats, including the following:

● **Common subtitle formats**: Files with the `.ass` or `.srt` extension.

● **Special effects and special formats**: Supports `sup` special-effect subtitles, as well as `SMI` and `SSA` formats.

## How to Obtain External Subtitles

Depending on your preference, external subtitles can either be downloaded manually from third-party websites or downloaded directly through the built-in online subtitle feature in the player.

### Method 1: Download from Third-Party Subtitle Websites

Common professional subtitle websites include [OpenSubtitles](https://www.opensubtitles.org/en/search/subs) (supports multiple languages and API access), [Zimuku](https://zimuku.org/) (mainly Chinese and bilingual subtitles), and [Subscene](https://subscene.com/) (multilingual subtitles).

1. Visit one of the above websites and search for the movie or TV show title.

2. Select a subtitle file that matches your video version (such as Web-DL or BluRay) and download it to your computer.

3. After downloading, upload the subtitle file to the UGREEN NAS and place it in the same folder as the video file. Rename the subtitle file so that it has exactly the same filename prefix as the video file.

**Example of naming and storage path:**

● Video file path: `media/tv/Interlaced.Scenes.S01E06.2024.mkv`

● Subtitle file path: `media/tv/Interlaced.Scenes.S01E06.2024.srt`

**Note:** Subtitle files with language suffixes such as `.zh-cn.srt` are also supported for recognition.

### Method 2: Download Through the Built-in Player Feature

UGREEN NAS supports searching for and loading online subtitles directly from the video playback interface.

1. While playing a video, click the "**CC**" subtitle icon in the player action bar.

![](https://file-us.ugreennas.com/admin/article/2026-05-09/3cf01f7bccf84fda975a9a91389b70fe.webp)

2. Click "**Add subtitle**," then select "**Download subtitles online**."

![](https://file-us.ugreennas.com/admin/article/2026-05-09/7d2f8b13726a4465bb770e8ff18e4d0e.webp)

3. Enter the video name in the search box and press Enter to search for subtitles.

Using the original English title of the video can improve matching accuracy.

![](https://file-us.ugreennas.com/admin/article/2026-05-09/639bc3a84feb4feca244d5d6c0b45ef9.webp)

4. Select the desired subtitle language and download it. The system will automatically recognize it as an external subtitle and load it during playback.

![](https://file-us.ugreennas.com/admin/article/2026-05-09/b2768fec3daf4271ba4b2203d0f876e7.webp)

**Online Subtitle Storage Location:**

Subtitles downloaded through the online search feature will be automatically saved in the same directory as the video file and automatically renamed according to the video filename. For example, if the video file is `MyMovie.mp4`, the subtitle file will be saved as `MyMovie.srt`.

## Player Subtitle Management

### Automatically Recognizing and Loading Local Subtitles

When playing a video, if automatic recognition and loading of locally downloaded external subtitles is preferred without manual addition, the following file placement and naming rules must be strictly followed.

**Automatic Loading Rules**

To ensure subtitles are correctly recognized, both of the following conditions must be met:

● Same Directory: The video file and subtitle file must be stored in the same folder path.

● Complete Filename Match: The subtitle filename must fully contain the main filename of the corresponding video file.

**Example**:

Assume there is a video file named `A01.mkv`, along with English and German subtitle files prepared for it. The correct directory structure would be as follows:

```
📁 Movie Storage Folder
 ├── 🎬 A01.mkv                （Main Video File）
 ├── 📝 A01-English.srt        （English Subtitle File）
 └── 📝 A01-Deutsch.srt        （German Subtitle File）
```

**Explanation**:

In the example above, the subtitle filenames (`A01-English` and `A01-Deutsch`) both fully contain the video filename (`A01`), and all files are stored in the same folder.

Once these conditions are met, the system will automatically recognize and load both subtitle files when `A01.mkv` is played in Theater. The subtitles can then be freely switched through the "**CC**" subtitle menu in the playback interface.

### Manually Adding Local Subtitles

If subtitles are not loaded automatically, or if subtitle files stored in other locations need to be attached manually, follow these steps:

1. Click the "**CC**" subtitle icon in the player interface.

2. Click "**Add subtitle**," then choose the corresponding subtitle source based on the platform currently in use:

● **From computer**: (Supported on both the PC client and Web browser) Select a subtitle file from the local hard drive of the current computer.

● **From NAS**: (**Supported only on the Web browser**) Locate and import subtitle files directly from the internal storage of the NAS.

3. In the file selection window, select and import the downloaded subtitle file.

4. After the subtitle is successfully added, click the "**CC**" icon again to view and switch between all available subtitles, including both embedded subtitles and the newly added external subtitles.

![](https://file-us.ugreennas.com/admin/article/2026-05-09/f16174a05187439cb06eb315a687a1b6.webp)

### Turn Off Subtitles

To stop displaying subtitles, click the "**CC**" icon and select "**Off**" from the pop-up list.

![](https://file-us.ugreennas.com/admin/article/2026-05-09/3b85342c1bed4d8e9da9edbb08bf21fc.webp)

## Notes

When loading or adjusting subtitles in the UGREEN NAS Theater player, please note the following feature limitations and differences between platforms (PC client and web browser):

### Dual Subtitle Not Supported

Theater currently does not support dual subtitles (displaying two subtitle streams in different languages simultaneously not supported).

### Subtitle Adjustment Features

Personalized subtitle adjustment and synchronization features may vary depending on the playback platform being used. For advanced subtitle adjustment, the UGREEN NAS desktop client is recommended.

**UGREEN NAS PC Client (Adjustment Supported)**:

● When using the built-in Theater in the desktop client, click the "**CC**" icon in the interface and select "**Adjust Subtitle**" to configure subtitle settings from the menu.

![](https://file-us.ugreennas.com/admin/article/2026-05-09/4e187ec245ba404098ecafbe910a9088.webp)

● The subtitle adjustment feature supports changing Subtitle Size, modifying Subtitle Height, and performing subtitle sync with millisecond (ms) precision (to resolve subtitle and video desynchronization issues).

![](https://file-us.ugreennas.com/admin/article/2026-05-09/429b01e3935a43e7bbeef20ce4d0e476.webp)

**Web/Browser (Adjustment Not Supported):**

● When Theater is accessed through a browser (Web browser), the subtitle adjustment features mentioned above are currently not supported due to environment limitations.

● After clicking the "**CC**" icon in the Web browser, the "**Adjust Subtitle**" option will not be displayed in the menu.
