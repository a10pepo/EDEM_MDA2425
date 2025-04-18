def es_primo (num):
    es_primo=True
    for div in range(2, num):
        resto=num%div
        if resto==0:
            es_primo=False
            break
    if num==1:
        es_primo=False
    if es_primo:
        print(f'{num} es primo')
    return es_primo
