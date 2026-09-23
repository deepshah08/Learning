# Beginner's Guide

> **Article ID**: `287`  
> **Category**: `Application Guide > UGOS Pro > Beginner's Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/287  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client, Web Browser

**Applicable Version**: UGOS Pro 1.18.0.0076 or later

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

# First Startup and System Login

Welcome to the UGOS Pro system! To help you complete the initial setup smoothly, this beginner’s guide provides detailed instructions for quickly completing basic operations, including **device initialization**, **enabling UGREENlink remote access**, and **following the new device setup tasks**.

## Add a NAS Device

You can add and register a NAS device through a web browser or the UGREEN NAS app.

**Add a Device via Web Browser**

1. Open a web browser and visit: <find.ugnas.com>. The system will automatically search for and display available devices on your current LAN.

2. Find your device and click "**Connection**" to start the device registration process.

![](https://file-us.ugreennas.com/admin/article/2026-08-13/62299c51ce374632971456f0ab09d211.webp)

**Add a Device via the UGREEN NAS App**

1. Visit the UGREEN NAS official website and go to the [Download Center](https://ai.ugreen.com/pages/downloads) to download and install the UGREEN NAS app client compatible with your device model.

2. Open the UGREEN NAS app. On the login page, click "**More Connections**" or "**New device registration**". The system will automatically search for and display available devices on your current LAN.

![](https://file-us.ugreennas.com/admin/article/2026-08-13/994fd8fd3a51492ea870dc11187643a5.webp)

3. Find your device and click "**Connection**" to start the device registration process.

**Note**:

● Make sure the NAS device is powered on and connected to the router via an Ethernet cable. The computer and NAS must be connected to the same LAN.

● If no device is found, refer to the document "[What to Do If "No Device Found" Appears During Registration or Scanning?](https://support.ugnas.com/knowledgecenter/detail/article/en-US/581?id=1738&type=tag002&clientType=PC) " for troubleshooting.

## Device Initialization Setup

In the initialization setup wizard, complete the following steps:

1. Set a device name that is easy to identify and remember. After reading the "User Agreement" and "Privacy Policy", select "**I have read and accept the User Agreement**"and "**Participate in the Device Analysis Improvement Program (Optional)**", then click "**Next**".

2. Create the first administrator account and password for the device, then click "**Next**".

**Notes**:

● Keep your administrator password secure and avoid using simple passwords.

● To protect your device security, it is recommended to set a strong password: at least 8 characters, including uppercase and lowercase letters, numbers, and special characters.

3. Enter the phone number to be bound and verify it with the verification code to complete the binding (used to enable UGREENlink remote access), then click "**Next**".

**Notes**:

● **Users in Hong Kong, Macao, Taiwan, and overseas regions**: You need to verify your email address to complete UGREEN account binding.

● **Skipping Account Binding**: If you do not want to register a UGREEN account or enable UGREENlink remote access for now, you can skip this step. You can enable UGREENlink and configure your account at any time later in Control Panel "**Device connection**".

● During initialization, do not disconnect the power supply or interrupt the network connection.

4. Select the system update method, then click "**Initialize**".

## View Desktop and Feature Guide

After completing device initialization, enter the UGOS Pro system interface for the first time and click "**Start**" to learn about the core features of your UGREEN NAS.

After completing the guide, proceed with the new device setup tasks.

# New Device Setup Tasks

## Create a Volume

To store installed application data and personal files on your UGREEN NAS, you need to create a storage pool, a volume, and the corresponding folders. After completing the setup, you can use the related features normally. When using the device for the first time, you can create a Volume in either of the following ways:

**Note**: To create a storage pool, at least one unused hard drive with a healthy status is required.

**Method 1: Create Using the On-Screen Wizard**

● After logging in to the UGOS Pro system for the first time and completing the desktop guide, click "**Go**".

● On the Storage Manager details page, learn about the main features of Storage Manager, then click "**Next**".

● Click "**Start creating**" to start creating a storage pool and Volume.

**Method 2: Create Directly from the** "**Storage**" **App**

● On the UGOS Pro desktop, find and open the "**Storage**" app. Select "**Storage**" > **Storage Pool & Volume**, then click "**Create**" to start creating a storage pool and Volume.

**Procedure**

1. Select the "**Hard Drive**" to be used for the storage pool and select the "**RAID type**", then click "**Next**".

**Notes**:

● For single-bay devices, Basic is recommended. For 2-bay devices, RAID 1 is recommended for better data protection. For 4-bay devices, RAID 5 is recommended. For 6-bay devices, RAID 5 or RAID 6 is recommended.

● A storage pool is a collection of one or more Hard Drives that can be protected using RAID. Different RAID types provide different levels of data protection and features. If you are unsure which RAID type to choose, refer to "[How to Choose the Right RAID Level for Your Needs](https://support.ugnas.com/knowledgecenter/detail/article/en-US/132)".

2. Enter the "**Allocated capacity**", select the "**File system**", and click "**Next**".

3. Click "**Create**" to start creating the Storage Pool & Volume.

4. Click "**Delete All Data**" to format the Hard Drive.

5. Enter the current administrator account password and click "**Confirm**" to complete the creation of the Storage Pool & Volume.

## Create a Personal Folder

After creating a Volume, you can create your first folder and upload files to your NAS.

**Procedure**

1. In the new device setup task card, select "**Create**"to create your first folder.

2. After learning the differences between Personal Folder, Shared Folder, and User Folder, click "**Start**".

3. After following the on-screen guide to learn the main features of the "**Files**" app, click "**Enable**" to create a Personal Folder.

4. On the "**Personal Folder management**" settings page, select a Volume as the "**Storage location**" for the Personal Folder. Choose whether to enable self-management permissions and set the Volume usage limit as needed, then click "**Confirm**" to apply the settings.

**Note**: After enabling Personal Folder, administrator users can also create Shared Folders and configure folder access permissions as needed.

## Enable UGREENlink Remote Access

UGREENlink is a remote access feature for UGREEN NAS that allows users to access their NAS devices anytime and anywhere through mobile devices, computers, or web browsers. After enabling this service, you can remotely manage your NAS and access files without requiring a public IP address.

**Note**: You must register a UGREEN account before enabling UGREENlink remote access. For details, refer to "[Manage Local Account and UGREEN Account](https://support.ugnas.com/knowledgecenter/detail/article/en-US/872)".

**Procedure**

#### If a UGREEN Account Has Already Been Bound

1. If a UGREEN account was bound during system initialization, UGREENlink remote access is enabled by default. In the new device setup task card, click "**Go**" to open the UGREENlink remote access page.

2. After learning about the definition and usage of UGREENlink remote access, click "**OK**".

#### If a UGREEN Account Has Not Been Bound

1. If a UGREEN account has not been bound, first learn about the definition and usage of UGREENlink remote access, then click "**Enable**".

2. On the "**Remote Access**" page, learn how to enable UGREENlink remote access, then click "**OK**".

3. Select "**UGREENlink remote access**". The system will display an enable notification. Click "**Confirm**".

4. You can choose to sign in to your UGREEN account using a password or SMS verification. Read and agree to the "User Agreement" and "Privacy Policy", then click "**Verify & Bind**".

**Note**:

● Users in Hong Kong, Macao, Taiwan, and overseas regions need to verify their email address to complete UGREEN account binding.

● If you do not have an account yet, click "**Register now**" to create one first.

5. After successful login, enter a custom ID in the UGREENlink ID field and click "**Apply**" to save. The UGREENlink remote access setup is now complete.

**Note**: The UGREENlink ID must be a unique and easy-to-remember string, such as 1234.

6. After the UGREENlink ID is verified, the system will generate a web access link and a client ID. You can use the web link for remote login or enter the UGREENlink ID in the client to log in.

After completing the new device setup tasks, you can start using your NAS at any time. You can continue adding family members or team members as needed, and customize your NAS interface settings.

## Related Links

● [The relationship between physical disks, storage pool, and storage space](https://support.ugnas.com/knowledgecenter/detail/article/en-US/418?clientType=PC)

● [How to Choose the Right RAID Level for Your Needs](https://support.ugnas.com/knowledgecenter/detail/article/en-US/132?clientType=COMMON)

###
