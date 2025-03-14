#!/bin/bash

rm -R /OwlArchRepo
cp -R /home/osArch/Desktop/owlArch/OwlArchRepo /
docker run --rm -v /OwlArchRepo:/workspace:z archlinux:latest /bin/bash -c "
	    echo 'Base:'
	    ls -R .
	    echo 'Workspace:'
	    ls -l /workspace
            useradd -m builder && echo 'builder:password' | chpasswd && \
            pacman -Sy --noconfirm sudo base-devel && \
            echo 'builder ALL=(ALL) NOPASSWD: /usr/bin/pacman' >> /etc/sudoers && \
            chown -R builder:builder /workspace && \
	    su - builder -c '
              find /workspace -type f -name PKGBUILD | while read PKGBUILD; do
                dir=\$(dirname \$PKGBUILD)
                echo \"Building package in \$dir\"
                cd \$dir && makepkg -si --noconfirm && cd -
              done
            '"


mkdir -p "/OwlArchRepo/pkgs/x86_64"
find find /OwlArchRepo -type f -name "*.pkg.tar.zst" | while read file; do
	echo "Copying: $file to /OwlArchRepo/pkgs/x86_64/"
	cp "$file" "/OwlArchRepo/pkgs/x86_64/"
done

docker run --rm -v /OwlArchRepo:/workspace:z -w /workspace archlinux:latest /bin/bash -c '
            pacman -Sy --noconfirm pacman-contrib && \
            echo "Pacman actualizado" && \
            
            # Eliminar la base de datos existente si existe
            rm -f /workspace/pkgs/x86_64/OwlArchRepo.db.tar.gz && \
            echo "Archivo de base de datos eliminado" && \
            
            # Crear la base de datos desde cero
            repo-add /workspace/pkgs/x86_64/OwlArchRepo.db.tar.gz && \
            echo "Base de datos creada" && \
            
            # Añadir los paquetes válidos a la base de datos
            cd /workspace/pkgs/x86_64 && \
            echo "Cambiando a directorio /workspace/pkgs/x86_64" && \
            
            find . -type f -name "*.pkg.tar.zst" | while read pkg; do \
              echo "Procesando: $pkg"; \
              
              # Verificar si el paquete es válido
              if tar -I zstd -tf "$pkg" &> /dev/null; then \
                echo "Paquete válido: $pkg"; \
                repo-add /workspace/pkgs/x86_64/OwlArchRepo.db.tar.gz "$pkg" && \
                echo "Paquete añadido: $pkg"; \
              else \
                echo "Saltando paquete inválido: $pkg"; \
              fi \
            done'
