# Linux_Comandos

Para entregar este ejercicio, debes copiar este archivo en tu carpeta de alumno y completar las respuestas a las preguntas que se formulan en el mismo.
Una vez completado, debes subirlo a vuestro repositorio remoto de GitHub y realizar una Pull Request poniendo a Pedro Nieto como reviewer.


Ejercicio de comandos en la consola de linux.

  1.Listar todos los archivos del directorio bin.
    
    1. ls bin
  
  2.Listar todos los archivos del directorio tmp.
   
    2. ls tmp (no se muestra nada al realizar esta acción)
    
  3.Listar todos los archivos del directorio etc que empiecen por t 
    
    3. ls etc/t* (al realizar dicha accion muestra README que es el fichero que se encuentra dentro del directorio terminfo)
  
  4.Listar todos los archivos del directorio dev que empiecen por tty.
    
    4. ls dev/tty*
    
  5.Listar todos los archivos del directorio dev que empiecen por tty y acaben en 3.
    
    5. ls dev/tty*3 (no encuentra ningun directorio ni fichero con estas especificaciones)
    
  6.Listar todos los archivos del directorio dev que empiecen por t y acaben en C1.
    
    6. ls dev/t*C1 (al igual que antes, no muestra nada)

  7.Listar todos los archivos, incluidos los ocultos, del directorio raíz.
    
    7. ls -a / 
    
  8.Listar todos los archivos del directorio etc que no empiecen por t.
    
    8. finde etc/ -not -name t*
    8. ls etc/[^t]* 
    (he encontrado que estos dos metodos muestran lo mismo aunque de diferente modo en la terminal)  

  9.Listar todos los archivos del directorio usr y sus subdirectorios.
    
    9. ls -R /usr

  10.Cambiarse al directorio tmp, crear directorio PRUEBA.
    
    10. cd tmp; mkdir /tmp/PRUEBA; cd..

  11.Verificar que el directorio actual ha cambiado.
    
    11. ls /tmp

  12.Mostrar el día y la hora actual.
    
    12. date

  13.Con un solo comando posicionarse en el directorio $HOME.
    
    13. cd $HOME
 
  14.Verificar que se está en él.
    
    14. pwd

  15.Listar todos los ficheros del directorio HOME mostrando sus permisos.
    
    15. ls -l ~/

  16.Borrar todos los archivos y directorios visibles de vuestro directorio PRUEBA.
    
    16. rm -r /tmp/PRUEBA; ls /tmp (de esta formna comprobamos que se ha borrado definitivamente ya que no debería salir nada en la terminal)

  17.Crear los directorios dir1, dir2 y dir3 en el directorio PRUEBA. Dentro de dir1 crear el directorio dir11. Dentro del directorio 
  dir3 crear el directorio dir31. Dentro del directorio dir31, crear los directorios dir311 y dir312.
    
    17. mkdir tmp/PRUEBA; mkdir /tmp/PRUEBA/dir1;  mkdir /tmp/PRUEBA/dir1/dir11; mkdir /tmp/PRUEBA/dir2; mkdir /tmp/PRUEBA/dir3; mkdir /tmp/PRUEBA/dir3/dir31;  mkdir /tmp/PRUEBA/dir3/dir31/dir311; mkdir /tmp/PRUEBA/dir3/dir31/dir312
    
  18.Copiar el archivo /etc/motd a un archivo llamado mensaje de vuestro directorio PRUEBA.
    
    18. cp /etc/networks /tmp/PRUEBA/mensajes (como no existe motd lo he realizado con el archivo networks)

  19.Copiar mensaje en dir1, dir2 y dir3.
    
    19. cp tmp/PRUEBA/mensajes tmp/PRUEBA/dir1; cp tmp/PRUEBA/mensajes tmp/PRUEBA/dir2; cp tmp/PRUEBA/mensajes tmp/PRUEBA/dir3
    
  20.Comprobar el ejercicio anterior mediante un solo comando.
    
    20. ls tmp/PRUEBA/dir1; ls tmp/PRUEBA/dir2; ls tmp/PRUEBA/dir3

    
   