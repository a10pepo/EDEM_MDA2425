'''
    ---------- RETO 5 Básico -----------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Escribe un programa que sea capaz de pedirle a un usuario por consola** que introduzca una contraseña y mientras que ésta no sea "admin", el programa seguirá pidiéndola.

Si la contraseña es errónea, deberá sacarle un mensaje de error y volver a pedirle la contraseña hasta que la introduzca bien. Si el usuario introduce "admin" correctamente, el programa le deberá mostrar un mensaje "Bienvenido al programa señor ADMIN" y luego terminar.

NOTA: Para pedir por pantalla y guardarlo en una variable llamada password debes hacer uso de password:str = input('Introduce una contraseña')
'''

def reto5Basico():
  acierto: bool = False
  valor_introducido: str = ''

  while not acierto:
      valor_introducido = input('Introduzca una contraseña: ')
      if(valor_introducido == 'admin'):
          acierto = True
          print(f"Bienvenido al programa señor ADMIN")
          break
      else:
          print("¡Contraseña incorrecta!")