# Sync with Another UGREEN NAS

> **Article ID**: `398`  
> **Category**: `Application Guide > Sync & Backup > Sync with Another UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/398  

---

Sync and backup functions support cross-device data synchronization, allowing for seamless real-time backup and sharing of files between multiple UGREEN NAS devices. This ensures data security and efficient management. If you have two UGREEN NAS devices and need to sync data, you can follow the steps below to connect them.

## **Create a Sync Task**

1. Open the **Sync&Backup** app.
2. In the **Sync** interface, click the "**Create Sync Task**" or "**Add**" button to create a new sync task.
3. Select "**Sync another UGREEN NAS**" as the sync target.
4. Click "**Next**" to continue.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250226/3d33d5d6-1491-461a-9f81-9171bfac236a.png)

## **Set Sync Target**

In the pop-up setup window, fill in the information for the other UGREEN NAS device to sync with:

* **IP Address/UGREENlink ID**: Enter the IP address, domain name, or UGREENlink ID of the other UGREEN NAS device.

* **Port**: The default port is 9999 when using the IP address or UGREENlink ID, and 22000 when using the domain name.

* **Username**: Enter the username to connect to the device.

* **Password**: Enter the corresponding login password.

* **Encryption**: By default, it is turned off.

After confirming the information is correct, click "**Confirm**" to proceed to the next step.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250226/880c450d-2101-4aa5-abf8-34cae13729f9.png)

If you have already connected a remote UGREEN NAS device, you can select the corresponding device from the "**Existing Connections**" dropdown menu and click "**Confirm**" to proceed.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250226/a0f96dfd-cb50-4362-925e-f9b00a960c43.png)

## **Set Sync Rules**

When creating a synchronization task, you need to specify the synchronization paths and select the synchronization method to ensure files are synced as needed.

### **Specify Synchronization Paths**

* **Remote Path**: Select the target location on the other UGREEN NAS where the synchronized files will be stored.

* **Local Path**: Select the source location on the current UGREEN NAS where the files to be synchronized are located.

### **Choose Sync Method**

* **Two-Way Sync**: Files are synchronized between both devices, ensuring data consistency on both sides.
* **One-Way Upload**: Only local data is uploaded to the remote device.
* **One-Way Download**: Only remote data is downloaded to the local device.

### **Example**

To synchronize **Shared Folder A** on the local device with **Shared Folder B** on the remote device, create a synchronization task with the following settings:

* **Remote Path**: Shared Folder B

* **Local Path**: Shared Folder A

* **Synchronization Method**: Bidirectional Sync

Once completed, the folders on both devices will always remain synchronized.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250226/8c64f11d-0acc-4d23-8c8c-85c587409c20.png)

## **Advanced Settings**

In the **Advanced Settings** section of the synchronization rules, you can fine-tune the details of your synchronization task.

### **Sync Folders**

You can choose the specific folders to synchronize:

* If a subfolder does not need to be synchronized, uncheck the corresponding option. This will prevent the subfolder from being synchronized.
* To restore synchronization for a subfolder, simply recheck the box next to it.

**Default Rule**: By default, synchronization tasks exclude files and folders with a "dot" prefix (e.g., hidden files). To synchronize these hidden files or folders, manually check the corresponding option.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250226/1d9e5ec2-551e-4efb-b356-4d58f8893a0a.png)

### **Filter Rule**

In the Filter Rules section, you can specify file names or extensions that should not be synced:

* Check the “**Filter the following file names or extensions**” option and adjust or add filter rules as needed.
* To remove a filter rule, hover over it in the list and click the floating “**X**” button.
* To add a new filter rule, click the “**Add**” button, then enter the file name or extension in the popup window. Use `“;”` to separate multiple entries.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250226/59b96162-0d0d-4af7-9e2f-30dd2ae8ee13.png)

**Example:**

● Filter specific file names: e.g., `abc.doc`;`test*.doc`;`tmp.*`.

● Filter specific file types: e.g., `*.jpg`.

**Default filter format:**

|  |  |
| --- | --- |
| \*.lnk | \*.swp |
| \*.temp | \*.tmp |

### **File Conflict Handling**

In the [**File Conflict**] settings, you can specify how to handle conflicts when files clash. By default, the system will rename the conflicting files to prevent data loss.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250226/bbe9f6c2-04e6-44f8-8bb9-bbb7a2b2e3a4.png)

### **Sync Strategy Settings**

After completing the **Sync Rules** configuration, click **“Next”** to proceed to the **Sync Strategy** settings page. In [**Sync Strategy]**, select a sync mode:

* **Real-time Sync:** The system automatically syncs files when changes are detected.
* **Manual Sync:** Sync is performed only when you manually click **“Sync Now”**.
* **Scheduled Sync:** To set up a scheduled sync, click “**Add Schedule**” to define the sync frequency (Once, Daily, Weekly, Monthly, or Custom) and configure the start time for synchronization.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250226/eaf184d8-42d1-4a87-87d8-202f41abe21c.png)

Once the selection is complete, click "**Next**" to proceed to the preview.

## **Preview and Task Creation**

In the [**Preview**] interface, you can customize the sync task name and review the configuration options set earlier. Once confirmed, click **“Confirm”** to create the sync task. If you check **“Sync Immediately After Creation”**, the system will start syncing as soon as the task is created.

## **Task Management**

After the task is created, you can manage connected sync devices and tasks in the [**Sync**] interface:

* **Pause Sync**: Click the **“Stop Syncing”** button to pause the task.
* **More Actions**: Click the **“More”** button to view the operation log, edit, or delete the task.
* **Quick Task Creation**: Click the **“···”** button on the right side of the sync device to quickly create a new sync task for that device.

## **Function Description**

**Version Requirements**

* The remote device must be running UGOS Pro system and have the "Sync and Backup" app installed.

**Connection Methods**

* Same Local Network: Direct connection via local IP address is supported.

* Cross-network: Use UGREENlink ID for remote connection.

* **Domain** Name Connection: Ensure both local and remote UGREEN NAS devices have "Sync and Backup" app version V1.1.2.0649 or higher.

* Make sure both devices have stable network connections and that the firewall or router does not block the required ports. Domain name connections require port `22000` to be mapped.

* If the connection fails, verify that the device is online and confirm the UGREENlink ID or domain name is entered correctly.
