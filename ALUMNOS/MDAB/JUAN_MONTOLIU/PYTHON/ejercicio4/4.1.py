#1.1
for number_primo in range(2, 101):
    if number_primo < 2:
        print(f"{number_primo} no es un número primo.")
    else:
        es_primo = True

        for i in range(2, int(number_primo**0.5) + 1):
            if number_primo % i == 0:
                es_primo = False 
                break 

        if es_primo:
            print(f"{number_primo} es un número primo.")

#1.2
number_primo=int(input(f"introduce el numero entero: ")) 
if number_primo < 2:
    print(f"{number_primo} no es un número primo.")
else:
    es_primo = True

    for i in range(2, int(number_primo**0.5) + 1):
        if number_primo % i == 0:
            es_primo = False 
            break 

if es_primo:
    print(f"{number_primo} es un número primo.")
else:
    print(f"{number_primo} no es un número primo.")

#1.3
x = int(input(f"Introduce el año que quieras identificar: "))
if x % 4 == 0 and (x % 100 ==0 or not x %400 == 0):
    print(f"{x} es bisiesto")
else:
    print(f"{x} no es bisiesto")




    


