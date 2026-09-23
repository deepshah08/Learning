# How to Add and Switch Models in OpenClaw

> **Article ID**: `823`  
> **Category**: `Application Guide > Docker > Container Application > How to Add and Switch Models in OpenClaw`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/823  

---

## Overview

The OpenClaw system supports configuring and storing multiple large language models. However, during actual runtime interactions, only one model can be active at a time. To add or switch models, you can use natural language commands directly within the AI chat interface.

## Add a New Model

**Note:** Entering plaintext credentials in the chat interface carries security risks. Please ensure the environment is secure and that you can update credentials at any time.

**Steps:**

1. Open the OpenClaw web chat interface and type the command "**Add new model**" in the input box. Include the target model's full URL, API key, and exact model name in your message.

2. Click the "**Send**" button (paper plane icon) to submit the configuration command to the AI.

**Example Configuration Command (MiniMax model):**  
It's recommended to copy the format below and replace the parameters before sending:

```
Add new model
URL:https://api.minimaxi.com/v1
Key:sk-cp-Hr--1yfuqwdqnd1290e1u2okjflsau3AhZNd2d8u21dorDXhOVNEt2bC
Model:MiniMax-M2.7
```

![](https://file-us.ugreennas.com/admin/article/2026-04-16/5495172ab4ec4ac78eb95274dc61396c.webp)

## Configuration Activation and Verification

1. After receiving the command, the AI will confirm completion with a message such as "**Config written**", and the OpenClaw application will automatically restart.

![](https://file-us.ugreennas.com/admin/article/2026-04-16/1c5cde1a45a74b3dbf8d2c358c5ccef7.webp)

2. Once the restart is complete, log in again. Then enter the command `View models from configuration file` in the chat and send it. You can then view the list of all currently saved models in the system to verify whether the new model has been successfully added.

![](https://file-us.ugreennas.com/admin/article/2026-04-16/74db90a9ef2541d29e8f8e60d34454cd.webp)

## Switch Active Model

When multiple model configurations are stored in the system, you can seamlessly switch between them using a chat command.

1. In the chat box, enter `Switch model to + model name` .

**Example**: type `Switch model to MiniMax-M2.7` and send the message.

![](https://file-us.ugreennas.com/admin/article/2026-04-16/97cd248da732483e946ff21a449636ed.webp)

2. Once the system responds and confirms the switch, the selected model will be activated for conversations and automated task processing.

## Mainstream LLM APIs

|  |  |
| --- | --- |
| **Model / Platform** | **API Address (Base URL)** |
| **OpenAI (GPT-4/4o)**​ | `https://api.openai.com/v1` |
| **Anthropic (Claude)**​ | `https://api.anthropic.com/v1` |
| **Google Gemini**​ | `https://generativelanguage.googleapis.com/v1beta/openai` |
| **xAI (Grok)**​ | `https://api.x.ai/v1` |
| **OpenRouter (AI Aggregation Platform)​** | `https://openrouter.ai/api/v1` |
| **Groq**​ | `https://api.groq.com/openai/v1` |
| **Together AI​** | `https://api.together.xyz/v1` |
| **DeepSeek​** | `https://api.deepseek.com` |
| **Baidu Qianfan (ERNIE)** | `https://qianfan.baidubce.com/v2` |
| **Alibaba Tongyi (Qwen)​** | `https://dashscope.aliyuncs.com/compatible-mode/v1` |
| **Tencent Hunyuan** | `https://api.hunyuan.cloud.tencent.com/v1` |
| **ByteDance Volcano Engine (Doubao)** | `https://ark.cn-beijing.volces.com/api/v3` |
| **Moonshot AI (Kimi)** | `https://api.moonshot.cn/v1` |
| **Zhipu AI (GLM)** | `https://open.bigmodel.cn/api/paas/v4` |
| **iFLYTEK Spark** | `https://spark-api-open.xf-yun.com/v1` |
| **MiniMax​** | `https://api.minimax.chat/v1` |
| **SiliconFlow** | `https://api.siliconflow.cn/v1` |
