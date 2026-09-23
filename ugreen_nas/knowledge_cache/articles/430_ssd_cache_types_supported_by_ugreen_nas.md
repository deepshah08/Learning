# SSD Cache Types Supported by UGREEN NAS

> **Article ID**: `430`  
> **Category**: `Application Guide > Storage > FAQ > SSD Cache Types Supported by UGREEN NAS`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/430  

---

## Applicability

**Applicable platform**: UGREEN NAS Private Cloud running UGOS Pro

**Applicable version**: UGOS Pro firmware 1.16.0.0042 and later

This document is for reference only. The actual interface and operation paths may vary slightly due to system or app version updates. Please refer to the actual interface.

## Overview

The SSD Cache feature uses high-speed SSDs to provide cache acceleration for storage pools created with HDDs. Once enabled, it can significantly improve random read/write performance and overall system responsiveness.

UGREEN NAS currently supports the following two SSD cache types.

## Read-only Cache

Read-only cache accelerates data reads only. The system automatically caches frequently accessed hot data to the SSD. When the data is accessed again, it is read from the SSD first, improving file opening and browsing speed.

Features:

● Supports creation with one SSD.

● Provides higher data security.

● Even if the cache SSD becomes abnormal, the original data in the storage pool will not be affected.

RAID types supported by Read-only cache:

● Basic: Uses a single SSD to create a cache for read-only cache acceleration.

● RAID0: Aggregates the performance of multiple SSDs to deliver higher cache read/write performance.

● RAID1: Mirrors cached data across two SSDs, providing redundancy protection while maintaining cache performance.

## Read-Write Cache

Read-Write cache accelerates both data reads and writes. The system writes data to the SSD first and then synchronizes it to the HDD, improving performance in scenarios involving frequent reads and writes of small files.

Features:

● Requires two SSDs.

● Supports cache creation in RAID1.

● Can significantly improve random read/write performance.

RAID type supported by Read-Write cache:

● RAID1: RAID1 mirrors cached data across two SSDs, providing redundancy protection while maintaining cache performance.

## Recommended Scenarios for SSD Cache

SSD cache is more suitable for random I/O-intensive scenarios, such as:

● Multiple users accessing the NAS at the same time

● Frequent reads and writes of a large number of small files

● Photo thumbnail generation

● Database applications

## Scenarios with Limited SSD Cache Benefits

In the following scenarios, SSD cache usually provides limited performance improvement:

● Sequential reads and writes of large files

For continuous transfer scenarios such as ISO images, large compressed files, and Blu-ray disc images, the performance bottleneck is mainly the sequential throughput of the HDD, so SSD cache may not provide noticeable improvement.

● HD video streaming

Video playback is a sequential read scenario, and data is usually preloaded into the player buffer. As a result, SSD cache may not be able to fully leverage its low-latency advantages.

● One-time random reads

SSD cache uses a hot data caching mechanism and only caches frequently accessed data. If a file is read once and not accessed again, the cache hit rate will be low, and performance improvement will be limited.

**Notes**

● SSD cache is used to accelerate storage pools created with HDDs. It does not increase the available storage capacity of the NAS.

● Deleting SSD cache will not delete the original data in the storage pool.

● SSD cache is more suitable for scenarios involving random reads and writes or frequent access to small files. If the NAS is mainly used for video playback or continuous large file transfers, the performance improvement may not be noticeable. It is not recommended to configure SSD cache solely for improving transfer speed.

● To create SSD cache for your NAS, refer to [How to Create an SSD Cache on Volume?](https://support.ugnas.com/knowledgecenter/#/detail/eyJ0eXBlIjoidGFnMDAyIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImlkIjoxMjQwLCJhcnRpY2xlSW5mb0lkIjo0MTUsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIiwicGF0aENvZGUiOiIifQ==) for detailed instructions.
