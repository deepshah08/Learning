# Control Panel

> **Article ID**: `63`  
> **Category**: `Application Guide > Control Panel > Control Panel`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/63  

---

## Applicability

**Applicable Clients**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: NAS Firmware 1.18.0.0093 and higher

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

Control Panel is used to centrally manage system features and basic device settings. Administrators can use Control Panel for User Management, File Service, Device Connection, Network, Security, Hardware & Power, System updates, and more.

**Note**: Control Panel is accessible only to administrators. Standard users cannot view or use Control Panel.

![](https://file-us.ugreennas.com/admin/article/2026-09-16/ce28ef411beb462db65389f2802e42fe.webp)

## How to Access Control Panel?

1. Log in to the device and open "**Control Panel**" from the system desktop.

2. Select the corresponding feature module as needed.

Control Panel supports search at the top. To quickly find a configuration option, enter the feature name in the search bar.

## Feature Modules Overview

Control Panel mainly includes the following feature modules:

|  |  |  |
| --- | --- | --- |
| **Category** | **Feature Module** | **Main Purpose** |
| Connection & Access | User Management | Manage local accounts and configure user permissions and access control |
| Connection & Access | File Service | Manage file sharing services such as SMB, NFS, FTP, WebDAV, and rsync |
| Connection & Access | Device Connection | Manage LAN, UGREENlink, DDNS, web access restrictions, and more |
| Connection & Access | Domain/LDAP | Manage permissions for domain or LDAP users when accessing system files |
| Connection & Access | Terminal | Manage Telnet / SSH access |
| General | Hardware & Power | Manage the buzzer, fan, LED indicator, power policies, and more |
| General | Time & Language | Set the system time and language |
| General | Network | Manage network interfaces, gateways, DNS, multiple gateways, and Network bridging |
| General | Indexing Service | Create file indexes to improve search and file lookup efficiency |
| General | Security | Manage the firewall, IP blocking, whitelist, and certificates |
| Service | About | View the device model, system version, and hardware information |
| Service | Update & Restore | Manage system updates, restore, and reset |

## Connection & Access

### User Management

User Management is used to manage local accounts on the device and supports the following operations:

● Add local accounts

● Edit local account information

● Delete local accounts

● Configure user permissions and access control

You can assign appropriate permissions to different users based on household or team needs.

### File Service

File Service is used to manage file sharing protocols and supports the following services:

● SMB

● NFS

● FTP

● WebDAV

● rsync

You can enable the required file access protocol based on the device and use case.

### Device Connection

Device Connection is used to manage device access methods and supports the following services:

● LAN

● Remote Access

● UGREENlink

● DDNS

● Web access restrictions

You can select the appropriate access method based on your actual network environment.

### Domain/LDAP

Domain/LDAP is used for account and permission management in enterprise or organizational environments. Administrators can use this feature to manage permissions for domain or LDAP users when accessing system files.

### Terminal

Terminal is used to manage Telnet / SSH access for system-level maintenance or troubleshooting. This feature is available only to administrators. Before enabling it, make sure you understand the associated risks.

## General

### Hardware & Power

Hardware & Power is used to manage device hardware and power policies and supports the following services:

● Buzzer

● Cooling fan

● LED indicator

● Scheduled startup and shutdown

● Hard drive sleep

Supported Hardware & Power features may vary by model. Please refer to the actual interface.

### Time & Language

Time & Language is used to set the system time, time zone, and language options.

Correct time settings help ensure that features such as logging, scheduled tasks, and certificate validation work properly.

### Network

Network is used to manage device network parameters and supports the following services:

● Network interfaces

● Default gateway

● DNS server

● Multiple gateways

● Network bridging

Incorrect network configuration may affect LAN access, remote access, and app network connectivity. Before making changes, make sure you understand the current network environment.

### Indexing Service

Indexing Service is used to create file indexes to improve Universal Search and file lookup efficiency. After indexes are created, you can find content on the device more quickly through Universal Search.

### Security

Security is used to manage system security features and supports the following services:

● Firewall

● IP block

● Whitelist

● Certificates

It is recommended to configure security rules based on your actual network environment and access requirements.

## System Service

### About

About is used to view basic device information, including:

● Device model

● System version

● CPU information

● Memory information

● Drive information

This page can be used to check the device status or provide basic information when contacting technical support.

### Update & Restore

Update & Restore is used to manage system updates and recovery operations and supports the following operations:

● Check for/perform system updates

● System restore

● Reset operations

Before performing a restore or reset, make sure you understand the impact of the operation.

## Feature Differences Between Models

The Control Panel features supported by different device series may vary. Taking the DH Series as an example, some features are limited:

● "**Hardware & Power**" does not include "**Power management**"

● "**LED indicator**" only supports on/off control and does not support additional custom settings

For specific feature support, please refer to the actual interface on your device.
