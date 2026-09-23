# Install OpenClaw on a UGREEN NAS and Configure the Gemini Model and Telegram Bot

> **Article ID**: `854`  
> **Category**: `Application Guide > Docker > Container Application > Install OpenClaw on a UGREEN NAS and Configure the Gemini Model and Telegram Bot`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/854  

---

## Overview

**OpenClaw** is a personal AI assistant that runs locally on your device. It interacts with users through common communication channels. The UGREEN NAS version has been deeply customized to provide a "**one-click**" installation experience, enabling a fully no-code deployment workflow.

This guide will walk you through deploying the Google Gemini model engine within OpenClaw, as well as configuring authentication for the Telegram interaction channel.

**Note**: This application consumes significant system resources. Ensure your system has at least **2 GB** of available RAM. The installation process may take more than **10 minutes**, which is normal.

### Supported Models

The following NAS models currently support the OpenClaw application (more models are being added):

● **DXP Series**: DXP2800, DXP4800, DXP4800 Plus, DXP4800 Pro, DXP6800, DXP6800 Plus, DXP6800 Pro, DXP8800, DXP8800 Plus, DXP8800 Pro, DXP480T Plus

● **iDX Series**: iDX6011, iDX6011 Pro

## Prerequisites

Before installing OpenClaw, go to the "**App Center**" on your UGREEN NAS and make sure that the **Docker** application is installed and updated to the latest version.

**Note**: OpenClaw relies heavily on the Docker container environment. If the Docker version is outdated, it may cause deployment failures, incorrect permission configurations, or runtime issues.

### Get a Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/) , sign in with your Google account, then click "**Get API key**" in the left sidebar and select "**Create API key**".

