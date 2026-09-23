# Enable Network Hostname Resolution Sharing

> **Article ID**: `352`  
> **Category**: `Application Guide > Control Panel > File Service > Enable Network Hostname Resolution Sharing`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/352  

---

By enabling network hostname resolution sharing, devices on the local network can mount the SMB service of the UGOS Pro device using its device name instead of its IP address. Below are the steps to enable hostname resolution sharing on Windows and macOS systems:

---

### **Windows**

On Windows, hostname resolution sharing can be achieved through NetBIOS, LLMNR, and the hosts file.

#### **Enable NetBIOS over TCP/IP**

1. **Open Network Connection Settings:**

   * Right-click the network icon in the taskbar and select [Open Network and Sharing Center].
   * Alternatively, go to [Control Panel] > [Network and Internet] > [Network and Sharing Center].
2. **Change Adapter Settings:**

   * Click "Change adapter settings" on the left sidebar.
3. **Open Network Connection Properties:**

   * Locate your network connection (e.g., “Ethernet” or “Wireless Network Connection”), right-click it, and select "Properties".
4. **Internet Protocol Version 4 (TCP/IPv4):**

   * Double-click "Internet Protocol Version 4 (TCP/IPv4)".
5. **Advanced Settings:**

   * In the TCP/IPv4 properties window, click "Advanced".
6. **WINS：**

   * In the "Advanced TCP/IP Settings" window, go to the "WINS" tab.
   * Select "Enable NetBIOS over TCP/IP".

#### **Enable LLMNR**

1. **Open the Local Group Policy Editor:**

   * Press `Win + R` to open the Run dialog, enter `gpedit.msc`, and press Enter.
2. **Navigate to:**

   * Computer Configuration > Administrative Templates > Network > DNS Client
3. **Find “Turn On/Off Multicast Name Resolution”:**

   * Make sure the setting is set to "Not Configured" or "Enabled".

### **macOS**

macOS uses Bonjour (zero-configuration networking) for hostname resolution. This feature is typically enabled by default.

#### **Ensure Bonjour Service is Running**

Bonjour is a built-in service on macOS and does not require manual activation. You can reset your network settings to ensure it is functioning properly:

1. **Open System Preferences:**

   * Click the Apple menu and select "System Preferences".
2. **Network:**

   * Select "Network".
3. **Choose Your Network Interface:**

   * Select the network interface you are currently using (e.g., "Wi-Fi" or "Ethernet"), then click "Advanced".
4. **TCP/IP：**

   * Under the "TCP/IP" tab, ensure that DHCP is being used.
5. **DNS：**

   * Under the "DNS" tab, make sure a valid DNS server is configured.

### **Manually Configure the Hosts File**

On all operating systems, you can also manually configure hostname resolution by editing the [hosts] file.

#### **Windows**

1. **Open the [hosts] file:**

   * Open Notepad with administrator privileges and open the file: `C:\Windows\System32\drivers\etc\hosts`。
2. **Add an entry:**

   * Add a line such as:

```
192.168.1.100   nas
```

3. **Save and close the file.**

#### **macOS**

1. **Open the [hosts] file:**

   * Open the file `/etc/hosts` with root privileges.
   * Run the following command in the terminal:

```
sudo nano /etc/hosts
```

2. **Add an entry:**

   * Add a line such as:

```
192.168.1.100   nas
```

3. **Save and close the file:**

   * In [nano], press `Ctrl + O` to save, then press  `Ctrl + X`to exit.

By following these steps, you can enable and configure hostname resolution sharing across different operating systems, making it easier to access the SMB service on UGOS Pro within your local network.
