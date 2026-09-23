# Firewall

> **Article ID**: `106`  
> **Category**: `Application Guide > Control Panel > Security > Firewall`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/106  

---

UGOS Pro supports a firewall feature to safeguard your device and stored data.

In [Control Panel] > [Security] > [Firewall], you can enable the firewall, create firewall rules, and configure firewall settings to prevent unauthorized logins and control service access.

You can allow or deny specific IP addresses from accessing certain network ports, effectively mitigating network attacks and data breaches.

## **Enable and Add Firewall Rules**

Go to [Control Panel] > [Security] > [Firewall] and check the box to enable the firewall.

1. In the "Firewall Configuration" section, click "New" to open the firewall configuration wizard.
2. Click "Add Rules", where you can configure the following rules:

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250310/316d0e7b-f6b5-4e3e-9820-4c8e9076929b.png)

(1) **Permission**: Choose to Allow or Deny access.

(2) **Network Connection**: Select LAN1 or LAN2. If an interface is not listed in the dropdown menu, it may be disconnected or assigned to another function.

3. **Ports:**

1. Select "All" to apply this firewall rule to all ports.
2. Select "Select a port from the list of built-in Services" (multiple selections supported).
3. Select "Custom" to define specific ports: Choose the port type (destination port or source port). Choose the communication protocol. Enter up to 15 ports (separated by commas) or specify a port range (1–65535, in ascending order).

4. **Source IP:**

1. Select "All" to apply the firewall rule to all IP addresses.
2. Select "Specific IP Address" to specify a single IP or an IP range.
3. Select "Location" to apply the rule to multiple designated locations.

5.Click "OK" to save the configuration.

If none of the above rules match, you can choose either "Allow Access" or "Deny Access" at the bottom of the rule list to determine how to handle requests that do not meet existing firewall rules for each interface.

## **Apply Firewall Configuration**

1. After creating firewall rules, you must check "Enable" on the New Firewall Configuration page. Click "OK" to apply the settings immediately.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250310/bc63d773-f3bd-4b83-adce-3ca0730b6caa.png)

2. In the Firewall Configuration Files section, you can also edit or delete configurations using the corresponding icons on the right side of the selected firewall profile.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250310/ee1d75cd-51e3-47d1-ab01-57d00a0f5563.png)

**Notes:**

1. A maximum of 10 custom firewall configurations can be created.
2. On the Firewall Rules List page, you can drag and rearrange rules—rules at the top have higher priority.
3. Firewall rules are executed in order of priority as listed.
4. If the same subnet is connected to multiple network interfaces, the firewall rules may not function correctly.
5. If you use link aggregation to combine multiple LAN ports, the firewall will apply the rules of the first network interface while retaining the rules for the second interface.

## **Configuration Examples**

**Example 1: Allow a Specific Subnet to Access All NAS Services**

* **Firewall Rule Name**: Allow Subnet Access

* **Permission**: Allow

* **Network Connection**: ALL (adjust based on your environment)

* **Port**: All

* **Source IP**: `192.168.1.0/24` (enter the subnet IP address and prefix length under "Specific IP Address")

This rule allows all IP addresses within the subnet `192.168.1.0/24` to access all NAS services.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250310/ec7483d5-d56c-4d94-99c5-f59e14d0c999.png)

**Example 2: Deny All IP Addresses from Accessing NAS WebDAV Service**

* **Rule Name**: Deny WebDAV Access

* **Permission**: Deny

* **Network Connection**: Bond6-1(adjust based on your environment)

* **Service/Port**: WebDAV (select the WebDAV port from the built-in service list)

* **Source IP**: All

This rule blocks all IP addresses from accessing the NAS WebDAV service.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250310/fe1a3cb6-9f21-4c60-b39a-5928da9ba665.png)

**Example 3: Deny Access to All NAS Services from Specific Locations**

* **Rule Name**: Deny NAS Access

* **Permission**: Deny

* **Network Connection**: ALL (adjust based on your environment)

* **Port**: All

* **Source IP**: Brazil, Canada (select from "Source IP Location")

This rule blocks all IP addresses from Brazil and Canada from accessing any NAS services.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250310/1ef5cd9b-5d08-4f18-969c-e607f92170c2.png)

**Related Tutorials:**

* [How to create firewall rules to allow or deny IP addresses access to UGREEN NAS?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjoxMDU3LCJhcnRpY2xlSW5mb0lkIjozNTQsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIn0=)
* [How to configure the firewall in UGOS Pro?](https://support.ugnas.com/knowledgecenter/#/detail/eyJhcnRpY2xlVmVyc2lvbiI6IiIsImxhbmd1YWdlIjoiZW4tVVMifQ==)

**Notes:**

**1.Port Type:**

* **Source Port**: The source port refers to the port on UGOS Pro/NAS that is used to send data. For example, if you configure a rule to deny a specific source port, other devices will be unable to access certain services on your NAS via that port.
* **Destination Port**: The destination port refers to the port on the remote device that receives data from UGOS Pro/NAS. For example, if you configure a rule to deny a specific destination port, you will be unable to access certain services (such as HTTP) through that port.

**2.Communication Protocol:**

* **All Protocols**: Applies the rule to all network protocols, ensuring comprehensive traffic control.
* **TCP Protocol**: A reliable transmission protocol used for services such as HTTP, HTTPS, and SSH.
* **UDP Protocol**: A fast, connectionless protocol used for services such as DNS and video streaming.
