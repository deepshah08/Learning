# Theater Movie Naming Convention Guidelines

> **Article ID**: `257`  
> **Category**: `Application Guide > Theater > FAQ > Theater Movie Naming Convention Guidelines`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/257  

---

This article provides a detailed introduction to the naming conventions for the core feature of UGREEN NAS Theater—movie scraping. If you have any confusion regarding scraping movie posters, reading this article will be helpful! Let's first take a look at the movie screenshot after the scraping process is completed.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250729/b03d22c1-f960-44a1-9d39-6c20fa094e09.png)

## **What is Movie Scraping?**

Movie scraping is the process of retrieving movie information from movie databases or other online resources. Typical information includes movie title, director, cast, release date, plot summary, posters, and other metadata. In UGREEN NAS Theater, movie scraping automatically searches online databases to retrieve movie information that matches the file name. This information is used to enrich the content in the Theater, providing more comprehensive movie details and a more engaging interface experience.

Overall, scraping technology transforms your experience from simple folder browsing to on-demand movie viewing, offering you a more convenient and enjoyable watching experience.

## **Scraping Naming Conventions**

The Theater has strict naming rules for movie files. If files are not organized according to these conventions, although it is sometimes possible to scrape successfully with a matching keyword, it often leads to scraping recognition errors or failure to identify the files. Below are some examples of naming conventions:

1. Correct Naming Convention Example:

* Fast Charlie 2023 CAN BluRay 1080p TrueHD5.1 x265 10bit-CHD

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250729/ed3dbd14-c892-4b58-8298-fb46e44e1b6b.png)

In the examples above, we follow the standard naming convention, which is movie title + release year, along with specific movie encoding information. Typically, this format can be directly recognized by the Theater, without the need for manual modification.

2. Non-compliant Naming Examples:

* Ten.Thousand.Worlds.S02.2022.1080p.WEB-DL.H265.AAC-ZeroTV
* The Dark Knight][2024][8G][MP4][Chinese-English Bilingual Audio with Dual Subtitles]

For non-compliant naming, there is often a large amount of irrelevant content, such as Chinese prefixes and suffixes, BT resource identifiers, etc., which complicates the scraping process in the Theater. Therefore, we should remove these extraneous elements and only retain the movie title and release year.

Please note:

1.When naming, ensure the title is clear and concise, avoiding information unrelated to the movie content.

2.For TV series, include the season and episode numbers to allow for more accurate scraping.

### **Movie Naming Convention**

The movie file name should begin with the full title of the film, which can be in either Chinese or English. Additional relevant file information may be added thereafter. If there are movies with the same title, the release date of the film must be included in the file name.

Example:

1. Film Title (Year)

Fast Charlie (2023)

2. Translation Name + Original Name + Year + Cut Version + Release Notes + Resolution + Source + Audio/Video Codec - Release Group Name

Fast Charlie 2023 CAN BluRay 1080p TrueHD5.1 x265 10bit-CHD

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250729/a0c7f70e-fa36-4973-8030-ad24d3ce6d7c.png)

**Note:**

1. Common separators such as the English period “.” should be used between the film title and each section of information.

2. Additional information after the film title in the file name (such as bluray, x264, 2160p, etc.) is considered extended information and will not affect scraping.

3. The fields following the year are extended information, and other relevant details can be added as needed.

### **TV Series Episode Naming Convention**

The filename for TV series episodes should start with the name of the series, ensuring that the series name is consistent across all episode files of the same series. The name can be in Chinese or English. Following the series name, the year, season number, and episode number should be included. For example: *A Certain Scientific Railgun.2010.S01E01*.

For bonus materials, special episodes, or other non-standard episodes of a TV series, the filename should still start with the series name, but the season number must be set to 0, and the episode number should be specified. For example: *A Certain Scientific Railgun.2010.S00E01.mkv*.

**Please note:**

Filenames should be concise and clear, avoiding any irrelevant information to ensure accurate scraping.

Use the standard season and episode format, such as S01E01 for Season 1, Episode 1.

For special types of files like bonus materials or special episodes, appropriate identifiers should be used, such as S00E01.

## **Manual Identification and Matching**

When the automatic matching of movies or TV series is incorrect, you can select the incorrect item in the media center, click on [··· ]> [Manual Identification], and enter the correct media information to match. Choose the correct media information from the matching results and click on it. The media center will then update the item with the correct information.
