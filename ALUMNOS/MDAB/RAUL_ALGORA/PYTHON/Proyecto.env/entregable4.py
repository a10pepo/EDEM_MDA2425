




# # FUNCIÓN QUE POR UN RANGO EN PARAMETRO TE DA LOS NUMEROS PRIMOS 
# def obtener_rango():
#     inicio = int(input("Dame el número de inicio del rango: "))
#     fin = int(input("Dame el número final del rango: "))
    
#     for i in range(inicio, fin):
        
#         es_primo = True
#         for num in range(2, int(i**0.5) + 1):  
#             if i % num == 0:
#                 es_primo = False
#                 break

#         if es_primo:
#             print(f'El numero {i} es primo')

# obtener_rango()


# FUNCIÓN PARA COMPROBAR SI UN NUMERO ES PRIMO O NO

# def es_primo():
#     numero = int(input('¿Qué número quieres probar?:'))
    
#     if numero < 2:
#         print(f"{numero} no es primo.")
#         return
    
    
#     for i in range(2, int(numero**0.5) + 1):
#         if numero % i == 0:
#             print(f"{numero} no es primo.")
#             return
    
#     print(f"{numero} es primo.")

# es_primo()


# FUNCIÓN PARA COMPROBAR SI UN AÑO ES BISIESTO O NO


# def año_bisiesto():
#     año = int(input('¿Qué año quieres probar?:'))
#     bisiesto = False
#     if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
#         bisiesto= True
    
#     if bisiesto:
#         print(f'El año {año} es bisiesto')
#     else:
#         print(f'El año {año} no es bisiesto')

# año_bisiesto()
    
#PARA HACER UNA CONSULTA A UN HTTPS

import requests

respuesta = requests.get(' https://randomuser.me/api')
datos = respuesta.json()
usuario = datos['results'][0]
nombre = usuario['name']['first']  
apellido = usuario['name']['last'] 

print(nombre, apellido)



