# Enable Version Retention

> **Article ID**: `400`  
> **Category**: `Application Guide > Sync & Backup > Enable Version Retention`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/400  

---

Enabling the version retention feature is a key measure to prevent data conflicts, especially when multiple users are editing the same file simultaneously. By keeping multiple versions, you can maintain data consistency and protect against potential conflicts.

### Enable Version Retention

The first step is to navigate to **Sync & Backup** > **Administrator Settings** > **General**, and enable the **Version Retention** feature. Once activated, the system will automatically retain historical versions of files in the synchronized **Shared Folders**, ensuring data integrity is preserved whenever changes are made to files.

### Set Default Version Retention

The next step is to configure the specific version retention settings. On the [**General**] page, click the "**Settings"** button:

* **New File Settings**: Select the default number of versions to retain, which will apply to newly created shared folders.
* **Existing File Settings**: In this section, click the "**Add"** button to choose the shared folders where version retention should be enabled and set the number of versions to retain. After selecting the target folders, click "**Confirm"** to complete the setup.

### Manage Version Retention for Shared Folders

For shared folders that are already linked to a sync connection, you can view their connection status in the **Existing File Settings** list. To modify the version retention for a shared folder, click “**Edit”** to adjust the settings. If you do not need version retention for a particular shared folder anymore, click "**Delete"** to remove the setting.

### Apply Changes and View Historical Versions

After completing all the settings, click "**Confirm"** to apply the changes. To view the historical versions of a shared folder, click "**File Version Explorer"** to access the version history page, where you can browse and manage the retained file versions. For more information on managing historical versions, please refer to the [**Version Management**](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAxIiwibGFuZ3VhZ2UiOiJlbi1VUyIsImlkIjo5NjksImFydGljbGVJbmZvSWQiOjMxOSwiY2xpZW50VHlwZSI6IlBDIiwiYXJ0aWNsZVZlcnNpb24iOiIxLjAiLCJwYXRoQ29kZSI6InBybzAwMixhVHRyOWEsRUhNOGt1In0=)guide.

### Notes

* **Version Retention**: When multiple users edit the same file at the same time, it can cause conflicts. To avoid data issues, it’s recommended to enable version retention, such as keeping multiple versions, to maintain consistency.

* **Network Bandwidth**: Syncing large amounts of data in real time can use up a lot of network bandwidth, especially in poor network conditions. To improve performance, adjust the sync frequency and method based on your needs, so it doesn’t affect other critical tasks.

* **Choose the Right Sync Method**: Different situations require different sync methods. For frequently updated work files, two-way sync ensures consistency. For backup data that doesn’t change often, one-way sync is better as it reduces unnecessary data transfer.

* **Regularly Check Sync Status**: Although syncing is automatic, it’s a good idea to check the sync logs and status reports regularly. This helps spot any problems like sync failures or file conflicts, so you can fix them quickly.

* **Use with Other Backup Tools**: While syncing is a powerful feature, it shouldn’t fully replace traditional backup methods. It's recommended to use syncing alongside backup tools to provide multiple layers of data protection and enhance security.
