# Import Uers

> **Article ID**: `71`  
> **Category**: `Video Tutorials > Features Overview > EasyNVR Quick Start Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/71  

---

Bulk create user accounts by importing a user list. Use the provided template to create the list.

**Batch Import Users**

1. Navigate to **[Control Panel > User Management > User > Add > Import].**
2. **Download the template**, open it with Excel, and enter the following user information in the corresponding cells of the same row as the template.

   * **Username**: Account name for UGOS Pro, unmodifiable after import (supports multilingual).
   * **Password**: No complexity requirements, option to require password change upon first login.
   * **Description**: Additional user information.
   * **Email:** Enter correctly formatted email addresses.
   * **Role (admin/users)**: Choose between admin (with system management rights) and users. Each user has one role.
   * **User Group**: Enter group names. If groups don't exist, create them first in "**User Groups**." Use commas "," to separate multiple groups.

![](https://pro-help.ugnas.com/ugreen-pro/admin/article/1708671238549/8d1ef19e887e5ec6525d6941311039fd63022b37ba7f48a280a674f76596e278.png)

**Notes:**

* Repeat for each user to be created.
* Save the Excel template as .xlsx.
* Username, password, and role are required; others are optional.
* See the example Excel sheet below. The header row is for illustration and should not be included in the actual file.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250221/dd284ac2-b556-423a-b97d-97479c8152a4.png)

3. Click "**Browse**" to select the Excel file, then "**Next**" to preview import details. Accounts with duplicate names or errors will not import. Edit the file, save, and reselect.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250221/975d0fea-870f-457b-a362-32719708f938.png)

4.(Optional) Check "**Force Password Change on First Login**" to compel imported users to change their passwords upon initial login, adding an extra layer of security to imported accounts.

5.Click "**Confirm Import**" to complete the user account import process.

![](https://pro-help.ugnas.com/ugreen-pro/admin/article/1708671251901/6b106bad6b63dab8fda10eda28c9ea06ea8724f7073a6c72265690a5d8a8b180.png)

## **Notes**

1.When adding users to groups, their permissions for shared folders, applications, and services are inherited from the group's permissions. In case of conflicts, the priority is: Forbidden Access > Read-Write > Read-Only for shared folders, and the smallest quota is taken for space usage limits. For application services, Deny > Allow.

2.If a regular user is not added to any user group, they will have no access to shared folders, denied access to applications, allowed access to internal services (like UGOS Pro, SMB, etc.), and no system management permissions. Authorize accordingly after user import if needed.
