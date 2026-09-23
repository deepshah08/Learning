# How to Configure and Use OpenClaw Console

> **Article ID**: `838`  
> **Category**: `Application Guide > Docker > Container Application > How to Configure and Use OpenClaw Console`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/838  

---

## Overview

OpenClaw Console, Provided by UGREEN NAS, serves as the core backend for managing AI large model services and multi-channel message distribution. Through this console, you can intuitively monitor container runtime status, flexibly configure large model APIs, and quickly integrate AI with external communication tools (such as Telegram, Feishu, etc.) to achieve efficient workflow for intelligent agents.

## Login and Access

1. On the UGREEN NAS desktop, locate and click the "**OpenClaw**" application shortcut. The system will automatically open your browser and navigate to the Web console page.

2. Upon first access, enter the previously configured gateway token in the prompted input field.

3. After entering the token, click the "**Sign in**" button to enter the console homepage.

![](https://file-us.ugreennas.com/admin/article/2026-05-11/ca6a981d6d384b7d97d33699ee3cb2ef.webp)

## Console Overview

The overview page provides real-time monitoring of container operations and global quick access controls. The top of the page displays the current service status (e.g., "**OpenClaw running**"). Click the "**Open OpenClaw**" button in the top-right corner to open the native Web interface of OpenClaw in a new browser tab.

● **Resource and Configuration Monitoring**: The central panel shows the current container's CPU usage, memory consumption, and uptime. The "**Container info**" section below lists underlying runtime parameters such as gateway ports, process PID, and virtual memory.

● **Restore Factory Settings**: At the bottom of the page, in the Advanced/Dangerous zone, you can perform a "**Reset to factory**" operation. Note that this action is irreversible. Executing it will reset all custom configurations—including model providers, default models, channels, plugin statuses, etc.—to their initial default state. Proceed with caution.

![](https://file-us.ugreennas.com/admin/article/2026-05-11/a6be089c4a394a718feca453d8d1acf2.webp)

### Model Provider

This feature allows centralized management of the AI model services used by OpenClaw.

![](https://file-us.ugreennas.com/admin/article/2026-05-11/3d35a6b483d045eb8df794237d0a5dd5.webp)

1. **Add a Provider**

In the "**Model providers**" section, click "**Add provider**" at the top-right corner. In the pop-up configuration window, select the corresponding provider (e.g., DeepSeek, OpenAI) and correctly enter the Base URL and dedicated API Key.

![](https://file-us.ugreennas.com/admin/article/2026-05-11/601e40cafb964a0088a01916e8b9d559.webp)

2. **Manage Existing Models**

The list displays all currently configured model cards. Click "**Edit**" on the right to modify the API Key or adjust specific model parameters; click "**Delete**" to remove the provider connection.

3. **Set Default Model**

In the "**Default model**" area at the bottom of the page, click the dropdown menu to select the main model that the application should prioritize. After switching, be sure to click "**Save**" on the right to apply the changes.

### Channels

This feature allows OpenClaw to connect with external communication platforms, enabling automatic receipt and response of AI messages.

1. **Enable Channel Plugin**

In the "**Plugin status**" section, select the platform you want to connect (e.g., Telegram) and click "**Enable**". The system will automatically fetch and install the plugin, and once completed, the status will change to green "**Ready**"**.**

![](https://file-us.ugreennas.com/admin/article/2026-05-11/8806d162927b426b9c59e6f4e607a5cd.webp)

2. **Configure Channel Parameters**

Taking Telegram as an example, once the plugin is ready, go to the "**Channels"** section below and click "**Add channel**" to establish a connection with the installed plugin. For channels that have already been added, click "**Edit**" to replace or update settings like Bot Token and DM Policy.

![](https://file-us.ugreennas.com/admin/article/2026-05-11/4603371bea7643d19ef4e9ecb7388a80.webp)

### Operation Logs

This feature provides transparent display of container runtime information, aiding in troubleshooting and status tracking.

1. **Real-Time Log Stream**

The terminal on the page continuously outputs OpenClaw Docker container logs and interaction events.

By default, "**Auto-scroll**" is enabled at the top-right, ensuring that the latest logs are always displayed at the bottom of the view without manual scrolling. To clear the log view, click "**Clear**".

![](https://file-us.ugreennas.com/admin/article/2026-05-11/db4f0a6eb3d44b3c8b82cffe263a2f9c.webp)
