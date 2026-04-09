print("+++ Combinación de listas y tuplas +++")

# Definir una lista que almacena tuplas de productos
productos =[
    ('P001','Camiseta',20.00),
    ('P002','Jeans',30.00),
    ('P003','Sudadera',40.00)
]
# Imprimir la información de cada producto
# Y calcular el precio total

precio_total = 0

print('Información de los productos')
for tupla in productos:
    #print(tupla)
    id,descripcion,precio=tupla #Unpacking
    print(f"Producto: ID: {id}\tdecripción: {descripcion}\tprecio: ${precio}")
    precio_total += precio #Tupla[2]
print(f"El precio total es:{precio_total }")