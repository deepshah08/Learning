# Introduction and User Guide for UGREEN NAS System's Breakpoint Resume Function

> **Article ID**: `606`  
> **Category**: `Application Guide > UGOS Pro > Introduction and User Guide for UGREEN NAS System's Breakpoint Resume Function`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/606  

---

Breakpoint resume refers to the ability of the system to automatically or manually resume a file transfer task from the point it was interrupted due to reasons like network failure or device power-off. This prevents the retransmission of the already completed parts, thus improving efficiency. Currently, the UGOS Pro system supports breakpoint resume functionality for file copy and move tasks.

**Supported Versions:** Firmware version 1.2.0.2121 and above

## How to View and Resume Tasks

If a file copy or move task is interrupted, you can view and resume the task by following these steps:

**1. Access the Task Center**

After logging in, go to the [Task Center.] On this page, you can see the currently running copy or move tasks, as well as any failed files. The Task Center will display detailed error messages to help you understand why the task was interrupted.

![](https://file-us.ugreennas.com/admin/article/2025-08-27/d8935f33b3164f7b9aa048f753d73d38.webp)

**2. Find the Interrupted Task**

If a task fails, you can restart the task and continue the transfer based on the error message. Different types of interruptions may have different recovery methods:

**Scenario 1: Network Interruption or Computer Shutdown**  
If a network interruption or computer shutdown occurs during file transfer, once the network is restored, the system will automatically resume the task and continue transferring the file from where it was interrupted, without requiring any user intervention.

![](https://file-us.ugreennas.com/admin/article/2025-08-27/619d96b0031942f6a735b2bc6d4daff0.webp)

**Scenario 2: NAS Power Off or Firmware Upgrade**

If the NAS experiences a power loss or a firmware upgrade causes a restart, the system will retain the current task state. Once the NAS restarts, you will need to manually resume the interrupted task by entering the Task Center. You can click the “Continue” button in the Task Center, and the task progress will resume from the interruption point.

**Note:** SMB and local file transfers support breakpoint resume functionality, so if an interruption occurs, the transfer will resume from the point where it was interrupted.For other file services, if the NAS experiences a power loss or firmware upgrade during the transfer, the task progress will restart from 0%.
