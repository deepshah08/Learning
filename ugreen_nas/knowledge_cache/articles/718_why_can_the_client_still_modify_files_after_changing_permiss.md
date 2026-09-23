# Why can the client still modify files after changing permissions in SAN Manager? How to ensure read-only permissions take effect?

> **Article ID**: `718`  
> **Category**: `Application Guide > SAN Manager > FAQ > Why can the client still modify files after changing permissions in SAN Manager? How to ensure read-only permissions take effect?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/718  

---

## Issue Description

● I have set the Group to “Read-Only” access, but the client can still modify files — the permission setting doesn't take effect.

● Why does the client still have the previous read-write access even after modifying the permission?

## Cause Analysis

● After modifying **LUN permissions** in **SAN Manager**, connected clients do not immediately respond to the updated permission settings. This is because the client’s connection to the NAS is session-based, and **the session does not automatically refresh** when permissions are changed.In this case, the connected client will retain the state of the original session.

● The new permissions (such as Read-Only) only take effect **after manually disconnecting and reconnecting the client**, which establishes a new session and fetches the updated settings.

● If the **Initiator IQN** **configured in the Group** does not exactly match the **client’s actual iSCSI IQN**, the system cannot correctly associate the client with the **Group**. As IQN is the unique identifier of the client, **any mismatch will prevent the permission configuration from being applied correctly**.

## Solutions

1. **Disconnect and Reconnect the Client**

After modifying LUN permissions, manually disconnect and reconnect all clients connected to that LUN. The new session will retrieve and apply the updated permissions (e.g., Read-Only).

2. **Restart the Client**

Some operating systems (e.g., Windows) may cache iSCSI permission settings. Restarting the client device can help enforce the new permission settings.

3. **Ensure Initiator IQN Matches the Client’s iSCSI IQN**

Verify that the **Initiator IQN** entered in **SAN Manager** is an exact match with the **IQN from the client’s iSCSI initiator settings**. Since the IQN is the unique identifier of a client, it must match for the permissions to be applied successfully. After verifying the IQN and modifying the permission, **reconnect the client** to ensure proper application of the new configuration.
