def mostrar_menu():
    print('''Operaciones disponibles
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')

def pedir_numero(mensaje):
    validacion=False
    while not validacion:
        valor = input(mensaje)
        validacion,valor = validar_valor(valor)
    return valor

def validar_valor(numero):
    try:
        numero=float(numero)
        return True,numero
    except:
        print('Número no válido')
        return False,None
def obtener_numeros():
    num1= pedir_numero('Ingrese el número 1: ')
    num2= pedir_numero('Ingrese el número 2: ')
    return num1,num2
def sumar (*args):
    total = 0
    for numero in args:
        total += numero
    print(f'La Suma es: {total}')
def restar (num1,num2):
    total = num1-num2
    print(f'La Resta es: {total}')
def mult (num1,num2):
    total = num1*num2
    print(f'La Multiplicación es: {total}')
def div (num1,num2):
    if not num2 == 0:
        total = num1/num2
        print(f'La División es: {total}')
    else:
        print('error de calculo (0)')