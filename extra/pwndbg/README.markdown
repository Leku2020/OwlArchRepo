---
layout: software
title: pwndbg
permalink: /pwndbg
---

[🔙 Go back home](/OwlArchRepo/)

# Pwndbg

## Introduction

Pwndbg is an extension for GDB that enhances debugging with advanced tools and a more intuitive interface. It is particularly useful for security analysis and binary exploitation.

## Features

- **Enhanced Register View**: Displays real-time register values with color coding.
- **Interactive Disassembly**: Highlights assembly code syntax.
- **Memory Inspection**: Simplifies heap, stack, and memory segment analysis.
- **Custom Commands**: Adds useful commands like `heap`, `vmmap`, and `telescope`.

## Installation

1. Open a terminal.
2. Install Pwndbg using the following command:

   ```sh
   pacman -S pwndbg-git
   ```

### Install verification
To verify that Pwndbg has been installed correctly, open GDB and check if Pwndbg is loaded:

   ```sh
   gdb
   ```

You should see a message indicating that Pwndbg is activated.

### Uninstall
To remove Pwndbg from your system, use:

   ```sh
   pacman -Rns pwndbg-git
   ```

## Usage

### Launching Pwndbg

Start GDB with your program:

   ```sh
   gdb -q ./my_program
   ```

Once inside GDB, you can use Pwndbg commands like:

   ```sh
   pwndbg> heap
   pwndbg> vmmap
   pwndbg> telescope $rsp
   ```

## Official documentation & More Info
- [Pwndbg GitHub Repository](https://github.com/pwndbg/pwndbg)

## Contributing
If you want to contribute to Pwndbg, visit the official GitHub repository for contribution guidelines.

## Support
For support and troubleshooting, check the GitHub issues section of the Pwndbg repository.

## License
Pwndbg is released under the MIT License. Refer to the [GitHub repository](https://github.com/pwndbg/pwndbg) for details.

---

<div style="display: flex; justify-content: space-between;">
  <a href="maltego">🔙 Maltego</a>
  <a href="shodan">🔜 Python Shodan</a>
</div>