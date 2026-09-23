# Rsync

> **Article ID**: `81`  
> **Category**: `Application Guide > Control Panel > File Service > Rsync`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/81  

---

rsync is an efficient data transfer protocol widely used for local and remote data synchronization and backup. The UGOS Pro system supports users in performing data backup and synchronization through the rsync protocol, ensuring the security and integrity of the data.

## **Enable rsync Service**

1. Open the "Control Panel" application, click on [File Service] > [Rsync].
2. Check the box for "Enable rsync backup service," select the NAS user to be used as the rsync account, and set a password (the password can be a unique rsync password).
3. Click "Apply" to save and take effect.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/2daf9364-f343-48c8-a1ff-db1f187af559.png)

### **Rsync Advanced Settings**

By default, the rsync service uses port number 873. If this port is occupied, you can modify it:

1. In the [Rync] option, click on "Advanced Settings" to change the port number.
2. Click "Save," then click "Apply" to make the settings effective.

### **Precautions for rsync**

* Ensure that the rsync service and client have the correct read and write permissions to prevent synchronization failures.
* Check the user account password and other settings in the rsync configuration to ensure they are correctly configured.
* Maintain consistent source and target directory structures during synchronization to avoid errors caused by changes in directory structure.

## **Rsync Usage Example**

The UGOS Pro system supports using the rsync protocol to back up files between two UGREEN NAS devices. Here are the specific steps:

### **Back up this NAS to another UGREEN NAS**

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/6312f5c0-319f-4025-8ba5-964c9d1a54ea.png)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/f3e23ba3-b24d-4229-bff8-7a267c8d0004.png)

3. Select "Backup this UGREEN NAS", and click "Next" to continue.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/13492ea3-f083-471e-8571-aadb324ca452.png)

4. Select "rsync" as the server type, enter the IP address of the other UGREEN NAS as the server address, and fill in the username and password set up in the [rsync] service. Leave other settings at their default values.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/647df280-850b-4590-bdba-aa7b7fbe5c68.png)

5. After the settings are completed, click "Confirm" to attempt a connection to another NAS.
6. Once connected successfully, select the folders on this machine that you want to back up, and set the storage location for the backup files on the other UGREEN NAS. Click "Next".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/1d0271f2-8829-4e74-8b4b-97cd1b2b7a4d.png)

7. Set the scheduled time for the backup plan to take effect, and click "Next" to continue.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/ca3ba8a9-845d-4739-b758-7ad2daf1bcc1.png)

8. Set the name of the backup task, and click "Confirm" to create the backup task.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/7c51cc0a-cdc8-4a95-a537-1b595092033e.png)

9. You can view and manage backup tasks at any time on the [Back up & Restore] page.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250404/29fb4f93-2f85-4698-8f1a-30eba3c2f0e0.png)

### **Back up another UGREEN NAS to this [NAS].**

1. Ensure that the other UGREEN NAS has the rsync service enabled, and note down the account and password set in the rsync service.
2. Open the [Sync & Backup] app and click the "Add" button.

![](https://alidocs.dingtalk.com/core/api/resources/img/5eecdaf48460cde5588831cfe2f3ba8afd09728f81a35c3475b8339e1c4c248338f7172fbdbb00108d68742cd653602a0524375348f90ffd6548c61b9d7a141ed63d6dd6bcf9eac237d4f84bf74bdc92cee52844b03aa766ce12d893bc7e6de7?tmpCode=baa4c39a-e1af-4f2e-8d3e-af37b8dc3c12)

3. For the backup type, select "Backup rsync server," and click "Next" to continue.

![](https://alidocs.dingtalk.com/core/api/resources/img/5eecdaf48460cde5588831cfe2f3ba8afd09728f81a35c3475b8339e1c4c248338f7172fbdbb00108d68742cd653602aa3ba6b64951bcf7ec35b2cc183afb50009ff6abf8f41d28f9b4f0023a047714d83727eea190d2aba48b6279544963798?tmpCode=baa4c39a-e1af-4f2e-8d3e-af37b8dc3c12)

4. Enter the IP address of the other UGREEN NAS for the server address, and fill in the username and password that were set up in the [rsync] service, leaving all other settings at their default values.

![](https://alidocs.dingtalk.com/core/api/resources/img/5eecdaf48460cde5588831cfe2f3ba8afd09728f81a35c3475b8339e1c4c248338f7172fbdbb00108d68742cd653602a358e919a3f95be9adeecc886998a49e2beba7eba89c202cfc788715c15a034f58611f72270b798953b08dc375507598c?tmpCode=baa4c39a-e1af-4f2e-8d3e-af37b8dc3c12)

5. After the settings are complete, click "Confirm" to attempt a connection to another NAS.
6. Once connected successfully, select the folders on the other UGREEN NAS that you want to back up, set the storage location for the backup files on this NAS, and click "Next".

![](https://alidocs.dingtalk.com/core/api/resources/img/5eecdaf48460cde5588831cfe2f3ba8afd09728f81a35c3475b8339e1c4c248338f7172fbdbb00108d68742cd653602aa3ba6b64951bcf7e68fb6e3c1106c25dc2e13e8b1694d94b2b44b0513c5000dcc167a018cbd197f3b1221881769dd4cb?tmpCode=baa4c39a-e1af-4f2e-8d3e-af37b8dc3c12)

7. Select the backup mode you want to use, set the scheduled activation time for the backup plan, and click "Next".

![](https://alidocs.dingtalk.com/core/api/resources/img/5eecdaf48460cde5588831cfe2f3ba8afd09728f81a35c3475b8339e1c4c248338f7172fbdbb00108d68742cd653602a15464a86392b1bf5337451d4d418def957390ecce4505db1f575ed6c1f8f47003dcf2ed1b85afb645d6ed084c6c54836?tmpCode=baa4c39a-e1af-4f2e-8d3e-af37b8dc3c12)

8. Set the name for the backup task, and click "Confirm" to create the backup task.

![](https://alidocs.dingtalk.com/core/api/resources/img/5eecdaf48460cde5588831cfe2f3ba8afd09728f81a35c3475b8339e1c4c248338f7172fbdbb00108d68742cd653602aa3ba6b64951bcf7ec7d487e9d604f5c9d3bb3b44a3d49f6176486ba548cb0c625194002a99d19d0cc9d7ed20d9d34c07?tmpCode=baa4c39a-e1af-4f2e-8d3e-af37b8dc3c12)

9. You can view and manage backup tasks at any time on the [Back up & Restore] page.

![](https://alidocs.dingtalk.com/core/api/resources/img/5eecdaf48460cde5588831cfe2f3ba8afd09728f81a35c3475b8339e1c4c248338f7172fbdbb00108d68742cd653602afa4cc552274ccc038db5a745f4544fc96d6cc68985f0ea2df90347e8722f1dae1dc2565aa6d441b339d5906575207134?tmpCode=baa4c39a-e1af-4f2e-8d3e-af37b8dc3c12)
