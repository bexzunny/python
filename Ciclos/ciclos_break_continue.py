print("Break y Continue")

#Ejemplo con break
print("\t Break")
for numero in range(1,10):
    if numero % 2 ==0: #Numero par
        print(numero)
        break #Salimos del ciclo inmediatamente

# Ejemplo con Continue
print("\t Continue")
for numero in range(1,10):
    if numero % 2 ==1: #Numero impar
        continue
        #No ejecuta todo lo demás de abajo del código
        #Se vá a la siguiente iteración
    print(numero)