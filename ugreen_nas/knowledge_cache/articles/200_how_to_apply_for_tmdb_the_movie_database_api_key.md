# How to apply for TMDB (The Movie Database) API key

> **Article ID**: `200`  
> **Category**: `Application Guide > Theater > FAQ > How to apply for TMDB (The Movie Database) API key`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/200  

---

## **Introduction to TMDB**

TMDB (The Movie Database) is a public film and television database that provides comprehensive data on movies, TV shows, actors, and production crews. Often referred to as the "Wikipedia of the film and TV industry," TMDB allows users to contribute by creating and editing entries. It offers an open API that enables users to retrieve movie posters, summaries, and other metadata.

The "Theater" application in UGOS Pro is preconfigured to use TMDB as its data source, eliminating the need for manual API key input. However, users also have the option to configure a custom TMDB API key if needed.

**Notes:** If you are unfamiliar with configuring a TMDB API key or modifying the HOST settings, it is recommended to keep the default configuration. Users with specific requirements can adjust the TMDB data source settings in the console as needed.

### **Advantages of Using a Personal API Key**

1. **Ensures Access Reliability** – A personally registered API key helps prevent data retrieval failures caused by public API rate limits.
2. **Improves Service Quality** – With a personal API key, users can customize language preferences, movie rating systems, and other settings for more accurate metadata.

**Note:** Usage of TMDB data must comply with [the Term of TMDB Use](https://www.themoviedb.org/terms-of-use).

## **Apply for a TMDB API Key**

Follow these steps to apply for a TMDB API key:

1. Visit the [**TMDB official website**](https://www.themoviedb.org/) and log in to your account. If you don’t have an account, create one first.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250612/3c479e1e-6da8-4fa4-b4c5-dd4e0c486277.png)

2. After logging in, click on your "profile avatar“ in the upper-right corner and select [Account Settings].

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250612/d37d6263-f8c5-4521-a051-b255d078f470.png)

3. In the [Account Settings] page, navigate to the [API] section on the left sidebar and click "click here" under [Request an API Key].

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250612/2b455a50-3011-405a-a1ad-ca829ec0a82c.png)

4. Select "Developer" as the account type when creating the API key.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250612/cefa1a7c-2f6c-4497-9375-20f9c3cc08cd.png)

5. Read and agree to the Terms of Use, then fill in the application details:

* **Type of Use**: Select Personal.
* **Application Name**: Choose a custom name, e.g., UGREEN ”Theater“.
* **Application URL**: Enter your UGREEN NAS IP address, such as http://192.168.1.31. You can find this in [Control Panel] > [Network] > [Network Connection].
* **Application Description**: Briefly describe your application and how you will use the API.

```
Film and Television Center is a home multimedia application, which is used to obtain TMDB video data and poster pictures to build a beautiful poster wall.
```

* **Personal Information**: Enter details such as your home address (this information is stored by TMDB and not accessed by the Theater).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250612/462f8691-a0f2-47af-8570-68407652c68a.png)

6. After completing the form, click "Submit" and wait for TMDB to generate your API key.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250612/a92718c6-b859-4813-b11b-2301cf908778.png)

7. After generating the API key, copy and save it securely. You will need this address later during the configuration process.

### **Configure TMDB Data Source**

1. Open the “Theater” app and click the [Settings] button in the upper-right corner to enter the Theater settings page.

2. On the settings page, click the [Data Source] option. Find The Movie Database (TMDB) and tap to enter the TMDB configuration screen.

3. In the TMDB configuration page, locate the API Key input field. Paste the TMDB API key you previously obtained into the field.

4. Click the [Check] button to verify whether the API key is valid. If the test is successful, you will see a confirmation message indicating the verification passed.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250612/bc6dd855-d5f7-4785-8849-f1662e70a78c.png)

5. Click [Apply] to save the TMDB data source configuration.

### **Adjust Library Video Information Source**

1. After configuration, set the library's video information source to TMDB to fetch posters and other metadata.

2. Return to the settings page and click the [Library] option.

3. In the library list, select the library for which you want to change the data source.

