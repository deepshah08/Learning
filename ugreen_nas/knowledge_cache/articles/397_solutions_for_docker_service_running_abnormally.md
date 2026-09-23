# Solutions for Docker Service Running Abnormally

> **Article ID**: `397`  
> **Category**: `Application Guide > Docker > FAQ > Solutions for Docker Service Running Abnormally`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/397  

---

## Applicability

**Applicable Version**: NAS Firmware 1.18.0.0032 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Problem Description

After enabling Docker, the running status displays "**Docker service is running abnormally**." Try to uninstall and reinstall the Docker application or restart the device have failed to resolve the issue, preventing normal usage.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20260810/dffdb613-657e-4578-9813-0c8251b98340.png)

## Solution

To address this problem, you need to connect to the device's terminal via SSH and execute the install.sh script located in the com.ugreen.dockerdirectory with root privileges to restore the Docker service. Follow these detailed steps:

### Enable SSH Service

1.Go to the "**Terminal**" settings in the "**Control Panel**" of UGOS Pro.

2.Check the box to enable SSH service and set the allowed port (default is 22).

### Connect to NAS via SSH

**For Windows**:

1. Ensure your UGREEN NAS and Windows device are on the same local network.

2. Press Win + R, type CMD, and press Enter to open Command Prompt.

3. Enter the following command to connect to your UGREEN NAS via SSH:

```
ssh username@NAS_IP -p port
For example
ssh ugreen@192.168.31.34 -p 22
```

username: Replace with your administrator account.

NAS\_IP: Replace with the IP address of the UGREEN NAS. You can find the UGREEN NAS IP address under "**Control Panel**" > "**Network**" > "**Network Connection**" (such as LAN1 or LAN2).

port: Replace with the SSH service port number.

4. Enter the administrator password to complete the login.

**For macOS**:

1. Ensure your UGREEN NAS and macOS device are on the same local network.

2. Open the "**Terminal**" application found in the "**Utilities**" subfolder within the "**Applications**" folder.

3. Enter the following command to connect to the UGREEN NAS via SSH:

```
ssh username@NAS_IP -p port
For example
ssh ugreen@192.168.31.34 -p 22
```

username: Replace with your administrator account.

NAS\_IP: Replace with the IP address of the UGREEN NAS. You can find the UGREEN NAS IP address under "**Control Panel**" > "**Network**" > "**Network Connection**" (such as LAN1 or LAN2).

port: Replace with the port number for the SSH service.

4. Enter your administrator password to complete the login.

### Switch to Root Privileges

1. After logging in, we need to switch to root privileges.

2. Enter the following command in the terminal:

```
sudo -i
```

3. Enter the administrator password for verification. Once successfully verified, you will switch to root privileges.

### Perform the recovery operation

1. Go to the installation directory of Docker. You can check the installation directory of Docker through the NAS's App Center. Typically, the installation directory corresponds to the path /volumeX/@appstore/com.ugreen.docker, where X represents the storage volume number.

2. Take storage volume 1 as an example, enter the following command to switch to the corresponding directory:

```
cd /volume1/@appstore/com.ugreen.docker
```

3. Execute the install.sh script in this directory to restore the Docker service:

```
./install.sh
```

4. After the script execution is complete, the Docker service should be restored to normal.
