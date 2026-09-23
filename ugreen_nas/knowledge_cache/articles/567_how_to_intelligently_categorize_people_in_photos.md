# How to Intelligently Categorize People in Photos?

> **Article ID**: `567`  
> **Category**: `Application Guide > Photos > How to Intelligently Categorize People in Photos?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/567  

---

**Applicable models**: DH series, DX series, DXP series, and iDX series

**Applicable clients**: UGREEN NAS PC client and web browser

**Applicable version**: UGOS Pro firmware 1.15.12.0051 and later

The screenshots in this article are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## Scenario Description

In UGREEN NAS, the "**Photos**" app provides intelligent "**People recognition**". It can automatically group faces in photos and videos and generate separate albums by person. When you need to quickly find all photos of a family member, or organize a large number of photos from trips, parties, and other events by person, this feature can greatly reduce manual sorting and improve photo management efficiency.

![](https://file-us.ugreennas.com/admin/article/2026-05-25/a32e0c6a8c824004b79083de0a2fb1d7.webp)

## Prerequisites

Before you begin, make sure the following requirements are met:

● **The "Photos**" **app has been installed**: If it is not installed, open "**App Center**", find the "**Photos**" app, and complete the installation.

● **The firmware and app have been updated**: We recommend updating the UGOS Pro firmware and Photos app to the latest versions for the best performance.

● **The AI model is ready**: People recognition depends on an AI model. You need to download and enable the "**People recognition**" model in **Model Manager** in advance. If it has not been downloaded, the system will prompt you to download it when you enable the feature.

## Steps

### Download and Enable the People recognition Model

1. Open the "**Photos**" app, click the "**Settings**" icon at the bottom of the sidebar, and go to the "**Intelligent**" page.

2. Find "**People recognition**" in the intelligent model list. If the model has not been downloaded, follow the on-screen instructions to complete the download. After the download is complete, click the switch to enable it.

**Note:** To also recognize people in videos, enable "**Recognize people in videos**" separately under "**People recognition**".

![](https://file-us.ugreennas.com/admin/article/2026-05-25/b8eecca5ef0a4941b4d7f3a7087dfcc3.webp)

### Start People Recognition

1. After the model is enabled, the system will automatically start scanning photos and videos in Library and perform face recognition. The time required for the first recognition depends on the number of files in Library. Please wait patiently.

2. After recognition is complete, click "**Categorization**">"**People**" in the sidebar to view all recognized people's profile photos and the number of corresponding photos.

![](https://file-us.ugreennas.com/admin/article/2026-05-25/88d4232e8e7446cebb1ae21f65254ecf.webp)

### View and Manage People Categories

1. On the "**People**" page, click any person's profile photo to enter the dedicated album for that person and view all photos and videos containing that person.

2. You can also right-click a person's profile photo, or click the "**More**" button on the right side of the interface, to perform the following management actions:

![](https://file-us.ugreennas.com/admin/article/2026-05-25/9ce0fecf10bb4065938d1738306deb2a.webp)

● **Rename**: Enter the person's name, such as Zhang San, for easier searching later.

● **Add to navigation bar**: Pin frequently used people albums to the custom navigation bar on the sidebar for quick access.

● **Hide**: Hide people you do not want to display. After a person is hidden, the album will no longer appear in People categories. You can unhide it at any time.

● **Lock**: After locking is enabled, the system will no longer automatically add new photos to this person.

● **Merge**: If the same person is recognized as multiple groups due to different angles, ages, or other factors, select the profile photos you want to merge and click "**Merge**". The system will automatically combine the photos into one album.

![](https://file-us.ugreennas.com/admin/article/2026-05-25/0255357454c0497f8f99a01981f613cf.webp)

### Recognize Again

If you are not satisfied with the recognition results, such as missed recognition or incorrect grouping, you can trigger recognition again:

1. Go to "**Settings**">"**Intelligent**" again.

2. In the "**People recognition**" model options, click "**Recognize again**".

3. The system will scan Library again and update the People category results.

![](https://file-us.ugreennas.com/admin/article/2026-05-25/1a439c3d04124f9e94d69f24d19df4cd.webp)

## Notes

● People recognition uses some CPU and disk resources on the device. We recommend running it when the system is idle.

● People albums are virtual categories generated by the system based on recognition results. Deleting photos from a People album will not delete the original files. It will only remove the association between the photo and the current People category.
