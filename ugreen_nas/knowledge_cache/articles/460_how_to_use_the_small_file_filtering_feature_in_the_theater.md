# How to Use the Small File Filtering Feature in the Theater

> **Article ID**: `460`  
> **Category**: `Application Guide > Theater > FAQ > How to Use the Small File Filtering Feature in the Theater`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/460  

---

To enhance your viewing experience and streamline library management, the UGOS Pro system of UGREEN NAS has introduced a new "Small File Filtering" feature in its [Theater]. This feature allows you to customize a file size threshold, ensuring that files smaller than the set value are not added to the library, thus preventing small files such as advertisement videos or clips from occupying the cover of the Theater.

## Advantages of Small File Filtering Feature

* **Improved Library Quality:** By filtering out small files such as advertisement clips and low-quality videos, the library becomes cleaner and more organized, enhancing the viewing experience.
* **Easy Operation:**There's no need for cumbersome manual deletion of small files; the system handles it automatically with simple settings.
* **Precise Filtering:**You can set a file size threshold (in MB) as needed, and any file smaller than this threshold will be automatically filtered out and not scraped into the library.
* **Flexible Control:**By default, the filtering function is off. You can enable it anytime and manually input the file size range (0-1000 MB) for filtering. When the value is 0, the system considers no filtering, and all files will be added to the library.

## How to Use the Small File Filtering Feature

**Entry 1: Modify an Existing Library**

* Open the "Theater" app and click the "Avatar" in the top right corner.
* Select the library you want to modify, click "···" > "Edit" to enter the editing interface.
* Find the [Filter Files Smaller Than] option under the [Additional Settings] section of "Video Information," check the box, and enter the desired file size threshold.

![](https://file-us.ugreennas.com/admin/article/2025-08-08/7edfb5ceafb24ff397b3e4c9de9c30eb.webp)

* After setting, click "Apply" to save the configuration.
* After modifying the filtering rules for an existing library, previously added small files will not be automatically removed. The new rules will only take effect after performing the [Scan and replace all] operation.
* After this operation, all files that meet the new file size threshold will be filtered, ensuring that the content in the library complies with the new filtering rules.

**Entry 2: Add a New Library**

* In the "Settings", select [Library] > [Add] to create a new library.
* During the creation process, in the [Additional Settings] section of "Video Information," find the [Filter Files Smaller Than] option and set the file size threshold.
* After applying the setting, the system will automatically filter out unqualified small files during the import process based on the set value.

### How to Make the Small File Filtering Rules Effective After Editing the Library

When editing an existing library, although small file filtering rules are added, they will not take effect immediately. To make the newly set filtering rules effective, you need to follow these steps:

1. **Enter the Console:**

* Open the "Theater", click the user avatar in the top right corner, and select [Settings] to enter the library management interface.

2. **Select the library and start scanning:**

* In the[Settings] , select the library where you want to apply the filtering rules.
* Click the "···" icon next to the library and select [Scan] > [Scan and replace all].

3. **Perform the filtering operation:**

* The scanning operation will trigger the system to recheck all imported files and remove small files that do not comply with the latest filtering rules.

## Notes

* The default threshold for the filtering function is 20 MB, which you can modify according to actual needs within the input range of 0 to 1000 MB.
* If you enter illegal characters or exceed the set range, the system will prompt you with an input error to ensure smooth operation.
