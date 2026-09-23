# How to handle multiple conflict files generated during file sync or backup?

> **Article ID**: `635`  
> **Category**: `Application Guide > Sync & Backup > FAQ > How to handle multiple conflict files generated during file sync or backup?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/635  

---

## **Problem Analysis**

* The user might be editing the file while it is being synced.
* Multiple users may be editing the file at the same time.

## **Solution**

1. Go to the sync or backup task page, locate the corresponding task, and select [More] > [Edit] > [Sync Rules], then click "Advanced Settings".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250711/c41eb3d8-f099-4a17-8f96-63387503d836.png)

2. Switch to the [File Conflict] tab, and configure the "When file conflict occurs" option according to your needs.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250711/2d5fc730-51e7-49e6-a984-c5cc40650d40.png)

* **Keep new files and rename old ones:** Both versions will be retained. The old file will be renamed to "filename-conflict-xxx".
* **Replace old files with new files:** Only the latest file will be kept.
