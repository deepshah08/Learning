# How to Fix the "Service Error" Message When Creating a Local Sync or Backup Task?

> **Article ID**: `887`  
> **Category**: `Application Guide > Sync & Backup > FAQ > How to Fix the "Service Error" Message When Creating a Local Sync or Backup Task?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/887  

---

## Issue Description

When creating a local sync task or backup task on a computer, if the page displays "**Service Error**", this usually indicates that the local sync service did not start properly or that the syncSpace program cannot run normally.

## Possible Causes

This issue may be caused by any of the following:

● Antivirus or system security software has mistakenly blocked or quarantined the syncSpace process, preventing the service from starting.

● The syncSpace process is incompatible with the current version of Windows.

● Required Microsoft runtime libraries are missing from the computer.

● Critical syncSpace files are corrupted, preventing the process from starting.

● The syncSpace process is running but cannot be accessed properly by the system.

The Windows computer must be running **Windows 7 SP1 or later**.

## Solution

Try the following:

1. Check whether antivirus or system security software has blocked or quarantined The syncSpace process.

2. Confirm that the current Windows version meets the system requirements.

3. Check whether the required Microsoft runtime libraries are installed.

4. Reopen the UGREEN NAS desktop client, then create the sync or backup task again.

If "**Service Error**" still appears, contact UGREEN NAS technical support for further assistance.

When submitting feedback, provide the following information:

● Computer operating system version

● UGREEN NAS desktop client version

● Screenshot of the error page

● Whether any third-party antivirus software is installed

● Whether the task being created is a sync task or a backup task
