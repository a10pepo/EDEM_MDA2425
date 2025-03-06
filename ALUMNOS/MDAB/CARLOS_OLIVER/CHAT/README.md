# Chat System

## Descripción

El objetivo de este proyecto es implementar un chat en tiempo real utilizando Apache Kafka como broker de mensajes. Para ello deberéis implementar varios interlocutores que se comunicarán entre sí a través de un topic de Kafka.

## Fase 1

Usando el código proporcionado debéis ser capaces de generar un chat usando streamlit que permita a varios usuarios comunicarse entre sí. 

### Pasos a seguir

En esta carpeta tienes una base de trabajo para empezar con vuestro desarrollo, para hacerlo funcionar debéis ejecutar estos pasos

```bash
streamlit run chatbot.py
```

Una vez ejecutado este comando, se abrirá un navegador con la interfaz de usuario de streamlit. En ella podrás ver un chat en el que podrás escribir mensajes y enviarlos.

Una vez que hayas conseguido que funcione, debes modificar el código para que los mensajes se intercambien a través de un topico de kafka. Para ello, deberás implementar un productor y un consumidor de mensajes que se comuniquen a través de un topic de kafka.

## Fase 2

Una vez que los mensajes se intercambien a través de kafka, debes implementar un sistema de supervisión de mensajes usando pyspark. Para ello, deberás implementar un consumidor que se suscriba a un topic de kafka y que sea capaz de detectar mensajes que contengan palabras malsonantes. En caso de detectar una palabra malsonante, el consumidor deberá enviar un aviso al emisor del mensaje con un aviso que bloqueará al usuario si llega a 3 avisos y reemplazar la palabra malsonante por asteriscos en el mensaje al destinatario.

## Fase 3

Una vez hayas llegado a este punto, estas listo para que todos los alumnos de clases compartáis un chat entre vosotros... qué necesitas cambiar para ello en el código?


