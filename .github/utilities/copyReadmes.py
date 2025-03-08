#!/usr/bin/env python3

import os
import sys
import shutil

def main():
    # Validar parámetros de entrada
    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} <ruta_entrada> <ruta_salida>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    # Verificar directorio de entrada
    if not os.path.isdir(input_dir):
        print(f"Error: El directorio '{input_dir}' no existe")
        sys.exit(1)

    # Crear directorio de salida
    os.makedirs(output_dir, exist_ok=True)

    # Procesar archivos recursivamente
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(".markdown"):
                # Obtener nombre de la carpeta contenedora
                parent_folder = os.path.basename(root)
                # Nuevo nombre en mayúsculas
                new_filename = f"{parent_folder.upper()}.markdown"
                # Ruta completa de origen y destino
                source_path = os.path.join(root, file)
                dest_path = os.path.join(output_dir, new_filename)
                # Copiar archivo
                shutil.copy(source_path, dest_path)

    print(f"Archivos copiados a '{output_dir}' con nombres basados en sus carpetas.")

if __name__ == "__main__":
    main()