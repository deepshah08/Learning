# Why Some Images Cannot Be Found with Keywords

> **Article ID**: `848`  
> **Category**: `Application Guide > Photos > FAQ > Why Some Images Cannot Be Found with Keywords`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/848  

---

## Applicability

**Supported Platforms**: UGREEN NAS PC Client, Web Browser, and UGREEN NAS mobile app.

**Supported Versions**: UGOS Pro firmware version 1.15.0.0114 and later.

The descriptions in this document are for reference only. Actual interfaces and operation paths may vary slightly depending on system or application version updates. Please refer to the actual interface on your device.

## Issue Description

When using the search feature in Photos, you may notice that some photos can be accurately found through keyword searches (intelligent search), while others cannot be searched at all.

## Cause Analysis

The effectiveness of intelligent search in Photos depends heavily on the type of folder where the photos are stored (shared or personal) as well as the current user's AI model activation status and folder permissions. The system operates according to the following logic:

**Shared Folders (Global Sharing)**

● **How it works**: If an administrator uploads photos to a "**Shared Folder**" added under "**Folder scope**" in Photos and enables AI recognition, the generated AI indexing data becomes available to all users who have access to that shared folder.

![](https://file-us.ugreennas.com/admin/article/2026-05-08/38a6101abf9e4870bc1339e4a079a426.webp)

● **Permission requirements**: Whether other users can find these photos through search depends on whether they have read permission for the shared folder. Shared folder permissions can be configured through the user permission management section in "**Folder scope**" settings.

**Personal Folders (Independent Recognition)**

● **How it works**: When a standard user uploads photos to their own **personal folder**, the AI recognition data for that directory is generated independently and remains isolated from other users.

● Standard users must manually enable the AI recognition models in the Photos app "**Settings**" and wait for the system to complete a full background scan of their personal folders before intelligent search can properly identify and locate their photos. Photos stored in personal folders will not appear in search results if the scan has not finished or the feature has not been enabled.
