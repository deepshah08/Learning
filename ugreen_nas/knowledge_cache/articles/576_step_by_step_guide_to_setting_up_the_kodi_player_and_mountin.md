# Step-by-step guide to setting up the KODI player and mounting NAS media shares to build a local media library

> **Article ID**: `576`  
> **Category**: `Application Guide > Theater > FAQ > Step-by-step guide to setting up the KODI player and mounting NAS media shares to build a local media library`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/576  

---

## **Introduction to KODI**

KODI is a powerful media player and library management software that supports installation on a wide range of devices, including smart TVs, Windows, Linux, Android, iOS, and even platforms like Raspberry Pi. By using KODI for decoding and playback, you can significantly reduce the resource load on your NAS while ensuring smooth playback of 4K Blu-ray source files—delivering an enhanced audio-visual experience.

This tutorial will walk you through the detailed steps of installing and configuring KODI, as well as mounting media shared folders from your UGREEN NAS in KODI.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/3f4ecccd-a519-4e6e-b152-048e0ca34921.png)

## **Downloading KODI**

KODI is a free and open-source software that runs on multiple operating systems. For security reasons, it is recommended to download the installation package suitable for your platform from [the official KODI website](https://kodi.tv/download/). For the purpose of this tutorial, we will use the Windows platform as an example.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/e76eeaf6-d5e6-4daf-87e2-83a42b672516.png)

## **Installing KODI**

1. Open the downloaded installer and follow the on-screen instructions to complete the installation (click “Next” until the process is finished).
2. Once installed, you can launch KODI either by clicking the desktop shortcut or by checking the “Run KODI” option at the end of the installation.

**Tip:** The installation process on Android devices and smart TVs is similar and can be carried out by referring to the steps in this tutorial.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/0b2edac3-5db1-402b-92c8-cdae9f1259b7.png)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/98a21d19-e9fb-4d21-bda2-8c37245ade2f.png)

## **Mounting NAS Media Shared Folders**

1、On the system settings page, go to the [Media] section.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/95492a3e-2440-4dc2-99a0-9ec4d68e0ac0.png)

2、After entering the Media settings page, go to [Library] > [Videos].

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/6e48798b-ba6d-4370-8ec4-4a6d31b1411e.png)

3、Click the "Add videos" button, then select "Browse".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/087ff0b5-714f-4333-ae43-431f625f625a.png)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/ac711f24-9472-4738-8eb2-d402737ca784.png)

4、On the "Browse" page, you can choose from several methods to connect to and access the location where your videos are stored:

* If the videos are on your local computer or NAS, you can select the local file system, then navigate to the "Share" folder, where your shared media folders are located.
* If you're using a NAS on the same local network, you can choose "Windows network (SMB)" to access the NAS shared folders.
* If your NAS doesn't appear under the SMB list, you can manually add it by selecting "Add network location" and entering the NAS's IP address.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/fd044a3c-14ba-4c90-bc2d-27de60f6d717.png)

5、In this tutorial, we will use the WebDAV connection method to remotely mount the shared folder on the NAS. On the "Add network location" page, select WebDAV as the protocol, then enter the NAS IP address, port number, username, and password.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/fe877b7e-ee72-4f82-ba45-fc01f7e5fc6e.png)

**Note:** If you choose the WebDAV protocol, make sure the WebDAV service is enabled on your NAS.

**To enable WebDAV on a UGREEN NAS running UGOS Pro, follow these steps:**

* Log in to the UGOS Pro management interface and go to [Control Panel] > [File Service] > [WebDAV].
* Check "Enable Service", then click "Apply" to activate the setting.
* You can adjust the access ports in "Advanced Settings" (default ports: HTTP: 5005, HTTPS: 5006).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/709e9581-c1e2-4b21-9d15-fa3643d40698.png)

6、After clicking "OK", return to the shared folder browsing page and locate the shared folder you just configured.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/b21edf56-49e1-4b17-b69f-db41b473fba9.png)

7、Click to enter the NAS shared folder and find your personal movie folder—for example, my movies are all stored in the “Movie” folder. Once inside the movie folder, it is recommended to scrape movies and TV shows separately.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/2522d4f5-e40c-437f-8e7a-855116d2d2de.png)

8、You can also rename the folder here or simply click “OK”.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/a65f5c4d-11ff-48b9-9de7-dd8bb8900720.png)

## **Setting up the KODI Media Library**

1、After clicking OK, a dialog box to configure the scraper will appear. For the first directory, select Movies. In Settings, it is recommended to change the preferred language to English, while other settings can remain unchanged. Then click OK again.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/28f3a405-bd8c-4b30-9901-ce589fc07158.png)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/c87adb8a-077f-4f03-b746-bcd08b9321fb.png)

2、After configuring the scraper, click the options icon at the bottom left and select “Update library”. KODI will then automatically scrape the movie information.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/d5e69ca9-177a-446a-9773-670ae8394a56.png)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/7719d911-1cee-4957-9831-2ac660b67d45.png)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/d80cf420-dc52-4a17-a1e9-59a64784820a.png)

**Note:** KODI uses TMDB as the default scraper, and its performance depends on your network environment and the file naming conventions. It is recommended to organize your movie information in advance using TMM software. For related tutorials, please refer to:[[Tutorial] How to Deploy TMM for Scraping Movie Information with Docker Compose to Create the Perfect NAS Poster Wall?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTI4MiwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0MjMsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

3、After a short wait (loading time depends on the number of movies), the KODI main interface will display the movie poster wall.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/3794319b-08e7-4683-812d-1d6fd8a42008.png)

4、Double-click a poster or right-click to play the movie. On the playback screen, you can also customize settings as needed.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/a931fc64-86ce-4150-9d3f-cbc09dd6b896.png)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/53a43aff-e703-43b6-925b-ee5b51609917.png)

5、You can also long-press or right-click and select “Information” to view the movie synopsis and cast & crew details.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/771f4050-bf7b-46a9-a4a7-a6f22889b536.png)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250717/2af36233-b246-4293-a965-b05927a6d705.png)

**Note:** TV show scraping works the same way as for movies. It is recommended to organize them by folder categories. For more features and settings, feel free to explore the [KODI official forum](https://forum.kodi.tv/) or search online for additional information.
