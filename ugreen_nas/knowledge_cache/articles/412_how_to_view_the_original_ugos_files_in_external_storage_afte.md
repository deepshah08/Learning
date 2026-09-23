# How to View the Original Ugos Files in External Storage After Switching to the UGOS Pro System?

> **Article ID**: `412`  
> **Category**: `Application Guide > Storage > FAQ > How to View the Original Ugos Files in External Storage After Switching to the UGOS Pro System?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/412  

---

**After switching from the UGOS system to the UGOS Pro system, the original storage space can only be used as external storage.**

**If you need to access, copy, move, or use files in the storage space, please follow the steps below to mount the hard drive used by the storage space as an external storage drive:**

The detailed operation guide is as follows:

1. **Access Storage**

● In the UGOS Pro system main interface, click the "My apps" icon in the top left corner.

● Go to [Storage] > [Hard Drive].

2. **Identify and Use the Hard Drive**

● In the [Hard Drive] interface, select the "HDD/SSD" option.

● Find the hard drive previously used in the UGOS system; these drives will be displayed as not used by default.

● Select the hard drive you want to use, click the "···" button on the right, and choose the "Use" option. In the pop-up window, select "External Storage" to use the hard drive as an external storage drive.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/3c6c7f18b1e549f3b457bc4700c920ba.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-16/da9a9fb558c749a5bd85cee1b794bffe.webp)

● If your storage space uses a RAID array, all hard drives associated with the RAID array must be inserted into the NAS device at the same time to ensure that RAID array information can be correctly read and used. For example, if you used three hard drives to form a RAID5 array in the UGOS system, after switching to UGOS Pro, all three hard drives must be inserted into the NAS device together.

3. **Mount the External Storage Drive**

● After a successful mount, you will be able to see the mounted external storage drive in the interface.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/6b002eb47e1c481d848084d69a5c12ce.webp)

4. **Configure Files**

● Open [Files] in the "My apps".

● Click the "Settings" button and find the "Hide specified files" option under "General Settings".

● Uncheck the "Start with ." option and click "Save" to apply the settings. (This is a necessary prerequisite because UGOS folders are hidden by default in external storage, and disabling the hide function will allow you to view the files.)

![](https://file-us.ugreennas.com/admin/article/2025-09-16/f63606bdf38d4453818a368c58784a71.webp)

5. **Access the External Storage Hard drive**

● Open Files and find the "External Devices" option in the left sidebar. Select the external storage hard drive you just mounted.

● After entering the hard drive directory, locate and open the folder named ".ugreen\_nas." This folder contains the user's files. If you cannot find the folder, make sure that Files is set to show hidden files.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/4cdf1f5ea84746909a5a23d8cd77188a.webp)

6. **Find the User Directory**

● In the “.ugreen\_nas” directory, you can find user folders consisting of 5-digit numbers. These folders correspond to the storage volumes you created in the UGOS system.

![](https://file-us.ugreennas.com/admin/article/2025-09-16/fd46079f51c74a0e8255e978a347b26f.webp)
