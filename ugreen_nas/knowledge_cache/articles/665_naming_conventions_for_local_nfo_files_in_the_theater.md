# Naming Conventions for Local NFO Files in the Theater

> **Article ID**: `665`  
> **Category**: `Application Guide > Theater > FAQ > Naming Conventions for Local NFO Files in the Theater`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/665  

---

UGREEN NAS's UGOS Pro Theater currently supports three scraping methods:

1、TMDB: Retrieves metadata from The Movie Database (TMDB), including movie titles, cast, synopsis, posters, and more.

2、Intelligent Recognition: The system automatically analyzes filenames and file attributes using algorithms to select the best-matched information from the database.

3、Read local information first: By configuring the resource NFO file locally for scraping, once this option is selected, the system will retrieve basic information, cover images, posters, and other data from the configuration file.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/f4bdd1d0-4aff-4892-b23d-4a37f919ee86.png)

**[Scraping Priority Logic Reference]**

[What is the priority order of NFO scraping, TMDB scraping, and Intelligent Scraping in the Theater?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTM4NCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0NjIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

This document introduces the use of NFO files. For video files that cannot be identified via TMDB or intelligent recognition (such as courses, variety shows, etc.), you can refer to the following information to manually create and edit basic NFO file data.

### **Creating a Movie NFO File**

1、Name the movie NFO file according to the following format:

```
<movie>
The middle part contains the basic information of the movie
</movie>
```

The section containing the basic movie information includes:

|  |  |
| --- | --- |
| Required Content | Editing Example |
| Specify movie title | <title>Movie Title</title> |
| Specify year | <year>2002</year> |
| Specify plot | <plot>Plot summary</plot> |
| Specify TMDB ID | <tmdbid>79</tmdbid> |
| Specify Douban ID | <doubanid>79</doubanid> |
| Specify release date | <releasedate>2006-01-02</releasedate> |
| Specify rating | <rating>7.2</rating> |
| Specify actor | <actor>  <name>Actor Name</name>  < role>Role Name</ role>  <tmdbid>Actor's TMDB ID</tmdbid>  </actor> |
| Country/Region (To be launched in January) | <country>Use the three-digit ISO 3166-1 numeric country code</country>  Example <country>156</country> China |
| Genre (To be launched in January) | Genres must use standard names or IDs. Using IDs is recommended.  Example<genre>War</genre> or  <genre>10752</genre>  See detailed genre ID list below. |
| MPAA Rating (To be launched in January) | <mpaa>PG-13</mpaa> |

Genre ID Information

|  |  |
| --- | --- |
| Genre ID | Genre Name |
| 18 | Drama |
| 35 | Comedy |
| 28 | Action |
| 10749 | Romance |
| 53 | Thriller |
| 80 | Crime |
| 9648 | Mystery |
| 10752 | War |
| 878 | Science Fiction |
| 16 | Animation |
| 27 | Horror |
| 10751 | Family |
| 12 | Adventure |
| 14 | Fantasy |
| 36 | History |
| 99 | Documentary |
| 10402 | Music |
| 37 | Western |

As an example: "Stranger Things"

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/cd9be277-fc54-43d9-95b4-9416b50f374d.png)

2、You can specify the desired poster image by placing the image file in the same directory as the video file.

Recommended poster cover size: 1080x1920

Recommended poster stills size: 1920x1080

Recommended poster logo size: 800x310

|  |  |
| --- | --- |
| Type | Naming Rules & Format |
| Portrait Poster | Video File Name-poster.jpg |
| Landscape Poster | Video File Name-background.jpg  Video File Name-backdrop.jpg  Video File Name-fanart.jpg |

As an example: "A Record of a Mortal's Journey to Immortality"

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/692af012-f86a-4b81-bdf1-2c426926b9e3.png)

### **Creating a TV Series NFO File**

1、The naming format for TV series NFO files is as follows:

There are three types of TV series NFO files: Same name as the video file with nfo、season.nfo、tvshow.nfo

(1)The NFO file with the same name as the video file is placed in the same folder as the video and contains information about that single episode.

The file must be named according to the following format:

```
<episodedetails>
the follow-up content
</episodedetails>
```

The basic information content part of the video same-named file includes:

|  |  |
| --- | --- |
| Required Content | Editing Example |
| Specify Episode Title | <title>Episode 1</title> |
| Specify Episode Plot | <plot>Plot</plot> |
| Specify Season | <season>1</season> |
| Specify Episode Number | <episode>1</episode> |

For example: TV Series *Stranger Things* - Episode 1

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/3f79939d-c77a-4df3-b4fc-95a14b694562.png)

The file storage path is the same as the video:

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/037f5fe2-ff50-409b-9769-187510262b70.png)

(2) season.nfo and tvshow.nfo files are placed in the corresponding season folder or the entire series folder, serving as the information source for that season and for automatic multi-season collection of the series.

The season.nfo file must be named according to the following format:

```
<season>
the follow-up content
</season>
```

The tvshow.nfo file must be named according to the following format:

```
<tvshow> 
the follow-up content 
</tvshow>
```

The basic information content part of the season and tvshow files includes:

|  |  |
| --- | --- |
| Required Content | Editing Example |
| Season Title | <title>Season 1</title> |
| Specify Season Number | <seasonnumber>1</seasonnumber> |
| Specify Episode Title | <title>Episode Title</title> |
| Specify Year | <year>2002</year> |
| Specify Plot | <plot>Plot</plot> |
| Specify TMDB ID | <tmdbid>79</tmdbid> |
| Specify Douban ID | <doubanid>79</doubanid> |
| Specify Release Date | <releasedate>2006-01-02</releasedate> |
| Specify Rating | <rating>7.2</rating> |
| Specify Actor | <actor>  <name>Actor Name</name>  < role>Role Played</ role>  <tmdbid>Actor’s TMDB ID</tmdbid>  </actor> |

Note: If both tvshow and season files have a , they will be concatenated as "Show Title Season Title."</p>

For example: TV Series Stranger Things - S02

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/153e95cf-535a-4793-9ef2-7c65c5c63c28.png)

File storage path example:

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/4d33da66-1867-43fb-b9d6-f276d5df7c26.png)

2、You can specify the desired poster image by placing the image files in the same directory as the video file or in the episode folder within the season folder.

Recommended poster cover size: 1080x1920

Recommended poster stills size: 1920x1080

Recommended series cover size: 1920x1080

|  |  |
| --- | --- |
| Type | Naming Rules & Format |
| Portrait Posters | Series poster: poster.jpg  Season poster: season01-poster.jpg |
| Landscape Posters | Video File Name-background.jpg  Video File Name-backdrop.jpg  Video File Name-fanart.jpg |
| Episode Cover Poster | Video File Name.jpg |
