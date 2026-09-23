# What Are the Roles of the NPU and GPU in the DH Plus Series? Which Features Currently Use Each?

> **Article ID**: `688`  
> **Category**: `Troubleshooting > Hardware Failure > What Are the Roles of the NPU and GPU in the DH Plus Series? Which Features Currently Use Each?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/688  

---

In UGREEN NAS DH Plus series devices, the system integrates two types of hardware acceleration units:

● **NPU (Neural Processing Unit):** A neural network processing unit dedicated to AI model inference tasks.

● **GPU (Graphics Processing Unit):** A graphics processing unit designed for graphical computing tasks such as image rendering and video processing.

These two acceleration units handle different types of computational workloads, powering core system functions like AI recognition and image/video rendering, respectively.

## **Feature Comparison Table**

|  |  |  |  |
| --- | --- | --- | --- |
| Processing Unit | Application Area | Current Main Use Cases | Features & Advantages |
| NPU | AI model inference, image recognition | Recognition of people, scenes, and objects in the album | High efficiency, low power consumption, purpose-built for neural inference |
| GPU | Image rendering, video processing | Image composition, subtitle generation, Docker-based image tasks | Parallel graphics computation, ideal for image and visual processing |

## **NPU Use Cases**

The NPU is primarily used in the AI Album Recognition feature, including:

‒ **People Recognition:** Detecting and classifying faces in photos

‒ **Scene Analysis:** Identifying typical scenes such as landscapes, architecture, and indoor environments

‒ **Object Classification:** Recognizing common objects like vehicles, animals, and food

‒ **Text Recognition in Images:** Extracting text from images to enable fast and accurate search

All of these tasks are performed using pre-trained image models, and the inference phase is accelerated by the NPU for efficient computation.

### **Limitations**

The current AI Album feature on DH Plus series devices does not support the following extended models. Future versions may introduce more advanced AI models supported by the NPU:

‒ Custom learning and training;

‒ Pet recognition models;

‒ Automatic detection models for potentially sensitive content.

## **GPU Use Cases**

The GPU plays a role in video and image processing scenarios as well as in certain Docker container application tasks:

|  |  |  |
| --- | --- | --- |
| Scenario | GPU Involved | Reason |
| HDMI Video Playback | ❌ No | Uses VPU decoding + DMA direct output, no graphic composition needed |
| Image Color Correction | ✅ Yes | Requires GPU graphics processing capability |
| Video Layer Overlay & Preview Generation | ✅ Yes | Requires GPU graphics processing capability |
| Docker Graphics-Based Containers | ✅ Yes | Supports GPU-accelerated computing |

Note: The GPU does not participate in AI model inference; it is mainly used for graphics rendering and image acceleration.

## **Notes**

● The NPU and GPU focus on different types of hardware acceleration tasks and do not conflict.

● If users prioritize AI capabilities, they should focus on the accuracy and efficiency of album recognition.

● For Docker users or video enthusiasts, the GPU’s graphics acceleration capabilities are more valuable.

● Future system upgrades may introduce support for more AI models and graphics tasks. It is recommended to keep the system updated to enjoy the latest hardware acceleration features.
