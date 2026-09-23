# How to Remotely Access UGREEN NAS via UGREENlink Without Public IP?

> **Article ID**: `454`  
> **Category**: `Application Guide > Control Panel > FAQ > How to Remotely Access UGREEN NAS via UGREENlink Without Public IP?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/454  

---

UGREENlink is a proprietary remote access service of the UGREEN UGOS Pro system, providing a secure and efficient way to connect remotely and allowing you to conveniently manage and access your UGREEN NAS devices. With this service, you can create a unique UGREENlink ID for your device to enable quick remote access.

## Steps to enable UGREENlink service

1. After logging in to the UGOS Pro system, go to [Control Panel] > [Device Connection] > [Remote Access].

2. Tick the **"Enable UGREENlink remote access"** option. Note: If you haven't registered a UGREEN NAS account, please click the "Register Now" link to sign up.![](https://file-us.ugreennas.com/admin/article/2025-09-01/cb0986be6b434d159dd0cf0c958ec3a1.webp)

3. Enter an ID you wish to use (e.g., ugreen) in the UGREENlink ID field and click "Apply". Note: It is recommended to use an easy-to-remember string for your ID. If the ID you set is already taken, the system will prompt you to re-enter one to avoid conflicts with other users' IDs.

4. After successfully creating your UGREENlink ID, the page will display the addresses for remote access to the UGOS Pro web and client ends.

![](https://file-us.ugreennas.com/admin/article/2025-09-01/331edb30c80446fcba722b6e7dc71dea.webp)

**Notes:**

1. To use the UGREENlink service, you must first register or log in to your UGREEN NAS account.

2. After enabling UGREENlink, you can remotely access your NAS via the internet without complex port forwarding settings.

3. UGREENlink will automatically generate a unique subdomain corresponding to your UGREENlink ID for your NAS device and configure an SSL certificate for it to ensure secure access.

## FAQs

### Q1: How do I change the phone number associated with my UGREENlink?

A1: To change the admin phone number associated with your UGREENlink, follow these steps:

1. Open <https://web.ugnas.com/account/login>in your browser and log in with the UGREENlink phone account you want to unbind.

2. Find the device you need to unbind and perform the unbind operation. Note: After unbinding, UGREENlink cannot connect to the NAS device anymore, so it is recommended to operate within a local area network.![](https://file-us.ugreennas.com/admin/article/2025-09-01/1e49854d170c456ba06a2fced2308e61.webp)

3. Log in to the device, go to [Control Panel] > [Device Connection] > [Remote access], uncheck the UGREENlink Remote Access Service, then recheck it, and the system will prompt you to bind a new phone number.

### Q2: What is the difference between enabling UGREENlink and using DDNS?

A2: The UGREENlink service is designed to allow you to easily access your home NAS device via the internet regardless of your location, enabling seamless data connection and remote management. With UGREENlink enabled, you can easily access your NAS device on your phone or computer. DDNS (Dynamic Domain Name System) service allows you to access your NAS device from anywhere by mapping a dynamic IP address to a fixed domain name. For more details, please refer to [What’s the difference between UGREENlink and DDNS?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjoxMDk3LCJhcnRpY2xlSW5mb0lkIjozNzMsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==) .
