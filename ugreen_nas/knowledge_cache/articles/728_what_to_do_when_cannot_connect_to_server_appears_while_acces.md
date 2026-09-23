# What to Do When "Cannot Connect to Server" Appears While Accessing Containers via UGREENlink

> **Article ID**: `728`  
> **Category**: `Troubleshooting > Network Failure > What to Do When "Cannot Connect to Server" Appears While Accessing Containers via UGREENlink`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/728  

---

## Issue Description

When accessing containers (such as **CloudDrive2** or **Moviepilot v2**) remotely via the **UGREENlink** desktop shortcut, the first access works correctly. **However, upon reopening the browser a second time, the page shows "Unable to connect to the server"**, and the container's web interface fails to load.

● CloudDrive2 Containers

![](https://file-us.ugreennas.com/admin/article/2025-07-02/c72ec59ee74b4fd0aeb22d35bc11818e.webp)

● Moviepilot v2 Containers

![](https://file-us.ugreennas.com/admin/article/2025-07-02/3251b00917e2410cabed22585d63dc93.webp)

## Cause Analysis

Some containers use web frontends with a caching mechanism that registers a Service Worker during the initial page load. When accessed via a changing network address (such as through UGREENlink remote connection), this mechanism can cause abnormal behavior, preventing subsequent connections to the container page.

## Solution

1. When you see the connection failure page, press **F12** to open the browser's **Developer Tools**.

2. Navigate to the **Application** tab in the top menu bar.

3. In the left-hand menu, select **Service Workers**, then click **Unregister**.

4. Close the Developer Tools and **refresh the page** to regain access to the container's web interface.

![](https://file-us.ugreennas.com/admin/article/2025-07-02/47e4d405576541e5a1055ebb29511cfc.webp)
