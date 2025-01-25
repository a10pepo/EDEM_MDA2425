def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

lista_primos=[]
for a in range(1,100):
    b=es_primo(a)
    if(b==True):
        lista_primos.append(a)
print(lista_primos)



