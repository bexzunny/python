print("Bienvenido a Zunny")
NO_PRODUCTOS_DESCUENTO=10
articulos_comprados = input("Ingrese los articulos que ha comprado: ")
membresia = input("Cuenta con la membresía (si/no): ")

es_vip = (articulos_comprados>=NO_PRODUCTOS_DESCUENTO and membresia.strip().lower()=="si")

print(f"Tiene acceso al sistema VIP?: {es_vip}")