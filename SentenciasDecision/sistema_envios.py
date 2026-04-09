# Sistema de envios indicando el destino, nacional o internacional y el peso del paquete

PRECIO_TARIFA_INTERNACIONAL = 20
PRECIO_TARIFA_NACIONAL = 10

nombre_destino = ""
destino = int(input("Ingrese el destino \n1: Nacional\n2: Internacional\n :"))
peso = int(input("Ingrese el peso del paquete (kg): "))

if destino == 1:
    tarifa = PRECIO_TARIFA_NACIONAL
    total = tarifa * peso
    nombre_destino = "Nacional"
elif destino == 2:
    tarifa = PRECIO_TARIFA_NACIONAL
    total = tarifa * peso
    nombre_destino = "Internacional"
else:
    print("Destino no localizado.")


print("----Detalles del envío----")
print(f"""destino: {nombre_destino}
Tarifa: {tarifa}
Peso del paquete : {peso}
Total: {total}""")
