# Importar las funciones
from funciones_inventario import *
print('---- Sistema de inventario ----')

# Declarar variables
inventario = [
    {
    "ID": 1,
    'nombre':'Camisa',
    'precio':20.99,
    'cantidad':10}]
while True:
    mostrar_menu()
    opcion = pedir_valor(": ",1)

    match opcion:
        case 1: # Mostar inventario
            mostrar_inv(inventario)
        case 2: # Agregar producto
            inventario.append(agregar_producto(len(inventario)))
        case 3: # Buscar producto por ID
            ide = pedir_valor("Ingrese el ID: ",1)
            buscar_producto(inventario,ide)
        case 4: # Salid
            break
        case _:
            print('Opción no válida')