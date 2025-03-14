---
layout: software
title: Radare
permalink: /radare
---

[🔙 Go back home](/OwlArchRepo/)

# Radare
**Binary Analysis and Reverse Engineering Toolkit**

## Introduction  
Radare2 (r2) is an open-source framework for analyzing, debugging, disassembling, and manipulating binaries. It is widely used in reverse engineering, malware analysis, and cybersecurity research.

## Features  
- Full binary analysis (disassembly, decompilation, and debugging).  
- Cross-platform support (Linux, macOS, Windows, etc.).  
- Scriptable command-line interface with automation capabilities.  
- Built-in hexadecimal editor and binary patching tools.  
- Integration with Ghidra, IDA Pro, and other reverse engineering tools.  

## Installation  

1. Open a terminal.  
2. Install Radare2 using:  
   ```sh  
   sudo pacman -S radare2  
   ```  

### Install Verification  
Check the version to confirm installation:  
```sh  
r2 -v  
```  

### Uninstall  
```sh  
sudo pacman -R radare2  
```  

## Usage  

### Analyze a Binary  
```sh  
r2 /bin/ls  
```  

### Key Commands (Inside Radare2 CLI)  
| Command       | Description                                  |
|---------------|----------------------------------------------|
| `?`           | Show help                                    |
| `aaa`         | Perform full binary analysis                |
| `afl`         | List identified functions                   |
| `pdf @ main`  | Display disassembly/pseudocode of `main`    |
| `s main`      | Seek to the `main` function                 |
| `i`           | Show binary metadata (architecture, format) |  

### Example Workflows  

#### Disassemble the `main` Function  
```sh  
r2 -A /bin/ls    # Auto-analyze the binary  
pdf @ main       # View disassembly of main  
```  

#### Search for Strings in a Binary  
```sh  
izz              # List all strings in the binary  
```  

#### Debug an Executable  
```sh  
r2 -d /bin/ls    # Start debugging  
```  

**Common Debugging Commands:**  
```  
db main    # Set breakpoint at main  
dc         # Continue execution to breakpoint  
dr         # Show register values  
px 32 @ esp # Dump 32 bytes from stack pointer  
```  

## Official Documentation & More Info  
- [GitHub Repository](https://github.com/radareorg/radare2)  
- [Radare2 Book](https://radare.gitbooks.io/radare2book/)  

## Contributing  
Contributions are welcome via GitHub pull requests. See the [contributing guidelines](https://github.com/radareorg/radare2/blob/master/CONTRIBUTING.md).  

## Support  
- Ask questions on the [Radare2 Discord](https://discord.gg/7V7Vg9Q).  
- Report issues on [GitHub](https://github.com/radareorg/radare2/issues).  

## License  
Radare2 is released under the **LGPLv3 License**.  

---

<div style="display: flex; justify-content: space-between;">
  <a href="shodan">🔙 Python Shodan</a>
  <a href="spiderfoot">🔜 SpiderFoot</a>
</div>