print("++++ Repetición de un mensaje ++++")

mensaje = input("Ingresa un mensaje a repetir: ")
no_repeticiones = int(input("Ingrese la cantidad de veces a repetir el mesnaje: "))

#Iterar sonre el rango de repeticiones
for _ in range(no_repeticiones):
    print(mensaje)