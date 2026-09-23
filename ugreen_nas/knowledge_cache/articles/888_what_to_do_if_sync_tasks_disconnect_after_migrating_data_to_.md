# What to Do If Sync Tasks Disconnect After Migrating Data to a New Mac

> **Article ID**: `888`  
> **Category**: `Application Guide > Sync & Backup > FAQ > What to Do If Sync Tasks Disconnect After Migrating Data to a New Mac`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/888  

---

## Applicability

**Supported clients:** UGREEN NAS PC Client (Windows/macOS)

**Supported versions:** NAS firmware 1.15.0.0034 or later.

The descriptions and screenshots in this document are for reference only. The actual interface and navigation may vary slightly depending on your system or application version. Please refer to the interface displayed on your device.

## Issue

After migrating data from one Mac to another, you may encounter the following issues when creating a sync or backup task on the new Mac:

● The NAS sync service recognizes only one of the two Macs.

● When one Mac connects to the sync service, the other Mac is disconnected.

● The sync task on the new Mac has the same name as the one on the old Mac.

● Sync tasks cannot be created or run normally on the new Mac.

## Cause

When data is migrated from the old Mac to the new one, the local configuration of the syncSpace sync engine is also migrated. As a result, the syncSpace sync engine on both Macs uses the same local configuration.

The system may recognize both Macs as the same device, resulting in sync connection conflicts.

## Solution

Clear the migrated local configuration on the new Mac.

Follow these steps:

1. Quit the UGREEN NAS desktop client. Then press and hold the **Option** key from the menu bar at the top of the screen.

2. Click “**Go**” at the top left > “**Library**”.

3. Navigate to the following directory:

```
Application Support/UGREEN_Nas_Pro/apps/syncSpace
```

4. In this directory, locate the configuration folder for the currently signed-in NAS account. The folder name is typically similar to the following:

```
1000ECxxxxxxxxx
```

5. Delete the **.config** folder in the configuration folder.

6. Restart the UGREEN NAS desktop client.

After the client restarts, create a new sync task or reconnect the existing one.

## If the .config Folder Cannot Be Found

If the **.config** folder is not found in the current user configuration directory, rename the parent user configuration folder instead.

For example, rename `1000ECxxxxxxxxx`to `1000ECxxxxxxxxx_backup`, and then restart the UGREEN NAS desktop client.

## Notes

● If multiple user configuration folders exist in this directory, do not delete all directly. First identify the user configuration that needs to be processed.

● Before deleting or renaming a configuration directory, it is recommended to quit the UGREEN NAS desktop client first. This helps prevent the client from using configuration files during the operation, which could result in incomplete cleanup.

● This operation is only used to resolve conflicts in the Mac local sync configuration. It will not delete files already saved on the NAS.
