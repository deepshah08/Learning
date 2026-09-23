# Poster Details Page

> **Article ID**: `212`  
> **Category**: `Application Guide > Theater > Poster Details Page`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/212  

---

> The content and image examples in this article are based on UGOS Pro firmware version 1.6.0.2890 and Media Center version 1.6.0.1078.Due to potential differences in the interface or functionality between firmware versions, please refer to the actual display on your device.

The **Theater's** poster detail page offers powerful features designed for easy browsing and management of movie content. Here is a brief introduction to its specific functionalities:

# Poster Details Display

The "Theater" provides **stunning poster backgrounds for display**. Movies scraped via the**TMDB** method, if available, will show the logo, with the title presented in the logo format, offering a richer visual experience.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/8429ca86d7e24bfa940d99e4fe0431c1.webp)

## Manually Upload a Logo

If you want to manually upload a logo, follow these steps:

1. In Media Center, locate the target video and enter its detail page.

2. On the video detail page, click the ···" (More) button to expand more options.

3. In the pop-up menu, select "Edit Info".

4. On the Edit Info page, click the **Logo** section to upload a custom logo file.  
After uploading, scroll to the bottom of the page and click "Save" to apply the changes.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/d9b394fbaed240ef9e25595947718a61.webp)

## Episode View Toggle

● The episodes support two modes: **List View and Card View**. Users can freely switch between these modes, and the system will apply the selected mode to all episodes, making it easier to browse and manage movie and TV resources quickly.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/4e2a10f0200143a3bd8f066346650fa5.webp)

● **Multi-episode TV Shows**: You can quickly locate the episode you want to watch using the List View based on **episode numbers**, improving search efficiency.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/2d0a376df89a461888b4dd63a1865a43.webp)

# Filter and Sorting

● **Filter Function**: Six main categories are available for filtering: Status, Progress, Genre, Region, Year, and Type. Users can quickly filter films based on their needs.

● **Sort Function**: Supports four sorting options: **Name, Add Time, Release Time, and Rating**, with the option to sort in **ascending or descending** order, enabling personalized management.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/c9a744e43f5844278fa6d7706b1529f8.webp)

# Movie Detail Page

● **Basic Information**: **Displays Title, Rating, Year, Genre, Region, Duration, Plot Summary, Cast Info, Resolution, Video Info, and Audio** Info.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/2dfadd05b9f24ddab6eda993df6375df.webp)

● **Detailed Specifications**: Provides detailed specs including **File Path, Size, Format, Audio/Video Encoding Info, Audio Tracks, and Subtitles**, making it easy for users to view movie data.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/de6a9ef9177a426c9659537fdb86f9a4.webp)

● **Cast and Crew Info**: Clicking on the names of Actors or Directors allows users to view detailed profiles and quickly browse other films they have starred in or directed.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/7a1accbba646429f90ffae0dc9d2571d.webp)

# TV Series / Anime Series Detail Page

● **Episode Information**: Displays **the title, description, and small cover for each episode**, allowing users to easily understand the content of each episode.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/d5754e2cc46043cda63c1cd58e579ae3.webp)

● **Series Collection**: Automatically groups **series films, multi-season TV shows, and anime series**, making it easier for users to organize and watch their content.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/5f72d63c3b354170b392e5279045609a.webp)

# Modify Poster Information

If the film's detailed information is incorrect, you can **rematch or manually identify it** on the poster detail page.

## Steps for Manual Identification

1. Click the "..." button and select "**Manual Identification**."

2. Enter the correct film title (e.g., *Civil War*) and click "**Search**" for smart identification.

3. Select the correct film from the search results, and the system will automatically update the full film information.

# Add and Manage Collections

The "**Theater**" supports automatic collection recognition, and you can also manually add collections to better organize movies of the same series or multi-season TV shows.

## Steps to Manually Add a Collection

1. Select the film you want to add to a collection, click the "..." button, and choose "Add to Collection."

