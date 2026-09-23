# Enable Movie Data Protection

> **Article ID**: `881`  
> **Category**: `Application Guide > Theater > Enable Movie Data Protection`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/881  

---

## Applicability

**Applicable client:** UGREEN NAS PC client (Windows/macOS).

**Applicable version:** NAS firmware 1.17.0.0034 or later.

This document is for reference only. The actual interface and operation paths may vary slightly depending on system or app version updates. Please refer to the actual interface.

## Overview

To prevent manually edited movie information, such as posters and descriptions, from being overwritten during media library scans, "**Theater**" provides a "**Data Protection**" mechanism. After it is enabled, the system will prioritize manually edited information and save the customized data locally on the device. When the media library runs a scan, this local data will be used first.

## How to Enable

1. Go to the details page of the target movie, then click "**…**">"**Edit information**".

![](https://file-us.ugreennas.com/admin/article/2026-06-29/367130e5e6f04b0aab225cc20c39374c.webp)

2. Turn on "**Data protection**" on the page, then click "**Save**".

![](https://file-us.ugreennas.com/admin/article/2026-06-29/2166dc811e624280ab1daaf1fbbeb99b.webp)

## Data Protection Mechanism

To ensure that customized data is not changed, the system defines when "**Data protection**" takes effect and when it becomes invalid.

### When It Takes Effect

Data protection is activated only when the system runs a "**Scan media library**" task. In this state, whether the scan is triggered in the background or manually, the system will read the locally locked protected data first. This applies to the following scan scenarios:

**Automatically triggered:** The scheduled "**Scan media library**" task enabled in "**Theater**" settings.

**Manually triggered for a media library:**

● **"Scan newly added and modified content"**

● **"Scan all missing content"**

● **"Scan and replace all"**

![](https://file-us.ugreennas.com/admin/article/2026-06-29/e677f1bc14db49928a5f940c6f93a2b7.webp)

### When It Becomes Invalid

Data protection does not block user-initiated changes. If "**Rescan**" or "**Scan manually**" is performed on a movie with data protection enabled, the system treats the operation as a forced reset command.

After either operation is triggered, data protection for the current movie becomes invalid, and the original locally protected data will be overwritten by the newly scraped online data.

![](https://file-us.ugreennas.com/admin/article/2026-06-29/d76c6e020d764394a5483c58568c9809.webp)

## FAQs

### What manually edited information can be protected from being overwritten?

Data protection locks 10 data fields: cover, background, logo, title or collection name, release date, country/region, genre, rating, description, and cast & crew.

**Note:** For "**Cast & Crew**", only changes to actor order and additions or edits to character roles are protected.

### If I have multiple versions of the same movie, such as 4K and 1080P, do I need to edit them separately?

No. The system uses a global linkage mechanism. After information is edited and protected for any version, all resolution versions associated with the same movie will be treated as "**locked**".

### Will my playback progress and favorite records be lost after editing movie information?

No. The system uses the absolute file path as the index key. As long as the physical file is not moved, changes to the displayed metadata will not affect the associated playback progress, watched status, last access time, or favorite records. These records will be retained and automatically linked to the updated metadata.

### Why can't I edit movie information or find the related button?

The current account does not have sufficient permissions. For media library management and system security reasons, modification features such as "**Edit information**" are available only to users with administrator permissions. Standard users can only view and play content, and cannot edit information or configure data protection.

### If I delete a media folder and add it again, will the previously edited and protected information still be retained?

No. The locked status of a movie is strongly tied to the current media library path. If a folder is removed from the media library and then imported again, the system treats it as a new path. The previous protection status will be cleared, and the system will run the standard scraping process for that directory again.
