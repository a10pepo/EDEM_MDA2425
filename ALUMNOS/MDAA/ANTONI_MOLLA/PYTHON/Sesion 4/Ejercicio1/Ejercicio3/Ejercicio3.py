def es_bisiestos(año):
    
    if( año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
        
    else:
        return False

#El 2100 es un ejemplo como año       
print(es_bisiestos(2100))