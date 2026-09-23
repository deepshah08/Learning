# Surveillance Center FAQs

> **Article ID**: `879`  
> **Category**: `Application Guide > Surveillance Center > Surveillance Center FAQs`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/879  

---

## Camera Connection and Usage Issues

### Q1: Why can't the camera connect?

Check the following:

1. **ONVIF is not enabled**: Some cameras require ONVIF to be enabled manually in their management interface. It may be disabled by default.

2. **Incorrect username or password**: Some cameras use separate credentials for the management interface and ONVIF access. Make sure the ONVIF username and password are entered.

3. **Unsupported protocol**: Surveillance Center supports standard ONVIF and RTSP protocols. Some camera brands use proprietary protocols, which cannot be connected through Surveillance Center.

4. **Multiple devices connecting to the same camera**: If the camera is already being accessed by multiple devices at the same time, it may exceed its streaming capacity, causing new connection attempts to fail. Disconnect unnecessary connections and try again.

### Q2: What should I do if the web interface says that "H.265-encoded files are not supported"?

![](https://file-us.ugreennas.com/admin/article/2026-07-09/63e68830b8694ae0adca9e775b62874c.webp)This message usually appears because **the browser does not support H.265 decoding**, rather than because Surveillance Center does not support it. Try the following methods:

● Use the UGREEN NAS PC client to access Surveillance Center.

● Use Google Chrome instead (Chrome generally provides better H.265 compatibility, but some versions still rely on the system's decoding capability).

If playback still fails, install the HEVC extension from the "Microsoft Store" on Windows.

### Q3: Why aren't the camera's built-in event recordings available after connecting via ONVIF?

Two conditions must be met for event recordings to be received:

1. **The corresponding event types must be selected in Surveillance Center.**  
In the camera settings, manually select the event types to record, such as "**People detection**" or "**Vehicle detection**". If an event type is not selected, Surveillance Center will not save it as an event recording even if the camera detects the event.

2. **The camera must actively report events through the standard ONVIF protocol.**  
Surveillance Center currently receives general event notifications through the standard ONVIF protocol using the PullPoint mechanism. If the camera does not actively report events through the standard protocol, Surveillance Center cannot receive them. Some camera brands use proprietary protocols for event notifications, which cannot be obtained through a standard ONVIF connection.

**Recommended checks**:

● First, confirm that the required event types are selected in the camera settings.

● If they are selected but event recordings are still unavailable, check whether the camera model supports the standard BaseNotification mechanism.

### Q4: Can Surveillance Center remotely add a camera if the NAS and camera are not on the same LAN?

**No.** The camera must be on **the same LAN** as the NAS to complete the connection setup. When remotely accessing the NAS, you cannot add cameras that are located in other network environments to Surveillance Center.

> Example: If you are at the office and want to remotely log in to your home NAS to add a camera at the office or another camera in a different network environment at home, this is not supported.

**Note**: First connect the NAS and camera to the same LAN and complete the camera setup. After that, you can remotely access the NAS to view surveillance footage.

### Q5: How do I enter the port when adding a camera to Surveillance Center?

The camera port can be found in the camera management interface. The port number may vary depending on the camera brand.

**Steps**:

1. Log in to the camera management interface.

2. Check the port number in the camera settings or device information page (for example, TP-Link cameras display the corresponding service port in the device information section of the management interface).

3. If you cannot find the port information, contact the camera manufacturer for assistance.

**Note**: Some cameras use port 80 or 2020 by default. Always use the actual port number obtained from the camera settings.

## Display Issues

### Q6: Why do two cameras with the same resolution settings appear in different aspect ratios?

When connected through UGREENlink, multiscreen preview uses the **third stream** where available, followed by the **substream**. Therefore, even if both cameras use a main-stream resolution of 2560 × 1440, differences in the substream or third-stream resolution may cause their aspect ratios to appear inconsistent.

To keep the aspect ratios consistent, open each camera's management interface and set the substream or third-stream resolution to the same aspect ratio.

## AI Detection Feature Issues

### Q7: Why does face merging show that the limit has been reached?

When merging faces in "**Face recognition**", a limit message appears because the current version **supports merging up to 80 faces into a single person group**.

**Note**: Once a person group contains 80 faces, the system will no longer allow new faces to be merged into that group. To continue merging faces, organize existing groups first (such as splitting groups or removing redundant faces).

## AI Detection Issues

### Q8: How many AI detection tasks are supported by each device model?

|  |  |  |
| --- | --- | --- |
| **Devicemodel** | **Supported camera channel** | **Maximum concurrent AI detection tasks** |
| DXP 2800 / 4800 / 2800S / 4800S / 2800GT / 4800GT | 8 | 3 |
| DH2300（8GB version）/ DH2300 Plus / DH4300 Plus | 8 | 4 |
| DXP 4800 Plus / 6800 / 4800 Pro / 6800 Plus / 8800 / 8800S | 8 | 6 |
| DXP 480T Plus / 6800 Ultra / 6800 Pro / 8800 Plus / 8800 Pro | 8 | 8 |
| iDX6011 / 6011 Pro | 8 | 12 |

**Notes**:

● "**Supported camera channels**" refers to the maximum number of cameras that can be added. Recording is not limited by the number of AI detection tasks.

● **Maximum concurrent AI detection tasks** refers to the maximum number of cameras that can use AI detection at the same time.

● The supported AI detection features (such as face detection and pet detection) vary by device model. Refer to the actual device model for details.

### Q9: How Many Tasks Does Each AI Detection Feature Use?

|  |  |  |  |
| --- | --- | --- | --- |
| **AI detection type** | **Dependency** | **Model used** | **Task used** |
| Pet detection | None | General detection | **1** |
| People detection | None | General detection | **1** |
| Face detection | Requires "People detection" first | General detection + Face recognition | **3** |

**Examples of Task Usage**:

● **One camera with only Pet detection enabled**: Uses the General detection model and consumes **1** task.

● **Multiple cameras using only general detection features**: If two cameras each have one general detection feature enabled, such as Pet detection on one camera and People detection on the other, they consume **2** tasks in total.

● **One camera with "People Detection + Face Recognition" enabled**: Uses the "General detection + Face recognition" models and consumes **3** tasks.

**Additional information**: After enabling a model in the "**Model Management**" App and granting it access to Surveillance Center, you can enable the corresponding AI detection features as needed in the camera settings.

### Q10: Why does the Face Recognition model use two task slots?

The Face Recognition model combines two AI capabilities:

● **ReID (person re-identification)**: Identifies and tracks the movement of the same person across frames.

● **Face recognition**: Extracts facial features and adds them to the face database to distinguish between "known people" and "strangers".

Therefore, enabling face detection on one camera channel actually consumes 2 task resources.

### Q11: Why are "Vehicle detection" and "Pet detection" available, but there is no vehicle or pet information management?

Surveillance Center currently uses the "**General detection**" model to detect people, vehicles, pets, and other objects and link the detections to event recordings. However, advanced recognition capabilities such as "**Vehicle recognition**" and "**Pet recognition**" are not yet supported. As a result, the system can currently record related events, but it cannot manage or classify vehicle and pet identities in the same way as Face recognition.

### Q12: How Are AI Detection and Event Recording Related?

Surveillance Center can obtain camera events in two ways:

1. **Events detected and reported by the camera**: The camera reports events through the standard ONVIF protocol.

2. **Events detected by Surveillance Center AI**: Local AI models analyze the video stream and identify abnormal events.

**For "Events only" recording to work, both of the following conditions must be met**:

1. At least one event type, such as "**People detection**", is selected in the camera settings.

2. The event can be obtained through either of the methods above: it is reported by the camera or detected by Surveillance Center AI.

**If the camera does not support event reporting, Surveillance Center AI can currently provide the following event types:**

|  |  |  |
| --- | --- | --- |
| **Event type** | **Supported by Surveillance Center AI** | **Required AI detection feature** |
| Fire detection | Not currently supported | — |
| Detection zone entry | Not currently supported | — |
| Detection zone exit | Not currently supported | — |
| Face detection | Supported | Requires the "Face detection" AI feature |
| Scene change | Not currently supported | — |
| People detection | Supported | Requires the "People detection" AI feature |
| Vehicle detection | Supported | Requires the "Vehicle detection" AI feature |
| Package detection | Not currently supported | — |
| Pet detection | Supported | Requires the "Pet detection" AI feature |

### Q13: What Does the Maximum Number of AI Detection Tasks Mean?

**The maximum number of AI detection tasks** indicates how many AI detection tasks the NAS can run at the same time. Task usage depends not only on the number of cameras, but also on the combination of AI detection features enabled for each camera.

**How Task Usage Is Calculated**

**A camera may use one or more task slots**, depending on the AI detection features enabled for it:

● "**General detection**" **features only**, such as People detection or Pet detection: **Each camera uses 1 task slot**.

● "**Face detection**" **enabled**: This feature requires both the General detection and Face recognition models. **Each camera therefore uses 3 task slots**.

**Example**:

● If People detection, Face recognition, Pet detection, and Vehicle detection are all enabled for one camera, the system loads two model types: General detection and Face recognition. The camera **therefore uses 3 task slots**.

● This limit does not affect video recording. All cameras can continue recording normally; only the available AI analysis capacity is limited.

Once all available task slots are in use, enabling AI detection for another camera will trigger a message indicating that the task limit has been reached. AI detection must first be disabled for one of the cameras currently using it.

## Other Issues

### Q14: Why can't I find the Surveillance Center App on my NAS?

The Surveillance Center App is not currently available on some NAS models (**DH2600 and DX4600 series**).

**Solution**：

1. Check your NAS model first.

2. If your NAS model is not from the DH2600 or DX4600 series, update the NAS firmware to the latest version.

3. After the update is complete, go to "**App Center**", search for "**Surveillance Center**", and download and install the App.

**Note**: If you still cannot find the App after updating the firmware, contact UGREEN official technical support.

### Q15: What is the difference between using a NAS as a surveillance storage drive and using Surveillance Center?

The key differences are as follows:

|  |  |  |
| --- | --- | --- |
| **Comparison Item** | **NAS as Surveillance Storage** | **Surveillance Center** |
| Core Function | Used only as volume | A complete NVR surveillance management app |
| Recording Management | Only stores recorded video files | Supports live stream viewing, scheduled recording, playback, and event management |
| Camera Management | Not supported | Supports adding and configuring multiple cameras |
| Event Detection | Not supported | Supports event detection and recording |
| Permission Management | Shared folder permissions | Supports hierarchical user access control |

In short, **using a NAS as surveillance storage** only stores recorded video files, while **Surveillance Center** is a complete NVR (Network Video Recorder) App that supports camera connection, video recording, playback, event detection, and permission management.
