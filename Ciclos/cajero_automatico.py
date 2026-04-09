#Programa: realizar un cajero automático
print("Aplicación de cajero automático")

def validar (mensaje):
    #Repetir el código hasta que retorne
    while True:
        numero = input(mensaje)
        try:
            # Convertir a flotante, en caso de ser incorrecto exception
            numero = float(numero)
            #Devolver el valor si es numero y si es mayor a 0
            return numero if numero > 0 else print("Debe ingresar un numreo positivo")
        except:
            print("Ingresa un número válido")

#Declarar variable de control del ciclo
salir=True


#Declarar el saldo inicial
saldo = 1000
while salir:

    #Imprimir datos
    print("""Operaciones a realizar:
    1. Consulta de saldo
    2. Retirar
    3. Depositar
    4. Salir""")
    # Validar que opcion sea un número
    opcion = validar("Escoja una opcion: ")

    if opcion == 1:
        print(f"Su saldo es de: ${saldo}")
    elif opcion == 2:
        retiro = validar("Ingrese el monto a retirar: ")
        if retiro <= saldo:
            saldo  = saldo - retiro
            print(f"Saldo restante: ${saldo}")
        else:
            print("No tienes tanto dinero")

    elif opcion == 3:
        deposito = validar("Ingrese el monto a depositar: ")
        saldo = saldo +deposito
        print(f"Saldo actual: ${saldo}")
    elif opcion == 4:
        print("Saliendo...")
        salir = False
    else:
        print("Operación no reconocida")

