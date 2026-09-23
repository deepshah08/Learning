# What is the Role of the Polling Period in Cloud Drives Tools?

> **Article ID**: `478`  
> **Category**: `Application Guide > Cloud Drives > What is the Role of the Polling Period in Cloud Drives Tools?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/478  

---

## Introduction

The polling cycle is the interval at which Cloud Drives regularly checks for changes to files in public cloud drives. Once enabled, the system retrieves the cloud drive file list at the configured polling interval and compares it with the current sync status.

If new, modified, or deleted files are detected, the system performs the corresponding operations according to the sync task rules.

For example, if the polling cycle is set to 1 hour, Cloud Drives checks the cloud drive for file changes every hour.

## Purpose of the Polling Cycle

For real-time sync tasks, Cloud Drives promptly processes detected file changes. After the polling cycle is enabled, the system performs a full comparison of the cloud drive file list at fixed intervals to detect file changes that may have been missed due to network fluctuations, transfer interruptions, or other issues.

Setting an appropriate polling cycle helps balance timely file updates and system resource usage.

● If files change frequently, you can shorten the polling cycle as needed.

● If files change less frequently, you can extend the polling cycle as needed.

## Set the Polling Cycle

1. Open "**Cloud Drives**" and go to the "**Connect**" page.

2. In the list of connected cloud drives, click "**···**" to the right of the target cloud drive>"**Management**".

![](https://file-us.ugreennas.com/admin/article/2026-09-16/2d882bddb9204f33ba87ef4e91287841.webp)

3. Find the "**Polling cycle**" setting, check "**Enable**", and set the polling interval.

![](https://file-us.ugreennas.com/admin/article/2026-09-16/06ca7bf3aad2439eaf9b96ce86387e02.webp)

4. Click "**Confirm**" to save the settings.

## Setting Range

The default polling cycle is 1 hour, and the maximum is 24 hours, or 1440 minutes. You can adjust it based on how frequently files in the cloud drive are updated.

## Notes

● Enabling the polling cycle requires the device to regularly access the cloud drive and check for file changes, which may affect hard drive sleep.

● When the network connection is unstable, setting the polling cycle too short may increase the likelihood of connection failures or task errors.
