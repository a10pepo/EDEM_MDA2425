# Ejercicios Prácticos con Kafka: Producer y Consumer

Este repositorio contiene ejercicios prácticos para trabajar con **Kafka Producer** y **Kafka Consumer** utilizando un JSON con datos de transferencias bancarias. Todos los ejercicios se realizan exclusivamente por consola, sin necesidad de bases de datos.

## Ejercicios

### 1. Ejercicio de Producción de Datos

- **Objetivo**: Configurar un productor de Kafka que lea el JSON de transferencias bancarias y lo envíe como mensajes a un tópico de Kafka.
- **Acción**: El productor envía cada transferencia como un mensaje JSON al tópico y muestra por consola cada mensaje enviado.

### 2. Ejercicio de Consumo de Datos

- **Objetivo**: Configurar un consumidor de Kafka que lea los mensajes desde el tópico donde se publican las transferencias.
- **Acción**: El consumidor deserializa los mensajes JSON y los muestra por consola, mostrando el detalle de cada transferencia.

### 3. Filtrado de Transferencias por País

- **Objetivo**: Filtrar y mostrar solo las transferencias de países específicos (ej. paraísos fiscales).
- **Acción**: El consumidor solo muestra las transferencias cuyo país de origen o destino sea **Islas Caimán** o **Singapur**, imprimiendo solo esos registros por consola.

### 4. Transformación de Datos (Suma de Montos)

- **Objetivo**: Transformar los datos y calcular el monto total de transferencias por país.
- **Acción**: El consumidor agrupa las transferencias por país de origen y muestra la suma total de los montos por país, todo en consola.

### 5. Almacenamiento Temporal en Memoria (Solo por Consola)

- **Objetivo**: Procesar solo las transferencias con estado **"Completada"**.
- **Acción**: El consumidor filtra las transferencias con estado "Completada" y las imprime por consola.

### 6. Tópico de Transacciones Pendientes

- **Objetivo**: Filtrar y mostrar solo las transferencias con estado **"Pendiente"**.
- **Acción**: El consumidor filtra las transferencias con estado "Pendiente" y las muestra por consola, indicando que están pendientes de procesar.

## Requisitos

- **Apache Kafka** instalado y corriendo.
- **Kafka Python (confluent-kafka)** para la implementación de Producer y Consumer.
- **JSON de Transferencias Bancarias** que contiene información como el ID de la transferencia, país de origen/destino, monto, etc.

## Ejecución

1. **Ejecutar el Productor**:
    - El productor enviará los datos de las transferencias al tópico de Kafka.

2. **Ejecutar el Consumidor**:
    - El consumidor leerá los mensajes de Kafka y los procesará según el ejercicio.

## Contribuciones

Si deseas contribuir, por favor haz un fork del repositorio, realiza los cambios necesarios y crea un pull request.
