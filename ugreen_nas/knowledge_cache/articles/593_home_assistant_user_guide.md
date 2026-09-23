# Home Assistant User Guide

> **Article ID**: `593`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Home Assistant User Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/593  

---

### App Overview

Home Assistant is an open-source home automation platform. With Home Assistant, you can connect smart home devices on your LAN and configure automated control rules.

The device's "**App Center**" provides the Home Assistant app, which can be installed and deployed directly without manually configuring complex runtime environment.

#### Login Information

The default access port for Home Assistant is: 8123

Local network access address format: `http://device-IP:8123`

Example: `http://172.17.70.86:8123`

### Installation and Access

1. Open "**App Center**" and find the "**Home Assistant**" app.

2. Click "**Install**", select volume, and click "**Next**".

3. Select configuration path and click "**Install App**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/130deb4497bc4100b18b719ca65e5126.webp)

After installation, click the "**Home Assistant**" icon to open the app.

### Access the Home Assistant Web Page

After the app is installed, you can access the Home Assistant page using the following methods.

#### Method 1: Access via the App Icon

Administrators can click the "**Home Assistant**" app icon, and the system will redirect to the login page.

#### Method 2: Access via LAN

Administrators and standard users can access it through browser on the LAN.

Access format: `http://device-IP:8123`

Example: `http://172.17.70.86:8123`

Device-IP is the LAN IP address of the current device.

#### Method 3: Remote Access via the Firefox App

Administrators can remotely access Home Assistant through the Firefox app installed on the device.

1. Log in to the device with `UGREENlink ID`**.**

2. Open the **Firefox** app on the device and verify the Firefox login password as prompted.

3. After logging in to Firefox, enter `http://device-IP:8123` in the browser.

Example: `http://172.17.70.86:8123`.

### Initialize Home Assistant

When using Home Assistant for the first time, complete the initial setup:

1. Click "**CREATE MY SMART HOME**" to start the setup guide.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/dc35d10f114d4b038a3ad1f3347c674a.webp)

2. Create Home Assistant account and follow the on-screen instructions to enter your name, username, and password.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/b5a7f43d4dd94fdd91907de6d6b60fea.webp)

3. Set your home location and click "**NEXT**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/2a3c25cf16e54060a86b6f92487eff7e.webp)

4. Choose whether to enable the relevant features as needed, then click "**NEXT**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/b62b5ce047fe42c7be0d7b063f89c230.webp)

5. Click "**FINISH**" to enter the Home Assistant home page.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/9370fcc92bde4bfb9922f7f0a59c5246.webp)

### Change Language

To change the Home Assistant interface language, adjust it in User Settings.

1. Click the current username and find "**Language**" on the "**General**" page.

2. Select the language you want to use.

After the setting is applied, the interface language will update according to Home Assistant's rules.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/8539ad26b3754fa483acc9a67c85120a.webp)

### Install Plugins and Integrations

Home Assistant can extend smart home capabilities through plugins or integrations. Common options include:

● HACS plugin store

● Official Xiaomi plugin `xiaomi_home`

● Third-party Xiaomi plugin `xiaomi-miot`

● Apple HomeKit

The following sections describe how to configure common plugins and integrations. Third-party plugin versions may change. Refer to the plugin's official page for the latest information.

#### Install the HACS Plugin Store

HACS (Home Assistant Community Store) is Home Assistant's community plugin store for installing, updating, and managing third-party plugins and themes.

1. Go to the HACS [GitHub Releases](https://github.com/hacs/integration/releases) page.

2. Download the latest HACS.zip.

At the time of writing, the latest HACS version is 2.0.5. Download the latest version shown on the actual page.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/c37432aa46b64ebb9ece269a74855e43.webp)

3. Open the "**Files**" app and go to the Home Assistant configuration path.

4. Create the `www` and `custom_components` folders under the configuration path.

`www`: Used to store static resources.

`custom_components` : Used to store plugin files.

The configuration path can be viewed in "**Control Panel**" > "**About**" > "**Apps**" by clicking the app name.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/8cd69bb9f7de4c2bb1fb6cc126a3ba6c.webp)

5. Decompress the downloaded `hacs.zip` file.

