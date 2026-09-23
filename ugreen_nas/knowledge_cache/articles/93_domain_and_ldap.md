# Domain and LDAP

> **Article ID**: `93`  
> **Category**: `Application Guide > Control Panel > Domain and LDAP`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/93  

---

## **Learn about domain and LDAP**

domain and LDAP are both crucial tools in network management. domain offer centralized management and heightened security, while LDAP provides flexibility and standardization benefits. When combined, they enable efficient and secure network resource management.

### **What is Domain?**

Domain is a network structure used for centralized management and control of network resources. The Domain Controller (DC) serves as the core server managing the domain, responsible for user authentication, permission management, and resource allocation. In a computer network, a domain functions as a logical grouping that typically includes a set of computers, users, and other resources, all centrally managed by the DC. domain facilitate secure management of user and resource access, allowing users to access all domain resources with a single account, simplifying network management, enhancing security, and improving controllability.

### **Advantages of Domain**

1. **Centralized Management:** Administrators can centrally manage user accounts, computers, and other resources through the DC.
2. **Security:** domain offer higher security, enabling uniform security settings configuration through Group Policy.
3. **Single Sign-On (SSO):** Users can access all domain resources with a single login.

### **What is LDAP?**

LDAP (Lightweight Directory Access Protocol) is a protocol used to access and manage directory services. Directory services are specialized databases designed for storing and retrieving information such as users, groups, devices, etc. LDAP is commonly used for user authentication and information lookup, making it a vital tool for SSO and unified identity management.

### **Advantages of LDAP**

1. **Standardization:** LDAP is an open standard widely supported by various operating systems and applications.
2. **Flexibility:** It can store various types of information, not limited to users and groups.
3. **Scalability:** Adapts to different needs through schema extensions.

## **Main Differences Between Domain and LDAP:**

1. domain primarily manage and organize computers and resources within a network, achieved through centralized management by DCs.
2. LDAP focuses on accessing and managing directory services, communicating with directory servers via protocols to enable user authentication and information lookup.

### **Relationship Between Domain and LDAP**

While domain and LDAP are distinct concepts, they are often used together. Domain controllers often utilize LDAP protocols to store and retrieve user information. For instance, Microsoft's Active Directory (AD) is an LDAP-based directory service for managing domain resources.

### **Advantages of Domain/LDAP:**

1. **Unified Management:** Through LDAP, domain controllers can uniformly manage users and resources, simplifying account and permission management via a single interface, enhancing efficiency.
2. **Enhanced Security:** Group Policy allows uniform configuration and enforcement of security settings, ensuring each device adheres to company security standards.
3. **SSO:** Employees can access all domain resources with a single account, eliminating the need to remember multiple passwords, improving user experience, and reducing password-related issues.

## **Usage Scenarios of Domain/LDAP in NAS**

### **Centralized Management and Authentication**

* **SSO:** Users can log in to NAS with a single account, simplifying user management.
* **Group Policy:** Administrators can manage NAS policies and uniformly configure permissions through the domain controller.
* **User Access Management:** Users can access shared folders on NAS based on individual and group access permissions.

### **Example Scenarios**

* **New Employee Onboarding:** With domain/LDAP, simply create an account for new employees to access all domain resources, enabling a quick start.
* **Resource Sharing:** Different departments share the same NAS device but can only access their respective folders, ensuring data security.
* **Personnel Changes:** When an employee's role changes, adjust their domain account's group permissions to promptly update their access rights.
* **Employee Departure:** Quickly disable departing employees' domain accounts to immediately terminate their access to all company resources, ensuring data security.

## **Configuration and Usage Guide**

### **Configuring Domain in UGOS Pro**

1. Open the **Control Panel** and click on the [Domain/LDAP] option.
2. Click "Join Domain/LDAP" to enter the Domain/LDAP Join Wizard.
3. In the Server Information section, select the Server Type, enter the Server Address, and DNS Server. Choose the type based on your server setup. Click "Next" after configuration.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/c1f0b490-5690-4877-b58b-cac0ea80b0e5.png)

4. Fill in the Domain Account and Domain Password. In Advanced Settings, set the sync interval for "Update User/Group List." The system will update the list accordingly. Click "Next" after configuration.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/1860a70f-ec9e-472a-904c-48d6a9a03a50.png)

5. The system will check your configuration. If successful, click "Confirm."

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/63f181b2-6ed4-4d62-b1ff-3f40a2a8cc5c.png)

