# How to Mount Cloud Drives to Theater and Generate a Poster Wall

> **Article ID**: `815`  
> **Category**: `Application Guide > Theater > How to Mount Cloud Drives to Theater and Generate a Poster Wall`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/815  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS).

**Applicable Version**: NAS Firmware 1.18.0.0034 or later.

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Feature Overview

After mounting a cloud drive through the Network folder feature in the Files app, you can add its directory to "**Theater**". The system will automatically scan and scrape cloud video resources, generate a visually appealing poster wall, and enhance your viewing experience.

Currently supported cloud drives:

● 115 Cloud Drive

● Quark Drive

● Alibaba Cloud Drive

● OneDrive

## Requirements

Before proceeding, mount the target cloud drive through the "**Network folder**" feature in the Files app. After mounting, make sure that the files in the cloud drive directory can be viewed properly in Files.

## Steps

1. Open "**Theater**", click the "**Settings**" button in the top navigation bar, and enter the Theater settings page.

2. Click "**Library**" in the left navigation pane, then click "**New library**" on the right.

3. In the pop-up configuration window, enter a custom name for the library. Then, under "**Folder**", select the mounted Network folder.

![](https://file-us.ugreennas.com/admin/article/2026-07-28/b0e93068624e48329aebedcc2c5a6626.webp)

4. After selecting the folder, click "**Apply**" to complete the creation.

After the library is created, Theater will scan the video files in the Network folder and match the corresponding video metadata.

After the scan is complete, return to the Theater homepage to view the generated movie poster wall. Click a movie poster to play videos stored on the cloud drive online.

## Update Newly Added Media Resources from Cloud Drives

When you add new video files to a mounted cloud drive directory, the Library in Theater does not automatically sync these updates in real time. You can update library resources through "**Manual scanning**" or "**Scheduled scanning**".

### Method 1: Manually Scan the Library

If you want to retrieve newly added videos immediately, use the manual scan feature.

1. Open the "**Settings**" page in Theater, then click "**Library**" in the left navigation pane.

2. Find the library you want to update in the list on the right, click the "**···**" icon, and select "**Scan**".

3. In the pop-up menu, select "**Scan newly added and modified content**". The system will start retrieving newly added files.

To rescan the entire directory, select "**Scan and replace all**".

![](https://file-us.ugreennas.com/admin/article/2026-07-28/0987efdb430b42de84db3ebbfe262c7a.webp)

### Method 2: Schedule Library Scanning

If you want the system to automatically sync cloud drive content in the background, you can configure a scheduled scan task.

1. Open the "**Settings**" page in Theater, then click "**Background tasks**" in the left navigation pane.

2. Enable "**Scheduled library scan**".

3. Select the libraries to which the task applies and set the scan time. The system will automatically scan according to the configured schedule.

![](https://file-us.ugreennas.com/admin/article/2026-07-28/da97dfb9e57f447b86b3df317a973214.webp)

## Notes

Please note the requirements for retrieving movie posters. The system relies on an external database to match video information.

● **Matching requirements**: The video file name must be searchable and matchable on the TMDB website. Only when this requirement is met can the system successfully retrieve and display movie posters.

● **Cases where posters cannot be retrieved**: If you upload personal videos recorded by yourself, or if the video is relatively uncommon and cannot be found on the TMDB website, the system will not be able to retrieve poster information. Such videos will only display the default video icon.

## Related Articles

### FAQs for Cloud Drive Direct Playback

<https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmODExIiwiY2xpZW50VHlwZSI6IiJ9>

### How to Connect to Quark Drive via a Network Folder

<https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmODAxIiwiY2xpZW50VHlwZSI6IiJ9>

### Mount OneDrive Using the Network folder Feature

<https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmOTA2IiwiY2xpZW50VHlwZSI6IlBDIn0=>
