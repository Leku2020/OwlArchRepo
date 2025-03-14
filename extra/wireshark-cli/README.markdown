---
layout: software
title: Wireshark
permalink: /wireshark
---

[🔙 Go back home](/OwlArchRepo/)

# Wireshark  
**Network Protocol Analyzer**

## Introduction  
Wireshark is a powerful open-source tool for capturing and analyzing network traffic in real time. It is widely used by network administrators, developers, and security analysts to troubleshoot networks, debug protocols, and investigate security incidents.

## Features  
- **Real-Time Packet Capture**: Analyze live network traffic across multiple interfaces.  
- **Protocol Decoding**: Supports over 3,000 protocols (HTTP, DNS, TLS, etc.).  
- **Graphical Interface (Qt)**: Visualize traffic with color-coded packet details.  
- **Command-Line Tools**: Use `tshark` for headless analysis.  
- **Filters**: Apply display and capture filters to isolate specific traffic.  
- **Export Data**: Save captures in PCAP, CSV, or JSON formats.  

## Installation  

### Available Packages  
- **`wireshark-cli`**: Command-line tools (`tshark`, `dumpcap`).  
- **`wireshark-qt`**: Full GUI version with Qt interface.  

1. Install both packages:  
   ```sh  
   sudo pacman -S wireshark-cli wireshark-qt  
   ```  

### Configure Permissions  
To capture packets without root privileges:  
1. Add your user to the `wireshark` group:  
   ```sh  
   sudo usermod -aG wireshark $USER  
   ```  
2. Grant capabilities to `dumpcap`:  
   ```sh  
   sudo setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap  
   ```  
3. Log out and log back in for changes to take effect.  

## Usage  

### Launch the GUI  
```sh  
wireshark  
```  

### Capture Traffic via CLI (`tshark`)  
```sh  
tshark -i eth0  
```  

### Common Commands  
| Command                          | Description                                  |
|----------------------------------|----------------------------------------------|
| `tshark -i <interface>`          | Capture traffic on a specific interface.    |
| `tshark -r file.pcap`            | Read a saved PCAP file.                      |
| `tshark -Y "http"`               | Filter HTTP traffic during capture.         |
| `tshark -T fields -e ip.src`     | Extract specific fields (e.g., source IPs).  |

### Example Workflow  
1. **Capture HTTPS traffic**:  
   ```sh  
   tshark -i eth0 -Y "tls" -w https_traffic.pcap  
   ```  
2. **Analyze DNS queries in the GUI**:  
   Open `https_traffic.pcap` in Wireshark and apply the filter `dns`.  

## Official Documentation & More Info  
- [Wireshark Official Site](https://www.wireshark.org/)  
- [Wireshark Documentation](https://www.wireshark.org/docs/)  
- [AUR Package (wireshark-cli)](https://aur.archlinux.org/packages/wireshark-cli/)  
- [AUR Package (wireshark-qt)](https://aur.archlinux.org/packages/wireshark-qt/)  

## Contributing  
- Contribute code or report bugs via [GitHub](https://github.com/wireshark/wireshark).  
- Follow the [developer guide](https://www.wireshark.org/docs/wsdg_html_chunked/).  

## Support  
- Ask questions on the [Wireshark Q&A Forum](https://ask.wireshark.org/).  
- Join the [Wireshark Discord](https://discord.gg/wireshark).  

## License  
Wireshark is released under the **GPL-2.0 License**.  

---

<div style="display: flex; justify-content: space-between;">
  <a href="volatility">🔙 Volatility</a>
  <a href="zeek">🔜 Zeek</a>
</div>