# How to Connect to UGOS Pro via SSH with Root Privileges?

> **Article ID**: `481`  
> **Category**: `Application Guide > Control Panel > FAQ > How to Connect to UGOS Pro via SSH with Root Privileges?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/481  

---

## Applicability

**Applicable Clients**: UGREEN NAS PC Client (Windows/macOS), Web Browser  
**Applicable Version**: UGOS Pro firmware 1.19.1.0126 or later  
The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

**SSH** is an encrypted remote login protocol used to securely connect to and manage UGOS Pro over untrusted networks. Administrators can log in to UGOS Pro via SSH with root privileges. Enabling the SSH service may introduce security risks, so it is recommended to enable it only when necessary and avoid making unnecessary changes to system configurations.

**Key Uses:**

● Remotely access the underlying UGOS Pro system to execute commands, run scripts, and configure services.

● View system logs and troubleshoot services.

● Provide secure file transfer via SFTP.

● Encrypt data in transit to help prevent account credentials from being exposed.

**Note**: Once SSH is enabled, make sure that only administrators use root privileges for SSH login to prevent unauthorized access. It is recommended to disable SSH when it is not needed.

## Enable SSH Service

1. Log in to the UGOS Pro system and go to "**Control Panel**"**>**"**Terminal**".

2. Check "**Enable**" for the SSH service.

![](https://file-us.ugreennas.com/admin/article/2026-09-10/3ae9b3ff123048a889828fc2975c89bb.webp)

3. Specify the SSH port number (default is 22). You can also customize the SSH port and configure additional advanced settings:

● Set an automatic SSH shutdown time.

● Configure encryption algorithms (keep the default settings unless otherwise required).

● Set access restrictions (such as allowing LAN access only).

● Choose whether to enable the SFTP service.

4. Click "**Apply**" to make the settings take effect.

**Note**: To enhance SSH connection security, it is recommended to change the default port number and avoid exposing it directly to the public network, reducing the risk of attacks.

## Connect to UGOS Pro via SSH on Windows

1. Make sure the NAS and Windows PC are on the same LAN.

2. Launch the terminal application on Windows: Press `Win + R` to open "**Run**", enter `PowerShell`, then click "**Confirm**" to open Windows PowerShell.

![](https://file-us.ugreennas.com/admin/article/2026-09-10/83ae41ac194a410ba8a8e2f489e2a585.webp)

3. **Enter** the command in the following format (ssh username@NAS\_IP -p port) and press **Enter**.

Replace username with your administrator account, NAS\_IP with your NAS IP address, and port with your SSH port number.

```
ssh username@NAS_IP -p port
For example
ssh ugreen@192.168.31.34 -p 22
```

4. Enter the password for your UGOS Pro administrator account and press **Enter** to complete the login verification.

5. After successfully logging in, enter the `sudo -i` command and press **Enter** to obtain root privileges.

6. The system will prompt you to enter the administrator password again. Enter the password and press **Enter**. You will then be logged in to UGOS Pro with root privileges.

![](https://file-us.ugreennas.com/admin/article/2026-09-10/b27cc1d24de44421b2b992ee7bd5f028.webp)

## Connect to UGOS Pro via SSH on macOS

1. Make sure the NAS and macOS device are on the same LAN.

2. Open the "**Terminal**" app (located in the "Applications > Utilities" folder).

3. Enter the following command in Terminal and press **Enter**.

Replace username with your administrator account, NAS\_IP with your NAS IP address, and port with your SSH port number.

```
ssh username@NAS_IP -p port
For example
ssh ugreen@192.168.31.34 -p 22
```

4. Enter the password for your UGOS Pro administrator account and press **Enter** to complete the login verification.

5. After successfully logging in, enter the `sudo -i` command and press **Enter** to obtain root privileges.

6. The system will prompt you to enter the administrator password again. Enter the password and press **Enter**. You will then be logged in to UGOS Pro with root privileges.

## Notes

SSH operations may affect the system. To help ensure system security and stability, follow these important guidelines:

1. SSH operations involve changes to the underlying system and may affect system stability and security. Make sure you fully understand the commands you execute.

2. Beginners are advised to perform SSH operations under the guidance of technical personnel. Technical support cannot provide solutions for issues caused by individual SSH operations.

3. Always back up important data before performing any SSH operations to prevent accidental data loss.

4. If individual SSH operations cause abnormal issues (such as system crashes or device failures) that require factory reflashing or repairs, you will be responsible for the related costs.

5. When using Terminal, it is recommended to enable "**Auto Block**" to help prevent brute-force attacks. For details, see "[Security](https://support.ugnas.com/knowledgecenter/detail/article/en-US/225) ".

6. If you encounter problems after SSH operations, try the following steps:

● **Restart the system**: Some temporary issues can be resolved by restarting the system.

● **Restore from backup**: If a backup is available, try restoring to a previous state (such as service configuration files, system configuration files, or related data files).

● **Factory reset**: If the issue persists but you can still access the system, try performing a factory reset. The system will be restored to its factory default state. User accounts, system configurations, installed apps, and other settings will be cleared, while data on the hard drives will be retained.
