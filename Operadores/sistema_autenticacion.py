<<<<<<< HEAD
print("++++Sistema de autenticación++++")
USUARIO="ZUNNY"
PASSWORD=12345

#Pedir los datos
usuario = print("Ingrese el usuario: ")
password = int(input("Ingrese el pin: "))

resultado = usuario.strip() == USUARIO and password == PASSWORD

=======
print("++++Sistema de autenticación++++")
USUARIO="ZUNNY"
PASSWORD=12345

#Pedir los datos
usuario = print("Ingrese el usuario: ")
password = int(input("Ingrese el pin: "))

resultado = usuario.strip() == USUARIO and password == PASSWORD

>>>>>>> 3a5a0ee2db19353d60567e72d2f2d61db3241772
print(f"Puede ingresar al sistema: {resultado}")