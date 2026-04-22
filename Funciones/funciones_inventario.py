def mostrar_menu():
    print("""    1. Mostrar Inventario
    2. Agregar producto
    3. Buscar producto ID
    4. Salir""")


def pedir_valor(mensaje,tipo):
    validacion=False
    while not validacion:
        valor= input(mensaje)
        if tipo == 1:
            validacion,valor = validar_valor(valor)
        else:
            validacion,valor = validar_valor_float(valor)
    return valor

def validar_valor(numero):
    try:
        numero=int(numero)
        return True,numero
    except:
        print('Número no válido')
        return False,None

def validar_valor_float(numero):
    try:
        numero=float(numero)
        return True,numero
    except:
        print('Número no válido')
        return False,None

def mostrar_inv(inventario):
    for producto in inventario:
        for clave,valor in producto.items():
            print(f'{clave}: {valor}')
        print("-----------")

def agregar_producto(ide):
    print(f'ID: {ide+1}')
    nombre= input("Nombre: ")
    precio = pedir_valor("Ingrese el precio: $",2)
    cantidad = pedir_valor("INgrese la cantidad: ",1)
    producto = {
        'id': ide+1,
        'nombre':nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    return producto

def buscar_producto(inventario,ide):
    for producto in inventario:
        if ide == producto['ID']:
            imprimir_producto(producto)

def imprimir_producto(producto):
    print("-------------")
    for clave, valor in producto.items():
        print(f'{clave}: {valor}')
    print('--------------')