6. If the check fails, follow prompts to verify your connection settings. Click "Details" to view the reason for failure.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/3c2f0a7e-849d-4125-8bf8-808d40f5822e.png)

7. Read the pop-up reminder, and click "OK" if everything is correct.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/59deb6a9-799f-4996-9c6c-43101224f0a0.png)

8. Once added successfully, you can view and manage your server information, domain users, and domain user groups in "Domain/LDAP".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/f1aa44e2-bb1a-42a9-907c-58d1a41518a0.png)

### **Exit Domain**

1. In the [Domain/LDAP] option, click "Exit Domain."
2. Click "OK" in the confirmation pop-up.
3. Enter the password of the currently logged-in administrator account and click "Submit."
4. After exiting, if you need to join the domain again, you will need to reconfigure and reconnect.

### **Configure LDAP in UGOS Pro**

1. Open the Control Panel and click the [Domain/LDAP] option.
2. Click "Join Domain/LDAP" to enter the Domain/LDAP Join Wizard.
3. In the Server Information section, select the Server Type, enter the Server Address, and DNS Server. Choose the type based on your server setup. Click "Next" after configuration.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/5c6e3f2e-d087-46f9-897d-eed755e6e430.png)

4. Fill in the Bind DN/Account, Password, and BASE DN. Encryption modes include SSL/TLS and STARTTLS, which can be set as needed.
5. In Advanced Settings, set the sync interval for "Update User/Group List." The system will update the list accordingly. Click "Next" after configuration.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/748a9767-d876-4147-9bad-83742d2f1a69.png)

6. The system will check your configuration. If successful, click "Confirm."

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/2786ce43-aa8a-4208-bf53-a18f9d9db6ec.png)

7. If the check fails, follow prompts to verify your connection settings. Click "Details" to view the reason for failure.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/34df5d69-6519-45d0-a76e-f0fb13a8aec8.png)

8. Read the pop-up reminder, and click "OK" if everything is correct.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/4bd99f4c-69ef-40fe-aeef-b30b3cf37055.png)

9. After successful addition, you can view and manage your server information, domain users, and domain user groups in "Domain/LDAP". Click "Test" to check the server's connection status. In Advanced Settings, you can set the sync interval for "Update User/Group List."

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250515/87340383-eae2-4fce-b2e8-e42c832e7482.png)

### **Exit LDAP**

1. In the [Domain/LDAP] option, click "Exit Domain."
2. Click "OK" in the confirmation pop-up.
3. Enter the password of the currently logged-in administrator account and click "Submit."
4. After exiting, if you need to join LDAP again, you will need to reconfigure and reconnect.

### **Modify Domain/LDAP User/Group Permissions**

* After successfully connecting to Domain/LDAP, you can view domain-synced user and group information in "Domain Users" and "Domain User Groups." If you update user and group information in the domain but it's not synced in NAS, you can manually click "Update Domain Data" to sync.
* By default, personal folders for domain users are disabled. To enable, select a user, click "Edit," check "Enable TA's Personal Folder" in domain user info, and click "Save." You can also set shared folder quotas and access permissions. Click "Edit," modify folder access permissions in "Permissions & Settings," set a maximum usage quota under "Quota," and click "Save."
* If a domain user has regular user permissions, shared folder access is defaulted to "Deny Access." Manually modify permissions by selecting a user, clicking "Edit," modifying desired shared folder permissions in "Permissions & Settings," and clicking "Save."
* For bulk modifications, add users to domain groups on the domain server. Then, modify group permissions in "Domain User Groups" in "Domain/LDAP". Select a group, click "Edit," modify desired shared folder permissions, and click "Save."

### **Logging in to UGOS Pro with a Domain/LDAP Account**

To log in to UGOS Pro using a domain user account, locate the corresponding domain username in the [Domain/LDAP] domain user list. Then, use the domain username and password to log in to UGOS Pro.

### **Notes**

1. When leaving the domain, if "Retain personal space data of domain users" is selected, the personal folders created by the domain users will not be deleted.
2. The permissions of domain users and user groups are consistent with those set on the domain server. If you need to change the permissions within the NAS (e.g., changing a common user to an administrator), manually edit and modify the settings under [Domain/LDAP] > "Domain Users."
3. In practical applications, to achieve unified identity authentication and access control for users, you can build a domain controller (AD domain) or LDAP directory service. It is recommended to use Windows Server 2012 R2 or later to set up the domain or LDAP service.
