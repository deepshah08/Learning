# GPU usage remains at zero during video playback? How to determine whether hardware decoding is enabled on UGREEN DH Plus series devices?

> **Article ID**: `685`  
> **Category**: `Troubleshooting > Hardware Failure > GPU usage remains at zero during video playback? How to determine whether hardware decoding is enabled on UGREEN DH Plus series devices?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/685  

---

The UGREEN DH PLUS series is based on the ARM architecture and features an efficient built-in video hardware decoder. It supports hardware decoding for multiple video formats such as H.264 and HEVC/H.265. The system utilizes a dedicated Video Processing Unit (VPU) for encoding and decoding acceleration, enabling high-performance video processing without relying on the GPU.

## **Why is there no visible GPU usage during video playback?**

The DH PLUS series NAS does not use the GPU for video encoding or decoding. Unlike traditional PC-based systems, the SoC used in the DH4300 Plus integrates a standalone VPU, which is specifically designed to handle video decoding tasks. The VPU is a dedicated hardware module that directly parses encoded streams and generates images, significantly reducing the load on both the CPU and GPU.

Therefore, it is normal if you observe no noticeable GPU usage when playing or transcoding videos on this device.

## **How to check if VPU decoding is enabled on DH PLUS NAS?**

You can confirm whether the VPU is active by logging into the NAS via SSH and running the following commands:

1. Set the status polling interval to 1000ms (1 second)

2. Check the workload (load) of the video encoding/decoding unit

```
echo 1000 > /proc/mpp_service/load_interval
cat /proc/mpp_service/load
```

● The command can display the workload of the RK chip’s hardware decoding and encoding units;

● In the returned result, the "load" field indicates the operating load of the system’s hardware video encoding and decoding unit;

● Each time a playback or transcoding task is initiated, you can observe changes in the load of rkvenc-core and rkvdec-core.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250616/b28c4c82-669d-4018-95eb-77225e04d71f.png)

## **VPU-Supported Video Formats**

Commonly Supported Video Formats by the Video Encoding Unit

|  |  |
| --- | --- |
| H.264（AVC） | AV1 |
| HEVC（H.265） | AVS2 |
| VP9 |  |
