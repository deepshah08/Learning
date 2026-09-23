# Deploying the Exameow AI Exam Question Generator with Docker

> **Article ID**: `927`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Deploying the Exameow AI Exam Question Generator with Docker`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/927  

---

## Introduction

**Exameow** is an open-source AI-powered exam question generator. It supports uploading PDFs, Word documents, PowerPoint presentations, spreadsheets, images, and text files. AI automatically analyzes the uploaded content and generates exam questions.

Exameow supports the following Question Types:

● Single Choice

● Multi Choice

● True / False

● Fill Blank

● Short Answer

Exameow also provides Practice, Generate, and Search features. You can configure AI compute resources, generate and export questions, launch exams, and view practice and exam records.

**Project URL**: [exameow/README\_zh.md - GitHub](https://github.com/heshengtao/exameow/blob/main/README.md)

**Note**: This article uses deployment with Docker Compose as an example. Pages and parameters may vary slightly depending on the system version, Docker app version, or Exameow version. Refer to the actual interface and the project documentation.

![](https://file-us.ugreennas.com/admin/article/2026-08-13/d5126cea2f91423eab39098eed5afcd2.webp)

## Features

Exameow provides the following key features:

● **AI Question Generation**: Upload study materials and automatically generate questions.

● **Practice**: Import a question bank and practice questions.

● **Exam**: Publish an exam and generate a verification code so other

● **Search**: Search for questions by text or photo.

● **Question Export**: Export questions as CSV or XLSX files.

● **AI Configuration**: Configure an OpenAI-compatible API.

## What File Formats Are Supported?

Exameow supports the following file formats: PDF, DOCX, XLSX, PPTX, EPUB, ODT, TXT, CSV, HTML, PNG, JPG, WEBP, GIF, and BMP.

Multiple files can be uploaded by drag and drop. Before uploading, make sure the files are clear and well structured. Higher-quality source documents generally result in more accurate AI-generated questions.

## What AI Models Are Supported?

Exameow supports OpenAI-compatible APIs and can work with the following models and services:

● OpenAI: GPT-4o、GPT-4、GPT-3.5

● DeepSeek

● Qwen

● Zhipu GLM

● Self-hosted models running through tools such as Ollama

● Other OpenAI-compatible API services

During deployment, enter the API endpoint, API key, and model name based on the AI service you are using.

## Docker Compose Configuration

Create a Compose project in the Docker app and enter the following configuration:

```
services:
  exameow:
    image: ailm32442/exameow:latest
    container_name: exameow-server
    ports:
      - "3060:3000" # Access port
    environment:
      - AI_ENDPOINT=https://api.deepseek.com # OpenAI-compatible API endpoint
      - AI_API_KEY=Replace with your API Key # AI API key
      - AI_MODEL=deepseek-v4-flash # Model
      - PORT=3000  # Service port
      - RUST_LOG=info # Log level
      - ADMIN_TOKEN=123456 # Admin access token
      - EXAM_DB_PATH=/app/data/exameow.db # SQLite database path for online exams
      - ADMIN_TOKEN_FILE=/app/data/admin_token.txt # Persistent file for the updated admin token
    volumes:
      - ./data:/app/data # Data storage location
    restart: always
```

## Deploy Exameow

1. Open the "**Docker**" app, go to the "**Project**" page, and click "**Create**".

2. Enter a project name and paste the Compose configuration.

3. Replace `AI_API_KEY` with the API key you are using.

4. Modify `AI_ENDPOINT` and `AI_MODEL` based on your AI service.

5. Click "**Deploy**".

After deployment is complete, wait for the container to start properly.

## Access Exameow

After deployment, enter `http://NAS_IP:3060` in your browser. Replace `NAS_IP` with the actual LAN IP address of your NAS.

Example: `http://192.168.1.100:3060`

If Exameow cannot be accessed, check the following:

● Whether the container is running properly

● Whether port 3060 is already in use

● Whether the NAS IP address is correct

● Whether your computer and NAS are on the same LAN

● Whether the Docker project logs contain any errors

## Page Navigation

The Exameow page includes the following navigation options:

● **Practice exercises**

● **Question Setting**

● **Search for topics**

● **Mine**

The top-right corner of the page provides the following options:

● Switch the display language

● Switch the page theme

● Open the GitHub project page

