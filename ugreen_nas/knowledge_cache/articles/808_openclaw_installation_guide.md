# OpenClaw Installation Guide

> **Article ID**: `808`  
> **Category**: `Application Guide > Docker > Container Application > OpenClaw Installation Guide`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/808  

---

## Applicability

**Supported Clients:** UGREEN NAS PC client, Web browser

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

OpenClaw is a personal AI assistant that runs locally on the user's device. It can interact with users through commonly used communication channels and perform related tasks within authorized directories, such as writing code, generating files, or reading specified file contents.

OpenClaw has been adapted for UGREEN NAS, offering one-click installation from the "App Center" for a fully code-free deployment experience.

**Note:** This application consumes a significant amount of system resources. Please ensure that your system has at least **2 GB of available RAM** before installation. The installation package is relatively large, and the installation process may take **over 10 minutes**. Keep the device powered on and maintain a stable network connection during installation.

## Supported Models

The following models currently support the OpenClaw application. More models are being adapted:

● **DH Series** (UGOS Pro): DH2600, DH2300 (8G), DH4300 PLUS

● **DX Series** (UGOS Pro): DX4600 Series, DX4700 Series

● **DXP Series:** DXP2800 Series, DXP4800 Series, DXP6800 Series, DXP8800 Series, DXP480T Plus

## Prerequisites

Before installing OpenClaw, update the **Docker** app to the latest version.

1. Open the "**App Center**" and locate the **Docker** app. If "**Update**" is displayed, click it to update Docker first.

2. After the update is complete, install OpenClaw.

An outdated version of Docker may lead to deployment failures, permission issues, or runtime errors.

## Installation and Access

1. Open the "**App Center**", locate the "**OpenClaw**" app, and click "**Install**".

2. Follow the on-screen instructions to complete the installation settings.

3. After completing the settings, click "**Install**" and wait for the installation to finish.