![](https://file-us.ugreennas.com/admin/article/2026-05-15/b2bc7b3b2c9545d9a92b8bbd06d4616b.webp)

2. Choose an existing project or create a new one.

3. After selecting the project, click "**Create Key**".

![](https://file-us.ugreennas.com/admin/article/2026-05-15/2ce8ac6d44164a5dbe1a515f76f86078.webp)

4. Copy and securely store the generated API Key.

![](https://file-us.ugreennas.com/admin/article/2026-05-15/168d1c2ca5344aa4b4620507eb64cf13.webp)

### Create a Telegram Bot

● Log in to Telegram and search for the official bot management tool `@BotFather`.

![](https://file-us.ugreennas.com/admin/article/2026-05-15/818b224cf92f464b8113026d5fbec619.webp)

● Send the command `/newbot` to start the creation process.

● Follow the prompts to configure:

**Bot Name**: The display name of your bot.

**Bot Username**: A globally unique identifier that must end with `bot` (e.g., `my_openclaw_bot`).

● After creation, copy and securely store the **Bot Token** provided by the system (example format: `1234567890:AAxxxxxxxxxxxxxxxxxxxxxxxx`).

![](https://file-us.ugreennas.com/admin/article/2026-05-15/42e3ef97b38b4106b23fec797e161f87.webp)

## Step 1: Install the Application

Log in to your UGREEN NAS, go to the "**App Center**", find **OpenClaw** under the "**All**" list, and click "**Install**".

![](https://file-us.ugreennas.com/admin/article/2026-05-15/6d8888db92894bea9d179e2bbeeabbed.webp)

## Step 2: Installation and Configuration

When installing the OpenClaw application, you must first complete the system path and model interface settings on the "**OpenClaw installation configuration**" page.

### Path Configuration

This section defines the file access scope for OpenClaw. For data security, grant permissions carefully.

![](https://file-us.ugreennas.com/admin/article/2026-05-15/5b33f3b6e03d41e19d7ab0f750c35b5d.webp)

● **Workspace path**: This is the default working directory for OpenClaw. It is used by AI to write code, generating files, and storing temporary data. It is recommended to assign an empty folder.

● **File access path**: Authorizes OpenClaw to read or modify existing files on the NAS (such as documents and videos). Multiple directories can be configured by clicking the "**Add**" button.

**Notes:**

● Do not select folders containing private or sensitive data. Deleting, modifying, or moving authorized folders may cause application malfunctions.

● The file access path must not overlap with the "**Workspace path**" or any of its subdirectories.

### API and Model Configuration

This section is used to connect to external large language model (LLM) services.

● **API Base URL**: Enter the interface address provided by the LLM service provider (e.g., `https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-lite-preview:generateContent`).

● **Model name**: Enter the specific model version to be invoked (e.g., gemini-3.1-flash-lite-preview).

● **API key**: Enter the dedicated access key obtained from the model provider.

● **Gateway token**: This token is required for authentication when accessing the OpenClaw Web interface via a browser.

![](https://file-us.ugreennas.com/admin/article/2026-05-15/5cf5ada489cb4cdc9b3f13e1ad504274.webp)

### Complete the Installation

After confirming that the above configurations are correct and fully understanding the associated risks, select "**I have read and understand and the installation risks**" in the lower-left corner of the page. Then click "**Install**" in the lower-right corner to begin deploying the application.

![](https://file-us.ugreennas.com/admin/article/2026-05-15/21957240a63948b38144c0c2a24cba4b.webp)

### 

### Risks and Precautions

OpenClaw is a highly privileged automation agent. Before installation, please carefully review the following key risks:

1. By default, the application runs within a Docker container with root privileges, allowing it to read and write files and execute system commands. It is strongly recommended not to expose this application to the public internet.

2. The current version does not provide secure multi-user isolation. If multiple users share the same application instance, they will share all tool permissions and data.

3. This open-source project is currently in the testing stage. Any legal, financial, or data-related risks arising from AI-driven automation—such as accidental file deletion or data leakage—shall be borne solely by the user.

## Usage and Connection

After installation, you need to verify the connection through the Web interface. The frontend console must connect to the OpenClaw backend gateway.

### Step 1: Access the Web Management Interface

1. On the UGREEN NAS desktop, locate the OpenClaw app and click its shortcut icon.

2. The system will automatically open your browser and navigate to the OpenClaw Web management interface.

3. After entering the interface, you will be prompted to enter the Gateway Token. Input the token you previously set.

4. Once entered, click the "**Connect**" button below.

![](https://file-us.ugreennas.com/admin/article/2026-05-15/ee6702d657844b178b9e6a9078619d14.webp)

### Step 2: Verify Connection Status

After a successful connection, you can confirm that the gateway is active through the interface:

● Click "**Overview**" in the left sidebar.

● Locate the "**Snapshot**" card on the right side.

Its status should display as green"**OK**"

![](https://file-us.ugreennas.com/admin/article/2026-05-15/dc7a420b9270494cb0c4dc8f7de4c161.webp)

### Step 3: Start Using the AI Assistant

The UGREEN NAS version comes with the high-performance MiniMax 2.1 large language model deeply integrated, eliminating the need for complex model or API configuration.

1. Click "**Chat**" in the left sidebar to return to the conversation interface.

2. Enter your question or command in the input box at the bottom of the page.

3. Click the "**Send**" button (paper plane icon). You can now start interacting with your AI assistant.

![](https://file-us.ugreennas.com/admin/article/2026-05-15/ae2f2951fb3e430984016c3d4509d7fe.webp)

## Connect to a Telegram Bot

Before configuring a third-party bot, you need to access the system command line via the terminal:

1. Open the "**Docker**" app, click "**Project"** in the left sidebar, then find the "**openclaw**" project and open its details.

![](https://file-us.ugreennas.com/admin/article/2026-05-15/6c4dcb51ae62472d8f76c4f0e8735cbb.webp)

2. Select the corresponding container and switch to the "**Terminal**" tab.

![](https://file-us.ugreennas.com/admin/article/2026-05-15/61d5462fab2d42b68a4c687eb29076e3.webp)

3. Click "**Add**" in the Terminal tab.

![](https://file-us.ugreennas.com/admin/article/2026-05-15/aeea372fdef9492b9bbba4c92604f41b.webp)

4. In the pop-up command box, enter `/bin/bash` and click "**Confirm**" to create the session.

![](https://file-us.ugreennas.com/admin/article/2026-05-15/cd445c25cc394060b4e1419491f99fb3.webp)

5. In the terminal window, enter the following command and press **Enter**: `openclaw configure`

![](https://file-us.ugreennas.com/admin/article/2026-05-15/ed45aa507413476eaa97fa4d416391cc.webp)

6. Follow the prompts and make the following selections (press Enter after each selection):

● `Where will the Gateway run?` → Select "**Local (this machine)**".

![](https://file-us.ugreennas.com/admin/article/2026-05-15/56773defbdb04deeba0f5845d2f11a6b.webp)

● `Select sections to configure` → Select "**Channels**".

![](https://file-us.ugreennas.com/admin/article/2026-05-15/8161b402891f42c4be8a98878d3741ce.webp)

● `Channels`→ Select "**Configure/link**".

![](https://file-us.ugreennas.com/admin/article/2026-05-15/d8ba6c6507314936b74283d9d049b217.webp)

● `Select a channel` → Select "**Telegram (Bot API)**"

![](https://file-us.ugreennas.com/admin/article/2026-05-15/72b370f75fbf484fb4552c21365d6814.webp)

● `How do you want to provide this Telegram bot token?`→ Select "**Enter Telegram bot token**".

![](https://file-us.ugreennas.com/admin/article/2026-05-15/be485410b1f2460a9264846a41962dcc.webp)

● `Enter Telegram bot token` → Paste your Telegram Bot Token and press **Enter**.

![](https://file-us.ugreennas.com/admin/article/2026-05-15/6d13112b92ae41019ceaa60431c5c645.webp)

7. After entering the token, the system will return to the channel selection screen. Select "**Finished**" and press Enter.

![](https://file-us.ugreennas.com/admin/article/2026-05-15/3c4160255c9d4d73841cc2ca32ca9f08.webp)

8. When prompted `Configure DM access policies now?`, select "**No**" and press Enter.

![](https://file-us.ugreennas.com/admin/article/2026-05-15/79bac8204c904a52b31db2ae506aaa64.webp)

9. Open Telegram, find your bot, and send the command `/start`. The system will return a unique pairing code (e.g., `7CDZV796`).

![](https://file-us.ugreennas.com/admin/article/2026-05-15/5852b2dbd2f5487b951fcc21e2166dfc.webp)

10. Return to the NAS container terminal and enter the following command (replace `7CDZV796` with your actual code), then press Enter:

```
openclaw pairing approve telegram 7CDZV796
```

![](https://file-us.ugreennas.com/admin/article/2026-05-15/0c3e2a0287e44a64b3f0aee66e0c5201.webp)

11. After authorization is approved, go back to the Telegram chat and send any message to the bot. If you receive a valid response, the integration has been successfully completed.

![](https://file-us.ugreennas.com/admin/article/2026-05-15/5aa78211f9af4aadae67ea566f472a91.webp)

## Related Reading

### OpenClaw User Guide

<https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmODA5IiwiY2xpZW50VHlwZSI6IiJ9>

### How to Add and Switch Models in OpenClaw

<https://support.ugnas.com/knowledgecenter/#/detail/eyJjb2RlIjoiMiYmODIzIiwiY2xpZW50VHlwZSI6IiJ9>

## Common LLM API Configuration

When configuring external large language models for your application, you typically need to provide the correct API endpoint (URL) and model ID. Below are reference configurations for commonly used models.

### OpenAI (GPT Series)

When configuring the OpenAI API, choose either the base URL or the full request URL based on your application’s requirements:

● Base URL:

```
https://api.openai.com/v1
```

● Full Request URL (Chat Completions):

```
https://api.openai.com/v1/chat/completions
```

### Google Gemini

When configuring the Google Gemini API, the request URL must be constructed by combining the base template with a specific model ID.

1. API Endpoint Template

Replace `{model}` with the actual model ID you want to use:

```
https://generativelanguage.googleapis.com/v1/models/{model}:generateContent
```

2. Example of a Complete Endpoint

For example, using `gemini-3.1-flash-lite-preview`:

```
https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-lite-preview:generateContent
```

3. Available Gemini 3 Series Model IDs

Select a model based on your token quota and task requirements:

● `gemini-3.1-flash-lite-preview`

● `gemini-3.1-flash-image-preview`

● `gemini-3.1-pro-preview`

● `gemini-3-flash-preview`

● `gemini-3-pro-image-preview`

## Security Risk Notice

● **Root Privileges and High-Risk Operations**: This application runs with **root privileges** inside a Docker container to support automation tasks. It can read/write/delete files, publish external messages, and execute system commands. **Only grant access to trusted directories and avoid mounting sensitive data paths**.

● **No Multi-Tenant Isolation**: By default, the Hermes Agent is designed for a single trusted user. It does not provide multi-user isolation. If shared, all users will have the same permissions.

● **Public Network Exposure Risks**: Do not expose the service to the public internet unless you are familiar with security hardening and access control. **UGREEN NAS does not provide guidance for public deployment**—consult professionals if needed.

● **Content Compliance**: When interacting externally (e.g., via messaging bots), ensure compliance with platform policies and local laws. Users are responsible for all AI-generated content.

● **Disclaimer**: This application is provided solely as a service integration tool. The provider offers deployment support only and makes no guarantees regarding the security, stability, or functional completeness of the OpenClaw software itself. Any customization, configuration choices, or operational decisions made by the user—and all resulting legal, financial, or data-related risks (including but not limited to data breaches, device damage, cost overruns, or legal disputes)—are the sole responsibility of the user. The provider assumes no liability.
