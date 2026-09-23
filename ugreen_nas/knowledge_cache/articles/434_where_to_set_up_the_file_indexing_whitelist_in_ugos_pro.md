# Where to set up the file indexing whitelist in UGOS Pro?

> **Article ID**: `434`  
> **Category**: `Application Guide > Control Panel > FAQ > Where to set up the file indexing whitelist in UGOS Pro?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/434  

---

## Why Set Up File Indexing?

Imagine UGREEN NAS as a library of personal data, where each file is like a book, neatly arranged on "shelves" according to the folder structure you set. If you want to find a specific file ("book"), you can enter a keyword in the "Universal Search", and the UGOS Pro system starts scanning the entire file library to find files that meet the criteria. However, as the number of files increases, this search process can become very time-consuming. Therefore, to quickly and accurately find a file, it is necessary for the system to generate an "index" similar to a library catalog.

In the UGOS Pro system, file indexing is enabled by default. When you upload a large amount of data to the NAS, the system will automatically start indexing tasks. The role of indexing is to generate an index table by mapping the key information of files (such as file name, format, creation time, etc.) to their folder locations. This process involves scanning and calculating all files, which may occupy a lot of CPU resources and may temporarily reduce system performance. To optimize the experience, it is recommended to reasonably set the indexing range when using UGREEN NAS to avoid affecting system performance during peak times.

## Where to Set the File Indexing Range (Whitelist)?

To customize the range of file indexing, follow these steps:

1. Go to [Universal Search]> [Settings] to enter the "Search Configuration" page.

![](https://file-us.ugreennas.com/admin/article/2025-08-08/c9acfbd01eb548098ee2e3f661656714.webp)

Or in the [Control Panel] > [Indexing Service] interface, click on "Search Range" to enter the search configuration page.

![](https://file-us.ugreennas.com/admin/article/2025-08-08/06c860da9c084ee9ad8d41313d38e0e9.webp)

2. Select the folders that need to be included in the search range. Folders that are not checked and the files they contain will not be indexed or searched.

3. Click "Apply" to save the settings.

**Tips:**Only folders included in the search range will be searched. If there are new or deleted files, the system will index these changes again, which may temporarily affect the performance of the NAS. Therefore, it is recommended to reasonably select the search range according to actual needs. For example, if the search range is not checked at all or only a few folders are checked, the system will only index the folders you have checked. This also includes directories of whitelisted applications, such as those used by Thunder.

![](https://file-us.ugreennas.com/admin/article/2025-08-08/99945c4e0ea44d33b19f9065e208dc96.webp)

## Notes

Although file indexing can improve search efficiency, invalid or excessive indexing can affect system performance. Here are some suggestions for reasonably setting up file indexing:

1. **Set up indexing based on file types:**

● Some file types (such as documents, pictures) are suitable for indexing because these types of files usually need to be searched frequently.

● For video and music files, indexing is not recommended unless particularly needed. Since these files are often larger and are not usually searched precisely by file name, indexing these files will consume system resources.

2. **Regularly maintain and optimize indexing settings:**

● As the number of files increases, regularly optimizing or rebuilding indexing settings helps maintain the system's efficient operation. By reasonably setting the search range and indexing rules, you can reduce the system burden and improve the user experience.
