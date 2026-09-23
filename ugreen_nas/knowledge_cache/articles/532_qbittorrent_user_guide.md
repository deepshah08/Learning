# qBittorrent User Guide

> **Article ID**: `532`  
> **Category**: `Application Guide > Docker > Container Application > qBittorrent User Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/532  

---

## App Overview

qBittorrent is an open-source BitTorrent client that allows users to manage BT download tasks on the device. It supports magnet links, torrent downloads, parallel tasks, speed limits, queue management, and more.

### Default Login Information

After installation, use the following information to log in to qBittorrent:

● Default Username: `admin`

● Default Password: `adminadmin`

### Default Ports

qBittorrent uses the following ports by default:

Web Management Page: 8888

TCP/UDP Forwarding Port: 6888

**Note**: Do not modify the Web management port. Changing the port will prevent administrators from accessing qBittorrent by clicking the app icon.

## Install qBittorrent

1. Open "**App Center**" and find the "**qBittorrent**" app.

2. Click "**Install**", set the resource download path, and click "**Install**".

After installation, click the "**qBittorrent**" icon to open the app.

## Access the qBittorrent Web Page

After the app is installed, you can access the qBittorrent page using the following methods.

### Method 1: Access via the App Icon

Administrators can click the "**qBittorrent**" app icon, and the system will redirect to the login page.

### Method 2: Access via LAN

Administrators and standard users can access qBittorrent through a browser on the LAN.

Enter `http://Device-IP:8888` in the browser.

Example: `http://172.17.70.86:8888`

Device-IP is the LAN IP address of the current device, and `8888` is the qBittorrent Web management port.

### Method 3: Remote Access via the Firefox App

Administrators can remotely access qBittorrent through the Firefox app installed on the device.

1. Log in to the device with **UGREENlink ID**.

2. Open the **Firefox** app on the device and verify the Firefox login password as prompted.

3. After logging in to Firefox, enter `http://Device-IP:8888` in the browser.

## Initial Configuration

When using qBittorrent for the first time, complete the initial configuration.

### Change Language

To change the qBittorrent interface language, adjust it in Options.

1. Click the gear icon at the top to open "**Options**".

2. Find "**Language**" on the "**Behavior**" page.

3. Select **"English"** and click **"Save"**.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/6c78a05ea66146aba0b8d8d208c9ceb0.webp)

### Change the Default Username and Password

After the first login, it is recommended to change the default username and password.

1. Click the gear icon at the top to open "**Options**".

2. Go to the "**WebUI**" page and change the username and password under "**Security**".

3. Click "**Save**" at the bottom.

After the changes are saved, use the new username and password the next time you log in.

### Configure the Listening Port

qBittorrent uses `6881` as its default listening port. UGOS Pro has changed the default port to `6888`.

To change the listening port:

1. Find **Listening Port** on the "**Connection**" page in Options.

2. Change the port and click **"Save"**.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/cfe339d6de744698805899ddcda9e7fb.webp)

### Configure WebUI Security Settings

In some cases, when accessing qBittorrent remotely through network tunneling or similar methods, an `Unauthorized` error may appear.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/ee6b8627d0bc4bd6be13a5b284af0561.webp)

You can adjust the settings as follows:

1. Open qBittorrent Options and go to the "**WebUI**" page.

2. Under "**Validation**" or "**Security**" on the WebUI page, disable the following options:

● **Enable clickjacking protection**

● **Enable Cross-Site Request Forgery (CSRF) protection**

● **Enable Host header validation**

![](https://file-us.ugreennas.com/admin/article/2026-09-18/aa4657834bac45d78ba8a1e1600bcbf5.webp)

3. After making the changes, click **"Save"**.

## Add Download Tasks

qBittorrent supports the following methods for adding download tasks.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/dfd7e34bec0d40cbb44ba7427e34aad2.webp)

### Add a Magnet-Link

1. Click "**Add Torrent Link**" in the toolbar.

