<<<<<<< HEAD
# Programa :Sistema de autenticación

USUARIO = "Zunny"
PASSWORD = 2007

usuario = input("Ingrese el usuario: ")
password = int(input("Ingrese el PIN: "))

validar_usuario = True if usuario == USUARIO else False
validar_password = True if password == PASSWORD else False

if validar_usuario and validar_password:
    print(f"Bienvenido al sistema: {usuario}")
elif not validar_usuario:
    print(f"Usuario inválido.")
elif not validar_password:
    print("Password incorrecta.")
else:
=======
# Programa :Sistema de autenticación

USUARIO = "Zunny"
PASSWORD = 2007

usuario = input("Ingrese el usuario: ")
password = int(input("Ingrese el PIN: "))

validar_usuario = True if usuario == USUARIO else False
validar_password = True if password == PASSWORD else False

if validar_usuario and validar_password:
    print(f"Bienvenido al sistema: {usuario}")
elif not validar_usuario:
    print(f"Usuario inválido.")
elif not validar_password:
    print("Password incorrecta.")
else:
>>>>>>> 3a5a0ee2db19353d60567e72d2f2d61db3241772
    print("Usuario y password inválidos.")