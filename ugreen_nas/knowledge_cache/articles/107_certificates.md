# Certificates

> **Article ID**: `107`  
> **Category**: `Application Guide > Control Panel > Security > Certificates`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/107  

---

Certificates can be used to secure SSL services on UGREEN NAS, such as web (all HTTPS services), FTPS, and other services. Having a certificate allows users to verify the identity of the server and administrator before transmitting any sensitive information.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250310/38232e87-21a9-4474-b1f4-4cd37b2593e1.png)

In [Control Panel] > [Security] > [Certificates], you can perform the following actions:

* Import a new certificate: You can import multiple certificates.
* Delete a certificate.
* Extend the certificate.

## **Add a Certificate**

To add a new certificate, you can choose the import method, which is the default option: You can import the private key, certificate, and intermediate certificates from a commercial or third-party certification authority.

1. Select "Import Certificate", then click "Next".
2. Follow the wizard instructions to complete the import of the private key, certificate, and intermediate certificate.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250310/ea1cb1bb-1115-452e-9b82-fb3edd6bbfb3.png)

**Note:**

1. Some certification authorities may issue certificates without an intermediate certificate.
2. Certificates must be in X.509 PEM or DER format.
3. Private keys support both ECC and RSA formats, but neither can be protected by a passphrase.
4. The default certificate cannot be deleted.

## **Extend Certificate**

When your certificate is about to expire, you can choose the "Extend" option to renew it. Follow these steps to extend your certificate:

1. Go to [Control Panel] > [Security] > [Certificates] and select the desired certificate.
2. Choose "Extend Certificate" for the certificate.
3. Click "Extend Certificate" to retrieve your new private key and certificate signing request (CSR). You can use the new CSR to apply for a certificate signed by another certification authority.
4. After successfully extending the certificate, you can click the "+" button on the certificate page to expand and view additional details such as the certificate's validity period, issuer, and usage.

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250310/3f121df2-c183-4307-9193-d8bceb56ab2f.png)

**Please Note:**

* By default, two system certificates are provided (default UGREEN and uglink certificates). These default certificates cannot be deleted. (When ug.link is enabled, the uglink certificate is issued. If the service is disabled, there is no need to delete the certificate.)
* The system default certificates support an automatic extension mechanism. Each time the system connects to the network, if the certificate's validity is less than one month, it will be extended by one month. You can also manually extend the certificate by one month.

## **Configure Certificate**

You can change the service's certificate to another one as needed.

1. Click on "Configuration" to access the configuration page, where you can view all services and their corresponding certificates (the default certificate is UGREEN).
2. Click on the current certificate for the target service.
3. Select the correct certificate from the dropdown menu and click "Save".

![](https://file-us.ugreennas.com/ugreen-pro/admin/article/20250310/f900ed62-0293-42a4-a3d4-53578b24ec4a.png)
