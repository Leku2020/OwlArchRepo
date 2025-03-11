---
layout: software
title: Maltego
permalink: /maltego
---

[🔙 Go back home](/owlArchRepo/)

# Maltego - Intelligence and Data Analysis Tool

## Introduction
Maltego is a data mining and analysis tool used for information gathering, cybersecurity, and OSINT (Open Source Intelligence) investigations.

## Features

- **Graph-based Analysis**: Visualize relationships between entities.
- **OSINT Integration**: Gather information from public sources.
- **Transformations**: Automate data collection and correlation.
- **Custom API Integration**: Connect with services like Shodan, VirusTotal, etc.
- **Collaboration Support**: Share intelligence with teams.

## Installation

1. Open a terminal.
2. Install Maltego using the following command:

   ```sh
   sudo pacman -S maltego
   ```

### Install verification
To verify that Maltego has been installed correctly, run:

   ```sh
   maltego
   ```

If the Maltego interface opens, the installation was successful.

### Uninstall
To remove Maltego from your system, use:

   ```sh
   sudo pacman -Rns maltego
   ```

## Usage

### Launching Maltego

To start Maltego, run:

   ```sh
   maltego
   ```

### Creating a New Entity

1. Open Maltego and select an entity type (Domain, IP, Person, etc.).
2. Drag the entity onto the workspace.

### Running Transformations

1. Right-click on an entity.
2. Select a transformation to retrieve more information.

### Saving and Exporting an Analysis

- To save the analysis, go to `File -> Save`.
- To export in another format, go to `File -> Export` and choose the desired format.

## Configuration

Maltego allows adding **Custom Transformations** and configuring **External APIs** to enhance information gathering. To configure them, go to:

   ```sh
   Edit -> Options -> Transform Servers
   ```

You can also add API keys in the configuration for access to advanced services like Shodan, VirusTotal, etc.

## Official documentation & More Info
- [Maltego Official Website](https://www.maltego.com/)
- [Maltego Documentation](https://docs.maltego.com/)

## Contributing
If you want to contribute to Maltego, check the official documentation for API extensions and community involvement.

## Support
For support and troubleshooting, visit the [Maltego Support Page](https://www.maltego.com/contact-support/).

## License
Maltego is distributed under a proprietary license. Refer to the [Maltego Terms of Service](https://www.maltego.com/terms-of-use/) for details.

---

<div style="display: flex; justify-content: space-between;">
  <a href="ivre">🔙 IVRE</a>
  <a href="pwndbg">🔜 PwnDBG</a>
</div>