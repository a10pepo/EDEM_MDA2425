✈️ Aeródromo Management System (PostgreSQL + Redshift)
Este script implementa un sistema de gestión para un pequeño aeródromo. Permite registrar y consultar información sobre:

Aviones

Vuelos

Pasajeros

Relación entre pasajeros y vuelos

⚙️ ¿Qué hace este código?
Conexiones a bases de datos
Se conecta a dos bases de datos:

Una base de datos PostgreSQL (RDS) que actúa como sistema de origen (Data Lakehouse)

Una base de datos Redshift que actúa como sistema de destino (Data Warehouse)

Crea tablas (si se habilita create_tables())
Define las siguientes tablas en PostgreSQL:

airplanes: Información de cada avión

passengers: Datos personales de los pasajeros

flights: Información de cada vuelo

flight_passengers: Relación vuelo-pasajeros

Carga de datos iniciales (opcional)
A través de la función insert_data, se inserta un conjunto inicial de datos de prueba.

Funciones interactivas desde terminal
El programa lanza un menú interactivo que permite al usuario:

Ver aviones en hangares

Ver vuelos que han aterrizado

Ver pasajeros que han llegado

Registrar un nuevo avión

Registrar un nuevo vuelo

Persistencia en base de datos
Toda la información ingresada se guarda de forma persistente en la base de datos PostgreSQL, y opcionalmente puede replicarse o transformarse en Redshift para análisis.

Migración a Redshift (DWH)
El script también incluye funciones para extraer datos de PostgreSQL y crear/inyectar esos datos en Redshift:

extract_data_from_postgres

extract_schema_and_type_from_postgres

create_table_from_schema_in_aws_redshift

insert_data_redshift

🧪 Dependencias
Asegúrate de tener instalados los siguientes paquetes de Python:
pip install psycopg2 python-dotenv