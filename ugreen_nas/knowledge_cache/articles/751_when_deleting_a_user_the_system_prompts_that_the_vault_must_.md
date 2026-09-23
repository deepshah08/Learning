# When deleting a user, the system prompts that the Vault must be reset first. What should I do?

> **Article ID**: `751`  
> **Category**: `Application Guide > Vault > When deleting a user, the system prompts that the Vault must be reset first. What should I do?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/751  

---

## Issue Description

When attempting to delete a user account, the system prompts that the Vault must be reset first, preventing direct deletion of the user.

![](https://file-us.ugreennas.com/admin/article/2025-08-05/1154aad8a742472ab1d17614bd740d28.webp)

## Cause Analysis

When a user has enabled the Vault feature, their data is bound to that account. To ensure data security, the system requires that related encrypted data be properly handled before the user can be deleted.

## Solution

Please log in to the NAS with the user account in question, open the "Vault" app, and perform a "Reset Vault" operation. After resetting, the user can be deleted normally.

![](https://file-us.ugreennas.com/admin/article/2025-08-05/3bf637aff2d84d91a8c0a61c171d203c.webp)

If the user is from an AD domain (company unified account system), when deleting the user, an option to “Keep Data” or “Delete Completely” will appear. Choosing “Keep Data” will retain the Vault data in storage, while selecting “Delete Completely” will permanently remove the associated data.
