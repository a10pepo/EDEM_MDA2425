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

echo 13.Con un solo comando posicionarse en el directorio $HOME.






