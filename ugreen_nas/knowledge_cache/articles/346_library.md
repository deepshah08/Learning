# Library

> **Article ID**: `346`  
> **Category**: `Application Guide > Theater > Library`  
> **Client Compatibility**: `MOBILE`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/346  

---

## Media Library Overview

Within the Media Library, users can browse all videos stored in the library. Clicking "Media Library" in the menu bar allows you to switch to viewing the media library's video collection.

1. When there are a large number of films, you can click **the** " **Filter" button** to set different filter criteria and view films that meet those criteria.

2. To search for a specific film, click **the "Search" button** and enter keywords in the search bar for quick results. Search results can be categorized by three types: (All, Movies, TV Series). Search **"History" is saved** on the search page. Long-press an individual search history to click " **X"** and delete it. Click the **"Delete"** button to clear all history.

3. To switch views or sorting options, tap the " **Toolbar" button**. View styles include Image & Text and Standard Cards. Sorting options include Name, Year, Update Time, and Rating.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251218/07b3d76f-1bf9-468c-a7b2-a320a37dfbbf.png)

To view a movie's details, tap the movie to enter its details page. Follow these steps:

1. Tap the " **Play** " button to start the video.

2. Click the **"Favorite** " button to add the video to " **My Favorites"**.

3. Click the "..." button **to open** the action menu.

