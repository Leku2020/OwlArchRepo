---
layout: software
title: SpiderFoot
permalink: /spiderfoot
---

[🔙 Go back home](/OwlArchRepo/)

# SpiderFoot  
**OSINT and Information Gathering Tool**

## Introduction  
SpiderFoot is an automated open-source intelligence (OSINT) tool that collects and analyzes data from diverse sources for security research, threat intelligence, and cyber investigations. It simplifies reconnaissance by aggregating information about domains, IPs, email addresses, and more.

## Features  
- **Automated OSINT**: Scans domains, IPs, email addresses, and usernames across 100+ data sources.  
- **Modular Design**: Enable/disable specific modules (e.g., DNS, WHOIS, breach data).  
- **Web Interface**: Visualize findings in real-time with an interactive dashboard.  
- **API Integration**: Supports VirusTotal, Hunter.io, and other third-party services (API keys required).  
- **Export Options**: Save results in CSV, JSON, XML, or GEXF formats.  

## Installation  

1. Open a terminal.  
2. Install SpiderFoot using:  
   ```sh  
   sudo pacman -S spiderfoot  
   ```  

### Install Verification  
Check the version to confirm installation:  
```sh  
spiderfoot --version  
```  

### Uninstall  
```sh  
sudo pacman -R spiderfoot  
```  

## Usage  

### Start the Web Interface  
```sh  
spiderfoot -l 127.0.0.1:5001  
```  
Access the dashboard at:  
[http://127.0.0.1:5001](http://127.0.0.1:5001)  

### Run a Scan via CLI  
```sh  
spiderfoot -m all -t example.com  
```  

### Export Scan Results  
```sh  
spiderfoot -m all -t example.com --csv results.csv  
```  

### Example Workflows  

#### Investigate a Domain  
1. Start the web interface:  
   ```sh  
   spiderfoot -l 127.0.0.1:5001  
   ```  
2. Enter `example.com` in the web UI and run a scan.  

#### Check for Breached Emails  
```sh  
spiderfoot -m breach -t user@example.com  
```  

#### Scan an IP Address  
```sh  
spiderfoot -m all -t 8.8.8.8  
```  

## Configuration  
1. **API Keys**:  
   - Add API keys (e.g., VirusTotal, Shodan) in the web UI under **Settings** to enhance data collection.  
2. **Manual Configuration**:  
   Edit the config file:  
   ```sh  
   nano ~/.spiderfoot/config.cfg  
   ```  

## Official Documentation & More Info  
- [SpiderFoot Website](https://www.spiderfoot.net/)  
- [GitHub Repository](https://github.com/smicallef/spiderfoot)  

## Contributing  
- Contribute modules or report issues via [GitHub](https://github.com/smicallef/spiderfoot).  
- Follow the [contribution guidelines](https://github.com/smicallef/spiderfoot/blob/master/CONTRIBUTING.md).  

## Support  
- Join the [SpiderFoot Discord](https://discord.gg/spiderfoot) for community support.  
- Check the [GitHub Wiki](https://github.com/smicallef/spiderfoot/wiki) for troubleshooting.  

## License  
SpiderFoot is released under the **MIT License**.  

---

<div style="display: flex; justify-content: space-between;">
  <a href="radare">🔙 Radare</a>
  <a href="suricata">🔜 Suricata</a>
</div>