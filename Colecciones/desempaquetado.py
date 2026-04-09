print(" +++ Desempaquetado de tuplas  +++")

producto = ("P001","Camisa",20.00)
print(f"Tupla completa: {producto}")
#Unpacking
id,descripcion,precio = producto
print(f"ID: {id}\ndescripcion: {descripcion}\nprecio: {precio}")