2. Enter the magnet link and click "**Confirm**".

### Upload a Torrent File

1. Click "**Add Torrent File**" in the toolbar.

2. Select a local torrent file.

3. Start the download.

## FAQs

### Q: Why Is My Torrent Download Not Showing Any Speed?

BT download speed depends on the torrent itself and seed availability. Common reasons for slow downloads include:

● The torrent does not have enough seeders.

● Only a small number of seeders are currently connected.

● The torrent was released a long time ago and has fewer active users.

Even if seeders are shown, the download speed may still be slow if only a small number of them are actually connected.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/dc2d3043273641a18ef722a48540c45e.webp)

### Q: What Should I Do If I Forget My qBittorrent Login Password?

If you forget the qBittorrent login password, you need to reinstall the qBittorrent app.

App data will not be retained after reinstallation. You will need to configure the account again, and previously added download tasks will not be retained.

## Notes

● After the first login, it is recommended to change the default username and password promptly.

● Changing the Web management port may prevent the app icon from redirecting properly.

● Make sure the download directory has sufficient storage space to avoid download task failures.

● If the downloaded content is copyrighted, make sure it comes from a legal source.

● Before deleting the app, check whether you need to retain existing configurations and download tasks.

# 英文标题：Quick Start Guide for qBittorrent

## Application Overview

qBittorrent is a powerful open-source BitTorrent client that supports magnet links, torrent downloads, parallel tasking, speed limits, queue management, and more. It is an excellent solution for efficiently managing BT download tasks on a NAS.

**Default Login Information:**

● **Default Username:** `admin`

● **Default Password:** `adminadmin`

**Default Ports:**

● **Web Access Port:** `8888`

● **TCP/UDP Forwarding Port:** `6888`

In the local network, you can access the qBittorrent Web management interface by entering `NAS_IP:8888` (e.g., `172.17.20.102:8888`) in your browser's address bar.

**Note**: Do not modify the WebUI port. Changing the port will result in the failure of the administrator's shortcut for accessing qBittorrent by clicking its application icon.

● **Developer Link:** [GitHub Project Address](https://github.com/userdocs/qbittorrent-nox-static)

## Installation Guide

Follow these steps to install the qBittorrent application on the **UGOS Pro** system:

**1. Install the Application**

● Open the **App Center**, locate the qBittorrent application, and click **"Install"**.

● By default, container applications are installed on **Storage Space 1**. If necessary, you can select a different storage space during installation. It is recommended to designate a dedicated storage space for long-term use to efficiently manage resources and downloaded files.

**2. Set the Download Directory**

● During the installation process, you need to configure the resource download directory for qBittorrent. All files downloaded via the application will be stored in this directory.

● It is recommended to select a storage space with sufficient capacity to avoid occupying storage reserved for other tasks, which could affect system performance.

## Access qBittorrent

On the **UGOS Pro** system, both administrators and regular users can access the qBittorrent application using the following methods:

### Method 1: Via Application Center (Administrator Only)

1. Open the **App Center** in the UGOS Pro system.

2. Locate and click the **qBittorrent** application icon. The system will redirect to the login interface.

### Method 2: Access via Local Network (Administrators and Regular Users)

Within the local network, both administrators and regular users can access qBittorrent by using the NAS IP address with port `8888`. For example, enter`192.168.22.158:8888` in the browser.

### Method 3: Access via Firefox in Non-Local Network (Administrator Only)

Administrators can access container applications outside the local network using the following method:

1. In a non-local network environment, the system might display a prompt: **"Please connect to the device via IP in the local network before opening."** This can be resolved using the Firefox browser. Firefox supports using **UGREEN Link** to log in to the NAS in non-local network environments.

2. Once logged into Firefox, administrators and regular users can access qBittorrent by entering the NAS IP address with port **8888**. For example, enter`192.168.22.158:8888` in the browser.

**Note:** When logging in on untrusted devices, promptly clear your browser's history to ensure data security.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/1a6f25c46e2b4e3da9c75dcc3d270496.webp)

### Usage Tips

1. Use a browser with strong compatibility, such as Chrome or Edge, for optimal performance when accessing qBittorrent on a local network.

2. Ensure data security when accessing the NAS in public networks to prevent leaks of sensitive information.

3. Administrators should safeguard access passwords to maintain confidentiality.

4. If Firefox is shared among multiple users for accessing container applications, disable the auto-save password feature and clear browser history regularly.

### Logging into qBittorrent

1. On the Web login interface, enter the default **username**: `admin` and **password**: `adminadmin`.

2. **For security purposes, it is recommended to change the default username and password immediately after the first login.** **(Refer to the** "**Changing Username and Password**" **section for detailed steps.**)

**Note:** If you forget the login password, you must reinstall the qBittorrent application. Please be aware that reinstalling the application will result in the loss of application data. You will need to reconfigure settings and re-add tasks.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/7925155c399840cebbaecf3df1ffe94d.webp)

