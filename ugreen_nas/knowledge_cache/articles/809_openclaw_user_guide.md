# OpenClaw User Guide

> **Article ID**: `809`  
> **Category**: `Application Guide > Docker > Container Application > OpenClaw User Guide`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/809  

---

## Overview

**OpenClaw** is a personal AI assistant that runs locally on your device. It interacts with users through common communication channels. The UGREEN NAS version has been deeply customized to provide a "**one-click**" installation experience, enabling a fully no-code deployment workflow.

This guide will walk you through deploying the Google Gemini model engine within OpenClaw, as well as configuring authentication for the Telegram interaction channel.

**Note**: This application consumes significant system resources. Ensure your system has at least **2 GB** of available RAM. The installation process may take more than **10 minutes**, which is normal.

### Supported Models

The following NAS models currently support the OpenClaw application (more models are being added):

● DXP Series: DXP2800, DXP4800, DXP4800 Plus, DXP4800 Pro, DXP6800, DXP6800 Plus, DXP6800 Pro, DXP8800, DXP8800 Plus, DXP8800 Pro, DXP480T Plus

● iDX Series: iDX6011, iDX6011 Pro

## Prerequisites

Before installing OpenClaw, go to the "**App Center**" on your UGREEN NAS and make sure that the **Docker** application is installed and updated to the latest version.

**Note**: OpenClaw relies heavily on the Docker container environment. If the Docker version is outdated, it may cause deployment failures, incorrect permission configurations, or runtime issues.

### Get a Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/) , sign in with your Google account, then click "**Get API key**" in the left sidebar and select "**Create API key**".

![](https://file-us.ugreennas.com/admin/article/2026-05-18/ddfefdae361e479995749c4ef4da2fec.webp)

2. Choose an existing project or create a new one.

3. After selecting the project, click "**Create Key**".

![](https://file-us.ugreennas.com/admin/article/2026-05-18/92aee88c4f794539823e27ac9d254aa0.webp)

4. Copy and securely store the generated API Key.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/27c675963d4344b68bc106bfea545ae0.webp)

### Create a Telegram Bot

● Log in to Telegram and search for the official bot management tool `@BotFather`.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/78a96db03e0c4a38bd6e1986f359eff2.webp)

● Send the command `/newbot` to start the creation process.

● Follow the prompts to configure:

**Bot Name**: The display name of your bot.

**Bot Username**: A globally unique identifier that must end with `bot` (e.g., `my_openclaw_bot`).

● After creation, copy and securely store the **Bot Token** provided by the system (example format: `1234567890:AAxxxxxxxxxxxxxxxxxxxxxxxx`).

![](https://file-us.ugreennas.com/admin/article/2026-05-18/70f6aef664fa41a5bbb47829064f9b20.webp)

## Step 1: Install the Application

Log in to your UGREEN NAS, go to the "**App Center**", find **OpenClaw** under the "**All**" list, and click "**Install**".

![](https://file-us.ugreennas.com/admin/article/2026-05-18/15f81b2c3f5049fdb8fc586f601234dd.webp)

## Step 2: Installation and Configuration

When installing the OpenClaw application, you must first complete the system path and model interface settings on the "**OpenClaw installation configuration**" page.

### Path Configuration

This section defines the file access scope for OpenClaw. For data security, grant permissions carefully.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/1670209d461b4924956e2c04f6a33910.webp)

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

![](https://file-us.ugreennas.com/admin/article/2026-05-18/b7f4aa6706c2479ba20463d0362337ca.webp)

### Complete the Installation

After confirming that the above configurations are correct and fully understanding the associated risks, select "**I have read and understand and the installation risks**" in the lower-left corner of the page. Then click "**Install**" in the lower-right corner to begin deploying the application.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/9b67a041157e4992b6b767ba60100f84.webp)

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

![](https://file-us.ugreennas.com/admin/article/2026-05-18/314c499176454ac7b1a99d58b2d4ec1c.webp)

### Step 2: Verify Connection Status

After a successful connection, you can confirm that the gateway is active through the interface:

● Click "**Overview**" in the left sidebar.

● Locate the "**Snapshot**" card on the right side.

Its status should display as green"**OK**"

![](https://file-us.ugreennas.com/admin/article/2026-05-18/41d98bbc13ab43e8b8b7b989ecc8d7f0.webp)

### Step 3: Start Using the AI Assistant

The UGREEN NAS version comes with the high-performance MiniMax 2.1 large language model deeply integrated, eliminating the need for complex model or API configuration.

1. Click "**Chat**" in the left sidebar to return to the conversation interface.

2. Enter your question or command in the input box at the bottom of the page.

3. Click the "**Send**" button (paper plane icon). You can now start interacting with your AI assistant.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/48f815c24d0c4b24844852aff6d8005b.webp)

## Connect to a Telegram Bot

Before configuring a third-party bot, you need to access the system command line via the terminal:

1. Open the "**Docker**" app, click "**Project"** in the left sidebar, then find the "**openclaw**" project and open its details.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/d3f2a8cc179847eeacf28b9877d482ea.webp)

2. Select the corresponding container and switch to the "**Terminal**" tab.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/b93313f5b24441ea9312e463523cabfd.webp)

