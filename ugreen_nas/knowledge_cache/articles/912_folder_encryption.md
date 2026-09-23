# Folder Encryption

> **Article ID**: `912`  
> **Category**: `Application Guide > Files > Folder Encryption`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/912  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS).

**Applicable Version**: NAS Firmware 1.18.0.0032 or later.

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

Administrator users can enable encryption for **Shared Folder** and the **Top-level Directories of User Folder**. After a folder is encrypted, the system generates a key file and automatically downloads it to the local device. The key is required when mounting or decrypting the encrypted folder later.

If an encrypted folder is unmounted and the correct key cannot be provided, the data stored in the folder cannot be accessed, even if the NAS drives are installed in another device.

**Note**: Encrypted folders formatted with Btrfs cannot be shared via NFS.

## Create an Encrypted Shared Folder

1. Open the Files app, then click "**+**" > "**Create shared folder**".

2. In the Create shared folder window, enter a folder name, then enable "**Encrypt folder**".

![](https://file-us.ugreennas.com/admin/article/2026-07-27/fc5dd3e8a8954e4fa469bbd5c1a3ce6d.webp)

3. Set key, and then click "**Save**".

![](https://file-us.ugreennas.com/admin/article/2026-07-27/7be91ea9085e4380bd53248017a4db9d.webp)

4. Click "**Create**" to create the shared folder.

## Encrypt an Existing Shared Folder

1. Open the Files app and locate the shared folder you want to encrypt.

2. Right-click the shared folder and select "**Properties**".

3. Go to the "**Encryption**" tab, then click "**Enable encryption**".

![](https://file-us.ugreennas.com/admin/article/2026-07-27/bb6c73db39e74a61b138bcc504ded898.webp)

4. Set key, and then click "**Save**".

![](https://file-us.ugreennas.com/admin/article/2026-07-27/de6a6e7ee13443628d010ec35d9bd084.webp)

## Encrypt a User Folder

Personal Folders support encryption. You can find the corresponding folder by username in the user folder list, or configure encryption after entering "**User Folder management**". Follow the steps below:

1. Open the **Files** app, and click "**Manage**" > "**User Folder management**" in the top bar.

2. On the User Folder management page, find the username of the folder you want to encrypt, then click "**···**" on the right ＞ "**Edit**".

3. On the Edit user folder page, switch to the "**Encryption**" tab.

4. Click "**Enable encryption**", set the key, and click "**Save**".

**Note**:

● If a standard user has enabled "**Hide personal files from other users**", the administrator cannot encrypt that user's folder.

● This feature requires the administrator to first enable "**Full rights**" for the user. After it is enabled, the user can enable "**Hide personal files from other users**" in Personal folder management.

## About the Key

The key is generated automatically only after a password is set, and it is automatically downloaded to the local device. The key cannot be downloaded again later by any other means.

If you forget the key or lose the key file, you will no longer be able to access the encrypted shared folder, and the data stored in it cannot be recovered.

The system automatically downloads the key file to the local device. The key file is required when mounting the encrypted shared folder later, so be sure to keep it in a safe place.

## Mount an Encrypted Folder

After a folder is encrypted, it is automatically mounted on the NAS. If you manually unmount the encrypted folder, you can mount it again from "**Management**" in the Files app.

To mount the folder, enter the key or import the corresponding key file.

![](https://file-us.ugreennas.com/admin/article/2026-07-27/4b36f376e2aa47e988f625b52a314129.webp)

**Notes**:

● If the key is incorrect or the key file does not match, the encrypted folder cannot be mounted.

● Keep the key file in a safe place. If the key is lost, you will no longer be able to access the data in the encrypted folder.

● After an encrypted folder is manually unmounted, it must be mounted again before it can be accessed.

### Mount an Encrypted User Folder

1. Open the Files app, then click "**Management**" > "**User Folder management**".

2. On the User Folder management page, locate the encrypted user folder, then click "**···**" > "**Mount**".

3. In the Mount window, enter the key or import the key file, then click "**Save**".

After the settings are saved, the system mounts the encrypted user folder. Once the folder is mounted successfully, you can access the data stored in it.

### Mount an Encrypted Shared Folder

1. Open the Files app, then click "**Management**" > "**Shared folder management**".

2. On the Shared folder management page, locate the encrypted shared folder, then click "**···**" > "**Mount**".

3. In the Mount window, enter the key or import the key file, then click "**Save**".

After the settings are saved, the system mounts the encrypted shared folder. Once the folder is mounted successfully, you can access the data stored in it.

![](https://file-us.ugreennas.com/admin/article/2026-07-27/aaca8328756f40adba7e4b32dda9edd6.webp)

## Decrypt an Encrypted Folder

After decryption, the folder is no longer encrypted, and users with permission to access the folder can continue to use the data stored in it. Follow these steps:

1. Open the Files app and locate the encrypted folder you want to decrypt.

2. Right-click the folder and select "**Properties**".

3. In the Properties window, go to the "**Encryption**" tab, then click "**···**" > "**Decrypt**".

4. In the Decrypt window, enter the key or import the key file, then click "**Confirm**".

The system will start decrypting the folder. Once the decryption is complete, you can access the data stored in the folder normally.

**Notes**:

● Only mounted encrypted folders can be decrypted. If the folder is currently unmounted, mount it first.

● After decryption, the folder is no longer protected by encryption.

● Decrypting a folder does not change its access permissions. Whether a user can access the folder still depends on its permission settings.

## Unmount an Encrypted Folder

After a folder is encrypted, it remains mounted by default and is ready for use. The folder continues to appear in the Files app, and users with the appropriate permissions can still access it.

If you do not want the encrypted folder to appear in the Files app or be accessible to other apps, you can manually unmount it.

After the folder is unmounted, it no longer appears in the file list of the Files app, and other apps (such as Music, Photos, and Theater) can no longer access its contents.

### Unmount an Encrypted User Folder

1. Open the Files app, then click "**Management**" > "**User Folder management**".

2. Locate the encrypted user folder you want to unmount, then click "**···**" > "**Unmount**".

3. In the confirmation dialog, click "**Unmount**".

### Unmount an Encrypted Shared Folder

1. Open the Files app, then click "**Management**" > "**Shared folder management**".

2. Locate the encrypted shared folder you want to unmount, then click "**···**" > "**Unmount**".

3. In the confirmation dialog, click "**Unmount**".

### Make the Folder Visible Again

To access an unmounted encrypted folder again, go to the corresponding folder management page and mount it.

When mounting the folder, enter the key or import the corresponding key file. Once the folder is mounted successfully, it will reappear in the Files app.

## Frequently Asked Questions

### Why can't I see an encrypted folder?

The encrypted folder may have been unmounted. You can check its status from the corresponding folder management page:

● Shared folders: Go to **Shared folder management**.

● User folders: Go to **User Folder management**.

If the folder has been unmounted, mount it again to make it appear in the Files app. When mounting the folder, enter the key or import the corresponding key file.

### Why does file transfer speed decrease after encrypting a shared folder?

This is normal. Folder encryption increases CPU workload. When reading from or writing to an encrypted folder, the system needs to encrypt or decrypt data, which may reduce file transfer speed.

The actual transfer speed depends on factors such as CPU performance, drive performance, network conditions, and file size.

### Can I back up data from an encrypted shared folder?

Yes. However, the encrypted folder must be mounted before it can be backed up. After the encrypted folder is mounted, the system can read the data in it in plaintext. You can then use the **Sync & Backup** feature to back up the data to another device.

Note that data backed up to another location will not retain the original folder's encryption status by default. If encryption is not enabled for the destination location, the backed-up data will be stored in plaintext.

If the encrypted folder is unmounted, the system cannot read the data inside it and cannot perform a backup.

### Why is there no encryption indicator after encrypting a folder?

When an encrypted folder is mounted, it does not affect the user experience during normal use. Therefore, the Files page does not display an obvious encryption indicator. To confirm whether a folder is encrypted, go to:

● **Shared folder management**

● **User Folder management**

Then check the encryption status on the corresponding folder management page.

### Can standard users use the folder encryption feature?

Yes. Standard users can enable encryption for their own user folders. Encrypting shared folders requires administrator permissions.

### Which apps are affected by the mount status of encrypted folders?

Apps that rely on folder contents may be affected. For example:

● Photos

● Docker

● Music

● Theater

● Snapshot

● Surveillance

If an encrypted folder is unmounted, these apps cannot access the content in that folder. After the folder is remounted, the apps can access the corresponding files again.

### Why Can't the Administrator Encrypt a User Folder?

If a standard user has enabled "**Hide personal files from other users**", the administrator cannot encrypt that user's folder.

This feature requires the administrator to first enable "**Full rights**" for the user. After it is enabled, the user can enable "**Hide personal files from other users**"in Personal folder management.

### What should I do if I forget the encryption key for an encrypted folder?

If you forget the key, you can use the system-generated key file to mount the folder.

When creating an encrypted folder, the system automatically generates a key file and downloads it to your local device. If you still have the key file, you can import it when mounting or decrypting the folder.

If both the key and key file are lost, the encrypted folder cannot be decrypted or mounted, and the data cannot be recovered.

If the encrypted folder is currently mounted, it is recommended that you copy or migrate important files to another secure location as soon as possible.
