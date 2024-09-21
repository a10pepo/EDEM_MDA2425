'''
    ---------- RETO 28 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    -------------------------------------------------
'''

'''
Crea un script que solicite al usuario que escriba una frase que contenga las palabras Madrid y Valencia.

Una vez lo haya introducido, se debe mostrar la frase, habiendo sustituido Madrid por Valencia y Valencia por Madrid.

Por ejemplo: Si el usuario introduce Vivo en Madrid y viajo a Valencia la salida del programa debe ser Vivo en Valencia y viajo a Madrid.
'''

def reto28Avanzado():
  print("Introduce una frase con 'Madrid' y 'Valencia'")
  text = input().split()

  for i in range(len(text)):
      if "Madrid" in text[i]:
          n = text[i].index("Madrid")
          text[i] = text[i][:n] + "Valencia" + text[i][n + 6:]
      elif "Valencia" in text[i]:
          n = text[i].index("Valencia")
          text[i] = text[i][:n] + "Madrid" + text[i][n + 8:]

  print(*text)