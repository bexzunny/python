print('Operadores de asignación')
numero = 5
print(f"Valor del número: {numero}")
numero = 10
print(f"Valor del número: {numero}")
cadena = 'Saludos desde python'
print(f"Valor de la cadena: {cadena}")

# Asignación multiple
x, y, z = 5, 'hola', -9.15
print(f"El valor de \nx: {x}\ty: {y}\tz: {z}")

# Asignación encadenada
a = b = c = 10
print(f"El valor de \na: {a}\tb: {b}\tc: {c}")

# Intercambio de valores de variables sin variable temporal
x, y = 5, 10
print(f"Valores iniciales: x:{x}\ty:{y}")
# Aplicando el concepto de asignación múltiple
x, y = y, x
print(f"Intercambio de valores: x:{x}\ty:{y}")

# Recibir multiples valores
nombre, apellido = input("Ingresa tu nombre y apellido separados por ,: ").split(",")
print(f"Nombre: {nombre.strip()}\t Apellido: {apellido.strip()}")