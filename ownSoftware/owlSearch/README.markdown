
```markdown
---
layout: software
title: OwlSearch
permalink: /owlsearch
---

[🔙 Go back home](/OwlArchRepo/)

# OwlSearch

A Python tool to search for information on VirusTotal and MalwareBazaar by hash, IP, domain, and more.

## Installation

```sh
pacman -S owlSearch
```

## Usage

Run the script with the following parameters based on the type of search you wish to perform.

```sh
owlSearch --vt --hash <HASH>
owlSearch --mb --tag <TAG>
```

### Available Options

#### VirusTotal
- `--vt` : Perform a search on VirusTotal.
- `--ip <IP>` : Search for an IP address on VirusTotal.
- `--hash <HASH>` : Search for a hash (MD5, SHA1, SHA256) on VirusTotal.
- `--domain <DOMAIN>` : Search for a domain on VirusTotal.

#### MalwareBazaar
- `--mb` : Perform a search on MalwareBazaar.
- `--hash <HASH>` : Search for a hash on MalwareBazaar.
- `--tag <TAG>` : Search by tag on MalwareBazaar.
- `--sig <SIGNATURE>` : Search by signature on MalwareBazaar.
- `--filetype <TYPE>` : Search by file type on MalwareBazaar.
- `--sample <SHA256>` : Retrieve a sample of a hash from MalwareBazaar.
- `--uploadSample <FILE>` : Upload a sample to MalwareBazaar.

## API Key Configuration

To use the tool, you need to configure your API keys for VirusTotal and MalwareBazaar. You can do this by editing the `virus_malware_search.py` file and replacing `YOUR_VIRUSTOTAL_API_KEY` and `YOUR_MALWAREBAZAAR_API_KEY` with your personal keys.

## Dependencies

This script requires Python 3 and the following libraries:
- `requests`
- `argparse`

If you installed the tool from the AUR, the dependencies will already be resolved.

## License

This project is licensed under the MIT License.

## Contributions

Contributions are welcome! If you'd like to improve the script, open an issue or submit a pull request on [GitHub](https://github.com/Leku2020/OwlArchRepo/tree/main/ownSoftware/OwlSearch).

<div style="display: flex; justify-content: space-between;">
  <a href="zeek">🔙 Zeek</a>
  <a href="brave">🔜 Brave</a>
</div>