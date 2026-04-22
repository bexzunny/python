print('---- Calculadora de impuesto ----')

# Métodos
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

def calcular_impuesto(pago_sin,impuesto):
    return pago_sin+(pago_sin*(impuesto/100))

pago = pedir_numero('Proporcione el pago sin impuesto: ')
impuesto = pedir_numero('proporcione el monto del impuesto: ')
print (f'Pago con impuesto: {calcular_impuesto(pago,impuesto)}')