## Configuration Settings

Before using qBittorrent, complete the necessary initialization settings.

### 1 Change Username and Password

To ensure security, modify the default username and password immediately after the first login:

1. Click the **"Options"** button in the top-right corner to open the settings page.

2. Under the **WebUI** section, scroll down to find the **Authentication** settings.

3. Set a new username and password.

4. After completing the changes, click **"Save"** at the bottom of the page.

The new username and password will be required for future logins.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/aca4c34ac5584f398041c32ebfc5c7db.webp)

### 2 Configure the Listening Port

● By default, qBittorrent uses port `6881`, but this port may result in slower download speeds for certain torrents. On **UGOS Pro**, the default port has been changed to `6888` for better performance.

● If you wish to use a different port:

○ Navigate to the **Connection** page.

○ Modify the **Listening Port**.

○ Click **"Save"** to apply the changes.

The new port settings will take effect immediately after saving.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/1e9862dd476f4791a4028b6720548894.webp)

qBittorrent supports multiple methods to add download tasks:

#### 1. Add Magnet Links

● Click the **"Add Torrent Link"** icon in the toolbar.

● Enter the magnet link in the dialog box that appears.

● Click **"Download"** to start the download.

#### 2. Upload Torrent Files

● Click the **"Add Torrent File"** icon in the toolbar.

● Select a local torrent file to upload.

● Once uploaded, the download will begin automatically.

|  |  |  |
| --- | --- | --- |
| **Number** | **Name** | **Operation** |
| 1 | Add Torrent Link | To download by entering the magnet link |
| 2 | Add Torrent File | To download by uploading torrent files |

![](https://file-us.ugreennas.com/admin/article/2026-09-18/8bc471602c2c4fcb9be561383b26a0b6.webp)

After adding the task, you can see the resource is downloading.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/ab045169e39e42f1a84d0b63612141f5.webp)

## Notes

When using the **UGOS Pro** system and container applications, please pay attention to the following to ensure proper system and application functionality:

#### 1. Avoid Modifying NAS Paths

Do not arbitrarily migrate, move, rename, or delete NAS paths mounted by container applications, as this may result in application malfunctions or data loss.

#### 2. Prevent Abnormal Access States

When accessing the NAS via Firefox, avoid repeated operations such as "Open NAS > Open Firefox > Reopen NAS" to prevent the system from entering an abnormal access state.

#### 3. Disable Multiple Gateways

If accessing container applications through a browser, disable the **Multiple Gateways** option under **Control Panel > Network** to prevent network conflicts.

#### 4. Recommended for Beginner Users

Container applications are suitable for beginner users. For more flexible configuration file management, consider deploying directly via Docker. Refer to **[Docker Usage: Setting Up QBittorrent Downloader on UGREEN NAS]**.

#### 5. Advanced Configuration with Docker

For greater flexibility in configuration and management, it is recommended to deploy qBittorrent using Docker. This allows for customized configuration files and access to advanced functionality.
