# How to Configure HOST?

> **Article ID**: `201`  
> **Category**: `Application Guide > Theater > FAQ > How to Configure HOST?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/201  

---

## **Introduction**

When using the UGREEN "Theater" application, the TMDB (The Movie Database) API is often used to retrieve movie and TV show posters and other information. Occasionally, you may encounter DNS resolution issues that prevent a connection to the TMDB server. This is typically caused by incorrect domain name resolution, preventing API requests from returning data and disrupting the functionality of the application. In simple terms, the server address cannot be found, so the required information cannot be retrieved.

To ensure normal use of the Video Scraper feature, this guide will walk you through how to modify the UGOS Pro system's "Theater" HOSTS configuration, manually specifying the TMDB API server’s IP address to ensure stable API connections.

**Notes:**

1. Configuring the HOST file is intended to optimize the scraping process of TMDB movie data, ensuring that the Theater app can accurately retrieve metadata such as posters, descriptions, and more. UGREEN NAS itself does not provide any video content; users are responsible for managing their own download sources and media file storage.
2. The Theater app in UGOS Pro is preconfigured with TMDB as the default data source, so there is no need to manually enter an API key. However, an option is available for users to customize the TMDB API key if desired.

## **Steps**

To resolve DNS resolution issues, the "Theater" offers a HOST configuration option, allowing users to manually configure the correct TMDB IP address, bypassing incorrect DNS resolutions to ensure proper access to the data source.

#### Here are the steps to retrieve TMDB API server IP address:

### **Find the IP Address of the TMDB API Server**

Before modifying the HOSTS file, you need to obtain the correct TMDB API IP address. Since DNS resolution might fail and not resolve to the correct IP, you can use the following methods to get the correct IP address:

1. Use an online IP lookup tool to check the global IP address of the domain `api.tmdb.org`.

● [DNS Checker](https://dnschecker.org/)

● [DNS Lookup Tool by Chinaz](https://tool.chinaz.com/dns/)

● [IPADDRESS.COM](https://ipaddress.com/)

2. Example using [IPADDRESS.COM](https://ipaddress.com/): In the search box, type api.tmdb.org and press Enter.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250729/f32352e2-3e27-49fb-a344-858626b2e7b8.png)

3. Scroll down the page to view the IP address resolved by the system. Copy and save it properly, as it will be used later during the configuration process.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250729/2a199b76-ffee-4848-915a-828569aad9e5.png)

### **Configure the HOST**

1. Open the [Theater] app and tap the [Settings] icon in the upper right corner to enter the Theater settings page.
2. Tap [Data Source], select [The Movie Database], and paste the previously obtained IP address into the HOST configuration input box. Make sure the format is correct. The required format is: IP address + space + domain name.
3. In the TMDB configuration, enter the IP address and domain name in the format “IP address + space + domain name” under HOST (you can add multiple entries as needed), for example:

```
52.85.151.18 api.themoviedb.org
```

4. After confirming that everything is correct, click "Import" to complete the setup.
5. Click "Apply" to save.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250729/beec5774-3d8c-4639-941a-c8c0c125012b.png)

## **Common Issues**

**1. Unable to Access the API**

Ensure that the IP address you obtained is up to date. If the API is still inaccessible, try re-querying the IP address or use other public DNS services for resolution.

**2. Why is there no change in the library after configuring TMDB?**

After configuring TMDB, the library won't update automatically. You need to do:

* **Adjust the video information source**: Set TMDB's priority to the highest.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250729/3ce8527f-9039-4c00-a8df-c4eb4ac7107e.png)

* **Rescan the library**: Choose [Scan and Replace All] to retrieve the latest metadata and posters from TMDB.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250729/e233cd4d-10f8-4b5e-b7f1-2cc87c96679f.png)

## **Related Links**

[[Tutorial] How to apply for TMDB (The Movie Database) API key?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjo0MTYsImFydGljbGVJbmZvSWQiOjE5OSwiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIifQ==)

[Why Is There No Change in Media Library Recognition After Configuring TMDB?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjoxOTE2LCJhcnRpY2xlSW5mb0lkIjo2MDIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIn0=)
