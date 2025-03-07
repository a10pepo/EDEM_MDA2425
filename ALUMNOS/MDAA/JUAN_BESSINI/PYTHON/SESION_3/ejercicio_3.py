#by Juan Bessini
def es_bisiesto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Lista de años de ejemplo
anos = [1900, 2000, 2024, 2025, 2100, 2400]

for ano in anos:
    if es_bisiesto(ano):
        print(f"El año {ano} es bisiesto.")
    else:
        print(f"El año {ano} no es bisiesto.")

