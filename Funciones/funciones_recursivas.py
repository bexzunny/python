print('---- Imprimir del 1 al 5 de forma recursiva ----')

# Definir la función recursiva
def fun_recursiva(numero):
    # Caso bse
    if numero==1:
        print(numero,end=' ') # 1 2 3 4 5
    else: # Caso recursivo
        fun_recursiva(numero-1)
        print(numero,end=' ')


fun_recursiva(5)