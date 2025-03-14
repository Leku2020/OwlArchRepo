---
layout: software
title: GDB
permalink: /gdb
---

[🔙 Go back home](/OwlArchRepo/)

# GDB - GNU Debugger

## Introduction
GDB (GNU Debugger) is a powerful debugging tool for Unix and Linux systems. It allows users to inspect program execution, set breakpoints, and analyze errors.

## Features

- **Breakpoints and Watchpoints**: Stop execution at specific points to inspect program state.
- **Step-by-Step Execution**: Execute code line by line for detailed debugging.
- **Variable Inspection**: View and modify variable values during runtime.
- **Core Dump Analysis**: Debug programs post-crash using core dump files.
- **Remote Debugging**: Debug applications running on remote systems.

## Installation

1. Open a terminal.
2. Install GDB using the following command:

   ```sh
   sudo pacman -S gdb
   ```

### Install verification
To check if GDB has been installed correctly, run:

   ```sh
   gdb --version
   ```

If the version number is displayed, the installation was successful.

### Uninstall
To remove GDB from your system, use:

   ```sh
   sudo pacman -Rns gdb
   ```

## Usage

GDB provides multiple functionalities for debugging programs. Some basic commands include:

- Start GDB with a program:

   ```sh
   gdb ./my_program
   ```

- Run the program inside GDB:

   ```sh
   run
   ```

- Set a breakpoint at a specific function:

   ```sh
   break function_name
   ```

- Continue execution after hitting a breakpoint:

   ```sh
   continue
   ```

- Inspect the value of a variable:

   ```sh
   print variable_name
   ```

- Exit GDB:

   ```sh
   quit
   ```

## Official documentation & More Info
- [GDB Official Website](https://www.gnu.org/software/gdb/)
- [GDB Git Repository](https://sourceware.org/git/?p=binutils-gdb.git)

## Contributing
If you want to contribute to GDB, check out the [GDB development mailing list](https://sourceware.org/gdb/) for guidelines.

## Support
For support and troubleshooting, visit the [GDB Bugzilla](https://sourceware.org/bugzilla/) or the [GDB mailing list](https://sourceware.org/gdb/mailing-lists/).

## License
GDB is released under the [GNU General Public License (GPL)](https://www.gnu.org/licenses/gpl-3.0.html).

---

<div style="display: flex; justify-content: space-between;">
  <a href="frida">🔙 Frida</a>
  <a href="ghidra">🔜 Ghidra</a>
</div>