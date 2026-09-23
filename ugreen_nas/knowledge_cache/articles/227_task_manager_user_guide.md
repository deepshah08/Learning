# Task Manager User Guide

> **Article ID**: `227`  
> **Category**: `Application Guide > Task Manager > Task Manager User Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/227  

---

## Applicability

**Applicable Clients**: UGREEN NAS PC Client (Windows/macOS), Web Browser

**Applicable Version**: UGOS Pro firmware 1.19.1.0126 or later

**Feature Differences**: NPU monitoring is supported on **iDX series** devices equipped with NPU hardware. Other models do not display the NPU monitoring item.

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

"**Task Manager**" is the resource monitoring tool in UGOS Pro. It lets you check your device status and resource usage in real time. You can monitor CPU, GPU, NPU, memory, network, hard drive, and volume usage, view resource usage by services and processes, and track overall resource usage trends for easier system monitoring and management.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/6297e8c7e3d24de0a01d5b09871ad9a7.webp)

## Running Status

On the "**Running Status**" page, you can view detailed charts and data for each system resource.

### Overview

The "**Overview**" page uses charts to show resource usage for device status, memory, network, hard drives, and volumes.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/2775edc735284e84af347265facf826c.webp)

### CPU

Displays real-time CPU utilization and temperature. Hover over the chart to view CPU utilization and temperature for a specific time period.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/86dfef74406641a89a9d178aacc97e28.webp)

### GPU

Displays real-time GPU utilization. Hover over the chart to view GPU utilization for a specific time period.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/73092876f885472387dd8309a37c7c95.webp)

### NPU

Displays real-time NPU utilization. The NPU accelerates local AI inference tasks, such as face recognition in Photos, speech transcription, and semantic search.

Hover over the chart to view detailed utilization data for a specific time period.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/75e11e44b05d4d879bd7949f469c7bc8.webp)

### Memory

Displays overall physical memory usage and the memory usage breakdown. Hover over the chart to view physical memory utilization for a specific time period.

**Note**: Memory usage may remain high because the system caches frequently accessed data for faster retrieval without reading from the hard drive. When overall memory is insufficient, the system automatically releases cached memory. If memory usage remains excessively high, system performance may be affected.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/e4af4d16d2c549aebdfe4bf2f8db0f4a.webp)

### Network

Displays network upload and download traffic as transfer rates in KB/s. Hover over the chart to view detailed transfer rates for a specific time period.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/39c36a02bc764a3386329afce591a50b.webp)

### Hard Drive

Click the drop-down menu in the upper-right corner of the chart to switch between the transfer performance and utilization of different hard drives. Hover over the chart to view hard drive utilization for a specific time period.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/2bb550b5239148e9b606c7719fe66d26.webp)

### Volume

Click the drop-down menu in the upper-right corner of the chart to switch between the transfer performance and utilization of different volumes.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/ad5f6c59b5064868b83b1134e30919da.webp)

## Services/Processes

On the "**Service**" page, you can view all running system services and their resource usage. Click the target service name, then select "**Restart**" or "**Disable**".

![](https://file-us.ugreennas.com/admin/article/2026-09-09/c197153cf0554cac85a936ae65e5c4d2.webp)

On the "**Process**" page, you can view all running processes and their resource usage. Click the target process, then select "**End Process**".

![](https://file-us.ugreennas.com/admin/article/2026-09-09/1fd3eefda8a74f83801d54ff762cd7a7.webp)

## Notes

● Restarting or ending a service/process may interrupt tasks currently being performed by that service. Proceed with caution.

● Ending a critical system process may make related features unavailable or cause system instability. Make sure you understand what the process does before ending it.

● Administrator permissions are required to manage services or processes in Task Manager.
