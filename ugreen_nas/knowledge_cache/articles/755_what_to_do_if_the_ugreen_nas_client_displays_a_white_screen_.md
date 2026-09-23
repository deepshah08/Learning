# What to Do If the UGREEN NAS Client Displays a White Screen or Flickers?

> **Article ID**: `755`  
> **Category**: `Troubleshooting > System and Software Failure > What to Do If the UGREEN NAS Client Displays a White Screen or Flickers?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/755  

---

## Scope of Application

● Applicable to the UGREEN NAS Client (PC) for Windows systems.

● Applicable when the client interface displays a white screen, flickers, or fails to load properly while uploading or downloading files to or from a UGREEN NAS.

## White Screen or Flickering When the Client Runs in the Background

Some users may experience a **white screen** or **flickering issue** when reopening the UGREEN NAS Client after closing its window during file upload or download tasks (while it continues running in the background). This issue prevents normal client operation.

### Cause Analysis

After investigation, most cases of white screen or flickering are related to the **AstrillVPN** dynamic library (`ASProxy64.dll`) .

When the UGREEN NAS Client performs upload or download tasks, the data stream passes through this library. If the library encounters an exception during operation, it may cause the client interface to render incorrectly or flicker.

If a white screen or flickering issue occurs, check **AstrillVPN** first. If AstrillVPN is not installed, check **Windows Defender Firewall**, **system proxy**, and **Smart App Control** configurations in order.

After clearing the cache or repairing system component libraries, most white screen issues can be resolved.

### Solution 1: Uninstall the AstrillVPN LSP Module

If AstrillVPN is installed on your computer, please follow the steps below:

1. Run the **AstrillVPN** application.

2. Hold down the **Ctrl** key and click the **three-dot menu** in the upper-left corner of the AstrillVPN client.

3. Go to **"HELP" > "LSP Uninstall"**.

4. After completing the process, close the AstrillVPN client.

5. Restart your computer.

After performing the above steps, the UGREEN NAS Client should function normally, and the white screen or flickering issue will no longer occur.

### Solution 2: General Windows System Repair Methods

If you are not using AstrillVPN, or if uninstalling it does not resolve the issue, please try the following methods:

**Reinstall the Application:**  
Uninstall the current UGREEN NAS Client, and try reinstalling it to a different drive (for example, install the program on Drive C instead of Drive D).

**Check Firewall Settings:**

1. Open "**Control Panel" > "Windows Defender Firewall"**.

![](https://file-us.ugreennas.com/admin/article/2026-04-30/77ffe055a6724ea7b7b49e79c0a21481.webp)

2. Click "**Allow an app or feature through Windows Defender Firewall"**.

![](https://file-us.ugreennas.com/admin/article/2026-04-30/37e7008ede0f4fcba9be0f01f8113852.webp)

3. Add the UGREEN NAS Client, and check both "**Private**" and "**Public**" networks.

![](https://file-us.ugreennas.com/admin/article/2026-04-30/322467338e014b5d83a956ea4d7a9ec9.webp)

4. If the issue persists, you may temporarily disable the firewall for testing. Open **Command Prompt** as an administrator, then enter the following command in command prompt and press Enter

```
netsh advfirewall set allprofiles state off
```

**Turn Off Smart App Control (Windows 11 only):**

If you are using Windows 11, open Windows Security, then go to **"App & browser control" > "Smart App Control"**. Select **"Off"**, restart your computer, and reinstall the UGREEN NAS Client after reboot.

![](https://file-us.ugreennas.com/admin/article/2026-04-30/71decfc2639742a79f0e07a925f9b99d.webp)

**Repair System Component Libraries:**

1. Download and install the Microsoft VC++ Runtime Library ([download link](https://aka.ms/vs/17/release/vc_redist.x64.exe) ).

2. Run command prompt as administrator.

3. Enter the following command, then press Enter:

```
sfc /scannow
```

4. Wait for the system to scan and automatically repair any missing or corrupted system files.

![](https://file-us.ugreennas.com/admin/article/2026-04-30/42a0d502256141388cdb6e79bb0b648a.webp)

### Solution 3: "Connection Failed" Error Troubleshooting

When the client displays the message: "**Connection failed. Please check the network settings of your computer or NAS.**"

Please check the following items in order:

1. **Check VPN or Proxy:**

Make sure that any VPN or proxy applications on your computer are completely closed — Do not just close the application interface—make sure all related background services are fully stopped.

Open the VPN settings and disable "**Launch at Windows startup**".

If a proxy starts automatically with the system, it may modify environment variables, causing network connection errors.

2. **Allow the Application Through the Firewall:**

Open Windows Defender Firewall, and click **"Allow an app or feature through Windows Defender Firewall"**.

Add the UGREEN NAS Client, and check both "**Private**" and "**Public**" networks.

![](https://file-us.ugreennas.com/admin/article/2026-04-30/388cbc2b77c84ff6851d8f2a2e852aff.webp)

3. **Clear Client Cache:**

Close the UGREEN NAS Client. Press Win + R, then enter `%appdata%` and press Enter.

Locate the following two folders and rename each (for example, add `_1` at the end of the folder name).

Reopen the UGREEN NAS Client and try logging in again.

![](https://file-us.ugreennas.com/admin/article/2026-04-30/628a2e7c8991478dbc8b7e878ee3b71d.webp)

4. **Delete System Proxy Environment Variables:**

If "Connection Failed" still appears after closing the VPN, open "**System Properties**", click "**Advanced"** **>** "**Environment Variables"**.

![](https://file-us.ugreennas.com/admin/article/2026-04-30/b93c128282de428395a7b2d8002c0b4e.webp)

Check for the following proxy entries: `http_proxy` or `https_proxy`

If they exist, delete both items, click "**OK"**, then restart your computer. After restarting, try opening the client again.

![](https://file-us.ugreennas.com/admin/article/2026-04-30/d0093a1fc57a4fde846773d7eba537a9.webp)

## White Screen After Overwriting Installation

Some users may experience a white screen after installation, when they upgraded by installing a new version over the old client.

### Cause Analysis

If user's computer's system time is incorrect, it can cause certificate validation errors. This may result in the client interface displaying a white screen.

### Solution

● **Windows system (taking Windows 11 as an example)**: Open "**Settings**." Then go to "**Time & language**" > "**Date & time**," and enable "**Set time zone automatically**."

![](https://file-us.ugreennas.com/admin/article/2026-04-30/2de18c480f7546daaeaa46da1602efc3.webp)

● **macOS system**: Open "**General**," then click "**Date & Time**," and enable "**Set date and time automatically**."

![](https://file-us.ugreennas.com/admin/article/2026-04-30/7d2e68f140284e75bb55978515394341.webp)

## White Screen After Opening Smart App Control

### Issue Description

On Windows system, if "**Smart App Control**" is enabled in Windows Security, it may cause the UGREEN NAS PC Client to be blocked by security policies when launching. As a result, the interface may remain white screen and fail to load content.

### Solution

You can temporarily disable this security feature to resolve the conflict. Follow these steps:

1. Open **Windows Security**, go to the "**App & browser control**" settings page, and turn off "**Smart App Control**."

![](https://file-us.ugreennas.com/admin/article/2026-04-30/bad9764d2aac401888cf84959072f248.webp)

2. After turning it off, reopen the UGREEN NAS PC Client. The interface should now render properly and display the login screen.

3. Once confirmed the client is no longer showing a white screen and is working normally, return to Windows Security and re-enable "**Smart App Control**."

**Note**: After completing the above steps, the system will usually establish the correct application trust cache. When you open the UGREEN NAS PC Client again in the future, the white screen issue should no longer occur.
