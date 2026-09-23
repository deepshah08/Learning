# Understand the Data Source of the Theater: The Movie Database (TMDB)

> **Article ID**: `556`  
> **Category**: `Application Guide > Theater > FAQ > Understand the Data Source of the Theater: The Movie Database (TMDB)`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/556  

---

In the UGOS Pro system, the theater supports the configuration of The Movie Database (TMDB) as a data source. This feature is designed to enhance the automatic retrieval of media information. The following is a detailed introduction to TMDB.

## **What is The Movie Database (TMDB)?**

The Movie Database (TMDB) is a global database created and maintained by movie and television enthusiasts, offering a massive collection of media metadata. Its main features include:

* **Extensive Media Information:** Provides detailed information about movies and TV shows, such as plot summaries, cast lists, directors, and release dates.
* **Community Driven:** User-contributed content with real-time updates and multilingual support.
* **High-Quality Resources:** Provides high-resolution posters, stills, and cover images.
* **Robust API Support:** Developers can access TMDB’s complete dataset via its API, supporting seamless integration with various media management tools.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250623/4bd6404b-6709-4b99-8dca-3050040d53a8.png)

## **Why Configure The Movie Database (TMDB) as a Data Source?**

Once the TMDB data source is configured, the theater can provide the following benefits:

* **Accurate Matching of Local Files:** Automatically identifies movies and TV shows and retrieves their detailed information.
* **Automated Metadata Retrieval:** Obtains information such as summaries, cast details, poster images, and multilingual titles.
* **Multilingual Support:** Enables access to media metadata in Chinese, English, or other languages.
* **High-Quality Posters and Cover Images:** Provides high-resolution artwork and stills, enhancing the visual experience.

## **How to Configure the TMDB Data Source**

1. Open the console of the theater app and click on the Data Sources option.
2. In the The Movie Database settings page, enter the following information:

* **API Key:** Obtain this by registering a TMDB account. You can refer to [How to apply for TMDB (The Movie Database) API key?](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6NDIzLCJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVJbmZvSWQiOjIwMCwiYXJ0aWNsZVZlcnNpb24iOiIxLjAuMC4wMzM0IiwicGF0aENvZGUiOiJwcm8wMDIsc2ozNWJnLHAzbDAzdCJ9)
* **HOST Configuration:** Set the correct IP address for TMDB to bypass DNS pollution and ensure the data source can be accessed normally.

3. Open the Data Sources section in the console, and in the The Movie Database settings, fill in the IP address for the host, followed by a space and the domain name. For example: `13.224.161.90 api.themoviedb.org`.
4. Click "Apply" to complete the setup.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250623/8340e82f-9688-4f01-85d6-391be426276a.png)

## **Custom API Key**

By default, the UGOS Pro system uses a built-in TMDB API key shared by all users. However, this shared key may be subject to usage limits (such as API call rate limits). Configuring your own TMDB API key allows you to:

* Avoid service interruptions caused by API overload.
* Ensure stable metadata fetching, especially when scraping a large number of files.
