# Crear un programa que ingrese un password y checar que sea vaálido

strng = ""
val = True
es_mayus = False
tiene_num = False
tiene_signo = False
cantidad_num = 0
while val:
    strng = input("Ingrese la contraseña:\n6 caracteres\n1 Mayus\n3 num.\n1 signo\n: ")
    if len(strng) >=6:
        for char in strng:
            if char.isupper():
                es_mayus = True
            if char.isdigit():
                cantidad_num += 1
            if cantidad_num == 3:
                 tiene_num = True
            if not char.isalnum():
                tiene_signo =True

        if not es_mayus:
            print("Debe tener una mayúscula.")
        if not tiene_num or cantidad_num < 3:
            print("Debe tener 3 numeros.")
        if not tiene_signo:
            print("Debe tener un signo.")
        if es_mayus and tiene_signo and tiene_num and cantidad_num>=3:
            print("Contraseña correcta.")
            val =True
    else:
        print("Debe tener mas de 6 caracteres")
