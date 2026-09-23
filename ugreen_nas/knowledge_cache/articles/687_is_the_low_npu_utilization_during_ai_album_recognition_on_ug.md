# Is the low NPU utilization during AI album recognition on UGREEN NAS (DH Plus series) a performance issue?

> **Article ID**: `687`  
> **Category**: `Troubleshooting > Hardware Failure > Is the low NPU utilization during AI album recognition on UGREEN NAS (DH Plus series) a performance issue?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/687  

---

Low NPU utilization is a normal phenomenon and not a performance issue. The NPU chip used in the DH4300 Plus series NAS features a multi-core architecture. The system displays the average utilization across all 3 NPU cores, meaning actual usage may be significantly higher than what appears in the interface. Here's why:

**1.****The System Shows "Total Average Utilization", Not Per-Core Load**

The NPU in the DH4300 Plus includes three parallel processing cores. The system shows usage as a global average across all cores. For example:

● If the AI model uses 50% of one core, the total displayed utilization is: 1 × 50% ÷ 3 = 16.6%

● What the user sees in the interface is 16.6%, which reflects the average rather than the true load on a single core.

Low utilization ≠ low efficiency — this is simply due to how UGOS presents the data.

**2. AI Image Recognition Is Multi-Stage — NPU Only Runs During Specific Phases**

The AI album recognition task doesn’t rely on the NPU throughout the entire process. It is a multi-stage cooperative task, including:

|  |  |  |
| --- | --- | --- |
| Processing Stage | Primary Resource Used | Description |
| Data Loading | CPU | Loads user photos into memory |
| Image Preprocessing | CPU | Performs scaling, cropping, and format normalization |
| Model Inference | NPU | Runs neural networks for face recognition, object classification, etc. |
| Result Storage | CPU + Storage System | Writes recognition results, tags, and index data to the database |

Only the model inference stage uses the NPU to perform deep learning tasks. Once the inference is complete, the NPU immediately releases resources. As a result, the NPU is not continuously active, and its utilization typically shows brief peaks followed by quick drops.

It is not recommended to use NPU utilization as the sole performance indicator. Instead, focus on task completion speed and recognition accuracy.

**3. Low Utilization Reflects NPU Efficiency**

The NPU is a high-efficiency, low-power processing unit specifically designed for deep learning inference. Its key characteristics include:

● High throughput for processing model tasks

● Rapid task completion followed by immediate resource release

● Cooperative operation with the CPU to enhance overall system concurrency

If you observe low NPU utilization but recognition tasks are completed within a reasonable time and with expected accuracy, it indicates that the system is running efficiently and resources are being allocated appropriately.
