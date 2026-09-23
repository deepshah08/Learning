# Music Tag Web Quick Start Guide

> **Article ID**: `672`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Music Tag Web Quick Start Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/672  

---

# **App Introduction**

Music Tag Web is a music tag editor that supports batch automatic editing of metadata such as title, album, artist, lyrics, and cover art for music files. It supports a wide range of audio formats, including: FLAC, APE, WAV, AIFF, WV, TTA, MP3, M4A, OGG, MPC, OPUS, WMA, DSF, MP4, and more.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/485f49e8-d38c-4d54-bae0-65d0014cde75.png)

## **Default Login Information**

* **Default Username:** admin
* **Default Password:** admin
* **Default Access Port:** 8022
* **LAN Access:** In your browser's address bar, enter `http://<NAS LAN IP>:8022`.

For example, if your NAS IP address is `172.17.70.86`, enter `http://172.17.70.86:8022` in your browser.

**Note:**

* You can find your NAS IP address by going to [Control Panel] > [Network] > [Network Connection].

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/4b7fbfa3-d808-4826-9074-16453e17615b.png)

* Do not modify the WebUI port number, as this may cause the shortcut feature in the UGOS Pro App Center to stop working for the administrator.

# **Installation Guide**

To install the Music Tag Web application, follow these steps:

1. Open the "App Center", find Music Tag Web in the app list, and click “Install”.
2. Select the folder where your music files are stored as the resource access path, then click “Install”. Please ensure a stable network connection during the installation to avoid any interruptions.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/84e6651e-2fad-4017-95c0-094a8eff90e9.png)

# **Accessing the Music Tag Web Application**

You can access the Music Tag Web app using the following methods:

## **Method 1: Access via App Center (Admin Only)**

Within the local network, the administrator can click the "Music Tag Web" app icon in the App Center, and the system will redirect to the login page.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/b96948df-4e18-4d08-a3f4-f9c2780d70db.png)

## **Method 2: Access via LAN (For Both Admin and Regular Users)**

Within the local network, access the app by entering `http://<NAS LAN IP>:<port>` in your browser. For example, if the NAS IP is `172.17.70.86`, enter `http://172.17.70.86:8022` in the browser to access it.

# **User Guide**

## **Accessing the Application Page**

Enter the following address in your browser’s address bar to access the Music Tag Web login page:

```
http://<NAS LAN IP>:<port>
```

The default username and password are both `admin`. (It is recommended to change the password immediately after logging in to ensure account security.)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/a95d5b61-d221-4439-bbf0-f0ae729b3a74.png)

## **Browsing Music Files**

After logging in, the left sidebar will display the shared folder paths mounted during installation—that is, the folders you have added.

1. If your music is organized into multiple folders, you need to navigate through the folder hierarchy step by step to see the music files inside.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/c77f7622-d1d8-4ea0-aad4-5cf9b781d85a.png)

2. The right side of the page, the dashboard, will display all the music files in the current folder.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/92b00853-4985-4b7f-be72-cd6f90c1378c.png)

## **Manual Editing and Scraping of Music Information**

Music Tag Web supports manual metadata editing and information scraping for individual music files:

1. Click the music file name to open the metadata editing interface.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/3076cce7-5e39-46be-bcb9-63b8703ff3f2.png)

2. Click the [Settings] icon in the top-right corner to select the tag source and the metadata fields to display (the field order will affect how information is arranged on the interface).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/39f86458-a2c1-457d-85da-2dd6f9818a5c.png)

3. Click the [Search] button to have the system look for matching information using the selected tag source.
4. Once the correct music information appears in the right panel, click [Save Info] to complete the manual scraping.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/4182580b-dec0-4393-810c-87a2d142513d.png)

## **Automatically Scrape Music Information in Batch**

If you want to match music information for all files within a folder, you can use the [Auto Scrape] feature:

1. Select the target folder, then click the [Auto Scrape] button in the toolbar.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/484a7703-d1fe-43b0-a824-aa7b60de18bc.png)

2. The system will automatically match the metadata for each song using the selected tag source and write the information into the music files.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/605b7dd4-9712-499e-9999-a885237b0436.png)

**Scraping Mode Description:**

* **Easy Mode:** Matches based only on "Title", offering faster speed but with a higher chance of incorrect results (e.g., duplicate titles or cover versions).
* **Strict Mode:** Requires a match of "Title + Artist" or "Title + Album", providing higher accuracy, though mismatches may still occur. It is recommended to run a small test batch first and manually verify the results during bulk processing.

## **Organizing Music Files**

Music Tag Web offers a powerful automated music file organization feature. It can intelligently create categorized folders based on embedded tags such as artist, album, genre, etc., helping you manage your music library more efficiently and quickly locate your favorite tracks.

**Steps to use the feature:**

1. In the Music Tag Web interface, check the music folder(s) you want to organize. You can select a single folder or multiple folders for batch processing.
2. Click the [Organize Files] button. You can customize the root directory where the organized music files will be saved. If no custom path is set, the system will use the default location. Click "Save" to begin preparing the organization task.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/60a9ba0b-b490-4913-a2f0-76eb78e84c0d.png)

3. You can view detailed information about all past organization tasks on the “Operation Log” page.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/0758cb1d-2fbc-4875-800b-847d07bcb043.png)

**Please note:**

* The application may be temporarily inaccessible during the organization process; this is normal.
* The page will automatically refresh once the file organization is complete.
* The organization process will change file paths, so it is recommended to back up important data beforehand.

## **Change Password**

1. Click the user icon in the top-right corner, then click [Backstage Management].

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/2ab4b275-e2b3-459b-b538-b3619e12bb6a.png)

2. On the admin panel page, click the user icon in the top-right corner, then click “Change Password.”

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/46248a87-0b30-4be6-b172-769f01fb84e3.png)

3. Enter your current password, set a new password, and click **“Change Password”** to apply the changes.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/95ddb02d-e8cb-4f07-bbfc-329f2f65da85.png)

## **Notes**

* Use accurate file naming whenever possible (e.g., “Artist - Song Title.mp3”) to improve scraping accuracy.

* Before using the automatic scraping or organizing features for the first time, it is recommended to manually process a sample set to verify that the scraping results meet your expectations.

* When using strict mode, carefully review the results to avoid incorrect metadata writing.

* The images used in this tutorial are developed and maintained by third parties; this guide is for reference only. UGREEN is not responsible for risks caused by improper operations, software bugs, or image updates, such as file corruption or data leakage. Please choose trusted images to ensure system and data security.
* Container file paths can be set as you prefer. When accessing via web, container ports and local ports must match, and local ports of different containers must not conflict.
* The image only provides a setup tutorial; for detailed usage and features, please refer to online resources. Follow the official image updates for configuration changes and bug fixes.
* It is recommended to store the container application’s configuration directory on storage space created by an SSD to avoid performance issues caused by slower mechanical hard drive read/write speeds.
