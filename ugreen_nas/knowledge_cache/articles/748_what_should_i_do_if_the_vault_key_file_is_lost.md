# What should I do if the Vault key file is lost?

> **Article ID**: `748`  
> **Category**: `Application Guide > Vault > What should I do if the Vault key file is lost?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/748  

---

## Issue Description

I accidentally deleted or lost the Vault’s .key file and can no longer access the Vault contents. What should I do?

## Cause Analysis

The Vault uses a dual encryption verification mechanism with the .key file and access password. Losing either may prevent unlocking the Vault.

● If only the .key file is lost but you still remember the access password, you can reset the password to regenerate the .key file and restore access.

● If you have also forgotten the access password, identity verification is impossible, and the original Vault contents cannot be recovered.

## Solution

If you still remember the access password, please follow these steps:

1. Open the "Vault" app, Click "Settings" > "Change Access Password."

2. Enter a new access password (it can be the same as the old one).

3. After clicking "Confirm," the system will regenerate the .key file and automatically download it to your computer. Please keep it safe.

If you have forgotten the access password, the only option is to "Reset Vault" to reactivate it, but the original Vault data cannot be recovered. Please proceed with caution.
