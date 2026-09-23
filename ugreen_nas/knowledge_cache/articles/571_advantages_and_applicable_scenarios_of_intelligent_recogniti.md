# Advantages and Applicable Scenarios of Intelligent Recognition

> **Article ID**: `571`  
> **Category**: `Application Guide > Theater > FAQ > Advantages and Applicable Scenarios of Intelligent Recognition`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/571  

---

Intelligent recognition is one of the core functions of the UGOS Pro system’s theater. It significantly improves the management efficiency of the library and the accuracy of video identification. By properly configuring and fully utilizing this feature, users can easily build a professional library to meet various needs for both home and enterprise applications. If you find that the intelligent recognition option is not available in your library, please check the theater’s settings switch status.

## **Advantages of Intelligent Recognition**

1. **Higher Matching Accuracy**  
   The intelligent recognition feature integrates multiple metadata sources (such as third-party databases) to more accurately match video information. Compared to a single data source, it performs better when handling complex media content.
2. **Automatic Correction**  
   Based on the video’s file name, folder structure, or other contextual information, intelligent recognition can automatically detect and correct erroneous or incomplete metadata, reducing the user’s need for manual editing.
3. **Ease of Use and Time Saving**  
   After enabling intelligent recognition, the system automatically matches and updates library metadata without requiring manual adjustment or editing one by one. This greatly saves time and effort when managing large-scale libraries.
4. **Wide Compatibility**  
   Intelligent recognition supports various types and formats of media files, ensuring all videos can be managed uniformly.

---

## **Applicable Scenarios**

1. **Complex File Naming Environments**  
   When media file names do not follow standard naming conventions (such as missing year or inconsistent formatting), intelligent recognition analyzes multi-dimensional information to automatically match the correct video data.
2. **Multilingual Video Management**  
   Intelligent recognition supports multilingual content well, especially Chinese titles and international titles, providing accurate metadata matching and localized information display.
3. **Home User Scenarios**

* **Quick Home Theater Setup:** Helps users organize large collections of videos with one click, providing cover images, plot summaries, and other detailed information to enhance the home viewing experience.
* **Children’s Content Management:** Parents can quickly categorize videos and mark age-appropriate content through intelligent recognition for easier management and access.

4. **Enterprise User Scenarios**

* **Project Video Classification:** Enterprises can use intelligent recognition to automatically organize training videos, promotional videos, and other content, improving work efficiency.
* **Localized Display:** Intelligent recognition provides a friendlier content display and management experience for multilingual enterprise users.

## **Usage Recommendations and Notes**

1. **Ensure Stable Network Connection**

The intelligent recognition function requires internet access to metadata sources. Please ensure the NAS system’s network configuration is normal to avoid scraping failures caused by connection issues.

2. **Optimize File Naming Conventions**

Standard naming format refers to including key information about the video in the file name, such as the title, year, resolution, etc. This information helps the scraping function more accurately match the video metadata.

**Recommended Formats**

* **Movie files:**  
  `Title (Year).format`  
  Example:`Inception (2010).mp4`
* **More detailed information:**  
  `Title (Year) - Quality - Language.format`  
  Example:`The.Roundup.Punishment.2024.1080p.WEB-DL.AAC2.0.H.264-Beans@chd`
* **TV series files:**   
  `SeriesName - SXXEYY.format`  
  Example: `Breaking Bad - S01E01.mp4`  
  (S = season, E = episode)

##### **Why Recommended?**

* **Year:** Avoids confusion between films with the same name (e.g., different versions of *Avatar*).
* **Quality:** Provides extra info for classification and quick retrieval.
* **Season/Episode Info:** Essential for accurately locating specific episodes in TV series.

##### **Notes**

* Do not use special characters (such as `*` or `?`) in file names, as they may cause system recognition errors or operational issues.
* Avoid overly long file names to improve system parsing efficiency.

Please refer to the [Theater Movie Naming Convention Guidelines](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6NzUwLCJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVJbmZvSWQiOjI1NywiYXJ0aWNsZVZlcnNpb24iOiIiLCJwYXRoQ29kZSI6IiJ9)

Using a consistent folder structure also facilitates system recognition.

3. **Manual Correction Assistance**  
   If intelligent recognition cannot fully match certain videos, you can manually adjust or add specific video information to ensure the completeness of the library.
