# Quick Start Guide for Jellyfin

> **Article ID**: `592`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Quick Start Guide for Jellyfin`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/592  

---

## **Application Overview**

Jellyfin is an open-source, free media server software that focuses on local media management and streaming services. Users can manage video, music, images, and other files in one place and stream them to multiple devices over the network. It supports features such as transcoding, subtitles, and plugin extensions.

### **Core Features**

1. **Media Library Management**

* Automatically categorizes movies, TV shows, and music, and supports automatic metadata fetching (e.g., cover art, descriptions, cast) from databases such as TMDB.
* Supports various formats, including MKV, MP4, FLAC, MP3, etc.

2. **Cross-Platform Streaming**

* Supports web, mobile (Android/iOS), TV (Android TV/Apple TV), and gaming consoles (e.g., Xbox).

* Real-time transcoding: Dynamically adjusts resolution and bitrate based on device performance (hardware acceleration required, such as Intel Quick Sync).

3. **User Access Control**

* Create multiple user accounts and assign different media library access permissions.

* Parental control: Restrict content ratings and playback time.

### **Default Login Information**

* **Default access port**: 8899
* **LAN access**: To access the Jellyfin web management interface, enter `http:NAS_IP:8899` in the browser address bar (e.g., `http:192.168.22.158:8899`).
* You can find the NAS device's IP address by going to the Network Settings in the Control Panel and clicking Network.

**Note**: Please do not change the WebUI port number, as this may disable the admin's ability to navigate through the UGOS Pro application center icon.

### **Resource Access Path**

This path is used to provide the Jellyfin application with media library folders that it can mount and read from.

* **Minimum Requirement**: At least 1 access path must be added.

* **Maximum Support**: Up to 5 access paths can be added.

### **Plugin Download Path**

A single path can be designated to store application plugins.

### **Path Mounting Rules：**

After the application is installed, you can view the corresponding paths in the **Configuration** section of the application details page.

* The first resource access path mounted by default corresponds to the `data`path within the application.
* For the second to the fifth mounted paths, the container path name will be the same as the directory being mounted.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250728/35efee69-c7aa-46b1-a154-d97dd627c04b.png)

## **Installation Guide**

To install the Jellyfin application, follow these steps:

1. Open the [App Center], locate the Jellyfin application, and click "Install the App."
2. Select the storage space and click "Next" to continue.
3. Set the resource access paths. The application will read the movies from these paths and match metadata such as posters.
4. Set the extension path. The application will read the plugin information from this path, then click "Install App" to proceed.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250728/0da0b7f9-b6ff-4c3a-977a-4ae0871e7633.png)

## **Access the Jellyfin Application**

You can access the Jellyfin application in the following ways:

### **Method 1: Access via App Center (Admin only)**

Click the Jellyfin app icon, and the system will redirect you to the login page.

### Method 2: Access via Local Network (Admin and Regular Users)

1. In your local network, use `http://NAS_IP:8899` to access Jellyfin. For example, if the NAS IP is `172.17.70.69`, enter `http://172.17.70.69:8899` in your browser to access the web management interface.
2. You can find the NAS device's IP address in the Control Panel. Go to "Network", click "Network Connection", and view the IP address of the NAS device.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250728/ac20284f-811f-4119-95b8-640993164e81.png)

### **Method 3: Access via Non-Local Network (Admin only)**

Admins can access Jellyfin in a non-local network environment through the Firefox app installed on the NAS system:

1. Log in to NAS using UGREEN Link, and open the Firefox browser.
2. After logging into Firefox, use `http://NAS_IP:8899` to access Jellyfin. For example, if the NAS IP is `172.17.70.86`, enter `http://172.17.70.86:8899` in the browser to access the web interface.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250728/384265b8-1f0c-4ecd-a89b-b4d22c145d9f.png)

**Note**: When logging in on untrusted devices, it is recommended to clear the browser’s access history in a timely manner to ensure data security.

### **Usage Tips**

1. For local network access, it is recommended to use browsers with better compatibility (such as Chrome or Edge) for the best experience.
2. When accessing NAS in a public network environment, be cautious about data security to avoid leaking sensitive information.
3. Admins should manage access passwords carefully to ensure their security.
4. If multiple users share the Firefox browser to access container apps, it is recommended to disable the "Remember Password" feature and regularly clear browsing history.

## **Initialization Configuration**

When using Jellyfin for the first time, you need to complete the initial setup:

1. **Set Display Language**

Choose your preferred language (e.g., "English") and click "Next" to continue.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250728/0f93897e-e16c-4312-bbfb-e2f290576ec5.png)

2. **Configure Account Information**

Set the username and password for the administrator account, then click "Next" to continue.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250728/8cfdc17e-1a09-4aa1-9f57-eed687a36e1f.png)

**3. Skip Media Library Setup**

You can skip configuring the media library during the initialization process, click "Next" to continue.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250728/db0365c9-003c-4144-8380-5443d0e28816.png)

