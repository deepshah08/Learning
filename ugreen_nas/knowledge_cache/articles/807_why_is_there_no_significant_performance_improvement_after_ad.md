# Why Is There No Significant Performance Improvement After Adding SSD Cache to a Storage Pool?

> **Article ID**: `807`  
> **Category**: `Application Guide > Storage > FAQ > Why Is There No Significant Performance Improvement After Adding SSD Cache to a Storage Pool?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/807  

---

## Issue Description

After adding SSD cache to a storage pool, there is no noticeable improvement in performance during actual use. Transfer speeds or response times may show little change.

## Cause Analysis

SSD cache is primarily designed to improve performance in scenarios involving frequent small-file read/write operations, multi-user concurrent access, and random I/O-intensive workloads. It does not provide noticeable acceleration in all usage scenarios.

Performance improvement may be limited in the following cases:

1. **Large Sequential Read/Write Operations**

Transferring large files (such as ISO images, large compressed archives, or video source files) is a typical sequential read/write scenario.

These operations are mainly limited by the hard drive's sequential throughput rather than IOPS performance. Since SSD cache provides limited improvement for sequential throughput, the acceleration effect may not be obvious.

2. **High-Definition Video Streaming**

Video playback typically involves continuous sequential reading. Data is preloaded into the player buffer and transmitted at a steady rate.

Because the access pattern lacks randomness, the low-latency advantage of SSD cache cannot be fully utilized.

3. **Completely Random and Non-Repeated Data Access (One-Time Reads)**

SSD cache uses a "**hot data caching**" mechanism, meaning only frequently accessed data is cached.

If the workload consists of random reads that are not repeated (data is read once and not accessed again), the cache hit rate will be very low, making it difficult to achieve noticeable performance gains.

## Recommended Actions

SSD cache is better suited for:

● Multi-user access to shared files

● Virtual machine storage

● Database applications

● Frequent small-file read/write workloads

If your primary use case is large file transfers or video playback, you may consider the following options first:

● Upgrade to higher-speed drives or add more drives

● Use RAID to improve throughput

● Upgrade network bandwidth (such as 2.5GbE or 10GbE)
