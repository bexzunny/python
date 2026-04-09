<<<<<<< HEAD
print("Ticket: ")

IMPUESTO = 0.16
precio_producto1 = float(input("Ingrese el precio de el producto 1: "))
precio_producto2 = float(input("Ingrese el precio de el producto 2: "))
precio_producto3 = float(input("Ingrese el precio de el producto 3: "))
precio_producto4 = float(input("Ingrese el precio de el producto 4: "))

descuento = int(input("Ingresa un descuento a realizar: "))
#Cálculo sin impuestos
subtotal = precio_producto1+precio_producto2+precio_producto3+precio_producto4

#Se calcula el descuento
descuento_porcentaje = (subtotal/100)*descuento
#
subtotal_descuento = subtotal-descuento_porcentaje
#Cálculo con impuestos
impuesto = subtotal_descuento*IMPUESTO

#Cálculo total de la ocmpra (sin impuestos)
total = subtotal_descuento+impuesto
print(f"""SUBTOTAL: ${subtotal:.2f}
Descuento aplicado del {descuento}%: {subtotal_descuento}
Impuesto (16%): ${impuesto:.2f}
TOTAL:\t${total:.2f}
""")
=======
print("Ticket: ")

IMPUESTO = 0.16
precio_producto1 = float(input("Ingrese el precio de el producto 1: "))
precio_producto2 = float(input("Ingrese el precio de el producto 2: "))
precio_producto3 = float(input("Ingrese el precio de el producto 3: "))
precio_producto4 = float(input("Ingrese el precio de el producto 4: "))

descuento = int(input("Ingresa un descuento a realizar: "))
#Cálculo sin impuestos
subtotal = precio_producto1+precio_producto2+precio_producto3+precio_producto4

#Se calcula el descuento
descuento_porcentaje = (subtotal/100)*descuento
#
subtotal_descuento = subtotal-descuento_porcentaje
#Cálculo con impuestos
impuesto = subtotal_descuento*IMPUESTO

#Cálculo total de la ocmpra (sin impuestos)
total = subtotal_descuento+impuesto
print(f"""SUBTOTAL: ${subtotal:.2f}
Descuento aplicado del {descuento}%: {subtotal_descuento}
Impuesto (16%): ${impuesto:.2f}
TOTAL:\t${total:.2f}
""")
>>>>>>> 3a5a0ee2db19353d60567e72d2f2d61db3241772
