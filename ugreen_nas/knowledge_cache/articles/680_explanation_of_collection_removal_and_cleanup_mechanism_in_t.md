# Explanation of Collection Removal and Cleanup Mechanism in the Theater

> **Article ID**: `680`  
> **Category**: `Application Guide > Theater > FAQ > Explanation of Collection Removal and Cleanup Mechanism in the Theater`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/680  

---

To improve content management efficiency and enhance user experience, "Theater" provides both automatic and manual mechanisms for cleaning up collections. The following are relevant notes on collection removal, disbandment, and cleanup:

**1. Automatic Collection Disbandment Mechanism**

When a user manually removes the last movie or episode from a collection on its detail page, the system will automatically detect that the collection is empty and disband it accordingly. After the operation is completed, the system will automatically return to the previous page; the user does not need to manually go back or delete the collection.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250530/93fc39a5-acbd-4ebd-9717-f6b877cf274a.png)

**2. Automatic Cleanup of Empty Collections During Library Scan**

Each time the user performs any type of media library scan (including incremental scan, full scan, scheduled scan, etc.) in the library, the system will automatically detect the content status of all collections within the library.

If any collection is found to contain no valid content (i.e., the collection is empty), the system will automatically clean up the empty collection to keep the library organized. This operation requires no user intervention and is completed automatically in the background.

**3. Manual One-Click Cleanup of Empty Collections on PC/Web (Admins Only)**

Theater provides a [Remove All Empty Collections] function in the [Collections] section of the PC/Web interface. Once clicked, the system will immediately scan and remove all collections without content in the current library.

**Please Note:**

* The [Remove All Empty Collections] function is only visible to and operable by system administrator accounts.
* This function is suitable for use during large-scale content changes, library maintenance, or troubleshooting abnormal collection displays.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250530/e9b97a63-73eb-4b8b-87f2-089ad291924f.png)