**4. Configure Metadata Language**

Set the preferred metadata language based on your language environment, then click "Next" to continue.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250728/1428d991-703b-4f49-8172-2bbf14590037.png)

**5. Set Remote Access**

Leave the default settings as shown in the image and click "Next" to continue.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250728/79714129-bc39-4f19-aa60-1d8da82be348.png)

6. **Complete Initialization**

Once you reach this step, the initialization is complete. Click "Finish."

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250728/22b32ca4-e11e-4a4d-b292-733920fdfbcb.png)

7. After the setup is done, log in using the user account you just created.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250728/01144ec2-ddbd-41b0-b2c5-ee08ec4d6ab3.png)

## **Add Media Library**

After logging in, follow these steps to add a media library and manage your resources:

1. On the Jellyfin main interface, click the "Management Menu" button in the top-left corner. In the expanded side panel, click "Dashboard" to enter the page.
2. In the dashboard interface, click "Libraries" > "Library" > "Add Media Library". Categorize the media based on the content type (e.g., "Movies" or "TV Shows").

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250728/baa0ca51-6bdb-49c7-bd06-451d1e54e226.jpeg)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250728/19d39882-a6cc-4cc7-823f-a1140d7eccde.png)

### **Movie Media Library Setup Guide**

#### **1.** **Basic Configuration**

● **Content Type**: Select "Movies" mode (automatically matches standard movie metadata structure).

● **Display Name**: It is recommended to name the library by theme, such as "4K Ultra HD Cinema" or "Classic Nostalgia Library", for easier multi-library management.

● **Folder Path**: This points to the root directory of your movie resources, which is the resource access path set during the app installation (`volume3/media/movies`).

*Note*: For folder structure, a single-layer folder is recommended to avoid nested directories (`/movies/Movie Name(Year)/moviefile.mkv`).

#### **2.** **Metadata Optimization**

* Select "English" for preferred metadata language (this can be adjusted as needed).
* Choose "YOUR NATION" for Country/Region (to adapt to localized translations and release information).

#### **3.** **Other Parameters**

● Other parameters can be adjusted according to personal preferences.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250728/6670b51b-a9f1-4833-8068-ff4417617f2f.png)

### **TV Show/Variety Media Library Setup Guide**

#### **1.** Basic Configuration

● **Content Type**: Select **Show** mode (to accommodate the series/season/episode structure).

● **Display Name**: Name it by type, such as Domestic Dramas, Netflix Shows, Variety Show Collection, etc.

● **Folder Path**: Point to the root directory of TV shows/variety shows, which is the resource access path set when the application was installed (e.g.`/media/tv_shows`).

#### **2.** **Metadata Optimization**

* Select "English" for preferred metadata language (this can be adjusted as needed).
* Choose "YOUR NATION" for Country/Region (to adapt to localized translations and release information).

#### **3.** **Other Parameters**

● Other parameters can be adjusted according to personal needs.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250728/8aa3b432-e4ce-464a-bf42-adf25665be36.png)

## **Enable Hardware Transcoding on DXP Series Devices**

1. **Enable Hardware Acceleration Transcoding (Intel QuickSync - QSV)**  
   Enabling hardware acceleration transcoding can improve playback performance, reduce stuttering in high bitrate videos, and lower CPU load.
2. In the console’s left menu, click [Playback] > [Transcoding].  
   ● **Hardware Acceleration**: Select `Intel QuickSync (QSV)`.  
   ● **QSV Device**: Enter the device path `/dev/dri/renderD128`.  
   ● **Enable Hardware Decoding**: Check all supported codec formats.
3. After completing the settings, scroll to the bottom of the page and click "Save".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250728/b6af7ef4-dbb2-4fb2-9c35-c3063bf573b3.png)

## **Enable Hardware Transcoding on DH Series Devices**

DH series devices are based on the ARM architecture and come with a built-in VPU (Video Processing Unit) to support video hardware acceleration. When using Jellyfin to play videos, you can enable hardware transcoding by utilizing the VPU to improve transcoding performance.

1. In the left-hand menu of the dashboard, click [Playback] > [Transcoding].
2. For Hardware Acceleration, select Rockchip MPP (RKMPP).
3. Check all supported encoding formats.
4. After configuring, click the "Save" button at the bottom of the page.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250728/a6fa699a-f1b6-4900-bf26-1e2671bc1e98.png)

## **Notes**

When using the UGOS Pro system and container applications, please pay attention to the following points:

1. Do not arbitrarily migrate, move, rename, or delete the NAS paths mounted by the container to avoid functional issues or data loss.
2. If accessing the container application through a browser, disable the Multi-Gateway option in [Control Panel] > [Network] to avoid network conflicts.
3. Container applications are suitable for novice users. For more flexible configuration and management, it is recommended to use Docker to deploy container applications yourself, allowing for custom configuration files and advanced features.
