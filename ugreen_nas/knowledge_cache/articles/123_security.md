# Security

> **Article ID**: `123`  
> **Category**: `Application Guide > Security > Security`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/123  

---

## Applicability

**Applicable Client**: UGREEN NAS PC Client (Windows/macOS).

**Applicable Version**: NAS Firmware 1.17.0.0031 or later.

The descriptions in this document are for reference only. The interface and operation paths may vary depending on system or app updates, please refer to the actual interface.

## Introduction

Security helps detect suspicious files on your NAS and provides features such as Real-time Protection, Manual Scanning, Scheduled Scanning, Quarantine, Scan History, and Log Management.

You can use Security to scan system files and user files to reduce security risks caused by suspicious files.

## Security Home Page

After opening Security, you can view the current security status of your device on the home page. The home page mainly displays the following information:

● **Real-time Protection**: Shows whether real-time protection is enabled.

● **Protecting Days**: Shows the total number of days Security has protected the system.

● **Time since last scan**: Shows the time elapsed since the last scan.

● **Suspicious files found**: Shows whether any suspicious files have been detected.

● **Quick Access**: Provides quick access to Full Scan, Custom Scan, and Quarantine.

To manually scan files on your device, click the corresponding scan option on the home page.

![](https://file-us.ugreennas.com/admin/article/2026-07-14/48d65165abbc4e49a756a41fa7cf1873.webp)

## Create a Scheduled Scan Task

Scheduled Scan can automatically run scan tasks at the specified time. Follow the steps below:

1. Open Security, click "**Scheduled Scan**" in the left sidebar, and click "**Create**" at the top of the page.

2. Set the scan scope, file types to scan, suspicious file handling method, and scan schedule. To run a scan immediately after creating the task, select "**Trigger immediately after creation**".

3. Click "**Done**".

After the task is created, the Scheduled Scan task will be displayed in the task list.

![](https://file-us.ugreennas.com/admin/article/2026-07-14/bf70687fe12e42ea8c4c984a8a6a3089.webp)

### Scheduled Scan Strategy Description

When creating a Scheduled Scan Strategy, you can configure the following settings as needed:

● **Strategy**: Used to identify the current Scheduled Scan task.

● **Target**: Select the file range to scan, such as system files or user files.

● **Scan file types** : Select whether to scan all file types or specify the file types to scan. If there are no special requirements, the default settings are recommended.

● **How to handle suspicious files**: Set how suspicious files are handled after detection, such as moving them to Quarantine.

● **Frequency**: Set the execution frequency and time for Scheduled Scan.

It is recommended to schedule scans during periods of low device usage to minimize the impact on normal operations.

### Set Scan Result Notifications

When creating a Scheduled Scan task, the system will prompt you to choose whether to display virus scan results in notifications. Select an option as needed:

![](https://file-us.ugreennas.com/admin/article/2026-07-14/82e70225dec3409088c1c35485a99f10.webp)

● Click"**Yes**": Enable scan result notifications. Future scan results can be viewed in the Notification Center.

![](https://file-us.ugreennas.com/admin/article/2026-07-14/4b81881adade401ea1c34facb9d62ed3.webp)

● Click "**No**": Do not enable scan result notifications for this task. You can configure "**Notification**" later in Security settings.

## Manage Scheduled Scan Tasks

After creating a Scheduled Scan task, you can view the task list on the **Scheduled Scan** page. The task list displays the following information:

● Strategy

● Creator

● Scope

● Frequency

● Status

Select the target task and click "**Operation**" to manage it. The available operations include:

● **Edit**: Modify the Scheduled Scan strategy.

● **Enable**: Enable a disabled Scheduled Scan task.

● **Disable**: Pause the Scheduled Scan task.

● **Delete**: Delete a Scheduled Scan task that is no longer needed.

After deleting a task, the corresponding Scheduled Scan strategy will no longer be executed.

![](https://file-us.ugreennas.com/admin/article/2026-07-14/1c44544a840e4c6dab72bc9af17d2fde.webp)

## View Scan Records

After a scan is complete, you can view the results on the **Scan Records** page. Follow the steps below:

1. Open Security, click "**Scan Records**" in the left sidebar, and go to the "**Scan Records**" page.

2. View the Strategy, Creator, Start Time, Duration, and Suspicious Files Found.

If suspicious files are detected, click "**Check & Handle**" on the right side of the record.

![](https://file-us.ugreennas.com/admin/article/2026-07-14/5b5802da8e4745ac82885f67c672f1d4.webp)

## Clear Scan Records

To clear scan records, select the target records in the record list, then click "**Clear Records**".

Clearing records only removes scan records. It does not restore or delete suspicious files in Quarantine.

## View Real-time Protection Records

After Real-time Protection is enabled, the system will record related events. Follow the steps below:

1. Open Security, click "**Scan Records**" in the left sidebar, and switch to the "**Real-time protection records**" tab.

2. View the Real-time Protection trigger records.

If there are no related events, the page will display no Real-time protection records.

## Manage Quarantine Files

After Security detects suspicious files, the files can be moved to Quarantine according to the handling rules. Follow the steps below:

1. Open Security, click "**Scan Records**" in the left sidebar, and switch to "**Quarantine**".

2. View the quarantined suspicious files, select the files to handle, and choose an action as needed.

Quarantine supports the following operations:

● **Delete**: Delete files in Quarantine.

● **Trust**: Add files to the trusted list.

● **Recover**: Recover files to their original location or a specified location.

Before handling files in Quarantine, confirm whether the file source is trustworthy. If you are unsure, it is recommended to keep the files quarantined or contact technical support for assistance.

## View Log

The Log page is used to view Security operation records and system events. Follow the steps below:

1. Open Security and click "**Log**" in the left sidebar.

2. View the log list.

The log list usually contains the following information:

● Level

● User

● Date & Time

● Log

You can enter keywords in the search box to find logs. You can also export or clear logs using the functions provided on the page.

![](https://file-us.ugreennas.com/admin/article/2026-07-14/3a2b3d0950a04fc294b7acc23826434e.webp)

## Configure Virus Database Updates

Security supports viewing the Virus Database version and configuring update strategies. Follow the steps below:

1. Open Security and click "**Settings**" in the left sidebar.

2. View the current version in the "**Virus Database**" section.

3. Configure the update strategy as needed.

4. To check for updates immediately, click "**Check for Updates**".

It is recommended to keep the Virus Database up to date to improve suspicious file detection.

![](https://file-us.ugreennas.com/admin/article/2026-07-14/45767fbcbe79450a9afa29d4b6607622.webp)

## Configure Default Scan Target

You can configure the default scan target on the Settings page. Manage the following options as needed:

● **Whitelist**

● **Only scan the selected file types**

If certain files are confirmed to be safe, you can add them to the Whitelist to reduce repeated prompts. If you only need to scan specific file types, configure the selected file types as needed. The available configuration options may vary depending on the actual page.

![](https://file-us.ugreennas.com/admin/article/2026-07-14/c9a309bc95104e38ab0cce846c3cd0ef.webp)

## Configure Default Handling Rules

You can configure the default handling method for suspicious files detected on the Settings page.

For example: Move to quarantine

It is recommended that general users keep the default handling rules. After suspicious files are moved to Quarantine, you can view and handle them later to prevent accidental deletion of important files.

![](https://file-us.ugreennas.com/admin/article/2026-07-14/f6c4b5bc459d41ab9255380ff1efecf9.webp)

## Configure Notification Management

Security supports Notification Management. After enabling this feature, scan results or suspicious file notifications can be displayed in the system Notification Center.

Follow the steps below:

1. Open Security, click "**Settings**" in the left sidebar, and find "**Notification Management**".

2. Enable Notification Management, configure the notification frequency and notification scope, and click "**Save**".

When creating a Scheduled Scan task, if the system prompts whether to display scan results in the Notification Center, select an option as needed.

![](https://file-us.ugreennas.com/admin/article/2026-07-14/b52b58cd77b249dd840440d85dd87ef6.webp)

## Notes

● Scanning may consume certain system resources. If large file transfers, backups, synchronization, or Media Indexing are in progress, it is recommended to avoid running Full Scan during high-load periods.

● Files in Quarantine cannot be used normally before being handled. If a file is confirmed to be safe, you can restore or trust it in Quarantine.

● After deleting files from Quarantine, the related files may not be recoverable. Confirm that the files are no longer needed before deleting them.

● Feature names and page layouts may vary slightly between different system versions. Please refer to the actual interface.
