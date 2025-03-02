---
layout: home
title: Index
permalink: /
---

# Repositorio de Paquetes para la Distribución OwlArch

Este repositorio contiene una colección de paquetes diseñados específicamente para la distribución **OwlArch**, una distribución basada en Arch Linux enfocada a tareas **OSINT** de **Malware**

## Descripción

OwlArch es una distribución minimalista y flexible que permite a los usuarios personalizar su entorno de manera sencilla. Este repositorio alberga paquetes adicionales que facilitan la instalación y gestión de herramientas y aplicaciones que mejoran la experiencia de usuario en OwlArch.

Los paquetes de este repositorio se actualizan regularmente y se incluyen en el repositorio oficial de OwlArch para garantizar la disponibilidad de las últimas versiones.

## Listado de Paquetes

A continuación, se presenta un listado de los paquetes disponibles en este repositorio:

1. [Brave](brave)

    Navegador web enfocado en privacidad y seguridad.
2. [Capstone](capstone)

    Framework para desensamblado de código máquina.
3. [Ghidra](ghidra)

    Herramienta de análisis de software de código abierto.
4. [Radare](radare2)

    Framework para ingeniería inversa y análisis binario.
5. [The harvester](theHarvester)

    Herramienta de recopilación de información para pruebas de seguridad.
6. [Frida](frida)

    Herramienta para instrumentación dinámica de aplicaciones.

## Instalación

Para instalar los paquetes de este repositorio en tu sistema OwlArch, sigue los siguientes pasos:

1. **Agrega el repositorio a tu archivo de configuración de `pacman`:**  
   Abre el archivo `/etc/pacman.conf` y agrega lo siguiente al final:

   ```ini
    [owlArchRepo]
    SigLevel = Optional TrustAll
    Server = https://leku2020.github.io/owlArchRepo/pkgs/x86_64
    ```