---
layout: software
title: TCPDump
permalink: /tcpdump
---

[🔙 Go back home](/owlArchRepo/)

# TCPDump
**Network Sniffer and Packet Analyzer**

## Introduction  
tcpdump is a command-line tool for capturing and analyzing network traffic. It is widely used by system administrators and cybersecurity professionals to diagnose network issues, monitor packets, and investigate security incidents.

## Features  
- **Packet Capture**: Capture live traffic from network interfaces.  
- **Filtering**: Use BPF (Berkeley Packet Filter) syntax to filter packets by protocol, host, port, or content.  
- **Protocol Support**: Decode protocols like TCP, UDP, ICMP, HTTP, DNS, and TLS.  
- **File Output**: Save captures to `.pcap` files for later analysis (compatible with Wireshark).  
- **Lightweight**: Minimal resource usage compared to GUI-based tools.  

## Installation  

1. Open a terminal.  
2. Install tcpdump using:  
   ```sh  
   sudo pacman -S tcpdump  
   ```  

### Install Verification  
Check the version to confirm installation:  
```sh  
tcpdump --version  
```  

### Uninstall  
```sh  
sudo pacman -R tcpdump  
```  

## Usage  

### Basic Commands  

#### Capture Traffic on a Specific Interface  
```sh  
sudo tcpdump -i eth0  
```  

#### Save Capture to a File  
```sh  
sudo tcpdump -i eth0 -w capture.pcap  
```  

#### Read Packets from a File  
```sh  
tcpdump -r capture.pcap  
```  

### Filtering Examples  

#### Filter by Protocol (e.g., ICMP)  
```sh  
sudo tcpdump -i eth0 icmp  
```  

#### Filter Traffic for a Specific Host  
```sh  
sudo tcpdump -i eth0 host 192.168.1.1  
```  

#### Filter Traffic on a Specific Port (e.g., HTTP)  
```sh  
sudo tcpdump -i eth0 port 80  
```  

### Advanced Filters  

#### Capture TCP Traffic Between Two Hosts  
```sh  
sudo tcpdump -i eth0 tcp and host 192.168.1.10 and host 192.168.1.20  
```  

#### Display Packet Contents in ASCII/Hex  
```sh  
sudo tcpdump -i eth0 -A  
```  

### Example Workflow  

#### Capture DNS Queries  
```sh  
sudo tcpdump -i eth0 port 53  
```  

#### Capture HTTP GET Requests  
```sh  
sudo tcpdump -i eth0 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420'  
```  

## Official Documentation & More Info  
- [tcpdump Official Site](https://www.tcpdump.org/)  
- [Manual Page](https://www.tcpdump.org/manpages/tcpdump.1.html)  

## Contributing  
tcpdump is maintained by the [TCPDUMP Group](https://www.tcpdump.org/#contributing). Contributions are welcome via patches or bug reports.  

## Support  
- Ask questions on the [tcpdump mailing list](https://www.tcpdump.org/#mailing-lists).  
- Check the [FAQ](https://www.tcpdump.org/faq.html) for troubleshooting.  

## License  
tcpdump is released under the **BSD 3-Clause License**.  

---

<div style="display: flex; justify-content: space-between;">
  <a href="suricata">🔙 Suricata</a>
  <a href="theharvester">🔜 TheHarvester</a>
</div>