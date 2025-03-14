# Package Repository for the OwlArch Distribution

This repository contains a collection of packages specifically designed for **OwlArch**, an Arch Linux-based distribution focused on **OSINT** and **Malware** analysis tasks.

## Description

OwlArch is a minimalist and flexible distribution that allows users to easily customize their environment. This repository hosts additional packages to simplify the installation and management of tools and applications that enhance the user experience in OwlArch.

Packages in this repository are regularly updated and included in the official OwlArch repository to ensure access to the latest versions.

## Package List

Below is a list of packages available in this repository:

1. **[Brave](https://leku2020.github.io/OwlArchRepo/brave)**  
   Privacy-focused web browser.
2. **[Capstone](https://leku2020.github.io/OwlArchRepo/capstone)**  
   Disassembly and reverse engineering framework.
3. **[Frida](https://leku2020.github.io/OwlArchRepo/frida)**  
   Dynamic instrumentation toolkit for debugging and reverse engineering.
4. **[GDB](https://leku2020.github.io/OwlArchRepo/gdb)**  
   Debugger for analyzing and troubleshooting programs.
5. **[Ghidra](https://leku2020.github.io/OwlArchRepo/ghidra)**  
   Reverse engineering and disassembly framework.
6. **[IVRE](https://leku2020.github.io/OwlArchRepo/ivre)**  
   Network reconnaissance and OSINT analysis framework.
7. **[Maltego](https://leku2020.github.io/OwlArchRepo/maltego)**  
   OSINT platform for visualizing data relationships (domains, IPs, social networks).
8. **[Pwndbg](https://leku2020.github.io/OwlArchRepo/pwndbg)**  
   GDB extension for exploit development and advanced debugging.
9. **[Shodan](https://leku2020.github.io/OwlArchRepo/shodan)**  
   CLI tool for discovering exposed devices and services on the internet.
10. **[Radare2](https://leku2020.github.io/OwlArchRepo/radare)**  
    Reverse engineering and binary analysis framework.
11. **[Spiderfoot](https://leku2020.github.io/OwlArchRepo/spiderfoot)**  
    OSINT automation tool for threat intelligence and data correlation.
12. **[Suricata](https://leku2020.github.io/OwlArchRepo/suricata)**  
    Intrusion detection system (IDS) and network traffic monitoring tool.
13. **[TCPDump](https://leku2020.github.io/OwlArchRepo/tcpdump)**  
    Command-line packet sniffer for network traffic analysis.
14. **[theHarvester](https://leku2020.github.io/OwlArchRepo/theharvester)**  
    OSINT tool for gathering emails, subdomains, and metadata.
15. **[Volatility](https://leku2020.github.io/OwlArchRepo/volatility)**  
    Memory forensics framework for malware investigations.
16. **[Wireshark](https://leku2020.github.io/OwlArchRepo/wireshark)**  
    GUI-based network protocol analyzer.
17. **[Zeek](https://leku2020.github.io/OwlArchRepo/zeek)**  
    Network security monitoring tool for traffic analysis and anomaly detection.

## Installation

To install packages from this repository on your OwlArch system, follow these steps:

1. **Add the repository to your `pacman` configuration file:**  
   Open `/etc/pacman.conf` and append the following lines:

   ```ini
   [OwlArchRepo]
   SigLevel = Optional TrustAll
   Server = https://leku2020.github.io/OwlArchRepo/pkgs/x86_64
   ```

## Distribution
This repository is intended for use with the OwlArch distribution. The source code of the machine can be found [here](https://github.com/Leku2020/OwlArch) and machine documentation can be found [here](https://leku2020.github.io/OwlArch).