print("++++ Sistema de administración de cuentas ++++")

opcion = 0
while opcion!=3:
    print("MENU")
    print("""\t\t1. Crear cuenta
    \t2. Eliminar cuenta
    \t3. salir""")
    opcion = int(input("Escoja una opcion: "))
    if opcion == 1:
        print("Creando cuenta...")
    elif opcion == 2:
        print("Eliminando cuenta...")
    elif opcion == 3:
        print("Saliendo del programa...")
    else:
        print("Opcion no válida")

