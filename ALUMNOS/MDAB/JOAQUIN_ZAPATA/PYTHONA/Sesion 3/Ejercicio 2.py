for i in range(2,101):
    es_primo= True
    for num in range(2, i):
        if i % num == 0:
            es_primo= False
            break
    if es_primo:
        print(i)