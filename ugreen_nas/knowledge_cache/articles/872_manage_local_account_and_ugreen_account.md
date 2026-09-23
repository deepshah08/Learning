# Manage Local Account and UGREEN Account

> **Article ID**: `872`  
> **Category**: `Application Guide > UGOS Pro > Manage Local Account and UGREEN Account`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/872  

---

## Applicability

**Applicable client:** UGREEN NAS PC client (Windows/macOS).  
**Applicable version:** NAS firmware 1.16.0.0042 and later.

This article is for reference only. The actual interface and operation path may vary slightly due to system or app version updates. Please refer to the actual interface.

## Feature Overview

Account settings provide centralized management for "**Local Account**" and "**UGREEN Account**". They support profile customization, login password changes, login activity monitoring, two-factor authentication (2FA), and personal storage quota checks, helping ensure independent and secure device access.

## Entry Point

1. Log in to the system desktop and click "**Me**" on the right side of the top bar.

2. Click the **username** of the currently logged-in account to open the "**Account Settings**" page.

![](https://file-us.ugreennas.com/admin/article/2026-06-09/074a47ce9fb048e0a0d2e8619ef52335.webp)

## Manage Local Account

After entering the account settings page, the "**Local Account**" page is opened by default. The following management actions are available.

![](https://file-us.ugreennas.com/admin/article/2026-06-09/c2fa4bc0fa2446bd8a796d0a30daeda4.webp)

**Change Profile Picture:**

● Click "**Edit**" below the profile picture to select a default system avatar, or upload an image from the NAS or local computer.

● `JPG`, `JPEG`, `PNG`, `GIF`, `BMP`, and `WEBP` formats are supported. The maximum image file size is **8 MB**.

**Change Login Password:**

● Click "**Change password**" and enter the current password for identity verification. After verification is successful, a new password can be set.

● If the current password is forgotten, contact the device administrator to reset it in "**User Management**" in Control Panel. For details, see [How to Change and Manage Passwords?](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmNzczIiwiY2xpZW50VHlwZSI6Ik1PQklMRSJ9)

**Change Email Address:** Click this option to change the email address.

**Two-Factor Authentication (2FA):**

● After it is enabled, signing in to a UGREEN NAS device requires both the regular account password and a second-step one-time password (OTP), improving account security. For details, see [2FA Two-Factor Authentication](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MTQ3OCwidHlwZSI6InRhZzAwMSIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo1MTAsImFydGljbGVWZXJzaW9uIjoiMS4wMCIsInBhdGhDb2RlIjoicHJvMDAxLHdvdHMxaixwOWNja3AsRTlkQmV5In0=) .

**Account Activity:**

● Click this option to open the account activity list. The list records login activity for the current account, including connection time, client used, access IP address, and access protocol.

● If abnormal login credentials are found, click "**Terminate**" on the right side of the record. After the connection is forcibly terminated, this IP address must sign in again before accessing the device.

![](https://file-us.ugreennas.com/admin/article/2026-06-09/b22e5346d84849028808f2e466fcc0fa.webp)

**View Storage Quota:**

This area shows **the used capacity** of the personal folder and **the total quota limit** assigned by the administrator.

## Manage UGREEN Account

A UGREEN Account is the global credential for the UGREEN cloud ecosystem. On the account settings page, click "UGREEN Account" in the left sidebar to manage UGREENlink services and cloud security for the NAS.

### Sign In and Register

● On the sign-in page, enter the phone number and password of the registered UGREEN Account to sign in.

● Click "**Verification code**" to sign in quickly using a mobile verification code.

● If no UGREEN Account has been registered, click "**Register account**" at the bottom of the page and follow the instructions to create one.

![](https://file-us.ugreennas.com/admin/article/2026-06-09/307595793fa4450895aaf1e7fea77245.webp)

After signing in, personal information, account security, and UGREENlink external access service status can be managed.

![](https://file-us.ugreennas.com/admin/article/2026-06-09/224b2c97c24b4ca9b1dee5620f6d21fa.webp)

### Personal Information

Click "**Profile**" to open the details page. The following actions are available:

● Click "Change avatar" below the avatar to customize the displayed profile picture.

● Nickname, gender, and date of birth can be changed. Click the corresponding setting item to edit the information. The registered country/region is automatically locked by the system and cannot be changed manually.

### Account Security

Click "**Account** **Security**" to open the configuration center for high-level security management.

![](https://file-us.ugreennas.com/admin/article/2026-06-09/738d3485e69746389a30e95f1f51155a.webp)

● **Password:** Reset the login password for the UGREEN Account.

● **Change mobile phone:** Change the security phone number linked to the current account.

● **Unbind device:** Unbind the current NAS hardware device from this UGREEN Account.

● **Account deletion:** After clicking this option, the system will redirect to the official [UGREEN Account](https://web.ugnas.com/account/login/#/login) website. Go to "**Account & Security**" on the website to complete the account deletion process.

**Note:** Account deletion will permanently delete the current UGREEN Account and all associated data. This is a high-risk operation. Please proceed with caution.

![](https://file-us.ugreennas.com/admin/article/2026-06-09/3389fda315a144c8a3faf4d0ff86c5bf.webp)

### UGREENlink External Access Service

● 点击下方"**UGREENlink 外部访问服务**"进入详情页，可以查阅官方中转服务的运行数据，确认外部访问服务是否处于"**在线**"状态。

● 支持查看服务的"**连接方式**"和"**连接带宽**"，以及统计本月已用流量总额。

● Click "**UGREENlink External Access Service**" below to open the details page. Here, the running data of the official relay service can be viewed to confirm whether the external access service is "**Online**".

● The "**Connection method**" and "**Connection bandwidth**" of the service can be viewed, along with the total data used this month.

![](https://file-us.ugreennas.com/admin/article/2026-06-09/c9431193d8eb41afb02590fd2248fa7c.webp)

### Sign Out of UGREEN Account Session

● To sign out of the session between the current device and this UGREEN Account, return to the UGREEN Account home page and click "**Logout**" at the bottom of the page.
