# Linux_Comandos

Para entregar este ejercicio, debes copiar este archivo en tu carpeta de alumno y completar las respuestas a las preguntas que se formulan en el mismo.
Una vez completado, debes subirlo a vuestro repositorio remoto de GitHub y realizar una Pull Request poniendo a Pedro Nieto como reviewer.


Ejercicio de comandos en la consola de linux.

1. Listar todos los archivos del directorio bin.
    
    ```bash
    ls /bin
    ```

2. Listar todos los archivos del directorio tmp.
    
    ```bash
    ls /tmp
    ```

3. Listar todos los archivos del directorio etc que empiecen por t 
    
    ```bash
    ls /etc/t*
    ```

4. Listar todos los archivos del directorio dev que empiecen por tty.
    
    ```bash
    ls /dev/tty*
    ```
    
5. Listar todos los archivos del directorio dev que empiecen por tty y acaben en 3.
    
    ```bash
    ls /dev/tty*3
    ```
 
6. Listar todos los archivos del directorio dev que empiecen por t y acaben en C1.
    
    ```bash
    ls /dev/t*C1
    ```

7. Listar todos los archivos, incluidos los ocultos, del directorio raíz.
    
    ```bash
    ls -a /
    ```

8. Listar todos los archivos del directorio etc que no empiecen por t.
    
    ```bash
    ls /etc | grep -v '^t'
    ```

9. Listar todos los archivos del directorio usr y sus subdirectorios.
    
    ```bash
    ls -R /usr
    ```

10. Cambiarse al directorio tmp, crear directorio PRUEBA.
    
    ```bash
    cd /tmp
    mkdir PRUEBA
    ```

11. Verificar que el directorio actual ha cambiado.
    
    ```bash
    pwd
    ```

12. Mostrar el día y la hora actual.
    
    ```bash
    date
    ```

13. Con un solo comando posicionarse en el directorio $HOME.
    
    ```bash
    cd ~
    ```

14. Verificar que se está en él.
    
    ```bash
    pwd
    ```

15. Listar todos los ficheros del directorio HOME mostrando sus permisos.
    
    ```bash
    ls -l ~
    ```

16. Borrar todos los archivos y directorios visibles de vuestro directorio PRUEBA.
    
    ```bash
    rm -rf /tmp/PRUEBA/*
    ```

17. Crear los directorios dir1, dir2 y dir3 en el directorio PRUEBA. Dentro de dir1 crear el directorio dir11. Dentro del directorio dir3 crear el directorio dir31. Dentro del directorio dir31, crear los directorios dir311 y dir312.
    
    ```bash
    cd /tmp/PRUEBA
    mkdir dir1
    mkdir dir1/dir11
    mkdir dir2
    mkdir dir3
    mkdir dir3/dir31
    mkdir dir3/dir31/dir311
    mkdir dir3/dir31/dir312
    ```
    
18. Copiar el archivo /etc/motd a un archivo llamado mensaje de vuestro directorio PRUEBA.
    
    ```bash
    cp /etc/motd /tmp/PRUEBA/mensaje
    ```

19. Copiar mensaje en dir1, dir2 y dir3.
    
    ```bash
    cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir1/
    cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir2/
    cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir3/
    ```
20. Comprobar el ejercicio anterior mediante un solo comando.
    
    ```bash
    ls -l -R /tmp/PRUEBA/*/mensaje
    ```
