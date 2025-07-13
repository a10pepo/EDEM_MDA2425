# Entregable End2End AWS Almacenamiento

## Descripción

En este entregable tenéis que practicar el desarrollo del end2end que hemos visto en clase.

La idea es que cojáis el código de `initial_info.py` con la información de aviones, vuelos y pasajeros y creéis un end2end que contenga lo siguiente:

- Una base de datos transaccional en PostgreSQL en AWS RDS que contenga el modelo de datos del fichero `initial_info.py`
- Una EL que lleve la información de la base de datos transaccional a una base de datos analítica en AWS Redshift
- Una EL que lleve la información a un data lakehouse usando Iceberg, S3 y Glue

Una vez estén estos pasos hechos, deberías poder dockerizar el código que hayáis hecho cada uno, y poder desplegarlo en una instancia de EC2.
