# Will Resetting the UGREEN NAS to Factory Settings Erase Data and Affect Hard Drive Files?

> **Article ID**: `465`  
> **Category**: `Application Guide > Control Panel > FAQ > Will Resetting the UGREEN NAS to Factory Settings Erase Data and Affect Hard Drive Files?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/465  

---

After a factory reset, user-defined settings in the NAS system will be restored to default values, but the data stored on the hard drives will not be deleted.

**Note:** Files on the drives will not be erased. However, as a precaution, please ensure that all important data has been backed up before performing this operation. For more detailed information, please refer to [How to Perform a Factory Reset](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjo5ODgsImFydGljbGVJbmZvSWQiOjMyNSwiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIiLCJwYXRoQ29kZSI6IiJ9) and [Update and Restore](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMTYsImFydGljbGVJbmZvSWQiOjExMCwiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIxLjAiLCJwYXRoQ29kZSI6InBybzAwMSx1cmNhYmksZ2liaHUzIn0=) .

## Scope of Impact

After performing a factory reset, the following system-level functions and user configurations will be reset or cleared:

● **File Service Reset**: File sharing services such as SMB and WebDAV will need to be reconfigured.

● **DLNA Path Reset**: The media folder paths for the DLNA service will need to be set up again.

● **UPS Settings Reset**: If an external UPS (Uninterruptible Power Supply) is connected, it must be reconfigured and re-enabled after the reset.

● **Client Backup Path Reset**: Backup path bindings on all clients (such as PCs or mobile devices) will become invalid and must be set up again.

● **Sync and Backup Task Reset**: All file synchronization tasks and backup task records will be cleared and need to be recreated.

● **Applications and App Data Cleared**: Applications installed in the NAS system (such as Docker or virtual machines) will need to be reinstalled.

● **Other System Settings Reset**: In addition to the items listed above, all other user-defined system preferences will be restored to factory default settings.

![](https://file-us.ugreennas.com/admin/article/2026-02-28/2d00653fb6fe440c8882b90e8187da88.webp)

## Related Links:

● [【FAQ】What are the functions of the reset button?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMjUxLCJhcnRpY2xlSW5mb0lkIjo0MTYsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==)
