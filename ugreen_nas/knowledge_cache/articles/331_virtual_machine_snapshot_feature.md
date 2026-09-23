# Virtual Machine Snapshot Feature

> **Article ID**: `331`  
> **Category**: `Application Guide > Virtual Machine > Virtual Machine Snapshot Feature`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/331  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client, Web Browser

**Applicable Version**: UGOS Pro 1.18.1.0098 or later

The screenshots in this document are for reference only. The actual interface may vary slightly depending on the system or app version, please refer to the actual interface displayed.

## Introduction

Virtual Machine snapshot record the current state of a virtual machine. Before modifying important configurations or when you need to preserve a recoverable state, you can create a snapshot for the virtual machine. After a snapshot is created, you can restore the virtual machine to the corresponding state when needed.

## Create a Virtual Machine Snapshot

1. Open the Virtual Machine app and find the target virtual machine in the virtual machine list.

2. Click "**···**"on the right side > "**Create snapshot**", and wait for the system to complete the snapshot creation.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/203aa47a809548c79e42d7f9104ea938.webp)

After the snapshot is created, the system will record the current state of the virtual machine.

## View Snapshot List

1. In the virtual machine list, click the target virtual machine. The virtual machine details panel will be displayed on the right side of the page.

2. Switch to the "**Snapshot**" tab to view the list of snapshots created for the virtual machine.

![](https://file-us.ugreennas.com/admin/article/2026-08-07/0cfc0395c36b4a6ba2abc2a89dbfcc7e.webp)

## Restore to a Specific Snapshot

1. Go to the "**Snapshot**" tab of the target virtual machine and find the desired snapshot.

2. Click "**Restore**" next to the target snapshot, and confirm the operation as prompted.

After restoration, the virtual machine will return to the state recorded by the snapshot.

## Edit or Delete Snapshots

Find the target snapshot in the snapshot list, click "**···**"on the right side, and select the required option:

● **Edit description**: Modify the snapshot description.

● **Delete**: Delete the current snapshot.

## Notes

● Restoring a snapshot will roll back the virtual machine to the state when the snapshot was created. Before restoring, confirm whether the current data needs to be retained.

● After a snapshot is deleted, the virtual machine cannot be restored using that snapshot.

● Creating and restoring snapshots consume storage space. It is recommended to regularly delete snapshots that are no longer needed.

● Page names and feature entry points may vary slightly depending on the system version. Please refer to the actual interface display.
