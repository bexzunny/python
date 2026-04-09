#Programa crear una calculadora
def ingresar_validar(mensaje):
    while True:
        numero = input(mensaje)
        try:
            numero = float(numero)
            return numero
        except:
            print("Ingrese un numero válido")


def pedir_numeros():
    no1 = ingresar_validar("Ingresa el número 1: ")
    no2 = ingresar_validar("Ingresa el número 2: ")
    return no1, no2


print("++++Calculaora de python++++")
no1=""
no2=""
salir = True
while salir:
    print("""Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir""")
    opcion = ingresar_validar("Ingrese la opción: ")
    match opcion:
        case 1:
            no1, no2 = pedir_numeros()
            total = no1 + no2
            print(f"el resultado de {no1} + {no2} = {total}")
        case 2:
            no1, no2 = pedir_numeros()
            total = no1 - no2
            print(f"el resultado de {no1} - {no2} = {total}")
        case 3:
            no1, no2 = pedir_numeros()
            total = no1 * no2
            print(f"el resultado de {no1} * {no2} = {total}")
        case 4:
            no1, no2 = pedir_numeros()
            if no2 == 0:
                print("Lo sentimos, no se puede dividir entre 0")
            else:
                total = no1 / no2
                print(f"el resultado de {no1} / {no2} = {total}")
        case 5:
            salir = False
        case _:
            print("Ingrese un número válido")
