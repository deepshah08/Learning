# Anyone Can Learn: A Step-by-Step Guide to Building the "Simplest" NAS Movie Library with TMM for Movie Metadata Scraping

> **Article ID**: `422`  
> **Category**: `Application Guide > Theater > FAQ > Anyone Can Learn: A Step-by-Step Guide to Building the "Simplest" NAS Movie Library with TMM for Movie Metadata Scraping`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/422  

---

## Overview of TinyMediaManager

**TinyMediaManager (TMM)** is a lightweight and feature-rich open-source media management tool designed specifically for organizing and managing metadata of movies and TV shows. TMM's main functions include automatically scraping and organizing detailed information of movies, cover images, actor lists, director information, and other metadata, helping users build a neat and organized "Library". **This tutorial introduces how to use TMM as a standalone scraper and media file management tool, while using UGREEN NAS Theater for media reading, playback, and display.** It is very suitable for new NAS users. TMM supports multi-platform operation, including Windows, macOS, and deployment via Docker. Since TMM does not require long-term background operation, this tutorial will focus on its installation and configuration on the Windows system.

## Preparation Before Starting

### TinyMediaManager Download

First, visit the [official website](https://www.tinymediamanager.org/download/) of TinyMediaManager, select the version suitable for your system, download, and install it. This tutorial takes the Windows system as an example, downloading the Windows version of the TMM client.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/69b8d4b903a642e5bc5e7105dca94f8a.webp)

### Mount UGREEN NAS Movie Files to Local Computer

Use the SMB protocol to mount the UGREEN NAS movie folder to the local computer, which facilitates TMM to scan and manage the media files in the NAS. More operation details can refer to the["【Tutorial】How to Use SMB Protocol for Fast File Transfer Among Multiple Terminals in the Local Area Network?"](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMDYyLCJhcnRpY2xlSW5mb0lkIjozNTksImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)

![](https://file-us.ugreennas.com/admin/article/2025-09-16/6e81c2b458b54dfaa7fb3295653ef792.webp)

### TinyMediaManager Setup Wizard

1. The first time you start TMM, a setup wizard interface will appear. It is recommended to keep the default settings here and not change them arbitrarily, just click "Next".

![](https://file-us.ugreennas.com/admin/article/2025-09-16/6288f642ec1142169e860da905e04cb5.webp)

2. Next, add the "Library" directory. Select the directory of the media folder you want to manage. It is recommended to choose the movie and TV series folders on the NAS according to the actual storage location.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/2276e3ac196f42238b66b719412852cb.webp)

3. When prompted to select the source of movie metadata scraping, it is recommended to choose `themoviedb.org`, which is a universal movie and TV information database.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/21fa5b4bd9a64107aaa83cb6781f16db.webp)

4. When prompted to add directory data, you can skip it for the time being, and we will add it later. Continue to click "Next".

5. When setting up the metadata scraping for TV shows, also choose`themoviedb.org`, and then click "Finish" to end the setup process.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/2908470fb8544340a260c4a02cd6a7b8.webp)

So far, the download and installation of the TMM client are all completed, and the whole process is very simple!

Additional: [" 【Tutorial】How to Deploy TMM for Scraping Movie Information with Docker Compose"](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmNDIzIn0=)

## Use tinyMediaManager to Organize and Scrape Movie Folders

1. After opening the TMM interface, click the gear button in the lower left corner to enter the settings. Here you mainly need to configure two places:

● Movie Library directory

● TV series Library directory

Other settings can remain default.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/f62f4864bdc444a093de12bbb4ef1f73.webp)

2. After setting the "Library" directory, click the "Update "Library"" button, select "**Update All Library Directories**", and TMM will automatically scan and update the information in the Library.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/ebb81a0d6a7a44cd90662d38fd0bb944.webp)

3. Select all the added movie information, right-click and choose "**Search and Scrape Selected Movies - Auto Scrape Match**", and click the "Start Scraping" button, TMM will start to automatically download movie covers, nfo files, and other related information.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/f78ace1077ae4172b02e91f5546163ba.webp)

4. Some movies may not match automatically, in which case you can manually enter the Chinese name of the movie to search. If still unable to find, you can go to Douban Movie, search for the corresponding IMDb link of the movie, copy the number in the link (e.g., `tt11155284`) to search, which usually can obtain the detailed information of the movie.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/579669f449b3440880e25fc619e0f8a5.webp)

5. The scraping of TV shows is similar to movies, but TMM will organize and categorize each episode of the TV show for easy classification and management. After all updates are completed, you can see the downloaded nfo movie information, poster cover images, etc., in the movie folder:

![](https://file-us.ugreennas.com/admin/article/2025-09-16/c5ea91eca1d34e0e85a8b76b01013f35.webp)

6. After scraping is completed, you can also choose to "Rename & Organize" the movie files to standardize the naming. However, it should be noted that if you are using PT seed download movies, renaming may cause the seed files to fail to continue uploading, so please consider whether to rename it yourself.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/67f67a69c7b644cda2416a25f8d73b07.webp)

## Use the Theater to Load TinyMediaManager-Organized Movies

1. On the homepage of the UGREEN NAS "Theater", click the avatar icon in the upper right corner to enter the console.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/7376f92dfdc3481ebf2c64b4f16f38ef.webp)

2. In the "Library", click "Add Library", select the completed scraping movie directory media folder, and click "Apply". It is recommended to cancel the built-in metadata scraper of the "Theater" or default to check "Prioritize Reading Local Information".

![](https://file-us.ugreennas.com/admin/article/2025-09-16/ed1a17829f104a66ad0ec5f103c72a15.webp)

3. After the "Library" is scanned, return to the homepage of the "Theater", and you will see the latest poster wall. Click on the movie card to view detailed movie information.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/66b20dc2d589451f89e1d69dd2b92daa.webp)
