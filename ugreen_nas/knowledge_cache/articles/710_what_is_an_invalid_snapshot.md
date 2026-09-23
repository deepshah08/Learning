# What is an invalid snapshot?

> **Article ID**: `710`  
> **Category**: `Application Guide > Snapshot > What is an invalid snapshot?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/710  

---

**Invalid Snapshots** refer to snapshots that have become disconnected from their original data paths due to changes in system environment or device status. While these snapshots still occupy storage space within the system, they can no longer be directly used for file restoration through conventional methods.

![](https://file-us.ugreennas.com/admin/article/2025-06-26/e68c0827a7cb4f898a5a068cbc899e38.webp)

# Common Scenarios of Snapshot Failure

1. **Reset****：**When a user resets the UGREEN NAS device to factory settings (initial state), all previously configured options (including snapshots) will be deleted, causing snapshots of user folders to become invalid.

2. **Hard Drive Transfer or Format Conversion****：**If the hard drives from a UGREEN NAS (e.g., DXP4800) are moved to another device (e.g., DXP6800) and configured as internal storage, the original snapshots of user folders will become invalid.

3. **Leaving a Domain (AD Domain)**: If a user exits an Active Directory (AD) domain, even if the domain user data is retained upon leaving, the snapshots associated with those user folders will become invalid.

# Solutions

Although these invalid snapshots still retain restore capabilities, they occupy storage space. Therefore, unnecessary snapshots can be cleaned up using the snapshot management interface.

● Before cleaning up, it is recommended to review the specific contents of these invalid snapshots to determine which ones are valuable and worth keeping.

● If there are important files within the invalid snapshots, you may contact our technical support team to obtain a list of these files and attempt recovery.
