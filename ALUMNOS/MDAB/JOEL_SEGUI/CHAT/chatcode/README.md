# Correcto funcionamiento

## Fase 1

- Hacer un docker compose up
- Instalar los requerimientos: 
    - ```pip install requirements -r```

## Fase 2
- **Ejecutar el chatbot**
    - ```cd chatcode```
    - ```streamlit run chatbot.py```

- **Ejecutar el controlador de censura**
    - ```python censory.py```

- **Ejecutar el consumidor**
    - ```python consumer.py```


## Fase 3

Escribe mensajes en el chatbot, los cuales se envian al tópico [chat], luego se analizan uno a uno con la intención de detectar palabrotas y se reenvían al tópico [censura], y finalmente, con el consumidor se puede ver los mensajes enviados censurados.