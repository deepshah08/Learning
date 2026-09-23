# How to Create a Custom Category with Model Training?

> **Article ID**: `874`  
> **Category**: `Application Guide > Photos > How to Create a Custom Category with Model Training?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/874  

---

**Applicable models**:DH Series, DX Series, DXP Series, and iDX Series

**Applicable clients**: UGREEN NAS PC client and web browser

**Applicable version**: UGOS Pro firmware 1.15.12.0051 and later

The screenshots in this article are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## Scenario Description

When organizing photos, it is common to sort them by specific objects or themes, such as "Jack-o-Lanterns", "Birthday Cakes", or "Graduation Photos". The album app provides a **custom category** feature that supports two methods:

● Enter a category name directly, and the system will automatically search for and group related photos.

● Upload sample images for model training, so the system can identify and categorize specific objects more accurately.

This feature is suitable for organizing large numbers of photos around specific themes, making them easier to find and manage.

![](https://file-us.ugreennas.com/admin/article/2026-06-10/fb4aefeaf8d1468db0120c4a2938c0f5.webp)

**Note:** Custom categories are supported only on some devices, including the iDX Series. Please refer to the actual interface for availability.

## Prerequisites

Before getting started, make sure the following requirements are met:

● **Photos is installed**: If it is not installed yet, open **"App Center"**, find **"Photos"**, and complete the installation.

● **Training photos are ready**: If using the **"Train model"** method, prepare 1–10 clear photos of the target object from different angles, and save them to the local computer or NAS in advance.

● **Sufficient system resources are available**: Model training and photo recognition may use a significant amount of system resources. It is recommended to perform these tasks during off-peak hours.

## Steps

### Method 1: Automatically Group Photos by Entering a Category Name

This method does not require model training. The system automatically searches for and groups related photos based on the meaning of the category name.

1. Open **"Photos"**, then click **"Categorization">"Custom"** in the sidebar.

2. Click **"Create categories by name"** and enter a category name, such as "Birthday cake".

![](https://file-us.ugreennas.com/admin/article/2026-06-10/ca15a9589f274c00bfe359b4c30dc0a9.webp)

3. The system will search the photo library based on the category name and automatically group matching photos into that custom category album.

### Method 2: Create a Custom Category with Model Training

Use this method when the automatic grouping results are not accurate enough, or when a specific object needs to be recognized. By training a dedicated model, the system can classify photos more precisely.

1. Go to **"Categorization">"Custom"**, then click **"Train model"**.

![](https://file-us.ugreennas.com/admin/article/2026-06-10/729849fa812b472689b96b44c3cb1ac3.webp)

2. Import training images. The following three options are supported:

● **From NAS library**: Select photos from the existing photo library.

● **From NAS**: Import photos from other folders on the NAS.

● **From computer**: Upload photos from the local computer.

![](https://file-us.ugreennas.com/admin/article/2026-06-10/dccf700463ff49efa412e21e0e73a3a6.webp)

3. In the selection window, choose 1–10 photos of the same object. It is recommended to select 10 photos covering different angles and scenarios. **Note:** A maximum of 10 photos can be selected. If more than 10 photos are selected, the system will use the first 10 by default.

4. After importing the images, enter a custom category name, such as "Jack-o-Lantern".

5. On the annotation page, annotate each image one by one. Use the mouse to draw a box around the target object in each image, that is, the object to be recognized by the model.

![](https://file-us.ugreennas.com/admin/article/2026-06-10/04d8885ffd224cc794ef3bdf2ea5f7a6.webp)

6. After all images are annotated, click **"Create"**.

7. The system will start training the model. The training time depends on the image size and device performance.

![](https://file-us.ugreennas.com/admin/article/2026-06-10/706ed94e12434899b077df1720ff2bdf.webp)

8. After training is complete, the generated category album can be viewed on the **"Custom"** page.

![](https://file-us.ugreennas.com/admin/article/2026-06-10/299ed9b87ca8455b824c8e10f4f53b7c.webp)

### Import a Trained Model

If a trained model package is already available, it can be imported directly for use.

1. Go to **"Categorization" > "Custom"**, click the **"+"** button, and select **"Import model"**.

![](https://file-us.ugreennas.com/admin/article/2026-06-10/5a491c7303c24ad594dd90630b5d8754.webp)

2. Select an upload method

● **From NAS**: Select a saved model package from the NAS.

● **From computer**: Upload a model package from the local computer.

![](https://file-us.ugreennas.com/admin/article/2026-06-10/d26014d1ce924009bba2693b32329c5e.webp)

3. After the import is complete, the system will automatically use the model to recognize photos in the library and generate the corresponding custom category album.

### Manage Custom Categories

On the **"Custom"** page, right-click a category album or click the **"More"** button on the right to perform the following actions:

![](https://file-us.ugreennas.com/admin/article/2026-06-10/b87d89677c9148259123e6ef13f4ef23.webp)

● **Add to navigation bar**: Pin the category to the custom navigation bar in the sidebar for quick access.

● **Rename**: Change the name of the custom category.

● **Export model**: Export the trained model package to the NAS or a local device.

● **Delete**: Delete the category.

**Note:** After deletion, the training data will be lost. Any object recognition albums and conditional albums generated from this category will also be deleted.

## Additional Notes

● Model training and photo recognition can use a large amount of system resources. It is recommended to perform these tasks when the system is idle, and avoid running other high-load tasks at the same time, such as data synchronization or video transcoding.

● High-quality and diverse training data can improve model accuracy. It is recommended to use 10 clear photos taken from different angles and under different lighting conditions, and accurately annotate the target object in each image.

● If the personal photo library contains a large number of photos, the recognition process may take a long time. If the wait time is unusually long, contact official technical support.

● Custom categories and model training are supported only on iDX Series devices. Please refer to the actual interface for availability.

● The AI custom category model runs and processes data locally, without requiring a network connection. This helps protect data security and privacy.
