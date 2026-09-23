# Universal Search User Guide

> **Article ID**: `739`  
> **Category**: `Application Guide > UGOS Pro > Universal Search User Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/739  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client, Web Browser

**Applicable Version**: UGOS Pro Firmware 1.18.1.0098 or later

**Feature Availability**: Document content search, document semantic search (AI), and Uliya Q&A are supported only on iDX series devices.

The descriptions in this document are for reference only. The interface may vary depending on system or app updates, please refer to the actual interface.

## Introduction

**Universal Search** is the unified search portal in UGOS Pro. Instead of switching back and forth between apps such as Theater, Music, Photos, and Files, you can enter a keyword or a specific question in the Universal Search box to quickly find content across your device, including files, films, music, photos, apps, and system settings.

**Supported search methods**:

● **Keyword search**: Find content precisely by file name, category tag, app name, and more.

● **Document content search (iDX series only):** Search for text within documents using keywords or locate the corresponding files. For example, searching for "shutdown" can find documents containing that term.

● **Semantic search (iDX series only)**: Search using a general description. For example, searching for "work summary" can find relevant files even if their file names do not contain the word "summary".

During a search, results are ranked based on how closely their titles, content, tags, and semantics match your query, with the most relevant results displayed first.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/064c60e77d314115b719c5ea0f9a82e9.webp)

## Quick Actions

|  |  |  |
| --- | --- | --- |
| **Action** | **Method** | **Description** |
| Open the search box | Shortcut: Command + F (Mac)  or Ctrl + F (Windows) | Quickly opens the search box from anywhere in the system |
| Click the search icon in the upper-right corner of the UGOS Pro desktop | - |
| Close the search box | Press Esc | Quickly hides the search interface |
| Select a result | Press the ↑ and ↓ arrow keys | Move up or down through the search results |
| Open the selected item | Press Enter | Opens the currently selected file or app |

● Search box: Enter keywords to find content

● Search Settings: Configure the indexing scope and excluded paths

● Category tabs: Filter search results by type

## Search Settings

To make search results more accurate and better suited to your needs, it is recommended to configure the basic search settings before use. You can access the Search Settings page in the following ways:

**Method 1: Access during first use**

Click the "**Search**" icon in the upper-right corner of the desktop to open Universal Search, then click "**Search settings**" below the search box to open the settings page.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/02aba6cca48a423e966285df74cac13b.webp)

**Method 2: Access from the search results page**

After entering a keyword to open the search results page, click the "**Settings**" (gear) icon in the upper-right corner to open the settings page.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/17744fd8a20544e395332a62abf9dec0.webp)

**Method 3: Access from Control Panel**

Open the "**Control Panel**" app, click "**Indexing Service**", locate "**Universal Search**", and click the "**Settings**" button on the right.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/ba0cbbda843d457582a8c8b3de7b955e.webp)

### File Search Indexing Settings

On the Search Settings page, you can enable different levels of indexing services as needed:

● **File name search**: The basic indexing service. It is enabled by default and cannot be disabled separately.

● **Content search**: When enabled, the system reads and indexes text within documents (such as TXT, Word, and PDF files). Even if you do not remember the file name, you can still find the file by searching for a phrase it contains.

● **Document semantic search (AI)**: When enabled, the system can understand the core concepts of documents. For example, searching for "work summary" can find relevant documents even if they do not contain the word "summary".

![](https://file-us.ugreennas.com/admin/article/2026-08-27/1e4a81f620364f86b1140e8d1863a7fb.webp)

**Index maintenance**: If search results are incomplete or abnormal, try clicking "**Rebuild index**" to resolve the issue.

**Note**:

● **Document content search and Document semantic search (AI) rely on NPU computing power and are supported only on iDX series devices.** You must also authorize the required models in the "**Model Management**" app.

● When Document content search or Document semantic search (AI) is enabled for the first time, the system needs some time to build the index in the background. During this process, some newly added files may not be searchable temporarily. Please wait for indexing to complete.

### Excluded Path Settings

If you do not want certain private or system folders to appear in search results, you can add them to the "**Excluded path**" list.

**Steps**:

1. On the Search Settings page, locate "**Excluded path**".

2. Click "**Add**", then select the folders you want to exclude in the pop-up window (Personal Folders, Shared Folders, and User Folders are supported).

3. After confirmation, the selected folders and their subfolders will no longer appear in search results.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/961c5c6616664d468146e131e8aa9213.webp)

**Note**: The Recycle Bin and certain hidden system directories are excluded by default, so no manual configuration is required.

### App Search Scope Settings

On the "**Application**" settings page, you can control which apps' content appears in Universal Search results.

For example, if you do not want "**Music**" content to appear in search results, simply turn off the Music app on this page.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/5ea8284c335146db8cc1a13e8bb6554d.webp)

## Using Search

After completing the search settings, you can use Universal Search to find content across your device.

#### Find Content by Category

On the search results page, click a category tab below the search box (such as "All", "Files", "Photos", "Theater", or "Music") to filter the results and view only a specific type of content.

For example, to find photos only, click the "**Photos**" tab. To find files only, click the "**Files**" tab.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/6790c8bc822a4a70b5f2a98152b445c6.webp)

#### View and Manage Search Results

Search results are intelligently ranked based on title match, content relevance, tags, and semantic similarity. The most relevant result appears first under "**Best match**", and matched keywords are highlighted to help you quickly locate the content you need.

![](https://file-us.ugreennas.com/admin/article/2026-08-27/21f292d8f2ff4c4c9302b9487d4d3b68.webp)

On the search results page, you can perform the following actions:

● **Open an item**: Double-click a search result to open the corresponding file, app, folder, or Control Panel setting.

● **More actions**: Click the "**...**" button on the right side of an item to:

○ **Download**: Download a file or folder to your local device (folders are downloaded as compressed files).

○ **Open file location**: Quickly navigate to the file's location on the device.

● **Use Uliya** (iDX series only): Click a search result and select "**Ask Uliya**" to perform conversational searches, generate smart summaries, translate content, and more for an individual file.

###