6. Upload the decompressed `hacs` folder to the `custom_components` folder.

After the upload is complete, return to the Home Assistant page.

7. Click "**Settings**" > "**···**" > "**Restart Home Assistant**" and wait for the restart to complete.

**Add the HACS Integration**

1. In Home Assistant, click "**Settings > Devices & Services**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/cb692b83373a4cc6a290a12fdeed1192.webp)

2. Click "**Add Integration**", then search for and select "**HACS**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/e5ade8c6446c4e589281984be193598e.webp)

3. Select the options on the page and click "**SUBMIT**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/72de7de26a494eb3b44407e0ca8d35bc.webp)

If `could_not_register` after submission, restart the device and submit again.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/cffee7af3b5d4b49b5649381d07812d7.webp)

**Bind GitHub Account**

1. After adding the HACS integration, copy the code from the pop-up window and click the GitHub address in the pop-up.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/89e8ef33790a4e9da40fc8f785b41c02.webp)

2. Follow the on-screen instructions to log in to or register GitHub account.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/7df2b4cc4f0b4f5bbc3bac82deb6df79.webp)

3. Enter the code and click "**Continue**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/8d66b08c785148f2aa0fb0423837347a.webp)

4. Click "**Authorize hacs**" to complete authorization.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/a1f0b28acacb4195bbd1b6c440d4f36e.webp)

After authorization is successful, the **HACS** entry appears in the Home Assistant sidebar.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/1081df4bdf2a4aa7bf312920de25504b.webp)

#### Install the Official Xiaomi Plugin xiaomi\_home

`xiaomi_home` is the official Home Assistant plugin provided by Xiaomi and can connect Mi Home devices through Xiaomi's official API.

1. Go to the official Xiaomi plugin [GitHub Releases](https://github.com/XiaoMi/ha_xiaomi_home/releases) page and download the latest package.

At the time of writing, `xiaomi_home` version `v0.1.5b2` is the latest. Download the latest version shown on the actual page.

2. After the download is complete, decompress `xiaomi_home.zip` and upload the decompressed folder to `custom_components` under the Home Assistant configuration path.

3. Return to the Home Assistant page, click "**Settings**">"**···**">"**Restart Home Assistant**", and wait for the restart to complete.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/ba500151f8bd4f5494c898e515422d68.webp)

4. After the restart, click "**Settings**" > "**Devices & Services**", select "**Add Integration**", then search for and add `Xiaomi Home`.

5. Follow the on-screen instructions to acknowledge the risk notice, then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/9b0dc641c7254977821f48d36f50e23d.webp)

1. Click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/633daac29e30424eac70406c0bb55a43.webp)

2. Log in to your Xiaomi account.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/4284e6034979494e87d067c2332639b6.webp)

3. Follow the on-screen instructions to select the home whose devices you want to import, then click "**Next**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/0084918a39614638a6a72446be13fcc5.webp)

4. When you can see the home devices, the deployment is successful. Click "**Finish**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/2ddb654fa89841d5bea760d7db3c197e.webp)

If the address on the redirected page after login is `homeassistant.local`, replace `homeassistant.local` in the address bar with the device IP address and access the page again.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/785116ca88bf445c917e0194244581a3.webp)

#### Install the xiaomi-miot Plugin

`xiaomi-miot` is third-party community plugin that connects devices through the Xiaomi MIoT protocol and supports some devices not covered by the official plugin.

1. Open HACS, search for "**Xiaomi Miot Auto**", and download the plugin.

2. After the download is complete, restart Home Assistant.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/b629f8ffcdb5482096dc2c4addfcd259.webp)

3. Click "**Settings > Devices & Services**", then click "**Add Integration**", search for "**xiaomi miot auto**", and select the integration to add it.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/6a9d443bb0fe439da09ca663187d65c4.webp)

4. Select "**Add devices using Mi Account**", then click "**NEXT**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/7548a940f4fc42f89d80be1e58fb5677.webp)

5. Enter your Xiaomi ID and password, select "Automatic", then click "**SUBMIT**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/592b981d8f494d0eb6bf51cc22bdce59.webp)

6. Select the devices to include or exclude as needed, then click "**SUBMIT**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/824b1d7e952143518cf3e1d7fadc8350.webp)

