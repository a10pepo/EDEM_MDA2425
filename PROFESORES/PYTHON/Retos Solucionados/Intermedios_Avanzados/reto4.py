'''
    ---------- RETO 4 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe un programa que almacene lenguajes de programación en una lista.
El programa deberá preguntar por consola si el usuario conoce o no el lenguaje. El usuario deberá responder "sí" o "no" y cualquier otra respuesta no será tenida en cuenta, preguntando de nuevo la misma pregunta:

¿Conoces el lenguaje de programación "lenguaje"? (si / no) donde "lenguaje" es cada uno de los lenguajes de la lista.
Finalmente, el programa debe mostrar por pantalla la lista de los lenguajes y si el usuario los conoce o no. 
Algo así:
- JavaScript: no
- TypeScript: sí
- Python: sí
- Dart: no

'''


def reto4Avanzado():

  lista_lenguajes: [str] = ['Python', 'TypeScript', 'JavaScript', 'Java', 'C#']
  lista_capacidades: [(str,str)] = []


  for lenguaje in lista_lenguajes:
      conoce: str = input(f"¿Conoces el lenguaje {lenguaje}? (si / no) ")
      while(conoce not in ['si', 'no']):
          conoce = input(f"Debes responder \"si\" o \"no\". ¿Conoces el lenguaje {lenguaje}? (si / no) ")
      lista_capacidades.append((lenguaje, conoce))


  for conocimiento in lista_capacidades:
      print(f"- {conocimiento[0]}: {conocimiento[1]}")