![](https://file-us.ugreennas.com/admin/article/2026-08-13/162e66ef857b4a1db6d959cda927929b.webp)

## Practice Exercises

Click "**Practice exercises**" in the top navigation bar to open the question bank page. On the Practice exercises page, you can select an imported question bank for practice or import a new one. Question banks can be imported in CSV or XLSX format.

![](https://file-us.ugreennas.com/admin/article/2026-08-13/57a2133f1fa948b681597880acf49bfa.webp)

Before starting, you can select a practice mode. Three practice modes are available. Refer to the actual interface for the options provided.

![](https://file-us.ugreennas.com/admin/article/2026-08-13/50be92365ed1484a9e0c808975384446.webp)

After you start practicing, you can switch between Practice mode and Memorization mode. Memorization mode displays the answers directly, making it suitable for review and memorization.

![](https://file-us.ugreennas.com/admin/article/2026-08-13/2c6397ad47d34ae991570abbe3021b9f.webp)

After you submit your answers, the practice results are displayed.

![](https://file-us.ugreennas.com/admin/article/2026-08-13/f2352c6b6ef6435c940f1b4d36c86073.webp)

## Question Setting

Click "**Question Setting**" in the top navigation bar to use the AI question generation feature. Follow these steps:

1. Go to the "**Question Setting**" page, click "**Select Document**", and upload the source files you want to generate questions from.

2. Select the question types, difficulty, and language, and enter Key Points / Chapters as needed.

3. Click "**Generate test questions**".

After generation is complete, the generated questions are displayed in a list at the bottom of the page. If the results do not meet your expectations, click "**Reissue the question**" to generate the questions again.

![](https://file-us.ugreennas.com/admin/article/2026-08-13/f0a222ea22e24f6890af4f773a06dac4.webp)

### Export Test Questions

After the test questions are generated, you can export them as a file in CSV or XLSX format. Follow these steps:

1. Make sure the test questions have been generated.

2. Click **CSV** or **XLSX** on the page.

3. Follow the browser prompts to download the file.

The exported file can be used for further organization, backup, or import into other systems.

![](https://file-us.ugreennas.com/admin/article/2026-08-13/a9b0f01e951549de8031bd195dcaa686.webp)

### Exam Release

After the test questions are generated, click "**Exam release**" to publish the exam. Once published, it can be used to initiate an exam. For specific exam settings and participation methods, refer to the prompts on the actual page.

### Take an Exam

In the upper-right corner of the Question Setting page, the following options are available:

● **Initiate the exam**

● **Take the exam**

To create an exam, click "**Initiate the exam**". To join an exam using information provided by someone else, click "**Take the exam**".

## Search for Topics

Exameow supports question search. The Docker-deployed web version supports:

● Text search topic

● Take photos and search for topics

The Docker-deployed web version currently does not support:

● Screen recording to search questions

● Tap the screen to search for topics

To use screen recording or camera-based screen search, go to the GitHub project page to download the Android client. Available features depend on the actual client version.

![](https://file-us.ugreennas.com/admin/article/2026-08-13/34168d925dbf4089aa6eb04b0273a8d5.webp)

## Configure AI Computing Power

When using the question generation feature, Exameow prioritizes the AI configuration specified in the Compose file, such as the API endpoint, API key, and model name.

To use a different AI service, you can also configure it on the Exameow page. Follow these steps:

1. Click "**Mine**" in the top navigation bar.

2. Click "**Computing power configuration**" to open the configuration page.

3. Click "**Customize the API**", enter the API endpoint and API key, and then click "**Get a list of models**".

4. Select the model you want to use.

5. Click "**Save the configuration**".

After the configuration is saved successfully, you can use the selected AI service to generate questions.

## What If the Image Fails to Pull

If the image fails to pull during deployment, check the project deployment logs.

If the following appears in the logs, it usually indicates an issue pulling the image from Docker Hub:

```
https://registry-1.docker.io/v2/
```

Configure a registry mirror or image proxy, and then redeploy the project. For detailed instructions, refer to the UGREEN NAS Docker guide "[How to Configure Registry Images, Image Sources, and Image Proxy in Docker?](https://support.ugnas.com/knowledgecenter/detail/article/en-US/297?clientType=PC)".

## Notes

● Exameow is a third-party open-source project. Features and interfaces may vary depending on the actual project version.

● AI-generated content may contain inaccuracies or misinterpretations. Manually review the questions before using them in a formal exam.

● Keep sensitive information such as `ADMIN_TOKEN` and `AI_API_KEY` secure.