4. When a movie has multiple video file versions (e.g., Dolby Vision, HDR, Director's Cut), click **the "..." button** for that video file to switch versions. Then click " **Play"** to start the video.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20251218/52971cee-891b-4604-b709-a2932e328078.png)

## Media Center Settings

**Within the** "Settings" section of the Media Center, you can perform the following actions:

● **Personalization**: Customize the interface and features through navigation menus, home page modules, content cards, and more to create a personalized experience.

● **Manage Media Library**: Create, edit, and delete media libraries.

● **Configure Data Sources**: Specify storage paths for media files.

● **User Permissions Management**: Control access rights to the media library for different users.

● **Scheduled Tasks:** Enable automated scanning and updating of the media library.

### Personalized Settings

The Media Center offers extensive customization options to tailor the interface and features to your personal preferences and needs. Below are detailed instructions for personalized settings:

**Note:** These settings apply only to the current user's mobile device.

**Navigation Menu Management**

You can adjust the display and order of the bottom navigation bar menus in the Media Center, as well as the content shown within each menu, to better align the interface with your usage habits.

Adjustable elements include:

● **Media Library Display**: Whether to show media library categories in the bottom navigation bar, which media libraries to display within the library, and their sorting order.

● **Category Management**: The Media Center automatically identifies media files and categorizes them as **Movies, TV Shows, and Other** (files not successfully identified are placed in "Other"). You can configure whether to display categories in the bottom navigation bar and which content appears within each category.

**Homepage Management**

1. **Slideshow Settings**

You can configure whether to display a poster carousel on the homepage. The carousel enhances page personalization and user experience.

Supports configuring carousel image sources. Examples include recently added movies, favorite movies, or movies from a specified media library.

2. **Home Page Module Settings**

Customize the modules displayed on your homepage. Enable/disable module visibility and reorder modules to streamline or enrich your homepage based on personal preferences.

**Content Card Management**

1. **Rating Display**

You can choose whether to display ratings on movie content cards, making it easy to quickly gauge a film's popularity.

2. **Resolution Display**

You can choose whether to display resolution on video content cards, allowing you to quickly assess video quality.

## Media Library Management

Within Media Library Management, you can quickly see which media libraries are currently created in the Media Center and the number of videos under each library. You can also edit media library settings and create new media libraries.

**Note**: This feature is available only to administrator users.

### Create Media Library

By adding folders **from File Management** as media libraries, the system automatically scans video files within them and fetches metadata such as movie information, posters, and cast lists from data sources. This creates a clearly categorized, visually appealing media center for your collection.

**Steps:**

1. Go to **the Media Center**, click " **Settings** " > " **Media Library Management"** to access the management page.

2. Click " **Create** " on the page to launch the creation wizard.

3. Configure media library parameters and rules. After confirming all settings are correct, click " **Save** " to create the media library.

The system will begin scanning your specified folder and scraping movie information. This process may take some time; please wait patiently.

**Parameter Configuration Guide**

In the pop-up creation wizard, fill in the following parameters according to your needs

**Media Library Name**

● **Function Description**: Set an easily recognizable name for this media library, such as "European and American Films" or "Children's Animations."

● **Notes**: The name is limited to a maximum of 20 characters. Avoid using special symbols (such as #, $, %, etc.).

**Media Library Language**

● **Function Description**: Select the default display language for movie information (e.g., title, synopsis). For example, choosing "Simplified Chinese" will cause the scraper to prioritize finding synopses and posters in Simplified Chinese.

● **Notes**: This setting only affects the interface display language and does not alter the audio or subtitle languages within the video files themselves.

**Media Folders**

● **Function Description**: Add folders containing video files. The Media Center will scan these folders and supports mainstream video formats like MKV and MP4.

● **Notes**: Only supports adding folder paths; individual video files cannot be added directly.

**Information Sources (Data Sources)**

● **Function Description**: Set the sources and priority for retrieving movie information. Sources listed higher in the list will be used first. Long-press and drag a data source to adjust its order.

**Auto-Add to Collection**

● When enabled, the system automatically categorizes films from the same series (e.g., "Iron Man") into the same collection for easier management.

**Prioritize Local Information**

● When enabled, the system prioritizes .nfo files and local images in the same directory as the video file as metadata sources.

**Filter File Size**

● You can set a file size threshold to exclude invalid files that are too small.

### Modify Media Library Settings

After creating a media library, you may need to adjust its settings based on your actual needs, such as changing the library language, adding new media folders, or modifying metadata sources. These modifications can be easily accomplished.

**Steps:**

1. In Media Library Management, locate and click the target media library you wish to modify.

2. On the Media Library Edit page, you can modify all parameters configurable during creation.

3. After making changes, click " **Save** " to return to the " **Media Library Management"** page.

4. Select the target media library, **then click "···" > "Scan All and Overwrite"**.

**Note:** After modifying media library settings, you must rescan the media library for the new configuration to take effect.

### Scanning the Media Library

When new videos are added to the media library folder or media library settings are modified, you can rescan the media library to retrieve updated video information.

1. In Media Library Management, select the target media library to scan.

2. **Click "···" > "Scan All and Overwrite"**.

### Differences in Scan Methods

● For quick updates, select " **Scan Newly Added and Modified."**

● To ensure completeness, select " **Scan All and Supplement Missing**."

● To perform a comprehensive scan and reacquire movie information, select " **Scan All and Overwrite** ".

● When changing the data source acquisition method, select " **Scan All and Overwrite** ".

### Deleting Media Libraries

1. In Media Library Management, select the target media library to delete.

2. Click the media library's **"..." > "Delete".**

3. A confirmation prompt will appear; click **"Confirm"** to delete.

## Data Source Management

The Media Center defaults to using the built-in TMDB data source to retrieve movie metadata (such as posters, synopses, and cast information). If you need to use your personal TMDB API interface, you can configure it here.

**Steps:**

1. [Follow the guide on How to Apply for a TMDB (The Movie Database) API Key](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmMjAwIn0=) . Visit The Movie Database (TMDB) official website [in](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjo0MTYsImFydGljbGVJbmZvSWQiOjE5OSwiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIifQ==) your browser, register and log in to your account, apply for an API Key, and copy it for safekeeping.

2. Open the U-Cloud App, navigate **to "Media Center,"** then tap **"Settings" > "Data Sources."**

3. Paste the copied personal key into the **TMDB API Key** field.

4. Click " **Test** " in the " **Connectivity Test"** field to ensure the connection succeeds.

5. After successful verification, tap **"Save"**.

Typically, the HOST setting requires no configuration and can remain at its default value. Modify it only if you know you need to set a specific proxy or custom address.

## User Management

The Media Center supports granular permission management. As an administrator, you can control which media libraries each user on the device can access.

**Steps:**

1. Enter " **Media Center**, **"** click **"Settings" > "User Management"** to **access** the user management page.

2. On the page, locate and click the target username for which you wish to set or modify permissions.

3. The system will navigate to the user's media library permissions page, where you can set **"Allow Access" or "Block Access"** for each media library.

4. After completing permission settings, click **"Save."**

New permissions take effect immediately. Upon the user's next visit to the Media Center, the media library content displayed will be filtered according to the new permissions.

## Scheduled Tasks

The Media Center provides the ability **to schedule scans to update media libraries**. You can configure the " **Start Time"** and " **Media Library Scan Scope"** for scheduled scan tasks.

**Steps:**

1. Open " **Media Center**, **"** click **"Settings" > "Scheduled Tasks"** to **enter** the task management page.

2. Enable **the "Schedule Media Library Scan"** toggle, then configure the target media library andscheduled scan time.

3. After configuration, the system will **automatically run the media library scan task** at the specified time.
