print('---- Factorial con recursividad')

def factorial(numero):
    if numero == 0 or numero == 1:
        print(f'Resultado factorial parcial {numero} es: 1')
        return 1
    else:
        fact_parcial = numero * factorial(numero-1)
        print(f'Resultado factorial parcial {numero} es: {fact_parcial}')
        return fact_parcial
print(f'El factorial de 5 es: {factorial(5)}')