---
layout: software
title: Ghidra
permalink: /ghidra
---
# Ghidra

Ghidra es una herramienta de análisis de software de código abierto desarrollada por la NSA. Se utiliza para la ingeniería inversa de binarios y ofrece una interfaz gráfica avanzada junto con potentes capacidades de desensamblado, depuración y análisis de código.

## Instalación

```
pacman -S ghidra
```
## Uso Básico

### Crear un Nuevo Proyecto

1. Abre Ghidra con `ghidra` desde la terminal.
    
2. Crea un nuevo proyecto y selecciona **Non-Shared Project**.
    
3. Importa el archivo binario que deseas analizar.
    

### Desensamblado y Análisis

- Usa la ventana de **CodeBrowser** para explorar el binario.
    
- Identifica funciones y variables con la opción **Auto-Analysis**.
    
- Genera código en diferentes lenguajes con el **Decompiler**.
    

### Depuración de Binarios

Si necesitas depurar un binario:

1. Habilita el modo de **Debugger**.
    
2. Conéctate a un proceso en ejecución.
    
3. Establece puntos de interrupción y monitorea la ejecución en tiempo real.
    

## Documentación Oficial

Para más información, consulta la documentación oficial:

- [Sitio Web](https://ghidra-sre.org/)
    
- [Repositorio en GitHub](https://github.com/NationalSecurityAgency/ghidra)