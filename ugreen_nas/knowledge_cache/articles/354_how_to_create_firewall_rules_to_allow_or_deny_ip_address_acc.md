# How to Create Firewall Rules to Allow or Deny IP Address Access to UGREEN NAS?

> **Article ID**: `354`  
> **Category**: `Application Guide > Control Panel > FAQ > How to Create Firewall Rules to Allow or Deny IP Address Access to UGREEN NAS?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/354  

---

This article provides two configuration examples to demonstrate how to create firewall rules on UGOS Pro to allow or deny access to specific network ports from specific IP addresses, helping prevent unauthorized logins and control service access.

## **Configuration Example 1: Allow Only Specific IP Addresses to Access UGREEN UGOS Pro**

If you want to allow access to UGOS Pro only from specific IP addresses (e.g., 192.168.1.1 to 192.168.1.100) and deny access from all other IPs, you will need to create two firewall rules.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250619/d3b262e7-60a3-4671-8f7f-c11998ed6ea1.png)

Go to [Control Panel] > [Security] >[Firewall] to enable the firewall.

1. Under the [Select Firewall Configuration] section, click "Add" to enter the Add Firewall Configuration wizard.

2. Click the "+ New Rules" button to configure the following rules.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Rule Name | Permission | Network Connection | Port | Source IP |
| Allow Specific IP Range | Allow | Select LAN based on environment | All | 192.168.1.1~192.168.1.100 |

This rule allows IP addresses in the range 192.168.1.1 to 192.168.1.100 to access all NAS services across all ports.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250619/40cf3239-88bb-4019-ac4c-464608f399df.png)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250619/a95b7886-1c73-4aca-92ef-915b87bb55d1.png)

3.Once the firewall rule is configured, check the "Enable" checkbox.

4.If none of the above rules are matched, check "Deny Access." Once enabled, only the IP addresses specified in the rules above will be allowed to access all NAS services.

5.After confirming, click "Apply" to save the settings.

## **Configuration Example 2: Deny Access to UGOS Pro from Specific IP Addresses**

If you want to deny access to your UGOS Pro from specific IP addresses (e.g., 192.168.1.0), while allowing access from all other IPs, you will need to create two firewall rules.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250619/2838db3e-7189-47c5-adad-bf72cf2b11c3.png)

Go to [Control Panel] > [Security] >[Firewall] to enable the firewall.

1. Under the [Select Firewall Configuration] section, click "Add" to enter the Add Firewall Configuration wizard.

2. Click the "+ New Rules" button to configure the following rules.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Rule Name | Permission | Network Connection | Port | Source IP |
| Deny Access from Specific IP | Deny | Select LAN based on environment | All | 192.168.1.0 |

This rule blocks the IP address 192.168.1.0 from accessing all internal NAS ports.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250619/c3c69b7a-df17-4c25-a6b2-23bfe5af131a.png)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250619/ffbd1174-bee5-4b89-a68b-5d1024cba5bd.png)

3.After configuring the firewall rules, check the "Enable" checkbox.

4.Then, if none of the above rules match, check "Allow Access." Once checked, only IP addresses specified in the rules above will be denied access to all NAS services.

5.After confirming, click "Apply" to save the settings.

## **Notes**

1. You must check "Enable" on the Add Firewall Configuration page for the firewall configuration to take effect.
2. Firewall rules are executed according to their priority order in the firewall rules list.
3. On the firewall rules list page, you can adjust the order of rules by dragging and dropping; rules higher in the list have higher priority.
4. If multiple network ports are connected to the same subnet, firewall rules may not function properly.
5. If you use multiple LAN ports combined with link aggregation, the firewall will only apply the rules from the first network interface.

For more details, please refer to: [[Control Panel] > [Security] > [Firewall]](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMTIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDEsdXJjYWJpLGh6d2JscCw5djNxNmwifQ==)
