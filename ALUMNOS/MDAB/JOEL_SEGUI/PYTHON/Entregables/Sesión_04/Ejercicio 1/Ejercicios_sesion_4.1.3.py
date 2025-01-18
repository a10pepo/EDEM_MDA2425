
def bisiesto(año):
    if(año%4 == 0 and (año%100 !=0 or año%400 == 0)):
        return True
    else:
        return False

year = 2024
resultado = bisiesto(year)

print(f'El año {year} es bisiesto? {resultado}')
