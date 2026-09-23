# Risks of Enabling SMB1 Protocol

> **Article ID**: `228`  
> **Category**: `Application Guide > Control Panel > File Service > Risks of Enabling SMB1 Protocol`  
> **Client Compatibility**: `PC`  
> **Official URL**: https://support.ugnas.com/knowledgecenter/#/detail/228  

---

Enabling SMB1 poses several security risks. Here are some risks associated with enabling SMB1:

1. **Man-in-the-Middle Attacks:** The lack of adequate encryption and authentication mechanisms in the SMB1 protocol makes it vulnerable to man-in-the-middle attacks. Attackers can intercept data, manipulate it, or impersonate legitimate users to gain sensitive information or execute malicious actions.
2. **Remote Code Execution Vulnerabilities:** SMB1 has known remote code execution vulnerabilities, allowing attackers to remotely execute malicious code and take control of systems. Enabling SMB1 increases the risk of these vulnerabilities, leading to system compromise.
3. **Denial of Service Attacks:** Attackers can exploit vulnerabilities in SMB1 to launch denial of service (DoS) attacks, causing services to become unavailable or systems to crash. This can disrupt access to shared resources and impact system availability and stability.
4. **Malware Propagation:** Many malware strains leverage SMB1 vulnerabilities for propagation. For instance, the WannaCry ransomware exploited SMB1 vulnerabilities to spread globally. Enabling SMB1 increases the risk of malware infections, leading to data breaches, system compromises, or other security issues.
5. **Transmission of Sensitive Information in Plain Text:** SMB1 typically transmits data in plain text rather than encrypted form. This means that sensitive information like usernames and passwords may be transmitted in plain text over the network, making it susceptible to interception and exploitation.
6. **Exploitation of Vulnerabilities:** SMB1 harbors many undisclosed or unpatched security vulnerabilities that attackers can exploit. These vulnerabilities may result in data breaches, system compromises, or malware infections.
7. **Network Broadcast Risks:** SMB1 uses broadcast for service discovery in the network, which can cause network congestion and performance degradation. High volumes of SMB1 broadcast traffic may affect network stability and responsiveness.
8. **Outdated Version:** SMB1 is a relatively outdated protocol lacking many of the security features and functionalities of modern file-sharing protocols. Enabling SMB1 may prevent systems from benefiting from the security enhancements and features of newer protocols.
9. **Difficulty in Monitoring and Management:** SMB1 has weaker security and activity monitoring capabilities, making it challenging to detect and respond to potential security threats promptly. Disabling SMB1 can simplify system monitoring and management, reducing potential security vulnerabilities and risks.
10. **Compatibility Issues:** Some modern operating systems and applications no longer support SMB1, leading to compatibility issues if SMB1 is enabled. This may affect system interoperability and work efficiency.

In conclusion, enabling SMB1 may introduce various security and performance issues. To mitigate security threats and enhance system performance and stability, it is advisable to disable the SMB1 protocol.
