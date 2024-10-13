# Linux_Comandos

Para entregar este ejercicio, debes copiar este archivo en tu carpeta de alumno y completar las respuestas a las preguntas que se formulan en el mismo.
Una vez completado, debes subirlo a vuestro repositorio remoto de GitHub y realizar una Pull Request poniendo a Pedro Nieto como reviewer.


Ejercicio de comandos en la consola de linux.

  1.Listar todos los archivos del directorio bin.

cd bin
ls

    
  2.Listar todos los archivos del directorio tmp.

cd tmp
ls -l

  3.Listar todos los archivos del directorio etc que empiecen por t 
cd etc 
ls -l | grep t*

 
  4.Listar todos los archivos del directorio dev que empiecen por tty. (Si listo con el ls - l me lista otro archivo que contiene tty pero no en el nombre por eso uso ls )
cd dev
ls | grep tty*


  5.Listar todos los archivos del directorio dev que empiecen por tty y acaben en 3 (No me aparece ninguno)
cd dev
ls

console  core  fd  full  mqueue  null  ptmx  pts  random  shm  stderr  stdin  stdout  tty  urandom  zero

ls -l | grep tty*3


  6.Listar todos los archivos del directorio dev que empiecen por t y acaben en C1.
cd dev
ls -l | grep t*c1


  7.Listar todos los archivos, incluidos los ocultos, del directorio raíz.
cd /
ls -la
    
    
  8.Listar todos los archivos del directorio etc que no empiecen por t.

ls -l /etc/[^t]*


  9.Listar todos los archivos del directorio usr y sus subdirectorios.

 ls -R /usr
    

  10.Cambiarse al directorio tmp, crear directorio PRUEBA.

cd /tmp
mkdir PRUEBA
    

  11.Verificar que el directorio actual ha cambiado.

ls /tmp
    

  12.Mostrar el día y la hora actual.

date
    

  13.Con un solo comando posicionarse en el directorio $HOME.
  
cd /home
    
 
  14.Verificar que se está en él.
    
pwd

  15.Listar todos los ficheros del directorio HOME mostrando sus permisos.
    
ls- /home

  16.Borrar todos los archivos y directorios visibles de vuestro directorio PRUEBA.
    
rm -r /PRUEBA/*

  17.Crear los directorios dir1, dir2 y dir3 en el directorio PRUEBA. Dentro de dir1 crear el directorio dir11. Dentro del directorio 
  dir3 crear el directorio dir31. Dentro del directorio dir31, crear los directorios dir311 y dir312.
    
cd /PRUEBA
mkdir -p dir1/dir11 dir2 dir3/dir31/dir311 dir3/dir31/dir312


    
  18.Copiar el archivo /etc/motd a un archivo llamado mensaje de vuestro directorio PRUEBA.
    
cp /etc/motd /PRUEBA/mensaje

  19.Copiar mensaje en dir1, dir2 y dir3.

cp /PRUEBA/mensaje /PRUEBA/dir1/mensaje
cp /PRUEBA/mensaje /PRUEBA/dir2/mensaje
cp /PRUEBA/mensaje /PRUEBA/dir3/mensaje
    
  20.Comprobar el ejercicio anterior mediante un solo comando.
    
ls -R /PRUEBA
    
   
