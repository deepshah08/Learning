# Administrator Settings

> **Article ID**: `221`  
> **Category**: `Application Guide > Sync & Backup > Administrator Settings`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/221  

---

Within "**Administrator Settings**" of the "**Sync & Backup**" application, administrators can perform a range of advanced management tasks to improve the efficiency and security of synchronization and backup operations. The main features and their usage are described below.

## General

### Enable Administrator Mode

After enabling "**Administrator mode**", administrators can view and manage the connection status of other users on the "**Overview**" page. This feature allows administrators to gain comprehensive visibility into system resource usage and make timely adjustments when necessary.

### Enable Version Retention

When "**Version retention"** is enabled, the system automatically keeps historical versions of files in personal folders or shared folders associated with synchronization tasks, helping ensure the security of synchronized data.

1. Go to the "**Administrator Settings"** page and enable "**Version retention"**.

2. Turn on the "**File Version Explorer**" option below to navigate to the "**File Version Explorer**" application.

![](https://file-us.ugreennas.com/admin/article/2026-01-05/b471761136e04f9ab9621ce0f084fa53.webp)

3. Click the "**Settings**" button in the lower-left corner to retrieve all existing personal folders and shared folders in the system.

![](https://file-us.ugreennas.com/admin/article/2026-01-05/a8f0ef57e3ff4d43a9a8edef70fe9c99.webp)

**Options and Descriptions:**

● **Version Retention**: Enables or disables version retention for all local users or shared folders. The system retains 8 versions by default, with a maximum of 32 versions. You can set an appropriate number based on your needs. When the number of generated versions exceeds the limit, older versions are deleted. If version retention is disabled, no historical versions will be kept for the selected shared folder, deleted files cannot be restored, and all existing file versions will be removed.

● **Number**: The number of versions retained for the current folder. This value can be adjusted at any time. When the number is reduced, excess versions are automatically deleted by the system.

● **Size**: Displays the amount of volume used by retained file versions.

● For more detailed instructions on version management, please refer to [**File Version Explorer**](https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmMzE2In0=) .

### Transfer Log Cleanup Policy

Administrators can configure a transfer log clear policy that applies to all users, defining both the maximum number of logs retained and the retention period. This policy page is visible only to administrators; general users do not have access to this setting. By default, the system retains the most recent 1 million records or logs from the last 6 months.

**Note**: Each clearing action is recorded as an entry in the Operation Logs.

![](https://file-us.ugreennas.com/admin/article/2026-01-05/7732c6cc2cc544cbb23ce79d00ea1d07.webp)

## Speed Limit Settings

Under "**Speed Limit**", administrators can apply bandwidth limits to already connected devices or to newly connected devices, optimizing system resource usage and ensuring network stability.

● **Set speed limits for connected devices**: Select a connected device and click "**Edit**" to configure a maximum speed limit for that device. This prevents any single device from consuming excessive bandwidth and affecting the normal operation of other devices.

● **Set speed limits for newly connected devices**: When "**New connection speed limit**" is enabled, all newly connected devices are subject to a default speed limit. This helps prevent new devices from consuming excessive system resources and degrading overall system performance.
