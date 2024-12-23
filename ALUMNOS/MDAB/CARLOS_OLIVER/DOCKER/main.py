def multiplicar(num1, num2):
    """
    Multiplica dos números y devuelve el resultado.
    """
    return num1 * num2

def main():
    print("Script de multiplicación")
    try:
        # Solicitar al usuario dos números
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        # Calcular el resultado
        resultado = multiplicar(num1, num2)
        
        # Mostrar el resultado
        print(f"El resultado de multiplicar {num1} por {num2} es: {resultado}")
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")

if __name__ == "__main__":
    main()