3. Click "**Add**" in the Terminal tab.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/2ca853f64e0f47d0ab193a5f1ea3d733.webp)

4. In the pop-up command box, enter `/bin/bash` and click "**Confirm**" to create the session.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/81ac60cda9f146428917334a8ab36af8.webp)

5. In the terminal window, enter the following command and press **Enter**: `openclaw configure`

![](https://file-us.ugreennas.com/admin/article/2026-05-18/b5deba05551945e8b121f36b1ef6a393.webp)

6. Follow the prompts and make the following selections (press Enter after each selection):

● `Where will the Gateway run?` → Select "**Local (this machine)**".

![](https://file-us.ugreennas.com/admin/article/2026-05-18/36208789b3ae441a9bfe0bd192a5cb1a.webp)

● `Select sections to configure` → Select "**Channels**".

![](https://file-us.ugreennas.com/admin/article/2026-05-18/524ac16126564617a968b646dcc41723.webp)

● `Channels`→ Select "**Configure/link**".

![](https://file-us.ugreennas.com/admin/article/2026-05-18/a6d148d90a8947fe9166beff638a1a94.webp)

● `Select a channel` → Select "**Telegram (Bot API)**"

![](https://file-us.ugreennas.com/admin/article/2026-05-18/4744615e10d645f0b5a218baf747d30b.webp)

● `How do you want to provide this Telegram bot token?`→ Select "**Enter Telegram bot token**".

![](https://file-us.ugreennas.com/admin/article/2026-05-18/b38069522ab943afa632b48109891927.webp)

● `Enter Telegram bot token` → Paste your Telegram Bot Token and press **Enter**.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/7c1eacbeecd547fa9112cbd6f64bd7d4.webp)

7. After entering the token, the system will return to the channel selection screen. Select "**Finished**" and press Enter.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/c1447b83fdfa43e2885138bd03d8357d.webp)

8. When prompted `Configure DM access policies now?`, select "**No**" and press Enter.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/4aabc53b75e046f6a6f9512446c29aae.webp)

9. Open Telegram, find your bot, and send the command `/start`. The system will return a unique pairing code (e.g., `7CDZV796`).

![](https://file-us.ugreennas.com/admin/article/2026-05-18/67527b28515d47b99d6704115e560db5.webp)

10. Return to the NAS container terminal and enter the following command (replace `7CDZV796` with your actual code), then press Enter:

```
openclaw pairing approve telegram 7CDZV796
```

![](https://file-us.ugreennas.com/admin/article/2026-05-18/5e10e477d1714bfc86054b504319e238.webp)

11. After authorization is approved, go back to the Telegram chat and send any message to the bot. If you receive a valid response, the integration has been successfully completed.

![](https://file-us.ugreennas.com/admin/article/2026-05-18/aa6935b8fca54163970500ae521c725c.webp)

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
