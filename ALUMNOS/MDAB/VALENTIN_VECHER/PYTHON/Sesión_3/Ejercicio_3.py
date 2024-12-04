# # al poner None queremos decir que no tiene retorno.
# def bisiesto(anio:int) -> None: #esto sirve para decir que va ha recibir de vuelta
#     if (anio%4==0) and ((anio%100!=0) or (anio%400==0)):
#         return True
#     else: 
#         return False

# def verificar_result(anios):
#     resultados={}
#     for anio in anios:
#       resultados[anio]= bisiesto(anio)  
#     return resultados

# lista_de_anios=[2020, 2021, 2022, 2023, 2024, 1900]

# resultados= verificar_result(lista_de_anios)

# for anio, es_bisiesto in resultados.items():
#     if es_bisiesto:
#         print(f'El {anio} es bisiesto')
#     else:
#         print(f'El {anio} no es bisiesto ')

# al poner None queremos decir que no tiene retorno.
def bisiesto(anyo) -> None: #esto sirve para decir que va ha recibir de vuelta
    if (anyo%4==0) and ((anyo%100!=0) or (anyo%400==0)):
        print(f'el {anyo} es bisiesto')     
    else: 
        print(f'el {anyo} no es bisiesto')

list_amios=[2020, 2021, 2022, 2023, 2024, 1900]
for anyo in list_amios:
    bisiesto(anyo)

