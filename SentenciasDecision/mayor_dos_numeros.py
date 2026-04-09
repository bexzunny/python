# Pedir el mayor de dos números e imprimir el mayor

no_1 = int(input("Ingrese el número 1:"))
no_2 = int(input("Ingrese el número 2:"))

if no_1 > no_2:
    print(f"El número mayor es: {no_1}")
elif no_2 > no_1:
    print(f"El número mayor es: {no_2}")
else:
    print(f"Son números iguales")