![](https://file-us.ugreennas.com/admin/article/2025-07-03/5ea4afb9ea2547dab994e863ad4039cc.webp)

2. Choose the desired collection from the list and click "Confirm" to add the film to that collection. If the collection you want is not available, click "Create New Collection" to add the film to a newly created collection.

3. Films that have been categorized will display the Collection icon in the top right corner.

4. To dissolve a collection, hover over the film poster and click the "..." to perform the operation.

## Collection Removal and Cleanup Mechanism

To improve content management efficiency and enhance user experience, "**Theater**" provides both **automatic and manual mechanisms for cleaning up collections**. The following are relevant notes on collection removal, disbandment, and cleanup:

**1. Automatic Collection Disbandment Mechanism**

When a user manually removes the last movie or episode from a collection on its detail page, the system will automatically detect that the collection is empty and disband it accordingly. After the operation is completed, the system will automatically return to the previous page; the user does not need to manually go back or delete the collection.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/684b16d2ab524b70a015a8b228233403.webp)

**2. Automatic Cleanup of Empty Collections During Library Scan**

Each time the user performs any type of media library scan (including incremental scan, full scan, scheduled scan, etc.) in the library, the system will automatically detect the content status of all collections within the library.

If any collection is found to contain no valid content (i.e., the collection is empty), the system will automatically clean up the empty collection to keep the library organized. This operation requires no user intervention and is completed automatically in the background.

**3. Manual One-Click Cleanup of Empty Collections on PC/Web (Admins Only)**

Theater provides a [Remove All Empty Collections] function in the [Collections] section of the PC/Web interface. Once clicked, the system will immediately scan and remove all collections without content in the current library.

**Please Note:**

● The [Remove All Empty Collections] function is only visible to and operable by system administrator accounts.

● This function is suitable for use during large-scale content changes, library maintenance, or troubleshooting abnormal collection displays.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/3d3fb1d64ea64832912e7b31cc934c73.webp)

# Episode Management

In the "**Theater**", after scanning the media library, you may encounter issues such as:

● **Incorrect identification of episodes** (especially for variety shows);

● **Missing episodes or incorrect order**;

● **Extra content (e.g., behind-the-scenes footage) that needs to be merged.**

Users can manually correct episode information through **Episode Management**, such as:

● Correcting misidentified episodes or reordering them;

● Merging behind-the-scenes footage with the main episode, preferably setting it as the last episode.

If you want to know more, please check the guide: [How to use "Episode Management" to correct misidentified TV series or variety shows in the library?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTUwOSwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo1MTUsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

# Download/Delete Source Files

**Delete Source Files**

● Hover over a single poster card, click "..." > "Delete Source File." The deleted file can be recovered from the "Recycle Bin" in the "**Files**" application.

**Download Movies**

● **Movies:** Hover over a movie poster card, click the "..." button, and select "Download" from the pop-up options to download the video to your local device.

● **Episodes:** For episodic content, use the "**Files**" application to download the episodes to your local device.

# Edit Movie Metadata

If you're not satisfied with the scraped metadata (poster information) in the media library, you can manually edit it. Editable fields include: **cover image, background image, movie title, release date, country/region, genre, rating, cast and crew information, movie description**, and more.

![](https://file-us.ugreennas.com/admin/article/2025-07-03/9a2be099f78b4e6998c439bcccd80319.webp)

If you want to know more, please view the guide: [Theater Movie Naming Convention Guidelines](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjo3NTAsImFydGljbGVJbmZvSWQiOjI1NywiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIiLCJwYXRoQ29kZSI6IiJ9) [Theater Movie Naming Convention Guidelines](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjo3NTAsImFydGljbGVJbmZvSWQiOjI1NywiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIiLCJwYXRoQ29kZSI6IiJ9)

# Create a Custom Movie Poster Wall with Local Images

If a video or movie cannot obtain poster information from TMDB or the auto-recognition feature, you can use the local image management feature to set custom posters and background images for movies and episodes. This feature is ideal for short films, media resources without .nfo files, or if you want to create your own personalized poster wall for a unique viewing experience.

If you want to know more, please view the guide: [UGOS Pro Theater Local Image Recognition Rules](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTc0NCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiZW4tVVMiLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo1ODMsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)
