---
layout: software
title: ProxyChains
permalink: /proxychains
---

[🔙 Go back home](/OwlArchRepo/)

# ProxyChains-NG

## Introduction
ProxyChains-NG is a tool that forces network connections to go through a chain of proxies for anonymity and security. It supports SOCKS and HTTP proxies, allowing users to mask their IP and bypass restrictions.

## Features

- *Proxy chaining*: Routes traffic through multiple proxies for enhanced anonymity.
- *Support for SOCKS4, SOCKS5, and HTTP proxies*: Allows various types of proxy protocols.
- *Flexible configuration*: Enables dynamic, strict, or random proxy chains based on user preference.

## Installation

1. Open a terminal.
2. Install proxychains-ng using the following command:

   ```sh
   sudo pacman -S proxychains-ng
   ```

### Uninstall
To remove OpenVPN from your system, use:

   ```sh
   sudo pacman -R proxychains-ng
   ```

## Usage

After installation, a configuration file needs to be established. This is done to set the proxy list and the proxy type that will be used by proxychains. Open the config file with:

   ```sh
   sudo nano /etc/proxychains.conf

   ```

Add the proxy at the bottom of the file, for example, for a SOCKS5 proxy, add:
  
   ```sh
   `socks5 127.0.0.1 9050`

   ```
Once set, choose a proxy set type from the available options explained below:
   - **Strict Chain**: Uses proxies in the exact order you set them.  
   - **Dynamic Chain**: Tries proxies in order but skips failed ones.  
   - **Random Chain**: Selects proxies randomly from the list.

Press `Ctrl + O` to save and `Ctrl + X` to exit the editor

Now, to use it, test the following command:
  
   ```sh
   `proxychains firefox`

   ```

Now that this is configured, traffic will be redirected through these proxy chains, increasing privacy and security in our searches!

## Official documentation & More Info
- [ProxyChains-NG official website](https://openvpn.net/)
- [ProxyChains-NG GitHub Repository](https://github.com/rofl0r/proxychains-ng)
- [ProxyChains-NG Cummunity](https://github.com/rofl0r/proxychains-ng)
- [ProxyChains-NG Wiki](https://github.com/rofl0r/proxychains-ng/wiki)

## Contributing
If you want to contribute to ProxyChains-NG, please visit the [contributing guide](https://github.com/rofl0r/proxychains-ng/blob/master/CONTRIBUTING.md).

## Support
For support and troubleshooting, visit the [ProxyChains-NG support](https://github.com/rofl0r/proxychains-ng/wiki).

## License
ProxyChains is released under the [GPL-3.0 License](https://opensource.org/licenses/GPL-3.0).

---

<div style="display: flex; justify-content: space-between;">
  <a href="owlsearch">🔙 OwlSearch</a>
  <a href="openvpn">🔜 OpenVpn</a>
</div>
