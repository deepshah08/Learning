# Deploy the DeepSeek large model on UGREEN NAS using OpenWebUI and the SiliconFlow API

> **Article ID**: `591`  
> **Category**: `Application Guide > Docker > Docker Gameplay > Deploy the DeepSeek large model on UGREEN NAS using OpenWebUI and the SiliconFlow API`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/591  

---

This tutorial will provide a detailed guide on how to deploy the DeepSeek large model on UGREEN NAS using OpenWebUI in conjunction with the SiliconFlow API. SiliconFlow is a professional large model hosting platform that offers a variety of API services for large models. Through this tutorial, you will learn how to register for a SiliconFlow account, obtain an API key, configure OpenWebUI, and ultimately deploy the DeepSeek model successfully.

## **1. Register a SiliconFlow Account**

First, visit the official SiliconFlow website, [SiliconCloud](https://cloud.siliconflow.cn/models) to register an account. Fill in the required information to complete the registration process. It is recommended to enter an invitation code during registration to enjoy new user benefits. Currently, new users can receive a free credit of 14 RMB upon registration, and inviting new users will earn an additional balance reward of the same amount.  
![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250429/c91b50f9-0fd7-4321-a2d1-09e1120580ee.png)

## 2. **Obtain the API Key**

After completing the registration, log in to your SiliconFlow account and enter the main interface.

### 2.1 **Create an API Key**

* Click on "API Key" in the left-side navigation bar.
* Click on "Create New API Key," set a description for the key, and create the key.
* **Note:** The API key is your credential for accessing the SiliconFlow API. Please keep it safe and do not disclose it.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250429/478791bb-cb4e-4739-b17f-20fa8c32c780.png)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250429/5aa25237-b971-41a0-a572-6660ad00d819.png)

---

## **3. Obtain the DeepSeek Model URL**

In [the official SiliconFlow API documentation](https://docs.siliconflow.cn/cn/api-reference/chat-completions/chat-completions), locate the URL link for the DeepSeek model.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250429/0522cc4c-5c44-4a0c-b770-2efe0b5bf148.png)

Since we are using OpenWebUI for integration, simply copy the URL up to`v1`， without including the `/chat/completions` suffix.

```
https://api.siliconflow.cn/v1
```

## **4. Configure OpenWebUI**

If you haven't set up OpenWebUI yet, please refer to the following tutorial:  
[Set up Open WebUI to deploy large language models on UGREEN NAS](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTgzMiwidHlwZSI6InRhZzAwMiIsImxhbmd1YWdlIjoiemgtQ04iLCJjbGllbnRUeXBlIjoiUEMiLCJhcnRpY2xlSW5mb0lkIjo1OTAsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ%3D%3D)

### **4.1 Add SiliconFlow API Connection**

1. Log in to OpenWebUI and click on your user avatar to enter the Admin Panel.
2. In the left-side menu, select Settings, then click on Connections.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250429/c90882c0-67dc-401c-bc07-4a0cbe148e0f.png)

3. In the “Connections” settings page, locate and enable the OpenAI API toggle, then click the "+" to add a new connection.
4. Enter the SiliconFlow API key, URL link, and DeepSeek model ID in the corresponding fields, and save the configuration.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250429/aab8bc40-a84d-48f6-8f12-dae22a549625.png)

### **4.2 Obtain the DeepSeek Model ID**

In [the official SiliconFlow API documentation](https://docs.siliconflow.cn/cn/api-reference/chat-completions/chat-completions), locate the Available Options section and copy the required DeepSeek model ID. For example:

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250429/122e5c03-52a2-472d-9571-b9bc18ff84ea.png)

```
deepseek-ai/DeepSeek-R1
Pro/deepseek-ai/DeepSeek-R1
deepseek-ai/DeepSeek-V3
Pro/deepseek-ai/DeepSeek-V3
```

## **5. Test the Connection**

In the OpenWebUI chat interface, select the SiliconFlow connection you just added to begin testing.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250429/82b49895-2dc7-48d5-afd4-4a4c61f4ff7d.png)

If the configuration is correct, you will see that the connection status is normal, and you can start using the DeepSeek model for conversations.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250429/cff855e0-c881-45eb-bdb3-2e8937aa226a.png)

## **6. Common Issues and Solutions**

Here are some common issues you may encounter when using the OpenWebUI API connection and their solutions.

### **6.1 Connection Failure**

* **Possible Cause**: Incorrect API key or URL.
* **Solution**: Double-check the API key and URL for accuracy, ensuring there are no extra spaces or characters.

### **6.2 Model Not Loading**

* **Possible Cause**: Incorrect model ID or unauthorized model.
* **Solution**: Verify that the model ID is correct and check if your SiliconFlow account has sufficient credits.

### **6.3 Slow Response Speed**

* **Possible Cause**: Network latency or server overload.
* **Solution**: Try switching to a different network or contact SiliconFlow customer support to inquire about server status.

By following this tutorial, you have successfully deployed the DeepSeek large model on your NAS using OpenWebUI and the SiliconFlow API. SiliconFlow provides cost-effective large model services, and with the flexible configuration of OpenWebUI, you can easily set up your own AI conversation system. If you encounter any issues during use, you can refer to the common issues section or contact SiliconFlow customer support for assistance.
