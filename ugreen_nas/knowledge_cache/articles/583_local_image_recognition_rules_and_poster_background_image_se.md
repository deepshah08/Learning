# Local Image Recognition Rules and Poster/Background Image Settings in the Theater

> **Article ID**: `583`  
> **Category**: `Application Guide > Theater > FAQ > Local Image Recognition Rules and Poster/Background Image Settings in the Theater`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/583  

---

In the Theater, the system can automatically recognize image files with the same name and located in the same directory as the video file, and use them as poster or background images. This method is especially useful for short dramas or video content that require manual management or do not contain a `.nfo`file, allowing quick generation of poster and background images.

Poster and background images currently support the following formats:`.jpg`,`.jpeg`,`.png`,`.webp`,`.bmp`.

## **Local Image Recognition Rules**

When you enable the "Read Local Information First" option, the Theater will automatically scan for local image files related to the video during the library import process, and load them as poster or background images according to the following rules:

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250731/a26d077b-a4e4-4c4f-9134-e03ec3e51071.png)

### **Poster and Background Image Rules for Movies**

1. **Poster Image**: If a file named `poster.jpg` exists in the same directory as the movie file, the system will set it as the poster image.
2. **Background Image**: If a file named `fanart.jpg` exists in the same directory, the system will set it as the background image.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250731/c942f7f5-dedb-4d63-95fa-177af5533c69.png)

### **Rules for Series Cover and Background Images**

1. **Series Cover**

The priority rule for selecting a series cover image is to use the image file named `poster.jpg` located in the series directory.

* **Example:** If the series folder is named `A Record of a Mortal's Journey to Immortality`and contains a file named `poster.jpg` , the system will set this file as the cover image for the series.
* **Cross-folder scenario:** When the series resources are distributed across multiple subfolders, the system will prioritize using the first detected `poster.jpg` file as the cover image.

2. **Series Background Image**

The priority rule for selecting a series background image is to use the image file named `fanart.jpg` located in the series directory.

* **Example:** If the series folder is named `A Record of a Mortal's Journey to Immortality`and contains a file named `fanart.jpg` , the system will set this file as the background image for the series.
* **Cross-folder scenario:** When the series resources are distributed across multiple subfolders, the system will prioritize using the first detected `fanart.jpg` file as the background image.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250731/cb504572-16dc-488d-9b73-5e56461ce2e5.png)

## **Setting the "Read Local Information First" Feature**

To ensure that local images are prioritized for recognition as cover or background images, please enable the relevant setting by following the steps below:

1. Open the Theater app and go to “Console” > “Library”. Edit the library you want to configure.
2. Scroll down the settings page and enable the “Read Local Information First” option. Click “Apply” to save and activate the setting.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250731/a0995aef-6418-48af-a8b8-359031d81e3d.png)

3. Ensure that the naming and storage location of local image files comply with the above rules.

## **Notes**

1. The naming conventions for image files must strictly follow the above requirements. Incorrect file names may cause recognition failure. For example, files named`poster1.jpg`or `background1.jpg` will not be recognized by the system.
2. The recommended resolution for cover images is 1080×1600 or higher to ensure clear display on large screens.
3. The recommended resolution for background images is 1920×1080 or 4K (3840×2160) to fit high-definition playback interfaces.
4. Please make sure that the image files are stored in the same directory as the video files so the system can properly retrieve them.
