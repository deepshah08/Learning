# How to Purchase a Domain and Obtain an AccessKey?

> **Article ID**: `939`  
> **Category**: `Application Guide > Docker > FAQ > How to Purchase a Domain and Obtain an AccessKey?`  
> **Client Compatibility**: `COMMON`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/939  

---

## Applicability

**Use Case**: Prepare a domain and access credentials from the domain service provider before configuring DDNS in UGREEN NAS.

## App Overview

Because a public IP address may change when the router restarts or when the ISP periodically refreshes it, you need to prepare an available domain before configuring DDNS. DDNS binds the dynamically changing public IP address to a fixed domain, allowing you to access the corresponding device services through that domain.

This guide uses Cloudflare as examples. Third-party platform pages may change as services are updated. Please refer to the actual pages displayed.

## Cloudflare

### Purchase a Domain

1. Sign in to [Cloudflare](https://dash.cloudflare.com/) , then click "**Domain registration**" > "**Register domains**" in the left sidebar.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/d34eb02af87b425da88d3550a124cb82.webp)

2. Search for the domain you want to purchase.

3. After confirming that the domain is available, follow the on-screen instructions to complete the payment and purchase the domain.

4. Return to the Cloudflare dashboard and click the domain you just purchased in the domain list.

5. Find "**Account ID**" on the right side of the page, then copy and save the ID.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/a0b458da43194f278a1fb644a57f05cd.webp)

In the UGREEN NAS DDNS configuration, Cloudflare's "**Account ID**" corresponds to "**AccessKey ID**".

### Create an API Token

1. On the Cloudflare domain details page, click "**Get your API token**".

![](https://file-us.ugreennas.com/admin/article/2026-09-18/8f2e62967dbe406bbff8c1a68ea26c94.webp)

2. Click "**Create Token**".

![](https://file-us.ugreennas.com/admin/article/2026-09-18/3afecf9d83a84bada9c174a056743520.webp)

3. Find the "**Edit zone DNS**" template, then click "**Use template**" on the right.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/7348bbedf7c1428a94fdc30046bd9daf.webp)

4. Under "**Zone Resources**", select the domain you just purchased from the drop-down menu, then click "**Continue to summary**".

![](https://file-us.ugreennas.com/admin/article/2026-09-18/6605e624f9aa4f538eec8e675a76b612.webp)

5. After confirming that the information is correct, click "**Create Token**".

![](https://file-us.ugreennas.com/admin/article/2026-09-18/667e087d926c45d784607611107ef533.webp)

6. Click **Copy** to copy the token.

![](https://file-us.ugreennas.com/admin/article/2026-09-18/3e72b0a7c4bb49c096af03f4fcba87ea.webp)

In the UGREEN NAS DDNS configuration, the Cloudflare API token corresponds to the **AccessKey key**.

## Return to UGREEN NAS to Configure DDNS

After purchasing the domain and obtaining the access credentials, return to the UGREEN NAS DDNS configuration page and follow the on-screen instructions to enter the domain, AccessKey ID, and AccessKey key.

## Notes

● AccessKey key and API tokens are sensitive information. Store them securely and do not disclose them.

● The purchase process, identity verification requirements, fees, and page entries of third-party domain service providers are subject to the provider's actual instructions.

● If the AccessKey or API token does not have sufficient permissions, DDNS may fail to update DNS records properly.

● Credential names vary by service provider. When entering the information, make sure each credential matches the corresponding field on the UGREEN NAS page.
