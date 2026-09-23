# Backup Rsync Server to UGREEN NAS

> **Article ID**: `169`  
> **Category**: `Application Guide > Sync & Backup > Backup Rsync Server to UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/169  

---

To protect your data, backing up data from a remote rsync file server (such as UGREEN NAS) to a local UGREEN NAS is an effective method. By configuring regular backup tasks, you can ensure important files are securely stored locally for easy access and management. Here are the steps and considerations:

## **Create Backup Task**

1.Log in to your UGOS Pro system and go to the **[Sync & Backup]** module.

2.On the left sidebar, select **Backup & Restore**, then click **"Add"**. In the popup options, choose **Backup Rsync Server**.

3.Click **"Next"** to enter the configuration wizard.

![](https://ugreen-pro.oss-cn-shenzhen.aliyuncs.com/ugreen-pro/admin/article/20241211/1d7d4813-318f-493d-8bfe-c96a5c830268.png)

## **Connect rsync Server**

In the popup **[New Backup Task]** interface, fill in the information as follows:

![](https://ugreen-pro.oss-cn-shenzhen.aliyuncs.com/ugreen-pro/admin/article/20241211/54d02dd7-b511-4475-a64c-c1c22a80e074.png)

### **1. Server Name/IP Address**

Enter the IP address of the remote rsync server. If the remote rsync server (e.g., another UGREEN NAS) is not on the same local network as the current device, ensure the following conditions are met:

● The remote rsync server has a public IP address and port mapping is configured. Please refer to the [**Enable DDNS Support**](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmODYifQ==) guide for more details.

● The current NAS can connect to the server via remote access.

● The remote device has the rsync service installed and enabled.

### **2. Port**

Enter the communication port number for the rsync service. The default port is **873**. If a non-default port is used, enter the appropriate one.

### **3. Username and Password**

Enter the username and password configured on the remote rsync server. Ensure the account has access rights to the corresponding backup directory.

### **4. Transmission Encryption**

You can choose whether to enable data encryption based on your needs. While enabling encryption enhances transfer security, it may slightly reduce the transfer speed.

### **5. Quick Connect Option**

If you have previously connected to the rsync server, you can directly select the device from the **“Existing Connections”** dropdown menu to avoid re-entering the information.

![](https://ugreen-pro.oss-cn-shenzhen.aliyuncs.com/ugreen-pro/admin/article/20241211/0572a00e-fdb1-41b3-862d-d9aa51bd4dea.png)

Once you’ve verified that all the information is correct, click **"Confirm"**.

## **Configure Backup Task**

### **1. Select Backup Source Directory**

* In the backup task configuration page, the system will automatically display the directory structure of the remote rsync server.
* Browse through the directories and select the **source directory** you want to back up, ensuring it contains the important files you wish to preserve.

### **2. Select Backup Destination**

Specify the backup storage path on your local UGREEN NAS.We recommend creating separate folders for each backup task to keep files organized and simplify future management. For example,

Backup Task 1: Store in `/Shared Folder/music1`

Backup Task 2: Store in `/Shared Folder/music2`

### **3. Set Filter Rule**

Filtering rules help you precisely select the files you want to back up, reducing unnecessary data transfer.

**File Size Limitation**

Enable the "Limit File Size" option to set a maximum file size. Files larger than this limit will not be backed up. For example, you can set the maximum size to 100 MB to exclude large video files.

**Filter by File Name or Extension**

Enable the "Filter by File Name or Extension" option, then click "Add" to input the file names or extensions you want to filter (separate multiple conditions with a semicolon`;`). For example, entering`*.log;*.tmp;*.swp` will exclude log files, temporary files, etc.

**Default Filtering Rules**

The system includes several default filtering rules, which you can adjust as needed:

`*.link`、`*.swp`、`*.temp`、`*.tmp`；

To delete a rule, hover over the target rule and click the "X" button that appears.

### **4. Set Backup Rules**

Choose the appropriate backup mode based on your needs, and set the backup schedule:

**Backup Mode**

* Incremental Backup：Backs up only the new or modified files since the last operation. Deleted files are still retained in the backup destination, making it ideal for scenarios where long-term historical records need to be preserved.
* Image Backup：Ensures the backup destination matches the source directory exactly, including removing files that were deleted from the source. This mode is suitable for precise synchronization needs.
* Multi-version Backup：Each backup creates a new version folder in the destination, allowing you to easily roll back to previous versions. You can configure a "Backup Version Policy" and set a version limit (e.g., 5). Once the limit is reached, the oldest versions will be automatically deleted.

**Backup Plan**

Set the backup frequency, such as daily, weekly, or monthly. Specify the time window for the task (e.g., start backup at 2:00 AM) to minimize the impact on device usage during the day.

Once configured, click “Next” to continue.

### **5. Backup Preview**

* **Custom Task Name**: Set a descriptive name for the backup task, such as "Project A Daily Backup."
* **Review Backup Settings**: Confirm the Source, Backup Destination, Backup Mode, and Backup Plan are correct.
* **Run Backup Immediately**: Check **"Back up immediately after creation"** box to start the backup automatically after creating the task.

Once all configurations are confirmed, click **“Confirm”** to create the backup task.

## **Monitor Real-time Task Status**

In the **[Back up & Restore]** module, you can monitor and adjust the status of your backup tasks at any time:

### **1. To Monitor Real-time Task Status**

The following key information will be displayed on the interface:

* **Connection Information**: Shows the IP address of the remote server and its connection status.

* **Task Name**: Identifies different backup tasks.

* **Backup Destination**: Displays the storage path for the task.

* **Last Execution Time and Result**: Indicates whether the task was completed successfully.

* **Next Scheduled Time**: Shows the next scheduled start time for the task.

### **2. To Adjust Task Settings**

* If you need to modify the task, ensure it has not been executed, then click the **“More”** button on the right side of the task and select **“Edit Task”**.

* You can modify the source directory, backup destination, filter rules, or backup mode.

### [**3. To**](http://3.To) **Pause or Delete a Task**

* **Pause Task**: Suitable for situations when you temporarily don’t need the backup to run.
* **Delete Task**: Suitable for removing completed or unnecessary backup tasks.

### **4. To Do Quick Action**

Click the **"..."** button on the right side of the task to perform the following quick actions:

* **Create New Task**: Quickly generate a new backup task based on the current task's server.

* **Set Notes**: Add custom notes or descriptions to the device or task.

* **Delete Connection**: Remove the server connection information.
