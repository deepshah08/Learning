# Why does the system resource usage of UGREEN NAS (DH4300 Plus) remain high after video playback ends?

> **Article ID**: `686`  
> **Category**: `Troubleshooting > Hardware Failure > Why does the system resource usage of UGREEN NAS (DH4300 Plus) remain high after video playback ends?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/686  

---

On DH Plus series NAS devices, users may notice that system resources (such as CPU usage) remain high for a short period after video playback ends. This is likely due to the “Theater” app performing library processing tasks in the background, rather than the video player failing to release resources.

## **Resource Release Mechanism**

After the player is closed, system resources related to video playback (such as decoding threads, cache, and video streams) are automatically released. This ensures there is no continued resource usage, and no manual intervention is required from the user.

## **Common Causes of High Resource Usage**

If the system is importing media into the library while playing videos, a temporary spike in NAS resource usage may occur. This is normal behavior. To reduce system load, it is recommended to avoid importing large amounts of media while watching videos. Try to stagger media organizing and video playback tasks.

Theater’s media import process includes the following background tasks:

**1. Asynchronous Image Processing Mechanism**

The system downloads and resizes image assets (such as covers, poster stills, logos, actor portraits, etc.) for newly added media to enhance visual presentation and improve interface loading performance.

**2. Multithreaded Downloading and Image Reconstruction**

The "Theater" app uses asynchronous multithreaded processing for metadata images. During periods of high concurrency or when importing a large number of media files, this may lead to noticeable CPU usage.

**3. Processing Time Depends on Content Scale**

The duration of image processing tasks is closely tied to factors such as the number of media files being imported, the number of images that need to be downloaded and generated per item, current network bandwidth, and system I/O load.
