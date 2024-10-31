

for num in range (1,101): #Range=Rango
    if num<= 1:
        continue #Sigue iterando sobre los valores menores de num para verificar si es numero primo

    for i in range(2, num):
        if num % i ==0:
                break

    else:
        print(num)


