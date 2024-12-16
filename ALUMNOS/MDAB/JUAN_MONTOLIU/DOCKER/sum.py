import sys

if len(sys.argv) != 3:
    print("Valores erroneos. Uso correcto: python3 sum.py <n1> <n2>")

else:
    n1 = float(sys.argv[1])
    n2 = float(sys.argv[2])
    print(f"La suma de {n1} y {n2} es {n1 + n2}")