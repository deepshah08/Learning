# [FAQ] Types of Virtual Machine Booting

> **Article ID**: `234`  
> **Category**: `Application Guide > Virtual Machine > FAQ > [FAQ] Types of Virtual Machine Booting`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/234  

---

How should I choose the boot type for virtual machines?

UGREEN NAS virtual machines have two boot types: BIOS (Basic Input/Output System) and UEFI (Unified Extensible Firmware Interface). The main differences between them are as follows:

1. Booting Method:

  • BIOS: Traditional booting method that uses Master Boot Record (MBR) to boot the operating system.

  • UEFI: Uses a unified firmware interface that supports modern booting methods and uses GUID Partition Table (GPT) to boot the operating system.

2. Capacity Limitation:

  • BIOS: Limited boot disk capacity, typically supporting a maximum of 2TB boot disk.

  • UEFI: No boot disk capacity limitation, can support larger capacity boot disks.

3. Security:

  • BIOS: Relatively fewer security features, susceptible to boot-time malware attacks.

  • UEFI: Supports security features like Secure Boot, which can prevent boot-time malware intrusion.

4. Compatibility:

  • BIOS: Good backward compatibility, suitable for older versions of operating systems and software.

  • UEFI: Supports more modern hardware and features but may be incompatible with some older operating systems and software.

When choosing the boot type for virtual machines, the following factors need to be considered:

Operating System Support:

Some operating systems may only support specific boot types. For example, Windows 8 and later versions, Windows Server 2012 and later versions, and the latest Linux distributions usually support UEFI booting. Therefore, if you plan to install one of these operating systems in the virtual machine, you may need to choose the UEFI boot type.

If your virtual machine runs on older operating systems (such as Windows 7 and earlier versions) or software, and you do not need the security features of UEFI, then choosing the BIOS boot type may be more appropriate.

Disk Capacity:

If you plan to use a hard disk larger than 2TB as the boot disk for the virtual machine, then the UEFI boot type is necessary because BIOS booting has a capacity limit.

Security Requirements:

If you need additional boot security, such as preventing malware from being loaded during boot, then UEFI booting may be more suitable because it supports Secure Boot functionality. Secure Boot ensures that only operating system boot loaders signed by trusted certificates can boot.

Hardware Compatibility:

Some newer hardware devices (such as the latest motherboards and firmware) may be better suited for UEFI booting because UEFI provides better support for modern hardware.

Recommendations for Choosing Boot Types:

In conclusion, if your virtual machine's operating system supports UEFI booting, and you need to use large capacity disks or enhanced security features, then choosing UEFI booting may be a better choice. If your operating system does not support UEFI booting, or if your hardware devices are more compatible with BIOS booting, then BIOS booting may be the more suitable choice.
