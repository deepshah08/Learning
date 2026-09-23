# Can files inside the Vault be backed up?

> **Article ID**: `749`  
> **Category**: `Application Guide > Vault > Can files inside the Vault be backed up?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/749  

---

## Issue Description

I want to back up important files stored in the Vault using the NAS’s "Sync & Backup" feature. Is this supported?

## Cause Analysis

Currently, UGREEN NAS’s "Sync & Backup" feature only supports synchronization and backup of contents within regular folders. The Vault uses an independent encrypted storage mechanism, and its data is not accessible by other applications, so it cannot be directly recognized or operated on by the sync and backup service.

## Solution

Files inside the Vault are not currently supported for automatic backup via the "Sync & Backup" feature.  
If backup is needed, it is recommended to manually copy files from the Vault to a regular folder first, and then use the sync and backup function to back them up.