After submission, you can view the added devices on the Home Assistant Overview page.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/2064937ac26f4997a323fe47190a5c95.webp)

#### Install Apple HomeKit

Home Assistant supports Apple HomeKit integration. With the HomeKit integration, you can add devices from Home Assistant to the Apple Home app for control, or add HomeKit devices to Home Assistant for unified management.

To add devices from Home Assistant to the Apple Home app, follow these steps:

1. In Home Assistant, click "**Settings > Devices & Services**", click "**Add Integration**", and search for "**apple**".

2. Click the Apple icon to open the next menu.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/270cb280df5c4d92b95fd2317644abba.webp)

3. Select "**HomeKit Bridge**", choose the domains to include as needed, then click "**SUBMIT**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/2da0e8d4c533412189c76f945922c9e0.webp)

4. On the "**Pair HomeKit**" page, follow the guide and click "**SUBMIT**" > "**FINISH**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/a624a419b7ee468587f2f94fc3e3173b.webp)

5. Click "**Notifications**" in the sidebar, then use the Apple Home app to scan the generated QR code and complete pairing.

After pairing is complete, you can view and control the connected devices in the Apple Home app. ![](https://file-us.ugreennas.com/admin/article/2026-09-15/33298c4ccee343f0a7f8ddf3ed1c0a6c.webp)

### Enable Remote Access for Home Assistant

The device supports exposing container apps as remote access services. Using Home Assistant as an example, once enabled, you can remotely access the Home Assistant management interface through Web browser, PC, or mobile device.

Before use, make sure both the UGOS Pro system firmware and the container app are updated to the latest versions. Older versions do not support this remote access feature.

**Note:**

● Remote access is available only when you log in to the device with UGREENlink ID.

● This feature is unavailable when logging in via DDNS or other methods.

#### Configure Reverse Proxy for Home Assistant

1. Open the Home Assistant Web page.

2. Click "**Settings**" > "**System**" in the left sidebar.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/6e2e47ce5fe64fb6b6cbed37dc7c0396.webp)

3. Click "**Network**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/e0e9d6dff4bd4d4587a8e5683391f132.webp)

4. Under "**HTTP Server**", expand "**Reverse Proxy**" and enable "**Trust X-Forwarded-For**".

5. Enter `0.0.0.0/0` under Trusted Proxies, then click "**Save**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/b3461b1669ba4c6b93c1de6e2e9a0b77.webp)

6. Follow the on-screen instructions and click "**Save and restart**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/1741b7adca20422a852c0bb6df93167a.webp)

#### Remote Access via the App Icon

After the restart is complete, log in to the device with your **UGREENlink ID**.

Click the **Home Assistant** icon, and the system will automatically redirect to the remote access interface.

### FAQs

#### Q: Why Doesn't Clicking the Home Assistant Icon Redirect Properly?

Check whether the WebUI port has been changed. The default Home Assistant access port is `8123`. Changing the WebUI port will cause app icon redirection to fail.

#### Q: How Can I View the Device IP Address?

Go to "**Control Panel**" > "**Network**" > "**Network Connection**" to view the device IP address.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/cc27038fbd054a06af8f6784f023b4b7.webp)

#### Q: Why Doesn't the Plugin Appear After Installation?

Make sure the plugin has been placed in the correct directory and restart Home Assistant. Third-party plugins usually appear in Integrations or the sidebar only after restart.

#### Q: What Should I Do If HACS Displays could\_not\_register?

Restart the device, return to the Home Assistant page, and submit the HACS configuration again.

#### Q: Can I Access Home Assistant Directly Outside the LAN?

To remotely access Home Assistant via the app icon, log in to the device with **UGREENlink ID** and complete the remote access configuration described in this guide.

### Notes

● Do not change the default Home Assistant WebUI port `8123`, as this may cause app icon redirection to fail.

● After setting the configuration path, do not delete or move the folder or rename it, as this may cause Home Assistant or plugins to malfunction.

● Third-party plugins, GitHub download pages, and external account services may change. Refer to the actual pages of the corresponding services.

● Remote access is available only when you log in to the device with UGREENlink ID.

● For more flexible custom configurations, consider deploying Home Assistant manually with Docker.
