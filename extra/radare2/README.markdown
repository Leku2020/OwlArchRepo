
# Radare2 - Análisis y Reversing de Binarios

Radare2 (r2) es un conjunto de herramientas de código abierto para analizar, depurar, desensamblar y manipular binarios. Es ampliamente utilizado en la ingeniería inversa y seguridad informática.

## Instalación

```
sudo pacman -S radare2
```


## Uso Básico

### Análisis de un binario

```
r2 /bin/ls
```

### Comandos Principales

Dentro de radare2, puedes usar los siguientes comandos:

|Comando|Descripción|
|---|---|
|`?`|Mostrar ayuda|
|`aaa`|Analizar completamente el binario|
|`afl`|Listar funciones encontradas|
|`pdf @ main`|Mostrar el pseudocódigo de la función `main`|
|`s main`|Saltar a la función `main`|
|`i`|Mostrar información del binario|

## Ejemplos de Uso

### Desensamblar la función `main`

```
r2 -A /bin/ls  # -A ejecuta un análisis automático
pdf @ main      # Mostrar el código ensamblador de main
```

### Buscar cadenas de texto dentro del binario

```
izz
```

### Depurar un ejecutable con radare2

```
r2 -d /bin/ls
```

Dentro de radare2:

```
 db main  # Poner un breakpoint en main
 dc       # Ejecutar hasta el breakpoint
 dr       # Mostrar registros
 px 32 @ esp  # Mostrar 32 bytes de la pila
```

## Recursos

- Documentación oficial
    
- [Repositorio GitHub](https://github.com/radareorg/radare2)