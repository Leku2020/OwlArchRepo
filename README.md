# Repositorio de Paquetes para la Distribución OwlArch

Este repositorio contiene una colección de paquetes diseñados específicamente para la distribución **OwlArch**, una distribución basada en Arch Linux enfocada a tareas **OSINT** de **Malware**

## Descripción

OwlArch es una distribución minimalista y flexible que permite a los usuarios personalizar su entorno de manera sencilla. Este repositorio alberga paquetes adicionales que facilitan la instalación y gestión de herramientas y aplicaciones que mejoran la experiencia de usuario en OwlArch.

Los paquetes de este repositorio se actualizan regularmente y se incluyen en el repositorio oficial de OwlArch para garantizar la disponibilidad de las últimas versiones.

## Listado de Paquetes

A continuación, se presenta un listado de los paquetes disponibles en este repositorio:

1. **paquete1**  
   Descripción breve del paquete 1. Función principal y características destacadas.

## Instalación

Para instalar los paquetes de este repositorio en tu sistema OwlArch, sigue los siguientes pasos:

1. **Agrega el repositorio a tu archivo de configuración de `pacman`:**  
   Abre el archivo `/etc/pacman.conf` y agrega lo siguiente al final:

   ```ini
   [owlarch-packages]
   SigLevel = Required DatabaseOptional
   Server = https://repos.owlarch.org/$arch
