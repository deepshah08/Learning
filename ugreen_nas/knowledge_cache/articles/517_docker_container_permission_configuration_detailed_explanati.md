# Docker Container Permission Configuration Detailed Explanation

> **Article ID**: `517`  
> **Category**: `Application Guide > Docker > FAQ > Docker Container Permission Configuration Detailed Explanation`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/517  

---

In the usage of Docker containers, permission settings are a key factor in ensuring the security and functionality of the container. Docker provides a flexible permission control mechanism for containers through Linux Capabilities, allowing precise management of process permissions without granting full root access. This article will explain in detail the permission configuration options within Docker containers.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250428/14ecb3d6-f049-46f5-bba2-56fce818e62e.png)

## **Default Allowed Capabilities (Removable)**

The table below lists the Linux capabilities that Docker grants to containers by default. These capabilities are sufficient for most scenarios.

|  |  |
| --- | --- |
| Capability Key | Description |
| AUDIT\_WRITE | Allows writing to the kernel audit log. |
| CHOWN | Allows arbitrary changes to the UID and GID of files (see chown(2)). |
| DAC\_OVERRIDE | Bypasses file read, write, and execute permission checks. |
| FOWNER | Bypasses permission checks for operations that would normally require the process's filesystem UID to match the file's UID. |
| FSETID | Allows setting the effective user ID and group ID of a file. |
| KILL | Allows sending signals to processes. |
| MKNOD | Allows creating special files using mknod(2). |
| NET\_BIND\_SERVICE | Allows binding to ports lower than 1024. |
| NET\_RAW | Allows using RAW and PACKET sockets. |
| SETFCAP | Allows setting file capabilities. |
| SETGID | Allows setting the group ID of a process. |
| SETPCAP | Allows setting process capabilities. |
| SETUID | Allows setting the user ID of a process. |
| SYS\_CHROOT | Allows using chroot(2) to change the root directory. |

## **Capabilities Not Granted by Default (Can Be Added)**

The following are capabilities that are not granted by default but can be manually added as needed. These capabilities typically involve sensitive operations and should be enabled with caution.

|  |  |
| --- | --- |
| Capability Key | Description |
| AUDIT\_CONTROL | Enables and disables kernel auditing; changes audit filtering rules; retrieves audit status and filtering rules. |
| AUDIT\_READ | Allows reading audit logs through multicast netlink sockets. |
| BLOCK\_SUSPEND | Allows blocking the system from suspending. |
| BPF | Allows creating BPF maps, loading BPF Type Format (BTF) data, retrieving JIT code for BPF programs, etc. |
| CHECKPOINT\_RESTORE | Allows operations related to checkpointing and restoring (introduced in kernel 5.9). |
| DAC\_READ\_SEARCH | Bypasses file read permissions checks as well as directory read and execute permissions checks. |
| SYS\_ADMIN | Allows various system administration operations (e.g., mounting filesystems, setting up network interfaces). |
| SYS\_MODULE | Allows loading and unloading kernel modules. |
| SYS\_PTRACE | Allows using ptrace(2) to trace arbitrary processes. |

## **Notes**

1. **Permission Adjustment Should Be Done Cautiously:** Enabling too many permissions may lead to security risks. Grant permissions based on actual needs, minimizing them as much as possible.

2. **Permission Changes and Isolation:** Adjusting permissions can affect container isolation. Ensure to carefully verify configurations before applying them inside the container.

For more detailed explanations, please refer to the Docker official documentation: [Running containers | Docker Docs](https://docs.docker.com/engine/containers/run/#commands-and-arguments)
