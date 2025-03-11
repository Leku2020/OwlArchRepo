---
layout: software
title: IVRE
permalink: /ivre
---

[🔙 Go back home](/owlArchRepo/)

# IVRE  
**Network Reconnaissance and Vulnerability Analysis Framework**

## Introduction  
IVRE (Instrument de VEille Réseau) is an open-source framework for network reconnaissance, vulnerability assessment, and asset management. It automates network scanning, processes scan results, and provides a web-based interface for analyzing and visualizing network data.

## Features  
- **Network Scanning**: Integrates with tools like Nmap, Masscan, and ZMap for automated scanning.  
- **Centralized Database**: Stores scan results in a MongoDB backend for efficient querying.  
- **Web Interface**: Interactive dashboard for visualizing network topology and vulnerabilities.  
- **Vulnerability Detection**: Cross-references scan data with CVE databases and exploit frameworks.  
- **Scalability**: Handles large-scale network scans and distributed deployments.  

## Installation  

1. **Install Dependencies**:  
   ```sh  
   sudo pacman -S mongodb nmap python-pip  
   ```  

2. **Install IVRE via pip**:  
   ```sh  
   pip install ivre  
   ```  

### Configuration  
1. **Set Up MongoDB**:  
   Start the MongoDB service:  
   ```sh  
   sudo systemctl enable --now mongodb  
   ```  

2. **Initialize IVRE Database**:  
   ```sh  
   ivre db --init  
   ```  

3. **Configure IVRE**:  
   Edit the configuration file at `~/.ivre.conf` to customize scan ranges, ports, and credentials.  

### Install Verification  
Check IVRE version:  
```sh  
ivre --version  
```  

### Uninstall  
```sh  
pip uninstall ivre  
```  

## Usage  

### Basic Commands  

#### Start a Network Scan  
```sh  
ivre scan --output=XML --range=192.168.1.0/24  
```  

#### Import Nmap Results into IVRE  
```sh  
ivre scan2db -s nmap -r scan_results.xml  
```  

#### Query the Database  
```sh  
ivre ip 192.168.1.1  
```  

#### Launch the Web Interface  
```sh  
ivreweb  
```  
Access the dashboard at `http://localhost:8000`.  

### Example Workflows  

#### Scan a Subnet and Visualize Results  
```sh  
ivre runscans --output=XML --range=10.0.0.0/24  
ivre scan2db -s nmap -r scan.xml  
ivreweb  
```  

#### Check Open Ports on a Specific IP  
```sh  
ivre ip 192.168.1.100 | grep "open ports"  
```  

#### Generate a Network Report  
```sh  
ivre report --format=html --output=report.html  
```  

## Official Documentation & More Info  
- [GitHub Repository](https://github.com/ivre/ivre)  
- [IVRE Documentation](https://ivre.readthedocs.io/)  

## Contributing  
- Report issues or contribute code via [GitHub](https://github.com/ivre/ivre).  
- Follow the [contribution guidelines](https://github.com/ivre/ivre/blob/main/CONTRIBUTING.md).  

## Support  
- Join the [IVRE Discord](https://discord.gg/invite/ivre) for community support.  
- Check the [GitHub Issues](https://github.com/ivre/ivre/issues) for troubleshooting.  

## License  
IVRE is released under the **AGPLv3 License**.  

---

<div style="display: flex; justify-content: space-between;">
  <a href="ghidra">🔙 Ghidra</a>
  <a href="maltego">🔜 Maltego</a>
</div>