# Restore Backup to UGREEN NAS

> **Article ID**: `403`  
> **Category**: `Application Guide > Sync & Backup > Restore Backup to UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/403  

---

The UGOS Pro system of UGREEN NAS offers two restore methods, catering to different backup storage locations and recovery needs:

|  |  |  |
| --- | --- | --- |
| **Restore Methods** | **Applicable Scenarios** | **Feature** |
| **Backup Task Restore** | Restore from UGREEN NAS or remote server | Automatically retrieve backup tasks, supporting multiple versions |
| **Backup File Restore** | Restore from local NAS, USB devices, or remote protocols | Flexibly adapts to various storage types |

## **Restore from Backup Task Guide**

### Step 1: Enter the Restore Interface

* Log into the UGREEN NAS UGOS Pro system > Click on the **Backup & Sync** app > In the left menu, select **Back up & Restore** > Click the “**Restore”** button.

### Step 2: Choose the Restore Method

* Click "**From Backup Task**" in [**Select Restore Mode**] interface.

### **Step3: Choose Backup Task and Version**

1. **Task Filtering**: The system lists all completed backup tasks > Select the target task (supports sorting by name and time).

2. **Version Selection**: Click the **Version Selection** dropdown menu > The system will automatically verify the backup package, and once verification is complete, select the content to restore. Supports folder hierarchy checkboxes > Expand the tree directory to select specific subfolders or files.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250303/07889fa5-42cf-4c47-9494-e8bda623555a.png)

### **Step 4: Download the Backup Package**

* Click "**Done**" to submit the task, and the system will automatically pull the data package from the backup storage location.
* You can view the progress bar of the restore task in the **Task Center** to track the file transfer percentage and remaining time.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250303/15aea577-2e80-4ba7-a5db-1ffb84a9b1ad.png)

## **Restore from Backup File Guide**

This method supports restoring backup files from local NAS folders, USB mounted devices, or file servers through rsync or WebDAV.

### **1.** Restore from Local NAS or USB Device

Prepare the backup package by copying the backup files to a USB drive and mounting it to the NAS, or directly store them in a NAS directory.

**Format Requirement**: The backup package folder must be in the `.ubk` format.

1. **Choose Restore Method**: In the[ **Select Restore Mode]** interface, click [**From Backup File]** > select" **Local Folder & USB**."
2. **Retrieve Backup Package**: Click "**Next** "> choose the backup package storage path > the system will automatically detect `.ubk` files.
3. **Configure Restore Content**: Select the backup package > click "**Next"** > choose the restore version > in[ Restore Content,] select the folders to restore > click "**Done**".

### **2.** Restore from rsync or WebDAV Server

1. **Connect to Remote Server**: In the [**Select Restore Mode]** interface, click [**From Backup File]** > select [**Rsync & WebDAV]**, then click "**Next"**.
2. **Fill in Server Parameters**: Enter the server address, port, username, password, etc., then click "**Connect**".
3. **Select Backup Package Storage Path**: The system will automatically detect the `.ubk` files.
4. **Configure Restore Content**: Choose the restore version > in [**Restore Content]**, select the folders to restore > click "**Done**"**.**

## **WebDAV Server Restore Path Configuration Guide**

**Applicable Scenario**: Restoring backup files from UGREEN NAS as a WebDAV server.

1. **Root Folder Path Format:** If the WebDAV server is UGREEN NAS, the root folder path must be the name of the shared folder.

|  |  |  |
| --- | --- | --- |
| **Example** | **Shared Folder Name** | **Path** |
| `downloads` | `/downloads` |
| `documents` | `/documents` |

2. **Path Entry Notes**:

* **Case-sensitive**: Ensure the path name matches exactly with the shared folder (e.g., `/Downloads` ≠ `/downloads`).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250303/c4c1df6f-79c4-4bd1-a6af-05ef4ba18f20.png)
