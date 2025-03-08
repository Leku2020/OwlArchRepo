---
layout: software
title: Python Shodan
permalink: /shodan
---

[🔙 Go back home](/)

# Shodan  
**Search Engine for Internet-Connected Devices**

## Introduction  
Shodan is a specialized search engine for discovering internet-connected devices such as servers, cameras, routers, and more. It is widely used in cybersecurity for threat analysis, vulnerability assessment, and network reconnaissance.

## Features  
- Search for devices by keywords, services, or banners.  
- Identify exposed databases, webcams, industrial control systems, and IoT devices.  
- Filter results by location, organization, operating system, or port.  
- Export data in CSV, JSON, or XML formats.  
- Real-time monitoring of network infrastructure changes.  

## Installation  

1. Open a terminal.  
2. Install Shodan using:  
   ```sh  
   sudo pacman -S shodan  
   ```  

### Install Verification  
Check the Shodan version to confirm installation:  
```sh  
shodan version  
```  

### Uninstall  
```sh  
sudo pacman -R shodan  
```  

## Usage  

### Configuration  
1. **Get an API Key**:  
   - Sign up at [Shodan](https://www.shodan.io/).  
   - Navigate to **My Account** > **API Keys** to retrieve your key.  

2. **Initialize the API Key**:  
   ```sh  
   shodan init YOUR_API_KEY  
   ```  

### Basic Commands  

#### Search for Devices  
```sh  
shodan search "apache"  
```  

#### Get Information About an IP Address  
```sh  
shodan host 8.8.8.8  
```  

#### List Common Services  
```sh  
shodan stats apache  
```  

#### Check Open Ports on an IP  
```sh  
shodan host 1.1.1.1 | grep ports  
```  

#### Export Results to CSV  
```sh  
shodan search --limit 100 "cisco" --fields ip_str,port,org --separator , > results.csv  
```  

### Example Workflow  
1. **Find vulnerable web servers**:  
   ```sh  
   shodan search "http.title:'Apache2 Ubuntu Default Page'"  
   ```  

2. **Identify exposed databases**:  
   ```sh  
   shodan search "product:mysql"  
   ```  

## Official Documentation & More Info  
- [Shodan Homepage](https://www.shodan.io/)  
- [API Documentation](https://shodan.readthedocs.io/)  

## Contributing  
Shodan is a proprietary tool, but community contributions to open-source integrations (e.g., Python libraries) are welcome. Check their [GitHub repositories](https://github.com/shodan-tool) for details.  

## Support  
- Ask questions on the [Shodan Community Forum](https://community.shodan.io/).  
- Report issues via the [Shodan Support Portal](https://help.shodan.io/).  

## License  
Shodan’s CLI tool is released under the **MIT License**.  

---

<div style="display: flex; justify-content: space-between;">
  <a href="pwndbg">🔙 PWNDBG</a>
  <a href="radare">🔜 Radare</a>
</div>