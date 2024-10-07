# Linux_Comandos

Para entregar este ejercicio, debes copiar este archivo en tu carpeta de alumno y completar las respuestas a las preguntas que se formulan en el mismo.
Una vez completado, debes subirlo a vuestro repositorio remoto de GitHub y realizar una Pull Request poniendo a Pedro Nieto como reviewer.


Ejercicio de comandos en la consola de linux.

  1.Listar todos los archivos del directorio bin.
    
    1. ls bin 
    
  2.Listar todos los archivos del directorio tmp.
   
    2. ls tmp (No lo lee, está vacío o algo)
    
  3.Listar todos los archivos del directorio etc que empiecen por t 
    
    3. ls /etc/t* (Para que te diga solamente las carpetas o archivos que empiecen por t hay que poner:  ls -d /etc/t*)
  
  4.Listar todos los archivos del directorio dev que empiecen por tty.
    
    4. ls /etc/tty*
    
  5.Listar todos los archivos del directorio dev que empiecen por tty y acaben en 3.
    
    5. ls /dev/tty*3 (obviamente no encuentra ningún archivo)
    
  6.Listar todos los archivos del directorio dev que empiecen por t y acaben en C1.
    
    6. ls /dev/t*C1

  7.Listar todos los archivos, incluidos los ocultos, del directorio raíz.
    
    7. ls -a / (-a muestra todos los archivos visibles + ocultos)
    
  8.Listar todos los archivos del directorio etc que no empiecen por t.
    
    8. ls /etc/[^t]* (lo he probado metiendo "!" en todos los sitios posibles y no funcionaba, y al final era con otra sintaxis.)

  9.Listar todos los archivos del directorio usr y sus subdirectorios.
    
    9. ls -R /usr (-R activa el modo recursivo = recorrer todos los directorios dentro de /usr)

  10.Cambiarse al directorio tmp, crear directorio PRUEBA.
    
    10. cd tmp ; mkdir PRUEBA  (; = salto de línea)

  11.Verificar que el directorio actual ha cambiado.
    
    11. ls tmp (debe salir PRUEBA)

  12.Mostrar el día y la hora actual.
    
    12. date

  13.Con un solo comando posicionarse en el directorio $HOME.
    
    13. cd $HOME <- te vas a tu directorio personal (~) || cd /$HOME <- te vas al root
 
  14.Verificar que se está en él.
    
    14. pwd (print working directory = ruta completa del directorio actual)

  15.Listar todos los ficheros del directorio HOME mostrando sus permisos.
    
    15. ls -l ~ (total  = 0 == ¿no hay ficheros?)

  16.Borrar todos los archivos y directorios visibles de vuestro directorio PRUEBA.
    
    16. rm -r /tmp/PRUEBA/* (con -r borramos recursivamente y con el "*" especificamos todos los archivos y directorios dentro de la carpeta que sean visibles) (rm -rf /tmp/PRUEBA <- elimina también la carpeta PRUEBA)

  17.Crear los directorios dir1, dir2 y dir3 en el directorio PRUEBA. Dentro de dir1 crear el directorio dir11. Dentro del directorio 
  dir3 crear el directorio dir31. Dentro del directorio dir31, crear los directorios dir311 y dir312.
    
    17. mkdir -p /tmp/PRUEBA/dir1/dir11 ; mkdir /tmp/PRUEBA/dir2 ; mkdir -p /tmp/PRUEBA/dir3/dir31/dir331 ; mkdir /tmp/PRUEBA/dir3/dir31/dir332 (-p para crear directorios de manera recursiva)
    
  18.Copiar el archivo /etc/motd a un archivo llamado mensaje de vuestro directorio PRUEBA.
    
    18. cp /etc/legal /tmp/PRUEBA/mensaje (como no existe motd voy a usar el archivo "legal")

  19.Copiar mensaje en dir1, dir2 y dir3.
    
    19. cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir1 ; cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir2 ; cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir3
    
  20.Comprobar el ejercicio anterior mediante un solo comando.

    20. ls /tmp/PRUEBA/dir1/mensaje /tmp/PRUEBA/dir2/mensaje /tmp/PRUEBA/dir3/mensaje

    
   
