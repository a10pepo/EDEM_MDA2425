

for num in range (1,101): #Range=Rango
    if num <= 1:

#Sigue iterando sobre los valores menores de num para verificar si es numero primo
        continue
    
#Continue da la orden de seguir on el orden del codigo
    for i in range(2, num):
        if num % i ==0:
                break

    else:
        print(num)


