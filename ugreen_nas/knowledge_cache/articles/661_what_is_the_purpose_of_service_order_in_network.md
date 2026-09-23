# What Is the Purpose of Service Order in Network?

> **Article ID**: `661`  
> **Category**: `Application Guide > Control Panel > FAQ > What Is the Purpose of Service Order in Network?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/661  

---

In UGREEN NAS network settings, the service order function dynamically adjusts the priority of network services to achieve precise traffic routing control.

Users can drag and reorder the list of network services; the highest priority service will automatically become the default gateway. All traffic without explicitly specified routes (such as regular internet access or NAS external services) will be transmitted through this gateway. For example, if the NAS needs to access the internet preferentially through a specific gateway, simply drag the corresponding network service to the top of the list.

## **Usage Scenario**

When the NAS device is connected to multiple network interfaces (such as multiple network cards or routers), you can adjust the service order to specify the default gateway, ensuring that traffic is transmitted through the designated interface.

If users have specific routing requirements, for example, placing a gateway used only for intranet access at the top to prioritize internal data transmission, and placing the gateway with internet access below for general internet use, these needs can be met by setting the service order.

## **How to Set Service Order**

1. Open the "Control Panel" application, then click [Network] > [Network Connection] > [Service Order].

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250709/b8f7c256-cc16-4651-9bda-7e1faffe73e0.png)

2. Adjust the order of network connections by dragging and dropping, then click "Save" to apply the settings.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250709/4398a91a-0ed3-4ea8-bd80-c656b7d0d01b.png)
