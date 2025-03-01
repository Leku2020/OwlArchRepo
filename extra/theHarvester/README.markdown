# theHarvester

## Descripción

theHarvester es una herramienta de código abierto para la recopilación de información (OSINT) sobre nombres de dominio, correos electrónicos, subdominios, direcciones IP y URLs relacionadas con un objetivo, utilizando fuentes públicas como motores de búsqueda y APIs.

## Características

- Búsqueda de información en diversas fuentes públicas
    
- Soporte para múltiples motores de búsqueda y APIs
    
- Integración con Shodan, DNSdumpster, VirusTotal, etc.
    
- Generación de informes detallados en distintos formatos
    

## Instalación

### Instalación 

```
pacman -S theHarvester
```

## Uso

Para ejecutar theHarvester, usa el siguiente comando:

```
theHarvester -d <dominio> -b <motores_de_busqueda>
```

### Ejemplo de uso

```
theHarvester -d example.com -b google,bing
```
## Opciones principales

- `-d <dominio>`: Especifica el dominio objetivo
    
- `-b <motores>`: Define los motores de búsqueda a utilizar (google, bing, yahoo, etc.)
    
- `-l <límite>`: Establece el número de resultados a recuperar
    
- `-f <archivo>`: Guarda el resultado en un archivo
    
- `-h`: Muestra la ayuda del programa
    

## Fuentes soportadas

- Google
    
- Bing
    
- Yahoo
    
- Shodan
    
- VirusTotal
    
- DNSdumpster
    
- CertSpotter
    
- Entre otros...
    

## Contribuir

Las contribuciones son bienvenidas. Puedes hacerlo mediante:

1. Fork del repositorio
    
2. Creación de una nueva rama con tus cambios
    
3. Envío de un Pull Request
    

## Licencia

Este proyecto está bajo la licencia **GPLv2**.

## Enlaces útiles

- Repositorio oficial: [GitHub](https://github.com/laramies/theHarvester)
    
- Documentación oficial: [Wiki](https://github.com/laramies/theHarvester/wiki)