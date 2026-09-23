# Advanced Settings for User Management

> **Article ID**: `68`  
> **Category**: `Video Tutorials > Features Overview > OpenList Quick Start Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/68  

---

In the "Control Panel" app, administrators can configure password policies—such as password strength and expiration rules—by going to [User Management] > [Advanced Settings], thereby enhancing account security. The detailed steps are as follows:

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250530/a8b0b2e4-08ba-40dc-b8b0-c244d36029e9.png)

## **Password Strength Policy Settings**

1. Open the [Control Panel] > [User Management] > [Advanced Settings] page.
2. Enable or disable the following password strength options based on your needs:

* **Block username inclusion**: When enabled, the password must not contain the associated username.
* **Block common passwords**: When enabled, commonly used high-risk passwords such as `123456`, `password`, `88888`, etc., are not allowed.
* **Require uppercase and lowercase letters**: When enabled, the password must contain both uppercase and lowercase letters.
* **Require numbers**: When enabled, the password must include at least one digit (0–9).
* **Require special characters**: When enabled, the password must include at least one special character (such as `~`, `@`, `#`, `%`, `&`, or a space).
* **Minimum password length** (enabled by default): When enabled, sets the minimum password length (6–127 characters).

1. After configuring, click [Apply] to save the settings.

**Notes**

* Password strength rules apply only when creating new users or changing the password of existing users. They do not apply to current passwords or users created via import.
* The "Minimum password length" option is enabled by default, with an initial value of 6. Empty passwords are not allowed.
* To enhance account security, it is recommended to set the minimum password length to at least 8 characters and enable at least three of the first five options listed above.

## **Password Expiry Rule**

1. Go to [User Management] > [Advanced Settings], and enable the password expiry rule.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250530/591af587-c684-4bcc-b1aa-d26905cd1dcb.png)

2. Configure the following options:

* **Password Validity Period**: Set the duration for which a password remains valid (unit: days).
* **Reminder days in advance (before password expires)**: Specify how many days before expiry the system reminds users to change their password.
* **Password change required after expiry**: When enabled, users must change their password upon login if it has expired.
* **Permanent password users**: Assign users whose passwords never expire; the above rules do not apply to them.

1. Once configuration is complete, click [Apply] to save the changes.

**Notes**

* Once Password expiry rules are enabled, the system will apply the rules to all users except those listed under Permanent password users.
* If Password change required after expiry is enabled, users whose passwords have expired will be prompted to change their password upon next login before accessing their account.
* It is recommended that administrators regularly check user account statuses and configure appropriate reminder days in advance to help maintain account security.
