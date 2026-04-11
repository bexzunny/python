print('---- Imprimir detalles de una persona usando kwargs ----')

# Función que acepte argumentos variables en forma de llave-valor
def imprimir_detalle(**kwargs):
    print(f'\n Valores recibidos:')
    for llave,valor in kwargs.items():
        print(f'{llave} : {valor}')

# Llamamos a la función
imprimir_detalle(nombre = 'Adair', edad = 18, ciudad = 'México')
imprimir_detalle()
imprimir_detalle(nombre = 'Luisa', edad = 20, ciudad = 'México',puesto = 'Gerente')