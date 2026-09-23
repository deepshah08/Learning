# When backing up UGREEN NAS to an Rsync server, the destination can be connected and the corresponding files can be seen, but cannot be clicked

> **Article ID**: `634`  
> **Category**: `Application Guide > Sync & Backup > FAQ > When backing up UGREEN NAS to an Rsync server, the destination can be connected and the corresponding files can be seen, but cannot be clicked`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/634  

---

## **Problem Analysis**

* The folder on the Rsync server is encrypted.
* The folder on the Rsync server does not have read/write permissions.

## **Solution**

You need to enable read and write permissions for the folder on the Rsync server. Follow these steps:

1. Log in to your Rsync server.
2. Locate the folder you want to back up.
3. Set read and write permissions for this folder.
