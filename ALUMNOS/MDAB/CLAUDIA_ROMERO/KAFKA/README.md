# Use case
Este proyecto detecta en tiempo real Pokémon legendarios usando Apache Kafka. Este enfoque puede aplicarse a videojuegos, sistemas de streaming de datos en tiempo real y análisis en vivo de grandes volúmenes de datos.

# Dataset selected
El dataset seleccionado contiene información detallada de Pokémon, incluyendo:
✅ Nombre
✅ Tipo(s)
✅ Estadísticas de combate (HP, Ataque, Defensa, Velocidad)
✅ Generación
✅ Indicador de si es un Pokémon legendario

# Final architecture implemented
1️⃣ Fuente de datos
- Archivo CSV con información de Pokémon (convertido a JSON).

2️⃣ Producer
- Envía datos JSON con estadísticas de Pokémon al topic de Kafka pokemon_data.

3️⃣ Consumer
- Recibe y lee los datos enviados por el producer.
- Filtra solo los Pokémon legendarios.
- Envía los datos filtrados al topic pokemon_legendary.

4️⃣ ksqlDB
- Procesa los datos en tiempo real.
- Crea un STREAM llamado POKEMON_STREAM con todos los Pokémon.
- Crea un STREAM secundario LEGENDARY_POKEMON_STREAM que filtra solo los legendarios.
- Consulta estadísticas de los Pokémon legendarios (promedio de ataque, defensa, etc.).

5️⃣ Kafka UI
- Visualización de los datos en tiempo real.

# Json examples of your data json model
{
    "pokemon": "Mewtwo",
    "type_1": "Psychic",
    "type_2": null,
    "hp": 106,
    "attack": 110,
    "defense": 90,
    "speed": 130,
    "generation": 1,
    "legendary": true
}

# Evidence
[🖥️ Terminal](imagenes/1.png)
[📊 Kafka UI](imagenes/2.png)
[🔍 Consulta en KSQL](imagenes/3.png)
[🔍 Consulta en KSQL](imagenes/4.png)
[📂 Acceder a todas las imágenes](./imagenes/)