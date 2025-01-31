import random

# GENERADOR DE MENSAJES DE LA PRESIÓN
msgs = [
    "Presión: 0 milibares - Regadío apagado",
    "Presión: 150 milibares - Advertencia: Presión baja",
    "Presión: 500 milibares - Regadío funcionando correctamente",
    "Presión: 1000 milibares - Advertencia: Presión alta",
    "Presión: 1200 milibares - Error: Riesgo de rotura en las tuberías"
]

def generate_msg():
    return random.choice(msgs)

# GENERADOR DEL LUGAR DEL CAMPO / CASETA DE REGADIO
casetas_goteo = [
    "Caseta Norte",
    "Caseta Sur",
    "Caseta Este",
    "Caseta Oeste",
    "Caseta Central",
    "Caseta Montaña",
    "Caseta Valle",
    "Caseta Lago",
    "Caseta Río",
    "Caseta Sierra",
    "Caseta Prado",
    "Caseta Colina",
    "Caseta Viñedos",
    "Caseta Olivar",
    "Caseta Huerta",
    "Caseta Bosque",
    "Caseta Pantano",
    "Caseta Molino",
    "Caseta Marisma",
    "Caseta Áridos"
]

def generate_place():
    return random.choice(casetas_goteo)






