<<<<<<< HEAD
print("++++Tienda en linea++++")
# Se añade la constante dl monto minimo
MONTO_MINIMO = 1000
#Se piden los datos
monto_compra = int(input("Ingrese el monto total de la compra: "))
es_miembro = input("Es miembro de la tienda (si/no): ")

if monto_compra>=MONTO_MINIMO and es_miembro.strip().lower() == "si":
    descuento = 0.10
elif es_miembro.strip().lower() == "si":
    descuento = 0.05
elif monto_compra >= MONTO_MINIMO:
    descuento = 0.3
else:
    descuento = 0

descuento_aplicado = monto_compra*descuento
total = monto_compra - descuento_aplicado

print(f"""El total de descuento adquirido: {descuento*100}%
Valor de descuento: {descuento_aplicado}
total: {total}""")
=======
print("++++Tienda en linea++++")
# Se añade la constante dl monto minimo
MONTO_MINIMO = 1000
#Se piden los datos
monto_compra = int(input("Ingrese el monto total de la compra: "))
es_miembro = input("Es miembro de la tienda (si/no): ")

if monto_compra>=MONTO_MINIMO and es_miembro.strip().lower() == "si":
    descuento = 0.10
elif es_miembro.strip().lower() == "si":
    descuento = 0.05
elif monto_compra >= MONTO_MINIMO:
    descuento = 0.3
else:
    descuento = 0

descuento_aplicado = monto_compra*descuento
total = monto_compra - descuento_aplicado

print(f"""El total de descuento adquirido: {descuento*100}%
Valor de descuento: {descuento_aplicado}
total: {total}""")
>>>>>>> 3a5a0ee2db19353d60567e72d2f2d61db3241772
