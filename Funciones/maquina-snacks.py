from funciones_snacks import *

print("---- Máquina de snacks ----")

snacks=[
    {
        'id':1,
        'nombre':'Papas',
        'precio': 27.00
    },
    {
        'id':2,
        'nombre':'totis',
        'precio': 15.50
    },
    {
        'id':3,
        'nombre':'barritas',
        'precio': 10.99
    },
]
while True:
    mostrar_menu()
    opcion = pedir_valor("_:")

    match opcion:
        case 1: # Mostar inventario
            mostrar_snacks(snacks)
        case 2: # Comprar Snack
            id_snack = pedir_valor('Snack a comprar: ')
            comprar_snack(snacks=snacks,snack=id_snack)
        case 3: # Buscar producto por ID
            mostrar_ticket()
        case 4: # Salid
            break
        case _:
            print('Opción no válida')