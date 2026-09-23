# SSH Encryption Algorithm Configuration Guide

> **Article ID**: `774`  
> **Category**: `Application Guide > Control Panel > FAQ > SSH Encryption Algorithm Configuration Guide`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/774  

---

The SSH service on UGREEN NAS offers two security levels: **High** and **Low**. These levels essentially reflect different restrictions on the encryption algorithms (cipher suites) allowed in the SSH configuration file (`sshd_config`).

To ensure secure data transmission, **it is strongly recommended to use the High level**. The **Low** level should only be considered when connecting to very old client devices.

## Comparison of Configuration Levels

The table below provides a quick reference to help you choose the appropriate security level:

|  |  |  |
| --- | --- | --- |
|  | **High Level** | **Low Level** |
| **Use Case** | Most users, especially in internet-exposed environments | Internal network connections to legacy industrial equipment or old systems |
| **Security** | Very high (supports PFS, AEAD, SHA-2) | Lower (potential SWEET32 risk, supports MD5/SHA1) |
| **Compatibility** | Modern clients (OpenSSH 7.4+) | Excellent (compatible with clients from 10+ years ago) |
| **Recommendation** | Keep as default | Enable only temporarily if you encounter "no matching cipher" errors |

## High-Security Configuration (Recommended)

This mode uses only strong, secure algorithms while disabling known vulnerable or outdated ones, providing the highest level of protection against eavesdropping or data tampering.

**Included Algorithms:**

1. **Encryption Algorithms (Ciphers)**

● **AEAD types** (e.g., `aes128-gcm@openssh.com`, `chacha20-poly1305@openssh.com`): These algorithms simultaneously encrypt data and generate an authentication tag, ensuring both confidentiality and integrity without requiring a separate MAC algorithm.

● **CTR mode** (e.g., `aes128-ctr`): Converts AES block cipher into a stream cipher mode, offering fast performance and parallel processing capabilities.

2. **Key Exchange (KexAlgorithms)**

● **Curve25519**: The modern default for SSH, providing excellent performance and strong security.

● **Diffie-Hellman**: Supports high-strength prime groups from Group 14 (2048-bit) to Group 18 (8192-bit), ensuring forward secrecy.

3. **Integrity Verification (MACs)**

● Only supports `hmac-sha2` series (SHA-256/512) and `umac-128`. These algorithms are highly resistant to collisions and are very difficult to forge.

## Low-Security Configuration (Compatibility Mode)

This mode exists to ensure **compatibility**. While preserving high-strength algorithms, it also permits the use of certain weak security algorithms that have already been deprecated by the industry.

**Included Algorithms:**

1. **3DES-CBC (3des-cbc)**

● Risk: Vulnerable to the SWEET32 attack. With a block size of only 64 bits, the probability of collisions increases significantly when transmitting large amounts of data, potentially leading to plaintext exposure.

2. **AES-CBC (aes128-cbc)**

● Risk: CBC mode is not AEAD and must be used with a MAC. Historically, CBC mode in SSH has been susceptible to plaintext recovery attacks (CVE-2008-5161).

3. **Weak MACs (hmac-md5, hmac-sha1)**

● Risk: The collision resistance of MD5 and SHA-1 has significantly weakened. Although HMAC constructions have not been fully broken, modern security standards generally recommend disabling them.
