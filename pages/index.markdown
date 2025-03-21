---
layout: home
title: Index
permalink: /
---

# Package Repository for the OwlArch Distribution

This repository contains a collection of packages specifically designed for **OwlArch**, an Arch Linux-based distribution focused on **OSINT** and **Malware** analysis tasks.

## Description

OwlArch is a minimalist and flexible distribution that allows users to easily customize their environment. This repository hosts additional packages to simplify the installation and management of tools and applications that enhance the user experience in OwlArch.

Packages in this repository are regularly updated and included in the official OwlArch repository to ensure access to the latest versions.

## Package List

Below is a list of packages available in this repository:

1. **[Brave](brave)**  
   Privacy-focused web browser.

2. **[Capstone](capstone)**  
   Disassembly and reverse engineering framework.

3. **[Frida](frida)**  
   Dynamic instrumentation toolkit for debugging and reverse engineering.

4. **[GDB](gdb)**  
   Debugger for analyzing and troubleshooting programs.

5. **[Ghidra](ghidra)**  
   Reverse engineering and disassembly framework.

6. **[IVRE](ivre)**  
   Network reconnaissance and OSINT analysis framework.
   
7. **[Maltego](maltego)**  
   OSINT platform for visualizing data relationships (domains, IPs, social networks).

8. **[Pwndbg](pwndbg)**  
   GDB extension for exploit development and advanced debugging.

9. **[Shodan](shodan)**  
   CLI tool for discovering exposed devices and services on the internet.

10. **[Radare2](radare)**  
    Reverse engineering and binary analysis framework.

11. **[Spiderfoot](spiderfoot)**  
    OSINT automation tool for threat intelligence and data correlation.

12. **[Suricata](suricata)**  
    Intrusion detection system (IDS) and network traffic monitoring tool.

13. **[TCPDump](tcpdump)**  
    Command-line packet sniffer for network traffic analysis.

14. **[theHarvester](theharvester)**  
    OSINT tool for gathering emails, subdomains, and metadata.

15. **[Volatility](volatility)**  
    Memory forensics framework for malware investigations.

16. **[Wireshark](wireshark)**  
    GUI-based network protocol analyzer.

17. **[Zeek](zeek)**  
    Network security monitoring tool for traffic analysis and anomaly detection.

18. **[OwlSearch](owlsearch)**  
    Network security monitoring tool for traffic analysis and anomaly detection.

19. **[OpenVPN](openvpn)**
    Open software virtual private network, used to establish secure encripted connections between the machine and remote-host.

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

## Repository Build Process

The repository is built automatically using a GitHub Actions pipeline that follows these steps:

1. Compiles packages from `PKGBUILD` files.
2. Publishes the generated packages to the GitHub repository.
3. Builds the documentation using Jekyll.
4. Generates and updates the `OwlArchRepo` package repository.
5. Deploys the documentation and packages to GitHub Pages.

For extended documentation, press [here](actions)

## How to Contribute

Contributions are welcome! To contribute to the repository:

1. Fork the repository on GitHub.
2. Clone your fork locally:
   ```sh
   git clone https://github.com/Leku2020/OwlArchRepo.git
   ```
3. Create a new branch for your changes:
   ```sh
   git checkout -b feature/new-package
   ```
4. Add or modify packages, update documentation, or improve the repo.
5. Commit your changes and push them to your fork.
6. Open a pull request describing your changes.

For an extended document explaining the contributing rules and steps please press [here](contribute)

## Discussion Forum

If you have questions, suggestions, or want to discuss the development of this project, join the official discussion forum on [GitHub Discussions](https://github.com/Leku2020/OwlArchRepo/discussions).

