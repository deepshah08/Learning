# [FAQ] Virtual Machine Graphics Card Introduction

> **Article ID**: `235`  
> **Category**: `Application Guide > Virtual Machine > FAQ > [FAQ] Virtual Machine Graphics Card Introduction`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/235  

---

UGREEN NAS virtual machines currently support four types of graphics cards: Cirrus, VGA, VMVGA, and Virtio. The choice of graphics card type when configuring a virtual machine will affect the graphical display quality and performance of the virtual machine. Below are the meanings and differences of these four common graphics card types.

1. Cirrus (Cirrus Logic GD5446):

Meaning: Cirrus is a traditional VGA graphics card emulator used to provide basic graphical display support.

Features: The Cirrus graphics card emulator is suitable for scenarios with low compatibility requirements, such as old operating systems or applications that do not require high-performance graphics.

2. VGA (Standard VGA):

Meaning: VGA is a standard VGA graphics card emulator that provides good compatibility and basic graphical display functionality.

Features: The VGA graphics card emulator is suitable for most virtual machine scenarios, providing general graphical display support suitable for common applications and operating systems.

3. VMVGA (VMware Virtual SVGA):

Meaning: VMVGA is a VMware-specific virtual graphics card type that provides higher performance and functionality to virtual machines.

Features: The VMVGA graphics card provides better graphical performance and feature support, suitable for applications that require higher graphical performance such as graphic design, video editing, etc.

4. Virtio (Virtio GPU):

Meaning: Virtio is a virtualization-based high-performance GPU that provides hardware-accelerated graphics processing capabilities.

Features: Virtio GPU provides higher graphical performance and hardware acceleration through virtualization technology, suitable for applications that demand high graphical performance such as gaming, virtual reality, etc.

Differences:

- Performance: VMVGA and Virtio typically provide higher graphical performance and hardware acceleration capabilities, while Cirrus and VGA have lower performance.

- Compatibility: Cirrus and VGA have good compatibility and are suitable for various scenarios, while VMVGA and Virtio may not be compatible with certain older operating systems.

- Functionality: VMVGA and Virtio provide richer graphical features and hardware acceleration support, suitable for applications that require advanced graphical features.

Different graphics card types are suitable for different needs and usage scenarios. Below are typical scenarios for each graphics card type:

1. Cirrus: Support for old operating systems: When you need to run old operating systems such as Windows 95/98 or MS-DOS in a virtual machine, the Cirrus graphics card emulator is usually a suitable choice because it provides basic graphical support for these ancient systems.

2. VGA:

General application scenarios: The VGA graphics card emulator is suitable for most general virtual machine application scenarios, including running various common operating systems (such as Windows, Linux, etc.) and applications, as well as performing general office work, web browsing, etc.

3. VMVGA:

Scenarios with high graphical performance requirements: VMVGA graphics cards are suitable for applications with high graphical performance requirements, such as graphic design, video editing, 3D modeling, etc., as it provides better graphics acceleration and performance.

4. Virtio:

High-performance graphic applications: Virtio GPU is suitable for applications with extremely high graphical performance requirements, such as game development, virtual reality, deep learning, etc., as it provides hardware acceleration and high-performance graphics processing capabilities.

You can choose the appropriate graphics card type based on your specific needs and usage scenarios to best meet the graphical display and performance requirements of your virtual machine.
