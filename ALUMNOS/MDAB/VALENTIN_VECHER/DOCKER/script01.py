import sys 

if len(sys.argv) != 3:
    print("Uso: python script.py <num1> <num2>")

else:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    print(f"Partiendo de los números {num1} y {num2}: {num1 + num2}")
