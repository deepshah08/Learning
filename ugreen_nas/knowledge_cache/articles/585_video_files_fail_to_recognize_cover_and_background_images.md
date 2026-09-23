# Video Files Fail to Recognize Cover and Background Images

> **Article ID**: `585`  
> **Category**: `Application Guide > Theater > FAQ > Video Files Fail to Recognize Cover and Background Images`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/585  

---

## **Problem**

In the UGOS Pro Theater, video files may sometimes fail to display cover and background images. This issue is typically caused by image file naming rules, storage locations, or formats not meeting system requirements.

## **Solution**

### **Image File Naming Rules**

**Cover Images**:

Must share the same name as the video file (excluding the extension) or be named

* Example: If the video file is named `Twisters 2024 2160p.mkv`, the cover image should be named `Twisters 2024 2160p.jpg`, `Twisters 2024 2160p.png`, `poster.jpg`, or `poster.png`.

**Background Images:** Must be named `background`or`fanart`

* Example: If the video file is named `Twisters 2024 2160p.mkv`, the background image should be named `background.jpg`, `background.png`, `fanart.jpg`, or `fanart.png`.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250827/7ad44849-7926-4601-b8a7-ce067342a585.png)

**Incorrect Example:** Files named `poster1.jpg` or `background1.jpg` will not be recognized by the system.

**Image Quality Recommendations**

* **Cover Images**:  
  To ensure clarity on large screens, a resolution of **1080x1600** or higher is recommended. High-quality cover images can enhance the viewing experience.
* **Background Images**:  
  A resolution of **1920x1080** or **4K (3840x2160)** is recommended to match high-definition playback interfaces. High-resolution background images improve visual effects and provide a more immersive viewing environment.

**Image Storage Location**

* Ensure that **cover images** and **background images** are stored in the **same directory** as the video file. The system will automatically scan this directory for image files to correctly display covers and backgrounds. If the image files are not stored in the same directory as the video file, the system will not recognize or apply them.

**Supported Image Formats**

* The current version supports only `.jpg` and `.png` formats.
* Other formats, such as `.webp` or `.bmp`, are not supported at this time.
* Ensure all cover and background images are saved in `.jpg` or `.png` format.

### **Retrieval Rules for Movie Cover and Background Images**

#### **Cover Images**

* The system first searches for an image file with the same name as the video file (excluding the extension), such as `Twisters 2024 2160p.mkv`, the system will look for `Twisters 2024 2160p.jpg` or `Twisters 2024 2160p.png`.

* If no matching image is found, the system will then look for a file named `poster.jpg` or `poster.png` in the same directory.

#### **Background Images**

* The system prioritizes image files named `background.jpg`or `background.png` in the same directory.
* If no such file is found, the system will search for `fanart.jpg` or`background.png`in the same directory.

### **Retrieval Rules for TV Series Cover and Background Images**

**Series Cover Images**

* The system will prioritize image files named `poster.jpg` or `poster.png` located in the series directory.
* If the series content is distributed across multiple subfolders, the system will use the first detected `poster.ext` file as the cover image.

#### **Series Background Images**

* The system will prioritize image files named `fanart.jpg` or `fanart.png` located in the series directory.
* If the series content is distributed across multiple subfolders, the system will use the first detected `fanart.ext` file as the background image.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250827/d66c767e-5385-4f85-969e-381a7b5d9774.png)

### **Notes**

* `.ext` **Format**: Refers to the `.jpg` or `.png` file extensions.
* Ensure the image file names are accurate, without extra spaces or special characters.
* If cover or background images are still not recognized, check the file permissions and directory structure to ensure the system has access to these files.
