# What is the Purpose of Configuring The Movie Database (TMDB) as a Data Source in the Theater?

> **Article ID**: `557`  
> **Category**: `Application Guide > Theater > FAQ > What is the Purpose of Configuring The Movie Database (TMDB) as a Data Source in the Theater?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/557  

---

The UGOS Pro theater app comes with TMDB data source pre-configured by default, so there's no need to manually enter an API key. However, it also offers the option to customize your own TMDB API key. The TMDB data source provides the following advantages:

**Note:**   
If you are unfamiliar with configuring TMDB API keys or customizing the HOST, it is recommended to keep the default settings. Users with special requirements can configure the TMDB data source in the console according to their needs.

## Benefits of Configuring a Custom API Key

The built-in TMDB data source key is shared among all users and may be subject to usage limits (e.g., API call rate limits). By configuring your own TMDB API key, you can avoid service interruptions caused by API overload and ensure stable metadata retrieval, especially when scraping a large number of movies and TV shows.

● **Ensure Access Permissions:** Using a personal API key helps prevent data retrieval failures caused by restrictions on public services.

● **Improve Service Quality:** A personal API key allows customization of preferences such as language and content rating, enabling you to get more accurate information.

## How to Configure the TMDB Data Source

1. Open the console of the theater app, and in the Data Sources section, click to open The Movie Database.

2. In the The Movie Database settings page, enter the following information:

● **API Key:** Obtain this by registering a TMDB account. You can refer to [How to apply for TMDB (The Movie Database) API key?](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmNTU3In0=)

● **HOST Configuration:** Set the correct IP address for TMDB to bypass DNS pollution issues and ensure normal access to the data source.

3. Click "Apply" to complete the setup.

## Configuring a Custom HOST to Resolve Network Issues

In some regions, TMDB's API may be inaccessible due to network restrictions. The theater app provides a HOST configuration option that allows users to specify the correct IP address for TMDB, bypassing DNS pollution issues and ensuring normal access to the data source. For example:

1. Specify the TMDB resolution address to fix DNS pollution problems.

2. Use proxy servers or specific network nodes to accelerate TMDB access and improve metadata fetching efficiency.

## How to Configure the HOST

1. Open the console's "Data Sources" section, and in "The Movie Database" settings, enter the IP address corresponding to the HOST followed by a space and the domain name, for example: 13.224.161.90 api.themoviedb.org.

2. Click "Apply"to save the settings.

![](https://file-us.ugreennas.com/admin/article/2025-08-26/39db6adb86784de69ac1aad76bd7ed3a.webp)

## Other Data Sources for the Theater

TMDB is one optional data source for the theater; you can also use other data sources such as intelligent recognition.

## If Metadata Does Not Display Correctly After Configuration

Please try the following troubleshooting steps:

1. Make sure the TMDB API key is correctly entered and the settings are saved.

2. Check if the TMDB API connection test indicates success.

3. Verify that the IP address entered in the HOST configuration is correctly resolved.

4. If the problem persists, try manually refreshing the library using "Scan All and Overwrite."

## Are There Additional Costs After Configuring the TMDB Data Source?

TMDB offers free basic services, but for advanced features or large-scale usage (such as frequent metadata updates), you need to register a TMDB account to obtain an API key and consult TMDB's official usage policies.

## Term Explanation

DNS pollution refers to the practice of forging or tampering with DNS responses, preventing users from accessing the genuine websites.
