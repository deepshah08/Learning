# [FAQ] NFS Mounting Prompts "'mount' Is Not Recognized as an Internal or External Command, Operable Program or Batch File"

> **Article ID**: `426`  
> **Category**: `Application Guide > Control Panel > FAQ > [FAQ] NFS Mounting Prompts "'mount' Is Not Recognized as an Internal or External Command, Operable Program or Batch File"`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/426  

---

## Problem Description

When attempting to mount a UGOS Pro folder using the NFS protocol in the Windows system, such as when executing the following command:

```
mount -o anon \\192.168.22.153\volume3\media N:
```

The system returns an error message:

```
'mount' is not recognized as an internal or external command, operable program or batch file.
```

## Solution

This error message indicates that the `mount` command is not recognized as an executable command in the Windows system. Common causes of this issue are as follows:

### Differences in Windows Versions and Components

Different editions of Windows 11 (such as Home, Professional, or Enterprise) have varying levels of support for NFS, and not all versions have the NFS client installed by default. If the NFS client is not installed, the system will not recognize the `mount` command.

#### Steps:

1. Open "Control Panel."

2. Click on "Programs and Features," and select "Turn Windows features on or off."

3. Check "Services for NFS" and "Client for NFS".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250903/ed5a59c4-633c-43d1-a619-44a743306d51.png)

4. After the installation is complete, restart the system.

After installing the NFS client, you can use the `mount` command to mount NFS shares. For example:

```
mount -o anon \\192.168.22.153\volume3\media N:
```

Alternatively, you can also mount the NFS share via the `net use` command:

```
net use N: \\192.168.22.153\volume3\media
```

### NFS Service Not Enabled or Improperly Configured

Even if the NFS client is installed, if the NFS service is not enabled or is incorrectly configured, you may still be unable to use NFS shares normally.

#### Steps:

1. Press `Win + R`, type `services.msc`, and open the "Services" window.

2. Locate and ensure that the **Client for NFS** service is running.

### **Additional Information:**

#### **Using** `net use` **as an alternative to** `mount`**:**

In some cases, if the `mount` command is not available or fails to install, you might consider using the `net use` command to mount a network drive. `net use`is more widely compatible with different network protocols, including SMB and NFS.

```
net use N: \\192.168.22.153\volume3\media
```
