<<<<<<< HEAD
print("Bienvenido a Zunny")
NO_PRODUCTOS_DESCUENTO=10
articulos_comprados = input("Ingrese los articulos que ha comprado: ")
membresia = input("Cuenta con la membresía (si/no): ")

es_vip = (articulos_comprados>=NO_PRODUCTOS_DESCUENTO and membresia.strip().lower()=="si")

=======
print("Bienvenido a Zunny")
NO_PRODUCTOS_DESCUENTO=10
articulos_comprados = input("Ingrese los articulos que ha comprado: ")
membresia = input("Cuenta con la membresía (si/no): ")

es_vip = (articulos_comprados>=NO_PRODUCTOS_DESCUENTO and membresia.strip().lower()=="si")

>>>>>>> 3a5a0ee2db19353d60567e72d2f2d61db3241772
print(f"Tiene acceso al sistema VIP?: {es_vip}")