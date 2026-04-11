print('---- Funcion par ----')
# Función para saber si un número es par o impar
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Llamamos a la función
if __name__ == '__main__':
    numero = int(input("Proporciona un valor numérico: "))
    print(f'Numero par?: {es_par(numero)}')