---
layout: software
title: Ghidra
permalink: /ghidra
---

[🔙 Go back home](/owlArchRepo/)

# Ghidra

## Introduction
Ghidra is an open-source software analysis tool developed by the NSA. It is used for reverse engineering binaries and offers an advanced graphical interface along with powerful disassembly, debugging, and code analysis capabilities.

## Features

- **Disassembly & Decompilation**: Converts binary code into human-readable formats.
- **Graphical Interface**: Provides an intuitive UI for easy navigation.
- **Auto-Analysis**: Identifies functions, variables, and structures automatically.
- **Cross-Platform**: Runs on Windows, Linux, and macOS.
- **Debugger Integration**: Supports debugging of running binaries.

## Installation

1. Open a terminal.
2. Install Ghidra using the following command:

   ```sh
   sudo pacman -S ghidra
   ```

### Install verification
To verify that Ghidra has been installed correctly, run:

   ```sh
   ghidra
   ```

If the Ghidra interface opens, the installation was successful.

### Uninstall
To remove Ghidra from your system, use:

   ```sh
   sudo pacman -Rns ghidra
   ```

## Usage

### Creating a New Project

1. Open Ghidra with `ghidra` from the terminal.
2. Create a new project and select **Non-Shared Project**.
3. Import the binary file you want to analyze.

### Disassembly & Analysis

- Use the **CodeBrowser** window to explore the binary.
- Identify functions and variables using **Auto-Analysis**.
- Generate code in different languages using the **Decompiler**.

### Debugging Binaries

If you need to debug a binary:

1. Enable the **Debugger** mode.
2. Connect to a running process.
3. Set breakpoints and monitor execution in real-time.

## Official documentation & More Info
- [Ghidra Official Website](https://ghidra-sre.org/)
- [Ghidra GitHub Repository](https://github.com/NationalSecurityAgency/ghidra)

## Contributing
If you want to contribute to Ghidra, check out the [GitHub repository](https://github.com/NationalSecurityAgency/ghidra) for contribution guidelines.

## Support
For support and troubleshooting, visit the [Ghidra GitHub Issues page](https://github.com/NationalSecurityAgency/ghidra/issues).

## License
Ghidra is released under the [Apache License 2.0](https://github.com/NationalSecurityAgency/ghidra/blob/master/LICENSE).

---

<div style="display: flex; justify-content: space-between;">
  <a href="gdb">🔙 GDB</a>
  <a href="ivre">🔜 ivre</a>
</div>