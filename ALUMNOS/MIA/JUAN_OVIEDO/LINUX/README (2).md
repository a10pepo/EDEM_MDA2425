# Linux_Comandos

Para entregar este ejercicio, debes copiar este archivo en tu carpeta de alumno y completar las respuestas a las preguntas que se formulan en el mismo.
Una vez completado, debes subirlo a vuestro repositorio remoto de GitHub y realizar una Pull Request poniendo a Pedro Nieto como reviewer.


Ejercicio de comandos en la consola de linux.

  1.Listar todos los archivos del directorio bin.
  
  root@ecf8066e33e2:/# ls ./bin
     
    
  2.Listar todos los archivos del directorio tmp.
  
  root@ecf8066e33e2:/# ls -l ./tmp
  total 4
  drwxr-xr-x 2 root root 4096 Oct  4 19:44 hsperfdata_root
    
    
  3.Listar todos los archivos del directorio etc que empiecen por t 
    
  root@ecf8066e33e2:/# ls /etc/t*
  /etc/timezone
   /etc/terminfo:
  README
  /etc/tmpfiles.d:
  
  4.Listar todos los archivos del directorio dev que empiecen por tty.
    
    root@ecf8066e33e2:/# ls /dev/tty*
    /dev/tty
    
  5.Listar todos los archivos del directorio dev que empiecen por tty y acaben en 3.
    
    root@ecf8066e33e2:/# ls /dev/tty*3
    ls: cannot access '/dev/tty*3': No such file or directory
    
  6.Listar todos los archivos del directorio dev que empiecen por t y acaben en C1.
    
    root@ecf8066e33e2:/# ls /dev/t*C1
    ls: cannot access '/dev/t*C1': No such file or directory

  7.Listar todos los archivos, incluidos los ocultos, del directorio raíz.
    
    root@ecf8066e33e2:/# ls -la ./
    total 112
    root@ecf8066e33e2:/# ls -a . 
# Aqui me han surgido dudas y he puesto los dos.. 

  8.Listar todos los archivos del directorio etc que no empiecen por t.
    
    root@ecf8066e33e2:/# ls -d /etc/[^t]*

  9.Listar todos los archivos del directorio usr y sus subdirectorios.
    
    root@ecf8066e33e2:/# ls /usr *

  10.Cambiarse al directorio tmp, crear directorio PRUEBA.
    
    root@ecf8066e33e2:/# cd tmp
    root@ecf8066e33e2:/tmp# mkdir prueba

  11.Verificar que el directorio actual ha cambiado.
    
    root@ecf8066e33e2:/tmp# ls /tmp

  12.Mostrar el día y la hora actual.
    
    root@ecf8066e33e2:/# date
    Fri Oct  4 21:15:50 CEST 2024

  13.Con un solo comando posicionarse en el directorio $HOME.
    
    root@ecf8066e33e2:/# cd /home
 
  14.Verificar que se está en él.
    
    root@ecf8066e33e2:/home# ls
    ubuntu

  15.Listar todos los ficheros del directorio HOME mostrando sus permisos.
    
    root@ecf8066e33e2:/home# ls -l
    total 4
    drwxr-x--- 2 ubuntu ubuntu 4096 Aug 27 16:06 ubuntu

  16.Borrar todos los archivos y directorios visibles de vuestro directorio PRUEBA.
    
    root@ecf8066e33e2:/# rm /prueba*
    bash: /usr/bin/rm: cannot execute: required file not found

  17.Crear los directorios dir1, dir2 y dir3 en el directorio PRUEBA. Dentro de dir1 crear el directorio dir11. Dentro del directorio 
  dir3 crear el directorio dir31. Dentro del directorio dir31, crear los directorios dir311 y dir312.
    
    root@b5c69abf16cd:/# mkdir PRUEBA
    root@b5c69abf16cd:/# mkdir PRUEBA/dir1
    root@b5c69abf16cd:/# mkdir PRUEBA/dir1/dir11
    root@b5c69abf16cd:/# mkdir PRUEBA/dir2
    root@b5c69abf16cd:/# mkdir PRUEBA/dir3
    root@b5c69abf16cd:/# mkdir PRUEBA/dir3/dir31
    root@b5c69abf16cd:/# mkdir PRUEBA/dir3/dir31/dir311
    root@b5c69abf16cd:/# mkdir PRUEBA/dir3/dir31/dir312
    
  18.Copiar el archivo /etc/motd a un archivo llamado mensaje de vuestro directorio PRUEBA.
    
    touch PRUEBA/mensaje
    touch /etc/motd >> /PRUEBA/mensaje

  19.Copiar mensaje en dir1, dir2 y dir3.
    
    root@b5c69abf16cd:/# cd PRUEBA
    root@b5c69abf16cd:/PRUEBA# cp mensaje dir1/mensaje
    root@b5c69abf16cd:/PRUEBA# cp mensaje dir2/mensaje
    root@b5c69abf16cd:/PRUEBA# cp mensaje dir3/mensaje
    
  20.Comprobar el ejercicio anterior mediante un solo comando.
    
root@b5c69abf16cd:/# ls -R PRUEBA
PRUEBA:
dir1  dir2  dir3  mensaje

PRUEBA/dir1:
dir11  mensaje

PRUEBA/dir1/dir11:

PRUEBA/dir2:
mensaje

PRUEBA/dir3:
dir31  mensaje

PRUEBA/dir3/dir31:
dir311  dir312

PRUEBA/dir3/dir31/dir311:

PRUEBA/dir3/dir31/dir312:
    
   
