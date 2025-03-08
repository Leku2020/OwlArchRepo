---
layout: software
title: Capstone
permalink: /capstone
---

[🔙 Go back home](/)

# Capstone

## Introduction
Capstone is a lightweight, multi-platform, and multi-architecture framework for machine code disassembly. It provides a powerful and flexible disassembly engine that supports multiple architectures, making it a valuable tool for reverse engineering and security research.

## Features

- **Multi-Architecture Support**: Works with x86, ARM, MIPS, and more.
- **Cross-Platform**: Available on Linux, macOS, and Windows.
- **Lightweight and Fast**: Optimized for performance and efficiency.
- **Bindings for Multiple Languages**: Supports Python, C, Java, and other languages.
- **Flexible Output**: Provides detailed instruction information in an easy-to-use format.

## Installation

1. Open a terminal.
2. Install Capstone using the following command:

   ```sh
   sudo pacman -S capstone-git
   ```

### Install verification
To check if Capstone is installed correctly, run:

   ```sh
   capstone -v
   ```

If the version number is displayed, the installation was successful.

### Uninstall
To remove Capstone from your system, use:

   ```sh
   sudo pacman -Rns capstone-git
   ```

## Usage

### Basic Disassembly
To disassemble a binary file using `objdump` with Intel syntax:

   ```sh
   objdump -d -M intel /path/to/file
   ```

### Using `capstone-engine` from CLI
If Capstone was compiled with CLI tools, you can use `cstool` to disassemble instructions:

   ```sh
   cstool x64 "55 48 8B 05 B8 13 00 00"
   ```

Expected output:

   ```
   0  55                             push    rbp
   1  48 8b 05 b8 13 00 00           mov     rax, qword ptr [rip + 0x13b8]
   ```

## Official documentation & More Info
- [Capstone Official Website](http://www.capstone-engine.org/)
- [Capstone GitHub Repository](https://github.com/aquynh/capstone)

## Contributing
If you want to contribute to Capstone, check out the [GitHub repository](https://github.com/aquynh/capstone) for contribution guidelines.

## Support
For support and troubleshooting, visit the official [Capstone GitHub issues page](https://github.com/aquynh/capstone/issues).

## License
Capstone is released under the [BSD License](https://github.com/aquynh/capstone/blob/master/LICENSE.TXT).

---

<div style="display: flex; justify-content: space-between;">
  <a href="brave">🔙 Brave</a>
  <a href="frida">🔜 Frida</a>
</div>