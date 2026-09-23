# Uliya AI Assistant User Guide

> **Article ID**: `850`  
> **Category**: `Application Guide > Uliya > Uliya AI Assistant User Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/850  

---

## Applicability

**Applicable Models**: iDX Series

**Applicable Clients**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: UGOS Pro firmware 1.19.10.0013 or later

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

**Uliya** is the intelligent assistant built into UGOS Pro. Through natural-language conversations, it can handle complex tasks such as file organization, media recommendations, and document processing. You can also upload documents to build a personal knowledge base, transforming your NAS from a storage device into an intelligent assistant that understands content and carries out tasks.

Core capabilities include:

● **Smart task assistant**: Give instructions in natural language, and Uliya automatically plans and carries out multi-step tasks while displaying the reasoning and execution process.

● **Intelligent Tools**: A knowledge-rich product Q&A encyclopedia that provides quick answers and easy access to information without complex task coordination.

● **Knowledge Base**: Upload documents to build a personal knowledge base for document-based search and Q&A.

● **Tools**: Install and use various Skills to continuously expand Uliya's capabilities.

● **Assistants Team**: Uliya includes multiple professional "**Assistants**" (such as the Media & Entertainment assistant and Photo assistant), each specializing in a specific field.

### Assistant Team Overview

Uliya includes multiple professional "**assistants**" (sub-agents), each specializing in specific types of tasks to provide more precise assistance. The currently built-in assistants and their areas of expertise are as follows:

|  |  |
| --- | --- |
| **Assistant Name** | **Specialty** |
| Media & Entertainment assistant | Personalized film recommendations, media collection search, subtitle search, playback control |
| Photo assistant | Photo search, photo organization, album management |
| Surveillance assistant | Surveillance event queries, identity recognition, evidence retrieval |
| File management assistant | File search, organization and archiving, duplicate cleanup, batch renaming, tag management |
| Document assistant | Document summaries, document Q&A, cross-document search, document translation, OCR and information extraction, writing assistance |
| Learning assistant | Topic search and Q&A, note organization and linking, knowledge graphs, mind maps and review plan generation, audio transcription |

**Note**:

● The available assistants list may vary slightly by device model. Please refer to the actual interface.

● File management assistant, Document assistant, and Learning assistant are file-based assistants. You must upload a file before sending a task. If no file is selected, the "**Send**" button is disabled.

## Installation and Access

1. Open "**App Center**" and find the "**Uliya**" app.

2. Click "**Install**" and follow the setup wizard to complete the installation.

3. After installation, you can quickly open Uliya in either of the following ways:

● Click the Uliya icon on the desktop.

● Click the Uliya shortcut in the upper-right corner of the desktop.

## Model Download & Authorization

When using Uliya for the first time, the system guides you through downloading and authorizing the required models. Follow the on-screen instructions and click "**Download**". In the "**Model Manager**" app, download and authorize the following models:

● **Large Language Models**: Used for personal knowledge bases, file conversations, summaries, translation, mind maps, reasoning, and task planning.

● **Semantic Search Models**: Used for knowledge base retrieval and semantic understanding.

● **Speech Recognition Models**: Used to understand speech content.

**Note**: Model downloads may take some time. Some models are large, so we recommend downloading them when network usage is low.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/b4b8d39e767c4656a854de1fb21e893f.webp)

**Note:**

● Model downloads may take some time. Please wait patiently. Some models are large, so we recommend downloading them when network usage is low.

● By default, the chat interface displays only "**Local Model**". To use "**Hybrid Mode**" or "**Cloud Model**", complete the following two configurations first:

1. Add a third-party cloud model in the "**Model Manager**" app.

2. Enable "**Cloud Models**" on the Uliya "**Settings**" page.

## Home Overview

The Uliya on the left sidebar contains the following menus:

![](https://file-us.ugreennas.com/admin/article/2026-09-15/bdd14d895bff49be8dd64c29b54eed08.webp)

● **Smart task assistant (Beta)**: Opens the main Smart task assistant page. Enabled assistants are listed below, and you can click one to quickly switch to its dedicated chat.

● **Intelligent Tools**: Opens the everyday Q&A and casual chat mode.

● **Knowledge Base**: Manage documents in your personal knowledge bases and perform document-based search and Q&A.

● **Assistants**: View all built-in assistants and their details. Click an assistant to enter its dedicated chat.

● **Tools**: View and manage installed Skills, and install system-recommended tools as needed.

The sidebar also displays **recent conversations from the past 30 days**, sorted in reverse chronological order. Click any history entry to open the task details page and view the complete execution chain and results. At the bottom, click "**Settings**" to open the Settings page.

## Smart Task Assistant

"**Smart task assistant**" is Uliya's main interface for handling complex tasks. Describe what you need in natural language, and Uliya will understand your intent, plan the steps, and carry out the task.

### Task Workspace

On the "**Smart task assistant**" page, you can view Uliya's **scenario cards**, which cover common scenarios such as identity recognition, media recommendations, and photo management. Click a card to quickly start a task.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/7d1279a9f46f4afb85cd2cbaf0101070.webp)

If you want to ask freely, you can enter your task directly in the input box. For example, enter “Recommend a few comedy films from my Theater library for the weekend,” then click Send to start the task.

**Note**:

● After entering an instruction on the Smart task assistant main page, the system automatically assigns the most suitable assistant based on your intent.

● On the main page, you can use **@** to manually assign an assistant to the task. You can also @ multiple assistants, and the system will automatically coordinate them.

● After entering an assistant's dedicated page, the conversation is locked to that assistant. You cannot invoke or @ other assistants. To switch assistants, select another assistant from the assistant list.

### Scenario Cards

Scenario cards are divided into two types:

● **Main Page Cards**: Recommend three of the most common scenarios: Album creation, Recommendations, and Identify recognition.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/2f9b3e760c3c4537a23185c9d4db2f03.webp)

● **Assistant-Specific Cards**: On an assistant's dedicated page, these cards show the assistant's most commonly used Skill scenarios.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/0b59ff2d61a049e8bb2136cd27958dc3.webp)

Click any card and the system automatically fills the instruction into the input box. After confirming the instruction, click "**Send**" to start the task.

### Chat and Task Execution

During a conversation, use the toolbar at the bottom of the input box to control the task in more detail:

● **Model Selection**: Choose "**Hybrid mode**" (the system automatically selects the best model), "**Local model**" (runs locally for protect privacy), or "**Cloud model**" (provides stronger reasoning capabilities but involves privacy risks).

**Note:** "**Hybrid Mode**" and "**Cloud Model**" are displayed only after you add a cloud model and enable "**Cloud Model**" in "**Settings**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/05404c192f9e4c1db638200543284255.webp)

● **Authorization Method**: Choose an authorization method based on your needs. Select "**Ask each time**" (the system always asks before editing files, using the internet, or performing security-sensitive actions) or grant "**Full access**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/d89d79da6787492e960d8ace9e6a6aa5.webp)

● **Tool Selection**: On an assistant's dedicated chat page, you can manually select the Skills required for the current task. You can also leave this unspecified and let Uliya automatically match the best tools.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/1e194332398c44fb8fc01ca09ee8b186.webp)

You can view all conversations in the **history** on the left side of the page and click any entry to view its details. While a task is running, you can **pause** or **interrupt** it at any time.

### Reasoning & Execution Chain

Uliya **displays the complete reasoning and execution process** **in real time** while handling complex tasks, so you can clearly follow the progress of each step (such as Uliya’s reasoning and analysis and the tools it invoked).

![](https://file-us.ugreennas.com/admin/article/2026-09-15/a730b0b77cad4f5c870899fe8c3faf79.webp)

After the task is complete, the execution chain automatically collapses and displays a **structured result card**. For example:

● **File Organization Task**: Shows the number of categorized files and the destination path. Click to open the corresponding folder.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/bdd7f21d74a64f4092086d35f4430a42.webp)

● **Film Search Task**: Shows the poster, film title, and year.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/0f6dfc5c61864db2aef873be98a46dac.webp)

● **Photo Search Task**: Shows photo thumbnails. Click to open Photos and locate the corresponding photo.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/aa17f505b5fb40a181e0985327c4331a.webp)

## Intelligent Tools

"**Intelligent Tools**" is designed for everyday Q&A and casual chat. It is ideal for quickly getting helps with using the product, general information, or answers to everyday questions. No complex task coordination or tool invocation is required. The page also provides suggested prompts that you can click to ask a question quickly (for example, "Which RAID type should I choose?").

### Core Components

**AI Tools Shortcuts**: Provides quick access to four core AI capabilities so you can quickly switch between modes.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/1a7bdc768950449ea657980171a18270.webp)

● **Knowledge base Q&A**: Searches and answers questions based on your personal local knowledge base.

● **Summary**: Upload a file or enter text to quickly extract key points and automatically generate a mind map.

● **Smart Translation**: Upload a file or enter text to quickly translate it into the desired language. Supports translation between Chinese, English, German, and Japanese.

● **Smart Commands**: Select a command or enter a task instruction in natural language to have the device automatically perform the corresponding action (such as searching for photos).

![](https://file-us.ugreennas.com/admin/article/2026-09-15/dac0def20e1549eb86918eea0733abe8.webp)

**Model Switcher**: Displays the current AI model (such as Qwen). Click the drop-down arrow to switch to another deployed local or third-party cloud model as needed (more models can be added; for details, see "[Model Management (DXP Series)](https://support.ugnas.com/knowledgecenter/detail/article/en-US/831?clientType=PC) ").

![](https://file-us.ugreennas.com/admin/article/2026-09-15/36bf65b40488436cb104e4417c928ee3.webp)

**Online Search**: When enabled, both local and cloud models can answer based on online search results. **Google** is the default search provider for overseas devices, while **Baidu** is the default search provider for devices in China.

**File Upload**: Click the "**+**" icon to upload files from local storage or the NAS (supports formats such as docx, txt, pdf, png, jpg, and jpeg) for analysis and processing.

### Differences from Smart Task Assistant

|  |  |  |
| --- | --- | --- |
| **Dimension** | **Smart Task Assistant** | **Intelligent Tools** |
| Core Purpose | Complex multi-step task execution | Everyday Q&A and casual chat |
| Reasoning Chain | Displays the complete execution chain | Simplified display or not shown |
| Tool Use | Proactively invokes Skills | Invokes tools as needed, mainly for lightweight tasks |
| Output Format | Structured cards + actionable | Primarily plain text |

On the "**Intelligent Tools**" page, you can enter a question directly, and Uliya will answer based on general knowledge or online search results.

## Knowledge Base

"**Knowledge Base**" is used to manage documents in your personal knowledge bases. Upload documents to a knowledge base, and Uliya can search and answer questions based on their content, turning your NAS into your personal knowledge hub.

### Create Knowledge Base

1. Click "**Knowledge Base**" in the sidebar to open the knowledge base management page.

2. Click "**Create knowledge base**", set a name for the knowledge base, and upload files from local storage or the NAS (supports formats such as docx, txt, pdf, png, jpg, jpeg).

3. After creating the knowledge base, select it on the Knowledge Base Q&A page and enter a question to get an answer based on the knowledge base content.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/22b623ee083849d7a3d01b96cd7f99c4.webp)

**Note**:

● The maximum size for a single file is 100 MB. Files exceeding this limit cannot be added.

● Knowledge Base Q&A **does not support online search**. Answers are based only on documents in the knowledge base.

### View & Manage Knowledge Base

On the Knowledge Base Q&A page, you can view the number of files and total storage used by each knowledge base.

Hover over a knowledge base and click the "**···**" icon to manage the knowledge base, clear its files, or delete it.

Double-click a knowledge base to open its management page, view details, and manage it.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/dffda281ec744a7cb54d96f677f2560d.webp)

## Assistants

Uliya includes multiple professional "**Assistants**" (sub-agents). Each assistant focuses on specific types of tasks to provide more precise assistance.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/ebf1d74aa60b467aa2512e45d1e43e31.webp)

### Use Assistants

You can use assistants in either of the following ways:

**Method 1: @ an assistant in Chat**

Enter the "**@**" symbol in the input box and select an assistants to assign the current task to that assistant.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/e518f19490e840a8a42e9e52a17faa41.webp)

**Method 2: Use an assistant from the assistants Page**

1. In the Uliya sidebar, click "**assistants**".

2. In the "**My assistants**" list, find the assistant you want to use.

3. Click "**Chat**" on the assistant card. The system automatically switches to that assistant's dedicated chat page.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/79ca9be76a934c9a9af1e97bc6794fb7.webp)

On the assistant's dedicated page, you can view **assistant-specific scenario cards** covering the assistant's most commonly used Skill scenarios. Click a card to quickly start a task.

### Assistant Details

Click an assistant card to view detailed information, including:

● System Prompts (to learn about the assistant's role, capability boundaries, and more)

● Associated Skills

![](https://file-us.ugreennas.com/admin/article/2026-09-15/ae26226905d14e48abdcd3cf0dc805c4.webp)

## Tools

"**Tools**" is Uliya's capability expansion center for managing Skills. Installed tools can be invoked by Uliya in "**Smart task assistant**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/7ae62aa628b944d68f171ff5e404baec.webp)

### My Tools

Displays all installed tools. Click a tool card to view details about the corresponding Skill.

● **Use Tool**: Click "**Use**" at the bottom of a tool card to quickly create a new task that references that tool.

● **Delete Tool**: Click a tool card and delete an unwanted tool from the tool details page.

**Note**: Built-in tools are preinstalled by the system and cannot be deleted. Only tools you install yourself can be deleted.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/63566d5f04ee4228a314adecf822fae7.webp)

### Recommended Tools

Displays recommended tools that can be installed. To expand Uliya's capabilities, find and install the Skills you need from the list.

**Install Tool**: Click "**Install**" on a tool card, select the assistant you want to install it for, then click Confirm to complete the installation.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/646269afd9c74d11a90ff807403d4c28.webp)

After installation, the card automatically moves to "**My tools**" and the tool can be selected for use in the corresponding assistant chat interface.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/dbaf62c9b507469db29ff3412170f8a2.webp)

## General Settings

On the "**Settings**" page, you can configure the following Uliya options:

![](https://file-us.ugreennas.com/admin/article/2026-09-15/d561b9581f3c4d61983d198a8a16a07b.webp)

● **Cloud model**: When enabled, you can select deployed third-party cloud models in chats. Documents uploaded during chats and knowledge base content are sent to the selected cloud model for analysis and processing.

● **Online search**: When enabled, Uliya analyzes and answers questions based only on online search results. Administrators can configure the maximum number of search results, compression method, and truncation length to balance the level of detail in the returned content and system performance.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/08c486540ae248c18dced127077a3b14.webp)

● **GPU Acceleration**: If the device has a dedicated graphics card, enabling this option lets the model use the dedicated GPU to improve inference and processing speed.

● **Upload Location**: Click "**Open**" to quickly locate where Uliya's historical chat data is stored.

● **Clear Chat History**: Click to delete all chat records with Uliya.

### Mobile Remote Control

You can bind Uliya to instant messaging (IM) apps. Once bound, you can chat with Uliya remotely through an IM app such as WeChat and send instructions directly. For example, send "Find a photo of a car in my Photos library" in WeChat. Uliya will carry out the task and return the result, allowing you to manage your NAS remotely from anywhere.

Supported IM channels include WeChat, WhatsApp, and Telegram (The supported channel types and binding methods vary by region. Please follow the on-screen instructions.).

**Binding Method** (using WeChat as an example):

1. On the Settings page, find "**Mobile remote control**".

![](https://file-us.ugreennas.com/admin/article/2026-09-15/1aeaa9b4a0bd446fa1b895a99c4a41fb.webp)

2. Select the IM channel you want to bind and follow the on-screen instructions to complete authorization (scan a QR code or enter Token information).

![](https://file-us.ugreennas.com/admin/article/2026-09-15/6e2dbcf87f9a46c9a524024b1a2b4412.webp)

3. After binding is complete, you can chat with Uliya through the IM app and remotely manage the device.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/3cd07588ba2c4f579ad61a966ae4b8bc.webp)

**Note**:

● When the authorization service expires, the system will notify you that the connection is no longer valid and prompt you to reauthorize it. Simply complete the binding process again.

● After binding, conversations started in the IM app share the same memory and context as the web version, allowing you to switch between clients and continue the task at any time.

## FAQs

### Q1: Why Can't I Find the Uliya App on My NAS?

Uliya AI Assistant is supported on **iDX Series** devices. If your device model is not supported, the app will not appear in App Center.

### Q2: How Long Does It Take to Download the Models the First Time?

Download time depends on the model size and network speed. Large language models usually take longer to download. We recommend downloading them when network usage is low and keeping the device powered on and running normally during the download.

### Q3: Can I Interrupt a Smart task assistant While It Is Running?

Yes. While a task is running, click "**Stop Generating**" in the chat interface to interrupt the current task. Steps that have already been completed are retained.

### Q4: What's the Difference Between assistants and Tools in the Toolbox?

● **Assistants** are "**professional assistants**" for specific domains, with full task planning and execution capabilities.

● **Skills in the Tools** are single-function "Skill packages" used to extend the specific capabilities of Uliya and its assistants. assistants and Skills work together to complete complex tasks.

### Q5: Can a Single Task Use Multiple assistants at the Same Time?

Yes. Uliya supports multi-assistant collaboration. For example, on the main Smart task assistant page, @**Surveillance assistant** @**Photo assistant** and enter the task "**Find the cat in the surveillance footage and save it to Photos**". Uliya automatically coordinates the assistants to work together.

![](https://file-us.ugreennas.com/admin/article/2026-09-15/61ef3cb565b84fac9b10ee796bb9f393.webp)