![](https://file-us.ugreennas.com/admin/article/2026-09-03/e5225715026b48929c44dee5a0093e6e.webp)

4. Once installed, click the OpenClaw icon on the desktop or under All Apps to start using it.

### Configure Installation Settings

During installation, configure the workspace path and file access path based on your needs.

● **Workspace path:** This is the default working directory for OpenClaw. It is recommended to assign OpenClaw a dedicated empty folder to avoid mixing its files with other important files.

● **File access path:** Authorizes OpenClaw to read or modify existing files on the NAS, such as documents, images, and other files that need to be processed by AI. Click "**Add**" to configure multiple accessible directories.

**Notes:**

● For the initial installation, it is recommended to select an empty folder as the workspace path. Do not select folders containing private or sensitive data for either the workspace path or file access path.

● Deleting, modifying, or moving configured paths may cause application malfunctions.

● The file access path must not overlap with the "**Workspace path**" or any of its subdirectories.

## Login and Access

After installation, click the **OpenClaw** icon on the desktop or under All Apps. The system will open the OpenClaw Console login page in your browser.

Enter the **Gateway token** to sign in to the OpenClaw Console provided by UGREEN NAS. In the console, you can view the runtime status and configure models, channels, operation logs, and other settings.

![](https://file-us.ugreennas.com/admin/article/2026-09-03/c0fc1361b8c64f0dacbd1b03fb4f0a3d.webp)

## Console Overview

The overview page provides real-time monitoring of container operations and global quick access controls. The top of the page displays the current service status, for example:

```
OpenClaw running
```

Click the "**Open OpenClaw**" button in the top-right corner to open the native Web interface of OpenClaw in a new browser tab.

The center of the overview page displays container runtime data, while the "**Container configuration**" section below shows the underlying runtime parameters.

Advanced operations, such as "**Restore factory configuration**", are available at the bottom of the page.

**Notes:**

● After resetting to factory settings, all custom configurations will be restored to their initial state, including model providers, the default model, channels, plugin statuses, and other settings.

● A factory reset cannot be undone. Proceed with caution.

● The OpenClaw Console currently supports Chinese and English only.

![](https://file-us.ugreennas.com/admin/article/2026-09-03/cedef9c9d9134561bdf90cec15d7bf15.webp)

## Model Configuration

This feature allows allows you to manage the AI model services used by OpenClaw. You need to purchase or obtain the API Key required to use the models yourself.  
UGREEN NAS does not provide third-party model APIs or API Keys.

![](https://file-us.ugreennas.com/admin/article/2026-09-03/0425772f35334da981337a6e68b1d238.webp)

### Add providers

1. Go to the OpenClaw Console and click "**Model providers**">"**Add providers**".

![](https://file-us.ugreennas.com/admin/article/2026-09-03/72f3b8b83c5f4d779cd845695ba7ad78.webp)

2. Select a provider, enter the URL and API Key provided by the provider, and click "**Save**".

Once saved, the model provider will appear in the model providers list.

![](https://file-us.ugreennas.com/admin/article/2026-09-03/5dc5192115dc4e0bbfbbeb5887e0fcda.webp)

### Manage Existing Models

The list displays all currently configured model cards. Click "**Edit**" to modify the API Key or adjust specific model parameters; click "**Delete**" to remove the provider connection.

After a provider is deleted, OpenClaw will no longer be able to use models from that provider.

### Set Default Model

The default model is the main model that OpenClaw prioritizes.

1. Find "**Default model**" at the bottom of the model configuration page.

2. Click the dropdown menu and select the model you want to use as the default.

3. Click "**Save**" on the right.

Once saved, the selected model will be used as the default model.

![](https://file-us.ugreennas.com/admin/article/2026-09-03/ab93ec10cb96447281cdf1dbfdcb099f.webp)

## Information Channels

This feature allows OpenClaw to connect with external communication platforms, enabling automatic receipt and response of AI messages. The OpenClaw Console provides multiple channel plugins that can be installed, enabled, and configured as needed.

### Enable Channel Plugin

1. Go to the OpenClaw Console and click "**Information** **channels**".

2. In the "**Plugin status**" section, select the platform you want to connect and click "**Enable**".

Wait for the system to automatically fetch and install the required components.

### Add Channels

Once the plugin is ready, you still need to add a channel connection.

1. In the "**Channels Configuration**" section, click "**Add channels**".

2. Select an installed plugin and enter the required channel parameters as prompted.

![](https://file-us.ugreennas.com/admin/article/2026-09-03/bf61cb670cc34781ae7cfd87b61182c7.webp)

3. Click "**Save**".

For channels that have already been added, click "**Edit**" to modify the configuration parameters.

**Note:** The required parameters vary by channel. Enter the information according to the official requirements of the corresponding messaging platform. If you have any questions, contact the platform provider.

If the channel you need is not available in the OpenClaw Console, configure it from the native OpenClaw interface.

## Runlog

This feature provides transparent display of container runtime information, aiding in troubleshooting and status tracking.The page displays OpenClaw Docker container logs and various interaction events in real time.

By default, "**Automatic scrolling**" is enabled at the top-right, ensuring that the latest logs are always displayed at the bottom of the view without manual scrolling.

To clear the currently displayed content, click "**Empty**".

**Note:** Clearing the displayed log content does not mean that all historical logs are deleted. Please refer to the actual behavior of the interface.

![](https://file-us.ugreennas.com/admin/article/2026-09-03/83c4e2f985ae4f7e8e4d42aeeecad235.webp)

## Access OpenClaw Web Page

In the OpenClaw Console, click "**Open OpenClaw**" in the upper-right corner to open the native OpenClaw Web interface in a new browser tab.

![](https://file-us.ugreennas.com/admin/article/2026-09-03/747a173218f348959b56a94aeb1c8e68.webp)

## Using AI Chat

1. Click "**Chat**" in the left navigation panel to return to the conversation window.

2. Enter your question or command in the input box at the bottom of the page.

3. Click the "**Send**" button (paper plane icon) to start a conversation with your dedicated AI assistant.

![](https://file-us.ugreennas.com/admin/article/2026-09-03/9fdea4c8fc4c42b385d1f8b5e23d90e7.webp)

## FAQs

### What if I forget the Gateway Token or folder path?

If you forget the configured gateway token or authorized folder paths, you can retrieve them through the system settings.

**Steps to retrieve:**

1 Return to the UGREEN NAS desktop and open the "**Control Panel**" app.

2 In the left sidebar, scroll to the bottom and click "**About**".

3 Switch to the "**Apps**" tab at the top.

4 Locate "OpenClaw" in the app list and click to open it.

5 In the pop-up "**Application configuration**" window, you can view the authorized "**Accessible folder**" paths and the configured "**Gateway token**".

![](https://file-us.ugreennas.com/admin/article/2026-09-03/4c3d0f81f57641d7ab2e776a4695347a.webp)

### Folder Configuration Limitations

After OpenClaw is installed, the system does not support adding, modifying, or deleting the configured"**File access path**" or "**Workspace path**".

If you need to change or add authorized folders, the only solution is to uninstall the app completely and reinstall it with new configurations.

**Recommendation:** During the initial setup in the installation wizard, please plan ahead and select all directories to be processed by the AI at once, to avoid having to reinstall the application later due to changes.

## Related Reading

● [OpenClaw User Guide](https://support.ugnas.com/knowledgecenter/detail/article/en-US/809)

● [How to Add and Switch Models in OpenClaw](https://support.ugnas.com/knowledgecenter/detail/article/en-US/823)

## Security Risk Notice

● **Root Privileges and High-Risk Operations:** This application runs with root privileges inside a Docker container to support automation tasks. It has the ability to write/delete files, publish content, and execute system commands. Only grant access to trusted directories, and do not mount paths containing sensitive data into the container.

● **No Multi-Tenant Isolation:** By default, OpenClaw is designed for a single trusted operator and does not provide isolation between multiple users. If multiple users share the same agent, they will have the same level of access and permissions.

● **Public Network Exposure Risk:** If you are not familiar with security hardening and access control, do not expose this service directly to the public internet. **UGREEN NAS does not provide technical guidance for public internet access**. If needed, consult a qualified professional.

● **Content Compliance:** When interacting externally through channel bots or similar interfaces, you must comply with the requirements of the relevant platforms and the laws and regulations of the applicable jurisdictions. Users are solely responsible for any AI-generated content.

● **Disclaimer:** This application is provided as a service integration tool. The provider offers deployment support only and does not guarantee the security, stability, or completeness of the OpenClaw software itself. Any customization, operational decisions, and resulting legal, financial, or data-related risks—including but not limited to data leaks, device damage, additional costs, or legal disputes—are the sole responsibility of the user. The provider assumes no liability for such risks.
