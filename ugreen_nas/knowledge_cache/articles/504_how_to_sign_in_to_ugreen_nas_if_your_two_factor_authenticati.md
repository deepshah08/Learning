# How to Sign In to UGREEN NAS If Your Two-Factor Authentication (2FA) Key Is Lost?

> **Article ID**: `504`  
> **Category**: `Troubleshooting > System and Software Failure > How to Sign In to UGREEN NAS If Your Two-Factor Authentication (2FA) Key Is Lost?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/504  

---

## Applicability

**Applicable Version**: NAS Firmware 1.19.1.0126 or later

The descriptions in this document are for reference only. The interface may vary depending on system or app updates, please refer to the actual interface.

## Introduction

If your phone is lost, the OTP app is unavailable, or you are unable to obtain a two-factor authentication (2FA) verification code, you can use the methods in this guide to regain access to your UGREEN NAS system and disable 2FA.

After restoring access, it is recommended to link a new OTP app to keep your account secure.

## Method 1: Sign In to the NAS Using the Emergency Verification Email

If you set an emergency verification email address when enabling two-factor authentication, you can sign in using a verification code sent to that email address.

**Note**: The emergency verification email address must be set in advance when enabling two-factor authentication. If no emergency verification email address was set, this method cannot be used.

1. On the verification code screen, click "**Cannot be verified through OTP**". The system will send a verification code to the emergency verification email address you provided.

![](https://file-us.ugreennas.com/admin/article/2026-08-28/9e302d22334c462aa716923fcaea4ebc.webp)

2. Open the email, find the verification code, enter it on the sign-in screen, and complete verification to sign in.

![](https://file-us.ugreennas.com/admin/article/2026-08-28/814f160269014e378b65c86e11f0d1e9.webp)

3. After signing in, click "**Me**" in the upper-right corner of the desktop.

4. Click the username of the currently signed-in account to open the account settings page.

![](https://file-us.ugreennas.com/admin/article/2026-08-28/b2fd71a63d4f4db8b2f920a17ee4726a.webp)

5. On the "**Local Account**" page, find "**Two-factor authentication (2FA)**" and turn it off.

![](https://file-us.ugreennas.com/admin/article/2026-08-28/26f0236fe15e4bc082efae1a670e2932.webp)

6. Follow the on-screen instructions to enter your sign-in password for verification. Once verified, two-factor authentication will be disabled.

## Method 2: Sign In Using a Trusted Device and Disable Two-Factor Authentication

If you previously set a device as trusted, you can use that trusted device to sign in to the NAS without entering an OTP verification code.

1. Sign in to UGREEN NAS using a trusted device. After signing in, click "**Me**" in the upper-right corner of the desktop.

2. Click the username of the currently signed-in account to open the account settings page.

![](https://file-us.ugreennas.com/admin/article/2026-08-28/6b36eb08b71c49f5ba2212b6d4b3883c.webp)

3. On the "**Local Account**" page, find "**Two-factor authentication (2FA)**" and turn it off.

![](https://file-us.ugreennas.com/admin/article/2026-08-28/5a16c5f78cac45f1908a78b1346518fd.webp)

4. Follow the on-screen instructions to enter your sign-in password for verification. Once verified, two-factor authentication will be disabled.

## Method 3: Ask Another Administrator to Disable Two-Factor Authentication

If there is another administrator account on the device, you can ask that administrator to disable two-factor authentication for your account.

1. Sign in to UGREEN NAS using another administrator account.

2. Open "**Control Panel**" > "**User Management**".

3. Find the account in the user list, then click "**···**" > "**Edit**" on the right.

![](https://file-us.ugreennas.com/admin/article/2026-08-28/6a9eb999731549e2a6b3bff2143d8b8a.webp)

4. On the "**Basic info**" page, find "**Two-factor authentication (2FA)**" and click "**Close**". Then click "**Save**".

![](https://file-us.ugreennas.com/admin/article/2026-08-28/85b032d54426451c82a6862deefb82be.webp)

After 2FA is disabled, you can sign in with the account and password without entering a two-factor authentication verification code.

## Method 4: Reset the Administrator Login Status Using RESET

If the current account is the only administrator account on the device and you cannot regain access using the emergency verification email, a trusted device, or another administrator, you can use the device's RESET button to reset the network settings and administrator password, then sign in to the system to manage the account settings.

1. While the device is powered on, press and hold the **RESET** button for about 5 seconds.

2. Release the button after you hear one **beep**.

3. Wait for the device to restart.

4. On the sign-in screen, sign in with the default administrator account. The username is admin, and the password is blank.

5. After signing in, reset the password for the original account.

Then sign in with the original account and the new password, and reconfigure two-factor authentication.

**Note**: The RESET operation restores some network and administrator-related settings.

## Notes

● When enabling two-factor authentication, it is recommended to also set an emergency verification email address so you can quickly regain access if you are unable to obtain the 2FA code.

● If another trusted administrator account is available, prioritize asking that administrator to help disable two-factor authentication.

● If you use the RESET button, follow the device instructions carefully to avoid triggering other reset procedures.

● To prevent future login issues, keep the recovery method for your OTP app or your emergency verification email information secure.
