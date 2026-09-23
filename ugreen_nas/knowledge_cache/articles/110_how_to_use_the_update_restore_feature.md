# How to Use the Update & Restore Feature

> **Article ID**: `110`  
> **Category**: `Application Guide > Control Panel > How to Use the Update & Restore Feature`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/110  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client, Web Browser

**Applicable Version**: UGOS Pro Firmware 1.18.0.0076 or later

The screenshots in this document are for reference only. The actual interface may vary slightly depending on the system or app version, please refer to the actual interface displayed.

## Introduction

During daily system maintenance and device migration, you can use the "**Update & Restore**" feature in Control Panel to upgrade UGOS Pro **Firmware update, Network reset, Reset and Cloud backup/Local backup** **of system configurations**.

## System Update

Open the "**Control Panel**" app and click "**Update & Restore**". On the "**Update**" page, you can check the current system version, update to the latest firmware, and customize the system update settings.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/7c07ab4c2fbe42df8cdbd11042182d7f.webp)

### Online Automatic Update

The system will automatically check whether a new version is available. If an update is available, click "**Update**" to start the automatic upgrade. The device will restart automatically during the update process (this is normal).

**Note**: Ensure a stable power supply when updating the firmware. Do not disconnect the power during the update process.

### Manually Update Firmware

If you need to install a specific version or have not received the system update notification, you can manually install a firmware update.

1. Visit the [UGREEN NAS Download Center](https://ai.ugreen.com/pages/downloads), find your device model, and download the corresponding firmware package (in `.img` format).

2. After the firmware package is downloaded, open the "**Control Panel**" app and go to "**Update & Restore**" > "**Update**", then click "**Manual installation**".

3. Click "**Browse**" and select the downloaded firmware package. After the system verifies the package, click "**Confirm**".

![](https://file-us.ugreennas.com/admin/article/2026-08-12/0fae743cb86d46ffacba48a1398684b7.webp)

4. Follow the system instructions to complete the installation. The device will restart automatically after the update is complete. Once the restart is finished, you can log in to your device account again and start using the device.

### Update Settings and Policies

Click "**More settings**" > "**Update settings**" on the page to configure the following policies:

![](https://file-us.ugreennas.com/admin/article/2026-08-12/a264716855244644aaf2a9e4e8645fc2.webp)

**System update policy**:

● **Download important updates automatically (recommended)**: Automatically handles only important security and feature patches.

● **Download the latest updates automatically**: Keeps the system up to date with the latest firmware version.

● **Notify me and let me decide whether to install it**: Suitable for users who prefer to manually control device restart and update time.

**Check for updates**: Select "**Custom inspection interval**" to set the frequency for automatically checking for new versions (for example, check for updates every 22 hours).

### Import Root Public Key

This feature is intended for users who need to manually install firmware from a specific source:

1. Click "**More settings**" > "**Import root public key**".

2. In the pop-up window, click "**Browse**", select the matching root public key file in `.pub`format, and click Confirm to import it.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/c387a9a1d7f24dbf8de44855b0a7988d.webp)

## Reset Network Settings

When the device encounters a severe network issue and becomes inaccessible, you can reset the network settings to restore the network configuration to its initial state. The system provides two reset methods:

### Method 1: Reset from the system interface (when the device is accessible)

Click "**Control Panel**" > "**Update & Restore**". On the "**Restore & Reset**" page, click "**Reset network**". In the pop-up confirmation window, select "**I accept**" and click "**Reset**".

![](https://file-us.ugreennas.com/admin/article/2026-08-12/517e2e5621ad422ea926f561feaa3d21.webp)

### Method 2: Reset using the physical button (when the device cannot be logged in)

you can no longer log in to the UGOS Pro system normally through the network, use the physical **RESET** button on the NAS device:

1. When the device is powered on, use a SIM ejector tool to press and hold the **RESET** button for 5 seconds. Release the button after you hear a beep. The device will restart automatically.

2. The device will restart automatically, and the LAN and DISK indicators will blink white normally. You can search for and connect to the device within the local network.

3. After connecting, log in directly using the **admin** account (no password required). This account is only used for password reset.

4. After logging in, follow the setup wizard to complete the administrator password reset.

**Notes**:

● After resetting the network settings, the system will automatically enable a temporary account named **admin**. The account **has no password** and is only used for emergency administrator password reset.

● When you use the **admin** account to successfully reset the password of any administrator account, or when another valid administrator account successfully logs in, the temporary account will be immediately disabled by the system to ensure device security.

## Restore Factory Settings

Restoring factory settings will completely initialize the system configuration of the UGREEN NAS device and restore all system settings to their default factory state.

### Method 1: Reset from the system interface (when the device is accessible)

。Click "**Control Panel**" > "**Update & Restore**". On the "**Restore & Reset**" page, click "**Factory reset**". In the pop-up window, select **I accept** and click the "**Reset**" button.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/d0449e3d5a434ae78b2f05006890474d.webp)

**Notes**:

● Restoring factory settings only clears all customized system-level settings (including network configurations, user accounts, system configuration parameters, and installed apps). It does not delete files stored on the hard drives.

● This operation only initializes the local device. If you need to completely unbind the device from the current UGREEN Account (for example, when preparing to sell a personal device), make sure to go to "**Me**" > "**UGREEN Account**" settings and perform the unbinding operation.

### Method 2: Reset using the physical button (when the device cannot be logged in)

If you can no longer log in to the UGOS Pro system normally through the network, use the physical "**RESET**" button on the NAS device:

1. When the device is powered on, use a SIM ejector tool to press and hold the "**RESET**" button for 5 seconds. After hearing a beep, continue holding the button for **8** seconds until the device beeps three times again, then release the button.

2. The device will restart automatically and restore factory settings. When the LAN and DISK indicators blink white normally, the device is ready for use.

3. After the reset is complete, you need to initialize the device again.

## Configuration Backup & Restore

To prevent accidental loss of system settings or quickly restore your environment on a new device, it is recommended to back up system configurations regularly.

### Back Up System Configuration

You can choose to back up configurations to the cloud or download them locally:

**Cloud Backup (Automatic/Manual):**

1. Click "**Cloud backup**", check "**Scheduled backup of system configuration to UGREEN Account**". A login window will appear—complete verification as prompted.

2. After verification, the feature will be enabled. If system configurations change within 24 hours, they will be automatically backed up to your cloud account.

3. To create an immediate backup, click "**Back up**". Click "**Save**" after completion.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/797d12e4b06646afb38e4cd80e7f80c7.webp)

**Local Backup**:

Click "**Local backup**". The system will package the current configuration into a `.ugb` file and download it to your computer.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/1f04aa13ab204275a2aa42ac0ff0d730.webp)

