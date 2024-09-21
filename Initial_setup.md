# Instalación Inicial

En la primera sesión del master se instalan todas las herramientas que usaremos a lo largo del curso. En este documento se recogen los pasos que se han seguido para instalarlas en caso de que alguien necesite repetir el proceso o no haya podido asistir a la sesión.

Durante este tutorial, instalaremos las siguientes herramientas:

- Visual Studio Code y sus plugins
- Git
- GitHub Desktop
- Python
- SSH Keys
- Docker

Adicionalmente para mac instalaremos Homebrew, un gestor de paquetes que nos permitirá instalar software de forma sencilla.


## Pre-requisitos

### Windows
Antes de realizar estas instalaciones, debemos asegurarnos de tener privilegios de administrador y espacio suficiente en el disco duro.

### Mac
Antes de instalar el software instalaremos el gestor de paquetes Homebrew. Para ello, abriremos una terminal y ejecutaremos el siguiente comando:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
 Una vez instalado, debemos incluir en el path de nuestro sistema el directorio donde se instalarán los paquetes. Para ello, ejecutaremos el siguiente comando:

```bash
echo 'PATH="/usr/local/bin:$PATH"' >> ~/.bash_profile
```

una vez hecho esto cerraremos la terminal y la volveremos a abrir para que los cambios surtan efecto.



## Visual Studio Code

### Windows
Para instalar esta herramienta basta con acceder a la web de Microsoft y descargar el instalable correspondiente:

https://code.visualstudio.com/download

### Mac
Para instlar visual studio code en mac, ejecutaremos el siguiente comando en una terminal:

```bash
brew install --cask visual-studio-code
```
una vez instalado podemos ejecutarlo desde la terminal con el siguiente comando:

```bash
code
```

## Visual Studio Plugins
Una vez instalado Visual studio code, accederemos a la pestaña de plugins en el menu lateral izquierdo y buscaremos la opción de plugins representada con unas cajas. Una vez dentro, buscaremos los siguientes plugins y los instalaremos:

- Python
- Docker
- Markdowwn
- Git

Para instalar un plugin solo debéis buscar el texto en el buscador y pulsar el botón de instalar. Una vez instalado, deberéis reiniciar Visual Studio Code para que los cambios surtan efecto.

## Git

### Windows
Para instalar Git en Windows, accederemos a la web de descargas de Git y descargaremos el instalador correspondiente:

https://git-scm.com/download/win

Una vez instalado Git, abriremos una terminal y ejecutaremos el siguiente comando para asegurar que la instalación se ha realizado correctamente:

```bash
git --version
```

### Mac
Para instalar Git en Mac, ejecutaremos el siguiente comando en una terminal:

```bash
brew install git
```

Una vez instalado Git, abriremos una terminal y ejecutaremos el siguiente comando para asegurar que la instalación se ha realizado correctamente:

```bash
git --version
```

## GitHub Desktop
Para instalar GitHub Desktop en Windows o Mac, accederemos a la web de descargas de GitHub Desktop y descargaremos el instalador correspondiente. 

https://desktop.github.com/

## Python
### Windows
Para instalar Python accederemos al marketplace de Microsoft y descargaremos el instalador correspondiente de python 3.10 o superior.
Una vez instalado, abriremos una terminal y ejecutaremos el siguiente comando para asegurar que la instalación se ha realizado correctamente:

```bash
python --version
```

### Mac
Para instalar Python en Mac, ejecutaremos el siguiente comando en una terminal:

```bash
brew update
brew upgrade
brew install python3
```

Una vez instalado, abriremos una terminal y ejecutaremos el siguiente comando para asegurar que la instalación se ha realizado correctamente:

```bash
python3 --version
```

## SSH Keys

Las claves SSH nos permitirán acceder a los servicios de forma segura sin necesidad de introducir contraseñas. Para ello, generaremos un par de claves pública y privada que nos permitirán acceder a los servicios de forma segura. Estas claves permiten, no usar contraseñas, pero si se pierden o se comparten, cualquiera podría acceder a los servicios que tengamos configurados con ellas. Por ello, es importante guardarlas en un lugar seguro y no compartirlas con nadie.

### Mac 

Para poder acceder a algunos servicios necesitaremos una clave privada y otra pública. Para generarlas, abriremos una terminal y ejecutaremos el siguiente comando, en el cual solo pulsaremos enter para aceptar los valores por defecto:

```bash
ssh-keygen -t rsa -m PEM -C 'personalkey'

Generating public/private rsa key pair.
Enter file in which to save the key (/Users/pedro.nieto/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /Users/pedro.nieto/.ssh/id_rsa.
Your public key has been saved in /Users/pedro.nieto/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:
XXXXXX
The key's randomart image is:
+---[RSA 3072]----+
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
+----[SHA256]-----+
```

Una vez generadas las claves, accederemos a la carpeta donde se han generado y copiaremos el contenido de la clave pública en el portapapeles:

```bash
cat ~/.ssh/id_rsa.pub
```

### Windows

Para poder acceder a algunos servicios necesitaremos una clave privada y otra pública. Para generar la clave usaremos puttygen que se puede descargar de la siguiente url:

https://www.puttygen.com/

Una vez instalado al abrirlo nos aparecerá una pantalla en la que seleccionaremos el tipo de clave RSA y el número de bits 3072. Una vez seleccionados pulsaremos el botón Generate y moveremos el ratón por la pantalla hasta que la barra de progreso se complete. Una vez completada la barra de progreso, se habrá generado la clave y podremos guardarla en un fichero con el nombre que queramos.

Se recomienda guardarlas en una carpeta con los nombres:
- id_rsa (privada)
- id_rsa.pub (pública)

Una vez generadas las claves, accederemos a la carpeta donde se han generado y copiaremos el contenido de la clave pública en el portapapeles.


## Docker

### Mac

Para instalar Docker en Mac, visitaremos la web de descargas de Docker y descargaremos el instalador correspondiente, teniendo en cuenta si nuestro sistema operativo es Intel o M1. Una vez descargado lo abriremos y validaremos que funciona con el siguiente comando. También deberemos registrarnos para su uso.

```bash
docker ps
```

Si el comando anterior nos devuelve un error, deberemos abrir la aplicación Docker y validar que funciona correctamente. En caso de no ser un comando reconocido, deberemos instalarlo con el siguiente comando:

```bash
brew install --cask docker
```

### Windows
Para instalar Docker en Windows, visitaremos la web de descargas de Docker y descargaremos el instalador correspondiente. Una vez descargado lo abriremos y validaremos que funciona con el siguiente comando. También deberemos registrarnos para su uso.

```bash
docker ps
```

Si nos da un error de wsl deberemos instalarlo con el siguiente comando, ejecutado desde un cmd con permisos de administrador.

```bash
wsl --update 
```

Una vez instalado, deberemos reiniciar el equipo y volver a abrir el docker desktop.
Si recibimos un error de Virtualization deberemos activarla en la BIOS del equipo... Aquí mejor buscamos ayuda de alguien que sepa :-).