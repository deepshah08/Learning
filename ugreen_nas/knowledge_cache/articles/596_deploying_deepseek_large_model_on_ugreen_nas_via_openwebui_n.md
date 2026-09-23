# Deploying DeepSeek Large Model on UGREEN NAS via OpenWebUI + NVIDIA NIM API

> **Article ID**: `596`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Deploying DeepSeek Large Model on UGREEN NAS via OpenWebUI + NVIDIA NIM API`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/596  

---

In a previous article, we introduced [Deploy the DeepSeek large model on UGREEN NAS using OpenWebUI and the SiliconFlow API](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTgzOCwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo1OTEsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D). Besides SiliconFlow, NVIDIA’s NIM (NVIDIA Inference Microservices) platform also provides API support for the DeepSeek model. NVIDIA NIM is a high-performance inference service platform specifically designed to optimize the deployment and inference of large models. With NVIDIA NIM, users can deploy and manage the DeepSeek model more efficiently.

This tutorial will guide you step-by-step on how to obtain the API key from NVIDIA NIM, configure OpenWebUI, and ultimately deploy the DeepSeek large model.

## **1. Register and Log In to Your NVIDIA NIM Account**

First, visit the official NVIDIA NIM platform website: [NVIDIA NIM](https://build.nvidia.com/), then register and log in with your NVIDIA developer account.

After logging in, locate the DeepSeek model and click to enter its page.  
![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250523/631489ce-2dcf-4cf4-8d7e-074fb6376a81.webp)

## **2. Obtain NVIDIA NIM API Key**

On the DeepSeek model page, click Get Api Key, then in the popup window click Generate Key to create the key.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250523/1ed34272-a670-46b6-bf91-e83a01f61a02.webp)

The generated API key is the credential for accessing the NVIDIA NIM API. Please keep it safe and do not disclose it to others.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250523/d8bc282c-94b9-4f9b-9ee2-c561e7878028.webp)

## **3. Obtain the DeepSeek Model URL and Model ID**

In the [deepseek-r1 Model by Deepseek-ai | NVIDIA NIM](https://build.nvidia.com/deepseek-ai/deepseek-r1)page, copy the URL link and Model ID of the DeepSeek model you need.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250523/7a91f3e3-c5b1-4de0-848a-b7083a6f7453.webp)

## **4. Configure OpenWebUI**

Next, configure the API connection in OpenWebUI. If you have not yet set up OpenWebUI, please refer to the following tutorial:  
[Set up Open WebUI to deploy large language models on UGREEN NAS](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTgzMiwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo1OTAsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

### **4.1 Add NVIDIA NIM API Connection**

1. Log in to OpenWebUI and click on your user avatar to enter the Admin Panel.
2. From the left-hand menu, select Settings, then click Connections.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250523/563a2cd8-aab3-425e-a63d-8d74b089a6a7.png)

3. On the "Connections" settings page, locate and enable the OpenAI API toggle, then click the "+" button to add a new connection.
4. Enter the NVIDIA NIM API key, DeepSeek model URL, and model ID into the corresponding fields, then save the configuration.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250523/930ff1b9-d0de-41e7-8c5a-edebf4cfbd76.png)

## **5. Testing the connection**

In the OpenWebUI chat interface, select the NVIDIA NIM connection you just added to start testing.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250523/3fdb448c-a546-4e7a-a8dc-2435ffb7a4ea.png)

If the configuration is correct, you will see a normal connection status and can start using the DeepSeek model for conversations.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250523/f4a69490-6112-4414-8374-a87276d73329.png)

## **6. Common Issues and Solutions**

Below are some common problems you might encounter when using API connections with OpenWebUI, along with their solutions.

### **6.1 Connection Failure**

* **Possible Cause:** Incorrect API key or URL.
* **Solution:** Verify that the API key and URL are correctly entered without extra spaces or characters.

### **6.2 Model Loading Failure**

* **Possible Cause:** Incorrect model ID or unauthorized model access.
* **Solution:** Confirm the model ID is correct and ensure your NVIDIA NIM account has sufficient quota.

### **6.3 Slow Response**

* **Possible Cause:** Network latency or high server load.
* **Solution:** Try switching to a different network environment, or contact NVIDIA NIM support to check the server status.

By following this tutorial, you have successfully deployed the DeepSeek large model on your NAS using OpenWebUI combined with the NVIDIA NIM API. NVIDIA NIM provides cost-effective large model services, and with OpenWebUI’s flexible configuration, you can easily build your own AI conversational system. If you encounter any issues during use, please refer to the common issues section or contact the official customer support of the respective platforms for assistance.
