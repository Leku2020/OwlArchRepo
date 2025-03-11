---
layout: software
title: Zeek
permalink: /zeek
---

[🔙 Go back home](/owlArchRepo/)

# Zeek  
**Network Traffic Monitoring and Analysis Framework**

## Introduction  
Zeek (formerly Bro) is an open-source network analysis tool designed for security monitoring, intrusion detection, and generating detailed logs of network activity. It provides deep visibility into protocols, connections, and anomalies in real time.

## Features  
- **Comprehensive Logging**: Tracks HTTP, DNS, SSL/TLS, FTP, and other protocol activities.  
- **Intrusion Detection**: Identifies suspicious behavior (e.g., port scans, brute-force attacks).  
- **Customizable Scripts**: Extend functionality with Zeek’s domain-specific scripting language.  
- **Offline Analysis**: Process PCAP files for post-capture investigation.  
- **Scalability**: Suitable for small networks to large enterprise deployments.  

## Installation  

1. Open a terminal.  
2. Install Zeek using:  
   ```sh  
   sudo pacman -S zeek  
   ```  

### Install Verification  
Check the version to confirm installation:  
```sh  
zeek -v  
```  

### Uninstall  
```sh  
sudo pacman -R zeek  
```  

## Usage  

### Analyze Live Traffic  
```sh  
sudo zeek -i eth0  
```  

### Process a PCAP File  
```sh  
zeek -r capture.pcap  
```  

### Inspect Generated Logs  
List logs:  
```sh  
ls -l *.log  
```  

View connection logs:  
```sh  
cat conn.log | zeek-cut id.orig_h id.resp_h service  
```  

### Example Workflow  

#### Detect SSH Brute-Force Attacks  
1. Analyze traffic:  
   ```sh  
   sudo zeek -i eth0 local "Site::local_nets += { 192.168.1.0/24 }"  
   ```  
2. Check `notice.log` for alerts:  
   ```sh  
   cat notice.log | grep "SSH::Bruteforce"  
   ```  

## Configuration  

### Main Configuration Files  
- **Global settings**:  
  ```sh  
  /usr/local/zeek/etc/zeekctl.cfg  
  ```  
- **Custom scripts**:  
  ```sh  
  /usr/local/zeek/share/zeek/site/local.zeek  
  ```  

### Example: Add a Custom Network Range  
Edit `local.zeek`:  
```sh  
nano /usr/local/zeek/share/zeek/site/local.zeek  
```  
Add:  
```zeek  
redef Site::local_nets += { 10.0.0.0/8 };  
```  

## Official Documentation & More Info  
- [Zeek Official Site](https://zeek.org/)  
- [Documentation](https://docs.zeek.org/)  
- [GitHub Repository](https://github.com/zeek/zeek)  

## Contributing  
- Contribute scripts or report issues via [GitHub](https://github.com/zeek/zeek).  
- Follow the [contributing guidelines](https://docs.zeek.org/en/master/development/howtos/contributing.html).  

## Support  
- Join the [Zeek Slack Community](https://zeek.org/community/).  
- Ask questions on the [Zeek Discourse Forum](https://forum.zeek.org/).  

## License  
Zeek is released under the **BSD 3-Clause License**.  

---

<div style="display: flex; justify-content: space-between;">
  <a href="wireshark">🔙 Wireshark</a>
  <a href="owlsearch">🔜 OwlSearch</a>
</div>