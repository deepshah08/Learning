# What is the Priority Order of NFO Scraping, TMDB Scraping, and Intelligent Scraping in the Theater?

> **Article ID**: `462`  
> **Category**: `Application Guide > Theater > FAQ > What is the Priority Order of NFO Scraping, TMDB Scraping, and Intelligent Scraping in the Theater?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/462  

---

## Introduction to Video Scraping

Video scraping is the process of automatically retrieving movie information from online databases or other sources. Common metadata includes the movie title, director, cast, release date, plot summary, and poster. In the Theater on UGREEN UGOS Pro, video scraping can automatically search online databases and match file names to retrieve relevant information. Currently supported scraping methods include **NFO scraping**, **TMDB scraping**, and [**Intelligent Identification**](%20) .

### Three Scraping Methods Supported in the Theater

1. **NFO Scraping (Read local information first)**

● **How it works:** NFO Scraping retrieves video information from local NFO files, which usually contain user-defined metadata. When "Read local information first" is enabled, the system will prioritize metadata from NFO files.

● **Recommended for:** Scenarios where NFO files are already organized and custom information needs to be preserved.

2. **TMDB Scraping**

● **How it works:** Retrieves metadata such as movie title, cast, synopsis, and posters from The Movie Database (TMDB).

● **Recommended for:** Suitable for videos without NFO files or when accurate media information is preferred from TMDB.

3. **Intelligent Recognition**

● **How it works:** The system uses algorithms to automatically identify the file name and properties, selecting the best-matched metadata from the database.

● **Recommended for:** Recommended when there are no NFO files and optimal metadata recognition is desired.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/b1e22ed87c3744bf94891058f568c5b2.webp)

## Default Scraping Priority in Theater

When NFO scraping, TMDB scraping, and Intelligent Recognition are all enabled in UGREEN NAS Theater, the system retrieves video information in the following order:

1. **Read local NFO file first:** Before adding resources to the library, if a local NFO file is found, the system will directly use the metadata from the file and skip other scraping methods.

2. **TMDB scraping if no NFO file is found:** If there is no NFO file, the system will attempt to fetch metadata from TMDB. If an NFO file is added to the library afterward and is identified as the same video, the information will be merged automatically.

**Notes:**

● If you only want to use local NFO files to scrape video information, please disable TMDB and Intelligent Recognition, and enable only "Read local information first (NFO Scraping)."

● During downloads, if the video file enters the library before the NFO file, the system may identify them as two separate resources. You can manually re-identify the resource after the download is complete to merge the information.

● If a video fails to be scraped or cannot be recognized, you can right-click the video and choose "Manual identification" or "Rescan" without rescanning the entire library.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/b21e58d4bf084a33b3c651cd6bb8ec05.webp)

## How to Adjust the Priority Order of NFO, TMDB, and Intelligent Recognition

To manually adjust the priority order of metadata scraping methods, follow these steps:

1. Go to [Theater] > [Settings].

2. In the Library section, select the library you want to edit, click the **"···"** button in the top-right corner, and choose **"Edit"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/6443881e09314744b27f048a369d1e7a.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-10/88715ad5dcf947819cd5f8b141d98c2f.webp)

3. On the pop-up "Modify library" page, locate the scraping settings under the "Video Infomation" section:

● **Drag to reorder the TMDB/Intelligent Recognition options:** For example, move the TMDB scraping method to the top and disable local NFO file recognition. The system will then prioritize the TMDB scraping method.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/8b1cbe358a784b93a0ff082e29479cc0.webp)

● **Check or uncheck scraping method options:** For example, uncheck the Intelligent Recognition and TMDB scraping options, leaving only "Read local information first." In this case, the system will use only NFO file scraping.

![](https://file-us.ugreennas.com/admin/article/2025-09-10/a61db2beb8b148109a05f81fdf8df12b.webp)

4. After making adjustments, click **"Apply"** to save the settings.
