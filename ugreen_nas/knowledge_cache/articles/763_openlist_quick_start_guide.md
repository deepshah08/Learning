# OpenList Quick Start Guide

> **Article ID**: `763`  
> **Category**: `Application Guide > Docker > Container Application > OpenList Quick Start Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/763  

---

**Applicable Version:** UGOS Pro firmware **1.9.0.0062** and later

**Applicable Model: DXP Series**

**Note:** The screenshots and interfaces in this document are for reference only. The actual display may vary depending on the system or application version. Some features may be adjusted in different versions. Please refer to your actual interface for accuracy.

## Application Overview

OpenList is an open-source fork of the original AList project, aiming to replace AList and provide a more reliable, transparent, and sustainable solution.

It supports multiple cloud drives and storage services, including local storage, Aliyun Drive, Baidu Netdisk, OneDrive, Google Drive, etc.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/2d25eb18bf504ddbb4f2d427e50b6cae.webp)

## Install the Application

1. Open **[App Center]**, find **OpenList** in the application list, and click "**Install"** to enter the installation wizard.

2. Set the resource access path (you can mount NAS folders to OpenList).

3. Follow the wizard step by step to complete the installation settings.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/07c03b99e2ac47028af0696ff8e9e6fe.webp)

# User Guide

## Initial Configuration

1. After installation, open the OpenList, or open a browser in the LAN and visit `http://<NAS_IP>:5445`, replacing `<NAS_IP>` with the actual IP address of the NAS.

The NAS IP can be found in **[Control Panel] > [Network] > [Network connection]**.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/669ab0b1cd24425fa53400adfbd04389.webp)

2. Use the default account **admin** and password **admin** to log in to OpenList.

After the first login, it is recommended to change the username and password immediately.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/2b0028a20c524b66adf58a78099b5c28.webp)

3. Click the "**Manage"** button at the bottom of the page to enter the management page.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/d1a884bf4ca242b2a98391fecf645834.webp)

4. In "**Profile"**, change the username and password, and click "**Save"** to update.

After modification, you need to log in again with the new username and password.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/7dbb38b5cc0041f6a32de88ca1a34197.webp)

**Note:** If you forget the login password, you need to reinstall the OpenList application. Reinstallation will clear all application data, and you will need to reconfigure storages and mount path tasks.

## Add Local Storage

OpenList supports mounting the resource access path set during installation.

1. On the OpenList manage page, click **[Storages]** > **[Add]**.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/39c89515c85040f592c67cbb15017873.webp)

2. Select "**Local"** as the driver type, and fill in the **Mount Path**.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/0057ff8c93844db09a496b4e77383d1c.webp)

The mount path can be viewed and copied in **[App Center] > [OpenList ]> [Configuration]**.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/20882ddaf80b421abfc3da94b8878156.webp)

3. Scroll down to the bottom of the page and click "**Add"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/46a39f45c7174fdd9565f3ccadfc5ecc.webp)

After returning to the homepage, you can see the newly mounted local directory.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/7785610ffe31442c87d5b0fb2c82bdfe.webp)

## Add Aliyun Drive to OpenList

### Get a Token

1. Open [api.oplist.org](https://api.oplist.org/) , and in the dropdown menu select **"Scan the code Aliyun drive (OAuth2) to log in"**.

2. Check **"Use the parameters provide by** OpenList**"**, and click **"Get a Token"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/8682207f562042d59764bc17a0b3c111.webp)

3. In the popup window, scan the QR code with your mobile phone to log in to Aliyun Drive.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/0dc01fe5419a4b3798d6b29e02a22568.webp)

4. After authorization succeeds, the page will display the **Access Token** and **Refresh Token**. Please copy and keep both tokens safely.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/5ad9186d57e441329967683ddc82f6d0.webp)

### Add the Aliyun Drive

1. On the OpenList manage page, click **[Storages] > [Add]**.

2. Select the driver type "**AliyundriveOpen"**.

3. Enter the mount path. After mounting, files from Aliyun Drive will be stored in this path. You can customize the path, for example: `aliyun-drive`.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/932ec28bf3214931a0d6b5b873e0b32a.webp)

4. Enter the **Refresh Token** obtained in the previous step.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/0189b68f4f43428b84b89e61facede20.webp)

5. Enable "**Use online api"**. Keep `Client id`and `Client secret` empty, and set the removal method to "**Trash"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/5fab4cd34d4e40359bebdcb2541a1431.webp)

6. Click "**Add"** to complete the Aliyun Drive storage mounting.

## Add Google Drive to OpenList

### Prerequisites

Before mounting Google Drive, please make sure the following conditions are met:

● The NAS running the OpenList service must be able to access Google Drive normally.

