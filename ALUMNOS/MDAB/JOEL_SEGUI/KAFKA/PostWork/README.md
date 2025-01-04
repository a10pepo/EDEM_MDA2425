# Monitor de Presión del Agua con Apache Kafka

## Descripción General

Esta aplicación está diseñada para supervisar el estado de la presión del agua en sistemas de riego mediante la simulación de mensajes que enviaría un IOT respecto al estado de la presión. Los mensajes se envían a un tópico de Apache Kafka cada 20 segundos, lo que permite monitorear el funcionamiento del sistema y detectar posibles problemas en tiempo real.

## Caso de Uso

Los sistemas de riego modernos requieren una supervisión constante para garantizar su correcto funcionamiento y prevenir daños en las tuberías. Esta aplicación tiene como objetivo facilitar la supervisión automatizada de la presión del agua mediante el uso de Apache Kafka, una plataforma de mensajería distribuida que permite procesar datos en tiempo real. Además, se podría implementar válvulas automáticas que cierren y apaguen el regadió en función de la situación para evitar problemas.

### Funcionalidades

- Generación automática de mensajes aleatorios con información sobre la presión del agua (simulación de un IOT).
- Envio de mensajes a un tópico de Apache Kafka para su posterior consumo.
- Clasificación de mensajes según el estado del sistema:
  - **Presión baja**: Indica que el riego está  funcionando de manera ineficiente.
  - **Presión normal o apagado**: Indica que el sistema está funcionando correctamente.
  - **Presión alta**: Emite advertencias o errores que requieren atención inmediata.

### Ejemplo de Mensajes

- **Presión 0 milibares** - Regadío apagado.
- **Presión 150 milibares** - Advertencia: Presión baja.
- **Presión 500 milibares** - Regadío funcionando correctamente.
- **Presión 1000 milibares** - Advertencia: Presión alta.
- **Presión 1200 milibares** - Error: Riesgo de rotura en las tuberías.

## Arquitectura

1. **Generador de Mensajes**: Un script de Python que genera mensajes aleatorios sobre el estado de la presión.
2. Productor de Kafka: Llama el generador de mensages y los envía a un tópico.
3. **Apache Kafka**: Plataforma de mensajería distribuida que actúa como mediador para enviar los mensajes generados al tópico correspondiente.
4. Consumidor / Productor: Lee los mensajes, los filtra y los envía a otro tópico (los mensajes relevantes).
5. **Consumidor Kafka**: Otro sistema o aplicación que consume los mensajes del tópico para visualizarlos, almacenarlos o realizar acciones correctivas.

## Casos de Uso en la Vida Real

1. **Supervisión Agrícola**:
   - Permite a los agricultores identificar problemas en los sistemas de riego y optimizar el consumo de agua.
2. **Mantenimiento Preventivo**:
   - Detecta presiones peligrosamente altas que podrían causar roturas en las tuberías, lo que reduce costos de reparación.
3. **Alertas en Tiempo Real**:
   - Envía notificaciones automáticas al personal técnico en caso de errores graves.

## Extensiones Futuras

- Integración con bases de datos para almacenar registros históricos.
- Implementación de un sistema de notificaciones por correo o SMS.
- Creación de un panel de control para visualizar la presión en tiempo real.

## Notas Finales

Este proyecto es una demostración de cómo Apache Kafka puede ser utilizado en aplicaciones de IoT y monitoreo en tiempo real. Es adaptable a diferentes contextos y puede ampliarse según las necesidades del sistema.

## Como ejecutarlo

- Hacer el docker compose up.
- Instalar todos los paquetes del requirements.
- Ejecutar el monitor_alerts.py que se encarga de hacer de filtro para enviarte los mensages importantes.
- Ejecutar el producer.py qu ees el productor de este proyecto de kafka.
- Y por último, ejecutar el consumer.py, que es el que se encarga de avistarte de las alertas importantes.

###### [si deseas que funcione más rápido tienes que bajar el timesleep del producer (se ubica en el loop for)]