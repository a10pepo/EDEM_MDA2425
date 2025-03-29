def bisiesto (año)->bool:
    bis=True
    if año % 4 == 0:
         print(f'{año} es bisiesto')
         bis=True
    else:
         print(f'{año} no es bisiesto')
         bis=False
    return bis