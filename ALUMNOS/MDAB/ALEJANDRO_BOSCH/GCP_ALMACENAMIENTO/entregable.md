# Entregable End2End GCP Almacenamiento 

En este documento, se quiere mostrar todos los pasos seguidos para desplegar una infraestructura en GCP, de manera manual, mediante la UI.

- En primer lugar, se crean las máquinas virtuales. Para este caso, se llamarán orders-app y delivery-app. La primera se creará manualmente, con región en europe-west1 (Bélgica), serie E2 micro y firewall abierto para los protocolos HTTP y HTTPS. El proceso de creación de delivery-app es similar, solo que ahora, en vez de hacerlo manualmente, se ha hecho mediante comando. Para ello, se ha creado mediante una imagen de orders-app, con las mismas dependencias instaladas (versiones de Python y Docker). Luego, se arrancan las imágenes creadas.
  ![alt text](images/image-1.png)

    ![alt text](images/image.png)

    ![alt text](images/image-6.png)

    ![alt text](images/image-5.png)

    ![alt text](images/image-3.png)


- A continuación, se han creado tanto topics como suscripciones de ambas apps (orders-app-events, orders-app-events-sub...)
  ![alt text](images/image-7.png)

- Luego, se procede a crear la instancia de PostgreSQL. Se introduce la configuración pertinente para el uso de esta infraestructura y se crea la red default. Una vez creada, se crea la BBDD ecommerce.

    ![alt text](images/image-8.png)

    ![alt text](images/image-9.png)

    ![alt text](images/image-10.png)

    ![alt text](images/image-11.png)

    ![alt text](images/image-12.png)

    ![alt text](images/image-13.png)

    ![alt text](images/image-14.png)

    ![alt text](images/image-15.png)

    ![alt text](images/image-16.png)

    - En esta parte, se hace uso del bucket creado para el Data Lake, utilizando el parquet generado.

    ![alt text](images/image-23.png)

    - También se aprovecha para crear la capa medallón. 

    ![alt text](images/image-20.png)


- En esta parte, se crea una nueva subscripción, para nuestra capa analítica, que será con BigQuery. 

    ![alt text](images/image-17.png)


- Aquí, desplegamos la parte de EL del pipeline para sincronizar la BBDD PostgreSQL con BigQuery. Para ello, creamos las credenciales por defecto con nuestra aplicación, permitiendo identificar los servicios de GCP con nuestra cuenta de usuario.
  ![alt text](images/image-18.png)

  ![alt text](images/image-19.png)

- En esta parte, se inician ambas máquinas (orders y delivery) y empiezan a generar mensajes.

  ![alt text](images/image-21.png)

  ![alt text](images/image-22.png)

-  A continuación, se ejecuta el script de DBT en local. Luego, se crea la vista en BQ del modelo **gold**.

  ![alt text](images/image-24.png)

  ![alt text](images/image-25.png)

- Finalmente se realiza un dashboard con Metabase, para ello se crea una **SA**, con los permisos de:
  - BigQuery Data Viewer (roles/bigquery.dataViewer) → Para leer datos.
  - BigQuery Job User (roles/bigquery.jobUser) → Para ejecutar consultas.
  - BigQuery Metadata Viewer (roles/bigquery.metadataViewer) → Para ver esquemas y tablas.


  ![alt text](images/image-27.png)

  ![alt text](images/image-28.png)


### Propuesta 1

  - Esta parte extra del e2e corresponde a la de añadir un nuevo tópico y suscriptor en Pub/Sub desde Orders App.
  En este caso, he optado por añadir un backup de orders-events.

  - Para ello, añado el código que se ve en las imágenes, para que cuando genere datos, se envien a ese tópico y subscriptor.
    - Destacar, que para ello, se ha editado el código de orders con VIM de la instancia, para añadir el código que se muestra.

  ![alt text](images/image-29.png)

  ![alt text](images/image-30.png)

  ![alt text](images/image-31.png)

### Propuesta 2

  - En esta parte, se ha añadido una **nueva app**, llamada **customer-service-app**
  - Para ello he creado una nueva VM, con el template de imágen que ya había.
  - Finalmente, se enciende la máquina, se configura, y se añade la carpeta con VIM de la nueva app, junto a su nuevo código para que envie a la nueva tabla.
  - Se crea un nuevo topic, junto a nueva subscripción que escribirá directamente a BigQuery los mensajes recibidos.


  ![alt text](images/image-32.png)

  ![alt text](images/image-33.png)

  ![alt text](images/image-34.png)

  ![alt text](images/image-35.png)

  ![alt text](images/image-36.png)
