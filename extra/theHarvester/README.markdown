---
layout: software
title: The Harvester
permalink: /theharvester
---

[🔙 Go back home](/owlArchRepo/)

# The Harvester  
**OSINT Tool for Domain and Email Discovery**

## Introduction  
theHarvester is an open-source OSINT (Open-Source Intelligence) tool designed to gather information about domains, emails, subdomains, IP addresses, and URLs associated with a target. It leverages public sources like search engines, APIs, and databases for reconnaissance.

## Features  
- Aggregates data from search engines, DNS records, and threat intelligence platforms.  
- Supports integration with Shodan, VirusTotal, DNSdumpster, and CertSpotter.  
- Generates detailed reports in multiple formats (TXT, XML, JSON).  
- Lightweight and optimized for penetration testing and security audits.  

## Installation  

1. Install via pacman:  
   ```sh  
   sudo pacman -S theHarvester  
   ```  

### Install Verification  
Check the version to confirm installation:  
```sh  
theHarvester -h | head -n 1  
```  

### Uninstall  
```sh  
sudo pacman -R theHarvester  
```  

## Usage  

### Basic Syntax  
```sh  
theHarvester -d <domain> -b <sources>  
```  

### Example: Harvest Emails and Subdomains  
```sh  
theHarvester -d example.com -b google,shodan  
```  

### Key Options  
| Option          | Description                                  |
|-----------------|----------------------------------------------|
| `-d <domain>`   | Target domain (e.g., `example.com`).         |
| `-b <sources>`  | Comma-separated list of sources (e.g., `google,bing`). |
| `-l <limit>`    | Maximum number of results to retrieve.      |
| `-f <file>`     | Save output to a file (e.g., `report.txt`).  |
| `-h`            | Display help menu.                           |

### Supported Sources  
- **Search Engines**: Google, Bing, Yahoo  
- **APIs**: Shodan, VirusTotal, DNSdumpster, CertSpotter  
- **Others**: Netcraft, SecurityTrails, CRT.SH  

### Example Workflow  

#### Find Subdomains and Emails  
```sh  
theHarvester -d target.com -b google,bing,shodan -l 500 -f results.txt  
```  

#### Analyze Results with VirusTotal  
```sh  
theHarvester -d malicious-domain.com -b virustotal  
```  

## Official Documentation & More Info  
- [GitHub Repository](https://github.com/laramies/theHarvester)  
- [Wiki Documentation](https://github.com/laramies/theHarvester/wiki)  

## Contributing  
1. Fork the repository.  
2. Create a feature branch (`git checkout -b feature/your-changes`).  
3. Submit a pull request via GitHub.  

## Support  
- Report issues on [GitHub](https://github.com/laramies/theHarvester/issues).  
- Join the community discussions in the repository’s [Discussions tab](https://github.com/laramies/theHarvester/discussions).  

## License  
theHarvester is released under the **GPLv2 License**.  

---

<div style="display: flex; justify-content: space-between;">
  <a href="tcpdump">🔙 TCPDUMP</a>
  <a href="volatility">🔜 Volatility</a>
</div>