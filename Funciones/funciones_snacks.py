# Variables (contadores)
pr_comprados = []
def mostrar_menu():
    print("""Menú:
    1. Mostrar Snacks
    2. Comprar Snack
    3. Mostrar Ticket
    4. Salir""")

def pedir_valor(mensaje):
    validacion=False
    while not validacion:
        valor = input(mensaje)
        validacion,valor = validar_valor(valor)
    return valor
def validar_valor(numero):
    try:
        numero=int(numero)
        return True,numero
    except:
        print('Número no válido')
        return False,None
def mostrar_snacks(snacks):
    print("----Snacks disponibles----")
    for snack in snacks:
        print(f'ID: {snack['id']} -> {snack['nombre']} - ${snack['precio']}')

def comprar_snack(snacks, snack):
    existe_snack = False
    dicc = {}
    global pr_comprados
    existe_snack = buscar_snack(snacks,snack)
    if existe_snack:
        dicc = obtener_dicc(snacks,snack)
        pr_comprados.append(dicc)
        print("Snack comprado")
    else:
        print("Snack no existente...")

def buscar_snack(snacks,snack):
    for item in snacks:
        if snack == item['id']:
            return True

def obtener_dicc(snacks,snack):
    for item in snacks:
        if snack == item['id']:
            return item

def mostrar_ticket():
    print("----Snacks comprados----")
    global pr_comprados
    for snack in pr_comprados:
        print(f'ID: {snack['id']} -> {snack['nombre']} - ${snack['precio']}')
