# How to Enable Hard Drive Sleep on UGREEN NAS?

> **Article ID**: `437`  
> **Category**: `Application Guide > Control Panel > FAQ > How to Enable Hard Drive Sleep on UGREEN NAS?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/437  

---

## Applicability

**Applicable Version**: UGOS Pro firmware 1.17.0.0031 or later

The descriptions in this document are for reference only. The actual interface may vary slightly depending on the system or app version. Please refer to the actual interface.

## App Overview

UGREEN NAS supports automatically putting hard drives to sleep when they are idle. Once enabled, a drive enters sleep mode automatically if no read or write activity occurs within the specified period, helping reduce power consumption.

**Hard Drive Sleep is available for**:

● Mechanical hard drives installed in a UGREEN NAS.

● External USB drives that support sleep mode.

SSDs do not support Hard Drive Sleep.

## Access on PC

1. Open the "**Control Panel**" app and click "**Hardware & Power**" > "**Power**".

2. On the Power tab, find "**Hard drive sleep**".

3. On this page, you can configure "**Enable hard drive sleep**" and "**Enable USB hard drive sleep**".

4. After configuring the settings, click "**Apply**" in the lower-right corner. The system will save the current hard drive sleep settings.

![](https://file-us.ugreennas.com/admin/article/2026-09-09/dd4a2bdf50ab4572a6313a12c44b0cf9.webp)

## Access on Mobile

1. Open the "**Control Panel**" app and click "**Hardware & Power**".

2. Find "**Hard drive sleep**". You can enable and configure "**Hard drive sleep**" and "**USB hard drive sleep**".

![](https://file-us.ugreennas.com/admin/article/2026-09-09/7a567afae8d84d9f9311710cc3c22ac9.webp)

3. After configuring the settings, the system will save the current hard drive sleep settings.

## Enable Hard Drive Sleep

**Enable hard drive sleep** controls the mechanical hard drives installed in the UGREEN NAS.

Once enabled, the system puts a drive to sleep after it has remained idle for the specified period.

The following options are available. Actual options may vary depending on what is displayed on the page:

● **Select hard drive**: Select the drives for which sleep mode will be enabled. You can select all drives or specific drives.

● **Automatic sleep**: Set how long a drive must remain idle before entering sleep mode. For example, selecting **20 minutes** means the drive will automatically go to sleep after 20 consecutive minutes with no read or write activity.

● **Wake-up strategy**: Choose how sleeping drives are woken. Select Sign-in or On-demand based on your usage needs.

● **Record hard drive sleeping logs**: When enabled, the system records events related to drive sleep. Click "**View logs**" to review when drives entered sleep mode or were woken.

**Record hard drive sleeping logs** is available only under "**Enable hard drive sleep**". **Enable USB hard drive sleep** does not support recording hard drive sleep logs.

## Enable USB Hard Drive Sleep

**Enable USB hard drive sleep** controls external USB drives connected to the UGREEN NAS.

Once enabled, a USB drive automatically enters sleep mode after remaining idle for the specified period, helping reduce power consumption.

The following options are available:

● **Select hard drive**: Select the USB drives for which sleep mode will be enabled. You can select all drives or specific USB drives.

● **Automatic sleep**: Set how long a USB drive must remain idle before entering sleep mode. For example, selecting **20 minutes** means the USB drive will automatically go to sleep after 20 consecutive minutes with no read or write activity.

● **Wake-up strategy**: Choose how a sleeping USB drive is woken. Select Sign-in or On-demand based on your usage needs.

## Wake-Up Strategies

● **On-demand:** The drive wakes automatically when the system needs to read or write data.

● **Sign-in**: After a user signs in, the system wakes the applicable drives based on the configured strategy.

## Notes

● Hard Drive Sleep applies only to mechanical hard drives. SSDs do not support this feature.

● Some USB drives or drive enclosures may not support sleep mode. Availability depends on the capabilities of the connected device.

● After a drive enters sleep mode, there may be a brief delay the first time its files are accessed while the drive wakes up. This is normal.

● Drives may not enter sleep mode while the device is running tasks such as downloads, sync, backup, indexing, or media library scans.

● To check a drive's sleep status, enable "**Record hard drive sleeping log**" and review the log entries.
