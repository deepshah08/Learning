# How to Change and Manage Passwords?

> **Article ID**: `773`  
> **Category**: `Application Guide > UGOS Pro > How to Change and Manage Passwords?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/773  

---

## Applicability

**Applicable client**:UGREEN NAS desktop client (Windows/macOS)

**Applicable version**: NAS firmware 1.16.0.0042 and later

This document is for reference only. The actual interface and operation paths may vary slightly due to system or app version updates. Please refer to the actual interface.

## Overview

This article applies to daily password security maintenance for UGREEN NAS, administrator permission management for multiple users, and emergency recovery when a password is forgotten.

## Change Login Password

Any user with login access can change their account password from the account settings page in "**Me**":

1. Log in to the UGREEN NAS desktop, then click "**Me**" in the upper-right corner of the top bar.

2. In the drop-down menu, click the **username** to go to the "**Account setting**" page.

![](https://file-us.ugreennas.com/admin/article/2026-06-02/66dfd4f42c864db8ab644ac440b3b4b1.webp)

3. Select "**Local Account**" in the left sidebar, then click "**Change password**" on the right.

![](https://file-us.ugreennas.com/admin/article/2026-06-02/f10b76c2b92f4362a116470cc542db74.webp)

4. In the verification window, enter the current login password and click "**Next**".

5. After verification is complete, enter and confirm the new password, then click "**Confirm**" to apply the change.

![](https://file-us.ugreennas.com/admin/article/2026-06-02/ae1eef4beb2f4592bdc039c61c53b152.webp)

## Administrator Password Management

Device administrators can manage passwords and permissions for all users.

### Force Reset Another User's Password

If a family member or company employee forgets their login password, an administrator can reset it for them:

1. Open "**Control Panel**" and click "**User Management**".

2. In the user list, find the target user and double-click the username. Alternatively, click "**···**" on the right and select "**Edit**" to open the user editing page.

![](https://file-us.ugreennas.com/admin/article/2026-06-02/47cccd73fab042f7b4bf894209150cad.webp)

3. On the "**Basic info**" tab, find the "**Password**" section and click "**Change password**" on the right.

![](https://file-us.ugreennas.com/admin/article/2026-06-02/a8207f9c3757462691e90da4c901043e.webp)

4. In the pop-up window, enter a new password and click "**Confirm**". The user's old password is not required.

After the password is reset, the user can log in again with the new password.

### Revoke Password Change Permission for Standard Users

For standard user accounts intended for shared use, administrators can prevent users from changing the password:

1. In "**User Management**", double-click the target user to open the user editing page.

2. On the "**Basic info**" tab, select "**This user is not allowed to change the password**", then click "**Save**".

Once this option is enabled, the standard user will no longer be able to change the password from their own account settings.

![](https://file-us.ugreennas.com/admin/article/2026-06-02/7561f7c2faa44a138e0355342bd39528.webp)

## What to Do If the Password Is Forgotten

### Scenario 1: A Standard User Forgets the Password

If a standard user forgets the account password, **contact the administrator of the NAS device**. The administrator can reset the password in the background by following the steps in "**Administrator Password Management**" above.

### Scenario 2: An Administrator Forgets the Password

If the device has only one administrator and the administrator password is completely forgotten, it can be reset using the physical `Reset` button on the back of the device:

1. Make sure the NAS is powered on and running normally.

2. Locate the `Reset` pinhole on the device. Use a SIM ejector pin or a similar tool to press and hold the button for about **5 seconds**.

3. **When the device buzzer makes one short beep, release the button immediately.**

4. The system network configuration and administrator password will now be reset.

5. Reconnect to the device, log in with the default account **admin** and leave the password field blank. Then follow the on-screen guide to set a new password.

**Note:** The Reset button is highly sensitive to how long it is pressed. Follow the rule strictly: release the button immediately after hearing **one beep**.

● **Press and hold for 5 seconds, until one beep is heard:** Only the network settings and login password are reset.

● **Continue holding for 8–10 seconds, until three consecutive beeps are heard:** The device will restart automatically and all system settings will be cleared and reset. This will not delete files stored on the hard drives, but all system configurations will be erased. Use this option with caution.
