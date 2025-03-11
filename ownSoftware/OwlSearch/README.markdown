---
layout: software
title: OwlSearch
permalink: /owlsearch
---

[🔙 Go back home](/)

# OwlSearch

Herramienta en Python para buscar información en VirusTotal y MalwareBazaar por hash, IP, dominio, entre otros.

## Instalación

```sh
pacman -S owlSearch
```

## Uso

Ejecuta el script con los siguientes parámetros según el tipo de búsqueda que desees realizar.

```sh
virus-malware-search --vt --hash <HASH>
virus-malware-search --mb --tag <TAG>
```

### Opciones disponibles

#### VirusTotal
- `--vt` : Realizar búsqueda en VirusTotal.
- `--ip <IP>` : Buscar una dirección IP en VirusTotal.
- `--hash <HASH>` : Buscar un hash (MD5, SHA1, SHA256) en VirusTotal.
- `--domain <DOMINIO>` : Buscar un dominio en VirusTotal.

#### MalwareBazaar
- `--mb` : Realizar búsqueda en MalwareBazaar.
- `--hash <HASH>` : Buscar un hash en MalwareBazaar.
- `--tag <TAG>` : Buscar por tag en MalwareBazaar.
- `--sig <SIGNATURE>` : Buscar por firma en MalwareBazaar.
- `--filetype <TIPO>` : Buscar por tipo de archivo en MalwareBazaar.
- `--sample <SHA256>` : Obtener muestra de un hash en MalwareBazaar.
- `--uploadSample <ARCHIVO>` : Subir una muestra a MalwareBazaar.

## Configuración de API Keys

Para utilizar la herramienta, necesitas configurar tus claves API de VirusTotal y MalwareBazaar. Puedes hacerlo editando el archivo `virus_malware_search.py` y reemplazando `TU_API_KEY_DE_VIRUSTOTAL` y `TU_API_KEY_DE_MALWAREBAZAAR` con tus claves personales.

## Dependencias

Este script requiere Python 3 y las siguientes librerías:
- `requests`
- `argparse`

Si instalaste la herramienta desde el AUR, las dependencias ya estarán resueltas.

## Licencia

Este proyecto está bajo la licencia MIT.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar el script, abre un issue o haz un pull request en [GitHub](https://github.com/Leku2020/owlArchRepo/tree/main/ownSoftware/OwlSearch).

<div style="display: flex; justify-content: space-between;">
  <a href="zeek">🔙 Zeek</a>
  <a href="brave">🔜 Brave</a>
</div>
