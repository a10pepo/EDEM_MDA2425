# postgressetup
Postgres and PGAdmin

Los pasos para levantar este ejercicio son:

1. Clonar el repositorio
2. Ejecutar el comando `docker-compose up -d`
3. Abrir el navegador en la url `http://localhost:5050`
4. Ingresar con las credenciales:
    - user: pgadmin4@pgadmin.org
    - password: admin
5. Crear un nuevo servidor con las siguientes credenciales:
    General:
    - Name: DBServer

    Connection:
    - Host name/address: postgres
    - Port: 5432
    - Maintenance database: postgres
    - Username: postgres
    - Password: Welcome01

6. Crear una nueva base de datos con el nombre `dvdrental`
7. Botón derecho "Restore"
8. Subir el archivo `dvdrental.tar` que se encuentra en esta carpeta
9. Una vez subido el archivo, escribir "/dvdrental.tar" en la barra hacer click en el botón "Select"
10. Hacer click en el botón "Restore" y esperar a que termine el proceso
11. En la parte superior ya puedes ir a Query Tool y ejecutar las consultas

