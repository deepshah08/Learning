# How to enable the video face recognition feature in the photos app?

> **Article ID**: `678`  
> **Category**: `Application Guide > Photos > FAQ > How to enable the video face recognition feature in the photos app?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/678  

---

This article will provide you with a detailed guide on how to enable and use the video face recognition feature in the "Photos" app of the UGOS Pro system.

### **Prerequisites**

Before enabling this feature, please update the NAS system firmware, the Photos app, and the people recognition model to the latest versions to ensure proper functionality.

### **Steps**

1. Open the “Photos” app, tap the “Settings” icon at the top right corner, then select [AI Settings] > [People Recognition].

If the model has not been downloaded yet or the version is outdated, please download or update it first to ensure you are using the latest version.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250605/70df0a2f-5ac8-4474-9302-97ea8c58fb4b.png)

2. After the update is complete, you can check one or both of the following options as needed:

* Apply the model to the personal library: recognize only photos or videos in the personal library.
* Apply the model to the shared library: recognize only photos or videos in the shared library.

Click [Advanced Settings] to continue to the next step.

3. On the [Advanced Settings] page, you can set the photo count threshold for automatically creating “People” clusters in both the personal and shared libraries. For example, when the number of photos containing people in a library reaches the set threshold, the system will automatically perform cluster recognition.
4. On the same page, check the “Recognize people in videos” option for both the personal and shared libraries. After completing the settings, click “Apply” to save and activate them.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250605/16560c79-25f7-4fb5-b10b-7a8d75fa88bb.png)

5. After the system completes video face recognition, you can return to the [People] album page to view the recognition results.

### **Notes**

* Performance impact reminder: Enabling the video recognition feature will increase the device’s performance load. It is recommended to avoid using it during peak business hours (such as during data synchronization or backup tasks).
* Recognition duration limit: Currently, only videos up to 30 minutes in length can be recognized. Longer videos will consume more resources, so please manage video length accordingly.
* Data retention notice: After disabling the video recognition feature, the system will retain previously recognized results, but newly uploaded videos will no longer be recognized.
