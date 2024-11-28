import sys  #Para aceptar argumentos desde el cmd

def suma(x, y):
    resultado = x + y
    print(f'El resultado de la suma es: {resultado}')

if __name__ == "__main__":
    # Obtener los números desde los argumentos
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    suma(x, y)
