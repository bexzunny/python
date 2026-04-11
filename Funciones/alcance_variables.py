print('---- Alcance de variables ----')

# Variable global
contador_global = 0

def incrementar_contador():
    # Declaramos una variable local
    contador_local = 0

    # Usar la variable global
    global contador_global

    # Invrementar la variable global
    contador_global += 1

    # Incrementar la variable local
    contador_local +=1
    print(f'Contador local: {contador_local}')
    print(f"Contador global: {contador_global}\n")

# Llamamos varias veces la función
incrementar_contador()
incrementar_contador()
incrementar_contador()

# Terminando el programa
print(f'Contador global :{contador_global}')