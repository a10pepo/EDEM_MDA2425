def es_primo(num):
     for n in range (2, num):
          if num % n ==0:
               print(f'El numero {num} no es primo')
               return False
          else:
               print(f'El numero {num} es primo')
               return True
       
es_primo(4)
