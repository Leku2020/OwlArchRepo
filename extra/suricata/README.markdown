---
layout: software
title: Suricata
permalink: /suricata
---

[🔙 Go back home](/OwlArchRepo/)

# Suricata  
**Intrusion Detection and Prevention System (IDS/IPS)**

## Introduction  
Suricata is a high-performance open-source tool for intrusion detection (IDS), intrusion prevention (IPS), and network security monitoring (NSM). It uses rule-based detection and protocol analysis to identify threats in real time.

## Features  
- **Multi-Threaded Architecture**: Optimized for high-speed networks.  
- **Protocol Analysis**: Deep inspection of HTTP, TLS, DNS, and other protocols.  
- **Signature-Based Detection**: Customizable rules for threat identification.  
- **File Extraction**: Extract files from network traffic for analysis.  
- **Integration**: Works with SIEM tools like Elasticsearch and Splunk.  
- **IPv6 and TLS Support**: Monitors modern network protocols.  

## Installation  

1. Open a terminal.  
2. Install Suricata using:  
   ```sh  
   sudo pacman -S suricata  
   ```  

### Install Verification  
Test the configuration file syntax:  
```sh  
suricata -T -c /etc/suricata/suricata.yaml  
```  

### Uninstall  
```sh  
sudo pacman -R suricata  
```  

## Usage  

### Run Suricata in IDS Mode  
```sh  
sudo suricata -c /etc/suricata/suricata.yaml -i eth0  
```  

### Analyze a PCAP File Offline  
```sh  
suricata -c /etc/suricata/suricata.yaml -r capture.pcap  
```  

### Monitor Real-Time Alerts  
```sh  
tail -f /var/log/suricata/fast.log  
```  

### Update Detection Rules  
```sh  
sudo suricata-update  
```  

## Configuration  

### Main Configuration File  
```sh  
/etc/suricata/suricata.yaml  
```  

### Rule Directories  
- **Default rules**:  
  ```sh  
  /var/lib/suricata/rules/  
  ```  
- **Custom rules**: Add `.rules` files to this directory and reload Suricata.  

### Example: Enable Community Rules  
1. Edit `suricata.yaml`:  
   ```sh  
   nano /etc/suricata/suricata.yaml  
   ```  
2. Uncomment or add rule sources (e.g., `community.rules`).  

## Official Documentation & More Info  
- [Suricata Official Site](https://suricata.io/)  
- [Documentation](https://suricata.readthedocs.io/)  

## Contributing  
- Report issues or contribute code via [GitHub](https://github.com/OISF/suricata).  
- Follow the [contribution guidelines](https://github.com/OISF/suricata/blob/master/CONTRIBUTING.md).  

## Support  
- Join the [Suricata Community Forum](https://forum.suricata.io/).  
- Ask questions on [GitHub Discussions](https://github.com/OISF/suricata/discussions).  

## License  
Suricata is released under the **GPLv2 License**.  

---

<div style="display: flex; justify-content: space-between;">
  <a href="spiderfoot">🔙 SpiderFoot</a>
  <a href="tcpdump">🔜 TCPDump</a>
</div>