'''
    ---------- RETO 7 Básico -----------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe un programa que contenga dos variables. Una de ellas representa la contraseña de un usuario y la otra un texto introducido. 
El programa debe poder mostrar por pantalla si las dos cadenas de texto son iguales sin tener en cuenta mayúsculas y minúsculas.
'''

def reto7Basico():
  pass_word: str = "admin"
  texto_introducido: str = "AdMiN"

  if(pass_word.lower() == texto_introducido.lower()):
      print ("¡HURRA! ¡Las contraseñas son iguales!")
  else:
      print ("¡ERROR! ¡Las contraseñas no coinciden!")