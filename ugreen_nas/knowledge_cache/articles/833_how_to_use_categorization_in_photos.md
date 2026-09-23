# How to Use Categorization in Photos?

> **Article ID**: `833`  
> **Category**: `Application Guide > Photos > How to Use Categorization in Photos?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/833  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: UGOS Pro Firmware 1.18.0.0060 or later

**Feature availability**: The features available under "Categorization" vary by device model. For details, see "Differences in AI Recognition Model Support" in this document.

The descriptions in this document are for reference only. The actual interface may vary depending on system or app updates, please refer to the actual interface.

## Introduction

The "**Categorization**" feature in Photos uses local AI models to analyze photos and videos in the background. Once enabled, it can identify faces, locations, scenes and objects, and text in your media, then automatically organize them into categories such as **People, Locations, and Scenes & Objects**, helping keep your photo library organized.

It also supports **Custom Categories**, allowing you to train the model to recognize specific objects and organize photos based on your personal needs.

## Prerequisites

Before using Categorization, download and authorize the required AI recognition models in the "**Model Management**" app and make sure the required models are enabled. For details on downloading and authorizing models, see the "[Model Management (DXP Series)](https://support.ugnas.com/knowledgecenter/detail/article/en-US/831)".

![](https://file-us.ugreennas.com/admin/article/2026-08-21/ab616ce679e04cf3b8d61a571f423f16.webp)

## Enable Intelligent Models

When using "**Categorization**" for the first time, you need to manually enable the intelligent recognition models.

1. Open the Photos app and click "**Settings**" > "**AI settings**".

2. On the "**AI settings**" page, enable the following options as needed:

![](https://file-us.ugreennas.com/admin/article/2026-08-21/8b1c2f5367f843c389761c3aca163e3a.webp)

● **People recognition**: Automatically recognizes facial features in photos and videos and groups the same people together. It also provides more granular controls for people recognition.

● **Text recognition**: Automatically extracts text from photos using OCR. Once enabled, you can quickly find photos by searching for keywords contained in them, such as ID numbers or invoice details.

● **Similar/Duplicate photo recognition**: Automatically scans for and identifies similar or duplicate photos in the background, providing data for the "**Similar & Duplicate**" cleanup feature.

● **Pet recognition**: Recognizes 39 common cat and dog breeds, such as Bulldogs, Shiba Inus, and British Shorthairs, and automatically organizes them into separate albums.

● **Sensitive content recognition**: Automatically identifies sensitive content, such as sexually explicit images, and blurs it by default when browsing photos to help protect privacy and improve the viewing experience.

● **Image recognition**: Analyzes image content and scene elements to support "**text-based image search**" and automatic categorization by scenes and objects in Photos.

● **Model training package**: Supports offline training of custom models to recognize specific objects. Once training is complete, the model can automatically categorize matching photos in the library for personalized organization.

**Note**:

● "**Categorization**" for the first time, you can also click "**Enable Now**" on the page. The system will automatically enable the models that have already been downloaded (If a required model has not been downloaded, follow the on-screen instructions to download it).

● After the relevant models are enabled, the system uses local computing resources to scan your media in the background. If you have a large photo library, the initial recognition and categorization process may take some time.

● If some photos are missed or recognized incorrectly, or if you recently migrated a large number of photos, click the more options menu next to the corresponding feature and select "**Recognize again**". The system will rescan the entire photo library and extract features again.

## People Categorization

After People recognition is enabled, the system automatically groups photos and videos of the same person into the corresponding album.

### View People Albums

Click "**Categorization**" > "**People**". The page displays all recognized people and their photos, where you can quickly search for or name a person.

![](https://file-us.ugreennas.com/admin/article/2026-08-21/bc6204069785454489a5f99cec26f964.webp)

### Manage People Albums

On the "**People**" page, right-click a person album or click "**More**" to access the available management options:

![](https://file-us.ugreennas.com/admin/article/2026-08-21/8ae64056e4444e31938d54606ce533ca.webp)

#### Set Up Quick Access

Right-click the profile image of a person album and select "**Add to navigation bar**". The person will then be pinned to the left sidebar for quick access.

![](https://file-us.ugreennas.com/admin/article/2026-08-21/9261960960104cf988a5eaf4c27ec4cb.webp)

#### Name a Person

On the "**People**" page under "**Categorization**", right-click a person's profile image and select "**Rename**". Change the default "Unnamed" to the person's actual name to make them easier to find later.

#### Hide a Person

The person will no longer appear in the category. To restore them, click "**Filter & Sort by**" > "**Show hidden people**".

![](https://file-us.ugreennas.com/admin/article/2026-08-21/254cd91e5d2242e781c13550a27e7d7d.webp)

#### Lock a Person

The system will no longer automatically add new photos to this person.

#### Merge People

Merge multiple groups of the same person into a single album.

![](https://file-us.ugreennas.com/admin/article/2026-08-21/f3c0738f5ae74b7a8e2ea0ec9ed20839.webp)

### Set a Person Album Cover

You can select your favorite or most representative photo from a person album and set it as the album cover.

1. Open the person album and find the photo you want to use as the cover.

2. Right-click the photo.

3. From the pop-up menu, select "**Set as cover**".

The system will automatically extract the recognized face of the target person from the selected photo and use it as the cover of the current person album.

![](https://file-us.ugreennas.com/admin/article/2026-08-21/eb95276c78654440b286d9c54a069b18.webp)

### Correct Recognition Errors

If some photos are categorized incorrectly due to lighting, angle, or other factors, you can correct them manually using either of the following methods:

**Method 1: Correct a Single Photo**

1. In the person album, find the incorrectly categorized photo and right-click it.

2. From the pop-up menu, select "**Move to another person**" and move it to the correct person group.

**Method 2: Correct Multiple Photos**

1. Hover over the photos you want to correct and click the checkboxes that appear to select multiple photos.

2. A floating action bar will appear at the bottom of the page. Click the "**...**" button on the right.

3. From the pop-up menu, select "**Move to another person**" to correct the selected photos in bulk.

![](https://file-us.ugreennas.com/admin/article/2026-08-21/f911785441f54cae85d8a2f09907f84e.webp)

## Location Footprints

Photos are automatically categorized by where they were taken based on their GPS information.

Click "**Categorization**" > "**Locations**". The system displays all recognized locations by city.

![](https://file-us.ugreennas.com/admin/article/2026-08-21/59291c5bb737498ba338adefbaf2e2d5.webp)

● **Map mode**: Click the "**Map**" tab to zoom in and out on the map and view your footprints across different cities.

● **City grouping**: The system automatically creates city cards based on GPS information (such as "Shenzhen" and "Huizhou"). Click a card to view all photos and videos taken in that location.

**Note**: Location recognition relies on GPS metadata in photos. If location services were disabled when the photo was taken or the metadata has been removed, recognition may be inaccurate.

## Screenshots and Selfies

After Image recognition is enabled, the system automatically creates the "**Screenshots**" and "**Selfies**" categories.

● **Screenshots**: Automatically identifies screenshots (such as chat records and QR code screenshots), making it easier to keep screenshots separate from the rest of your library.

● **Selfies**: Automatically groups selfie photos together for easier browsing and review.

![](https://file-us.ugreennas.com/admin/article/2026-08-21/d26defd4b8b0416abf3a927bbcde7595.webp)

## Object Recognition

The "**Object recognition**" feature uses AI to analyze image content and scene elements, automatically categorizing photos by scenes and objects to help you quickly find specific types of photos in a large library.

1. Go to the "**Categorization**" page and tap "**Object recognition**". You'll see a preview of some automatically generated category cards such as "**Weddings**", "**Dogs**", "**Mountains**", etc.

2. Tap the expand button on the right to view all category cards, which mainly include:

![](https://file-us.ugreennas.com/admin/article/2026-08-21/89c9196038504c7286c5e64f5fa41289.webp)

● **Pets & Animals**: Accurately recognizes common cat and dog breeds and creates dedicated albums for your pets.

● **Daily & Natural Scenes**: Automatically identifies moments like gatherings, beaches, waterfalls, snow scenes, sunrises, sunsets, forests, and more.

● **Documents & Receipts**: Automatically filters and groups screenshots, IDs, product codes, text, invoices/receipts, and other useful information for quick access.

● **Other Categories**: Includes common elements such as food, selfies, and more.

3. Tap any category card, and you can view all photos within it.

## Custom Categorization

If the system's automatic categorization does not meet your needs, or if you need to recognize specific objects, you can train a custom model for more accurate categorization.

**Method 1: Create Categories by Name** (supported on iDX series only)

1. Go to "**Categorization**" > "**Custom**".

2. Click "**Create categories by name**" and enter a category name (such as "Birthday Cake").

3. AI will automatically search your library and group matching photos.

![](https://file-us.ugreennas.com/admin/article/2026-08-21/2d34aa44786645a8829d4ac8aab8f2df.webp)

**Method 2: Create by Training a Model**

If creating a category by name does not meet your needs, you can upload sample images to train a custom model for more accurate categorization. You can also directly import a previously trained model package.

For details, see "[How to Create a Custom Category with Model Training?](https://support.ugnas.com/knowledgecenter/detail/article/en-US/874?clientType=PC) ".

![](https://file-us.ugreennas.com/admin/article/2026-08-21/3b9ddb5590dc42a996cd54aaed412331.webp)

Right-click a category or click the "**More**" button to access the following options:

![](https://file-us.ugreennas.com/admin/article/2026-08-21/44e2cc7ad3294d058e17df57eb908fbb.webp)

● **Add to navigation bar**: Pin the category to the custom navigation area in the sidebar for quick access.

● **Rename**: Change the name of the custom category.

● **Export model**: Export the trained model package to the NAS or your local device.

● **Delete**: Delete the category.

**Note**: After a category is deleted, its training data will be lost, and any object recognition albums and conditional albums generated from it will also be deleted.

## Differences in AI Recognition Model Support

AI categorization capabilities and the range of object recognition categories vary by device model. iDX series devices can recognize a wider range of scenes and objects. See the table below for details:

|  |  |  |
| --- | --- | --- |
| **Model Series** | **AI Categorization Capabilities** | **Description** |
| iDX series | Full support | Supports all features, including custom categorization, model training, object recognition (including video recognition), people recognition (including video recognition), and text recognition |
| DXP / GT / DX series | Basic support | Supports object recognition and people recognition (including video recognition), but does not support custom categorization or model training. |
| DH2600 | Basic support (limited) | Supports object recognition and people recognition (including video recognition), but does not support pet recognition, sensitive content recognition, and other features. |
| DH2300 Plus / DH4300 Plus | Partial support | Supports object recognition, people recognition (including video recognition), and some other recognition features, but does not support pet recognition, sensitive content recognition, and other features. |
| DH2300 | Limited support | Supports only basic object recognition (3 categories only: product codes, animals, and vehicles) and people recognition. All other features are not supported. |

**Note**：

● The number of category albums available under "Object recognition" also varies by device model. iDX series devices can recognize a wider range of scenes and objects.

● "Video recognition" refers to the ability to intelligently analyze people and visual content in video files. This feature is not supported on all device models.

## Image Formats Supported for AI Recognition

UGREEN NAS Photos currently supports AI recognition for the following image formats:

● **Common formats**: JPG, JPEG, PNG, GIF, BMP, WEBP, HEIC, HEIF

● **RAW formats**: 3FR, ARW, CR2, CR3, DNG, NEF, ORF, PEF, RAF, RW2
