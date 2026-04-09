print("++++Sistema de autenticación++++")
USUARIO="ZUNNY"
PASSWORD=12345

#Pedir los datos
usuario = print("Ingrese el usuario: ")
password = int(input("Ingrese el pin: "))

resultado = usuario.strip() == USUARIO and password == PASSWORD

print(f"Puede ingresar al sistema: {resultado}")