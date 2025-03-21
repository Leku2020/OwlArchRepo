---
layout: software
title: OpenVPN
permalink: /openvpn
---

[🔙 Go back home](/OwlArchRepo/)

# Open VPN

## Introduction
OpenVPN is a free and open-source virtual private network software. It is designed to establish encrypted connections between devices over the internet, ensuring privacy and data protection while accessing remote networks.
It is an SSL VPN that implements OSI layer 2 and 3 secure network extension, with the up to industry standard SSL/TLS protocol.

## Features

- **SSL/TLS**: Enables secure protocol connections.
- **Privacy Protection**: Shields your connection activity.
- **Commertial/Private VPN**: Allows the use of custom or commertial VPN configurations.
- **Security**: Easily accessible security for end users.

## Installation

1. Open a terminal.
2. Install OpenVPN using the following command:

   ```sh
   sudo pacman -S openvpn
   ```

### Install verification
To verify that OpenVPN has been installed successfully, run:

   ```sh
   openvpn --version
   ```

If the version number is displayed, the installation was successful.

### Uninstall
To remove OpenVPN from your system, use:

   ```sh
   sudo pacman -Rns openvpn
   ```

## Usage

After installation, a configuration file needs to be established to conenct to either a commertial VPN server or a private server. This configuration file needs to be downloaded and stored in a dedicated folder, such as:

   ```sh
   mkdir -p ~/openvpn-configs
   cp /path/to/downloaded/config.ovpn ~/openvpn-configs/

   ```

Once stored, the file needs to be set as the openvpn config with the following command:
  
   ```sh
   sudo openvpn --config ~/openvpn-configs/config.ovpn

   ```
Once set, a prompt that requires user credentials will be required. Enter the corresponding credentials.
The log will show in the messages in console, and if successful, you will be connected to the VPN! Verify it using the following command:
  
   ```sh
   curl ifconfig.me

   ```

To deactivate the VPN connection, use the following command:
  
   ```sh
   sudo killall openvpn

   ```

OpenVPN even allows users to customize a systemctl service configuration to make openvpn automatically startup and connect at boot, giving them flexibility and easy of access in the future, however it is not implemented by default as each user needs to enter their own configuration file and credentials.

## Official documentation & More Info
- [OpenVPN official website](https://openvpn.net/)
- [Brave GitHub Repository](https://github.com/openvpn)
- [OpenVPN Community Support](https://community.openvpn.net/openvpn)

## Contributing
If you want to contribute to OpenVPN, please visit the [contributing guide](https://community.openvpn.net/openvpn/wiki/Contributing).

## Support
For support and troubleshooting, visit the [OpenVPN Support](https://support.openvpn.com/hc/en-us).

## License
OpenVPN is released under the [GPL license version 2](https://openvpn.net/License/).

---

<div style="display: flex; justify-content: space-between;">
  <a href="owlsearch">🔙 OwlSearch</a>
  <a href="capstone">🔜 Capstone</a>
</div>
