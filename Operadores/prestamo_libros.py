<<<<<<< HEAD
print("++++Sistema de prestamo----")

DISTANCIA_MAX=3 #km
tiene_credencial = input("Tiene credencial? (si/no): ")
distancia_casa = int(input("A cuantos kilometros vive de la biblioteca: "))
resultado = tiene_credencial.strip().lower() == "si" or distancia_casa<=DISTANCIA_MAX
=======
print("++++Sistema de prestamo----")

DISTANCIA_MAX=3 #km
tiene_credencial = input("Tiene credencial? (si/no): ")
distancia_casa = int(input("A cuantos kilometros vive de la biblioteca: "))
resultado = tiene_credencial.strip().lower() == "si" or distancia_casa<=DISTANCIA_MAX
>>>>>>> 3a5a0ee2db19353d60567e72d2f2d61db3241772
print(f"Puede tomar libros prestados?: {resultado}")