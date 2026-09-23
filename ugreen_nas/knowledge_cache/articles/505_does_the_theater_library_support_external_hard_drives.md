# Does the Theater Library Support External Hard Drives?

> **Article ID**: `505`  
> **Category**: `Application Guide > Theater > FAQ > Does the Theater Library Support External Hard Drives?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/505  

---

In the Theater app of the UGREEN UGOS Pro system, you can select folders on an external hard drive as the media source when creating a library.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250619/77fa795b-86cb-419b-b169-19f125ff83ba.png)

## **Supported Media Folder Types**

The Theater Library currently supports the following types of media folders:

* **Personal Folder**

* **Shared Folder**
* **User Folder**
* **Peripheral：**Hard drives connected to the NAS via USB can be used directly as media sources by selecting folders from the drive.
* **Network Folder：**Folders from other network storage devices mounted to the NAS system (via protocols such as SMB or NFS), allowing flexible expansion of the library’s storage scope.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250619/9bd40992-422e-4add-837b-21acd29b78ec.png)

## **How to Add an External Hard Drive as a Library Source?**

1. **Ensure the External Hard Drive Is Properly Connected**

   * Connect the hard drive to the UGREEN NAS via the USB port.
   * Go to [Storage] > [External Storage] to check if the drive has been recognized and mounted.
2. **Create or Edit a Library**

   * Open the Theater app, click the user avatar in the top right corner, and go to [Console] > [Library].
   * Click "+ New library" or edit an existing one.
3. **Select a Folder on the External Hard Drive**

   * In the [Folder ] selection screen, navigate to the path of the external hard drive.
   * Select the desired folder on the drive to use as the media source.
4. **Save the Settings**

   * Click “OK” to complete the creation or update of the library. The Theater app will automatically scan the files on the external hard drive and generate media entries.

## **Notes**

* If folders on the external hard drive have access restrictions, please ensure that the currently logged-in UGREEN NAS system account has read permissions. If you are unable to access files on the external hard drive, please check whether you are using a general user account, and go to [Storage]> [External Storage] > [Advanced Settings] to ensure that “Use allowed” is enabled.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250619/198c4895-9d35-468b-9212-b56760c04cae.png)

* Make sure the file system format used by the external hard drive is compatible with the UGOS Pro system. Please refer to [Supported Peripheral Storage Formats](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjo4MzIsImFydGljbGVJbmZvSWQiOjI1NCwiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIxLjAiLCJwYXRoQ29kZSI6InBybzAwMSxqb3pyY2ksejd0eHQ2In0%3D).
* If the external hard drive is removed or disconnected, the Theater app will no longer be able to access the corresponding media content. It is recommended to keep the drive connected after setup.
* Once a media folder from the external hard drive is added, the system will automatically scan and index its contents. For large-capacity drives, the scanning process may take longer—please be patient.

**Related Reading**

* [Learn How to Quickly Set Up Your Personal Media Library in 3 Steps](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTI5OSwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo0MzIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)
