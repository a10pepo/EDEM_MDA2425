'''
    ---------- RETO 5 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe un programa que realice lo mismo que el programa del reto 4,
pero que elimine de la lista aquellos lenguajes que el usuario conoce y únicamente muestre aquellos que no conoce.
'''

def reto5Avanzado():
  lista_lenguajes: [str] = ['Python', 'TypeScript', 'JavaScript', 'Java', 'C#']
  lista_capacidades: [(str,str)] = []

  for lenguaje in lista_lenguajes:
      conoce: str = input(f"¿Conoces el lenguaje {lenguaje}? (si / no) ")
      while(conoce not in ['si', 'no']):
          conoce = input(f"Debes responder \"si\" o \"no\". ¿Conoces el lenguaje {lenguaje}? (si / no) ")
      
      if(conoce == 'si'):
          lista_capacidades.append((lenguaje, conoce))


  for conocimiento in lista_capacidades:
    print(f"- {conocimiento[0]}: {conocimiento[1]}")