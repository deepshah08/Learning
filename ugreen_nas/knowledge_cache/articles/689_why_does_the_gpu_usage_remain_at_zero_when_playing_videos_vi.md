# Why does the GPU usage remain at zero when playing videos via HDMI on UGREEN NAS (DH Plus series)? Does HDMI not support hardware decoding?

> **Article ID**: `689`  
> **Category**: `Troubleshooting > Hardware Failure > Why does the GPU usage remain at zero when playing videos via HDMI on UGREEN NAS (DH Plus series)? Does HDMI not support hardware decoding?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/689  

---

The DH Plus series devices do support hardware decoding via HDMI. It is normal for the GPU usage shown in the UGOS Pro system’s “Task Manager” to remain at zero—this does not mean that hardware decoding or rendering isn't being used. The reason lies in the hardware architecture of the DH4300 Plus, which adopts a dedicated VPU (Video Processing Unit) for video hardware decoding. After decoding, the video data is output through a specialized hardware pipeline rather than the GPU rendering channel, resulting in more efficient video playback.

## **Dedicated Video Decoding and Display Pipeline**

The DH4300 Plus is based on an ARM embedded architecture and integrates an independent video codec unit (VPU) and a graphics scaling unit. The HDMI playback process works as follows:

**1.****Video Decoding:** The VPU performs hardware decoding of video streams such as H.264 and H.265.

**2.****Image Output:** The decoded video frame data is sent directly to the display controller and written to HDMI memory via DMA (Direct Memory Access).

**3.****Display:** The display controller sends the contents of the image buffer directly to the HDMI output, without involving GPU rendering.

As long as the HDMI output does not involve complex graphical tasks such as overlays, visual effects, or UI animations, the GPU will not be invoked. Therefore, GPU usage will not appear in system monitoring tools, even though hardware decoding is active.

## **GPU Usage Scenarios**

The SoC used in the DH4300 Plus belongs to the RK (Rockchip) ARM embedded platform. On this platform, the GPU is primarily used for the following scenarios:

● **Image composition** (e.g., multi-layer overlays, filter effects)

● **Dynamic graphics rendering** (e.g., UI animations, visual transitions)

● **Graphic algorithm processing** (e.g., scaling, rotation, edge detection)

● **Graphics-related tasks within Docker apps** (e.g., OCR tools)

If the playback process involves only pure video decoding and output, the GPU remains largely idle.

|  |  |  |
| --- | --- | --- |
| Project | GPU Involved | Reason |
| HDMI Video Playback | ❌ No | Uses VPU for decoding and DMA for direct output; no graphic composition needed |
| Video Effects (Filters, Animation) | ✅ Yes | Requires GPU for graphics processing |
| Image Composition / Large Image Generation | ✅ Yes | Requires parallel graphics computation |
| UI Animation Rendering | ✅ Yes | Dynamic interface effects are driven by the GPU |
| Docker Graphics-Based Containers | ✅ Yes | Supports GPU-accelerated computing |
