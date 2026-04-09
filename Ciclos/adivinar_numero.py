# Programa: adivinar un numeor con pustas
# Importar sólo randint
from random import randint

#Inicializar variables
reintentar ="si"
es_correcto = False
intentos = 0
respuesta = 0
#Crear los métodos para ingreso y validación del número
def validacion(numero):
    if numero.isdigit():
        es_valido = True
        return es_valido

def ingreso():
    es_valido = False
    while not es_valido:
        respuesta = input("Ingrese su número: ")
        es_valido = validacion(respuesta)
    return int(respuesta)
print("¡¡¡Adivina el número!!!")

#Iniciar el ciclo de nuevos intentos
while reintentar.lower().strip()=="si":
    #Crear el número a adivinar
    numero = randint(1,51)
    while not es_correcto and intentos<10:
        intentos += 1
        respuesta = ingreso()
        if respuesta > numero:
            print(f"Tu número es mayor...\nIntentos restantes: {10-intentos}\n")
        elif respuesta < numero:
            print(f"Tu número es menor...\nIntentos restantes: {10-intentos}\n")
        if intentos>=10:
            print(f"Te quedan mas intentos, el numero era: \n{numero}")
        if respuesta==numero:
            es_correcto = True
            print(f"\tFELICIDADES\nAdivinaste el número: {numero}\n")
    reintentar = input("Quieres juagr de nuevo?: ")

