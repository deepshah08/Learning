# How to Set DHCP on a Computer

> **Article ID**: `386`  
> **Category**: `Application Guide > Control Panel > FAQ > How to Set DHCP on a Computer`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/386  

---

DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses, making it easy for devices to connect to the network. Below is a tutorial on how to set up DHCP on Windows and macOS systems.

#### **Setting up DHCP on Windows**

1. Open Network Connections Settings:

   * Press `Win + R` to open the "Run" dialog box.
   * Type `ncpa.cpl`and press Enter to open "Network Connection."
2. Select Network Connection:

   * Find the network connection you are using (such as Ethernet or Wi-Fi).
   * Right-click on the connection and choose “Properties”.
3. Configure IPv4 Settings:

   * In the list under "This connection uses the following items," select "Internet Protocol Version 4 (TCP/IPv4)," then click "Properties."
   * Choose "Obtain an IP address automatically" and "Obtain DNS server address automatically."
   * Click "OK" to save the settings.
4. Configure IPv6 Settings (Optional):

   * If using IPv6, select "Internet Protocol Version 6 (TCP/IPv6)" and click "Properties."
   * Choose "Obtain an IPv6 address automatically" and "Obtain DNS server address automatically."
   * Click "OK" to save the settings.

#### **Set up DHCP on macOS**

1. Open System Preferences:

   * Click the Apple icon in the top-left corner of the screen and select "System Preferences."
2. Enter Network Settings:

   * Select the "Network" icon.
3. Select Network Connection:

   * In the left-hand list, choose the network connection you are using (such as Wi-Fi or Ethernet).
4. Configure DHCP:

   * Click the "Advanced" button.
   * Select the "TCP/IP" tab.
   * From the "Configure IPv4" dropdown menu, select "Using DHCP."
   * Click "OK" to save the settings.
5. Apply Settings:

   * Return to the main Network Settings window and click "Apply" to ensure the changes take effect.

By following these steps, your computer will be able to automatically obtain an IP address and DNS server information via DHCP, simplifying the network configuration process.
