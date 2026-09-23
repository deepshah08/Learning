# How to Back Up and Restore UGOS Pro System Settings When Replacing or Resetting a UGREEN NAS Device?

> **Article ID**: `464`  
> **Category**: `Application Guide > Control Panel > FAQ > How to Back Up and Restore UGOS Pro System Settings When Replacing or Resetting a UGREEN NAS Device?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/464  

---

When replacing or resetting your UGREEN NAS device, you can back up the UGOS Pro system configuration to quickly restore system settings. This helps avoid reconfiguring the system from scratch and saves significant time. Below are the detailed steps for backing up and restoring system settings.

## Configuration Items Supported for Backup and Restore

● **Connectivity & Access:** User and user groups (including permissions and advanced settings), File Service, UGREENlink device connection, DDNS, Portal Settings, Terminal, Domain/LDAP.

● **General Settings:** Time & Language, Notification Settings, Network Configuration, Security, Indexing Service.

● **System Services:** System Updates, System Reset, Configuration Backup and Restore.

**Note:** Some configurations, such as network settings, traffic control, and firewall rules, may not apply after restoration depending on your current environment.

## How to Back Up UGOS Pro System Settings?

You can choose between two backup methods: **cloud backup** or **local backup**.

![](https://file-us.ugreennas.com/admin/article/2025-09-15/4d9f0025f259468aa7c3d4cb2b815db9.webp)

### Method 1: Cloud Backup

1. Go to [Control Panel] > [Update & Restore] > [Configuration backup & restore].

2. Select "Cloud backup". You can choose to enable the "Periodically update configuration backup automatically to online account" feature to regularly sync the latest configuration to your online account.

3. After clicking "Save", you will be redirected to the UGREEN Account login page. Enter your registered account credentials to bind your device. If you don’t have an account, please register first. See guide: How to Register a UGREEN Account?

4. In the [Cloud backup] pop-up window, click "Back up". The system will automatically back up your current UGOS Pro configuration to the cloud.

![](https://file-us.ugreennas.com/admin/article/2025-09-15/4cc4b43a01ee4b64954829a91efda07a.webp)

5. After confirming the backup is complete, click "Save".

Note: If the "Auto Backup System Configuration" feature is enabled, any configuration changes made within 24 hours will be automatically synced to the linked UGREEN Cloud account.

### Method 2: Local Backup

1. Go to [Control Panel] > [Update & Restore] > [Configuration backup & restore].

2. Click the "Local backup" button. The system will automatically download the configuration file to your computer in `.ugb` format.

![](https://file-us.ugreennas.com/admin/article/2025-09-15/e7da1ad7e66a47e08d5578c59e8f9127.webp)

## How to Restore UGOS Pro System Settings?

You can restore your UGOS Pro system configuration either from your **UGREEN Account** or from a **local configuration backup file stored on your computer**.

![](https://file-us.ugreennas.com/admin/article/2025-09-15/2c5cf24b803747d4ae1377307860f294.webp)

### Method 1: Restore from UGREEN Account

1. Go to [Control Panel] > [Update & Restore] > [Configuration backup & restore], and click "Restore configuration".

2. In the "Restore System Configuration" source options, select "Restore from UGREEN Account".

![](https://file-us.ugreennas.com/admin/article/2025-09-15/8be296f88fe24885b958a4d67baadbba.webp)

3. Click "Next" to be redirected to the UGREEN Account login page. Enter your account credentials to complete verification.

4. In the "Restore configuration" pop-up window, select the specific items you wish to restore, then click "Confirm".

![](https://file-us.ugreennas.com/admin/article/2025-09-15/e3a06b1628e54e8caf810c762be42ca9.webp)

5. Check the box "I accept", then click "Restore". The system will automatically apply the selected configuration settings to the current system.

![](https://file-us.ugreennas.com/admin/article/2025-09-15/903a8e1601cf43cdb8e1cc72f94135f4.webp)

### Method 2: Restore from a Local Configuration File on Your Computer

1. Go to [Control Panel] > [Update & Restore] > [Configuration backup & restore], and click "Restore configuration".

2. In the "Restore System Configuration" source options, select "Restore from the local configuration file on the computer".

![](https://file-us.ugreennas.com/admin/article/2025-09-15/376ac54267bf47cb9f5f00338f63ca20.webp)

3. Click "Browse" to select the `.ugb` configuration file from your computer, then click "Next" to upload the file.

4. In the "Restore Configuration" pop-up window, select the specific items you want to restore and click "Confirm".

5. Check the box "I accept", then click "Restore". The system will automatically apply the selected configuration settings to the current system.
