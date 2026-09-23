# What Should I Do If Docker Container Cannot Access a Mapped Folder or Shows a Permission Denied Error?

> **Article ID**: `356`  
> **Category**: `Application Guide > Docker > FAQ > What Should I Do If Docker Container Cannot Access a Mapped Folder or Shows a Permission Denied Error?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/356  

---

## Applicability

**Applicable Version**: UGOS Pro firmware 1.19.0.0093 or later

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## Problem Description

When a Docker container is running, if it cannot access the mapped folders or files on UGOS Pro, issues such as download failures, task errors, or unexpected container stops may occur. The container logs may display the following error messages:

```
Permission denied
File error alert
```

If you see similar errors, it usually indicates that the container does not have sufficient permissions to access the mapped directory.

## Cause Analysis

This issue is usually related to permissions for the directory mounted to the container. If you use a manually created directory as the container mount path, the directory may not have sufficient read and write permissions, preventing the container from accessing files or writing data.

After Docker is installed, the system automatically creates a shared folder named **docker** under Shared Folder in the "**Files**" app.  
This folder has the permissions required for most container read and write operations by default.

## Solution 1: Use the Automatically Created Docker Shared Folder

We recommend using the system-generated **docker** shared folder as the container mount path.

1. Open "**Files**" and find the system-generated **docker** shared folder.

2. Create or select the folder you want to use for the container under the **docker** directory.

3. In the container settings, set this folder as the mount path.

4. Save the settings and restart the container.

After switching to the **docker** shared folder, the container should normally be able to access the mapped folders and files.

## Solution 2: Adjust Permissions for a Manually Created Directory

If you need to use a manually created directory, make sure it has sufficient access permissions. You can sign in to the NAS via SSH and run the following command to adjust the directory permissions:

```
chmod -R 777 /path/to/your/manual/directory
```

Replace the path in the command with the actual directory path.

```
chmod -R 777 /volume1/your-folder
```

This command recursively changes the permissions of the target directory, its subdirectories, and files to allow read, write, and execute access.

## Notes

● We recommend using the system-generated **docker** shared folder whenever possible to avoid permission issues.

● Before manually modifying directory permissions, make sure the path is correct to avoid accidentally changing other important directories.

● `chmod -R 777` grants read/write, and action permission to the target directory. It is recommended to use this command only for trusted directories.

● If the issue persists after modifying permissions, check the Docker logs to confirm whether permission errors such as `Permission denied` still exist.。
