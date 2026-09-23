# Theater Settings

> **Article ID**: `208`  
> **Category**: `Application Guide > Theater > Theater Settings`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/208  

---

"**Theater Settings**" provides a variety of personal settings and service management features, allowing users to customize the interface and functions according to their preferences, creating a playback experience that fits their habits.

**To enter the settings page:** open the "**Theater"** app, then click the "**Settings"** button at the top.

**Function Overview:**

In Theater settings, you can manage the following features:

● **Navigation Menu**: Configure the display and order of modules in the left navigation bar.

● **Homepage**: Customize the homepage Carousel and module layout.

● **Content Cards**: Control what information is displayed on movie cards (such as ratings, resolution).

● **Library**: Manage categories of video content, display language, folder paths, and metadata acquisition methods.

● **Data Source**: Configure sources of movie information (such as TMDB).

● **User Management**: Set Theater access permissions for different users.

● **Background Management**: Monitor and manage background tasks (such as scheduled library scans, identifying intros & outros).

## Navigation Menu

Users can customize the modules displayed in the homepage left navigation bar and their order:

● **Supported modules**: Recently Played, My Favorites, Folder, Collection, Library.

● **Sorting method**: Hold the left mouse button on a module to drag and reorder.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/8c00401171664567adb0e8a66a02a9f0.webp)

## Homepage

In Homepage, you can configure the following:

● **Carousel**: Choose whether to display a large-screen carousel on the homepage, and select its content source.

● **Homepage modules**: Customize which modules appear on the homepage, and drag to adjust their order.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/f14be64079cb42b0afc54339e89c045b.webp)

## Content Cards

You can configure the display information on video Content Cards:

● Whether to Show ratings.

● Whether to Show resolution.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/af853c392bba47e1803cabe5b4c7ce6c.webp)

## Library

The Library is the core module of Theater, used to manage and recognize stored video resources. With the Library, you can:

● Systematically categorize movies and TV Series.

● Configure data source for video information.

● Set display language.

● Set permission to control access for different users.

### Basic Functions

● Create multiple media libraries to organize content by category or purpose.

● Configure media library settings such as name, language, linked folders, metadata sources, and filtering rules.

● Edit, scan, or remove media libraries as needed.

● Configure access permissions for each media library to control content availability for different users.

### Create New Library

**Steps:**

1. In the Theater settings page, click "**Library**"＞"**New library**" to open the configuration window.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/fc36a0d995f8413381ac62edba3ef85c.webp)

2. Set the following information:

● **Name**: customizable name (up to 20 characters, avoid special symbols such as #, $, %).

● **Language**: interface display language (affects titles, descriptions, etc., but not video audio tracks).

● **Folder**: select one or more NAS folders storing videos.

● **Metadata Scraping**: choose sources for video information (supports TMDB, Intelligent recognition, etc.), priority can be configured.

● **Set permission**: assign access permissions for different users.

3. Click "**Apply"** to save and create.

**Library configuration notes:**

● **Prioritize same-name NFO metadata**: NFO files are plain text or XML files containing metadata of movies or TV Series (such as synopsis, cast, director, etc.), used to enrich and customize the Library's display information. If a same-name `.nfo` file exists in the video directory, the system will prioritize its data.

● **Automatically identify video series and add to Collection**: automatically group related videos (e.g., TV Series, director's works).

● **Filter files smaller than specified size**: set a threshold (e.g., 100 MB) to exclude invalid files.

### Manage Library

After creating a Library, you can perform the following:

● **Edit**: right-click the Library, or click the "**···**"＞"**Edit"**.

● **Rename**: right-click the Library, or click the "**···**"＞"**Rename**".

● **Scan**: Right-click the media library, or click "**···**"＞"**Scan**" in the upper-right corner. This allows you to re-identify or manually match metadata. Three scan modes are supported: "**Scan newly added and modified content**", "**Scan all missing content**", "**Scan and repalce all**".

● **Remove**: removes the configuration only (does not delete actual files).

**Note:**

● Under normal circumstances, Theater automatically monitors changes in folders linked to a media library and initiates indexing accordingly. If you want to speed up recognition or force a content refresh, you can manually scan the media library using the options above.

● The scanning process consumes system resources. The larger the number of files, the longer the scan will take.

● If metadata scraping fails after a full overwrite scan, the system will display a screenshot as a temporary poster, or show a blank cover image.

● Description of the three media library scan modes:

**Scan newly added and modified content**: Processes only newly added or modified files. This mode is more efficient.

**Scan all missing content**: Traverses all content and fills in missing metadata fields only.

**Scan and repalce all**: Re-identifies all files from scratch, and existing metadata will be overwritten. This mode is recommended only for initial library creation or after major changes, to avoid overwriting accurate existing information.

## Data Source

● Theater comes with **TMDB** as a default data source, which can be used directly. You may also configure your own TMDB API key to improve recognition speed and stability.

● **Intellient Recognition**: The intelligent metadata scraper provided by UGREEN NAS is enabled by default. If you do not need this intelligent recognition data source, you can disable this option. Once disabled, the intelligent recognition data source will no longer appear in the media library settings.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/ae51637f0ff5425c92e329479c0943bc.webp)

**Note**: For more information about TMDB, please refer to [How to apply for TMDB (The Movie Database) API key](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmMjAwIn0=) .

## User Management

In user management, the administrator can configure Theater access permissions for different users.

**Steps:**

1. In Theater settings, click "**User Management**", select the target user, and click "**Set permission**". In the pop-up permission configuration window, select the accessible Libraries for that user and assign permissions.

2. Click "**Apply"** to save.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/bef37feed8284215ba6bc8470007e77a.webp)

## Background Management

### Scheduled Library Scan

The system supports scheduled scans to automatically update new content in the Library.

**Steps:**

1. In Theater settings, click "**Background Management**", and enable "**Scheduled library scan**".

2. Select the target Library and set scan time. The system will automatically run the scan task at the specified time.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/d6f2c4f763334949a284a873bced347d.webp)

### Identify Intros & Outros

The system can intelligently detect repetitive intro and outro segments in TV Series, and automatically skip them during playback.

**Steps:**

1. In Theater settings, click "**Background Management**", and enable "**Identify intros & outros**".

2. Select the Library to process, and the system will perform automatic recognition.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/6b9c2684f65c497dbb57a9269814f5f2.webp)

**Notes:**

● Priority is given to recently played TV Series, followed by entry order.

● Recognition may take longer if there are many episodes (uses local computing).

● After recognition, white markers will appear on the progress bar during playback.

● While playing, you can view the time range in "**Player settings**"＞"**Skip intros & outros**".

![](https://file-us.ugreennas.com/admin/article/2026-01-04/639ba0b22c1b42ebb6116db609f70581.webp)

● At the intro time point, playback will automatically skip the intro.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/dbcaa4a1b5404f3dab9571de6183c36b.webp)

● At the outro time point, a prompt will appear before skipping the outro.

![](https://file-us.ugreennas.com/admin/article/2026-01-04/f1fa65a05dd64be5969603b77d15e735.webp)
