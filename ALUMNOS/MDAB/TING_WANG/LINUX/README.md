# Linux_Comandos

Para entregar este ejercicio, debes copiar este archivo en tu carpeta de alumno y completar las respuestas a las preguntas que se formulan en el mismo.
Una vez completado, debes subirlo a vuestro repositorio remoto de GitHub y realizar una Pull Request poniendo a Pedro Nieto como reviewer.


Ejercicio de comandos en la consola de linux.

  1.Listar todos los archivos del directorio bin.
    
     ls -l ./bin
    
  2.Listar todos los archivos del directorio tmp.
   
    ls -l ./tmp
    
  3.Listar todos los archivos del directorio etc que empiecen por t 
    
    ls /etc/t*
  
  4.Listar todos los archivos del directorio dev que empiecen por tty.
    
    ls -l /dev/tty*
    
  5.Listar todos los archivos del directorio dev que empiecen por tty y acaben en 3.
    
    ls -l /dev/tty*3
    
  6.Listar todos los archivos del directorio dev que empiecen por t y acaben en C1.
    
    ls -l /dev/tty*C1

  7.Listar todos los archivos, incluidos los ocultos, del directorio raíz.
    
    ls -al /
    
  8.Listar todos los archivos del directorio etc que no empiecen por t.
    
    ls /etc/[!t]*

  9.Listar todos los archivos del directorio usr y sus subdirectorios.
    
    ls -lR /usr

  10.Cambiarse al directorio tmp, crear directorio PRUEBA.
    
    cd /tmp
    mkdir PRUEBA

  11.Verificar que el directorio actual ha cambiado.
    
    pwd

  12.Mostrar el día y la hora actual.
    
    date

  13.Con un solo comando posicionarse en el directorio $HOME.
    
    cd ~
 
  14.Verificar que se está en él.
    
    pwd

  15.Listar todos los ficheros del directorio HOME mostrando sus permisos.
    
    ls -l ~


  16.Borrar todos los archivos y directorios visibles de vuestro directorio PRUEBA.
    
    rm -rf /tmp/PRUEBA/*

  17.Crear los directorios dir1, dir2 y dir3 en el directorio PRUEBA. Dentro de dir1 crear el directorio dir11. Dentro del directorio 
  dir3 crear el directorio dir31. Dentro del directorio dir31, crear los directorios dir311 y dir312.
    
    mkdir /tmp/PRUEBA/dir1 /tmp/PRUEBA/dir2 /tmp/PRUEBA/dir3
    mkdir /tmp/PRUEBA/dir1/dir11
    mkdir /tmp/PRUEBA/dir3/dir31
    mkdir /tmp/PRUEBA/dir3/dir31/dir311 /tmp/PRUEBA/dir3/dir31/dir312
    
  18.Copiar el archivo /etc/motd a un archivo llamado mensaje de vuestro directorio PRUEBA.
    
    No existe motd ? Es mtab?
    cp /etc/mtab /tmp/PRUEBA/mensaje

  19.Copiar mensaje en dir1, dir2 y dir3.
    
    cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir1 
    cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir2 
    cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir3

    ## Cómo se puede hacer a la vez? 
    
  20.Comprobar el ejercicio anterior mediante un solo comando.
    
    ls /tmp/PRUEBA/*
    
   
