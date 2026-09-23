# Synchronization

> **Article ID**: `166`  
> **Category**: `Application Guide > Sync & Backup > Synchronization`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/166  

---

In **Sync & Backup**, the sync feature refers to the automatic mechanism that keeps files or data consistent across different devices. UGOS Pro offers powerful sync capabilities, supporting data synchronization between local NAS, remote UGREEN NAS, and computers, ensuring that file versions remain consistent across all devices. If you make changes to a file on one device (such as adding or deleting), these changes would be automatically synced to all other connected devices. This is especially important for users who need to access the same data from different locations or devices.

The sync process in UGOS Pro is fully automated, requiring no manual intervention from users, which effectively reduces the risk of human error. Any file changes are immediately applied across all synced devices, ensuring data consistency and real-time updates.

## Accessing Sync

To access the **[Sync]** interface in **Sync & Backup**, follow these steps:

1. Open the UGOS Pro main interface and go to the App Library.
2. Navigate to the **Sync & Backup** app and click to open it.
3. In the **Sync & Backup** app, select the **Sync** option to enter the sync settings interface.

If you have not installed the **Sync & Backup** app yet, please follow these steps to install it:

1. Open the **App Center**.
2. Enter “Sync & Backup” in the search bar and search.
3. Find the **Sync & Backup** app and click the "**Install"** button.

Once installed, follow the steps above to access the **[Sync]** interface and begin setting up your sync tasks.

![](https://ugreen-pro.oss-cn-shenzhen.aliyuncs.com/ugreen-pro/admin/article/20241211/71f98f65-397e-4b15-92d8-96023b596772.png)

## Sync Use Cases

1. **Multi-device Collaboration**: In team environments, members often use different devices (such as desktops, laptops, and smartphones) to work on the same files. UGOS Pro’s sync feature automatically keeps these files consistent across all devices. Whether adding, modifying, or deleting files, any changes are instantly updated across all connected devices, saving the hassle of manual updates or copying. This ensures that everyone always has access to the latest version of the file.
2. **Remote Work**: Whether you're working from home, the office, or while traveling, UGOS Pro’s sync feature helps you seamlessly access and manage your data. With automatic syncing, you can continue working on the same set of data from different locations, maintaining continuity and efficiency in your workflow. This eliminates the geographic limitations of remote work and ensures smooth operations.
3. **Backup Sync**: Syncing is not just a powerful tool for multi-device collaboration; it’s also an efficient way to back up your data. You can sync data between multiple NAS devices to create redundant backups. If one device fails, the data will still be safely stored on other synced devices. This significantly improves data security and ensures continuous availability.
4. **Cross-platform Data Sharing**: UGOS Pro supports a variety of platforms, including Windows and macOS. This cross-platform support makes it easy to share and sync data between different operating systems, ensuring a consistent data experience no matter which device you're using.
5. **Version Control**: For files with multiple version updates, UGOS Pro’s sync feature makes it easy for teams to manage and track different versions.

## Supported Sync Modes

* **Two-Way Sync**: In this mode, file changes on both devices are automatically synchronized, ensuring consistency across all devices. For instance, if you edit a document on your computer, the corresponding file on the NAS will be updated as well.

* **One-Way Sync**: This mode supports one-way synchronization only, where data is either uploaded from the local device to the remote or downloaded from the remote to the local device. Data flows in only one direction, from the source device to the target device, without reverse synchronization. This method is ideal for backing up files but is not recommended for frequently edited work files.
