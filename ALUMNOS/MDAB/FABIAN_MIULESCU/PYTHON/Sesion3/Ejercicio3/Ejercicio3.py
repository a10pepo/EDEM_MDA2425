lista_anos = [1900, 2000, 2004, 2010, 2020, 2024, 2100]

for ano in lista_anos:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"El año {ano} es bisiesto.")
    else:
        print(f"El año {ano} no es bisiesto.")

