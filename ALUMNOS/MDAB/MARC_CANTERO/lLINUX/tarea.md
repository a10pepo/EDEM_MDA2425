Para entregar este ejercicio, debes copiar este archivo en tu carpeta de alumno y completar las respuestas a las preguntas que se formulan en el mismo. 
Una vez completado, debes subirlo a vuestro repositorio remoto de GitHub y realizar una Pull Request poniendo a Pedro Nieto como reviewer.

Ejercicio de comandos en la consola de linux.

1.Listar todos los archivos del directorio bin.

	ls /bin

2.Listar todos los archivos del directorio tmp.

	ls /tmp

3.Listar todos los archivos del directorio etc que empiecen por t

	cd /etc
	ls -d t*
	(Archivos no hay ninguno, solamente el directorio "terminfo", por eso "-d")

4.Listar todos los archivos del directorio dev que empiecen por tty.

	ls /dev | grep tty*

5.Listar todos los archivos del directorio dev que empiecen por tty y acaben en 3.

	ls /dev | grep tty*3

6.Listar todos los archivos del directorio dev que empiecen por t y acaben en C1.

	ls /dev | grep t*C1

7.Listar todos los archivos, incluidos los ocultos, del directorio raíz.

	ls -a

8.Listar todos los archivos del directorio etc que no empiecen por t.

	ls /etc | grep -v t*
	(-v hace que grep excluya la condicion en vez de buscarla)

9.Listar todos los archivos del directorio usr y sus subdirectorios.

	ls -lr /usr

10.Cambiarse al directorio tmp, crear directorio PRUEBA.

	cd /tmp
	mkdir PRUEBA
	
11.Verificar que el directorio actual ha cambiado.
	
	ls /tmp

12.Mostrar el día y la hora actual.

	date

13.Con un solo comando posicionarse en el directorio $HOME.

	cd /root

14.Verificar que se está en él.

	pdw

15.Listar todos los ficheros del directorio HOME mostrando sus permisos.

	ls -l /home

16.Borrar todos los archivos y directorios visibles de vuestro directorio PRUEBA.

	cd /tmp/PRUEBA
	rm -rf ./*

17.Crear los directorios dir1, dir2 y dir3 en el directorio PRUEBA. Dentro de dir1 crear el directorio dir11. Dentro del directorio dir3 crear el directorio dir31. 
Dentro del directorio dir31, crear los directorios dir311 y dir312.

	cd /tmp/PRUEBA
	mkdir dir1 dir2 dir3
	cd dir1
	mkdir dir11
	cd ..
	cd dir3
	mkdir dir31
	cd dir31
	mkdir dir311 dir312

18.Copiar el archivo /etc/motd a un archivo llamado mensaje de vuestro directorio PRUEBA.

	cp /etc/motd /tmp/PRUEBA/mensaje
	(me da error porque aparentemente no existe ningun archivo llamado "motd" en esa ruta)

19.Copiar mensaje en dir1, dir2 y dir3.

	cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir1/
	cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir2/
	cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir3/

	o con una sola funcion:

	cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir1/ & cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir2/ & cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir3/

20.Comprobar el ejercicio anterior mediante un solo comando.

	find /tmp/PRUEBA/dir{1,2,3} -name mensaje | grep 'dir[1-3]'

	Con esta funcion, find buscara en la ruta nombrada.
	"dir{1,2,3}" hara que busque en las 3 a la vez.
	-name mensaje, buscara un archivo que coincida exactamente con mensaje
	| grep -o cojera exactamente lo que le entre de la funcion find y el -o lo que hace es darte el directorio solamente sin darte la ruta completa
	'dir[1-3]' coincide con los directorios dir1, dir2, dir3 que grep encontrara y mostrará exactamente.
