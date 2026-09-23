# How to Enhance the Security of Your UGREEN NAS?

> **Article ID**: `448`  
> **Category**: `Application Guide > Control Panel > FAQ > How to Enhance the Security of Your UGREEN NAS?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/448  

---

> Applicable Note: This article applies to UGOS Pro firmware version 1.8.20.0012. Screenshots are for reference only; the actual interface may vary depending on system or app versions. Some options and features may differ between versions—please refer to the actual interface.

NAS devices are mainly exposed to security risks from malicious software and ransomware threats over the Internet. To effectively prevent these attacks and protect your UGREEN NAS and data, administrators are advised to configure the following measures:

## Set Password Strength and Expire Rules

1. Open the "Control Panel" app, then go to "User Management" > "Advanced Setting".

2. Configure the "Password strength rules" and "Password expire rules", then click "Apply" to save.

![](https://file-us.ugreennas.com/admin/article/2025-08-27/b5b3b09f220e4ffcb98e634b26ceb611.webp)

## Set Account Security Rules

1. Open the "Control Panel" app, then go to "Security" > "Security".

2. Enable the illustrated security rules, adjust them as needed, and click "Apply" to save.

![](https://file-us.ugreennas.com/admin/article/2025-08-27/aeee224dbf6c4fec99827ca7e640fc99.webp)

3. Switch to the "Account security" page and enable "Account blocking". Accounts meeting the conditions will be automatically blocked.

![](https://file-us.ugreennas.com/admin/article/2025-08-27/1994f3279691440284ff0b366f35c1b3.webp)

## Install the Security App

1. Open the "APP Center", locate "Security", and click "Install".

2. After installation, open the app and enable "Real-time Protection".

![](https://file-us.ugreennas.com/admin/article/2025-08-27/779bf7f4c23144a898730ae6e398c2c5.webp)

## Data Sync & Backup

### Sync data to another UGREEN NAS

● The "Sync & Backup" feature supports cross-device synchronization, enabling real-time backup and sharing between multiple NAS devices.

● Reference: [Sync with Another UGREEN NAS.](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MzI2LCJ0eXBlIjoidGFnMDAxIiwicGF0aENvZGUiOiJwcm8wMDIsazZybGJzLGczNWZvdyw2azhPdnQiLCJsYW5ndWFnZSI6InpoLUNOIiwiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIifQ==)

### Backup between storage pools

● Within "Sync & Backup", the "Backup between storage pools" feature allows regular backup of important data across different storage pools, enhancing data security and flexibility.

● Reference: [Backup Between Storage Pools](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6NDYzMSwidHlwZSI6InRhZzAwMSIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo2ODEsImFydGljbGVWZXJzaW9uIjoiMS4wIiwicGF0aENvZGUiOiJwcm8wMDIsazZybGJzLHJ6d3Y3dCxVanYydEkifQ==) .

### Enable Two-Factor Authentication (2FA)

● After enabling Two-Factor Authentication, logging in requires both the password and a one-time password (OTP). Even if someone obtains your username and password, they cannot log in to your NAS.

● Reference: [2FA Two-Factor Authentication](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmNTEwIn0=).

## Update NAS Firmware

1. Open the "Control Panel" app, go to" Update & Restore", and click "Update check interval" on the system update page.

2. If a new version is available, click "Update now" to upgrade.

![](https://file-us.ugreennas.com/admin/article/2025-08-27/514ab848a7b14ff7b4cc35a7c83837c4.webp)
