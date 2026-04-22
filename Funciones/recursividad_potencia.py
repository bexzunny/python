print('---- Potencia de un número con recursividad ----')
def potenciar(ba,po):
    if po==1:
        return ba
    else:
        return ba * potenciar(ba,po-1)
base = int(input('Ingrese el número de la base: '))
potencia = int(input('Ingrese la potencia: '))

print(f'El numero {base} elevado a {potencia} es: {potenciar(base,potencia)}')