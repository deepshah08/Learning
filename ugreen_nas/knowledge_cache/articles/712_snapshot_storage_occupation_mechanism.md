# Snapshot Storage Occupation Mechanism

> **Article ID**: `712`  
> **Category**: `Application Guide > Snapshot > Snapshot Storage Occupation Mechanism`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/712  

---

## **How Snapshots Consume Storage Space？​​**

Snapshots act as "time machines" preserving pre-modification states.​**When Files Are Modified,**​ system archives original data blocks (like saves),then new data overwrites original locations.**When Files Are Unmodified,**minimal space usage (only original data stored)

```
Original Data (Snapshot 1): [A][B][C][D]
Modified Data (Snapshot 2): [A][X][C][D] (B→X)    
Snapshot 1 saves [B]; Snapshot 2 uses no extra space (matches current data)
When file A is deleted，Snapshot 1 & 2 will collectively occupy space for A and B

chapter in the "Snapshots" documentation to learn how to configure these rules.If file A appears in multiple snapshots (Snapshot 1, 2, 3...), the physical storage consumes just one copy of A's data.
```

## **When Does Snapshot Storage Spike?**

|  |  |  |
| --- | --- | --- |
| **Factor** | **Impact** | **Analogy** |
| **Frequent File Changes** | Each edit/deletion stores old data, increasing snapshot size | Like repetitive game saves bloating save files |
| **Excessive Snapshots** | More snapshots = more unique data blocks stored | Keeping 100 saves vs. 3 recent ones |

## **Why Btrfs Snapshots Save Space?**

● **Traditional Backup**: Full copies (100% storage per backup).

● **Btrfs Snapshots**: Only stores modified/deleted data (incremental).

## **​Why Isn’t Space Usage Obvious?**

Storage consumption **grows stealthily**—minor changes seem harmless until accumulated.​

## **​How to Optimize Snapshot Storage Space?​​**

**Reduce Snapshot Quantity**.Regularly purge older snapshots (e.g., retain only the most recent 7 days' worth)

Snapshot Space Consumption = Modification Frequency × Number of Modified Files × Total Snapshot Count

Btrfs achieves significant space savings through incremental backup technology, but requires proactive management to prevent gradual disk saturation.

## **Why do multiple snapshots occupy more space?**

● Each snapshot retains the data state at its creation time, and **differing data blocks** across multiple snapshots need to be stored separately;

● As file modifications increase, differences between different snapshots also grow, leading to continuous **storage space growth**;

● Although a single snapshot may occupy relatively little space, **frequent creation and long-term retention of snapshots** will gradually accumulate large amounts of differential data.

To prevent excessive snapshot space usage, it is recommended to enable [Snapshot Retention Policy]. The system can automatically clean up expired snapshots according to settings to save storage space, and will periodically delete old snapshots that exceed the policy-defined range.

● **Time-based retention policy**: e.g., "Retain snapshots from the last 7 days";

● **Quantity-based retention policy**: e.g., "Retain a maximum of 24 snapshots";

You can refer to the “[Snapshot Retention Policy](https://support.ugnas.com/knowledgecenter/#/detail/eyJpZCI6MzQ5LCJ0eXBlIjoidGFnMDAxIiwicGF0aENvZGUiOiJwcm8wMDIsNHpGVU5SIiwibGFuZ3VhZ2UiOiJ6aC1DTiIsImNsaWVudFR5cGUiOiJQQyIsImFydGljbGVWZXJzaW9uIjoiIn0=)” chapter in the "Snapshots" documentation to learn how to configure these rules.
