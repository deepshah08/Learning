# Terminal

> **Article ID**: `84`  
> **Category**: `Application Guide > Control Panel > Terminal`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/84  

---

In the Terminal, you can enable and manage SSH and Telnet features. Below is an introduction to both:

# SSH Overview

**SSH** is an encrypted remote login protocol used to securely connect to and manage the NAS over an untrusted network. Compared to Telnet, SSH offers stronger security and is the recommended option.

**What can SSH do?**

● Remotely access the underlying NAS system to execute commands, run scripts, and configure services

● View system logs and debug services

● Provide secure file transfer via SFTP

● Encrypt data transmission to prevent credential leakage

## Enabling SSH Service

1. Open "**Control Panel**">"**Terminal**" settings, and check the box to "**Enable**" SSH.

2. It is recommended to change the default port number (e.g., change to 922) and set an auto-disable timeout for SSH.

3. In "**Advanced settings**", you can configure:

4. Encryption algorithms (it is recommended to keep the default settings unless specific requirements exist)

5. Access restrictions (e.g., allow access only from the local network)

6. Whether to enable SFTP service

7. Click "**Apply**" to save the settings.

![](https://file-us.ugreennas.com/admin/article/2025-12-22/eaab972b4399440c90e774aaba9a3f96.webp)

### About SSH Encryption Algorithms

The **High** and **Low** security levels provided by the Terminal (SSH service) on UGREEN NAS essentially reflect different restrictions on the encryption algorithm suites (cipher suites) allowed in the SSH configuration file (`sshd_config`).

To ensure secure data transmission, **it is strongly recommended to use the High level.** Switching to the **Low** level is only advised when you need to connect very old client devices.

For more details, please refer to [**SSH Encryption Algorithm Configuration Guide**](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmNzc0In0=) **.**

### About SFTP

SFTP is an encrypted file transfer protocol based on SSH. Once enabled, you can use clients such as WinSCP to connect to the NAS and manage files securely. SFTP is not compatible with FTP and does not support anonymous access.

### Connect to NAS via SSH from Windows

1. Make sure that both the Windows and the NAS are on the same local network.

2. Press `Win + R`, type `cmd`, and press Enter to open the Command Prompt.

3. Enter the following command format:

```
ssh username@NAS_IP_address -p port_number
```

Replace username with your administrator account. For example:

```
ssh ugreen@172.17.70.69 -p 922
```

4. Enter the administrator password to complete the connection.

You can find the NAS IP address in "**Control Panel**">"**Network**">"**Network connection**".

![](https://file-us.ugreennas.com/admin/article/2025-12-22/6daacbcf0f4f4461920b38b603b0e31a.webp)

### Connect to NAS via SSH from macOS

1. Make sure that your macOS device and the NAS are on the same local network.

2. Open the "**Terminal**" application (Path: Applications>Utilities).

3. Enter the same SSH command format as used on Windows:

```
ssh username@NAS_IP_address -p port_number
```

4. Enter the password to complete the login.

## Telnet Overview

Telnet is an early remote login protocol. While it is simple to use, it transmits data in plain text and poses security risks.

## Enabling Telnet Service

1. Open "**Control Panel**">"**Terminal**" settings.

2. Locate Telnet, check "**Enable**", then click "**Apply**" to save the settings.

![](https://file-us.ugreennas.com/admin/article/2025-12-22/281b97afaeda4ca6bddac6f940090060.webp)

### How to Use

**Telnet** is used in the same way as SSH on both Windows and macOS.

1. In the macOS Terminal or Windows Command Prompt, enter:

```
telnet NAS_IP
```

2. Enter the NAS username and password to complete the login.

### Connecting to the Telnet Service on Windows

To connect to the Telnet service on Windows, follow these steps:

● Press `Win + R` to open the "**Run**" dialog, type `cmd`, and press **Enter** to open the Command Prompt (run as administrator).

1. Enabling the Telnet client: enter the following command to enable the Telnet client feature:

```
dism /online /Enable-Feature /FeatureName:TelnetClient
```

2. Connecting to your NAS: In the Command Prompt, enter the following command to connect to your NAS device:

```
telnet <NAS_IP>
```

3. Replace <NAS\_IP>: Substitute`<NAS_IP>` with the IP address of your NAS (for example, `telnet 192.168.78.228`).

4. Log in: Enter the administrator username and password you set on the NAS to log in.

5. Use Telnet Commands: Once logged in, you can use the Telnet service just like a command-line interface to execute commands and manage the NAS.

### Connecting to the Telnet Service on macOS

To connect to the Telnet service on macOS, follow these steps:

1. Open the Terminal app: On macOS, you can open Terminal in the following ways:

● use Spotlight by pressing `Command (⌘) + Space`, type "**Terminal**"， and press Enter.

● open the "**Applications**" folder, navigate to "**Utilities**", and launch "**Terminal**".

2. Connect to your NAS: In the Terminal, type the following command to connect to your NAS via Telnet:

```
telnet <NAS_IP>
```

Replace `<NAS_IP>` with the IP address of your NAS.

3. Log in: Once connected, you will be prompted to enter your username and password. Input the credentials configured on your NAS to complete the login.

4. Use Telnet commands: After logging in, you can use the Telnet interface just like a command-line session to execute commands and manage your NAS.

If the Terminal reports that the Telnet command is not found, this may be because your macOS version no longer includes the Telnet client. In this case, it is recommended to use SSH instead.

## Security Tips

● It is recommended to enable the "**auto block**" feature in the Terminal settings to prevent brute-force attacks. For detailed instructions, please refer to the Block Management section of [Security](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmMjI1In0=) .

● Do not arbitrarily change SSH configurations (such as ports or forwarding) to avoid connection issues.

● Beginners are advised to operate SSH under the guidance of technical personnel. UGREEN does not provide technical support for SSH operations.
