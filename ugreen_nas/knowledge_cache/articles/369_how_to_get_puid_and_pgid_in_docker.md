# How to Get PUID and PGID in Docker?

> **Article ID**: `369`  
> **Category**: `Application Guide > Docker > FAQ > How to Get PUID and PGID in Docker?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/369  

---

## Applicability

**Applicable Version**: UGOS Pro Firmware 1.18.1.0098 or later

The screenshots in this document are for reference only. The actual interface may vary slightly depending on the system or app version, please refer to the actual interface displayed.

## Introduction

When deploying containers with Docker, you may need to enter PUID and PGID. PUID and PGID specify which user and user group the application inside the container runs as.

After proper configuration, the container can access NAS folders with the corresponding user permissions, preventing issues such as files being inaccessible, unable to be written, or insufficient permissions.

## What Are PUID and PGID?

**PUID** is the user ID used to identify a specific user in the system. **PGID** is the group ID used to identify a specific user group in the system.

In Docker containers, applications may need to read and write files in mapped NAS folders. By configuring PUID and PGID, the container can access these folders with the specified user permissions.

## How Should Beginners Configure PUID and PGID?

If an image requires PUID and PGID but does not have special permission requirements, you can enter the following default values:

● PUID=1000

● PGID=1000

Some images can run properly with these default values. If the container still reports insufficient permissions, follow the steps below to obtain the actual PUID and PGID.

## How to Get PUID and PGID?

### Enable SSH

1. Log in to the UGREEN NAS system, open "**Control Panel**", and click "**Terminal**".

2. Find SSH and select "**Enable**".

3. Click "**Apply**" to save the settings.

### Log in to the NAS via SSH

Open an SSH client on the same LAN, such as Xshell or XTerminal, and enter the following connection information:

● Host: NAS LAN IP address

● Port: 22

● Username: Administrator account

● Password: Administrator account password

After logging in, enter sudo -i and press Enter. Enter the administrator password to complete verification and switch to root privileges.

### Check User UID and GID

Replace username in the following commands with the username you want to query.

● Check user UID and GID: id username

● Check UID only: id -u username

● Check GID only: id -g username

Enter id ugreen and press Enter. If the following result is returned:

uid=1000(ugreen) gid=1000(ugreen) groups=1000(ugreen)

This means that both PUID and PGID should be set to 1000.

## How to Configure PUID and PGID in Compose?

In Docker Compose, PUID and PGID need to be added as environment variables under environment. For example:

```
services:
 app:
 image: your-image:latest
 container_name: your-container
 environment:
 - PUID=1000
 - PGID=1000
 - TZ=Asia/Shanghai
 volumes:
 - ./config:/config
 - /volume1/media:/media
 restart: unless-stopped
```

If the queried UID and GID are not 1000, replace them with the actual values.

For example, if the query result is:

uid=1001(testuser) gid=100(users)

Configure the Compose file as follows:

environment:

● PUID=1001

● PGID=100

## Notes

● This configuration only takes effect when the image supports PUID and PGID parameters.

● Parameter names may vary between images. Refer to the official documentation of the image for details.

● PUID and PGID should match the permissions of the user who needs to access the mapped directory.

● If the container still reports Permission denied, check the permissions of the mapped directory itself.

● After modifying the Compose configuration, redeploy or restart the container for the changes to take effect.

● SSH operations require some technical knowledge. Make sure the commands and paths are correct before executing them.
