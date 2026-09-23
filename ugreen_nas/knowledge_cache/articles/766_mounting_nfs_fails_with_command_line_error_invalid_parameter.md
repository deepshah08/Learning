# Mounting NFS Fails with "Command Line Error. Invalid Parameter."

> **Article ID**: `766`  
> **Category**: `Application Guide > Control Panel > File Service > Mounting NFS Fails with "Command Line Error. Invalid Parameter."`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/766  

---

![](https://file-us.ugreennas.com/admin/article/2025-11-06/444c2a16523546dfaa50e1a11bebb9a0.webp)

If you encounter the message **"Command line error. Invalid parameter."** when mounting NFS, follow the steps below to troubleshoot the issue:

1. **Verify basic requirements**

Make sure all the following conditions are met:

● NFS service has been enabled on the NAS.

● The target folder in Files has been properly configured with NFS client permissions.

● The computer has the NFS client feature enabled.

● The computer and NAS are on the same local network, and the NAS IP address can be pinged successfully.

2. **Check the folder name**

If all the above conditions are met but the "Invalid parameter" error still appears, check whether the folder name contains spaces. If the path includes spaces, enclose the entire path in double quotation marks.

**Example:**

Incorrect example (space in path without quotes):

```
mount -o anon \172.17.70.69volume1Time Machine N:
```

Correct example (space in path with double quotes):

```
mount -o anon "\172.17.70.69volume1Time Machine" N:
```

After adding double quotes, the NFS directory can be mounted successfully.

![](https://file-us.ugreennas.com/admin/article/2025-11-06/605bf64b1e144d06abe237d52059cf2a.webp)