4. Click the [···] button on the right side of the library and select [Edit].

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250612/8cd9b176-7075-43fe-b360-f64b4f293a29.png)

5.On the edit page, locate the [Video Info] option.

6.Long-press to drag and reorder the sources, setting TMDB as the highest priority.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250612/8cf0b4ea-446b-445c-a596-1c6f0828d6e1.png)

7. Click the [Apply] button to save the settings.

### **Rescan the Library**

1. After saving the settings, return to the Library page.

2. Click the [···] button on the right side of the media library and select [Scan].

3. In the scan options, click [Scan and Replace All]. This will rescan all files in the media library and fetch the latest metadata and posters from TMDB.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250612/dcda4c08-3a39-4561-911c-8cd236170624.png)

**Note:** If your API key verification is successful, there is usually no need to configure HOST. The HOST configuration is used to resolve TMDB’s correct IP address, bypassing DNS pollution issues, ensuring stable access to the data source.

## **About TMDB**

### **Metadata Not Displaying Correctly**

If metadata does not display correctly after configuration, try the following steps:

1. Ensure the TMDB API key is correctly entered and saved.
2. Check whether the TMDB API detection confirms a successful connection.
3. Verify that the IP address configured in the HOST settings resolves correctly.
4. If the issue persists, try using "Scan and Replace All" to manually refresh the media library.

### **If Configuring the TMDB Data Source Require Additional Fees or Not**

TMDB provides basic services for free, but for advanced features or high-volume access (such as frequent metadata updates), you need to register a TMDB account to obtain an API key. For details on usage policies, refer to TMDB's official guidelines.

## **About HOST Configuration**

In some regions, TMDB's API may encounter DNS resolution failures. To address this, the Theater app provides a HOST configuration option, allowing users to manually assign the correct IP address for TMDB. This bypasses incorrect public DNS resolution and ensures stable access to the data source.

**Please note:** Configuring the HOST file is intended solely to optimize the TMDB metadata scraping process, ensuring that the Theater app can accurately retrieve movie metadata such as posters and descriptions. UGREEN NAS does not provide any video resources — users are responsible for managing their own video downloads and storage.

### **What Can HOST Configuration Do?**

When using the Theater app, the metadata scraping function relies on external metadata services to retrieve detailed movie information.  
Due to network restrictions or issues with service providers, this scraping function may not always work properly. By configuring the HOST file, you can specify IP addresses to resolve those metadata services, effectively bypassing potential network issues and ensuring smooth metadata retrieval.

### **Obtain TMDB's IP Address**

1. Visit [IPADDRESS.COM](https://ipaddress.com/).

2. Enter api.tmdb.org in the search bar and press Enter.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250612/d12fc92e-bf10-4a62-9411-50b2f3e8132e.png)

3. Scroll down the page to view the IP address resolved by the system. Copy and save it properly, as it will be used later during the configuration process.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250612/f6d65055-b804-4967-b37b-58e6c902dd57.png)

### **HOST Configuration Method**

1. Open the [Theater] app and click the [Settings] button in the upper-right corner to enter the settings interface.

2. Click [Data Source], select [The Movie Database], and paste the previously obtained IP address into the HOSTS Configuration input field. Make sure the format is correct: IP address + space + domain name.

3. In the TMDB configuration, enter the HOST in the following format, for example:

```
52.85.151.18 api.themoviedb.org
```

4. After verifying the information, click "Import" to complete the setup.
5. Click "Apply" to save the changes.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250612/3d943a15-6c56-4dfb-86c2-50c8aec5906c.png)

### **Glossary**

**DNS Pollution:** The act of forging or altering DNS responses to prevent users from accessing legitimate websites.

## **Related Links**

[[Tutorial] How to Configure HOSTS?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjo0MjQsImFydGljbGVJbmZvSWQiOjIwMSwiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIiLCJwYXRoQ29kZSI6InBybzAwMixzajM1YmcifQ==)

[What Is the Purpose of Configuring The Movie Database (TMDB) Data Source in ”Theater“?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjoxNjkyLCJhcnRpY2xlSW5mb0lkIjo1NTcsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIn0=)
