'''
    ---------- RETO 11 Avanzado --------------
    AUTOR: MARTÍN SAN JOSÉ DE VICENTE
    EMAIL: martin@imaginagroup.com
    AÑO: 2021
    LICENCIA CÓDIGO: OSS
    ------------------------------------------
'''

'''
Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:

- NIF (string)
- nombre (string)
- apellidos (string)
- teléfono (string)
- email (string)
- preferente (boolean)

El programa debe mostrar las siguientes opciones para que escoja el usuario:

(1) Añadir un cliente
(2) Eliminar cliente por NIF
(3) Mostrar Cliente por NIF
(4) Listar TODOS los clientes
(5) Mostrar ÚNICAMENTE los clientes preferentes
(6) Finalizar Programa

'''


#Cartera de Clientes
lista_clientes: [] = []
cliente = {}

def crearCliente():
    global lista_clientes
    cliente['NIF'] = input('NIF:')
    cliente['Nombre'] = input("Nombre: ")
    cliente['Apellidos'] = input("Apellidos: ")
    cliente['Telefono'] = input("Telefono: ")
    cliente['Email'] = input("Email: ")
    cliente['Preferente'] = input('¿Es un cliente preferente? (Si / No)')
    
    lista_clientes.append(cliente)

def mostrarClientes():
    global lista_clientes
    for i, cliente in enumerate(lista_clientes):
        print(f"{i} - {cliente['Nombre']} {cliente['Apellidos']}")

def mostrarPreferentes():
    global lista_clientes
    lista_preferentes: [] = []
    for i, cliente in enumerate(lista_clientes):
        if(cliente['Preferente'] == 'Si'):
            lista_preferentes.append(cliente)
    print('Lista de clientes preferentes:')
    for i, preferentes in enumerate(lista_preferentes):
        print(f"{i} - {cliente['Nombre']} {cliente['Apellidos']}")
    print('No existe ningún cliente con este NIF')


def mostrarClienteNIF():
    global lista_clientes
    nif = input('¿NIF?')
    for i, cliente in enumerate(lista_clientes):
        if(nif == cliente['NIF']):
            print(f"{nif} - {cliente['Nombre']} {cliente['Apellidos']}")
            return
    print('No existe ningún cliente con este NIF')

def eliminarClienteNIF():
    global lista_clientes
    nif = input('¿NIF?')
    for i, cliente in enumerate(lista_clientes):
        if(nif == cliente['NIF']):
            lista_clientes.remove(cliente)
            return
    print('No existe ningún cliente con este NIF')

def mensajeCierre():
    print("Cerrando...")

def switch(opcion):
    switcher = {
        #invocar métodos
        1 : crearCliente,
        2 : mostrarClientes, 
        3 : mostrarPreferentes,
        4 : mostrarClienteNIF,
        5 : eliminarClienteNIF, 
        0 : mensajeCierre,
    }

    func = switcher.get(opcion, "¡Opción no valida!")
    func() # Ejecutamos la función asignada a la propiedad escogida

opciones = """
Opcion 1 : Añadir un cliente
Opcion 2 : Mostrar Todos los Clientes
Opcion 3 : Mostrar Clientes Preferentes
Opcion 4 : Mostrar Cliente por NIF
Opcion 5 : Eliminar Cliente por NIF
Opcion 0 : Salir 
"""

def reto11Avanzado():
  opcion = ""

  while(opcion!=0):
      print(opciones)
      try:
        opcion = int(input("Bienvenido a tu cartera de clientes. Escoge una opción: "))
        print(f'Escogida {opcion}')
        switch(opcion)
      except:
        print("Opcion no valida")