### Restore System Configuration

Click "**Restore configuration**" and choose a method based on your backup type:

![](https://file-us.ugreennas.com/admin/article/2026-08-12/66d7c3abbc9345b9a72d81d4beef6610.webp)

**Method 1: Restore from UGREEN Account**

1. Select "**Restore from UGREEN account**" and click "**Next**". Log in and verify your account.

2. In the cloud list, select the configuration items you want to restore and click "**Confirm**".

![](https://file-us.ugreennas.com/admin/article/2026-08-12/e70feff8132e4cd8989820956cd8544f.webp)

3. Check "**I accept**" and click"**Restore**". Wait for the process to complete.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/ef8ed22a9da444c08a3451f1c5163d0f.webp)

**Method 2: Restore from Local File**

1. Select "**Restore from the local configuration file on computer**", click "**Browse**", and upload the `.ugb` file. Wait for validation.

2. After validation, click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-08-12/2ef196ad70114f7c9e0f23776e563898.webp)

3. Select the configuration items to restore and click "**Confirm**".

![](https://file-us.ugreennas.com/admin/article/2026-08-12/5099375ba87c4f2c95305fa89638209d.webp)

4. Check "**I accept**" and click **"Restore**". Wait for completion.

![](https://file-us.ugreennas.com/admin/article/2026-08-12/1a74575ef16a475695e452ff821f0b70.webp)

**Notes**:

After the configuration restore is complete, the system environment will be changed, and all current login sessions will be forcibly logged out. You need to log in to the UGOS Pro desktop again using the restored account information.
