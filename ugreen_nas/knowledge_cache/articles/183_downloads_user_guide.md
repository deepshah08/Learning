# Downloads

> **Article ID**: `183`  
> **Category**: `Application Guide > Downloads > Downloads User Guide`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/183  

---

The Downloads feature in the UGOS Pro system is an efficient and practical download management tool that supports multiple protocols and download methods, helping users easily manage various file download tasks. Whether it’s movies, music, documents, or large files, Downloads enables automated downloading and centralized management. It offers the following key features:

|  |  |
| --- | --- |
| **Feature Name** | **Description** |
| **Integrated with multiple download protocols** | Supports a variety of download methods including Torrent, magnet links, HTTP, and FTP, allowing users to download files, videos, music, and other types of resources. |
| Compatible with private tracker rules, enabling users to continue seeding after downloads to help maintain resource availability and stability. |
| **Simultaneous multi-task downloading** | Allows users to download multiple files at the same time, making full use of NAS storage and network resources for greater efficiency. |
| **Remote management** | Lets users remotely add and manage download tasks via the UGREEN NAS mobile app, enabling access and control anytime, anywhere. |

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250521/e517ea8c-7a62-453f-ba6d-054177045e03.png)

## **Overview of Downloads Features**

|  |  |
| --- | --- |
| **Feature Module** | **Description** |
| **Multi-protocol Support** | Supports a variety of protocols including Torrent, magnet links, HTTP, and FTP. |
| **Task Management** | Allows batch addition, pause, start, and deletion of download tasks. |
| **Speed Limit Control** | Enables global download/upload speed limits for all tasks. |
| **Torrent File Management** | Supports importing `.torrent` files to directly download torrent resources. |
| **Magnet Link Recognition** | Automatically parses magnet links and displays selectable resource content. |
| **Task Categorization** | Categorizes download tasks by status, such as downloading or installed. |
| **Notification** | Provides system notifications upon task completion or error. |

## **Installing Downloads**

Downloads is not a built-in system application. To use it for the first time, please go to "App Center", locate "Downloads", and install the app. If the app is already installed, you can open it directly or update it as needed.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250521/b5e0a396-49fa-4c1b-af02-bf7550f678fb.png)

## **Glossary of Common Terms**

|  |  |  |
| --- | --- | --- |
| **Term** | **Definition** | **Features** |
| **BT（BitTorrent）** | A protocol for peer-to-peer (P2P) file sharing. | The more users downloading, the faster the speed; users upload while downloading, creating a shared network. |
| **PT（Private Tracker）** | A private download protocol based on BT, emphasizing access control and traffic statistics. | Strict privacy (limited access); upload/download traffic is tracked to determine user permissions. |
| **Torrent File（.torrent）** | An index file used by the BT protocol that contains no actual content but records file information and tracker addresses. | Contains metadata (e.g., file chunk info, tracker addresses); connects users for downloading. |
| **Tracker Server** | A server that coordinates the BT network by providing user IP addresses to facilitate data transfer. | Acts like a “switchboard” matching downloaders; if it fails, connections may be affected. |
| **DHT** | A decentralized technology allowing BT clients to connect directly without a tracker. | Decentralized storage; reduces tracker load; enables downloads even if tracker is unavailable. |
| **Seeding (Download Status)** | The state where a user continues uploading files after download completion to assist others. | Requires hash check to confirm file integrity; upload contribution affects user privileges (e.g., in PT communities). |
| **Maximum Number of Peers** | The maximum number of other peers allowed to connect simultaneously. | Higher limits improve download speed but may consume more bandwidth or system resources. |
| **Automatic Download Watch Folder** | A feature that triggers download tasks automatically when new files appear in a specified folder. | Useful for automated downloads; no manual task initiation needed. |
| **Timeout Cancellation (Download Status)** | Automatically cancels a download task if it is not completed within a set time. | Prevents resource waste; timeout thresholds should be set based on network conditions. |
