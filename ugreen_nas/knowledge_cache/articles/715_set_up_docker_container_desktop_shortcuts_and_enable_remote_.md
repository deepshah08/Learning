# Set up Docker container desktop shortcuts and enable remote access functionality

> **Article ID**: `715`  
> **Category**: `Application Guide > Docker > FAQ > Set up Docker container desktop shortcuts and enable remote access functionality`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/715  

---

> The content and screenshots in this article are based on:UGOS Pro system firmware version 1.6.0.2890,Docker version 1.6.0.0663.Interface and features may vary across firmware versions. Please refer to your actual device display.

Docker Containers Support Desktop Shortcuts.Users can quickly access containers via desktop shortcuts. After logging in with a UGREENlink ID, remote access to container web interfaces is enabled for a more convenient operational experience.

### Configuring Desktop Shortcuts

1. Open the "Docker", select [**Containers**], and choose your target container.

2. Click the **"**···**"** (More)button next to the container, then select **"Desktop shortcut"** to open settings.

![](https://file-us.ugreennas.com/admin/article/2025-07-02/46bef638457043d38ff25e71c50c0578.webp)

3. In the pop-up window,you can customize the name, access port, and icon.For bridge network containers, the port auto-populates.

4. If the container uses host network or uses bridge network but has multiple ports, you need to manually configure the port.

> If you are unsure about the port number, you can check the official Docker Hub page to view the default port of the container image;
>
> You can also check the port settings when creating the container in Docker.

![](https://file-us.ugreennas.com/admin/article/2025-07-02/4c09ea1507be443eb004c69ad5f4ab52.webp)

5. Click **"Confirm"** to create the desktop shortcut.

![](https://file-us.ugreennas.com/admin/article/2025-07-02/5e0d1bd926d145ed9f923ebaac293aa9.webp)

### Remote Access via UGREENlink

After creating the desktop shortcut, click the shortcut icon to access the container's web interface. Docker containers support remote access, but you must log in to the system **using your UGREENlink ID to enable this functionality**.

**Restrictions:**

● Remote access is **only available to users logged in via UGREENlink**;

● If you log in using **DDNS or other methods**, you cannot use UGREENlink remote access.
