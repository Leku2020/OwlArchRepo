---
layout: software
title: Capstone
permalink: /capstone
---

# Capstone

Capstone es un framework ligero, multiplataforma y multi-arquitectura para desensamblado de código máquina.

## Instalación


```
pacman -S capstone-git
```


## Uso Básico

### Verificar instalación y versión

```
capstone -v
```

### Desensamblado de un archivo binario

```
objdump -d -M intel /ruta/al/archivo
```

### Uso con `capstone-engine` desde línea de comandos

Si has compilado Capstone con herramientas CLI, puedes utilizar `cstool` para desensamblar instrucciones:

```
cstool x64 "55 48 8B 05 B8 13 00 00"
```

Salida esperada:

```
 0  55                             push    rbp
 1  48 8b 05 b8 13 00 00           mov     rax, qword ptr [rip + 0x13b8]
```

## Documentación Oficial

Para más información, visita la documentación oficial de Capstone:

- [Sitio Web](http://www.capstone-engine.org/)
    
- [Repositorio en GitHub](https://github.com/aquynh/capstone)