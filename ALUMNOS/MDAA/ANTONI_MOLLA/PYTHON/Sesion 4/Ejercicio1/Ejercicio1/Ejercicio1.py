def numeros_primos (inicio, fin):
    print(f'Los numeros primos entre {inicio} y {fin} son:')
    for num in range (inicio,fin+1): #Range=Rango
        if num <= 1:
            continue
        for i in range(2, num):
            if num % i ==0:
                break
        else:
            print(num)
    
numeros_primos(1,100)