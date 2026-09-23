# How to Configure Firewall Rules to Improve System Security?

> **Article ID**: `353`  
> **Category**: `Application Guide > Control Panel > FAQ > How to Configure Firewall Rules to Improve System Security?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/353  

---

## Applicability

**Applicable Clients**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: UGOS Pro firmware 1.18.0.0093 or later

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

You can configure firewall rules to control which port services specific IP addresses can access in UGOS Pro. This lets trusted devices connect while blocking suspicious sources, helping prevent unauthorized users from signing in to or controlling the system.

Common use cases:

● **Home use**: Allow all devices on your home LAN to access UGOS Pro while blocking access from unknown external networks.

● **Remote work**: Allow remote access only from your office's fixed public IP address and block all other addresses.

● **Limit exposure**: When making a file-sharing service such as SMB externally accessible, allow access only from the intended user's fixed IP address or subnet instead of exposing the service to the entire internet.

## Prerequisites

Before you begin, prepare the following:

● Identify your home LAN subnet (run ipconfig in Command Prompt on Windows or check "System Settings > Network" on macOS), for example, 192.168.1.0/24. **Subnets vary by network, so replace this example with your actual subnet when configuring the rule**.

● List the IP addresses or IP ranges that should be allowed to access UGOS Pro, including the fixed public IP address of the remote office. If the public IP address is dynamic, the rule will stop working after the address changes.

● Identify the services that need to be allowed, such as SMB file sharing, as well as the IP addresses or locations that need to be blocked.

## Understand the "Network Connection" Option

The **Network Connection** setting in a firewall rule specifies which network interface the rule applies to. There are two options: **All** and a specific **LAN port**. Note that LAN ports are displayed using their actual interface names (for example, VBR-LAN2), rather than always appearing as "LAN":

|  |  |  |
| --- | --- | --- |
| **Option** | **Applies To** | **Description** |
| All | All network interfaces on the device | Covers all access paths into the device, including access from the public internet. Recommended when configuring source rules to avoid missing an interface. |
| A specific LAN port | Only the selected network port | The rule applies only to traffic entering through that port. |

**Note**: A device can have multiple network interfaces, such as multiple LAN ports, virtual bridges, and link aggregation interfaces. If you select a single LAN port, traffic entering through other interfaces will not match the rule. Unless you are familiar with every access path to the device, we recommend selecting **All** and using the "Source IP/Location" conditions to control what is allowed or blocked.

Unless you need fine-grained control by network interface, In the examples in this guide, set **Network Connection** to **All**. You can also select a specific LAN port, which is shown by its actual interface name.

## Configuration Example

This guide uses four firewall rules to show how to manage traffic by **IP address** (a single host or subnet), **Location**, and **built-in services**.

**Matching mechanism**: Firewall rules are evaluated from top to bottom. Once a rule matches, it is applied immediately and no rules below it are evaluated. If none of the rules match, the "**Default Action**" is applied. Rule order is therefore critical. Follow these principles:

1. Place the rule that allows access from your own management device at the top to avoid accidentally locking yourself out.

2. "**Deny**" rules must be placed **before** broader "**Allow**" rules that they are intended to override.

3. For rules of the same type,**place the more specific rule first**: a specific IP takes priority over a subnet, and a subnet takes priority over "All IPs".

Example rule overview (the default action will ultimately be changed to "Access denied"):

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Rule Order** | **Rule Name** | **Network**  **Connection** | **Source IP** | **Port** | **Permission** |
| 1 | Allow All Services for the LAN Subnet | All or the actual LAN port | Home LAN subnet 192.168.1.0/24 | All | Allow |
| 2 | Allow Remote Office IP to Access All Services | ALL | Office fixed public IP (example: 1.2.3.4) | All | Allow |
| 3 | Deny All Services from Specific Locations | ALL | Specific Locations | All | Deny |
| 4 | Allow Branch Office Subnet to Access SMB | ALL | Branch office subnet 198.51.100.0/24 (example) | SMB (built-in service) | Allow |

In this example, Rule 3 is placed before Rule 4, so IP ddresses from the blocked locations cannot access any service, including SMB.

## Enable the Firewall

1. Go to "**Control Panel**" > "**Security**" > "**Firewall**", then click the enable button.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/54508d37948243139f679221ab058d13.webp)

2. On the "**Add firewall configuration**" page, click "**New Rules**" to start adding rules. Configure the rules using the examples below.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/dd408d51dba344759dbad7a9eed2a637.webp)

## Manage by IP Address (Rules 1 and 2)

The following example creates two firewall rules: one for the home LAN and one for the remote office.

**Rule 1: Allow the Home LAN to Access All Services**

|  |  |
| --- | --- |
| **Rule Item** | **Configuration** |
| Rule Name | Allow All Services for the LAN Subnet |
| Network Connection | ALL (or select the actual LAN port used by your home devices) |
| Port | All |
| Source IP | Specific IP: 192.168.1.0/24 (available host addresses on this subnet: 192.168.1.1–192.168.1.254; replace this with your actual home subnet) |
| Permission | Allow |

**Steps**:

1. On the "**Add firewall configuration**" page, click "**New Rules**". Set the rule name, permission (Allow), network connection (All), port (All), and other options.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/62f226c545764064b2ac1f64c4697897.webp)

2. Under "**Source IP**", select "**Specific IP address**" and click "**Select**". Then enter the IP address, subnet, or IP range to which the rule should apply. In this example, enter a subnet such as 192.168.1.0/24.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/4ec4ef1992344e9e81dba7fe02d4e57f.webp)

3. Click "**Confirm**" to add the rule to the firewall rule list. Check "**Enable**" and click Confirm for the rule to take effect. Repeat this step to enable each rule you add.

**Note**: If your home network uses multiple subnets, such as separate wired and wireless subnets, add an Allow rule for each subnet.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/390f34eb25784125a70097a940c7e39f.webp)

**Rule 2: Allow the Remote Office's Fixed IP to Access All Services**

|  |  |
| --- | --- |
| **Rule Item** | **Configuration** |
| Rule Name | Allow Remote Office to Access All Services via External IP |
| Network Connection | **ALL** (remote traffic can reach the device through different router paths, so selecting All covers all interfaces) |
| Port | All |
| Source IP | Specific IP: 1.2.3.4 (single host; example only—replace it with the office's actual fixed public IP address) |
| Permission | Allow |

**Steps**:

1. On the "**Add firewall configuration**" page, continue by clicking "**New Rules**". Set the permission (Allow), network connection (All), port, and other options.

2. Under "**Source IP**", select "**Specific IP address**" and click "**Select**". Then enter the IP address, subnet, or IP range you want to allow. In this example, enter the single host 1.2.3.4.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/19394021377345feb06460676e71ebe4.webp)

3. Click "**Confirm**" to add the rule to the firewall rule list. Check "**Enable**" and click Confirm for the rule to take effect.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/67178b00d9ec475ebd29b90ec23749ba.webp)

**Note**:

● Make sure this is the office network's **fixed public egress IP address**. If the public IP address is dynamic, the rule will stop working when the address changes, which may go unnoticed. In this case, we recommend using the official UGOS Pro remote access feature instead.

● If the device is behind a router, map the required service ports on the router to the device. Some network setups, such as double NAT or a reverse proxy, can rewrite the source IP address, preventing the rule from matching the public IP correctly. Test actual connectivity after configuration.

## Manage by Location (Rule 3)

The following example uses "Location" to create a blocking rule.

**Rule 3: Deny All Services from Specific Locations**

|  |  |
| --- | --- |
| **Rule Item** | **Configuration** |
| Rule Name | Deny All Services from Specific Locations |
| Network Connection | ALL |
| Port | All |
| Source IP | Location: select by country/region (multiple selections allowed) |
| Permission | Deny |

**Steps**:

1. On the "**Add firewall configuration**" page, continue by clicking "**New Rules**". Set the permission (Deny), network connection (All), port (All), and other options.

2. Under "**Source IP**", select "**Location**", then specify the locations to which the firewall rule should apply. You can select multiple locations. In this example, select the system-reserved location options.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/ffdcbfc421154a3a9e10aa7d0db5a7cd.webp)

3. Click "**Confirm**" to add the rule to the firewall rule list. Check "**Enable**" and click Confirm for the rule to take effect.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/b99de99b16a741e2ad8010786fcf9535.webp)

**Note**:

● Rule 3 must be placed **above** Rule 4 (Allow SMB). This ensures that IP addresses from blocked locations cannot access any service, including SMB. If the Allow rule is placed above it, SMB traffic from those locations will be allowed under the first-match principle, and the "Deny All Services" rule will not take effect.

● Location-based blocking relies on an IP geolocation database and may be bypassed by proxies or VPNs. Use it as an additional risk-reduction measure rather than your only line of defense.

## Manage by Built-in Services (Rule 4)

The following example uses a built-in service to allow a branch office subnet to access the SMB file-sharing service.

**Rule 4: Allow a Branch Office Subnet to Access SMB**

|  |  |
| --- | --- |
| **Rule Item** | **Configuration** |
| Rule Name | Allow Branch Office Subnet to Access SMB |
| Network Connection | ALL |
| Port | Select from the built-in service list: SMB (137–139, 445; refer to the actual interface) |
| Source IP | Specific IP: 198.51.100.0/24 (example branch office subnet; replace it with your actual subnet) |
| Permission | Allow |

**Steps**:

1. On the "**Add Firewall Configuration**" page, continue by clicking "**New Rules**". Set the permission (Allow), network connection, and other options.

2. Under "**Port**", select "**Select a port from the list of built-in services**", then click "**Select**".

![](https://file-us.ugreennas.com/admin/article/2026-09-07/4086970ec0bc46c897fc1670c7035962.webp)

3. Select the built-in application to which the firewall rule should apply. In this example, select SMB.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/923f01e79aff4e1e8043397be19642b6.webp)

4. Return to the rule configuration page. Under "**Source IP**", select "**Specific IP address**" and enter 198.51.100.0/24. Click "**Confirm**", check "**Enable**", and confirm to apply the rule.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/7ee90d5be5334eec86251bcf8b3c03c6.webp)

**Note**:

● SMB ports, especially port 445, are common targets for worms and ransomware. Exposing SMB file sharing to the entire internet carries a very high security risk.

● Many internet service providers block SMB traffic from the public internet, so SMB may still be unreachable even if you allow all incoming traffic.

● If you must make SMB accessible from the public internet, you can change Source IP to "All". However, carefully assess the risks and prioritize safer methods such as the official UGOS Pro remote access feature or a VPN for file sharing.

## Check Rule Priority

After configuration, make sure the rules are in the correct order.

1. **Make sure the IP address of your computer has the highest priority in the firewall rule table** to avoid accidentally blocking your own access.

2. Check the rule order. Traffic that needs to be "**Deny**" must have its Deny rule placed **before** any broader Allow rule that could otherwise permit it. For example, in this guide, IP addresses from "Specific Locations" must not be able to access SMB. Therefore, "Deny All Services from Specific Locations" (Rule 3) must be placed above "Allow a Branch Office Subnet to Access SMB" (Rule 4). If the order is reversed, the first-match principle will prevent the Deny rule from blocking SMB traffic.

3. For rules of the same type, place the more specific rule first (specific IP before subnet, and subnet before "All IPs").

Once the order is correct, you can **drag and drop** rules on the firewall rule list page to fine-tune their order. Rules higher in the list have higher priority.

## Update the Default Action

Follow the steps below in order to avoid losing access to the system after changing the default action:

1. Add and enable all firewall rules.

2. Verify that access works correctly from both LAN and remote devices.

3. After verification, under "**If none of the above rules match**", the system will apply the selected default action (Allow Access by default). For this example, change the default action from "**Access allowed**" to "**Access denied**" to block all access requests that do not match an existing rule.

● **Access allowed** (default): Allows all access requests that are not blocked by a firewall rule. Recommended for typical LAN environments where the device is not directly exposed to the public internet.

● **Access denied** (strict mode): Allows only access requests explicitly permitted by a rule and blocks all others. Recommended when the system is exposed to the public internet or requires stricter security.

4. After switching the default action, test all access scenarios again, including LAN access, remote access, and file sharing.

![](https://file-us.ugreennas.com/admin/article/2026-09-07/23f21dab4a4b497792ece2f40763066b.webp)

**Note**: After switching to "**Access denied**", access to the management interface is also controlled by firewall rules. Make sure "Network Connection" and "Source IP" are configured correctly for each rule, and that at least one Allow rule covers your current access path. Otherwise, you may be unable to sign in remotely. If you are accidentally blocked, sign in to Control Panel from the local LAN to adjust the rules or temporarily disable the firewall.

## Notes

● After adding a firewall rule, you must check "**Enable**" for the firewall configuration to take effect.

● You can create up to **10** custom firewall configuration profiles, with up to 50 rules in each profile.

● On the firewall rule list page, you can **drag and drop** rules to change their order. Rules higher in the list have higher priority, and rules are evaluated from top to bottom.

● If multiple network ports are connected to the same subnet, firewall rules may not work properly.

● After the firewall is configured, ports exposed by Docker containers may be blocked by default and must be allowed manually. Virtual machines may also be unable to obtain an IP address or connect to the network because of firewall restrictions.

● If you use multiple LAN ports with link aggregation, the firewall applies only the rules of the first network interface.

● Source IP rules apply by address family. If IPv6 is enabled on your network, make sure corresponding rules are configured for every address family you need to control. Otherwise, IPv6 traffic may bypass rules that were configured only for IPv4.

● Rules based on "Location" rely on an IP geolocation database and may be bypassed by proxies or VPNs. Use them as an additional security measure rather than your only line of defense.
