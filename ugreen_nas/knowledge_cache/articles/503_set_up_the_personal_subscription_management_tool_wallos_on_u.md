# Set Up the Personal Subscription Management Tool Wallos on UGREEN NAS

> **Article ID**: `503`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Set Up the Personal Subscription Management Tool Wallos on UGREEN NAS`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/503  

---

## Container Overview

Wallos is an open-source tool specifically designed for managing subscription services. As internet applications continue to grow, many services have adopted a subscription-based model. While this brings convenience, it also makes it harder to manage and track subscriptions—especially when they originate from different platforms such as credit cards, the iOS App Store, or PayPal.

Wallos addresses this challenge by providing a centralized platform that enables users to easily track, manage, and analyze their subscription statuses. With Wallos, users can clearly view all their active subscriptions, avoid duplicate subscriptions or missed payment dates, and gain better control over their personal expenses.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/a6ea142396ec46c3a8539c14a31f70ff.webp)

## Deploy the Container Using Docker Compose

On the UGOS Pro system, it is recommended to use the Project (Docker Compose) method to quickly deploy containers. This approach is ideal for scenarios that require managing multiple containers simultaneously, as it simplifies both deployment and management tasks. Below are the detailed steps for deploying Wallos using Docker Compose.

Click to learn more: [What is a Project (Docker Compose)?](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjozMzIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiJwcm8wMDIsOWpvcDV3LGUyZVNueiJ9)

### Enter the Docker Project Interface

On the UGOS Pro system, open the Docker app and go to [Project] > [Create] to launch the project creation wizard.

### Configure the Docker Compose File

In the project creation wizard, you will need to upload a Docker Compose configuration file. Below is a sample configuration for Wallos:

```
services:
  wallos:
    container_name: wallos
    image: bellamy/wallos:latest
    restart: always
    volumes:
      - ./db:/var/www/html/db #Database files
      - ./logos:/var/www/html/images/uploads/logos #
    environment:
      TZ: Asia/Shanghai #Time zone setting for the container
    ports:
      - "28282:80" #Maps port 8282 on the host to port 80 in the container
```

### Parameter Explanation

**image:** Specifies the Docker image and version to use. `latest` means the latest version of the image will be pulled.

restart：Defines the container's restart policy. `always` ensures the container restarts automatically if it stops or crashes.

**volumes：**

`./db:/var/www/html/db`: Used to store Wallos's database files. `./` refers to the directory where the Docker Compose file is located, and it mounts the `db` folder from the host machine to the `/var/www/html/db` path inside the container.

`./logos:/var/www/html/images/uploads/logos`: Mounts the `logos` folder from the NAS host to `/var/www/html/images/uploads/logos` in the container, used to store logo image files.

**environment：**

`TZ: Asia/Shanghai`Sets the container's time zone to `Asia/Shanghai`, matching China Standard Time. You can change this to suit your region, such as `America/New_York` or `Europe/London`.

**ports：**Maps port `28282` on the host to port `80` in the container. You can access Wallos on your local network via `http://<NAS_IP>:28282`.

### Deploy the Project

Once the configuration is confirmed, click [Deploy] to begin. The system will automatically pull the image and start the container. After deployment, you can access the Wallos homepage at `http://<NAS_IP>:port` (for example: `http://192.168.22.153:28282`).

![](https://file-us.ugreennas.com/admin/article/2025-09-09/080c190e6a0e47bdae9a261cb3c95c83.webp)

## Access the Web Interface

Open a browser and enter `http://<NAS_IP>:28282` to access the Wallos web interface. When accessing port 28282, you will be prompted to set a username and password. On the Wallos homepage, you can first switch the language to English and set the **primary currency** to US Dollar. Then, proceed to register by setting your username, email address, and password.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/c9d36ad93fb648c481cbceeaaed43b69.webp)

After successful registration, you will be redirected to the login page. Use the account you just created to log in.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/3cbdd01f60384cdbb911122b61cd5c33.webp)

### Add a Subscription

**Wallos** is very easy to use. Click [Add Your First Subscription] to begin tracking a subscription. In the subscription setup options, you can configure the price, currency, and payment method according to your needs. You can also set the payment frequency and due date. **Wallos** also allows you to enter the subscription URL, making it convenient to jump directly to the subscription service later.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/cd953bc7457a47379998aa84b550c17a.webp)

After adding a subscription, you can view basic information such as the subscription name, payment frequency, and price on the homepage.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/ab38a40a1b2442b39aa97816dbc5b527.webp)

### Subscription Expense Statistics

In addition to the basic subscription adding feature, Wallos also supports tracking all subscription information. Click on **the avatar in the top right corner** and select **[Statistics]** to view the expenses for all subscriptions.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/aa527b33f30c479fa4052b7e73403c55.webp)

### Automatic Currency Conversion

If your subscription services involve foreign currencies, Wallos also supports the Fixer API to query exchange rates for conversion. This allows you to view the converted subscription expenses directly in the statistics. On the Wallos homepage, click the user avatar to enter [Settings], scroll down to find the Fixer API Key option, and enter your API key to save and activate it.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/d3c5c366030f4fa1821ed42205f9b13d.webp)

You can apply for a free Fixer API by visiting [the Fixer API application link.](https://fixer.io/#pricing_plan) Choose the appropriate API plan based on your needs. For individual users, the free plan may be sufficient to meet your requirements.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/5cff40dc27f84897870b11b8b9eb803d.webp)

Click on the "free" subscription, fill in the registration information, and then click [Visit Dashboard] to be redirected to the dashboard where you can copy your API Key. Copy the API Key and return to Wallos, then paste it in the Fixer API Key section in the settings and save to activate it.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/e64a1ddc689a447fab614bcb1e8a4f1a.webp)

![](https://file-us.ugreennas.com/admin/article/2025-09-09/840baef5dd5842baab7ad99934fd9ef4.webp)

Note: After configuring currency exchange conversion, you may encounter display issues. To resolve this, first go to the Profile section in the settings page and change the "Main Currency" to the currency of the product you added, such as Euros or Chinese Yuan. After saving, change it back to "US Dollars" and save again. After doing this, the system will correctly display the converted RMB amount.

In the future, when you add subscription bills, simply select the original currency of the bill, and the system will automatically perform the currency conversion to ensure proper display.

### Email Notifications

Wallos also supports email notifications. Once configured, you will receive reminders for subscription expirations.

![](https://file-us.ugreennas.com/admin/article/2025-09-09/f079f4b39b324ced8744469022e3aec0.webp)

## Notes

Please note that the image used in this tutorial is developed and maintained by a third party, and this tutorial is for reference only. UGREEN is not responsible for any risks caused by improper user operations, third-party software vulnerabilities, or image updates, including but not limited to:

● Third-party images may cause unexpected modification or deletion of files in the UGOS Pro system.

● Using insecure images may result in data being uploaded to third-party servers, posing risks of privacy and data leakage.

● To ensure system stability and data security, please carefully choose third-party images from trusted sources.

**Other Notes:**

1. The file/folder paths for the container are for reference only; you can create them according to your personal preferences.

2. The container port and local port for web access should match. If there is a conflict, change to an unused port. Local ports between containers must be unique; port conflicts will prevent the container from starting.

3. The container's web link is only accessible in bridge mode.

4. The image only provides a setup tutorial; for specific usage and advanced features, please refer to online resources.

5. The image is developed by a third party, so for configuration changes and bug fixes, please follow the relevant official information.

6. It is recommended to store the Docker configuration directory on an SSD to avoid system performance issues caused by mechanical drives.
