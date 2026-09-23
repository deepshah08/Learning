# Solution for “Service Error” When Creating a Local Sync or Backup Task on the Computer

> **Article ID**: `633`  
> **Category**: `Application Guide > Sync & Backup > FAQ > Solution for “Service Error” When Creating a Local Sync or Backup Task on the Computer`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/633  

---

## **Problem Analysis**

This issue may be caused by the following reasons:

* The syncSpace program might have been mistakenly identified as a virus or malware by antivirus software and thus was blocked or removed, preventing the service from starting.
* The syncSpace program may be incompatible with the Windows version; it requires Windows 7 SP1 or later, and the system may be missing necessary runtime libraries.
* The syncSpace program may fail to start due to corruption of certain files.
* syncSpace cannot be accessed via port 127.0.0.1:8395, possibly because the program did not start correctly.

## **Solution**

### **UGREEN NAS Client (Universal)**

1. Open the UGREEN NAS client and go to the [App Center].
2. Click on "Sync & Backup" to enter the application details page. Select "Disable" in the upper left corner, then click "Enable" to restart the sync service.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/deabc0ab-1e2e-4387-9417-39da0cbed532.png)

### **Windows Computer Troubleshooting**

**Exit and restart the client:**

Right-click the UGREEN NAS icon in the Windows system tray, select Exit, then restart the UGREEN NAS client.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/6c9dd932-8a00-4c49-9ced-c6c581998e6f.png)

**Check the status of the syncSpace program:**

1. Press Ctrl + Shift + Esc to open Task Manager, then search for syncSpace to see if the program is running.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/39d2d1f4-fc0a-4899-9323-122eb01caf16.png)

**If it is not running:**

1. Check the Recycle Bin and your antivirus software to ensure that the syncSpace program has not been mistakenly deleted.
2. Verify whether the syncspace\_pro.exe file exists in the UGREEN NAS installation directory (path: `C:\Program Files\UGREEN NAS\resources\public\win32\syncspace`).

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/fc585261-46c2-4f91-b484-cbd3af444937.png)

**If the program is running:**

1. Exit the UGREEN NAS client.
2. Using Windows File Explorer, navigate to the folder:

`%appdata%\UGREEN_Nas_Pro\apps\syncSpace` and open it.

3. Inside the `syncSpace` folder, you will see multiple folders named after device serial numbers (SN), such as `1000ECxxxxxxxxx`.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/1eaf1b1a-b6dc-4359-84e0-498ea1fad24b.png)

4. Locate the folder corresponding to your device and open it, then delete the `.config` folder inside.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/ef52a14a-62f2-4823-b9b3-c3b5d5f5e7de.png)

5. After deleting, reopen the UGREEN NAS client and check if the issue is resolved.

### **Mac Computer Troubleshooting**

1. Exit the UGREEN NAS client.
2. Hold down the Option key, click the [Go] menu at the top-left corner of the screen, and select Library.
3. Navigate to `Application Support/com.ugreen.desktop/UGREEN_Nas_Pro/apps/syncSpace` and open this folder.
4. Inside the `syncSpace` folder, you will see multiple folders named after device serial numbers (SN), such as `1000ECxxxxxxxxx`.
5. Locate the folder corresponding to your device and open it, then delete the `.config` folder inside.
6. After deletion, reopen the UGREEN NAS client and check if the issue is resolved.

## **Solution for Syncthing Not Starting on Some Windows Systems**

If you cannot access `127.0.0.1:8395` in your browser, it indicates that the Syncthing program failed to start properly. This may be caused by missing essential components in the Windows system.

### **Solution**

1. Download the latest official version of `syncthing.exe` from [the Syncthing GitHub page.](https://github.com/syncthing/syncthing)
2. If you encounter an error message when running the program, it means your Windows system might be missing critical components.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250715/418fa3df-fca1-4c96-b308-2b59576474b1.webp)

3. Install the Microsoft Visual C++ Redistributable packages on your computer. After installation, restart your computer.
4. Try running Syncthing again. If the program starts normally, the issue is resolved, and you can continue using the sync and backup features.
5. If it still fails to start, your Windows version may be a stripped-down edition that does not support the Syncthing service. It is recommended to use a full version of Windows.

> If you have tried all the above steps and the problem persists, please contact UGREEN NAS official technical support promptly for further assistance and solutions.
