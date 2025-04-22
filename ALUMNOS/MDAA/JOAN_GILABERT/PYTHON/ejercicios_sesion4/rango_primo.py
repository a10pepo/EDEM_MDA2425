def primo (min, max):
    lista=[]
    for num in range(min,max+1):
        es_primo=True
        for div in range(2, num):
            resto=num%div
            if resto==0:
                es_primo=False
                break
        if num==1:
             es_primo=False
        if es_primo:
            lista.append(num)
    return f'Los números primos son: {lista}'
    