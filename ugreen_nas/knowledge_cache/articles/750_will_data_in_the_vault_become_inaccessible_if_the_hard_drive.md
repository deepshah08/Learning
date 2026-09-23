# Will data in the Vault become inaccessible if the hard drive is removed or disabled?

> **Article ID**: `750`  
> **Category**: `Application Guide > Vault > Will data in the Vault become inaccessible if the hard drive is removed or disabled?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/750  

---

## Issue Description

After a hard drive is removed or disabled, data in the Vault may become inaccessible or lost.

## Cause Analysis

Vault data is tightly bound to the storage space specified during its creation. For example:

* When the user first creates a Vault, its storage location is set to "Volume 1".
* Later, the hard drive containing "Volume 1" is removed or disabled.
* Then, the Vault is re-enabled on "Volume 2".

In this case, the system can only recognize the currently available Vault environment. The newly created Vault will not be linked to the original data, and the original Vault data will not be automatically migrated or displayed.

## Solution

Please reinsert or enable the hard drive that contains the original Vault’s storage space. The system will automatically recognize and load the original Vault data, and the original data will not be lost. If you need to migrate Vault data, please export or migrate it while the original storage space is still available.
