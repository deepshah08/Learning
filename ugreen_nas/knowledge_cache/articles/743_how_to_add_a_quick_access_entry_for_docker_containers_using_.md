# How to Add a Quick Access Entry for Docker Containers Using Host Network Mode?

> **Article ID**: `743`  
> **Category**: `Application Guide > Docker > FAQ > How to Add a Quick Access Entry for Docker Containers Using Host Network Mode?`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/743  

---

## **Issue Description**

When deploying containers using Docker Compose or similar Docker projects, the system typically identifies access ports via the `ports` field and automatically displays service entry points under [Quick Access]. However, when a container uses `network_mode: host`, the system is unable to detect these ports by default, resulting in no quick access entry being shown.

This tutorial explains how to correctly configure the `ports` field for containers in host mode, so that the system can still recognize and display quick access entries.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250725/f343f40e-93ed-4961-b80e-29e17e5bce5c.png)

## **Cause Analysis**

In the default `bridge` network mode, the `ports` field is used for port mapping, and the system relies on this field to identify quick access entries. However, in `host` mode, port mapping is actually ineffective, so the `ports` field needs to be added to help the system recognize the port.

For example, in the following `docker-compose` configuration, Jellyfin uses `network_mode: host` but does not include the `ports` field, so the system cannot generate a quick access entry for it.

```
services:
  jellyfin:
    image: jellyfin/jellyfin:latest
    container_name: jellyfin
    tty: true
    restart: always
    devices:
      - /dev/dri:/dev/dri
    volumes:
      - ./config:/config
      - ./cache:/cache
    network_mode: host
```

## **Solution**

1. In `host` mode, you can add the `ports` field to the project's Compose configuration to help the system recognize the service port.

```
services:
  jellyfin:
    image: jellyfin/jellyfin:latest
    container_name: jellyfin
    tty: true
    restart: always
    devices:
      - /dev/dri:/dev/dri
    volumes:
      - ./config:/config
      - ./cache:/cache
    network_mode: host
    ports:
      - "8096:8096"  # Port for the system to recognize and display a quick access entry
```

2. After adding this and redeploying the project, the container will have a recognizable quick access entry.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250725/1c48233e-a3d2-4849-bb41-a4fbba424cf6.png)

## **Notes**

* If you are unsure about the container’s access port, please check the official documentation or tutorial page of the container image.
* Use the `port:port` format exactly like `"8096:8096"`, matching the actual access port.
* Do not write it as `8888:8096`; the system will fail to recognize it correctly, causing access issues.
* In host mode, port mapping is not actually performed; it is only used for recognizing the “Quick Access” entry.
* Quick access recognition in host network mode is supported only for containers created via project (Compose) deployment; containers created directly through the Docker container panel in host mode do not support this feature.
