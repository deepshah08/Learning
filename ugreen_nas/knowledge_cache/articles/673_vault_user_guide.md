# Vault User Guide

> **Article ID**: `673`  
> **Category**: `Application Guide > Vault > Vault User Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/673  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client, Web Browser

**Applicable Version**: UGOS Pro Firmware 1.7.0.3056 or later

The descriptions in this document are for reference only. The interface may vary depending on system or app updates, please refer to the actual interface.

## Introduction

The "**Vault**" uses encryption and access controls to protect the privacy of your sensitive data. It encrypts files using a dual-verification mechanism combining an "**access password + key file**", ensuring that only you can access the data.

● **Availability**: Currently available to "**admin**" only.

● **Data isolation**: Once enabled, each administrator on the device can create their own Vault. Vault data is isolated between administrators, and administrators cannot view the contents of other administrators’ Vaults.

## Installation and Access

1. Open "**App Center**" and find the "**Vault**" app.

2. Click "**Install**" and follow the on-screen instructions to complete the installation and setup.

3. Once installed, click the app icon on the desktop or under All Apps to start using it.

## Initial Setup

When opening the "**Vault**" app for the first time, complete the following initial setup:

1. Set a dedicated access password.

2. Click "**Volume**" and select where the encrypted data will be stored.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/1e4f391ccd24488ea14eeabd91889f06.webp)

3. Click "**Open now**". The system will automatically generate a unique .key key file.

4. Click "**Continue**" to complete the initial setup.

## Unlock and Access

After the initial setup is complete, authentication is required each time you access the Vault:

1. Enter the access password you set, or import the .key key file.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/4194083b1f964eeb9e2bfecfa1a8b6b0.webp)

2. Click "**Open**". Once authentication is successful, you can access the Vault.

## Features and Operations

After entering the Vault, you can manage encrypted data using the top toolbar or the right-click menu.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/1d93737806d9453eb4a5c84b0d2a0ccf.webp)

**Common Features**:

● **Create**: Click the "**+**" button on the top toolbar to create a new folder in the current location. You can also right-click a blank area in the folder list and select "**Create**" to quickly create a folder, document, or text file.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/804b82885eff4f1495a3f9e1a341294c.webp)

● **Upload**: Upload files or folders from your local computer to the Vault. Uploaded data is automatically encrypted.

● **View**: Switch between file display modes (icon view / list view).

● **Sort**: Sort files by name, modification date, or size.

● **Settings**: Change the storage location, change the password, or set the auto-lock time.

● **Search**: Enter keywords to quickly find files in the Vault.

## Manage Files

### Move to Vault

You can move files from NAS folders to the Vault for encrypted protection. The items you can move vary depending on the folder category.

**Rules**:

● **Personal Folder/User Folder**: After entering the category, you can directly select any folder or file to move.

● **Shared Folder**: You must first open a specific Shared Folder, then select a subfolder or file within it to move (the Shared Folder itself cannot be moved).

**Steps**:

1. Open the "**Files**" app.

2. Locate and select the target item:

● Under "**Personal Folder**" or "**User Folder**", directly select the target folder or file.

● Under "**Shared Folder**", first open the specific Shared Folder, then select a subfolder or file within it.

3. Right-click the target item and select "**Move to Vault**".

4. In the pop-up window, choose how to handle files with duplicate names. The system will then move and encrypt the data.

### Remove from Vault

1. In the Vault, select the target file, right-click it, and select "**Remove from vault**".

![](https://file-us.ugreennas.com/admin/article/2026-09-07/5e55a8f0ad9441579be953e8f0269b61.webp)

2. In the pop-up window, select the destination path, then click "**Confirm**" to move the file out of the Vault.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/f10acdd0ecac40469c95d8af02de4e71.webp)

### Auto-Lock

To help prevent unauthorized access while you are away, the Vault supports automatic locking:

1. Open "**Settings**" in the Vault.

2. Under "**Auto-lock window when not in operation**", set the idle time.

3. Click "**Confirm**" to apply the setting.

**Note**: After the Vault is locked, images that are already open and videos that are currently playing will not be forcibly closed and can still be viewed.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/34dfc2b6da3a47d1a259a7eaf9f3efa9.webp)

## Key and Password Management

### Key (.key) File Location

● **PC**: When enabling the Vault for the first time or changing the password, you will be prompted to manually select a location to save the key file.

● **Android**: `File Manager > Download > ugreenPro > key`

● **iOS**: `Files > On My iPhone > UGREEN NAS > OfflineCache > key`

**Note**: You can search for "**key**" directly in the file manager on your phone to quickly locate the key file.

### Forgot Password or Key File

● **Key file lost only**: If you still remember your access password, go to "**Settings**" > "**Change access password**" and enter a new password (it can be the same as your current password). The system will generate and download a new `.key` file.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/3856e9cadae94f539579b6bffaea105b.webp)

● **Both password and key file lost**: If you lose both the key file and access password, the data cannot be decrypted. You can only use "**Reset Vault**" to set up the Vault again.

### Reset Vault

This operation permanently deletes all data in the Vault for the current account and cannot be undone. You can reset the Vault if you forget the access password and lose the key file, or if you need to clear all data and configure the Vault again. The reset only affects the Vault of the current account.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/a7cca747f40f4822be9576779fe51c08.webp)

## FAQs

### Q1: Will resetting the NAS to factory settings delete Vault data?

No. A factory reset only resets system settings. Vault data remains in the storage location you specified.

### Q2: Will uninstalling the Vault app delete Vault data?

No. After reinstalling the app, simply enter the original access password to verify your identity and access the existing data.

### Q3: What should I do if I cannot delete a user?

If a user has activated the Vault, you must first log in to that user account, open the Vault app, and click "**Reset** '**Vault**'" to clear the Vault data before deleting the user.

For an AD domain user, whether the Vault data is retained depends on whether you select "**Keep data**" when deleting the AD domain user.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/5b37fb16806548a48a1c2504dc0fd181.webp)

### Q4: Why is my Vault data not visible after replacing a drive?

The Vault is linked to a specific Volume. If you remove the drive containing the original Volume and enable the Vault again on a new drive, the system will not recognize the existing Vault data on the original drive. Reinsert the original drive to access the data.

**Example**:

● When creating the Vault for the first time, you selected "**Volume 1**".

● You later removed the drive containing "**Volume 1**" and enabled the Vault on the drive containing "**Volume 2**".

● The system can now only recognize the Vault in "**Volume 2**". The data in "**Volume 1**" will not be recognized until the original drive is reinserted.

### Q5: Can files in the Vault be backed up?

Encrypted files in the Vault currently cannot be backed up using "**Sync & Backup**".
