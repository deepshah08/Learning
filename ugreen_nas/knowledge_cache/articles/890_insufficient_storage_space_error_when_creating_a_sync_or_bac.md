# Insufficient Storage Space Error When Creating a Sync or Backup Task on PC

> **Article ID**: `890`  
> **Category**: `Application Guide > Sync & Backup > FAQ > Insufficient Storage Space Error When Creating a Sync or Backup Task on PC`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/890  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS).

**Applicable Version**: NAS Firmware 1.17.0.0034 or later.

The descriptions in this document are for reference only. The actual interface and operation paths may vary slightly depending on your system or application version. Please refer to the actual interface.

## Issue Description

After creating a PC sync or backup task, you may see one of the following messages when the task runs:

● **Insufficient storage space on UGREEN NAS or your PC.**

● **Insufficient storage space on your PC or NAS.**

These messages usually indicate that there is not enough available storage space on either the PC or the NAS. As a result, the task cannot continue writing files or generating the required cache.

## Cause

This issue may be caused by one of the following:

● The folder or storage space associated with the task on the NAS does not have enough available capacity.

● There is not enough free space on the C: drive of your Windows PC.

● There is not enough available storage space on your Mac.

● The drive where the task directory is located does not have enough available space.

● The available storage space on the sync or backup destination is smaller than the size of the files to be written.

For Windows PCs, **make sure the free space on the C: drive is greater than 1% of its total capacity**. For Macs, make sure **the available storage space is greater than 1% of the total storage capacity.**

For example, if your Mac has a total storage capacity of 500 GB, it is recommended to keep more than 5 GB of available storage space.

## Solution

### Check the NAS Storage Space

First, check whether the folder or storage space associated with the task on the NAS has enough available capacity.

If there is not enough available storage space on the NAS, delete unnecessary files or switch to a storage space with more available capacity, and then run the task again.

### Check the Storage Space on Your Windows PC

If you are using a Windows PC, check the following:

● Make sure the free space on the Windows C drive is greater than 1**%** of its total capacity.

● Make sure the drive where the sync or backup task directory is located has enough available space.

● Make sure the drive where the sync or backup task directory is located has enough available space.

If there is not enough available space, free up space on the Windows C drive or the drive where the task directory is located, and then run the task again.

### Check the Storage Space on Your Mac

If you are using a Mac, make sure the available storage space is greater than 1**%** of the total storage capacity.

If you are using a Mac, make sure the available storage space is greater than 1**%** of the total storage capacity.

If you are using a Mac, make sure the available storage space is greater than 1**%** of the total storage capacity.

### Run the Task Again

After freeing up storage space, return to the UGREEN NAS PC Client and run the sync or backup task again.

If the task still reports insufficient storage space, make sure that both the source and destination have enough available space. For two-way sync tasks, available space is required on both sides to prevent file write failures.

## Still Need Help

If the issue persists after confirming that both your PC and NAS have enough available storage space, contact UGREEN Technical Support for further assistance.

When contacting support, it is recommended to provide the following information:

● Your computer operating system and version.

● The version of the UGREEN NAS PC Client.

● Your NAS model and firmware version.

● A screenshot of the error message.

● The task type (sync task or backup task).

● The available space on the drive where the task directory is located on your PC.

● The available capacity of the storage space where the task directory is located on the NAS.
