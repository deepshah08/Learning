# Frequently Asked Questions (FAQ) About Snapshots

> **Article ID**: `713`  
> **Category**: `Application Guide > Snapshot > Frequently Asked Questions (FAQ) About Snapshots`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/713  

---

### **Q: If the snapshot schedule is set to run on the 31st of each month, will it skip when the current month doesn't have a 31st day?**

**A：**

When the current month has no 31st day, **the snapshot schedule will skip execution for that month**. For example, if a month only has 30 or fewer days, the system will not attempt to execute the snapshot plan for the 31st.

### **Q：Can snapshots be taken for a specific subfolder within a user folder?**

**A：**

Currently, **snapshots only support operations on entire user folders** and do not allow snapshotting individual subfolders or files.

**Shared folders and user folders are at the same hierarchical level**, meaning you can only take snapshots of entire folders rather than specific subfolders or files.

### **Q：If I'm in the middle of cutting or moving files when a scheduled snapshot triggers, will the snapshot be skipped?**

**A：**

The snapshot will proceed as scheduled, **but the captured data may be incomplete**. Since files are being modified during cut/move operations, **files in transition may not be fully recorded in the snapshot**. This could result in partial data loss or unrecoverable files. We recommend avoiding major file operations during scheduled snapshot times or manually pausing the snapshot schedule.

**Note:** During file transfers or cuts, incomplete operations may prevent snapshots from capturing the latest file states, potentially leading to data loss.
