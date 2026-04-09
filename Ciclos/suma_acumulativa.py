print("++++ Suma acumulativa ++++")

# Sumar los primeros 5 numeros
MAXIMO = 5
numero = 1
acumulador_suma = 0

#Iterar
while numero <= MAXIMO:
    #Imprimir lo que se va a sumar
    print(f"acumulador_suma + numero = {acumulador_suma} + {numero}")
    acumulador_suma+=numero
    numero+=1
    #Imprimir el resultado de la suma parcial
    print(f"Suma parcial acumulada: {acumulador_suma}\n")
print(f"\nLa suma total del 1-5 es: {acumulador_suma}")