● [Google Drive API service](https://doc.oplist.org/guide/drivers/google_drive#21-%E5%90%AF%E7%94%A8-google-drive-api-%E7%9A%84-api) has been enabled (for details, please refer to [Google Workspace > Google Drive > Quick Start Guide](https://developers.google.com/workspace/drive/api/quickstart/js) ).

## Enable Google Drive API

1. Go to the [Google Drive API management page](https://console.cloud.google.com/apis/library/drive.googleapis.com?project=peak-comfort-473208-e4) , click "**Enable"**, and wait until it is completed.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/6767f134d3c7401ab3e852d60ed0cd3d.webp)

2. After enabling, the page will automatically redirect to the Google Drive API page and show that the API has been enabled.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/e53306fa534049d0864f07197b894557.webp)

### Create a Google Auth Platform App

1. Click "**OAuth consent screen"** to enter the Google Auth Platform page.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/3368681f7f4844da823e04734adf22a0.webp)

2. Click "**Get started"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/8d20e6e48fc148fb956fb64e4fb50da4.webp)

3. On the application information page:

● APP name: enter `openlist`

● User support email: select the email address currently logged into Google Drive

● Click "**Next"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/1f8a024e918f463ebb03945621dadcd1.webp)

4. Under audience, select "**External"**, then click "**Next"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/707859b1b2f540069083366c91f13f5c.webp)

5. Fill in the contact Information email address, then click "**Next"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/3bcb56dda5fa468d99bc999ae21a3b79.webp)

6. Check "**I agree"**, then click "**Create"** to finish.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/aba26039c60541e393868ae97ea75367.webp)

### Create OAuth Client

1. On the [Credentials](https://console.cloud.google.com/apis/credentials?hl=zh-cn) page, click **"Create credentials" > "OAuth client ID"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/329007dadf0245f2b25d2029f528d82f.webp)

2. In the pop-up window:

● Select **Web application** as the application type

● APP name: enter `openlist`

● Under **Authorized redirect URIs**, add:

```
https://api.oplist.org/googleui/callback
```

![](https://file-us.ugreennas.com/admin/article/2025-09-28/862e4ec230b34c7789e5d9fb50dce331.webp)

● Click "**Create"**.

3. The system will generate the **Client ID** and **Client secret**. Please copy and save them.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/6bb3d30dca4f4d7cab3695fc61392b8a.webp)

4. In the left menu, select "**Audience"**, then click "**+ Add users"** to add test users. Enter your Google account email address in the pop-up window and press Enter to add. Then click "**Save"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/64ea1f05d65d441dbae6947c006320ee.webp)

5. After adding test users, click the "**Publish app"** button under **Publishing status**. Then click "**Confirm"** to complete publishing.

### Get Refresh Token

1. Open the [OpenList Google authorization page](https://api.oplist.org/) , select "**GoogleDrive Login (OAuth2)"** from the dropdown, enter the previously saved **OAuth client ID** and **Client secret**, then click "**Get a token"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/94b75b74a6f14e18a965d9d1eba346fe.webp)

2. The system will redirect to the Google authorization page. Log in with your Google account.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/530cca8932b2473198092d430662bf4a.webp)

3. Click "**Advanced"**, then click "**Go to oplist.org (not secure)"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/81e9eca46deb4d498dfc6157e1fe9e3b.webp)

4. Click **"Go on"**.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/490b79f922884d458a3e038b23108677.webp)

5. After authorization, the system will return a **Refresh Token** and an **Access Token**. Please copy and save the refresh token, which will be required for later configuration.

![](https://file-us.ugreennas.com/admin/article/2025-09-28/bfc66d76acb74895b564ea27055b6bde.webp)

### Add Google Drive

1. Log in to the OpenList manage page, click [Storages] > [Add].

2. Select "**Google Drive"** as the driver, and fill in the following information:

● **Mount Path**: enter `/google` (path can be customized)

![](https://file-us.ugreennas.com/admin/article/2025-09-28/2caaefc241db415fa0bb85dd775bd19c.webp)

● Root folder id: enter `root`

● Refresh token: enter the Refresh Token obtained in the previous step

● Uncheck "**Use online api"**

● **Client id**: enter the OAuth client ID

● **Client secret**: enter the OAuth client secret

![](https://file-us.ugreennas.com/admin/article/2025-09-28/5c8ddfb42f814badbe01ae2e6468d6ee.webp)

3. Click "**Add"** to complete the mount.

Once mounted successfully, Google Drive files will appear under the `/google` path.

## Add Other Cloud Drives

OpenList also supports mounting the following common cloud drives:

● **Quark Drive**

● **189Cloud**

● **Baidu Netdisk**

For detailed mounting steps, please refer to the [official OpenList documentation](https://doc.oplist.org/guide/drivers/189) .

## Notes

When using the UGOS Pro system and container applications, please pay attention to the following:

1. Do not arbitrarily migrate, move, rename, or delete the NAS paths mounted by containers, otherwise it may cause malfunction or data loss.

2. When accessing container applications via a browser, please disable **"multiple gateway"** in **[Control Panel]** > **[Network]** to avoid network conflicts.

3. Container applications are suitable for quick use by beginners. For more flexible storage and access control, it is recommended to use Docker deployment.
