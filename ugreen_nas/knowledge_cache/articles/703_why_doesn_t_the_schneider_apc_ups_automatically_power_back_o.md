# Why doesn't the Schneider APC UPS automatically power back on after being set to shut down automatically?

> **Article ID**: `703`  
> **Category**: `Application Guide > Control Panel > FAQ > Why doesn't the Schneider APC UPS automatically power back on after being set to shut down automatically?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/703  

---

## **Problem Description**

When the UGREEN NAS is connected to a Schneider APC UPS (such as BK650M2-CH or BE600M1) and configured with the protection mode "Shut down automatically after power failure" + "Execute now," while the NAS is also set to "Auto boot after loss of power," the NAS fails to automatically restart if utility power returns within 2 minutes after the UPS shuts down.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250613/a971d366-4143-4a25-af89-3aee48fa82f5.png)

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250613/857e5f6d-596b-47ec-abc7-b4e4eb2d3725.png)

## **Cause Analysis**

This issue is due to hardware design limitations in certain APC UPS models. Specifically:

● After receiving a shutdown signal, APC UPS devices (such as BK650M2-CH and BE600M1) do not cut power immediately. Instead, they enter a fixed 2-minute delayed shutdown countdown.

● During this 2-minute period, the UPS continues to supply power to the NAS. As a result, the NAS does not actually experience a complete power loss, and therefore, the "power-off → power-on" auto-restart mechanism is not triggered.

● This 2-minute delay is a default setting in the UPS firmware and cannot be modified.

## **Solution**

● If you're using an APC UPS, it is recommended to wait at least 2 minutes after initiating the automatic shutdown before restoring power. This ensures that the UPS has completed the power-off process, allowing the NAS to enter the auto power-on sequence properly.

|  |  |  |
| --- | --- | --- |
| Scenario Description | Auto Power-On Supported | Explanation |
| Power is restored within 2 minutes after NAS shutdown | No | The UPS has not truly cut off power, so the NAS does not recognize a power-off → power-on event |
| Power is restored more than 2 minutes after NAS shutdown | Yes | The UPS has completed its shutdown, and the NAS can detect power restoration and auto boot |

● Alternatively, consider using a UPS device that supports fast shutdown (within 5 seconds) for a smoother power-off and reboot experience. Based on tests, most other UPS models supported by UGREEN NAS are able to cut power approximately 5 seconds after the NAS shuts down, avoiding this issue. For more compatibility details, please refer to the [UPS (Uninterruptible Power Supply) Compatibility List.](https://support.ugnas.com/knowledgecenter-h5/#/articleDetail?custom=eyJpZCI6MTQ0LCJ0eXBlIjoidGFnMDA0IiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVJbmZvSWQiOjEzNiwiYXJ0aWNsZVZlcnNpb24iOiIxLjAiLCJwYXRoQ29kZSI6IiJ9)
