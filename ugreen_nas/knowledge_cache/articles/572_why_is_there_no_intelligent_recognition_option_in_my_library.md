# Why is there no "Intelligent Recognition" option in my library?

> **Article ID**: `572`  
> **Category**: `Application Guide > Theater > FAQ > Why is there no "Intelligent Recognition" option in my library?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/572  

---

## **[Issue Description]**

When creating or editing a library, you may notice that under the metadata scraping options, only "TMDb" is available and the "Intelligent Recognition" option is missing. As a result, the library cannot automatically retrieve and match movie information using the intelligent scraping feature.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250708/eb60c9a8-6ed6-4efc-bfd2-2d0da0342695.png)

## **[Cause Analysis]**

This issue is usually due to the Intelligent Recognition feature being disabled in the Theater app's Console. When this feature is turned off, the library cannot use Intelligent Recognition as a metadata scraping source and will rely solely on the TMDb database.

## **[Solution]**

**Step 1: Check the Intelligent Recognition Toggle**

1. Log in to the UGOS Pro system using an administrator account.
2. Open the "Theater" app and go to the "Console" interface.
3. Click “Settings” in the left-hand menu and locate the “Intelligent Recognition” toggle.
4. Check whether the toggle is currently turned off.

**Step 2: Enable the Intelligent Recognition Feature**

1. If the feature is disabled, switch the toggle to “On”.
2. Click “Apply” to save the settings.

**Step 3: Verify That the Feature Is Active**

1. Return to the Library management interface. When creating or editing a library, check whether “Intelligent Recognition” now appears as an option under metadata scraping sources.
2. Select “Intelligent Recognition” as the scraping method and rescan the library to confirm that the feature is working properly.

**[Additional Info: Advantages and Use Cases of Intelligent Scraping]**

1. **Advantages of Intelligent Scraping**

* **Higher Match Accuracy:** Compared to using the TMDb database alone, Intelligent Recognition integrates multiple metadata sources, increasing the accuracy of content identification.
* **Auto-Correction:** It can automatically correct incorrect metadata based on video filenames, folder structures, and more.
* **Time-Saving:** Reduces the need for manual adjustments or post-editing, significantly simplifying library management.

2. **Ideal Use Cases**

* **Complex File Naming Environments:** When video files have irregular or incomplete names, intelligent scraping is more effective at recognizing and matching the correct content.
* **Multilingual Films:** For movies with multilingual titles—such as English names or other localized titles—intelligent scraping provides more accurate matching results.

## **[Notes]**

1. **Ensure Stable Network Connection**

The Intelligent Recognition feature relies on internet access to fetch metadata. Make sure your UGREEN NAS is properly configured and can connect to external services.

2. **Optimize File Naming Conventions**

Use standardized naming formats (e.g., “Movie Title (Year)”) to improve scraping accuracy and success rate. Refer to the [Theater Movie Naming Convention Guidelines](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6NzUwLCJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVJbmZvSWQiOjI1NywiYXJ0aWNsZVZlcnNpb24iOiIiLCJwYXRoQ29kZSI6IiJ9)

3. **Enable Intelligent Recognition**

When using the Theater app for the first time or creating a new library, administrators are advised to check and enable the Intelligent Recognition feature to avoid repeated setup.

4. **Keep UGOS Pro System Up to Date**

Regularly update your system and the Theater module to access the latest improvements in intelligent recognition algorithms and feature enhancements.
