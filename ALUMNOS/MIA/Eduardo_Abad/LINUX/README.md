# Linux_Comandos

Para entregar este ejercicio, debes copiar este archivo en tu carpeta de alumno y completar las respuestas a las preguntas que se formulan en el mismo.
Una vez completado, debes subirlo a vuestro repositorio remoto de GitHub y realizar una Pull Request poniendo a Pedro Nieto como reviewer.


Ejercicio de comandos en la consola de linux.

  1.Listar todos los archivos del directorio bin.
    
  root@76e0c2c4ed1d:~# ls /bin   
    
  2.Listar todos los archivos del directorio tmp.
   
  root@76e0c2c4ed1d:~# ls /tmp 
    
  3.Listar todos los archivos del directorio etc que empiecen por t 
    
  root@76e0c2c4ed1d:/etc# ls t* 
  
  4.Listar todos los archivos del directorio dev que empiecen por tty.
    
  root@76e0c2c4ed1d:/dev# ls tty*  
    
  5.Listar todos los archivos del directorio dev que empiecen por tty y acaben en 3.
    
  root@76e0c2c4ed1d:~# ls /dev/tty*3 
    
  6.Listar todos los archivos del directorio dev que empiecen por t y acaben en C1.
    
  rroot@76e0c2c4ed1d:~# ls /dev/t*C1 

  7.Listar todos los archivos, incluidos los ocultos, del directorio raíz.
    
  root@76e0c2c4ed1d:/# ls -al 
    
  8.Listar todos los archivos del directorio etc que no empiecen por t.
    
  root@76e0c2c4ed1d:/etc# ls --ignore=t*  

  9.Listar todos los archivos del directorio usr y sus subdirectorios.
    
  root@76e0c2c4ed1d:/usr# ls -R 

  10.Cambiarse al directorio tmp, crear directorio PRUEBA.
    
  root@76e0c2c4ed1d:/tmp# mkdir PRUEBA 

  11.Verificar que el directorio actual ha cambiado.
    
  root@76e0c2c4ed1d:/tmp# ls  

  12.Mostrar el día y la hora actual.
    
  root@76e0c2c4ed1d:/# date  

  13.Con un solo comando posicionarse en el directorio $HOME.
    
  root@76e0c2c4ed1d:/tmp# cd $HOME  
 
  14.Verificar que se está en él.
    
  root@76e0c2c4ed1d:/home# pwd 

  15.Listar todos los ficheros del directorio HOME mostrando sus permisos.
    
  root@76e0c2c4ed1d:/home# ls -l  

  16.Borrar todos los archivos y directorios visibles de vuestro directorio PRUEBA.
    
  root@76e0c2c4ed1d:/tmp# rm -r PRUEBA  

  17.Crear los directorios dir1, dir2 y dir3 en el directorio PRUEBA. Dentro de dir1 crear el directorio dir11. Dentro del directorio 
  dir3 crear el directorio dir31. Dentro del directorio dir31, crear los directorios dir311 y dir312.
  root@76e0c2c4ed1d:/tmp# cd PRUEBA
  root@76e0c2c4ed1d:/tmp/PRUEBA# mkdir dir1
  root@76e0c2c4ed1d:/tmp/PRUEBA# mkdir dir2
  root@76e0c2c4ed1d:/tmp/PRUEBA# mkdir dir3
  root@76e0c2c4ed1d:/tmp/PRUEBA# cd dir3
  root@76e0c2c4ed1d:/tmp/PRUEBA/dir3# mkdir dir31
  root@76e0c2c4ed1d:/tmp/PRUEBA/dir3# cd dir31
  root@76e0c2c4ed1d:/tmp/PRUEBA/dir3/dir31# mkdir dir311
  root@76e0c2c4ed1d:/tmp/PRUEBA/dir3/dir31# mkdir dir312  
    
    
  18.Copiar el archivo /etc/motd a un archivo llamado mensaje de vuestro directorio PRUEBA.
    
  root@76e0c2c4ed1d:/# find / -name motd #He buscado con este comando donde estaba ese documento ya que con esa ruta no lo encontraba
  /usr/share/motd
  /usr/share/base-files/motd
  /etc# cp /usr/share/base-files/motd /tmp/PRUEBA/mensaje
    

  19.Copiar mensaje en dir1, dir2 y dir3.
  
  root@76e0c2c4ed1d:/etc# cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir1
  root@76e0c2c4ed1d:/etc# cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir2
  root@76e0c2c4ed1d:/etc# cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir3
  
    
    
  20.Comprobar el ejercicio anterior mediante un solo comando.
  root@76e0c2c4ed1d:/tmp/PRUEBA# ls -R
  

    
   
