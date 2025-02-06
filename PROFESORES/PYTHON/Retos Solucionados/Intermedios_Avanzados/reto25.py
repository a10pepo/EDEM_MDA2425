'''
    ---------- RETO 25 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    -------------------------------------------------
'''

'''
Partiendo de la lista:

comunidades = ["Madrid", "Aragón",
                    "Valencia", "Cataluña",
                    "Extremadura", "Castilla y León",
                    "Castilla La Mancha", "Asturias",
                    "Murcia", "Cantabria", "País Vasco",
                    "Andalucia"]

Crea una función que sea capaz de devolver una lista ordenada según la longitud de su nombre.
'''

def comunidadMasLarga(lista):
    longitud = []
    for comunidad in lista:
        longitud.append((len(comunidad), comunidad))
    longitud.sort()
    return longitud[-1][1]


def reto25Avanzado():
  print(comunidadMasLarga(["Madrid", "Aragón",
                      "Valencia", "Cataluña",
                      "Extremadura", "Castilla y León",
                      "Castilla La Mancha", "Asturias",
                      "Murcia", "Cantabria", "País Vasco",
                      "Andalucia"]))
