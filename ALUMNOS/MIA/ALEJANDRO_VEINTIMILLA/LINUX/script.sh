#!/bin/bash

echo 1.Listar todos los archivos del directorio bin.

ls /bin

echo 2.Listar todos los archivos del directorio tmp.

ls  /tmp

echo 3.Listar todos los archivos del directorio etc que empiecen por t

cd /etc
ls  t*

echo 4.Listar todos los archivos del directorio dev que empiecen por tty.

cd /dev
ls  tty*

echo 5.Listar todos los archivos del directorio dev que empiecen por tty y acaben en 3.

ls  tty*3

echo 6.Listar todos los archivos del directorio dev que empiecen por t y acaben en C1.

ls t*C1

echo 7.Listar todos los archivos, incluidos los ocultos, del directorio raíz.

cd /
ls -a

echo 8.Listar todos los archivos del directorio etc que no empiecen por t.

ls /etc | grep -v "^t"

echo 9.Listar todos los archivos del directorio usr y sus subdirectorios.

ls -R /usr

echo 10.Cambiarse al directorio tmp, crear directorio PRUEBA.

cd /tmp
mkdir PRUEBA

echo 11.Verificar que el directorio actual ha cambiado.

ls

echo 12.Mostrar el día y la hora actual.

date

echo 13.Con un solo comando posicionarse en el directorio HOME.

cd $HOME

echo 14.Verificar que se está en él.

echo $PATH

echo 15.Listar todos los ficheros del directorio HOME mostrando sus permisos.

ls -l

echo 16.Borrar todos los archivos y directorios visibles de vuestro directorio PRUEBA.

rm -r PRUEBA

echo 17.Crear los directorios dir1, dir2 y dir3 en el directorio PRUEBA. Dentro de dir1 crear el directorio dir11. Dentro del directorio dir3 crear el directorio dir31. Dentro del directorio dir31, crear los directorios dir311 y dir312.

mkdir PRUEBA
cd PRUEBA
mkdir dir1 dir2 dir3
cd dir1
mkdir dir11
cd ..
cd dir3
mkdir dir31
cd dir31
mkdir dir311 dir312

echo 18.Copiar el archivo /etc/mtab a un archivo llamado mensaje de vuestro directorio PRUEBA.

cd ..
cd ..
cp /etc/mtab ~/PRUEBA
mv mtab mensaje 
cp mensaje ~/PRUEBA/dir1 
cp mensaje ~/PRUEBA/dir2
cp mensaje ~/PRUEBA/dir3 

echo 20.Comprobar el ejercicio anterior mediante un solo comando.

ls -lR