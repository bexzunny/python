<<<<<<< HEAD
# Programa: Generar email con nombre, apellidos, nombre de la empresa, y extensión

# Pedir los nombres
nombre = input("Ingrese su nombre: ")
# Pedir los apellidos
apellidos = input("Ingrese sus apellidos: ")

#Pedir datos de empresa
empresa = input("Ingrese el nombre de la empresa: ")
# Pedir el dominio web
dominio = input("Ingrese la extensión del dominio: ")

email = (f"{nombre.replace(" ",".").lower()}"
         f"."
         f"{apellidos.replace(" ", ".").lower()}"
         f"@"
         f"{empresa.replace(" ","").lower()}"
         f"{dominio}")
=======
# Programa: Generar email con nombre, apellidos, nombre de la empresa, y extensión

# Pedir los nombres
nombre = input("Ingrese su nombre: ")
# Pedir los apellidos
apellidos = input("Ingrese sus apellidos: ")

#Pedir datos de empresa
empresa = input("Ingrese el nombre de la empresa: ")
# Pedir el dominio web
dominio = input("Ingrese la extensión del dominio: ")

email = (f"{nombre.replace(" ",".").lower()}"
         f"."
         f"{apellidos.replace(" ", ".").lower()}"
         f"@"
         f"{empresa.replace(" ","").lower()}"
         f"{dominio}")
>>>>>>> 3a5a0ee2db19353d60567e72d2f2d61db3241772
print(f"Su generación del email es: \n\t{email}")