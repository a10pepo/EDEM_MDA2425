# Desarrollar un script en Bash

## Descripción

En este ejercicio vamos a desarrollar un script en Bash que nos permita realizar una serie de tareas de forma automática. Para ello, vamos a utilizar los conocimientos adquiridos en el módulo de Linux. Para realizar este ejercicio separaremos la forma de probar dichos ejercicios en dos grupos de alumnos (Mac y Windows). 
Antes de empezar recordemos las bases del ejercicio:

1) Las carpetas deben crearse en la carpeta de Usuario de cada alumno dentro de linux (Nota: Directorio de Trabajo)
2) El script debe ser capaz de crear las carpetas y los archivos necesarios para realizar las tareas sin intervención del usuario más allá de su ejecución
3) El script debe ser reejecutable sin necesidad de modificarlo, por lo que debe borrar al inicio lo creado en la ejecución anterior
4) El script debe mostrar una leyenda al inicio de cada tarea indicando que tarea se va a realizar (Nota: echo)

### Comunes

Abre tu Visual Studio y crea un nuevo archivo llamado `script.sh`. En este archivo vamos a desarrollar el script que nos permita realizar las tareas a automatizar.  
Recuerda que el script debe tener siempre la siguiente primera línea:

```bash
#!/bin/bash
```


### Mac

Si ya has generado el script toca probarlo, en el caso de Mac debemos ir a la terminal de Visual Studio y ejecutar el siguiente comando:

```bash
./script.sh
```
En caso de recibir un error de permisos, debemos darle permisos de ejecución al script. Para ello, ejecutaremos el siguiente comando:

```bash
chmod 777 script.sh
```
Una vez ejecutado el script deberemos poder listar los contenidos de las carpetas creadas en el ejercicio y validar que el resultado es correcto. Si es así FEICIDADES, has terminado el ejercicio.


### Windows

Si ya has generado el script toca probarlo, en el caso de Windows como ya hemos comentado en clase debido a la virtualización que usa no podemos ejecutar un script de Linux. Para solucionarlo realizaremos los siguientes pasos:

1) Dentro de la terminal de Visual Studio Code, ejecutaremos el siguiente comando:

```bash
docker create -it --name unix ubuntu:latest
docker start unix
docker exec -it unix /bin/bash
apt update
apt install vim
```

2) Una vez ejecutados nos aseguraremos que estamos dentro del contenedor, nuestro prompt debe ser algo similar a:

```bash
root@f0b3c2c3f0b3:/#
```

3) Una vez abierto, abriremos la terminal y ejecutaremos los siguientes comandos:

```bash
vi script.sh
```

4) Una vez dentro de Vi pulsaremos lo siguiente para entrar en modo edición:

```bash
a
```
Y se activará el modo edición:

**-- INSERT --**

5) Ahora copiaremos el contenido del script que hemos generado en Visual Studio Code y lo pegaremos en la terminal de Vi usando el botón derecho del ratón. Una vez pegado, pulsaremos la tecla `ESC` y escribiremos `:wq` para guardar y salir del editor.

6) Una vez guardado el script, ejecutaremos el siguiente comando para darle permisos de ejecución:

```bash
chmod 777 script.sh
```

7) Una vez ejecutado el script deberemos poder listar los contenidos de las carpetas creadas en el ejercicio y validar que el resultado es correcto. Si es así FEICIDADES, has terminado el ejercicio. Si no es así, puedes ejecutar el siguiente commando que borrará el script y volver al punto 3:

```bash
rm script.sh
```

