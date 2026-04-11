print("---- Sistema de inventario ----")
inventario = []

productos = int(input("Cuantos productos agregará al inventario: "))
for i in range(productos):
    inventario.append({})
    print(f"Proporciona los valores del producto {i+1}")
    inventario[i]['ID'] = i+1
    inventario[i]['Nombre'] = input("Nombre: ")
    inventario[i]['Precio'] = float(input("Precio: "))
    inventario[i]['Cantidad'] = int(input("Cantidad: "))

print(inventario)
buscar_id = int(input("Ingrese el indice a buscar: "))
for i in inventario:
    if buscar_id == i['ID']:
        for clave, valor in i.items():
            print(f"{clave} : {valor}")
        print("---------")

print("---- Inventario actualizado ----")
for producto in inventario:
    for clave,valor in producto.items():
        print(f"{clave} : {valor}")
    print("---------")