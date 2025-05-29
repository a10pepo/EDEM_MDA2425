Mi propuesta para el entregable de Kafka se basa en una arquitectura donde recibimos en formato JSON datos de diferentes maquinas sobre sus temperaturas, es decir, un modelo de IoT. Este tipo de modelos son muy comunes en entornos como fabricas y almacenes donde hay maquinaria cuya temperatura es importante controlar.

Como se puede ver en "architecture.png", tenemos un generador.py que ha generado aleatoriamente 1000 entradas de temperatura en un json las cuales lee nuestro producer.py y  las envia a un topic de Kafka llamado "iot_e2e" con 2 seg de espera entre cada envio (para simular un entorno algo mas realista). Tambien las printea por consola como se puede ver en las capturas.

Posteriormente, el primer consumer "consumer_temp_high" lee dichas temperaturas y filtra solamente las altas temperaturas (temp > 80) para almacenarlas en otro topic "high_temp_iot", ademas de printearlas por consola como se puede ver en las capturas.

Luego mediante KSQL (he usado KSQL-UI), he generado un stream, una tabla y un nuevo TOPIC llamado AVG_TEMPERATURE. Lo que hacemos con este apartado es leer las high_temp y sacar la media (avg) por maquina (id). Esto podria ser relevante en un contexto real para su posterior analisis en caso de querer ver por ejemplo que máquinas se calientan mas de media.

Finalmente el "consumer_final" lo que hace es leer dicho topic con las avg_temp y printearlas por consola. Todo esto se puede ver en las capturas.